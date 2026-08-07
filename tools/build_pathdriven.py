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


def build_pathdriven(tapp):
    b.configure(tapp)
    overlays, registries, required = e.build(tapp)

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
