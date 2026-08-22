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
import tapp_source
import schema_path_parser as spp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------- intermediate representation ----------
class Obj:
    __slots__ = ("props", "types")

    def __init__(self):
        self.props = {}   # curie -> Obj | Arr | Leaf
        self.types = []   # @type consts asserted by UpperCamel segments (used by Phase 2)


class Arr:
    __slots__ = ("selkey", "branches", "append", "required", "extra_items")

    def __init__(self):
        self.selkey = None      # selector key curie, e.g. "schema:name"
        self.branches = {}      # (selector key, value) -> Obj — keyed by BOTH so one array can
                                # hold items discriminated by different keys (see insert())
        self.append = None      # Obj | Leaf for a bare "[]" append (no selector)
        self.required = set()   # selector values that must be present (=> contains)
        self.extra_items = []   # item schemas permitted alongside the branches, but not `contains`ed
                                # (the base's analyte-identifier column)


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

# prov:used is an array of role-keyed WRAPPERS (CDIF 2026-08): each item carries exactly one of
# these keys, and the value is an array of entities. The item is discriminated by which key is
# PRESENT, not by a selector value, so these branches need their own marker -- `_WRAPPER` -- to
# tell to_schema to emit `if required:[key] then properties:{key: …}` rather than the
# `if key == value` form every other branch uses.

PROV_USED = "prov:used"
WRAPPER_KEYS = {"schema:instrument", "bios:computationalTool", "prov:reagent"}
_WRAPPER = "\0wrapper"

# Roles that discriminate members of an OPTIONAL collection. bios:computationalTool and
# bios:reagent are optional -- a TAPP need not own software or reference materials -- so a
# required row selecting on one of these means "record the role of what you list", never "you
# must possess one of these". The role itself is required on each member that IS listed.
ROLE_KEYS = {"ada:toolRole", "ada:reagentRole"}

# What each wrapper's entities ARE. Referencing the base rather than restating its shape keeps one
# definition of an instrument / tool / reagent, and it is what makes the generated examples usable:
# the example emitter supplies @type where a schema REQUIRES one, so without these refs a detail
# block demands nothing and the entities come out untyped.
WRAPPER_ITEM_REF = {
    "schema:instrument": "../../../../BaseSchema/instrument/schema.yaml",
    # Reference the tool/reagent shapes at their home in the generic geochemProduct base, NOT
    # through the adaProduct alias: the technique detail is a geochem artifact and must not depend
    # on the ADA-specific product layer. (The adaProduct alias also mis-resolves as a cross-file
    # $ref-of-a-$ref — it inlines the whole product schema, leaking @type [Dataset,Product] onto the
    # tool/reagent — whereas the direct geochemProduct fragment resolves to the correct shape.)
    "bios:computationalTool": "../../../../BaseSchema/geochemProduct/schema.yaml#/$defs/UsedComputationalTool",
    "prov:reagent": "../../../../BaseSchema/geochemProduct/schema.yaml#/$defs/UsedReagent",
}

# base-owned array properties whose items are rich objects defined in tappDefinition
# (ComputationalTool). A bare "[]" append leaves items as {type:object} so the base's object shape
# applies instead of a spurious string-item constraint from the path leaf.
#
# ada:analyteColumns used to be listed here too, which silently dropped every technique's analyte
# columns. Each such row ends at "…ada:analyteColumns[]" carrying a SCALAR Data Type (the column's
# value type), so falling through to Leaf(leaf_schema) would emit items:{type:string} — wrong,
# since items are AnalyteColumn objects — and with every row writing the same append, last-one-wins.
# It is now handled by ANALYTE_COLUMN_ARRAY below, which turns each row into a generated column def
# rather than consuming the row's leaf.
BASE_OWNED_OBJECT_ARRAY = {"bios:computationalTool"}

# ada:defaultAnalytes (and the analogous ada:defaultChannels) hold the template's DEFAULT ROWS: a
# list of analyte/channel identifiers, each a bare string OR a schema:DefinedTerm — never an object
# carrying per-column values (those live in the columns array). Whether the sidecar row targets the
# property directly or with a bare "[]", the array's item shape is this anyOf, not the row's scalar.
DEFAULT_ROW_ARRAYS = {"ada:defaultAnalytes", "ada:defaultChannels"}
DEFAULT_ROW_ITEMS = {"anyOf": [{"type": "string"},
                               {"$ref": "../../../../BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm"}]}

# The per-analyte column array. Each row targeting it names one column; the emitter generates a
# column def per row and narrows the array to those columns plus the base's identifier column.
ANALYTE_COLUMN_ARRAY = "ada:analyteColumns"

# tappDefinition's mandatory analyte-identifier column, which must stay permissible once the
# overlay narrows `items` to the technique's own columns.
ANALYTE_IDENTIFIER_REF = {
    "$ref": "../../../../BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn"
}

# Keyed tables: one row per member of a domain, one column per field whose value repeats over it
# (the TAPP workbook's `Keyed By` column). Every domain has the same three parts — a template
# object, a columns array, and a base-owned identifier column that must stay permissible once the
# overlay narrows `items` to the technique's own columns. Only the names differ, so they are
# table-driven rather than special-cased per domain.
KEYED_TABLES = {
    "ada:analyteColumns": {
        "template": "ada:analyteTemplate",
        "registry": "analyteColumns",
        "identifier_ref": ANALYTE_IDENTIFIER_REF,
    },
    "ada:channelColumns": {
        "template": "ada:channelTemplate",
        "registry": "channelColumns",
        "identifier_ref": {
            "$ref": "../../../../BaseSchema/tappDefinition/schema.yaml"
                    "#/$defs/ChannelIdentifierColumn"
        },
    },
    "ada:reportedPropertyColumns": {
        "template": "ada:reportedPropertyTemplate",
        "registry": "reportedPropertyColumns",
        "identifier_ref": {
            "$ref": "../../../../BaseSchema/tappDefinition/schema.yaml"
                    "#/$defs/ReportedPropertyIdentifierColumn"
        },
    },
    # An MC-ICP-MS collector: ada:collectorConfiguration IS the channel-column array directly (it
    # lives on instrument[ICPMS].hasPart[Collector], not in a top-level template, and has no
    # identifier column). Channel column @ids use the ada:channelColumn namespace.
    "ada:collectorConfiguration": {
        "template": None,
        "registry": "channelColumns",
        "identifier_ref": None,
    },
}


def normalize_path(p):
    """Collapse the collectorConfiguration channel table to its emitted shape.

    The sidecar addresses MC-ICP-MS channels as `…collectorConfiguration.ada:channelColumns[]` and
    the default channel list as `…collectorConfiguration.ada:defaultChannels[]`, but the emitted
    structure is `ada:collectorConfiguration` = the channel-column array itself, with
    `ada:defaultChannels` a SIBLING of it on the Collector (an array cannot also hold a
    defaultChannels key). Rewrite both so schema and example agree without touching the sidecar.

    Also collapse a trailing `[]` on a default-ROW array (ada:defaultAnalytes[]/ada:defaultChannels[]):
    the emitter carries the transcribed member list as a single scalar leaf on the template (the way
    the reference LA-MC-ICPMS sidecar addresses it — no brackets), whereas the array-segment form
    routes into the append leaf and would emit the raw items schema instead of the members. The
    schema side keys off the property NAME, so both grammars still emit the same array constraint."""
    return (p.replace(".ada:collectorConfiguration.ada:channelColumns", ".ada:collectorConfiguration")
             .replace(".ada:collectorConfiguration.ada:defaultChannels", ".ada:defaultChannels")
             .replace(".ada:defaultAnalytes[]", ".ada:defaultAnalytes")
             .replace(".ada:defaultChannels[]", ".ada:defaultChannels"))


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
def insert(root: Obj, parsed: spp.ParsedPath, leaf_schema=None, require=False, element=None,
           branch_key=None):
    """Fold one path into the tree. `leaf_schema` sets a scalar terminal field; `element`
    (an Obj|Leaf) is placed as the selected array element when the path ends at a selector
    (used for registry-$ref additionalProperty entries). `branch_key` places `element` as a
    named branch of a bare "[]" array — the analyte-column case, where the array has no
    selector but each row still contributes one distinct permitted item."""
    node = root
    segs = parsed.segments
    for i, seg in enumerate(segs):
        is_last = i == len(segs) - 1
        if seg.is_type:                       # UpperCamel: @type of the current object, not a nav
            if isinstance(node, Obj) and seg.prop not in node.types:
                node.types.append(seg.prop)
            continue
        curie = seg.prop
        # prov:used -> one wrapper item per role key, so an instrument, a tool and a reagent are
        # three separate items rather than three keys on one item.
        if (curie == PROV_USED and not is_last
                and segs[i + 1].prop in WRAPPER_KEYS and not segs[i + 1].is_type):
            arr = node.props.get(curie)
            if not isinstance(arr, Arr):
                arr = Arr(); node.props[curie] = arr
            wrapper_key = segs[i + 1].prop
            branch = arr.branches.get((_WRAPPER, wrapper_key))
            if not isinstance(branch, Obj):
                branch = Obj(); arr.branches[(_WRAPPER, wrapper_key)] = branch
            node = branch
            continue
        if seg.is_array or seg.selector:      # array container (selected element or append)
            arr = node.props.get(curie)
            if not isinstance(arr, Arr):
                arr = Arr(); node.props[curie] = arr
            if seg.selector:
                key, val = seg.selector
                # Branches are keyed by (selector key, value), not value alone: ONE array can hold
                # elements discriminated by DIFFERENT keys. prov:used is the case that forced this —
                # its items are instruments (schema:additionalType), computational tools
                # (ada:toolRole) or reagents (ada:reagentRole). A single Arr.selkey made the last
                # path win, so every branch was emitted against the wrong key.
                arr.selkey = key                        # last key seen; kept for bare-append callers
                if require and key not in ROLE_KEYS:
                    arr.required.add((key, val))
                if is_last:
                    if element is not None:
                        arr.branches[(key, val)] = element   # provided element (e.g. a $ref Leaf)
                    elif (key, val) not in arr.branches:
                        o = Obj(); o.props[key] = _sel_key_node(key, val)
                        arr.branches[(key, val)] = o
                    return                     # value IS the selected element
                item = arr.branches.get((key, val))
                if item is None:
                    item = Obj(); item.props[key] = _sel_key_node(key, val)
                    arr.branches[(key, val)] = item
                node = item
            else:                              # bare "[]"
                if is_last:
                    if branch_key is not None and element is not None:
                        # one named permitted item (analyte column) rather than an item-shape leaf
                        arr.branches[(None, branch_key)] = element
                    elif curie in DEFAULT_ROW_ARRAYS:
                        arr.append = Leaf(DEFAULT_ROW_ITEMS)   # string | DefinedTerm rows
                    elif curie in BASE_OWNED_OBJECT_ARRAY:
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


def _jsonld_card(sch):
    """A scalar-typed property in JSON-LD may appear as the value OR an array of it. When
    materializing a nested leaf as a constraint, tolerate both so real instances (e.g.
    schema:identifier as ['igsn:...']) validate. Non-scalar schemas pass through unchanged."""
    if isinstance(sch, dict) and sch.get("type") in ("string", "integer", "number", "boolean"):
        desc = sch.get("description")
        base = {k: v for k, v in sch.items() if k != "description"}
        out = {"anyOf": [base, {"type": "array", "items": base}]}
        return {"description": desc, **out} if desc else out
    return sch


# A dataset variable that is not one of the TAPP's declared reported properties: any object typed
# as a CDIF instance variable or a schema:PropertyValue. Kept deliberately loose - the surrounding
# base schema already constrains the variable's shape; this branch only has to stop the overlay's
# anyOf from excluding genuine variables.
CDI_VARIABLE = "cdi:InstanceVariable"

GENERIC_VARIABLE = {
    "title": "Dataset variable",
    "description": ("A measured variable of this dataset that is not one of the procedure's declared "
                    "reported properties. schema:variableMeasured carries the dataset's actual "
                    "variables; the reported-property branches above are permitted members of it, "
                    "not the whole of it."),
    "type": "object",
    "required": ["@type"],
    "properties": {"@type": {"type": "array",
                             "contains": {"enum": ["cdi:InstanceVariable", "schema:PropertyValue"]}}},
}


def _vm_array(root, truncated):
    """The Arr node the reported-property branch was just inserted into."""
    node = root
    for seg in truncated.segments:
        if seg.is_type or not isinstance(node, (Obj, Arr)):
            continue
        node = node.props.get(seg.prop) if isinstance(node, Obj) else None
        if node is None:
            return None
    return node


_TERM_SCHEME_CACHE = {}


def _term_scheme(consts):
    """The ada:vocab ConceptScheme a set of selector tokens belongs to, or None.

    The selector token on schema:additionalType is now a controlled term (see
    tools/build_instrument_codelist.py): the instrument-type and instrument-component-type schemes
    are generated from these very sidecars. Annotating the emitted constraint with
    schema:inDefinedTermSet is the convention this repo already uses for componentType - the
    vocabulary is discoverable and SHACL-checkable without hard-enumerating it in JSON Schema.

    The two schemes are disjoint, so the scheme is identified from the token itself and no extra
    context has to be threaded through the tree builder. @type tokens (prov:Plan, ...) match neither
    and are left unannotated.
    """
    if not _TERM_SCHEME_CACHE:
        import json as _json
        for fn, sid in (("adaInstrumentType.json", "ada:vocab/instrumentType"),
                        ("adaInstrumentComponentType.json", "ada:vocab/instrumentComponentType")):
            f = os.path.join(ROOT, "_sources", "registry", "vocab", fn)
            try:
                doc = _json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            for c in doc.get("skos:hasTopConcept") or []:
                n = c.get("skos:notation")
                if n:
                    _TERM_SCHEME_CACHE[n] = sid
    found = {_TERM_SCHEME_CACHE.get(c) for c in consts}
    found.discard(None)
    return found.pop() if len(found) == 1 else None


# ---------- serialize IR -> JSON Schema ----------
def to_schema(node):
    if isinstance(node, Leaf):
        return node.schema
    if isinstance(node, AddlType):
        opts = [{"const": c} for c in node.consts] + ([node.item_leaf] if node.item_leaf else [{"type": "string"}])
        out = {"type": "array",
               "items": {"anyOf": opts} if len(opts) > 1 else opts[0],
               "allOf": [{"contains": {"const": c}} for c in node.consts]}
        scheme = _term_scheme(node.consts)
        if scheme:
            out["schema:inDefinedTermSet"] = scheme
        return out
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
                opts = list(node.extra_items) + [v.schema for v in vals]
                items = {"anyOf": opts} if len(opts) > 1 else opts[0]
            else:
                # MATERIALIZE nested structure: for each object branch that carries content beyond its
                # selector (e.g. schema:instrument[ICPMS] -> hasPart[ICP Source] -> additionalProperty),
                # emit `if <member matches this selector> then <the branch's nested properties>`. The
                # nested props are OPTIONAL (no `required`), so the array stays open and a minimal
                # instance that omits the tree still validates — while an instance that DOES carry an
                # ICPMS instrument has its hasPart/additionalProperty shape enforced (recursively).
                cond = []
                for (skey, val), br in node.branches.items():
                    if not isinstance(br, Obj):
                        continue
                    if skey == _WRAPPER:
                        # a role-keyed wrapper: discriminate on the key being present
                        inner = br.props.get(val)
                        if inner is not None:
                            sch = to_schema(inner)
                            ref = WRAPPER_ITEM_REF.get(val)
                            if ref and isinstance(sch.get("items"), dict):
                                sch["items"] = {"allOf": [{"$ref": ref}, sch["items"]]}
                            cond.append({"if": {"required": [val]},
                                         "then": {"properties": {val: sch}}})
                        continue
                    skey = skey or node.selkey
                    nested = {k: _jsonld_card(to_schema(v)) for k, v in br.props.items() if k != skey}
                    if nested:
                        sel = {"contains": {"const": val}} if skey in ARRAY_VALUED else {"const": val}
                        # the discriminating token is a controlled term (instrument type /
                        # instrument component type); annotate the scheme it comes from, the way
                        # componentType is annotated, so the vocabulary behind the const is
                        # discoverable rather than an undocumented magic string.
                        _sch = _term_scheme([val])
                        if _sch:
                            sel = dict(sel, **{"schema:inDefinedTermSet": _sch})
                        cond.append({"if": {"properties": {skey: sel}, "required": [skey]},
                                     "then": {"properties": nested}})
                items = {"type": "object", "allOf": cond} if cond else {"type": "object"}
                # bios:computationalTool and bios:reagent are optional collections -- a TAPP need
                # not own software or reference materials in every role the workbook enumerates.
                # What is NOT optional is saying which role a member plays, so the discriminator is
                # required per item instead of each role being required to exist. (The role's value
                # is held to the enum by tappDefinition / adaProduct.)
                skeys = {sk for sk, _ in node.branches if sk != _WRAPPER}
                if len(skeys) == 1 and next(iter(skeys)) in ROLE_KEYS:
                    items["required"] = [next(iter(skeys))]
            out = {"type": "array", "items": items}
            # per-branch presence: a $ref branch is optional-and-at-most-one; a required object
            # branch must be CONTAINED (selector key = the token/name).
            allof = []
            for (skey, val), br in node.branches.items():
                if skey == _WRAPPER:
                    if (skey, val) in node.required:
                        allof.append({"contains": {"required": [val]}})
                    continue
                skey = skey or node.selkey
                if isinstance(br, Leaf):
                    allof.append({"contains": br.schema, "minContains": 0, "maxContains": 1})
                elif (skey, val) in node.required:
                    key_c = ({"contains": {"const": val}} if skey in ARRAY_VALUED else {"const": val})
                    _sch = _term_scheme([val])
                    if _sch:
                        key_c = dict(key_c, **{"schema:inDefinedTermSet": _sch})
                    allof.append({"contains": {"properties": {skey: key_c},
                                               "required": [skey]}})
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
        # Emit BOTH selector branches and a bare "[]" append when they coexist: schema:object can
        # carry a selector-keyed materialsample (Sample Form) AND a bare target-material DefinedTerm
        # (Target Material) — dropping the append lost the latter entirely.
        out = [to_instance(v) for v in node.branches.values()]
        if node.append is not None:
            out.append(to_instance(node.append))
        return out
    raise TypeError(node)


# ---------- leaf schema from workbook Data Type ----------
# A transcriber records "missing" when the source -- typically the publication being transcribed --
# does not state a controlled field. Omitting the key instead would lose the distinction between
# "checked, not reported" and "nobody looked", so every controlled enum admits the sentinel. It is
# not published as a vocabulary concept (vocab_obj drops it with N/A and None): it marks the absence
# of a value, not one of them.
SENTINEL = "missing"


def with_sentinel(values):
    out = list(values)
    if SENTINEL not in out:
        out.append(SENTINEL)
    return out


def leaf_for(desc, dtype, enum=None, default=None):
    dl = (dtype or "").lower()
    if enum:
        strict = {"type": "string", "enum": with_sentinel(enum)}
        # "Controlled list / Text": the controlled vocabulary is guidance, but free text is
        # also admitted (publications routinely report these fields as prose or as several
        # values joined together). Emit anyOf[enum, string] so a controlled term validates on
        # the enum branch and a free-text description validates on the string branch.
        s = {"anyOf": [strict, {"type": "string"}]} if "text" in dl else strict
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
    b.configure(tapp)
    rows = tapp_source.rows(b.XLSX)        # .csv or .xlsx
    H = [b.norm(v).lower() for v in rows[0]]
    # "Procedure-Level Tier" since the 2026-08 delivery; "Protocol-Level Tier" before it. Both are
    # accepted because a missed tier column is SILENT — g() yields "", every row reads as neither
    # Basic nor Advanced, and the schema quietly loses its required-branch constraints instead of
    # failing. (bootstrap_schemapaths.load_rows already accepted both spellings.)
    ci = {"P": next((i for i, v in enumerate(H) if v.startswith(("procedure", "protocol"))), None),
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
    # Per-field dtype overrides in docs/<workbook>.overrides.json (ours, not Ruolin's delivery):
    # lets us retype a field to "Controlled list / Text" (enum guidance + free text) without editing
    # the Drive-synced workbook, for fields publications report as prose or several joined values.
    ovp = os.path.join(b.ROOT, "docs",
                       os.path.splitext(os.path.basename(b.XLSX))[0] + ".overrides.json")
    if os.path.exists(ovp):
        for item, o in json.load(open(ovp, encoding="utf-8")).items():
            if isinstance(o, dict) and o.get("dtype") and item in out:
                out[item]["dt"] = o["dtype"]
    return out


# registry-ref path prefix per artifact root (from the artifact's own directory)
_REG_PREFIX = {"MethodDefinition": "../../../../registry", "Dataset": "../../../../registry"}


def _is_addl_param(p: spp.ParsedPath) -> bool:
    """True for a `…<container>[schema:name='X'].schema:(value|defaultValue)` path — an ADA
    parameter resolving to a registry PropertyValue(Spec) $ref. The container is schema:additional-
    Property (method/analysis parameters) or schema:variableMeasured (reported properties: a reported
    variable is likewise a PropertyValueSpecification default / PropertyValue measured value)."""
    s = p.segments
    return (len(s) >= 2 and not s[-1].is_array and s[-1].selector is None
            and s[-1].prop in ("schema:value", "schema:defaultValue")
            and s[-2].prop in ("schema:additionalProperty", "schema:variableMeasured")
            and s[-2].selector is not None)


def analyte_column_def(name, item, desc, jtype, read_only, ptier="", atier="", prefix="ada:analyteColumn", as_value=False):
    """One generated AnalyteColumn $def, mirroring build_tapp.param_template_def.

    Built here rather than via _tapp_lib.analyte_column_obj: that helper keys its @id off a
    module-global TAPP_NAME (which stays 'empaTAPP' unless the legacy matrix route configured it,
    so LA-ICP-MS columns came out with empaTAPP @ids) and returns OrderedDicts that
    yaml.safe_dump cannot represent. b.PARAM_BASE is configured per TAPP by b.configure().
    """
    base = (b.PARAM_BASE or "ada:parameter/unknownTAPP").replace("ada:parameter/", prefix + "/")
    col_id = f"{base}/{name}"
    # ada:tier is M/R/O (Mandatory/Recommended/Optional) and follows the PROCEDURE-level tier: a
    # Basic column is one the procedure must state, Advanced is recommended. It was hardcoded "M",
    # which marked every column mandatory regardless of what the workbook said. Only the base's
    # analyte-identifier column is unconditionally M, and that one lives in tappDefinition.
    tier = {"Basic": "M", "Advanced": "R"}.get(ptier, "O")
    valtype = ({"anyOf": [{"type": "number"}, {"type": "string"}]}
               if jtype in ("number", "integer") else {"type": "string"})
    if "channelColumn" in prefix:
        # A channel property value may be a delimited list (e.g. Interfering Species reports several
        # species) — allow an array of the base type alongside the literal. This is the ONLY place a
        # property value is permitted to be either a literal or a list; a deliberate exception.
        valtype = {"anyOf": [valtype, {"type": "array", "items": valtype}]}
    if as_value:
        # A fixed/recorded column value -> schema:PropertyValue (schema:value), mirroring
        # param_value_def. Used for read-only channel columns on the procedure and for every column
        # on the $Dataset side (the analysis records the value it actually used, never a default).
        props = {
            "@id": {"const": col_id},
            "@type": {"const": ["schema:PropertyValue"]},
            "schema:propertyID": {"const": [{"@id": col_id}]},
            "schema:name": {"const": item},
            "ada:dataType": {"const": jtype},
            "ada:tier": {"const": tier},
        }
        required = ["@id", "@type", "schema:propertyID", "schema:name", "ada:dataType"]
        if ptier in ("Basic", "Advanced") or atier in ("Basic", "Editable", "Advanced"):
            props["schema:value"] = valtype
            if ptier == "Basic" or atier == "Basic":
                required.append("schema:value")
        return {"title": item, "description": desc, "type": "object",
                "properties": props, "required": required}
    props = {
        "@id": {"const": col_id},
        "@type": {"const": ["schema:PropertyValueSpecification"]},
        "schema:valueName": {"const": name},
        "schema:name": {"const": item},
        "ada:dataType": {"const": jtype},
        "schema:readonlyValue": {"const": bool(read_only)},
        "ada:tier": {"const": tier},
    }
    required = ["@id", "@type", "schema:valueName", "schema:name", "ada:dataType"]
    # The column's protocol-level default, mirroring param_template_def: a column the analysis can
    # vary per analyte still has one value the procedure registers. Declared only where the
    # procedure specifies the column at all (C != N/A), and REQUIRED at Basic — the procedure must
    # state it. Without this the default had nowhere to live and no type.
    if ptier in ("Basic", "Advanced"):
        props["schema:defaultValue"] = valtype
        if ptier == "Basic":
            required.append("schema:defaultValue")
    # No `$id`: these defs are INLINED into the overlay, and an inlined $id would re-base $ref
    # resolution for that subschema. Identity lives in the @id const, matching param_template_def.
    return {"title": item, "description": desc, "type": "object",
            "properties": props, "required": required}


def _is_analyte_column(p: spp.ParsedPath) -> bool:
    """True for a `…ada:analyteTemplate.ada:analyteColumns[]` path — one per-analyte column of the
    technique's element table. The row's Data Type describes the COLUMN'S VALUE, not the array
    item, so the leaf is used to type the generated column def rather than the array's items."""
    s = p.segments
    return bool(s) and s[-1].prop in KEYED_TABLES and s[-1].is_array and s[-1].selector is None


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
    registries = {"parameterTemplates": {}, "parameterValues": {}, "analyteColumns": {}}
    required = {"MethodDefinition": [], "Dataset": []}
    # Rows a composed module already supplies. They are dropped from this overlay so a shared field
    # is defined once — otherwise the technique's copy sits alongside the module's and silently wins
    # wherever the two differ, which is the drift composition exists to end. module_composition only
    # reports a row as covered when a module $def demonstrably provides it on that root.
    import module_composition as mc
    _, _covered = mc.plan(b.XLSX)
    # A module publishes its PARAMETERS as separate Param_<Side>_<name> $defs rather than inside its
    # root $def, because a module cannot constrain schema:additionalProperty - it can only offer a
    # branch to union in. So a covered parameter row must be REPLACED by the module's branch, not
    # merely dropped: dropping it removed the parameter from the technique's schema entirely while
    # its instances still carried it.
    _param_refs = mc.param_refs(b.XLSX)
    pt_seen, pv_seen = set(), set()
    for item, rec in spec.items():
        m = meta.get(item, {})
        paths = rec["path"] if isinstance(rec["path"], list) else [rec["path"]]
        for path in paths:   # usually 1; 2 for a dual-homed editable param (TAPP default + detail value)
            path = normalize_path(path)
            parsed = spp.parse(path)
            _key = mc.ms._norm(mc.ms.rename(item))
            if _key in _covered[parsed.root]:
                continue                  # the module carries this one
            require = (m.get("P") == "Basic") or (m.get("A") == "Basic")
            # A TAPP-definition property is JSON-Schema readOnly unless it is editable at the dataset
            # level (Analysis tier Editable/Basic/Advanced) — i.e. read-only / protocol-only fields are
            # locked, so a UI editing a dataset instance (which uses the TAPP) knows what it may change.
            read_only = (parsed.root == "MethodDefinition"
                         and (m.get("A") or "").strip() not in ("Editable", "Basic", "Advanced"))
            non_type = [s for s in parsed.segments if not s.is_type]
            if require and len(non_type) == 1 and non_type[0].selector is None and not non_type[0].is_array:
                if non_type[0].prop not in required[parsed.root]:   # top-level direct prop, Basic tier
                    required[parsed.root].append(non_type[0].prop)
            if _is_addl_param(parsed):
                # PARAMETER COMPOSITION. module_composition._is_composable excludes
                # schema:additionalProperty from allOf composition, and rightly so: two universal
                # constraints on one closed array cannot both hold. But a module parameter does not
                # need allOf - it needs to be a BRANCH of the technique's own anyOf, which is a
                # union, not an intersection. Where a module supplies this parameter, reference its
                # Param_<Side>_<name> $def instead of minting a technique-scoped duplicate. That is
                # what gives a shared parameter ONE identity (ada:parameter/module/<Module>/<name>)
                # rather than one per consuming TAPP.
                _mref = _param_refs.get((_key, parsed.root))
                # Only compose where the technique puts the parameter in the SAME KIND of slot the
                # module does. A module parameter lives on schema:additionalProperty; where a
                # technique instead routes the field to schema:variableMeasured (a reported
                # property), the module's def is the wrong shape for that slot - it lacks the
                # cdi:InstanceVariable typing every dataset variable needs - and the wrong thing
                # semantically. Keep the technique's own def there.
                if _mref is not None and any(x.prop == "schema:variableMeasured"
                                             for x in parsed.segments):
                    _mref = None
                if _mref is not None:
                    insert(roots[parsed.root],
                           spp.ParsedPath(parsed.root, parsed.segments[:-1]),
                           element=Leaf(dict(_mref)),
                           require=(m.get("P") == "Basic") or (m.get("A") == "Basic"))
                    continue
                bd = {"item": item, "name": (sidecar.get(item, {}).get("name") or b.camel(item)),
                      "jtype": b.jtype(m.get("dt", "")), "unit": b.unit(m.get("dt", "")),
                      "desc": m.get("desc", ""), "A": m.get("A", "")}
                if parsed.segments[-1].prop == "schema:defaultValue":
                    name, body = b.param_template_def(bd, pt_seen)
                    registries["parameterTemplates"].update(body); pt_seen.add(name)
                    ref = {"$ref": f"{_REG_PREFIX[parsed.root]}/parameterTemplates/schema.yaml#/$defs/{name}"}
                else:
                    name, body = b.param_value_def(bd, pv_seen)
                    # A reported property sitting on schema:variableMeasured is a DATASET VARIABLE as
                    # well as a PropertyValue, and the base shape requires @type to contain
                    # cdi:InstanceVariable. param_value_def pins @type to ["schema:PropertyValue"]
                    # alone - right for an additionalProperty parameter, but unsatisfiable here: no
                    # instance could match both that const and the base's contains.
                    if any(x.prop == "schema:variableMeasured" for x in parsed.segments):
                        tc = ((body[name].get("properties") or {}).get("@type") or {})
                        if isinstance(tc.get("const"), list) and CDI_VARIABLE not in tc["const"]:
                            tc["const"] = tc["const"] + [CDI_VARIABLE]
                    registries["parameterValues"].update(body); pv_seen.add(name)
                    ref = {"$ref": f"{_REG_PREFIX[parsed.root]}/parameterValues/schema.yaml#/$defs/{name}"}
                if read_only:
                    ref["readOnly"] = True   # $ref + sibling keyword is valid in JSON Schema 2020-12
                truncated = spp.ParsedPath(parsed.root, parsed.segments[:-1])
                vm = any(s.prop == "schema:variableMeasured" for s in parsed.segments)
                # A Basic-tier reported property IS required, exactly like any other Basic field, so
                # it earns a hard `contains` here too. (This previously suppressed `contains` for
                # every schema:variableMeasured entry, which made a Basic reported property optional.)
                insert(roots[parsed.root], truncated, element=Leaf(ref), require=require)
                if vm:
                    # schema:variableMeasured is the CDIF slot for the dataset's ACTUAL measured
                    # variables, which are dataset-specific and arbitrary — not merely the TAPP's
                    # reported properties. Narrowing `items` to the reported-property branches alone
                    # made every real variable (measurement_value, position_x) invalid. Permit the
                    # generic CDIF variable alongside them; the base schema still enforces its shape.
                    arr = _vm_array(roots[parsed.root], truncated)
                    if isinstance(arr, Arr) and GENERIC_VARIABLE not in arr.extra_items:
                        arr.extra_items.append(GENERIC_VARIABLE)
                continue
            if _is_analyte_column(parsed):
                cfg = KEYED_TABLES[parsed.segments[-1].prop]
                # One generated AnalyteColumn def per row, referenced as a permitted item of the
                # array. The defs are INLINED downstream (build_pathdriven) rather than $ref'd to
                # the shared registry: that registry keys defs by bare name, so a column name used
                # by two TAPPs (e.g. detectionLimit) would resolve to the other TAPP's def and its
                # @id const — the same reason parameter defs are inlined.
                bare = sidecar.get(item, {}).get("name") or b.camel(item)
                name = b.def_key(bare)   # TAPP-namespaced: the registry is shared across TAPPs
                # A dual-homed channel column defines TWO shapes under one name — a procedure default
                # (PropertyValueSpecification on $MethodDefinition) and an analysis value
                # (PropertyValue on $Dataset). Keep them as distinct $defs so one does not overwrite
                # the other in the shared registry (which made an editable procedure column adopt its
                # dataset counterpart's PropertyValue form).
                if cfg["registry"] == "channelColumns" and parsed.root == "Dataset":
                    name = name + "AnalysisValue"
                # @id namespace per table: analyteColumns -> ada:analyteColumn, channelColumns ->
                # ada:channelColumn, reportedPropertyColumns -> ada:reportedPropertyColumn.
                # Channel columns type by tier+root: a read-only procedure column and EVERY dataset
                # column record a fixed value (schema:PropertyValue); an editable procedure column
                # registers a default (schema:PropertyValueSpecification). Analyte columns keep the
                # specification form.
                as_value = (cfg["registry"] == "channelColumns"
                            and (parsed.root == "Dataset" or read_only))
                registries.setdefault(cfg["registry"], {})[name] = analyte_column_def(
                    bare, item, m.get("desc", "") or "", b.jtype(m.get("dt", "")), read_only,
                    ptier=(m.get("P") or "").strip(), atier=(m.get("A") or "").strip(),
                    prefix="ada:" + cfg["registry"].rstrip("s"), as_value=as_value)
                ref = {"$ref": f"{_REG_PREFIX[parsed.root]}/{cfg['registry']}/schema.yaml"
                                f"#/$defs/{name}"}
                insert(roots[parsed.root], parsed, element=Leaf(ref), branch_key=name, require=require)
                # keep the base's identifier column permissible under the narrowed `items`
                arr = roots[parsed.root].props.get(cfg["template"])
                arr = arr.props.get(parsed.segments[-1].prop) if isinstance(arr, Obj) else None
                if isinstance(arr, Arr) and cfg["identifier_ref"] not in arr.extra_items:
                    arr.extra_items.append(cfg["identifier_ref"])
                continue
            if parsed.segments[-1].prop in DEFAULT_ROW_ARRAYS:
                # a template's default-ROW array (defaultAnalytes/defaultChannels): the leaf is the
                # string|DefinedTerm array, not the row's scalar Data Type. Overriding the base's
                # array constraint with the row's {type:string} otherwise made every list invalid.
                insert(roots[parsed.root], parsed,
                       {"type": "array", "items": DEFAULT_ROW_ITEMS}, require=require)
                continue
            enum = None
            dl = (m.get("dt") or "").lower()
            if "controlled" in dl:
                parts = [p.strip().strip("'\"") for p in (m.get("ex") or "").split("|")
                         if p.strip() and not p.strip().lower().startswith("e.g") and "specify" not in p.strip().lower()]
                enum = parts or None
            leaf = leaf_for(m.get("desc"), m.get("dt"), enum)
            if read_only:
                leaf = {**leaf, "readOnly": True}
            insert(roots[parsed.root], parsed, leaf, require=require)
    return {r: to_schema(o) for r, o in roots.items()}, registries, required


# base building block each overlay extends via allOf (relative to the artifact's own dir)
_BASE_REF = {"MethodDefinition": "../../../../BaseSchema/tappDefinition/schema.yaml",
             "Dataset": "../../../../BaseSchema/adaProduct/schema.yaml"}


def wrap(root, overlay, required, title=None, description=None, module_refs=()):
    """Wrap an overlay as a full artifact schema: allOf[{$ref base}, *modules, {overlay + required}].

    The module refs sit between the base and this technique's own properties, which is only
    presentation — allOf is unordered — but reads as inherit, then compose, then specialise.
    """
    inner = {"type": "object", "properties": overlay.get("properties", {})}
    if required:
        inner["required"] = required
    out = {"$schema": "https://json-schema.org/draft/2020-12/schema"}
    if title:
        out["title"] = title
    if description:
        out["description"] = description
    out["allOf"] = [{"$ref": _BASE_REF[root]}, *module_refs, inner]
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
