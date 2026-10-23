#!/usr/bin/env python
"""PROTOTYPE: factor the per-technique parameter registries into a variable registry.

Writes `docs/variable_registry_draft.json`. Report-only -- NOTHING consumes it, no schema changes,
no generator is wired to it. It exists to answer "is this feasible, and what does it cost" with
measurements instead of estimates, in the shape of CODATA's variable index
(https://ai.codata.org/variableindex).

WHAT THE REGISTRIES LOOK LIKE TODAY. Six collections under `_sources/registry/` hold 1893 `$defs`
between them, every one minted per consuming technique: the `$def` key carries a technique prefix
(`epma_detectionLimitDefault`) and the `@id` const is `ada:parameter/<tapp>TAPP/<name>`. The
LOGICAL variable is neither of those -- it is the `schema:name` const, the TAPP workbook's Metadata
Item, and there are 267 distinct ones. So one logical variable such as `Pre-Analysis Imaging and
Screening` exists 116 times over, once per technique that consumes it.

THE TARGET SHAPE IS ALREADY DEFINED UPSTREAM, which is what makes this tractable. CDIF publishes
`cdifDataType/cdifRepresentedVariable` and `cdifDataType/cdifInstanceVariable`, and the latter
carries `cdif:isDefinedBy_RepresentedVariable` -- "the RepresentedVariable this InstanceVariable
instantiates". The relation this registry needs is therefore a vendored CDIF property, not an
extension we have to propose upstream:

    267 x cdi:RepresentedVariable      the concept + value domain, not dataset-bound
    1893 x the existing registry defs  each referencing its RepresentedVariable

Two things an earlier pass got wrong, measured here instead:

  * `schema:propertyID` is NOT patchily present. It partitions CLEANLY by side -- 1233
    analysis-side defs carry it and none carry `schema:valueName`; 660 procedure-side defs carry
    `valueName` and none carry `propertyID`; 0 defs carry both, 0 carry neither. There is no
    coverage gap and no branch is needed. CDIF documents `cdif:uses` as "essentially the same as
    schema:propertyID", so the analysis side already carries the link in all but name.
  * The name belongs in `cdif:name` and the definition in `cdif:definition`, per the vendored
    `cdifRepresentedVariable` schema. `cdi:measures` is a different property -- it points at the
    CONCEPT measured, not at the variable's label.

THE REAL COST IS DEFINITIONAL, NOT MECHANICAL. 31 of the 267 logical names carry more than one
`description` across their defs, and only 2 of those reduce to the procedure/analysis side split
(where two descriptions of one concept at two levels is correct, and is precisely the
RepresentedVariable/InstanceVariable distinction this registry is built on). The other 29 conflict
WITHIN a side: the same workbook label means subtly different things per technique. `Detection
Limit` has 5 variants across 23 defs -- a procedure-typical estimate, a session value in ug/g, a
method detection limit at 99% confidence, an elemental limit with units specified, and one
carrying an isotope-dilution caveat. That is not wording drift.

So each of the 29 is a decision nobody can automate: ONE RepresentedVariable whose definition is
chosen and whose per-technique nuance moves onto the usage, or SEVERAL because the label is
overloaded. This tool refuses to pick. It emits them under `conflicts` with every variant and the
defs behind it, and mints a RepresentedVariable only where the definition is already unanimous.

Usage:
    python tools/draft_variable_registry.py           # measure and report
    python tools/draft_variable_registry.py --write   # write docs/variable_registry_draft.json
"""
import argparse
import collections
import io
import json
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join("docs", "variable_registry_draft.json")

# Every collection build_tapp writes a parameter or column def into. The side is derived PER DEF
# from which identity property it carries, never from the collection: monitoredPropertyColumns
# holds 62 procedure-side defs and 1 analysis-side one, so a per-collection assumption mis-sides
# that one.
COLLECTIONS = ("parameterTemplates", "parameterValues", "targetSpeciesColumns",
               "monitoredPropertyColumns", "targetMaterialColumns", "reportedPropertyColumns")


def _camel(label):
    """A stable @id token from a workbook label. Lower camel, per the repo's naming decision.

    A trailing optional-plural `(s)` is dropped rather than folded in: four labels carry one
    (`Data Processing Software(s)`, `Background Position(s)`, `EDS Calibration Standard(s)`,
    `Spectroscopic Detector(s)`) and keeping it yields `dataProcessingSoftwareS`, which reads as
    a typo. Verified not to collide with any other label's token after stripping. Parentheses
    elsewhere hold an acronym or a qualifier and ARE folded in, which is why this is a suffix
    rule and not a general paren rule.
    """
    label = re.sub(r"\(s\)\s*$", "", label, flags=re.I)
    parts = [p for p in re.split(r"[^0-9A-Za-z]+", label) if p]
    if not parts:
        return "unnamed"
    head = parts[0]
    head = head.lower() if head.isupper() and len(head) > 1 else head[:1].lower() + head[1:]
    return head + "".join(p[:1].upper() + p[1:] for p in parts[1:])


def load_defs():
    """Every registry $def, with the fields a variable registry would need from it."""
    out = []
    for coll in COLLECTIONS:
        path = os.path.join(ROOT, "_sources", "registry", coll, "schema.yaml")
        doc = yaml.safe_load(io.open(path, encoding="utf-8")) or {}
        for key, sub in (doc.get("$defs") or {}).items():
            props = sub.get("properties") or {}

            def const(name, _p=props):
                return (_p.get(name) or {}).get("const")

            out.append({
                "collection": coll,
                "def": key,
                # The side is the identity property, measured per def. See COLLECTIONS.
                "side": "analysis" if "schema:propertyID" in props else "procedure",
                "id": const("@id"),
                "name": const("schema:name"),
                "definition": (sub.get("description") or "").strip(),
                "dataType": const("ada:dataType"),
                "unitText": const("schema:unitText"),
            })
    return out


def build(defs):
    """({variable @id -> node}, [conflict, ...]) grouped on the logical name."""
    by_name = collections.defaultdict(list)
    for d in defs:
        if d["name"]:
            by_name[d["name"]].append(d)

    variables, conflicts = {}, []
    for name in sorted(by_name):
        rows = by_name[name]
        variants = collections.defaultdict(list)
        for r in rows:
            variants[r["definition"]].append(r["def"])

        # Does the divergence reduce to the side split? Two descriptions of one concept, one per
        # side, is CORRECT -- it is the level distinction, not a disagreement. Anything beyond
        # that is a genuine conflict.
        per_side = {s: {r["definition"] for r in rows if r["side"] == s}
                    for s in ("procedure", "analysis")}
        side_only = all(len(v) <= 1 for v in per_side.values())

        vid = "ada:variable/" + _camel(name)

        if len(variants) > 1 and not side_only:
            # Emitted as a QUESTION, not a variable. Taking the most common definition here would
            # bury four other readings of `Detection Limit` behind a majority vote.
            conflicts.append({
                "proposed@id": vid,
                "cdif:name": name,
                "defs": len(rows),
                "why": ("more than one definition within a single side, so this label is either "
                        "overloaded -- several RepresentedVariables -- or needs one definition "
                        "chosen and the per-technique nuance moved onto the usage"),
                "variants": [{"definition": d, "defs": sorted(ks)}
                             for d, ks in sorted(variants.items(), key=lambda kv: -len(kv[1]))],
            })
            continue

        node = {
            "@id": vid,
            "@type": ["cdi:RepresentedVariable"],
            "cdif:name": name,
            # Where the only divergence IS the side split, both readings are kept, keyed by side,
            # rather than collapsed: the procedure side defines what will be recorded, the
            # analysis side what was.
            "cdif:definition": (sorted(variants)[0] if len(variants) == 1
                                else {s: sorted(v)[0] for s, v in per_side.items() if v}),
            "ada:usageCount": len(rows),
            "ada:usages": [{"@id": r["id"], "def": r["def"], "collection": r["collection"],
                            "side": r["side"]} for r in sorted(rows, key=lambda r: r["def"])],
        }
        dtypes = sorted({r["dataType"] for r in rows if r["dataType"]})
        units = sorted({r["unitText"] for r in rows if r["unitText"]})
        if dtypes:
            node["cdi:hasIntendedDataType"] = dtypes[0] if len(dtypes) == 1 else dtypes
        if units:
            node["cdi:describedUnitOfMeasure"] = units[0] if len(units) == 1 else units
        variables[vid] = node

    return variables, conflicts


def report(defs, variables, conflicts):
    sides = collections.Counter(d["side"] for d in defs)
    names = {d["name"] for d in defs if d["name"]}
    print("registry $defs                       : %d" % len(defs))
    print("  procedure side (schema:valueName)  : %d" % sides["procedure"])
    print("  analysis side  (schema:propertyID) : %d" % sides["analysis"])
    print("distinct logical variables           : %d" % len(names))
    print("  mintable now (definition agreed)   : %d" % len(variables))
    print("  blocked on a definitional decision : %d" % len(conflicts))
    dedup = len(defs) - len(names)
    print("\ndefs that would become usages of a shared variable: %d (%.0f%% of the registry)"
          % (dedup, 100.0 * dedup / max(len(defs), 1)))
    print("\nmost-reused variables:")
    for vid, n in sorted(((v["@id"], v["ada:usageCount"]) for v in variables.values()),
                         key=lambda kv: -kv[1])[:8]:
        print("   %-52s %d usages" % (vid[:52], n))
    if conflicts:
        print("\nblocked -- each needs a human decision, worst first:")
        for c in sorted(conflicts, key=lambda c: -len(c["variants"]))[:10]:
            print("   %-46s %d variants, %d defs"
                  % (c["cdif:name"][:46], len(c["variants"]), c["defs"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write %s" % OUT)
    args = ap.parse_args()

    defs = load_defs()
    variables, conflicts = build(defs)
    report(defs, variables, conflicts)

    doc = {
        "generator": "tools/draft_variable_registry.py",
        "status": ("DRAFT / PROTOTYPE. Nothing reads this, no schema references it, and no "
                   "generator emits from it. It is a feasibility measurement, not a deliverable."),
        "modelled_on": "https://ai.codata.org/variableindex",
        "target_shape": {
            "represented_variable": ("CDIF's vendored cdifDataType/cdifRepresentedVariable -- the "
                                     "concept plus value domain, not bound to any dataset"),
            "usage": ("each existing registry $def, referencing its variable through "
                      "cdif:isDefinedBy_RepresentedVariable, a vendored CDIF property on "
                      "cdifInstanceVariable, so no upstream extension is needed"),
            "name_carrier": ("cdif:name, with cdif:definition for the definition. NOT cdi:measures, "
                             "which points at the concept measured rather than at the label."),
            "propertyID": ("no branch needed: propertyID and valueName partition cleanly by side "
                           "(0 defs carry both, 0 carry neither), and CDIF documents cdif:uses as "
                           "'essentially the same as schema:propertyID'"),
            "open": ("whether a procedure-side schema:PropertyValueSpecification should be typed "
                     "cdi:InstanceVariable at all -- a specification is not an instance. The "
                     "reference to the RepresentedVariable is right either way, so this draft "
                     "records the usages without asserting an @type on them."),
        },
        "counts": {
            "registry_defs": len(defs),
            "distinct_logical_variables": len({d["name"] for d in defs if d["name"]}),
            "mintable_now": len(variables),
            "blocked_on_a_definition": len(conflicts),
        },
        "conflicts": sorted(conflicts, key=lambda c: (-len(c["variants"]), c["cdif:name"])),
        "variables": variables,
    }
    if args.write:
        io.open(OUT, "w", encoding="utf-8", newline="\n").write(
            json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
        print("\nwrote %s" % OUT)
    else:
        print("\ndry run; --write to emit %s" % OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
