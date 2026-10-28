#!/usr/bin/env python3
"""Build the consolidated vocabulary catalog: ONE scheme per property, not per technique x property.

Until 2026-10-28 build_tapp.write_vocab() minted `ada:vocab/<TAPP>/<field>` once per consuming
technique, so a value list shared across techniques existed once per technique:
`samplePreparationMethod` 61 times, `samplingUnitType` 61, and 14 schemes whose entire content was
`Yes`/`No`. Stephen's ruling: one general vocabulary per property, with per-technique allowed-term
restrictions expressed in TAPP-specific SHACL (`sh:in`) rather than by partitioning the scheme.

The interoperability win falls out of collapsing the scheme @id, because `_tapp_lib.concept_obj`
already scopes a concept as `<scheme_id>/<slug(term)>`: "Polished section" becomes ONE IRI,
`ada:vocab/sample-preparation-method/polished-section`, wherever it appears.

WHY THIS IS A SHARED STAGE AND NOT PART OF THE PER-TECHNIQUE `tapp` STAGE

A property-scoped scheme is the UNION across techniques, which a single-technique run cannot see.
Accumulating into a shared file one technique at a time would make the output depend on invocation
order -- a `--tapp` spot regen would emit a partial scheme -- and a generator that varies by
invocation cannot be diffed, which forecloses `Regenerate and diff`. So this reads every delivery
in one pass: build_tapp.configure(t) + route() over all TAPP_CONFIGS entries. Deterministic by
construction, and no manifest needed.

IT DOES NOT TOUCH THE FOUR SCHEMES OTHER GENERATORS OWN

  componentType.json       apply_componentType_enums.py
  productType.json         apply_productType_enum.py
  adaInstrumentType.json           } build_instrument_codelist.py
  adaInstrumentComponentType.json  }

Those are already property-scoped, are not per-technique, and are referenced by
`schema:inDefinedTermSet` from 37, 27, 77 and 2 schema.yaml respectively. PROTECTED below.

    python tools/build_vocab_catalog.py            # report what it would do
    python tools/build_vocab_catalog.py --write
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _tapp_lib as _L            # noqa: E402
import build_tapp as bt           # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab")
SIDECAR = os.path.join(ROOT, "docs", "vocab_terms.json")

# Written by other generators; never read, rewritten or deleted here.
PROTECTED = {
    "componentType.json",
    "productType.json",
    "adaInstrumentType.json",
    "adaInstrumentComponentType.json",
}

# The slug rule lives in _tapp_lib.vocab_slug, NOT here: schema_path_emitter mints the
# schema:inDefinedTermSet references that point at these @ids, so the two must agree to the
# character. A reference that resolves nowhere looks like working wiring, and nothing but
# check_vocab_references.py would notice.
slugify = _L.vocab_slug


def load_sidecar():
    """Authored per-term decisions, keyed by property slug. See docs/vocab_terms.json."""
    if not os.path.exists(SIDECAR):
        return {}
    with open(SIDECAR, encoding="utf-8") as f:
        raw = json.load(f)
    return {k: v for k, v in raw.items() if not k.startswith("$")}


def collect():
    """{property: {"terms": {notation: [tapps]}, "labels": Counter, "descs": Counter}}.

    One pass over every delivery. route() is what the per-technique `tapp` stage uses, so the
    terms here are exactly the ones it would have emitted per technique.
    """
    props = collections.defaultdict(
        lambda: {"terms": collections.defaultdict(list),
                 "labels": collections.Counter(),
                 "descs": collections.Counter()})
    for tapp in sorted(bt.TAPP_CONFIGS):
        bt.configure(tapp)
        for entry in bt.route()["vocab"]:
            p = props[entry["name"]]
            if entry.get("item"):
                p["labels"][entry["item"]] += 1
            if entry.get("desc"):
                p["descs"][(entry["desc"] or "")[:300]] += 1
            for term in entry["terms"]:
                t = str(term)
                # One sentinel predicate for every vocabulary emitter, _tapp_lib's. This was
                # `t in ("N/A", "None") or _L.is_text_sentinel(t)`, which let "Unknown" through
                # and published it as an allowed term in 17 of 90 schemes while
                # build_ada_vocabulary dropped it. An absence is not one of the values.
                if _L.is_sentinel_value(t):
                    continue
                if tapp not in p["terms"][t]:
                    p["terms"][t].append(tapp)
    return props


def _pick(counter, fallback):
    """Most common, ties broken alphabetically. Deterministic, which run-order is not."""
    if not counter:
        return fallback
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


def build_scheme(prop, data, sidecar):
    """One consolidated skos:ConceptScheme for one property."""
    pslug = slugify(prop)
    scheme_id = "ada:vocab/" + pslug
    side = sidecar.get(pslug, {})
    slug_override = side.get("slug", {})
    alt = side.get("altLabel", {})
    broader = side.get("broader", {})

    # An alternate label is not itself a concept: it is folded onto the preferred one.
    folded = {v for vs in alt.values() for v in vs}

    concepts, slugs = [], {}
    for notation in sorted(data["terms"]):
        if notation in folded:
            continue
        s = slug_override.get(notation) or slugify(notation)
        slugs[notation] = s
        concepts.append(_L.concept_obj(
            scheme_id, notation, notation, None,
            slug=s,
            alt_labels=alt.get(notation),
            broader=("%s/%s" % (scheme_id, broader[s])) if s in broader else None,
        ))

    label = _pick(data["labels"], prop)
    desc = _pick(data["descs"], "Allowed values for %s." % label)
    return scheme_id, pslug, _L.concept_scheme_obj(scheme_id, label, desc, concepts), slugs


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write the catalog and remove the "
                                                         "per-technique schemes it supersedes")
    args = ap.parse_args()

    sidecar = load_sidecar()
    props = collect()

    # Everything currently on disk, minus what other generators own.
    existing = {os.path.basename(p) for p in glob.glob(os.path.join(VOCAB, "*.json"))}
    protected_present = existing & PROTECTED
    superseded = existing - PROTECTED

    schemes, all_slugs, collisions = {}, {}, []
    for prop, data in sorted(props.items()):
        scheme_id, pslug, obj, slugs = build_scheme(prop, data, sidecar)
        if pslug in schemes:
            collisions.append("two properties slug to %r: %r and %r"
                              % (pslug, schemes[pslug][0], prop))
        schemes[pslug] = (prop, obj, data)
        seen = {}
        for notation, s in slugs.items():
            if s in seen:
                collisions.append("in %s, %r and %r both slug to %r"
                                  % (pslug, seen[s], notation, s))
            seen[s] = notation
        all_slugs[pslug] = seen

    shared = sum(1 for _, (_, _, d) in schemes.items() if len({t for ts in d["terms"].values()
                                                               for t in ts}) > 1)
    print("CONSOLIDATION PLAN")
    print("  per-technique schemes superseded : %d" % len(superseded))
    print("  protected (other generators)     : %d  %s"
          % (len(protected_present), sorted(protected_present)))
    print("  consolidated property schemes    : %d" % len(schemes))
    print("     of which minted by >1 technique: %d" % shared)
    print("  distinct concepts                : %d" % sum(len(v) for v in all_slugs.values()))
    print("  concept @id collisions           : %d" % len(collisions))
    for c in collisions:
        print("     COLLISION: %s" % c)
    print("  files after                      : %d -> %d"
          % (len(existing), len(schemes) + len(protected_present)))

    # Sidecar entries that match nothing are a silent no-op otherwise.
    for pslug, side in sorted(sidecar.items()):
        if pslug not in schemes:
            print("  WARNING sidecar names an unknown property: %s" % pslug)
            continue
        known = set(all_slugs[pslug].values()) | set(all_slugs[pslug])
        for notation in list(side.get("slug", {})) + list(side.get("altLabel", {})):
            if notation not in schemes[pslug][2]["terms"] and notation not in known:
                print("  WARNING sidecar %s names an absent term: %r" % (pslug, notation))
        for narrower, up in side.get("broader", {}).items():
            # all_slugs[pslug] maps SLUG -> notation, so the keys are what broader names.
            have = set(all_slugs[pslug])
            if narrower not in have:
                print("  WARNING sidecar %s broader names an absent concept: %r" % (pslug, narrower))
            if up not in have:
                print("  WARNING sidecar %s broader names an absent parent: %r" % (pslug, up))

    if collisions:
        print("\nREFUSING to write: a concept @id collision would fork one IRI across two terms.")
        return 1
    if not args.write:
        print("\n(dry run; pass --write)")
        return 0

    for name in sorted(superseded):
        os.remove(os.path.join(VOCAB, name))
    for pslug, (_, obj, _) in sorted(schemes.items()):
        # newline="\n" like every other generator here: on Windows the default text mode writes
        # CRLF, and .gitattributes then normalises on commit, so the blob is right but the working
        # copy disagrees with a freshly regenerated one. Every generated file in this repo is LF.
        with open(os.path.join(VOCAB, pslug + ".json"), "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    print("\nwrote %d consolidated schemes, removed %d per-technique schemes"
          % (len(schemes), len(superseded)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
