"""Phase 2/3 of the nested-interpreter work: EMITTER (schema side first).

Turns a set of parsed schema paths (Phase 1) + per-row workbook metadata into a nested JSON
Schema overlay, by folding every row into one tree via a generic MERGER. The merger is the
reusable keystone: Phase 3 (this file, schema leaves) and Phase 2 (example instance leaves)
share the same walk; only the leaf differs.

Intermediate representation (IR), built by insert(), serialized by to_schema():
    Obj  - an object node: {prop -> child}, plus recorded @type consts (for Phase 2)
    Arr  - an array node: selector branches {value -> Obj} and/or a bare-append item; the
           selector values that must be present become an allOf/contains constraint
    Leaf - a terminal: the JSON-Schema fragment for a scalar field (or scalar list item)

Scope: the CLEAN families (everything whose path does not descend into schema:instrument).
Instrument nesting is deferred until the 33 instrument canonical cells land.

    python tools/schema_path_emitter.py            # self-test: emit laicpms clean-family schema
    python tools/schema_path_emitter.py <tapp>     # e.g. laicpmsTAPP
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schema_path_parser as spp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------- intermediate representation ----------
class Obj:
    __slots__ = ("props", "types")

    def __init__(self):
        self.props = {}   # curie -> Obj | Arr | Leaf
        self.types = []   # @type consts asserted by UpperCamel segments (used by Phase 2)


class Arr:
    __slots__ = ("selkey", "branches", "append", "required")

    def __init__(self):
        self.selkey = None      # selector key curie, e.g. "schema:name"
        self.branches = {}      # selector value -> Obj (the item shape for that value)
        self.append = None      # Obj | Leaf for a bare "[]" append (no selector)
        self.required = set()   # selector values that must be present (=> contains)


class Leaf:
    __slots__ = ("schema",)

    def __init__(self, schema):
        self.schema = schema


# ---------- merger: fold one path into the tree ----------
def insert(root: Obj, parsed: spp.ParsedPath, leaf_schema=None, require=False, element=None):
    """Fold one path into the tree. `leaf_schema` sets a scalar terminal field; `element`
    (an Obj|Leaf) is placed as the selected array element when the path ends at a selector
    (used for registry-$ref additionalProperty entries)."""
    node = root
    segs = parsed.segments
    for i, seg in enumerate(segs):
        is_last = i == len(segs) - 1
        if seg.is_type:                       # UpperCamel: @type of the current object, not a nav
            if isinstance(node, Obj) and seg.prop not in node.types:
                node.types.append(seg.prop)
            continue
        curie = seg.prop
        if seg.is_array or seg.selector:      # array container (selected element or append)
            arr = node.props.get(curie)
            if not isinstance(arr, Arr):
                arr = Arr(); node.props[curie] = arr
            if seg.selector:
                key, val = seg.selector
                arr.selkey = key
                if require:
                    arr.required.add(val)
                if is_last:
                    if element is not None:
                        arr.branches[val] = element     # provided element (e.g. a $ref Leaf)
                    elif val not in arr.branches:
                        o = Obj(); o.props[key] = Leaf({"const": val}); arr.branches[val] = o
                    return                     # value IS the selected element
                item = arr.branches.get(val)
                if item is None:
                    item = Obj(); item.props[key] = Leaf({"const": val})
                    arr.branches[val] = item
                node = item
            else:                              # bare "[]"
                if is_last:
                    arr.append = Leaf(leaf_schema) if leaf_schema is not None else Obj()
                    return
                if not isinstance(arr.append, Obj):
                    arr.append = Obj()
                node = arr.append
        else:                                  # plain property
            if is_last:
                existing = node.props.get(curie)
                if (isinstance(existing, Leaf) and isinstance(existing.schema, dict)
                        and "const" in existing.schema):
                    # collision with a selector const (e.g. an instrument's schema:additionalType,
                    # which is array-valued): model as an array whose items match this row and that
                    # CONTAINS the selector value — keeps the selector meaning + the row's value.
                    node.props[curie] = Leaf({"type": "array", "items": leaf_schema or {"type": "string"},
                                              "allOf": [{"contains": existing.schema}]})
                else:
                    node.props[curie] = Leaf(leaf_schema)
                return
            child = node.props.get(curie)
            if not isinstance(child, Obj):
                child = Obj(); node.props[curie] = child
            node = child


# ---------- serialize IR -> JSON Schema ----------
def to_schema(node):
    if isinstance(node, Leaf):
        return node.schema
    if isinstance(node, Obj):
        return {"type": "object",
                "properties": {k: to_schema(v) for k, v in node.props.items()}}
    if isinstance(node, Arr):
        if node.branches:
            vals = list(node.branches.values())
            if all(isinstance(v, Leaf) for v in vals):
                # registry-$ref elements (schema:additionalProperty): anyOf of the refs, each
                # optional-and-at-most-one via allOf/contains (mirrors build_tapp's overlay).
                refs = [v.schema for v in vals]
                return {"type": "array",
                        "items": {"anyOf": refs} if len(refs) > 1 else refs[0],
                        "allOf": [{"contains": r, "minContains": 0, "maxContains": 1} for r in refs]}
            branches = [to_schema(o) for o in vals]
            out = {"type": "array",
                   "items": {"anyOf": branches} if len(branches) > 1 else branches[0]}
            if node.required:
                out["allOf"] = [{"contains": {"properties": {node.selkey: {"const": v}},
                                              "required": [node.selkey]}}
                                for v in sorted(node.required)]
            return out
        if isinstance(node.append, Leaf):
            return {"type": "array", "items": node.append.schema}
        if isinstance(node.append, Obj):
            return {"type": "array", "items": to_schema(node.append)}
        return {"type": "array"}
    raise TypeError(node)


# ---------- leaf schema from workbook Data Type ----------
def leaf_for(desc, dtype, enum=None, default=None):
    dl = (dtype or "").lower()
    if enum:
        s = {"type": "string", "enum": enum}
    elif dl.startswith("bool"):
        s = {"type": "boolean"}
    elif "integer" in dl:
        s = {"anyOf": [{"type": "integer"}, {"type": "string"}]}
    elif "numeric" in dl or "number" in dl:
        s = {"anyOf": [{"type": "number"}, {"type": "string"}]}
    else:
        s = {"type": "string"}
    if desc:
        s = {"description": desc, **s}
    if default is not None:
        s["default"] = default
    return s


# ---------- drive from a workbook + its schemapaths.json ----------
def _load_rows(tapp):
    """{item -> {desc, P, A, dtype}} from the workbook (mirrors build_tapp column detection)."""
    import openpyxl
    b.configure(tapp)
    ws = openpyxl.load_workbook(b.XLSX, data_only=True, read_only=True)["TAPP"]
    rows = list(ws.iter_rows(values_only=True))
    H = [b.norm(v).lower() for v in rows[0]]
    ci = {"P": next((i for i, v in enumerate(H) if v.startswith("protocol")), None),
          "A": next((i for i, v in enumerate(H) if v.startswith("analysis")), None),
          "dt": next((i for i, v in enumerate(H) if v == "data type"), None),
          "ex": next((i for i, v in enumerate(H) if v.startswith("example")), None)}
    out = {}
    for r in rows[1:]:
        item = b.norm(r[0])
        if not item or re.match(r"^\d+\.\s", item):
            continue
        g = lambda k: b.norm(r[ci[k]]) if ci[k] is not None and ci[k] < len(r) else ""
        out[item] = {"desc": b.norm(r[1]), "P": g("P"), "A": g("A"), "dt": g("dt"), "ex": g("ex")}
    return out


# registry-ref path prefix per artifact root (from the artifact's own directory)
_REG_PREFIX = {"MethodDefinition": "..", "Dataset": "../../techniqueProtocols"}


def _is_addl_param(p: spp.ParsedPath) -> bool:
    """True for a `…schema:additionalProperty[schema:name='X'].schema:(value|defaultValue)` path —
    an ADA method/analysis parameter that resolves to a registry PropertyValue(Spec) $ref."""
    s = p.segments
    return (len(s) >= 2 and not s[-1].is_array and s[-1].selector is None
            and s[-1].prop in ("schema:value", "schema:defaultValue")
            and s[-2].prop == "schema:additionalProperty" and s[-2].selector is not None)


def build(tapp):
    """Return ({root -> JSON-Schema overlay}, {registry -> {$defs}}) for one TAPP, driven entirely
    by its canonical schema paths — including instrument nesting. additionalProperty parameters
    (at any depth) resolve to registry PropertyValue / PropertyValueSpecification $defs (reusing
    build_tapp), referenced by $ref from the overlay."""
    meta = _load_rows(tapp)   # configures b.XLSX / PARAM_BASE
    sidecar = b.load_sidecar()
    spec_path = os.path.join(ROOT, "docs", os.path.splitext(os.path.basename(b.XLSX))[0] + ".schemapaths.json")
    spec = json.load(open(spec_path, encoding="utf-8"))
    roots = {"MethodDefinition": Obj(), "Dataset": Obj()}
    registries = {"parameterTemplates": {}, "parameterValues": {}}
    required = {"MethodDefinition": [], "Dataset": []}
    pt_seen, pv_seen = set(), set()
    for item, rec in spec.items():
        path = rec["path"]
        parsed = spp.parse(path)
        m = meta.get(item, {})
        require = (m.get("P") == "Basic") or (m.get("A") == "Basic")
        non_type = [s for s in parsed.segments if not s.is_type]
        if require and len(non_type) == 1 and non_type[0].selector is None and not non_type[0].is_array:
            if non_type[0].prop not in required[parsed.root]:   # top-level direct prop, Basic tier
                required[parsed.root].append(non_type[0].prop)
        if _is_addl_param(parsed):
            bd = {"item": item, "name": (sidecar.get(item, {}).get("name") or b.camel(item)),
                  "jtype": b.jtype(m.get("dt", "")), "unit": b.unit(m.get("dt", "")),
                  "desc": m.get("desc", ""), "A": m.get("A", "")}
            if parsed.segments[-1].prop == "schema:defaultValue":
                name, body = b.param_template_def(bd, pt_seen)
                registries["parameterTemplates"].update(body); pt_seen.add(name)
                ref = {"$ref": f"{_REG_PREFIX[parsed.root]}/parameterTemplates/schema.yaml#/$defs/{name}"}
            else:
                name, body = b.param_value_def(bd, pv_seen)
                registries["parameterValues"].update(body); pv_seen.add(name)
                ref = {"$ref": f"{_REG_PREFIX[parsed.root]}/parameterValues/schema.yaml#/$defs/{name}"}
            truncated = spp.ParsedPath(parsed.root, parsed.segments[:-1])
            insert(roots[parsed.root], truncated, element=Leaf(ref), require=require)
            continue
        enum = None
        dl = (m.get("dt") or "").lower()
        if "controlled" in dl:
            parts = [p.strip().strip("'\"") for p in (m.get("ex") or "").split("|")
                     if p.strip() and not p.strip().lower().startswith("e.g") and "specify" not in p.strip().lower()]
            enum = parts or None
        insert(roots[parsed.root], parsed, leaf_for(m.get("desc"), m.get("dt"), enum), require=require)
    return {r: to_schema(o) for r, o in roots.items()}, registries, required


# base building block each overlay extends via allOf (relative to the artifact's own dir)
_BASE_REF = {"MethodDefinition": "../tappDefinition/schema.yaml",
             "Dataset": "../../adaProfiles/adaProduct/schema.yaml"}


def wrap(root, overlay, required, title=None, description=None):
    """Wrap an overlay as a full artifact schema: allOf[{$ref base}, {overlay + required}]."""
    inner = {"type": "object", "properties": overlay.get("properties", {})}
    if required:
        inner["required"] = required
    out = {"$schema": "https://json-schema.org/draft/2020-12/schema"}
    if title:
        out["title"] = title
    if description:
        out["description"] = description
    out["allOf"] = [{"$ref": _BASE_REF[root]}, inner]
    return out


def full_tapp(tapp):
    """Assemble the complete path-driven TAPP artifact: wrapped schema + registries + Dataset overlay."""
    overlays, registries, required = build(tapp)
    tapp_schema = wrap("MethodDefinition", overlays["MethodDefinition"], required["MethodDefinition"],
                       title=b.CFG.get("title"), description=b.CFG.get("description"))
    return tapp_schema, registries, overlays["Dataset"]


def _ref_names(node, acc):
    if isinstance(node, dict):
        r = node.get("$ref", "")
        m = re.search(r"/(parameterTemplates|parameterValues)/schema\.yaml#/\$defs/(.+)$", r)
        if m:
            acc.setdefault(m.group(1), set()).add(m.group(2))
        for v in node.values():
            _ref_names(v, acc)
    elif isinstance(node, list):
        for v in node:
            _ref_names(v, acc)
    return acc


def _shipped_top_props(tapp):
    import yaml
    p = os.path.join(b.TAPP_DIR, "schema.yaml")
    d = yaml.safe_load(open(p, encoding="utf-8"))
    for blk in d.get("allOf", []):
        if isinstance(blk, dict) and blk.get("type") == "object":
            return set((blk.get("properties") or {}).keys())
    return set()


def _self_test(tapp="laicpmsTAPP", out_dir=None):
    import jsonschema
    tapp_schema, registries, dataset_overlay = full_tapp(tapp)
    print(f"=== {tapp}: path-driven TAPP artifact (base allOf-wrapped) ===")
    # 1. structural validity
    try:
        jsonschema.Draft202012Validator.check_schema(tapp_schema)
        print("check_schema (wrapped TAPP): OK")
    except jsonschema.SchemaError as e:
        print(f"check_schema: FAIL — {e.message}"); return 1
    # 2. $ref consistency: every registry $ref must resolve to a generated $def
    used = _ref_names(tapp_schema, {})
    dangling = {reg: sorted(names - set(registries[reg])) for reg, names in used.items()
                if names - set(registries[reg])}
    print("$ref consistency:", "OK (every ref has a generated $def)" if not dangling else f"DANGLING {dangling}")
    overlay_props = tapp_schema["allOf"][1]["properties"]
    print(f"TAPP overlay: {len(overlay_props)} props, {len(tapp_schema['allOf'][1].get('required', []))} required; "
          f"registries: {len(registries['parameterTemplates'])} templates + {len(registries['parameterValues'])} values; "
          f"Dataset overlay (for detail rework): {len(dataset_overlay.get('properties', {}))} props")
    # 3. diff vs the shipped (tier-matrix) schema
    shipped = _shipped_top_props(tapp)
    gen = set(overlay_props)
    print(f"\n--- top-level property diff vs shipped {tapp}/schema.yaml ---")
    print(f"  added by path-driven ({len(gen - shipped)}): {sorted(gen - shipped)[:12]}")
    print(f"  gone from shipped   ({len(shipped - gen)}): {sorted(shipped - gen)[:12]}")
    print(f"  unchanged           ({len(gen & shipped)})")
    # 4. write the generated artifact to a sandbox for inspection (non-destructive)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"{tapp}.schema.json"), "w", encoding="utf-8") as f:
            json.dump(tapp_schema, f, indent=2, ensure_ascii=False)
        with open(os.path.join(out_dir, f"{tapp}.registries.json"), "w", encoding="utf-8") as f:
            json.dump(registries, f, indent=2, ensure_ascii=False)
        print(f"\nwrote generated artifact to {out_dir}")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    od = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--out=")), None)
    sys.exit(_self_test(args[0] if args else "laicpmsTAPP", out_dir=od))
