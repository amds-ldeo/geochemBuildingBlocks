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
import copy
import re
import sys
import yaml

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
        # DEEP COPY, never the const object itself. Returning s["const"] by reference made every
        # generated instance ALIAS the loaded schema: a later in-place edit of the instance (adding
        # a @type, filling a value) mutated the schema's own const, and because one $def serves many
        # examples the damage accumulated across a run - which is how a channel column's
        # @type const grew from ["schema:PropertyValue"] to ["schema:PropertyValue",
        # "schema:PropertyValueSpecification"] while the file on disk stayed correct.
        return copy.deepcopy(s["const"])
    # a resolved column def often nests its shape under allOf (base column shape + pinned consts);
    # merge the members' properties/required so the identifier column instantiates from its consts.
    props, req = dict(s.get("properties") or {}), list(s.get("required") or [])
    for m in (s.get("allOf") or []):
        if isinstance(m, dict):
            props.update(m.get("properties") or {})
            req += (m.get("required") or [])
    if props:
        keys = req or list(props)
        return {k: instance_from_def(props[k]) for k in keys if k in props}
    t = s.get("type")
    if t == "boolean":
        return True
    if t in ("number", "integer"):
        return 1
    if "anyOf" in s:
        return 1 if any(br.get("type") in ("number", "integer") for br in s["anyOf"]) else "example value"
    return "example value"


_MODPARAM_CACHE = {}


def _module_param_def(item, root):
    """The module Param_ $def that supplies `item` on `root`, or None.

    Mirrors the composition schema_path_emitter performs, so schema and example agree on which
    parameters are module-owned and therefore carry ada:parameter/module/<Module>/<name>.
    """
    import module_composition as mc
    key = b.XLSX
    if key not in _MODPARAM_CACHE:
        refs = mc.param_refs(b.XLSX)
        loaded = {}
        for k, ref in refs.items():
            path, frag = ref["$ref"].split("#/$defs/")
            f = os.path.normpath(os.path.join(ROOT, "_sources", path.replace("../", "")))
            if f not in loaded:
                try:
                    loaded[f] = (yaml.safe_load(open(f, encoding="utf-8")) or {}).get("$defs") or {}
                except Exception:
                    loaded[f] = {}
            d = loaded[f].get(frag)
            if d:
                _MODPARAM_CACHE.setdefault(key, {})[k] = d
        _MODPARAM_CACHE.setdefault(key, {})
    return _MODPARAM_CACHE[key].get((mc.ms._norm(mc.ms.rename(item)), root))


WIKIDATA_INSTRUMENT = "https://www.wikidata.org/wiki/Q3099911"


def instrument_id(token):
    """A document-scoped @id for an instrument, derived from its type token.

    Derived rather than sequential so it is stable across regenerations: a counter would rewrite
    every example on every run.
    """
    return "ex:instrument/" + (re.sub(r"[^A-Za-z0-9]+", "-", str(token or "instrument")).strip("-")
                               or "instrument")


def normalize_instrument_tree(inst):
    """Supply the structural fields an instrument node needs but a schema path never names.

    THE ONE normalizer for instrument trees. Both example builders call it: build_tapp_examples for
    publication examples, and route() below for the synthetic -P0 ones. They previously had separate
    implementations, which drifted -- the synthetic one supplied @id but typed components
    ["schema:Thing"] alone, so every ICP-MS detail -P0 failed the component branch that requires
    schema:Product too. Two copies of a rule is two chances to be half-right.

    The instrument building block requires, on each node:
      * @type [schema:Product, schema:Thing] -- on the instrument AND every inline component
      * @id -- so a monitored species can name the device, or the PART, that reports it
      * on a component: the scientific-instrument Wikidata term, and a schema:name
      * @type on schema:model / schema:manufacturer

    The path interpreter builds these nodes by nesting from [additionalType=...] selectors and
    carries only the metadata leaves, so the discriminators are supplied here rather than left to
    the validator-driven fills, which cannot resolve them through the instrument $def's deep anyOf.
    """
    def token(node, fallback):
        t = next((x for x in (node.get("schema:additionalType") or []) if isinstance(x, str)), None)
        return re.sub(r"[^A-Za-z0-9]+", "-", str(t or fallback)).strip("-") or fallback

    def walk(node, is_component, parent_id=None):
        if not isinstance(node, dict):
            return
        node.setdefault("@type", ["schema:Product", "schema:Thing"])
        if not isinstance(node.get("@id"), str):
            # a component is scoped under its parent, so two instruments may each carry their own
            # Collector without the identifiers colliding
            node["@id"] = ("%s/part/%s" % (parent_id or instrument_id("instrument"),
                                           token(node, "component"))
                           if is_component else instrument_id(token(node, "instrument")))
        if is_component:
            at = node.setdefault("schema:additionalType", [])
            if not any(isinstance(x, dict) and x.get("@id") == WIKIDATA_INSTRUMENT for x in at):
                at.append({"@id": WIKIDATA_INSTRUMENT})
            node.setdefault("schema:name", "missing")
        m = node.get("schema:model")
        if isinstance(m, dict):
            m.setdefault("@type", ["schema:ProductModel"])
        mf = node.get("schema:manufacturer")
        if isinstance(mf, dict):
            mf.setdefault("@type", ["schema:Organization"])
        for part in (node.get("schema:hasPart") or []):
            walk(part, True, node.get("@id"))

    def find(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k == "schema:instrument":
                    for i in (v if isinstance(v, list) else [v]):
                        walk(i, False)
                find(v)
        elif isinstance(n, list):
            for v in n:
                find(v)

    find(inst)


def strip_annotation(v, m=None):
    """Drop a trailing transcription note from a cell destined for a CONTROLLED slot.

    Publication columns carry curator notes in brackets - "Multi-collector sector-field ICP-MS [all
    columns state \"multi-collector inductively coupled plasma mass spectrometer\"]". Free text can
    keep them, but a value routed to a controlled term (schema:additionalType, a Controlled-list
    row) has to match the vocabulary exactly, so the note has to come off. `meaningful()` already
    strips the [P...] form; this is the general one.
    """
    if not isinstance(v, str):
        return v
    dt = (m or {}).get("dt", "") or ""
    if "controlled" not in dt.lower():
        return v
    return re.sub(r"\s*\[[^\]]*\]\s*$", "", v).strip() or v


def numify(raw, dtype):
    """A numeric field whose source cell carries a number PLUS prose (e.g. "1250 W RF power",
    "~60% of maximum output"): return (number, full_text) so the extracted number becomes the
    value/defaultValue and the full original text is preserved in schema:description. A pure number
    returns (number, None); anything non-numeric returns (raw, None)."""
    if dtype in ("number", "integer") and isinstance(raw, str):
        m = re.search(r"-?\d+(?:\.\d+)?", raw)
        if m:
            n = float(m.group(0)) if "." in m.group(0) else int(m.group(0))
            return n, (raw if m.group(0) != raw.strip() else None)
    return raw, None


def placeholder(m, item, sidecar):
    """A schema-satisfying placeholder value for a direct/scalar terminal."""
    name = sidecar.get(item, {}).get("name") or b.camel(item)
    dl = (m.get("dt") or "").lower()
    if "controlled" in dl:
        parts = [p.strip().strip("'\"") for p in (m.get("ex") or "").split("|")
                 if p.strip() and not p.strip().lower().startswith("e.g") and "specify" not in p.strip().lower()]
        if parts:
            return parts[0]
        # Column F is consumer-owned and can be empty on a row a TAPP inherited from a module
        # without filling in its own half — VNMIR shipped exactly that for Analytical Mode. The
        # `example <name>` fallback below is then not merely unhelpful, it is guaranteed WRONG:
        # where the generator also emits an enum for this property, no placeholder string can
        # satisfy it, and the example fails the very schema it is meant to demonstrate. Prefer
        # the enum the schema is being built from; it is the same list, from the same config.
        enum = (getattr(b, "CFG", None) or {}).get("enum_props", {}).get(name)
        if enum:
            return enum[0]
    if dl.startswith("bool"):
        return True
    if "integer" in dl:
        return 1
    if "numeric" in dl or "number" in dl:
        return 1.0
    return f"example {name}"


def _split_top_level(v):
    """Split a transcribed list on commas/semicolons at PARENTHESIS DEPTH ZERO, so a member's own
    parenthetical (e.g. '(7 cups monitoring Kr, Rb, Er)') is kept intact rather than shredded."""
    out, buf, depth = [], [], 0
    for ch in v:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch in ",;" and depth == 0:
            if "".join(buf).strip():
                out.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if "".join(buf).strip():
        out.append("".join(buf).strip())
    return out


def build_example(tapp, values=None, emit_reported_property=False):
    """{root -> instance dict} built from the canonical paths, reusing the schema-emitter merger.

    values=None  -> the synthetic minimal example: placeholder leaves, and the base-owned rich MD
        objects (instrument tree, target-material object, workflow steps, …) are SKIPPED because
        placeholders cannot synthesise them and they are optional in tappDefinition.
    values={item: cell}  -> a PUBLICATION example: the transcribed cell value is placed at each
        item's canonical sidecar path, the rich MD objects ARE populated (an instrument model, a
        target material, a workflow-step parameter all land at their real nested homes), and only
        items the publication reports are emitted — empty cells are omitted and required-but-absent
        scalars are back-filled with a sentinel downstream (fill_required_sentinels).

    emit_reported_property -> when a publication lists 'Reported Variables and Units', its reported
        properties are emitted at schema:variableMeasured (the 'reported property' Key-by rows);
        otherwise those rows are skipped in favour of their non-reported-property counterparts."""
    pub = values is not None
    meta = e._load_rows(tapp)
    sidecar = b.load_sidecar()
    import schemapath_io
    spec = schemapath_io.load_spec(schemapath_io.csv_path(b.XLSX))

    # Fields the composed modules contribute. The example must satisfy the COMPOSED schema, and a
    # module can require something the technique's own table never lists: Group1 requires Session
    # Identifier on the activity, which appears in no technique sidecar, so an example built from
    # the technique alone became invalid the moment composition was wired.
    import module_composition as mc
    _refs, _covered = mc.plan(b.XLSX)
    _injected = set()
    for _name, _ in _refs:
        _sc = schemapath_io.csv_path(os.path.join(mc.ts.modules_dir(), f"Module_{_name}.csv"))
        if not os.path.exists(_sc):
            continue
        for _item, _rec in schemapath_io.load_spec(_sc).items():
            # Mirrors module_composition's rule exactly: inject what the module now carries, and
            # never a schema:additionalProperty row. The technique constrains that array as a
            # closed anyOf over the parameters it enumerates, so an element it has never heard of
            # matches no branch and the example fails against its own schema.
            # Filter PER PATH, not per item. A dual-homed module row carries a composable
            # procedure path AND a parameter dataset path; keeping the item on the strength of the
            # first injected the second too, putting an element in the example that the technique's
            # closed anyOf had never enumerated.
            _paths = _rec["path"] if isinstance(_rec["path"], list) else [_rec["path"]]
            _keep = [_p for _p in _paths if _p and mc._is_composable(_p)]
            if not _keep:
                continue
            # WHERE THE MODULE COVERS THE ITEM, THE MODULE OWNS THE PLACEMENT. "A technique's own
            # row wins" was right while modules only added fields, but a covered row is dropped from
            # the technique's overlay -- so letting the technique's row win here emitted a placement
            # the schema no longer has, and suppressed the module's. SEM kept its variableMeasured
            # row for Goodness-of-Fit and so never emitted the module's dqv default, which the
            # module's Basic tier requires.
            _k = mc.ms._norm(mc.ms.rename(_item))
            _owned = any(_k in _covered[_r] for _r in ("MethodDefinition", "Dataset"))
            if _item not in spec or _owned:
                _injected.add(_item)
                spec[_item] = {**_rec, "path": _keep}
            meta.setdefault(_item, {})

    roots = {"MethodDefinition": e.Obj(), "Dataset": e.Obj()}
    pt_seen, pv_seen = set(), set()
    # base-owned rich-object properties (analyteTemplate, computationalTool, workflow steps, the
    # instrument tree, the plan's target-material schema:object, relatedLink) need objects the
    # placeholder can't synthesise and are all OPTIONAL in tappDefinition — so omit them from the
    # minimal valid TAPP-side example (the schema still constrains them). Dataset-side (detail)
    # sample/relatedLink are kept: the detail is validated standalone, not against the strict base.
    SKIP_MD = ("ada:analyteTemplate", "ada:reportedPropertyTemplate", "ada:channelTemplate",
               "bios:computationalTool",
               "schema:actionProcess", "schema:instrument", "schema:object", "schema:relatedLink")
    # Publication mode populates the rich objects from real cells. What still stays out are the
    # keyed-table COLUMN DEFINITIONS (analyteColumns/channelColumns/reportedPropertyColumns) — those
    # are structural, emitted schema-side, never carrying per-publication values — while the default
    # ROWS (defaultAnalytes / defaultChannels) and the collector-configuration data ARE populated.
    COLUMN_DEFS = ("ada:analyteColumns", "ada:channelColumns", "ada:reportedPropertyColumns",
                   "ada:collectorConfiguration",
                   # reported properties are a conditional template: emitted only when the procedure
                   # enumerates "Reported Variables and Units" (build_tapp_examples gates them),
                   # never by the generic interpreter — otherwise every reported field would appear
                   # both here and on its workflow step.
                   "schema:variableMeasured")
    DEFAULT_ROWS = ("ada:defaultAnalytes", "ada:defaultChannels")
    for item, rec in spec.items():
        m = meta.get(item, {})
        if pub and item not in values:
            continue                     # publication example: emit only what the source reports
        paths = rec["path"] if isinstance(rec["path"], list) else [rec["path"]]
        for path in paths:   # usually 1; 2 for a dual-homed editable param (TAPP default + detail value)
            path = e.normalize_path(path)
            parsed = spp.parse(path)
            if (item not in _injected
                    and mc.ms._norm(mc.ms.rename(item)) in _covered[parsed.root]
                    and not mc._is_composable(path)):
                # The module carries this field, so the technique's own schema:additionalProperty
                # branch for it is gone -- emitting ada:parameter/<TAPP>/<name> matched no branch.
                # Only the PARAMETER path goes, though: the module's $def still REQUIRES the
                # composable placement (ada:ablationSpotDurationDefault and friends), so dropping
                # the item outright stripped required properties out of the example instead.
                continue
            if any(c in path for c in COLUMN_DEFS):
                continue                 # structural column defs, schema-side only — never a value
            if pub:
                if "schema:variableMeasured" in path and not emit_reported_property:
                    continue             # reported-property row unused when no variables are listed
            elif parsed.root == "MethodDefinition" and any(t in path for t in SKIP_MD):
                # synthetic mode omits the rich base-owned objects (placeholders cannot build them)
                continue
            if pub and parsed.segments[-1].prop in DEFAULT_ROWS:
                # a default-row array: split the transcribed list into members on top-level commas /
                # semicolons only — a parenthetical like "H3 (⁸⁸Sr) (7 cups monitoring Kr, Rb, …)"
                # keeps its internal commas rather than being shredded into bogus members.
                v = strip_annotation(values[item], m)
                items = _split_top_level(v) if isinstance(v, str) else v
                e.insert(roots[parsed.root], parsed, items)
                continue
            if e._is_addl_param(parsed):
                # Where a module supplies this parameter, the SCHEMA now references the module's
                # Param_ $def instead of a technique-scoped one (see schema_path_emitter). The
                # example has to follow: minting the technique form here would emit
                # ada:parameter/<TAPP>/<name> against a schema that pins
                # ada:parameter/module/<Module>/<name>, and match no branch.
                _mdef = _module_param_def(item, parsed.root)
                if _mdef is not None and any(x.prop == "schema:variableMeasured"
                                             for x in parsed.segments):
                    _mdef = None      # same carve-out as the schema side
                if _mdef is not None:
                    elem = instance_from_def(_mdef)
                else:
                    bd = {"item": item, "name": (sidecar.get(item, {}).get("name") or b.camel(item)),
                          "jtype": b.jtype(m.get("dt", "")), "unit": b.unit(m.get("dt", "")),
                          "desc": m.get("desc", ""), "A": m.get("A", "")}
                    if parsed.segments[-1].prop == "schema:defaultValue":
                        _, body = b.param_template_def(bd, pt_seen); pt_seen.add(next(iter(body)))
                    else:
                        _, body = b.param_value_def(bd, pv_seen); pv_seen.add(next(iter(body)))
                    elem = instance_from_def(next(iter(body.values())))
                if pub and isinstance(elem, dict):
                    num, desc = numify(values[item], b.jtype(m.get("dt", "")))
                    elem[parsed.segments[-1].prop] = num          # real default/value, not placeholder
                    if desc:
                        elem["schema:description"] = desc          # number extracted; keep the prose
                trunc = spp.ParsedPath(parsed.root, parsed.segments[:-1])
                e.insert(roots[parsed.root], trunc, element=e.Leaf(elem))
                continue
            e.insert(roots[parsed.root], parsed,
                     strip_annotation(values[item], m) if pub else placeholder(m, item, sidecar))
    out = {r: e.to_instance(o) for r, o in roots.items()}
    for v in out.values():
        normalize_instrument_tree(v)
    return out


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

    Five shapes are in use across the base schemas: `const: [...]`; an array with
    `contains: {const: X}` (the CDIF person profile, and instrument additionalType); an array with
    `contains: {enum: [...]}` where the schema permits a choice of kinds (the reagent branch — take
    the first as the placeholder); a `default` (the organization profile); and an `enum` of
    permitted tokens.
    """
    t = (subschema.get("properties") or {}).get("@type")
    if not isinstance(t, dict):
        return None
    if isinstance(t.get("const"), list):
        return list(t["const"])
    c = t.get("contains")
    if isinstance(c, dict) and isinstance(c.get("const"), str):
        return [c["const"]]
    if isinstance(c, dict) and isinstance(c.get("enum"), list) and c["enum"]:
        return [c["enum"][0]]
    # several required types, each asserted by its own `contains` under an allOf -- the CDIF
    # instrument shape (schema:Product AND schema:Thing). All of them must be present.
    if isinstance(t.get("allOf"), list):
        consts = [b["contains"]["const"] for b in t["allOf"]
                  if isinstance(b, dict) and isinstance(b.get("contains"), dict)
                  and isinstance(b["contains"].get("const"), str)]
        if consts:
            return consts
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
    # Only a BRANCH keyword's value is a list of subschemas. `required` also holds a list -- of
    # property names -- so unwrapping it walked into the names and lost the branch, which meant a
    # required-@type error reported directly (not via an anyOf) could never be filled.
    if (err.validator in ("anyOf", "oneOf", "allOf")
            and isinstance(node, dict) and isinstance(node.get(err.validator), list)):
        node = node[err.validator]
    best = node if isinstance(node, dict) and "@type" in (node.get("properties") or {}) else None
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
                # cand.path is relative to err ONLY when cand came from err.context; when cand IS
                # err it already holds the absolute path, and appending it doubled the path so the
                # node was never found.
                rel = list(cand.path) if cand is not err else []
                node = _at(inst, list(err.absolute_path) + rel)
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


def _extendable_type(inst, err, rel):
    """False when the node is an @type array the schema PINS by const.

    The plain-token append exists for stub nodes whose @type the schema builds up from several
    `contains` clauses (an instrument part that must carry schema:Thing as well as schema:Product).
    But a node instantiated from a registry $def has its @type fixed by a `const`, and extending
    that array makes it match NO branch: a channel column pinned to ["schema:PropertyValue"] grew a
    "schema:PropertyValueSpecification" borrowed from a SIBLING column's contains clause, and then
    validated against neither. Such nodes are recognisable by carrying their own @id, which is what
    the const-pinned branches key on.
    """
    path = list(err.absolute_path) + list(rel)
    if not path or path[-1] != "@type":
        return True
    # Only an ARRAY ELEMENT is const-pinned this way: a registry-def instance sitting in a
    # channelColumns / additionalProperty / variableMeasured array. The document ROOT also carries an
    # @id, and its @type legitimately IS built up from several contains clauses (prov:Plan,
    # cdi:Activity, ...) - guarding it stripped those and left the root typed by vocabulary terms
    # alone. So require the owner to be an array member before treating its @type as pinned.
    if len(path) < 2 or not isinstance(path[-2], int):
        return True
    owner = _at(inst, path[:-1])
    return not (isinstance(owner, dict) and isinstance(owner.get("@id"), str))


def fill_structural_gaps(inst, resolved_schema, max_passes=6):
    """Supply the other things a schema path cannot carry, read off the schema the same way.

    Two cases, both structural rather than metadata, and both introduced by composing the base
    instrument shape into a technique detail:

      * a required `schema:name` the paths never set (an instrument is identified in the sidecar by
        schema:additionalType, so nothing names it) -> a placeholder, flagged as such;
      * an unsatisfied `contains` whose subschema pins an @id to a const -- the Wikidata
        "measuring instrument" term every instrument carries -> append that exact IRI reference.

    Mutates `inst`; returns how many gaps were filled.
    """
    import jsonschema
    validator = jsonschema.Draft202012Validator(resolved_schema)
    filled = 0
    for _ in range(max_passes):
        added = 0
        for err in validator.iter_errors(inst):
            for cand in ([err] + list(err.context or [])):
                rel = list(cand.path) if cand is not err else []
                node = _at(inst, list(err.absolute_path) + rel)
                if cand.validator == "required" and "'schema:name'" in cand.message:
                    if isinstance(node, dict) and "schema:name" not in node:
                        node["schema:name"] = "example instrumentName"
                        added += 1
                        break
                # a labeledLink / identifier requires a resolvable URL the sidecar never carries (a
                # coupled-technique relatedLink has a name/target but no link) -> a placeholder URL.
                if cand.validator == "required" and "'schema:url'" in cand.message:
                    if isinstance(node, dict) and "schema:url" not in node:
                        node["schema:url"] = "https://ada.astromat.org/missing"
                        added += 1
                        break
                # a 1..* / 0..* property is always a JSON array in these schemas, but a schema path
                # carries one value, so the builder writes the bare value. Wrap it.
                if (cand.validator == "type" and cand.validator_value == "array"
                        and node is not None and not isinstance(node, list)):
                    path = list(err.absolute_path) + rel
                    parent = _at(inst, path[:-1]) if path else None
                    if isinstance(parent, (dict, list)):
                        parent[path[-1]] = [node]
                        added += 1
                        break
                if cand.validator == "contains" and isinstance(node, list):
                    sub = (cand.schema or {}).get("contains") or {}
                    const = ((sub.get("properties") or {}).get("@id") or {}).get("const")
                    if const and not any(isinstance(x, dict) and x.get("@id") == const for x in node):
                        node.append({"@id": const})
                        added += 1
                        break
                    # a plain token the array must contain -- an instrument part carrying
                    # schema:Thing but not schema:Product. Extend rather than replace: the node
                    # already holds types that other branches require.
                    plain = sub.get("const")
                    if isinstance(plain, str) and plain not in node and _extendable_type(inst, err, rel):
                        node.append(plain)
                        added += 1
                        break
                    # a COMPONENT the array must contain, pinned by an additionalType token: a hasPart
                    # the sidecar routes a property onto (e.g. an ICP-MS Collector carrying
                    # ada:collectorConfiguration). The contains targets
                    # schema:additionalType.contains rather than an @id, so neither branch above fires
                    # -- append a minimal component carrying that type; later passes fill its required
                    # schema:name / @id the same way they do for any other node.
                    at = (((sub.get("properties") or {}).get("schema:additionalType") or {})
                          .get("contains") or {}).get("const")
                    if isinstance(at, str) and not any(
                            isinstance(x, dict) and at in (x.get("schema:additionalType") or []) for x in node):
                        stub = {"schema:additionalType": [at]}
                        # borrow @type from a sibling component so the stub is a valid instrument part
                        # in this same pass (fill_required_types may already have run).
                        sib = next((x for x in node if isinstance(x, dict) and "@type" in x), None)
                        if sib:
                            stub["@type"] = list(sib["@type"]) if isinstance(sib["@type"], list) else sib["@type"]
                        # …and the term reference its siblings carry. The instrument-component
                        # branch requires additionalType to contain the Wikidata scientific-instrument
                        # IRI; a stub with only its own token matched no branch, so the component the
                        # sidecar asked for was added and then failed validation.
                        ref = next((t for x in node if isinstance(x, dict)
                                    for t in (x.get("schema:additionalType") or [])
                                    if isinstance(t, dict) and t.get("@id")), None)
                        if ref:
                            stub["schema:additionalType"].append(dict(ref))
                        # the component branch requires schema:name; the comment above assumed a
                        # later pass would supply it, but nothing does for a nested hasPart. Name it
                        # after the token that made it necessary.
                        stub["schema:name"] = at
                        # inline components require @id (a monitored species must be able to name
                        # the part that reports it); derive it from the token that made the stub.
                        stub["@id"] = "ex:instrument/part/" + re.sub(r"[^A-Za-z0-9]+", "-", str(at)).strip("-")
                        node.append(stub)
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
