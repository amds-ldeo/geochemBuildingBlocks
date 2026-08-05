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


# keys whose value is always a JSON array (schema.org additionalType on a Thing). A selector on
# such a key is modeled uniformly as an array that CONTAINS the token — never a scalar const — so
# selector branches and any terminal on the same key compose (e.g. instrument ICP-MS Type appends).
ARRAY_VALUED = {"schema:additionalType", "@type"}

# schema.org / PROV properties whose value is always a JSON array. A plain nav into one yields an
# array-of-objects container; a bare terminal on one asserts array cardinality without constraining
# the item shape (adaProduct owns it). Selector-keyed arrays (contributor, additionalProperty, …)
# are handled separately via branches.
KNOWN_ARRAY = {"prov:wasGeneratedBy", "schema:measurementTechnique", "schema:funding"}

# base-owned array properties whose items are rich objects defined in tappDefinition
# (ComputationalTool, AnalyteColumn). A bare "[]" append leaves items as {type:object} so the
# base's object shape applies instead of a spurious string-item constraint from the path leaf.
BASE_OWNED_OBJECT_ARRAY = {"bios:computationalTool", "ada:analyteColumns"}


class AddlType:
    """An array-valued key (schema:additionalType): required selector token(s) + an optional finer
    terminal value. to_schema -> array whose items are the token consts (+ terminal leaf) and that
    CONTAINS each token; to_instance -> the list of tokens (+ terminal value)."""
    __slots__ = ("consts", "item_leaf")

    def __init__(self, const_val):
        self.consts = [const_val]
        self.item_leaf = None       # mode-specific (schema fragment | placeholder value) or None


def _sel_key_node(key, val):
    return AddlType(val) if key in ARRAY_VALUED else Leaf({"const": val})


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
                        o = Obj(); o.props[key] = _sel_key_node(key, val); arr.branches[val] = o
                    return                     # value IS the selected element
                item = arr.branches.get(val)
                if item is None:
                    item = Obj(); item.props[key] = _sel_key_node(key, val)
                    arr.branches[val] = item
                node = item
            else:                              # bare "[]"
                if is_last:
                    if curie in BASE_OWNED_OBJECT_ARRAY:
                        arr.append = Obj()     # base-owned object array -> items:{object}, defer shape to base
                    else:
                        arr.append = Leaf(leaf_schema) if leaf_schema is not None else Obj()
                    return
                if not isinstance(arr.append, Obj):
                    arr.append = Obj()
                node = arr.append
        else:                                  # plain property
            if is_last:
                existing = node.props.get(curie)
                if isinstance(existing, AddlType):
                    # a terminal on an array-valued key (e.g. instrument ICP-MS Type) -> a finer
                    # value appended alongside the selector token(s).
                    existing.item_leaf = leaf_schema
                elif curie in KNOWN_ARRAY:
                    node.props[curie] = Arr()   # assert array cardinality only (base owns the shape)
                else:
                    node.props[curie] = Leaf(leaf_schema)
                return
            if curie in KNOWN_ARRAY:            # nav into an always-array property -> array of objects
                arr = node.props.get(curie)
                if not isinstance(arr, Arr):
                    arr = Arr(); node.props[curie] = arr
                if not isinstance(arr.append, Obj):
                    arr.append = Obj()
                node = arr.append
            else:
                child = node.props.get(curie)
                if not isinstance(child, Obj):
                    child = Obj(); node.props[curie] = child
                node = child


# ---------- serialize IR -> JSON Schema ----------
def to_schema(node):
    if isinstance(node, Leaf):
        return node.schema
    if isinstance(node, AddlType):
        opts = [{"const": c} for c in node.consts] + ([node.item_leaf] if node.item_leaf else [{"type": "string"}])
        return {"type": "array",
                "items": {"anyOf": opts} if len(opts) > 1 else opts[0],
                "allOf": [{"contains": {"const": c}} for c in node.consts]}
    if isinstance(node, Obj):
        return {"type": "object",
                "properties": {k: to_schema(v) for k, v in node.props.items()}}
    if isinstance(node, Arr):
        if node.branches:
            vals = list(node.branches.values())
            # items: strict anyOf of the registry $ref branches; but if any branch is an object
            # (e.g. schema:contributor selected by roleName), keep items OPEN so other members
            # (a principalInvestigator contributor, extra additionalProperty entries) are allowed.
            if all(isinstance(v, Leaf) for v in vals):
                items = {"anyOf": [v.schema for v in vals]} if len(vals) > 1 else vals[0].schema
            else:
                items = {"type": "object"}
            out = {"type": "array", "items": items}
            # per-branch presence: a $ref branch is optional-and-at-most-one; a required object
            # branch must be CONTAINED (selector key = the token/name).
            allof = []
            arr_key = node.selkey in ARRAY_VALUED
            for val, br in node.branches.items():
                if isinstance(br, Leaf):
                    allof.append({"contains": br.schema, "minContains": 0, "maxContains": 1})
                elif val in node.required:
                    key_c = {"contains": {"const": val}} if arr_key else {"const": val}
                    allof.append({"contains": {"properties": {node.selkey: key_c},
                                               "required": [node.selkey]}})
            if allof:
                out["allOf"] = allof
            return out
        if isinstance(node.append, Leaf):
            return {"type": "array", "items": node.append.schema}
        if isinstance(node.append, Obj):
            return {"type": "array", "items": to_schema(node.append)}
        return {"type": "array"}
    raise TypeError(node)


# ---------- serialize IR -> JSON-LD instance (Phase 2, same merger) ----------
def to_instance(node):
    if isinstance(node, Leaf):
        s = node.schema
        if isinstance(s, dict) and set(s.keys()) == {"const"}:   # a selector key -> its literal value
            return s["const"]
        return s                                                  # a placeholder value or built element
    if isinstance(node, AddlType):                               # array-valued key: [tokens, +row value]
        return list(node.consts) + ([node.item_leaf] if node.item_leaf is not None else [])
    if isinstance(node, Obj):
        out = {}
        if node.types:
            out["@type"] = list(node.types)
        for k, v in node.props.items():
            out[k] = to_instance(v)
        return out
    if isinstance(node, Arr):
        if node.branches:
            return [to_instance(v) for v in node.branches.values()]
        if node.append is not None:
            return [to_instance(node.append)]
        return []
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
_REG_PREFIX = {"MethodDefinition": "../../../registry", "Dataset": "../../../registry"}


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
    import schemapath_io
    spec = schemapath_io.load_spec(schemapath_io.csv_path(b.XLSX))
    roots = {"MethodDefinition": Obj(), "Dataset": Obj()}
    registries = {"parameterTemplates": {}, "parameterValues": {}}
    required = {"MethodDefinition": [], "Dataset": []}
    pt_seen, pv_seen = set(), set()
    for item, rec in spec.items():
        m = meta.get(item, {})
        paths = rec["path"] if isinstance(rec["path"], list) else [rec["path"]]
        for path in paths:   # usually 1; 2 for a dual-homed editable param (TAPP default + detail value)
            parsed = spp.parse(path)
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
_BASE_REF = {"MethodDefinition": "../../../BaseSchema/tappDefinition/schema.yaml",
             "Dataset": "../../../BaseSchema/adaProduct/schema.yaml"}


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
