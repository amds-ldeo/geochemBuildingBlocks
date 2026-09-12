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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp", nargs="?")
    ap.add_argument("--all", action="store_true",
                    help="the released TAPPs -- those TAPP_CONFIGS sources from the "
                         "delivery, not the repo-local drafts")
    ap.add_argument("--write", action="store_true", help=f"emit into {os.path.relpath(OUTDIR, ROOT)}")
    ap.add_argument("--drafts", action="store_true", help="with --all, include the drafts too")
    a = ap.parse_args()

    reg = load_registry()
    term_techs = term_technique_index(reg)
    counts = collections.Counter(t for t, _, _ in reg.values() if t)

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
