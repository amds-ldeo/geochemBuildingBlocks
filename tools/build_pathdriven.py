"""Path-driven TAPP writer — emits the two schema.yaml artifacts for a TAPP whose CFG is generated
"via the path-driven pipeline" (schema paths, not the tier matrix):

  * <tapp>/schema.yaml        — MethodDefinition overlay wrapped over ../tappDefinition/schema.yaml;
                                 method parameters $ref the SHARED parameter registries.
  * detail<Short>/schema.yaml — a standalone schema:Dataset overlay reusing CDIF/schema.org slots
                                 (schema:contributor[analyst], prov:wasGeneratedBy, schema:funding,
                                 schema:measurementTechnique, dqv:hasQualityMeasurement, …), with the
                                 per-dataset PropertyValue defs INLINED (self-contained; the shared
                                 registry is left untouched). It is combined with adaProduct via allOf
                                 in the technique profile; ada:componentType lives on the profile's
                                 schema:distribution.hasPart, not here.

This makes the detailLAICPMS rebuild (commit 549df865) reproducible and reusable for the other
path-driven workbooks. It reads the same canonical docs/<wb>.schemapaths.json the schema/example
emitters use, so schema and example stay mutually consistent.

Prerequisite: run `python tools/build_tapp.py <tapp>` first — that populates the shared parameter
registries + vocab + gen_index (the TAPP schema $refs those registry $defs).

    python tools/build_pathdriven.py <tapp>          # e.g. geochronTAPP
"""
import copy
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schema_path_emitter as e
import schema_path_example_emitter as ex

_REG_RE = re.compile(r"/(parameterTemplates|parameterValues|analyteColumns)/schema\.yaml#/\$defs/(.+)$")


def _inline_registry_refs(node, registries, cache):
    """Replace every registry $ref with the generated def, reusing ONE object per def name so
    PyYAML emits anchors/aliases (the detail's items.anyOf and contains reference the same def)."""
    if isinstance(node, dict):
        m = _REG_RE.search(node.get("$ref", ""))
        if m and m.group(2) in registries.get(m.group(1), {}):
            key = (m.group(1), m.group(2))
            if key not in cache:
                cache[key] = copy.deepcopy(registries[m.group(1)][m.group(2)])
            siblings = {k: v for k, v in node.items() if k != "$ref"}
            if siblings:                       # e.g. readOnly on a read-only TAPP param — preserve it
                return {**copy.deepcopy(cache[key]), **siblings}
            return cache[key]                  # shared object -> PyYAML anchors/aliases
        return {k: _inline_registry_refs(v, registries, cache) for k, v in node.items()}
    if isinstance(node, list):
        return [_inline_registry_refs(v, registries, cache) for v in node]
    return node


_REGISTRY_ID_PREFIX = {
    "analyteColumns": "ada:analyteColumn/",
    "parameterTemplates": "ada:parameter/",
    "parameterValues": "ada:parameter/",
}


def _def_id(body):
    return str(((body.get("properties") or {}).get("@id") or {}).get("const", ""))


def _write_registry(reg_name, defs, tapp):
    """Publish this TAPP's generated $defs into the shared registry file, ADDITIVELY.

    Deliberately additive, deduplicated on the def's @id const (its true identity) rather than on
    the $def key. Replace-by-ownership was tried and is wrong here: the legacy matrix route
    (build_tapp/_tapp_lib, reading the richer annotated workbooks) and the path-driven route read
    DIFFERENT sources and have different coverage — EPMA has 26 analyte columns in the registry but
    only 2 rows in its schema-path sidecar — so replacing a TAPP's entries would have destroyed 24
    real EPMA columns, ~46 parameterTemplates and ~136 parameterValues that no path-driven run
    reproduces.

    Consequence: entries the path-driven route no longer generates are NOT pruned. Converging the
    two routes is a separate decision; until then the registry is a union and never loses content.
    """
    path = os.path.join(b.ROOT, "_sources", "registry", reg_name, "schema.yaml")
    if not os.path.exists(path):
        print(f"  registry {reg_name}: {path} missing, skipped")
        return
    with open(path, encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    existing = doc.get("$defs") or {}
    have_ids = {_def_id(v) for v in existing.values()}
    new = {k: v for k, v in defs.items() if _def_id(v) not in have_ids}
    if not new:
        print(f"  registry {reg_name}: {tapp} already represented, no change")
        return
    merged = dict(existing)
    merged.update(new)
    doc["$defs"] = dict(sorted(merged.items()))
    b.write(path, b.dump_yaml(doc))
    print(f"  registry {reg_name}: +{len(new)} from {tapp} "
          f"({len(defs) - len(new)} already present), {len(doc['$defs'])} total")


def build_pathdriven(tapp, write_registries=True):
    b.configure(tapp)
    overlays, registries, required = e.build(tapp)

    # ---- shared registries: publish this TAPP's generated analyte columns so the catalog covers
    # every technique, not just the two the legacy route happened to write. The schemas below still
    # INLINE the defs (see the note on the TAPP schema); publishing and inlining are independent.
    #
    # Only analyteColumns for now. The parameter registries hold ~180 legacy-route defs the
    # path-driven route does not regenerate, so publishing there would add a second, namespaced
    # copy of everything alongside them — churn without a decision on converging the two routes.
    if write_registries and registries.get("analyteColumns"):
        _write_registry("analyteColumns", registries["analyteColumns"], tapp)

    # ---- TAPP schema: MethodDefinition overlay over the base tappDefinition.
    # Inline the parameter defs (like the detail) rather than $ref the shared registry: the shared
    # registry keys defs by bare name, so a param name shared with another TAPP (e.g. laicpms)
    # resolves to that TAPP's def — including its per-TAPP @id const — which the geochron example's
    # (geochron-@id'd) parameter instances then fail. Inlining from THIS TAPP's in-memory registry
    # keeps schema and example on the same @ids.
    md = _inline_registry_refs(overlays["MethodDefinition"], registries, {})
    tapp_schema = e.wrap("MethodDefinition", md, required["MethodDefinition"],
                         title=b.CFG.get("title"), description=b.CFG.get("description"))
    b.write(os.path.join(b.TAPP_DIR, "schema.yaml"), b.dump_yaml(tapp_schema))

    # ---- detail schema: standalone Dataset overlay, PropertyValue defs inlined
    ds = _inline_registry_refs(overlays["Dataset"], registries, {})
    detail = {"$schema": "https://json-schema.org/draft/2020-12/schema",
              "title": b.CFG.get("detail_title"), "description": b.CFG.get("detail_description")}
    detail.update(ds)  # type + properties (+ any node-level constraints)
    if required["Dataset"]:
        detail["required"] = required["Dataset"]
    b.write(os.path.join(b.DETAIL_DIR, "schema.yaml"), b.dump_yaml(detail))

    # ---- examples: synthetic -P0 for the TAPP and the detail, built from the same schema paths
    short = tapp.replace("TAPP", "").upper()
    examples = ex.build_example(tapp)
    tapp_inst = {"@context": ex._CTX, "@id": f"ex:{tapp}-P0", "@type": ex._TAPP_TYPE,
                 "schema:name": f"Example {tapp}", **examples["MethodDefinition"]}
    detail_inst = {"@context": ex._CTX, "@id": f"ex:detail{short}-P0",
                   "@type": ["schema:Dataset", "schema:Product"], **examples["Dataset"]}
    _write_json(os.path.join(b.TAPP_DIR, f"example{tapp}-P0.json"), tapp_inst)
    _write_json(os.path.join(b.DETAIL_DIR, f"exampledetail{short}-P0.json"), detail_inst)

    print(f"DONE {tapp}: TAPP overlay {len(overlays['MethodDefinition'].get('properties', {}))} props; "
          f"detail {len(ds.get('properties', {}))} props; required MD={required['MethodDefinition']} "
          f"DS={required['Dataset']}")


def _write_json(path, obj):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("wrote", os.path.relpath(path, e.ROOT))


def validate(tapp):
    """Validate the shipped -P0 examples against the locally-resolved resolvedSchema.json for both
    the TAPP and its detail. Returns 0 if both green."""
    import jsonschema
    b.configure(tapp)
    short = tapp.replace("TAPP", "").upper()
    rc = 0
    for label, ex_path, res_path in [
        (tapp, os.path.join(b.TAPP_DIR, f"example{tapp}-P0.json"),
         os.path.join(b.TAPP_DIR, "resolvedSchema.json")),
        (f"detail{short}", os.path.join(b.DETAIL_DIR, f"exampledetail{short}-P0.json"),
         os.path.join(b.DETAIL_DIR, "resolvedSchema.json"))]:
        inst = json.load(open(ex_path, encoding="utf-8"))
        schema = json.load(open(res_path, encoding="utf-8"))
        errs = sorted(jsonschema.Draft202012Validator(schema).iter_errors(inst), key=lambda x: list(x.path))
        if errs:
            rc = 1
            print(f"{label}: {len(errs)} error(s)")
            for er in errs[:12]:
                print(f"  /{'/'.join(map(str, er.path))}: {er.message[:110]}")
        else:
            print(f"{label}: GREEN")
    return rc


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit("usage: build_pathdriven.py <tapp> [--validate]   (run build_tapp.py <tapp> first)")
    if "--validate" in sys.argv:
        sys.exit(validate(args[0]))
    build_pathdriven(args[0])
