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
import tapp_source

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODDIR = tapp_source.modules_dir()
BBDIR = os.path.join(ROOT, "_sources", "BaseSchema", "modules")
# What the built module $defs actually carry. Ours, generated, read by module_composition.
EMITTED_PATH = os.path.join(ROOT, "docs", "modules", "emitted.json")

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
           "UPb": "uPb", "Geochronology": "geochronology", "ArAr": "arAr", "Group1": "group1",
           # An all-caps acronym is the case the first-character fallback gets wrong: it produced
           # `iCPMS`, which reads as a typo beside mcIcpms and would have to be renamed after
           # everything $refs it.
           "ICPMS": "icpms"}


def dirname(name):
    """Directory for a module BB: lowerCamelCase, matching every other building block here.

    DIRNAME carries the irregular ones (MCICPMS -> mcIcpms, UPb -> uPb). Everything else lowers
    only the FIRST character - `name.lower()` was the old fallback and turned TargetSelection into
    `targetselection`, which reads as a different naming convention from its siblings and is
    painful to correct once anything $refs it.
    """
    return DIRNAME.get(name, name[:1].lower() + name[1:])
PREFIX_IRI = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
              "prov": "http://www.w3.org/ns/prov#", "bios": "https://bioschemas.org/",
              "dqv": "http://www.w3.org/ns/dqv#",
              "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"}


def is_composable(path):
    """False for a path landing in a container a module CANNOT constrain through `allOf`.

    Three containers, one failure mode. The consuming technique already constrains each of them as
    a CLOSED shape derived from its own table, and `allOf` makes every element satisfy the
    technique's constraint AND the module's — so two universal constraints on one array can never
    both hold unless each side already knows about the other.

      schema:additionalProperty   a closed anyOf over the parameters the table enumerates
      a keyed-table COLUMN array  (ada:analyteColumns, ada:channelColumns,
                                   ada:reportedPropertyColumns, ada:collectorConfiguration) —
                                  narrowed to the technique's generated column defs plus the base's
                                  identifier column
      a default-ROW array         (ada:defaultAnalytes, ada:defaultChannels) — string | DefinedTerm

    The column case arrived with Module_ICPMS in the 2026-09 delivery and broke 96 examples: a row
    ending at `…ada:analyteColumns[]` carries the COLUMN'S scalar Data Type, so composing it emitted
    `items: {type: string}` against the technique's `items: {anyOf: [...column objects...]}`, and
    nothing validated. The row therefore stays with the technique, which is where the column defs
    and the registry entry are minted anyway.
    """
    if "schema:additionalProperty" in path:
        return False
    return not any(prop in path for prop in set(e.KEYED_TABLES) | e.DEFAULT_ROW_ARRAYS)


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


def module_blocks(name):
    """{block -> [field]} for a conditional module, else None. Declared in the module's own .json.

    ReportingCore is the only one today, but the flag is what is tested, not the name: a consuming
    TAPP takes only the blocks that apply to it, so composing the whole module would give a
    technique fields its own table deliberately omits. See docs/REPORTINGCORE_BLOCKS.md.
    """
    p = os.path.join(MODDIR, f"Module_{name}.json")
    if not os.path.exists(p):
        return None
    j = json.load(open(p, encoding="utf-8"))
    if not j.get("conditional"):
        return None
    return {b["name"]: list(b.get("fields") or []) for b in j.get("blocks") or []}


def build_schema(name, only=None):
    """({root -> subschema}, stats) from the module's sidecar paths.

    `only` limits the build to a set of field names — how a conditional module gets one $def per
    block rather than one covering everything.
    """
    rows = module_rows(name)
    spec = schemapath_io.load_spec(schemapath_io.csv_path(os.path.join(MODDIR, f"Module_{name}.csv")))
    meta = {i: (P, A, dt, d) for i, P, A, dt, d in rows
            if only is None or i in only}
    roots = {"MethodDefinition": e.Obj(), "Dataset": e.Obj()}
    # Object-level requiredness is NOT carried in the tree — Obj has no `required`, and
    # schema_path_emitter.build() accumulates it separately for wrap() to apply. Calling
    # insert()/to_schema() directly therefore loses it silently, which is how the first run of this
    # generator produced four modules asserting nothing required at all. Same condition as build():
    # a Basic tier, on a path that is a single top-level direct property.
    required = {"MethodDefinition": [], "Dataset": []}
    shacl_top = {"MethodDefinition": set(), "Dataset": set()}
    used, placed, unplaced, params = set(), 0, [], []
    emitted = {}
    for item, (P, A, dt, desc) in meta.items():
        paths = spec.get(item, {}).get("path")
        paths = ([paths] if isinstance(paths, str) else list(paths or []))
        paths = [p for p in paths if p]
        if not paths:
            unplaced.append(item)
            continue
        for path in paths:
            # A module $def must not constrain schema:additionalProperty. The consuming technique
            # already constrains that array as a closed anyOf over the parameters its own table
            # enumerates, and allOf makes every element satisfy both — so two universal constraints
            # on one array can never both hold. Parameters stay with the technique; see
            # module_composition._is_composable. 54 of the 105 module paths remain, all 22 of
            # Group1's among them.
            if not is_composable(path) and "schema:additionalProperty" not in path:
                # A keyed-table column or default-row array: not composable, and not a parameter
                # either, so it is neither emitted here nor published as a Param_ $def. The
                # technique keeps its own row (module_composition._is_composable agrees, so the
                # overlay is not dropped).
                unplaced.append(item)
                continue
            if "schema:additionalProperty" in path:
                # Collected, not composed. See emit_parameter_defs: the module publishes one $def
                # per parameter so a technique can UNION them into its own anyOf. Nothing $refs
                # these yet - wiring that is a separate, reviewable step - so emitting them changes
                # no technique schema today.
                params.append((item, P, A, dt, desc, path))
                continue
            parsed = spp.parse(path)
            require = (P == "Basic") if parsed.root == "MethodDefinition" else (A == "Basic")
            e.insert(roots[parsed.root], parsed, e.leaf_for(desc, dt), require=require)
            # Recorded HERE, at the one point an insertion actually happens, and reported out as
            # `emitted`. module_composition reads it rather than re-deriving coverage from the
            # sidecar: the sidecar says where a field SHOULD go, the built $def says where it DID,
            # and those two diverge whenever a module BB has not been rebuilt since its sidecar
            # changed. That divergence silently deleted `Limit of Quantification (LOQ) Method`
            # from nine ICP-MS schemas on 2026-09-03 -- the planner called the field covered, so
            # simplify_sidecars blanked every technique's row, while the stale $def carried
            # nothing. Because this manifest is written by the same run that writes the schema,
            # a stale build now yields a stale manifest that AGREES with it, and coverage fails
            # closed instead of open.
            emitted.setdefault(ms._norm(ms.rename(item)), set()).add(parsed.root)
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
        sch = _reref_module_depth(e.to_schema(node))
        if sch.get("properties"):
            if required[r]:
                sch = {**sch, "required": sorted(required[r])}
            out[r] = sch
    return out, {"fields": len(meta), "placed": placed, "unplaced": unplaced,
                 "emitted": {k: sorted(v) for k, v in emitted.items()},
                 "param_defs": emit_parameter_defs(name, params), "params": params,
                 "prefixes": sorted(used & set(PREFIX_IRI)),
                 "shacl_top": {r: sorted(v) for r, v in shacl_top.items()}}


def _reref_module_depth(obj):
    """Rewrite emitter $refs from technique-schema depth to module depth.

    `schema_path_emitter`'s REF_MAP writes BaseSchema $refs at technique-schema depth
    (`_sources/techniqueProfile/geochemProfile/<T>/tapp/` — four hops up to `_sources`, hence
    `../../../../BaseSchema/...`). A module BB lives at `_sources/BaseSchema/modules/<name>/`, two
    hops shallower, so the same target is `../../<X>`. Without this, a module that places a field on
    e.g. `schema:instrument` emits a $ref that climbs past the repo root and the OGC postprocess
    fails with "target file does not exist" (only branch CI catches it, not validate_examples)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str) and v.startswith("../../../../BaseSchema/"):
                obj[k] = "../../" + v[len("../../../../BaseSchema/"):]
            else:
                _reref_module_depth(v)
    elif isinstance(obj, list):
        for v in obj:
            _reref_module_depth(v)
    return obj


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
    for defname, (r, sch, label) in defs.items():
        doc["$defs"][defname] = {"title": f"{label} on the "
                                 f"{'procedure' if r == 'MethodDefinition' else 'analysis'}",
                                 "description": DEF_BLURB[r], **sch}
    return doc


def write_bb(name, doc, stats, composed_by):
    d = os.path.join(BBDIR, dirname(name))
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
          "link": "https://github.com/amds-ldeo/geochemBuildingBlocks",
          "maturity": "draft", "scope": "unstable",
          "tags": ["ada", "astromat", "tapp", "composition-module", "profile",
                   re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()],
          "sources": [{"title": f"TAPP Module {name} (2026-08-11 library)",
                       "link": "https://github.com/amds-ldeo/geochemBuildingBlocks"},
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


def emit_parameter_defs(module, params):
    """One $def per parameter the module declares, keyed Param_<Side>_<name>.

    A module $def cannot CONSTRAIN schema:additionalProperty - the technique already closes that
    array with an anyOf over its own parameters, and allOf would make the two unsatisfiable
    together. It can however PUBLISH a branch that a technique unions into its own anyOf, which is
    what these are for.

    SHAPE IS NOT DEFINED HERE. A parameter has two established shapes, and which one applies is
    decided by the side it sits on, not by the module:

      Procedure  -> build_tapp.param_template_def  (schema:PropertyValueSpecification, the
                    method-level template: schema:valueName, ada:dataType, ada:fieldScope,
                    schema:readonlyValue, ada:tier)
      Analysis   -> build_tapp.param_value_def     (schema:PropertyValue, the per-dataset value:
                    schema:propertyID, schema:value)

    Both carry schema:unitText whenever the Data Type column names a unit - required on the value
    side, a const on the template side. Delegating rather than restating the shape here is the
    point: an earlier hand-rolled variant emitted a hybrid of the two (ada:dataType and
    schema:valueName on BOTH sides, no propertyID, no unitText), which made every module parameter
    differ structurally from the technique parameter it duplicates - 181 spurious conflicts that
    were one defect, not 181 decisions.

    IDENTITY. A technique mints `ada:parameter/<TAPP>/<name>`, so the same logical parameter exists
    once per consuming TAPP. A module-owned parameter gets ONE identity instead:
    `ada:parameter/module/<Module>/<name>`. Adopting it changes the @id wherever a module supplies
    the parameter; that was settled deliberately in favour of single identity.
    """
    import re as _re
    import build_tapp as bt

    out = {}
    for item, P, A, dt, desc, path in params:
        side = "Procedure" if path.startswith("$MethodDefinition") else "Analysis"
        m = _re.search(r"schema:additionalProperty\[schema:name='([^']*)'\]", path)
        label = m.group(1) if m else item
        vname = _re.sub(r"[^A-Za-z0-9]+", " ", label).title().replace(" ", "")
        vname = vname[:1].lower() + vname[1:]
        b = {"item": label, "name": vname, "P": P, "A": A, "desc": desc or label,
             "jtype": bt.jtype(dt), "unit": bt.unit(dt)}
        # The canonical emitters read PARAM_BASE (the @id stem) and CFG["prefix"] (the registry
        # $def key) from build_tapp module state, which configure() sets per TECHNIQUE. A module is
        # not a technique, so stand in for that state across the call and restore it after.
        saved_base, saved_cfg = bt.PARAM_BASE, bt.CFG
        bt.PARAM_BASE = "ada:parameter/module/%s" % module
        bt.CFG = {"prefix": "module"}
        try:
            emit = bt.param_template_def if side == "Procedure" else bt.param_value_def
            _key, block = emit(b, None)
        finally:
            bt.PARAM_BASE, bt.CFG = saved_base, saved_cfg
        blk = next(iter(block.values()))
        # A parameter placed on schema:variableMeasured is a DATASET VARIABLE as well as a
        # PropertyValue: the base shape requires @type to contain cdi:InstanceVariable, and a def
        # pinning @type to ["schema:PropertyValue"] alone is unsatisfiable there. schema_path_emitter
        # applies the same rule to technique-minted parameters; a module-supplied one now composes
        # into the very same slot, so it needs it too.
        if "schema:variableMeasured" in path:
            tc = ((blk.get("properties") or {}).get("@type") or {})
            if isinstance(tc.get("const"), list) and "cdi:InstanceVariable" not in tc["const"]:
                tc["const"] = tc["const"] + ["cdi:InstanceVariable"]
        out["Param_%s_%s" % (side, vname)] = blk
    return out


def write_examples(d, name, doc):
    import jsonschema
    ex, problems = [], []
    for defname, sub in doc["$defs"].items():
        if defname.startswith("Param_"):
            continue          # a published parameter branch, not an instance shape
        inst = _sample(sub)
        # A module $def may $ref a sibling building block by relative path
        # (../../geochemProduct/schema.yaml#/$defs/UsedComputationalTool). jsonschema cannot follow
        # a relative FILE ref - it falls back to urllib and raises Unresolvable - so the sample is
        # checked against the module's own constraints and any cross-BB ref is left to the resolved
        # schema, which is where those refs are inlined and where CI checks them. Reporting an
        # unresolvable ref as an example PROBLEM would be reporting a limitation of this check.
        try:
            errs = list(jsonschema.Draft202012Validator(
                {"$schema": "https://json-schema.org/draft/2020-12/schema", **sub}).iter_errors(inst))
        except Exception as e:
            if "Unresolvable" not in type(e).__name__ and "Unresolvable" not in str(e):
                raise
            errs = []
            problems.append((defname, "not checked here: cross-BB $ref (%s)" % str(e)[-60:]))
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
    # A PARAMETER-ONLY module (blank, calibrationFactor) has no root $def, so the loop above
    # produces nothing and the module would ship an empty examples.yaml. Its published parameters
    # are the only instance shape it has, so demonstrate those instead - one example per parameter,
    # which is exactly what a consuming TAPP unions into its own schema:additionalProperty anyOf.
    if not ex:
        for defname, sub in doc["$defs"].items():
            if not defname.startswith("Param_"):
                continue
            inst = _sample(sub)
            errs = list(jsonschema.Draft202012Validator(
                {"$schema": "https://json-schema.org/draft/2020-12/schema", **sub}).iter_errors(inst))
            if errs:
                problems.append((defname, errs[0].message[:120]))
            side = "procedure" if defname.startswith("Param_Procedure") else "analysis"
            ex.append({
                "title": f"{name} published parameter ({defname})",
                "content": (f"A parameter the {name} module publishes for the {side} side. The module "
                            f"places no root fields, so its parameters are what it contributes: a "
                            f"consuming TAPP unions this branch into its own additionalProperty anyOf."),
                "prefixes": {pf: PREFIX_IRI[pf] for pf in sorted(_prefixes_in(inst))},
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
        if defname.startswith("Param_"):
            continue          # published parameter branch: no target class, no sample
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
        if defname.startswith("Param_"):
            continue          # published parameter branch: no target class, no sample
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
              f"- $ref: ../../../BaseSchema/modules/{dirname(name)}/schema.yaml"
              "#/$defs/ProcedureIdentification", "- type: object",
              "  properties: {}   # only what this technique itself owns", "```", "",
              "`allOf` composes constraints and cannot relax them: a technique composing this "
              "module accepts its required set in full.", ""]
    with open(os.path.join(d, "description.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def main():
    manifest = {}
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    man = json.load(open(tapp_source.manifest_path(), encoding="utf-8"))
    usage = collections.Counter()
    for entry in man.get("composed") or []:
        for m in entry.get("modules") or []:
            usage[m.get("name")] += 1

    names = a.module or [f[len("Module_"):-4] for f in sorted(os.listdir(MODDIR))
                         if f.startswith("Module_") and f.endswith(".csv")
                         and not f.endswith(".schemapaths.csv")]   # the sidecars sit alongside
    for name in names:
        # Group1 was hand-written as the pilot, before this generator existed, and it is a THIN
        # profile: it asserts schema:relatedLink is an array without saying what is in one. That was
        # harmless while nothing composed it, and became a real loss the moment techniques started
        # dropping their own rows in its favour — 210 property paths went missing across twelve
        # schemas, because the module replaced structure with a stub. Generated from its sidecar it
        # carries the same shape the techniques had.
        if not usage.get(name):
            print(f"{name:<22s} skipped (composed by no table in the manifest)")
            continue
        whole, stats = build_schema(name)
        if not whole and stats.get("param_defs"):
            # Every placement is a parameter, so there is no root $def to build - but the module
            # still has something to publish. Blank and CalibrationFactor are entirely this: one
            # field each, both parameters. Reporting them as "unplaced" conflated them with
            # Geochronology/UPb, whose fields have no placement anywhere; these have placements
            # that a module cannot CONSTRAIN, only publish.
            print(f"{name:<22s} parameters only — {len(stats['param_defs'])} published, "
                  f"no root $def (a module cannot constrain schema:additionalProperty)")
            doc = render(name, {}, stats, usage[name])
            doc.setdefault("$defs", {}).update(stats["param_defs"])
            if a.write:
                d = write_bb(name, doc, stats, usage[name])
                # examples too: a BB with none fails the audit, and this module's published
                # parameters are a perfectly good instance shape to demonstrate.
                problems = write_examples(d, name, doc)
                write_description(d, name, doc, stats, usage[name])
                print(f"{'':22s} wrote {os.path.relpath(d, ROOT)}")
                for defname, msg in problems:
                    print(f"{'':22s} EXAMPLE FAILS {defname}: {msg}")
            continue
        if not whole:
            print(f"{name:<22s} CANNOT GENERATE — all {stats['fields']} fields unplaced "
                  f"({', '.join(stats['unplaced'][:4])}{'…' if len(stats['unplaced']) > 4 else ''})")
            continue

        # A conditional module gets one $def per block per side, so a consumer composes only the
        # blocks its manifest entry selects. Composing the whole of ReportingCore would hand
        # Lab-XCT a Procedural Blank Level for a technique with no blank — and five of its six
        # fields are Basic on some tier, so most such additions become requirements the table never
        # stated. allOf cannot relax a constraint, so the selection has to happen here.
        blocks = module_blocks(name)
        defs = {}
        if blocks:
            for blk, fields in blocks.items():
                sub, _ = build_schema(name, only=set(fields))
                camel = "".join(w.capitalize() for w in blk.split("_"))
                for r, sch in sub.items():
                    side = "Procedure" if r == "MethodDefinition" else "Analysis"
                    defs[f"{camel}_{side}"] = (r, sch, f"{name} · {blk}")
        for r, sch in whole.items():
            side = "Procedure" if r == "MethodDefinition" else "Analysis"
            key = f"AllBlocks_{side}" if blocks else DEF_NAME[r]
            defs[key] = (r, sch, f"{name} (all blocks)" if blocks else name)

        doc = render(name, defs, stats, usage[name])
        # Published for a technique to union into its own parameter anyOf. Added AFTER render so
        # they bypass the root->$def mapping, which only knows MethodDefinition/Dataset.
        if stats.get("param_defs"):
            doc.setdefault("$defs", {}).update(stats["param_defs"])
        manifest[name] = stats.get("emitted") or {}
        halves = ", ".join(defs)
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
    if a.write:
        # Written by the same run that writes the schemas, so it is exactly as fresh as they are.
        # module_composition treats a module absent from here as composing nothing, which is the
        # safe direction: a technique keeps its own row rather than losing the field.
        with open(EMITTED_PATH, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"generated_by": "tools/build_module_bb.py --write",
                       "note": ("What each module's $defs ACTUALLY carry, per root. Read by "
                                "module_composition.plan() instead of re-deriving coverage from "
                                "the sidecars, so the planner cannot claim a field the built $def "
                                "does not have. Regenerated with the schemas; never hand-edit."),
                       "modules": {k: manifest[k] for k in sorted(manifest)}},
                      f, indent=2, sort_keys=False)
            f.write("\n")
        print(f"{'':22s} wrote {os.path.relpath(EMITTED_PATH, ROOT)} "
              f"({sum(len(v) for v in manifest.values())} field placements)")
    else:
        print("\n(dry run — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
