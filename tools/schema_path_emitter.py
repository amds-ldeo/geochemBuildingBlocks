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
def insert(root: Obj, parsed: spp.ParsedPath, leaf_schema, require=False):
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
                item = arr.branches.get(val)
                if item is None:
                    item = Obj(); item.props[key] = Leaf({"const": val})
                    arr.branches[val] = item
                if require:
                    arr.required.add(val)
                if is_last:
                    return                     # value IS the selected element (already keyed)
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
            branches = [to_schema(o) for o in node.branches.values()]
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


IS_INSTRUMENT = re.compile(r"schema:instrument\b")


def build(tapp):
    """Return {root -> JSON-Schema overlay object} for the CLEAN families of one TAPP."""
    meta = _load_rows(tapp)   # configures b.XLSX
    spec_path = os.path.join(ROOT, "docs", os.path.splitext(os.path.basename(b.XLSX))[0] + ".schemapaths.json")
    spec = json.load(open(spec_path, encoding="utf-8"))
    roots = {"MethodDefinition": Obj(), "Dataset": Obj()}
    skipped = []
    for item, rec in spec.items():
        path = rec["path"]
        if IS_INSTRUMENT.search(path):
            skipped.append(item); continue
        parsed = spp.parse(path)
        m = meta.get(item, {})
        # enum from Example/Allowed Content for controlled lists (best-effort, same rule as build_tapp)
        enum = None
        dl = (m.get("dt") or "").lower()
        if "controlled" in dl:
            parts = [p.strip().strip("'\"") for p in (m.get("ex") or "").split("|")
                     if p.strip() and not p.strip().lower().startswith("e.g") and "specify" not in p.strip().lower()]
            enum = parts or None
        leaf = leaf_for(m.get("desc"), m.get("dt"), enum)
        require = (m.get("P") == "Basic") or (m.get("A") == "Basic")
        insert(roots[parsed.root], parsed, leaf, require=require)
    return {r: to_schema(o) for r, o in roots.items()}, skipped


def _self_test(tapp="laicpmsTAPP"):
    import jsonschema
    overlays, skipped = build(tapp)
    print(f"=== {tapp}: path-driven CLEAN-family overlays ===")
    for root, sch in overlays.items():
        props = sch.get("properties", {})
        print(f"\n[{root}] {len(props)} top-level properties")
        try:
            jsonschema.Draft202012Validator.check_schema(sch)
            print("   check_schema: OK")
        except jsonschema.SchemaError as e:
            print(f"   check_schema: FAIL — {e.message}")
    print(f"\nskipped (instrument bucket): {len(skipped)}")
    # show the Dataset overlay (the new analysis-instance level) in full
    print("\n--- $Dataset overlay (analysis-instance level) ---")
    print(json.dumps(overlays["Dataset"], indent=2)[:2600])
    return 0


if __name__ == "__main__":
    sys.exit(_self_test(sys.argv[1] if len(sys.argv) > 1 else "laicpmsTAPP"))
