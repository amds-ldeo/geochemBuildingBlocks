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

    python tools/build_pathdriven.py <tapp>          # e.g. semTAPP
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

_REG_RE = re.compile(r"/(parameterTemplates|parameterValues|analyteColumns|reportedPropertyColumns|channelColumns)/schema\.yaml#/\$defs/(.+)$")


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
    "reportedPropertyColumns": "ada:reportedPropertyColumn/",
    "channelColumns": "ada:channelColumn/",
    "parameterTemplates": "ada:parameter/",
    "parameterValues": "ada:parameter/",
}


def _def_id(body):
    return str(((body.get("properties") or {}).get("@id") or {}).get("const", ""))


def _write_registry(reg_name, defs, tapp):
    """Publish this TAPP's generated $defs into the shared registry file by UPSERT.

    Keyed on the def's @id const (its true identity), not the $def key:
      - an @id already present has its BODY REPLACED, under its EXISTING key so `$ref`s survive
      - an @id not present is inserted
      - nothing is ever deleted

    Upsert, not replace-by-ownership. Replacement was tried and is wrong here: the legacy matrix
    route (build_tapp/_tapp_lib, reading the richer annotated workbooks) and the path-driven route
    read DIFFERENT sources with different coverage — EPMA has 26 analyte columns in the registry but
    only 2 rows in its schema-path sidecar — so replacing a TAPP's entries destroys 24 real EPMA
    columns, ~46 parameterTemplates and ~136 parameterValues no path-driven run reproduces.

    Pure-additive was tried too, and is what this replaces: it SKIPPED any @id already present, so a
    corrected generator could never update a def that already existed. That silently blocked two
    separate fixes — the tier/defaultValue rules on parameter templates and on analyte columns —
    each of which reached only the handful of defs whose @id happened to be new. Upsert keeps the
    non-destructive property while letting a regenerated body actually land.

    Consequence: entries the path-driven route no longer generates are still NOT pruned. Converging
    the two routes remains a separate decision; the registry stays a union.
    """
    path = os.path.join(b.ROOT, "_sources", "registry", reg_name, "schema.yaml")
    if not os.path.exists(path):
        print(f"  registry {reg_name}: {path} missing, skipped")
        return
    with open(path, encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    existing = doc.get("$defs") or {}
    key_by_id = {_def_id(v): k for k, v in existing.items()}
    merged = dict(existing)
    updated = added = same = 0
    for k, v in defs.items():
        prior = key_by_id.get(_def_id(v))
        if prior is None:
            merged[k] = v
            added += 1
        elif merged[prior] == v:
            same += 1
        else:
            merged[prior] = v      # keep the established key; $refs point at it
            updated += 1
    if not (added or updated):
        print(f"  registry {reg_name}: {tapp} already current ({same} unchanged), no change")
        return
    doc["$defs"] = dict(sorted(merged.items()))
    b.write(path, b.dump_yaml(doc))
    print(f"  registry {reg_name}: {tapp} +{added} new, ~{updated} updated, {same} unchanged; "
          f"{len(doc['$defs'])} total")


def registry_diff(tapp):
    """Report what switching this TAPP's registry merge to replace-by-ownership would do.

    The merge is currently ADDITIVE (see _write_registry): it only ever adds, so the registry
    still holds legacy-route defs the schema-path sidecar does not reproduce. Replacing would make
    the sidecar authoritative — deleting a TAPP's entire existing set and rewriting it — which is
    the goal, but only once the sidecar's coverage has caught up.

    This answers that question without writing anything: for each registry it compares the @ids the
    sidecar generates against the @ids the registry currently holds for this TAPP.

      WOULD DELETE  in the registry, not generated -> a sidecar row still missing (or a genuinely
                    retired column, which only you can tell apart)
      WOULD ADD     generated, not yet in the registry
      unchanged     present in both

    Exit status is 0 when nothing would be deleted (safe to replace) and 1 otherwise, so it can
    gate a script.
    """
    b.configure(tapp)

    # Pre-flight: parse each sidecar path on its own. e.build() dies on the first bad one with a
    # bare traceback, which is useless mid-review — report every malformed row instead.
    import schemapath_io
    import schema_path_parser
    spec = schemapath_io.load_spec(schemapath_io.csv_path(b.XLSX))
    malformed = []
    for item, rec in spec.items():
        for p in (rec["path"] if isinstance(rec["path"], list) else [rec["path"]]):
            try:
                schema_path_parser.parse(p)
            except Exception as ex:
                malformed.append((item, p, str(ex)))
    if malformed:
        print(f"{len(malformed)} unparseable Schema Path(s) in the {tapp} sidecar — fix these first:\n")
        for item, p, msg in malformed:
            print(f"  {item}\n     {p}\n     -> {msg}\n")
        return 1

    _, registries, _ = e.build(tapp)

    print(f"registry diff for {tapp} — what replace-by-ownership would do\n")
    total_del = 0
    for reg_name in ("analyteColumns", "reportedPropertyColumns", "channelColumns",
                     "parameterTemplates", "parameterValues"):
        path = os.path.join(b.ROOT, "_sources", "registry", reg_name, "schema.yaml")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            existing = (yaml.safe_load(f) or {}).get("$defs") or {}

        owned = f"{_REGISTRY_ID_PREFIX[reg_name]}{tapp}/"
        # key by @id, the stable identity: $def keys changed when they were namespaced by TAPP,
        # so comparing keys would report every legacy entry as deleted-and-re-added.
        have = {_def_id(v): k for k, v in existing.items() if _def_id(v).startswith(owned)}
        gen = {_def_id(v): k for v, k in ((v, k) for k, v in registries.get(reg_name, {}).items())}

        to_delete = sorted(set(have) - set(gen))
        to_add = sorted(set(gen) - set(have))
        same = len(set(have) & set(gen))
        total_del += len(to_delete)

        verdict = "SAFE" if not to_delete else f"{len(to_delete)} WOULD BE DELETED"
        print(f"  {reg_name}: {len(have)} owned in registry, {len(gen)} generated, "
              f"{same} unchanged  -> {verdict}")
        for i in to_delete:
            print(f"      - DELETE  {have[i]:38s} {i}")
        for i in to_add:
            print(f"      + ADD     {gen[i]:38s} {i}")

    print()
    if total_del:
        print(f"NOT safe to replace yet: {total_del} def(s) would be lost. Each is either a "
              f"sidecar row still to map, or a column genuinely retired from the workbook.")
    else:
        print("Safe to replace: the sidecar reproduces everything the registry holds for this TAPP.")
    return 1 if total_del else 0


def build_pathdriven(tapp, write_registries=True):
    b.configure(tapp)
    overlays, registries, required = e.build(tapp)

    # ---- shared registries: publish this TAPP's generated analyte columns so the catalog covers
    # every technique, not just the two the legacy route happened to write. The schemas below still
    # INLINE the defs (see the note on the TAPP schema); publishing and inlining are independent.
    #
    # Only the keyed-table registries. The parameter registries hold ~180 legacy-route defs the
    # path-driven route does not regenerate, so publishing there would add a second, namespaced
    # copy of everything alongside them — churn without a decision on converging the two routes.
    if write_registries:
        for _reg in ("analyteColumns", "reportedPropertyColumns", "channelColumns"):
            if registries.get(_reg):
                _write_registry(_reg, registries[_reg], tapp)

    # ---- TAPP schema: MethodDefinition overlay over the base tappDefinition.
    # Inline the parameter defs (like the detail) rather than $ref the shared registry: the shared
    # registry keys defs by bare name, so a param name shared with another TAPP (e.g. laicpms)
    # resolves to that TAPP's def — including its per-TAPP @id const — which the geochron example's
    # (geochron-@id'd) parameter instances then fail. Inlining from THIS TAPP's in-memory registry
    # keeps schema and example on the same @ids.
    md = _inline_registry_refs(overlays["MethodDefinition"], registries, {})
    # Compose the modules this TAPP's manifest entry names. ReportingCore contributes one $def per
    # BLOCK, so a technique takes only the blocks that apply to it — see docs/REPORTINGCORE_BLOCKS.md.
    import module_composition as mc
    _refs, _ = mc.plan(b.XLSX)
    # ada:analyticalMode is PLACED by the core module — one shared $def across all 16
    # techniques — but its options are this technique's own mode columns (the Y/N block
    # between 'Keyed By' and 'Literature Assessment'). The enum therefore cannot live in the
    # module, and the technique contributes it as a NARROWING: wrap() puts the overlay in its
    # own allOf branch, so {items: {enum: ...}} intersects with the module's unconstrained
    # array rather than redefining it. Without this a procedure may declare any mode string,
    # including one its own table does not define. Skipped for a single-mode technique (the
    # Solution trio has no mode columns): an empty enum would admit nothing at all.
    _modes = b.mode_names()
    if _modes:
        md.setdefault("properties", {})["ada:analyticalMode"] = {
            "type": "array", "items": {"type": "string", "enum": _modes}}
    tapp_schema = e.wrap("MethodDefinition", md, required["MethodDefinition"],
                         title=b.CFG.get("title"), description=b.CFG.get("description"),
                         module_refs=mc.ref_objects(_refs, "MethodDefinition"))
    b.write(os.path.join(b.TAPP_DIR, "schema.yaml"), b.dump_yaml(tapp_schema))

    # ---- detail schema: standalone Dataset overlay, PropertyValue defs inlined
    ds = _inline_registry_refs(overlays["Dataset"], registries, {})
    detail = {"$schema": "https://json-schema.org/draft/2020-12/schema",
              "title": b.CFG.get("detail_title"), "description": b.CFG.get("detail_description")}
    ds_refs = mc.ref_objects(_refs, "Dataset")
    if ds_refs:
        # the detail is a standalone overlay, so its own body becomes one allOf branch beside the
        # module refs rather than sitting at the root
        body = {k: v for k, v in ds.items() if k not in ("$schema", "title", "description")}
        if required["Dataset"]:
            body["required"] = required["Dataset"]
        detail["allOf"] = [*ds_refs, body]
    else:
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
    # ---- resolvedSchema.json: the flattened form, and the ONLY thing --validate reads.
    # Nothing used to regenerate it, so every schema.yaml written above silently drifted from its
    # resolution: --validate then compared a freshly-built example against a stale schema and
    # reported failures that were neither the example's nor the schema's fault. Rebuild both here,
    # so the build leaves the pair consistent and validation tests what was actually just built.
    #
    # Resolved BEFORE the examples are written, because filling their @type discriminators needs
    # the resolved schema — see ex.fill_required_types.
    tapp_res = _resolve(os.path.join(b.TAPP_DIR, "schema.yaml"))
    detail_res = _resolve(os.path.join(b.DETAIL_DIR, "schema.yaml"))
    tapp_sch = json.load(open(tapp_res, encoding="utf-8"))
    detail_sch = json.load(open(detail_res, encoding="utf-8"))
    n1 = ex.fill_required_types(tapp_inst, tapp_sch)
    n2 = ex.fill_required_types(detail_inst, detail_sch)
    if n1 or n2:
        print(f"  filled {n1 + n2} required @type discriminator(s) in the examples")
    # @type first: typing a node is what exposes the rest of what its branch requires.
    g1 = ex.fill_structural_gaps(tapp_inst, tapp_sch)
    g2 = ex.fill_structural_gaps(detail_inst, detail_sch)
    if g1 or g2:
        print(f"  filled {g1 + g2} structural gap(s) (instrument name / Wikidata term)")

    _write_json(os.path.join(b.TAPP_DIR, f"example{tapp}-P0.json"), tapp_inst)
    _write_json(os.path.join(b.DETAIL_DIR, f"exampledetail{short}-P0.json"), detail_inst)

    print(f"DONE {tapp}: TAPP overlay {len(overlays['MethodDefinition'].get('properties', {}))} props; "
          f"detail {len(ds.get('properties', {}))} props; required MD={required['MethodDefinition']} "
          f"DS={required['Dataset']}")


def _resolve(schema_yaml):
    """Rewrite resolvedSchema.json beside a schema.yaml we just emitted; return its path."""
    import pathlib
    import resolve_schema
    out = resolve_schema.resolve_and_write_structured(pathlib.Path(schema_yaml).resolve())
    print(f"  resolved {os.path.relpath(schema_yaml, b.ROOT)} -> {os.path.basename(out)}")
    return out


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
        raise SystemExit("usage: build_pathdriven.py <tapp> [--validate | --registry-diff]\n"
                         "  (run build_tapp.py <tapp> first)\n"
                         "  --registry-diff  show what replace-by-ownership would add/delete; writes nothing")
    if "--validate" in sys.argv:
        sys.exit(validate(args[0]))
    if "--registry-diff" in sys.argv:
        sys.exit(registry_diff(args[0]))
    build_pathdriven(args[0])
