"""Phase 2 of the nested-interpreter work: EXAMPLE EMITTER.

Builds a JSON-LD example instance for a TAPP from its canonical schema paths, reusing the SAME
merger as the schema emitter (schema_path_emitter.insert / Obj/Arr/Leaf/Collision) — only the leaf
differs: here a leaf is a placeholder VALUE (or, for additionalProperty parameters, a full
PropertyValue/PropertyValueSpecification instance derived from the registry $def). to_instance()
serializes the shared tree to instance JSON.

The generated example is validated against the path-driven SCHEMA (schema_path_emitter.build) made
self-contained (registry $defs inlined, $refs localised) — proving schema and example are mutually
consistent. This is the last piece needed to flip a TAPP to path-driven and go green end-to-end.

    python tools/schema_path_example_emitter.py            # build + validate laicpms example
    python tools/schema_path_example_emitter.py <tapp> --out=<dir>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schema_path_parser as spp
import schema_path_emitter as e

ROOT = e.ROOT

# a plausible instance @type / @context for the TAPP plan (mirrors the shipped examples)
_TAPP_TYPE = ["prov:Plan", "cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"]
_CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/", "prov": "http://www.w3.org/ns/prov#",
        "bios": "https://bioschemas.org/", "dqv": "http://www.w3.org/ns/dqv#"}


def instance_from_def(s):
    """A minimal valid instance satisfying a generated registry $def (const -> its value; typed -> a
    placeholder)."""
    if "const" in s:
        return s["const"]
    if "properties" in s:
        req = s.get("required") or list(s["properties"])
        return {k: instance_from_def(s["properties"][k]) for k in req if k in s["properties"]}
    t = s.get("type")
    if t == "boolean":
        return True
    if t in ("number", "integer"):
        return 1
    if "anyOf" in s:
        return 1 if any(br.get("type") in ("number", "integer") for br in s["anyOf"]) else "example value"
    return "example value"


def placeholder(m, item, sidecar):
    """A schema-satisfying placeholder value for a direct/scalar terminal."""
    dl = (m.get("dt") or "").lower()
    if "controlled" in dl:
        parts = [p.strip().strip("'\"") for p in (m.get("ex") or "").split("|")
                 if p.strip() and not p.strip().lower().startswith("e.g") and "specify" not in p.strip().lower()]
        if parts:
            return parts[0]
    if dl.startswith("bool"):
        return True
    if "integer" in dl:
        return 1
    if "numeric" in dl or "number" in dl:
        return 1.0
    return f"example {sidecar.get(item, {}).get('name') or b.camel(item)}"


def build_example(tapp):
    """{root -> instance dict} built from the canonical paths, reusing the schema-emitter merger."""
    meta = e._load_rows(tapp)
    sidecar = b.load_sidecar()
    import schemapath_io
    spec = schemapath_io.load_spec(schemapath_io.csv_path(b.XLSX))
    roots = {"MethodDefinition": e.Obj(), "Dataset": e.Obj()}
    pt_seen, pv_seen = set(), set()
    # base-owned rich-object properties (analyteTemplate, computationalTool, workflow steps, the
    # instrument tree, the plan's target-material schema:object, relatedLink) need objects the
    # placeholder can't synthesise and are all OPTIONAL in tappDefinition — so omit them from the
    # minimal valid TAPP-side example (the schema still constrains them). Dataset-side (detail)
    # sample/relatedLink are kept: the detail is validated standalone, not against the strict base.
    SKIP_MD = ("ada:analyteTemplate", "ada:reportedPropertyTemplate", "bios:computationalTool",
               "schema:actionProcess", "schema:instrument", "schema:object", "schema:relatedLink")
    for item, rec in spec.items():
        m = meta.get(item, {})
        paths = rec["path"] if isinstance(rec["path"], list) else [rec["path"]]
        for path in paths:   # usually 1; 2 for a dual-homed editable param (TAPP default + detail value)
            parsed = spp.parse(path)
            if parsed.root == "MethodDefinition" and any(t in path for t in SKIP_MD):
                continue
            if e._is_addl_param(parsed):
                bd = {"item": item, "name": (sidecar.get(item, {}).get("name") or b.camel(item)),
                      "jtype": b.jtype(m.get("dt", "")), "unit": b.unit(m.get("dt", "")),
                      "desc": m.get("desc", ""), "A": m.get("A", "")}
                if parsed.segments[-1].prop == "schema:defaultValue":
                    _, body = b.param_template_def(bd, pt_seen); pt_seen.add(next(iter(body)))
                else:
                    _, body = b.param_value_def(bd, pv_seen); pv_seen.add(next(iter(body)))
                elem = instance_from_def(next(iter(body.values())))
                trunc = spp.ParsedPath(parsed.root, parsed.segments[:-1])
                e.insert(roots[parsed.root], trunc, element=e.Leaf(elem))
                continue
            e.insert(roots[parsed.root], parsed, placeholder(m, item, sidecar))
    return {r: e.to_instance(o) for r, o in roots.items()}


def _selfcontained(overlay, registries):
    """The path-driven overlay as a standalone schema: registry $defs inlined, $refs localised to
    #/$defs/. (Validates the generated constraints; the base tappDefinition allOf is checked at the
    live-switch resolve step.)"""
    defs = {}
    for reg in registries.values():
        defs.update(reg)

    def rewrite(n):
        if isinstance(n, dict):
            if "#/$defs/" in n.get("$ref", ""):
                return {"$ref": "#/$defs/" + n["$ref"].split("#/$defs/")[1]}
            return {k: rewrite(v) for k, v in n.items()}
        if isinstance(n, list):
            return [rewrite(v) for v in n]
        return n

    return {"$schema": "https://json-schema.org/draft/2020-12/schema",
            "allOf": [rewrite({"type": "object", "properties": overlay.get("properties", {})})],
            "$defs": defs}


def _self_test(tapp="laicpmsTAPP", out_dir=None):
    import jsonschema
    examples = build_example(tapp)
    inst = {"@context": _CTX, "@id": f"ex:{tapp}-example", "@type": _TAPP_TYPE,
            "schema:name": f"Example {tapp}", **examples["MethodDefinition"]}
    overlays, registries, _ = e.build(tapp)
    schema = _selfcontained(overlays["MethodDefinition"], registries)
    print(f"=== {tapp}: path-driven example validated against path-driven schema ===")
    errs = sorted(jsonschema.Draft202012Validator(schema).iter_errors(inst),
                  key=lambda x: list(x.path))
    print(f"MethodDefinition instance: {len(inst)} top keys; schema $defs: {len(schema['$defs'])}")
    if errs:
        print(f"VALIDATION: {len(errs)} error(s)")
        for er in errs[:8]:
            print(f"  /{'/'.join(map(str, er.path))}: {er.message[:120]}")
        rc = 1
    else:
        print("VALIDATION: OK — example satisfies the path-driven schema")
        rc = 0
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"{tapp}.example.json"), "w", encoding="utf-8") as f:
            json.dump(inst, f, indent=2, ensure_ascii=False)
        print(f"wrote example to {out_dir}")
    return rc


# ---------- @type discriminators ----------
def _type_const(subschema):
    """The @type value a subschema demands, or None.

    Four shapes are in use across the base schemas: `const: [...]`; an array with
    `contains: {const: X}` (the CDIF person profile, and instrument additionalType); a `default`
    (the organization profile); and an `enum` of permitted tokens.
    """
    t = (subschema.get("properties") or {}).get("@type")
    if not isinstance(t, dict):
        return None
    if isinstance(t.get("const"), list):
        return list(t["const"])
    c = t.get("contains")
    if isinstance(c, dict) and isinstance(c.get("const"), str):
        return [c["const"]]
    if isinstance(t.get("default"), str):
        return [t["default"]]
    if isinstance(t.get("default"), list):
        return list(t["default"])
    items = t.get("items")
    if isinstance(items, dict):
        for cand in ([items] + list(items.get("anyOf") or [])):
            if isinstance(cand, dict) and isinstance(cand.get("enum"), list) and cand["enum"]:
                return [cand["enum"][0]]
    return None


def _declaring_branch(err, cand):
    """The subschema that both demanded @type and declares what it should be.

    A `required` error's own .schema is just {"required": [...]} — the keyword, not the branch. The
    branch is an ancestor. For an anyOf/oneOf/allOf the context error's schema_path is relative to
    that KEYWORD'S LIST, so the walk starts there, not at err.schema itself.
    """
    node = err.schema
    if isinstance(node, dict) and isinstance(node.get(err.validator), list):
        node = node[err.validator]
    best = None
    for step in list(cand.schema_path):
        if isinstance(node, dict) and "@type" in (node.get("properties") or {}):
            best = node
        try:
            node = node[step]
        except (KeyError, IndexError, TypeError):
            return best
    if isinstance(node, dict) and "@type" in (node.get("properties") or {}):
        best = node
    return best


def _at(inst, path):
    for step in path:
        try:
            inst = inst[step]
        except (KeyError, IndexError, TypeError):
            return None
    return inst


def fill_required_types(inst, resolved_schema, max_passes=6):
    """Supply @type where the schema requires one and the path-driven builder could not know it.

    A schema path names metadata fields, never @type — @type is structural. So any node whose base
    schema discriminates on it comes out incomplete: schema:creator emitted {schema:name} against a
    CDIF person/organization anyOf that requires @type, and every prov:used entry has the same
    shape. Rather than hard-code a table of node -> type, this is driven by the validator: each
    "'@type' is a required property" error names both the offending node and the branch that wanted
    it, so the fix is read off the schema itself and keeps working as the base schemas change.

    Mutates `inst` in place; returns how many nodes were filled. Iterates because filling one node
    can expose the next.
    """
    import jsonschema
    validator = jsonschema.Draft202012Validator(resolved_schema)
    filled = 0
    for _ in range(max_passes):
        added = 0
        for err in validator.iter_errors(inst):
            # an anyOf reports the real reason in .context, one entry per rejected branch
            for cand in ([err] + list(err.context or [])):
                if cand.validator != "required" or "'@type'" not in cand.message:
                    continue
                node = _at(inst, list(err.absolute_path) + list(cand.path))
                if not isinstance(node, dict) or "@type" in node:
                    continue
                branch = _declaring_branch(err, cand)
                t = _type_const(branch) if branch else None
                if t:
                    node["@type"] = t
                    added += 1
                    break
        filled += added
        if not added:
            break
    return filled


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    od = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--out=")), None)
    sys.exit(_self_test(args[0] if args else "laicpmsTAPP", out_dir=od))
