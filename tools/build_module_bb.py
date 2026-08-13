#!/usr/bin/env python3
"""Generate a composition module's building block from its CSV and sidecar.

Group1 was hand-written as a proof. The rest are generated, so a module BB cannot silently drift
from the sidecar that defines it: change a path or a tier upstream and re-running this is the whole
update.

The schema is built with the SAME merger the technique overlays use (schema_path_emitter.insert /
to_schema), for the same reason the emitter exists at all — a module field can be a nested
instrument property or a workflow-step parameter, not just a scalar, and re-deriving that placement
logic here would be a second implementation to keep in step with the first.

Two $defs, split by path root, because a procedure and an analysis are separate documents here:

  ProcedureIdentification   from the module's $MethodDefinition paths — what the procedure asserts
  AnalysisIdentification    from its $Dataset paths — what each run supplies

A module with paths on only one side gets only that $def. Requiredness follows the tier matrix:
Basic on a side makes the field required there.

A module whose fields are ALL unplaced generates nothing and says so. Geochronology and UPb are in
that state — their nine fields appear in no technique sidecar, so there is no placement to build
from, and emitting an empty schema would assert that a conforming procedure carries nothing.

    python tools/build_module_bb.py                 # report
    python tools/build_module_bb.py --write
    python tools/build_module_bb.py --module MCICPMS --write
"""
import argparse
import collections
import datetime
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import migrate_sidecar as ms
import schema_path_emitter as e
import schema_path_parser as spp
import schemapath_io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODDIR = os.path.join(ROOT, "TAPPS20260811", "Claude Skills for TAPP", "modules")
BBDIR = os.path.join(ROOT, "_sources", "BaseSchema", "modules")

DEF_NAME = {"MethodDefinition": "ProcedureIdentification", "Dataset": "AnalysisIdentification"}
DEF_BLURB = {
    "MethodDefinition": ("Composed into a TAPP (prov:Plan) schema: what the procedure asserts once, "
                         "for every analysis that follows it."),
    "Dataset": ("Composed into a technique detail (schema:Dataset) schema: what each run supplies "
                "fresh, because it cannot be known until the analysis happens."),
}
# camelCase directory name, matching the existing group1/
DIRNAME = {"ReportingCore": "reportingCore", "LaserAblation": "laserAblation",
           "SolutionIntroduction": "solutionIntroduction", "MCICPMS": "mcIcpms",
           "UPb": "uPb", "Geochronology": "geochronology", "ArAr": "arAr", "Group1": "group1"}
PREFIX_IRI = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
              "prov": "http://www.w3.org/ns/prov#", "bios": "https://bioschemas.org/",
              "dqv": "http://www.w3.org/ns/dqv#",
              "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"}


def module_rows(name):
    """[(item, P, A, dt, desc)] for the module's OWNED fields (a tier-less row is an overlay)."""
    src = os.path.join(MODDIR, f"Module_{name}.csv")
    import tapp_source
    raw = tapp_source.rows(src)
    hdr = [b.norm(v).lower() for v in raw[0]]
    di = next((i for i, h in enumerate(hdr) if h.startswith("description")), 1)
    desc = {}
    for r in raw[1:]:
        it = b.norm(r[0]) if r and r[0] else ""
        if it:
            desc[it] = b.norm(r[di]) if di < len(r) else ""
    return [(i, P, A, dt, desc.get(i, "")) for i, P, A, dt in ms.source_items(src) if P or A]


def build_schema(name):
    """({root -> subschema}, stats) from the module's sidecar paths."""
    rows = module_rows(name)
    spec = schemapath_io.load_spec(schemapath_io.csv_path(os.path.join(MODDIR, f"Module_{name}.csv")))
    meta = {i: (P, A, dt, d) for i, P, A, dt, d in rows}
    roots = {"MethodDefinition": e.Obj(), "Dataset": e.Obj()}
    # Object-level requiredness is NOT carried in the tree — Obj has no `required`, and
    # schema_path_emitter.build() accumulates it separately for wrap() to apply. Calling
    # insert()/to_schema() directly therefore loses it silently, which is how the first run of this
    # generator produced four modules asserting nothing required at all. Same condition as build():
    # a Basic tier, on a path that is a single top-level direct property.
    required = {"MethodDefinition": [], "Dataset": []}
    shacl_top = {"MethodDefinition": set(), "Dataset": set()}
    used, placed, unplaced = set(), 0, []
    for item, (P, A, dt, desc) in meta.items():
        paths = spec.get(item, {}).get("path")
        paths = ([paths] if isinstance(paths, str) else list(paths or []))
        paths = [p for p in paths if p]
        if not paths:
            unplaced.append(item)
            continue
        for path in paths:
            parsed = spp.parse(path)
            require = (P == "Basic") if parsed.root == "MethodDefinition" else (A == "Basic")
            e.insert(roots[parsed.root], parsed, e.leaf_for(desc, dt), require=require)
            non_type = [s for s in parsed.segments if not s.is_type]
            if (require and len(non_type) == 1 and non_type[0].selector is None
                    and not non_type[0].is_array
                    and non_type[0].prop not in required[parsed.root]):
                required[parsed.root].append(non_type[0].prop)
            # The CONTAINER a required field sits in is itself implied, however deep the field is.
            # JSON Schema `required` deliberately covers only top-level direct properties (matching
            # build()), but a Basic field under actionProcess.step still means the procedure has an
            # actionProcess — and that is a true, checkable statement. Without it a module whose
            # only required field is nested produces no shapes at all: UPb's sole Basic field lives
            # under a step, so its rules.shacl came out empty and the BB audit rejected it.
            if require and non_type:
                shacl_top[parsed.root].add(non_type[0].prop)
            placed += 1
            used.update(re.findall(r"\b([a-z]+):", path))
    out = {}
    for r, node in roots.items():
        sch = e.to_schema(node)
        if sch.get("properties"):
            if required[r]:
                sch = {**sch, "required": sorted(required[r])}
            out[r] = sch
    return out, {"fields": len(meta), "placed": placed, "unplaced": unplaced,
                 "prefixes": sorted(used & set(PREFIX_IRI)),
                 "shacl_top": {r: sorted(v) for r, v in shacl_top.items()}}


def render(name, defs, stats, composed_by):
    today = datetime.date.today().isoformat()
    doc = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"TAPP Composition Module: {name}",
        "description": (
            f"The shared {name} block of the 2026-08-11 TAPP library "
            f"(Claude Skills for TAPP/Module_{name}.csv), composed by {composed_by} of the sixteen "
            f"delivery tables. {stats['fields']} owned fields over {stats['placed']} schema paths.\n\n"
            "GENERATED by tools/build_module_bb.py from the module's CSV and its schema-path "
            "sidecar — edit those, not this file. Requiredness follows the TAPP tier matrix: a "
            "field Basic on a side is required there, Advanced is permitted, N/A is absent from "
            "that side entirely.\n\n"
            "This is a PROFILE, not a vocabulary: it asserts which properties a conforming "
            "procedure or analysis carries. Column F (Example / Allowed Content) is consumer-owned "
            "per the module manifest, so no enum is pinned here — a consuming TAPP may narrow a "
            "value space, never widen it."),
        "$defs": {},
    }
    for r, sch in defs.items():
        doc["$defs"][DEF_NAME[r]] = {"title": f"{name} fields on the "
                                     f"{'procedure' if r == 'MethodDefinition' else 'analysis'}",
                                     "description": DEF_BLURB[r], **sch}
    return doc


def write_bb(name, doc, stats, composed_by):
    d = os.path.join(BBDIR, DIRNAME.get(name, name.lower()))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "schema.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True, width=100)

    today = datetime.date.today().isoformat()
    bb = {"$schema": "metaschema.yaml",
          "name": f"TAPP Composition Module: {name}",
          "abstract": (f"The shared {name} block of the 2026-08-11 TAPP library, composed by "
                       f"{composed_by} of the sixteen delivery tables. {stats['fields']} owned "
                       f"fields over {stats['placed']} schema paths, split into the procedure and "
                       f"analysis halves a TAPP schema and a technique detail compose "
                       f"respectively. A profile over existing tappDefinition/adaProduct "
                       f"properties, not a new vocabulary. Generated from the module CSV and its "
                       f"schema-path sidecar."),
          "status": "under-development", "dateTimeAddition": f"{today}T00:00:00Z",
          "itemClass": "schema", "register": "cdif-building-block-register",
          "version": "0.1", "dateOfLastChange": today,
          "link": "https://github.com/usgin/geochemBuildingBlocks",
          "maturity": "draft", "scope": "unstable",
          "tags": ["ada", "astromat", "tapp", "composition-module", "profile",
                   re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()],
          "sources": [{"title": f"TAPP Module {name} (2026-08-11 library)",
                       "link": "https://github.com/usgin/geochemBuildingBlocks"},
                      {"title": "ADA Metadata Schema v3",
                       "link": "https://github.com/amds-ldeo/metadata"}]}
    with open(os.path.join(d, "bblock.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(bb, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ctx = {"@context": {p: PREFIX_IRI[p] for p in stats["prefixes"]}}
    with open(os.path.join(d, "context.jsonld"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(ctx, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return d


def _sample(sch):
    """A plausible instance for a generated subschema — every property, not just the required ones.

    Covers all of them because these modules are profiles: the point of the example is to show what
    a conforming procedure looks like, and a minimal instance of a $def with no required properties
    is `{}`, which shows nothing.
    """
    if not isinstance(sch, dict):
        return "example value"
    if "const" in sch:
        return sch["const"]
    if "enum" in sch:
        return sch["enum"][0]
    if "anyOf" in sch:
        return _sample(sch["anyOf"][0])
    t = sch.get("type")
    if t == "object" or "properties" in sch:
        return {k: _sample(v) for k, v in (sch.get("properties") or {}).items()}
    if t == "array":
        items = sch.get("items") or {}
        # the additionalProperty shape: one item per if/then branch, each carrying its discriminator
        conds = [c for c in (items.get("allOf") or []) if isinstance(c, dict) and "if" in c]
        if conds:
            out = []
            for c in conds:
                sel = {k: _sample(v) for k, v in (c["if"].get("properties") or {}).items()}
                out.append({**sel, **{k: _sample(v)
                                      for k, v in ((c.get("then") or {}).get("properties") or {}).items()}})
            return out
        return [_sample(items)] if items else []
    if t == "boolean":
        return True
    if t in ("number", "integer"):
        return 1
    return "example value"


def write_examples(d, name, doc):
    import jsonschema
    ex, problems = [], []
    for defname, sub in doc["$defs"].items():
        inst = _sample(sub)
        errs = list(jsonschema.Draft202012Validator(
            {"$schema": "https://json-schema.org/draft/2020-12/schema", **sub}).iter_errors(inst))
        if errs:
            problems.append((defname, errs[0].message[:120]))
        side = "procedure" if defname.startswith("Procedure") else "analysis"
        article = "a" if side == "procedure" else "an"
        ex.append({
            "title": f"{name} composed into {article} {side} ({defname})",
            "content": (f"The {side} half of the {name} module, with every property populated. "
                        f"Generated from the schema, so it tracks the sidecar."),
            "prefixes": {p: PREFIX_IRI[p] for p in sorted(_prefixes_in(inst))},
            "snippets": [{"language": "json", "code": json.dumps(inst, indent=2, ensure_ascii=False)}],
        })
    with open(os.path.join(d, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.dump(ex, f, Dumper=_BlockDumper, sort_keys=False, allow_unicode=True, width=100)
    return problems


class _BlockDumper(yaml.SafeDumper):
    """Emits multi-line strings as literal blocks, so the JSON snippet stays readable in the file
    instead of collapsing into one escaped line (which is what safe_dump does by default)."""


_BlockDumper.add_representer(
    str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s,
                                         style="|" if "\n" in s else None))


def _prefixes_in(obj):
    found = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                m = re.match(r"^([a-z]+):", str(k))
                if m:
                    found.add(m.group(1))
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(obj)
    return found & set(PREFIX_IRI)


_SHACL_HEAD = """@prefix sh:     <http://www.w3.org/ns/shacl#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix schema: <http://schema.org/> .
@prefix prov:   <http://www.w3.org/ns/prov#> .
@prefix ada:    <https://ada.astromat.org/metadata/> .
@prefix cdifd:  <https://cdif.org/validation/0.1/shacl#> .
@base <https://www.ogc.org/rules/template/> .

# GENERATED by tools/build_module_bb.py. Restates the module's required sets so they are checkable
# in RDF as well as in JSON Schema. Warning severity: the JSON Schema $defs enforce this for
# anything composing the module, and a harvested graph may be a partial view that should not be
# called invalid for lacking a field its source document carried.
"""

_TARGET = {"ProcedureIdentification": "https://ada.astromat.org/metadata/TAPPDefinition",
           "AnalysisIdentification": "http://schema.org/Dataset"}


def write_shacl(d, name, doc, stats):
    body = [_SHACL_HEAD]
    for defname, sub in doc["$defs"].items():
        # top-level containers implied by this side's Basic fields, so a module whose required
        # field is nested still yields a real shape rather than none
        root = "MethodDefinition" if defname.startswith("Procedure") else "Dataset"
        req = sorted(set(sub.get("required") or []) | set(stats["shacl_top"].get(root) or []))
        if not req:
            continue
        shape = f"cdifd:{name[0].lower()}{name[1:]}{defname}Shape"
        body.append(f"\n{shape}\n    a sh:NodeShape ;\n    sh:target [\n        a sh:SPARQLTarget ;"
                    f"\n        sh:select \"\"\"\n            SELECT ?this\n            WHERE {{"
                    f"\n                ?this a <{_TARGET[defname]}> .\n            }}\n"
                    f"        \"\"\" ;\n    ] ;")
        for p in req:
            body.append(f"    sh:property [\n        sh:path {p} ;\n        sh:minCount 1 ;"
                        f"\n        sh:severity sh:Warning ;\n        sh:message "
                        f"\"{name} requires {p} on the "
                        f"{'procedure' if defname.startswith('Procedure') else 'analysis'}.\" ;\n    ] ;")
        body.append(f"    sh:message \"{name} {defname} required properties.\" ;\n    .")
    if len(body) == 1:
        body.append("\n# This module declares no required properties on either side.\n")
    with open(os.path.join(d, "rules.shacl"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(body) + "\n")


def write_description(d, name, doc, stats, composed_by):
    lines = [f"# TAPP Composition Module: {name}", "",
             f"The shared **{name}** block of the 2026-08-11 TAPP library, composed by "
             f"**{composed_by} of the sixteen** delivery tables — {stats['fields']} owned fields "
             f"over {stats['placed']} schema paths.", "",
             "Generated by `tools/build_module_bb.py` from "
             f"`Module_{name}.csv` and its schema-path sidecar. Edit those, not the schema.", "",
             "This is a **profile, not a vocabulary**: it asserts which properties a conforming "
             "procedure or analysis carries, all of them already defined by `tappDefinition` or "
             "`adaProduct`.", "", "## The two `$defs`", "",
             "| `$def` | composed into | properties | required |", "|---|---|---|---|"]
    for defname, sub in doc["$defs"].items():
        into = "a TAPP schema (`prov:Plan`)" if defname.startswith("Procedure") \
            else "a technique detail (`schema:Dataset`)"
        lines.append(f"| `{defname}` | {into} | {len(sub.get('properties') or {})} | "
                     f"{len(sub.get('required') or [])} |")
    lines += ["", "Requiredness follows the TAPP tier matrix: a field Basic on a side is required "
              "there, Advanced is permitted, N/A is absent from that side entirely.", ""]
    if stats["unplaced"]:
        lines += ["## Not yet placed", "",
                  "These fields belong to the module but have no schema path in any sidecar, so "
                  "they are absent from the schema until one is authored:", ""]
        lines += [f"- {u}" for u in stats["unplaced"]] + [""]
    lines += ["## Composing it", "", "```yaml", "allOf:",
              "- $ref: ../../../BaseSchema/tappDefinition/schema.yaml",
              f"- $ref: ../../../BaseSchema/modules/{DIRNAME.get(name, name.lower())}/schema.yaml"
              "#/$defs/ProcedureIdentification", "- type: object",
              "  properties: {}   # only what this technique itself owns", "```", "",
              "`allOf` composes constraints and cannot relax them: a technique composing this "
              "module accepts its required set in full.", ""]
    with open(os.path.join(d, "description.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    man = json.load(open(os.path.join(ROOT, "TAPPS20260811", "composed_tapps.json"), encoding="utf-8"))
    usage = collections.Counter()
    for entry in man.get("composed") or []:
        for m in entry.get("modules") or []:
            usage[m.get("name")] += 1

    names = a.module or [f[len("Module_"):-4] for f in sorted(os.listdir(MODDIR))
                         if f.startswith("Module_") and f.endswith(".csv")
                         and not f.endswith(".schemapaths.csv")]   # the sidecars sit alongside
    for name in names:
        if name == "Group1":
            print(f"{name:<22s} skipped (hand-authored building block)")
            continue
        if not usage.get(name):
            print(f"{name:<22s} skipped (composed by no table in the manifest)")
            continue
        defs, stats = build_schema(name)
        if not defs:
            print(f"{name:<22s} CANNOT GENERATE — all {stats['fields']} fields unplaced "
                  f"({', '.join(stats['unplaced'][:4])}{'…' if len(stats['unplaced']) > 4 else ''})")
            continue
        doc = render(name, defs, stats, usage[name])
        halves = ", ".join(DEF_NAME[r] for r in defs)
        print(f"{name:<22s} {stats['fields']:2d} fields, {stats['placed']:2d} paths -> {halves}"
              f"{'   unplaced: ' + ', '.join(stats['unplaced']) if stats['unplaced'] else ''}")
        if a.write:
            d = write_bb(name, doc, stats, usage[name])
            problems = write_examples(d, name, doc)
            write_shacl(d, name, doc, stats)
            write_description(d, name, doc, stats, usage[name])
            print(f"{'':22s} wrote {os.path.relpath(d, ROOT)}")
            for defname, msg in problems:
                print(f"{'':22s} EXAMPLE FAILS {defname}: {msg}")
    if not a.write:
        print("\n(dry run — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
