#!/usr/bin/env python3
"""Build the ada:vocabulary block a TAPP instance carries, from the registry.

A TAPP instance today names its controlled values as bare strings. Nothing in the record
says which scheme a value came from or what it means, and the annotation that was meant to
carry that -- schema:inDefinedTermSet: "ada:vocab/<tapp>/<field>" -- points at IRIs that do
not resolve. This embeds the vocabulary instead, so a registered procedure is readable
without a resolver, which is what a DOI'd record needs.

**The registry stays authoritative.** This is a materialised view, the same relationship
resolvedSchema.json has to schema.yaml: generated, never hand-edited, and safe to delete
and rebuild. Nothing here is a second source of truth.

Four decisions it implements (2026-09-12):

  1. the block is embedded in the INSTANCE; the tappSchema constrains its shape, not its
     values
  2. a term a technique invents lives in that technique's local namespace
  3. scheme IRIs derive from a stable scheme name -- NOT the field name, which moves:
     analyteEstimationMethod became targetSpeciesEstimationMethod on 2026-09-01, and a
     minted URI must survive that. Until the registry assigns stable names this slugs the
     field name as a PLACEHOLDER; see --check-stability.
  4. a concept IRI binds to the TERM STRING, so one term has one IRI wherever it appears.
     Measured across the registry: 1,631 of 1,687 terms occur in exactly one field, so this
     matches scheme-scoping for 96.7% of them, and for the recurring remainder -- LIF, SDD,
     Hough transform -- one IRI is the right answer rather than a compromise.

Shared versus local is decided by evidence: a term more than one technique uses is shared;
one only this technique uses is local.

**Definitions.** Concepts carry skos:definition when the registry has one, and today it
almost never does -- 1,206 of 3,491 concepts are defined and all but one of those are
FIELDS (from adaAnalyticalParameters), not allowed VALUES. Adding definitions to the
registry is what makes these IRIs worth resolving. Note the hazard before doing it by hand:
_tapp_lib overwrites any codelist whose $id it owns, so a definition typed into
empa_beamMode.json is destroyed by the next regenerate. Definitions need a source that
survives regeneration -- the schemapaths sidecar is the pattern this repo already uses for
exactly that.

    python tools/build_ada_vocabulary.py empaTAPP
    python tools/build_ada_vocabulary.py --all
    python tools/build_ada_vocabulary.py --all --write   # emit build/vocabulary/<tapp>.json
    python tools/build_ada_vocabulary.py --check-stability  # what blocks minting; exit 1 if unsafe
"""
import argparse
import collections
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab")
OUTDIR = os.path.join(ROOT, "build", "vocabulary")

# Decision 3. Versioned, and `tapp` rather than `tappregistry` to match the single-word
# segments already registered under /geochem (analyticalmethod, agent). One constant: if
# the w3id registration lands differently this is the only line to change.
BASE = "https://w3id.org/geochem/1.0/tapp"

# Not concepts: the absence of a value rather than one of them. vocab_obj already drops the
# first three; Unknown/Other/Yes/No recur across more fields than any real term and behave
# the same way, so they are treated alike rather than minted twenty times over.
SENTINELS = {"n/a", "none", "missing", "unknown", "other", "yes", "no",
             "not applicable", "not reported"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load_registry():
    """{stem: (tapp, field, scheme)} for every codelist that has concepts."""
    out = {}
    for p in sorted(glob.glob(os.path.join(VOCAB, "*.json"))):
        try:
            j = json.load(io.open(p, encoding="utf-8"))
        except Exception:
            continue
        if not j.get("skos:hasTopConcept"):
            continue
        sid = (j.get("@id") or "").replace("ada:vocab/", "")
        if "/" in sid:
            tapp, field = sid.split("/", 1)
        else:
            tapp, field = None, sid
        out[os.path.basename(p)[:-5]] = (tapp, field, j)
    return out


def term_technique_index(reg):
    """{notation: {tapp, ...}} -- how many techniques use each term."""
    idx = collections.defaultdict(set)
    for _, (tapp, _, j) in reg.items():
        for c in j["skos:hasTopConcept"]:
            n = (c.get("skos:notation") or "").strip()
            if n and n.lower() not in SENTINELS:
                idx[n].add(tapp or "_shared")
    return idx


def build(tapp, reg, term_techs):
    mine = {s: v for s, v in reg.items() if v[0] == tapp}
    schemes, concepts = [], {}
    stats = collections.Counter()
    local_ns = f"{BASE}/{slug(tapp.replace('TAPP', ''))}/term"
    for _, (_, field, j) in sorted(mine.items(), key=lambda kv: kv[1][1]):
        scheme_iri = f"{BASE}/scheme/{slug(field)}"
        members = []
        for c in j["skos:hasTopConcept"]:
            n = (c.get("skos:notation") or "").strip()
            if not n:
                continue
            if n.lower() in SENTINELS:
                stats["sentinel"] += 1
                continue
            shared = len(term_techs[n]) > 1
            iri = f"{BASE}/term/{slug(n)}" if shared else f"{local_ns}/{slug(n)}"
            stats["shared" if shared else "local"] += 1
            if iri not in concepts:
                concepts[iri] = {
                    "@id": iri,
                    "@type": ["skos:Concept"],
                    "skos:prefLabel": c.get("skos:prefLabel") or n,
                    "skos:notation": n,
                    "skos:inScheme": [],
                }
                if c.get("skos:definition"):
                    concepts[iri]["skos:definition"] = c["skos:definition"]
                    stats["defined"] += 1
            ref = {"@id": scheme_iri}
            if ref not in concepts[iri]["skos:inScheme"]:
                concepts[iri]["skos:inScheme"].append(ref)
            members.append({"@id": iri})
        schemes.append({
            "@id": scheme_iri,
            "@type": ["skos:ConceptScheme"],
            "skos:prefLabel": field,
            "skos:definition": j.get("skos:definition"),
            "schema:dateModified": j.get("schema:dateModified"),
            "skos:hasTopConcept": members,
        })
    block = {
        "@context": {
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
        },
        "ada:vocabulary": {
            "@type": ["ada:VocabularySnapshot"],
            "schema:isBasedOn": {"@id": BASE},
            "ada:conceptScheme": schemes,
            "ada:concept": list(concepts.values()),
        },
    }
    return block, stats


def notations(j):
    """The real terms in a codelist -- sentinels are absences, not concepts."""
    return frozenset(n for n in ((c.get("skos:notation") or "").strip()
                                 for c in j["skos:hasTopConcept"])
                     if n and n.lower() not in SENTINELS)


def check_stability(reg, term_techs):
    """What has to be settled before an IRI is minted.

    Every segment this tool mints slugs something mutable, and a permanent identifier
    cannot track a mutable thing. Reports each case, separating what is already wrong
    in the output from what is a decision waiting to be taken. Returns the blocking
    count so the tool exits non-zero while minting is unsafe.
    """
    try:            # terms carry non-ASCII (the zeta-factor labels); cp1252 would abort
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    blocking = 0

    # 1. A scheme IRI is {BASE}/scheme/{slug(field)} with no technique segment, so two
    #    techniques naming a field alike mint ONE scheme IRI. Fine where they agree on
    #    members; a defect where they do not, because the IRI then denotes a different
    #    scheme depending on which record you read it from.
    members = collections.defaultdict(dict)
    for _, (tapp, field, j) in reg.items():
        members[slug(field)][tapp] = notations(j)
    shared = {s: d for s, d in members.items() if len(d) > 1}
    diverge = {s: d for s, d in shared.items() if len(set(d.values())) > 1}
    print("1. scheme IRIs, minted from the field name")
    print(f"   {len(members)} distinct scheme slugs; {len(shared)} minted by more than one "
          f"technique, of which {len(shared) - len(diverge)} agree on members")
    if diverge:
        print(f"   BLOCKING -- {len(diverge)} slug(s) name a DIFFERENT scheme per technique.")
        print("   Grouped by member set: each group is one scheme, and they share one IRI.")
        for sl, d in sorted(diverge.items(), key=lambda kv: -len(set(kv[1].values()))):
            groups = collections.defaultdict(list)
            for t, v in d.items():
                groups[v].append(t)
            common = set.intersection(*map(set, d.values()))
            print(f"     /scheme/{sl}  --  {len(groups)} distinct member sets across "
                  f"{len(d)} techniques, {len(common)} term(s) common to all")
            for v, ts in sorted(groups.items(), key=lambda kv: -len(kv[1])):
                who = ", ".join(sorted(ts)[:3]) + (f" +{len(ts) - 3} more" if len(ts) > 3 else "")
                only = sorted(set(v) - common)
                tail = "  e.g. " + "; ".join(only[:2]) if only else ""
                print(f"       {len(v):>3d} terms  [{len(ts):>2d}] {who}{tail}")
        blocking += len(diverge)

    # 2. A concept IRI is slug(term), so the IRI encodes the label and the label can
    #    then never be corrected. Collisions are the readable symptom; mutability is
    #    the real hazard, and no check can see a rename that has not happened yet.
    by_slug = collections.defaultdict(set)
    for _, (_, _, j) in reg.items():
        for n in notations(j):
            by_slug[slug(n)].add(n)
    coll = {s: v for s, v in by_slug.items() if len(v) > 1}
    print()
    print("2. term IRIs, minted from the label")
    print(f"   {sum(len(v) for v in by_slug.values())} distinct terms -> {len(by_slug)} slugs")
    if coll:
        print(f"   REVIEW -- {len(coll)} slug(s) reached by more than one term; merging is "
              f"right only where they mean the same thing:")
        for sl, v in sorted(coll.items()):
            print(f"     /term/{sl} <- " + " | ".join(sorted(v)))

    # 3. Shared-vs-local is recomputed from the current data on every run, so a local
    #    term's IRI leaves its technique namespace the day a second technique adopts
    #    it, orphaning every record already carrying the old one.
    local = [n for n, t in term_techs.items() if len(t) == 1 and "_shared" not in t]
    edge = [n for n, t in term_techs.items() if len(t) == 2]
    print()
    print("3. the shared/local split, recomputed on every run")
    print(f"   REVIEW -- {len(local)} term(s) are technique-local today; each one's IRI "
          f"changes if a second technique adopts it")
    print(f"   {len(edge)} term(s) sit at exactly two techniques, one drop from the "
          f"reverse move")

    # 4. Decision 4 gives a term one IRI, hence one definition. Correct for a crystal
    #    like LIF, wrong for a word like Linear that two fields may use differently.
    by_field = collections.defaultdict(set)
    for _, (_, field, j) in reg.items():
        for n in notations(j):
            by_field[n].add(field)
    rec = sorted(((len(f), n) for n, f in by_field.items() if len(f) > 1), reverse=True)
    print()
    print("4. one term, one IRI, one definition")
    print(f"   REVIEW -- {len(rec)} of {len(by_field)} terms recur across fields; each needs "
          f"a definition that fits every field it appears in:")
    for c, n in rec:
        print(f"     {c}x  {n}")

    print()
    if blocking:
        print(f"BLOCKING: {blocking} scheme IRI(s) denote more than one scheme. Do not mint.")
    else:
        print("No blocking defect. The REVIEW sections are decisions, not errors.")
    return blocking


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp", nargs="?")
    ap.add_argument("--all", action="store_true",
                    help="the released TAPPs -- those TAPP_CONFIGS sources from the "
                         "delivery, not the repo-local drafts")
    ap.add_argument("--write", action="store_true", help=f"emit into {os.path.relpath(OUTDIR, ROOT)}")
    ap.add_argument("--drafts", action="store_true", help="with --all, include the drafts too")
    ap.add_argument("--check-stability", action="store_true",
                    help="report what blocks URI minting; exits non-zero if a minted "
                         "IRI is already ambiguous")
    a = ap.parse_args()

    reg = load_registry()
    term_techs = term_technique_index(reg)
    counts = collections.Counter(t for t, _, _ in reg.values() if t)

    if a.check_stability:
        print(f"registry: {len(reg)} codelists across {len(counts)} namespaces")
        print(f"base: {BASE}")
        print()
        return 1 if check_stability(reg, term_techs) else 0

    if a.all:
        # Which TAPPs are "the sixteen" is not a question the registry can answer -- a
        # scheme count is a proxy that silently drops SEM_FIBSEM and SEM_Imaging at 7
        # schemes each. TAPP_CONFIGS knows: a released TAPP reads its table from the
        # delivery, a draft reads one from draftTAPPs/ in this repo.
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import build_tapp as b
        released = {n for n, cfg in b.TAPP_CONFIGS.items()
                    if str(cfg.get("xlsx", "")).startswith("tapp/")}
        tapps = sorted(t for t in counts if a.drafts or t in released)
        missing = sorted(released - set(counts))
        if missing:
            print(f"note: {len(missing)} released TAPP(s) have no registry codelists: "
                  f"{', '.join(missing)}\n")
    elif a.tapp:
        tapps = [a.tapp]
    else:
        ap.error("give a TAPP name or --all")

    print(f"registry: {len(reg)} codelists across {len(counts)} namespaces")
    print(f"building: {len(tapps)} TAPP(s)\n")
    print(f"{'tapp':24s} {'schemes':>8s} {'concepts':>9s} {'shared':>7s} {'local':>6s} "
          f"{'defined':>8s} {'KB':>7s}")
    tot = collections.Counter()
    total_bytes = 0
    for t in tapps:
        block, st = build(t, reg, term_techs)
        blob = json.dumps(block, indent=2, ensure_ascii=False)
        total_bytes += len(blob.encode("utf-8"))
        v = block["ada:vocabulary"]
        print(f"{t:24s} {len(v['ada:conceptScheme']):>8d} {len(v['ada:concept']):>9d} "
              f"{st['shared']:>7d} {st['local']:>6d} {st['defined']:>8d} "
              f"{len(blob.encode('utf-8'))/1024:>7.1f}")
        for k, n in st.items():
            tot[k] += n
        tot["schemes"] += len(v["ada:conceptScheme"])
        tot["concepts"] += len(v["ada:concept"])
        if a.write:
            os.makedirs(OUTDIR, exist_ok=True)
            io.open(os.path.join(OUTDIR, f"{t}.json"), "w",
                    encoding="utf-8", newline="\n").write(blob)

    print(f"\naggregate: {tot['schemes']} schemes, {tot['concepts']} concept entries "
          f"({tot['shared']} shared refs, {tot['local']} local), "
          f"{tot['sentinel']} sentinels dropped")
    print(f"total embedded: {total_bytes/1024:.0f} KB across {len(tapps)} TAPPs "
          f"({total_bytes/1024/max(len(tapps),1):.1f} KB mean)")
    defined_pct = 100.0 * tot["defined"] / max(tot["concepts"], 1)
    print(f"concepts carrying a definition: {tot['defined']} ({defined_pct:.1f}%)"
          f"  <== the gap definitions in the registry would close")
    if a.write:
        print(f"wrote {len(tapps)} files to {os.path.relpath(OUTDIR, ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
