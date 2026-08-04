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
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schema_path_emitter as e

_REG_RE = re.compile(r"/(parameterTemplates|parameterValues)/schema\.yaml#/\$defs/(.+)$")


def _inline_registry_refs(node, registries, cache):
    """Replace every registry $ref with the generated def, reusing ONE object per def name so
    PyYAML emits anchors/aliases (the detail's items.anyOf and contains reference the same def)."""
    if isinstance(node, dict):
        m = _REG_RE.search(node.get("$ref", ""))
        if m and m.group(2) in registries.get(m.group(1), {}):
            key = (m.group(1), m.group(2))
            if key not in cache:
                cache[key] = copy.deepcopy(registries[m.group(1)][m.group(2)])
            return cache[key]
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

    print(f"DONE {tapp}: TAPP overlay {len(overlays['MethodDefinition'].get('properties', {}))} props; "
          f"detail {len(ds.get('properties', {}))} props; required MD={required['MethodDefinition']} "
          f"DS={required['Dataset']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: build_pathdriven.py <tapp>   (run build_tapp.py <tapp> first)")
    build_pathdriven(sys.argv[1])
