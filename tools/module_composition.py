#!/usr/bin/env python3
"""Which module $defs a TAPP composes, and which of its rows those modules already cover.

Wiring composition is two halves that must agree. A technique schema gains a `$ref` per module
`$def`, and the rows those modules supply stop being emitted into its own overlay — otherwise every
shared field is defined twice, and the technique's copy silently wins wherever the two differ.

The safety property is that the second half NEVER runs ahead of the first: a row is dropped from the
overlay only if a module `$def` demonstrably provides it, which means the module has that field, the
field has a placement in the module's sidecar, and the `$def` for that side actually exists. A
module field with no path contributes nothing, so the technique must keep its own row.

`ReportingCore` is conditional — see docs/REPORTINGCORE_BLOCKS.md. It exposes one `$def` per block
per side, and a consumer composes only the blocks its manifest entry names, so what it covers
differs per TAPP.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import migrate_sidecar as ms
import schemapath_io
import tapp_source as ts

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BBDIR = os.path.join(ROOT, "_sources", "BaseSchema", "modules")
# The directory a module BB lives in. Imported from build_module_bb rather than mirrored: the two
# copies drifted the moment a new module arrived - this one still lowercased TargetSelection to
# `targetselection` after the builder had been taught lowerCamelCase, so composition emitted a $ref
# to a directory that does not exist. One definition, one behaviour.
from build_module_bb import DIRNAME, dirname, is_composable
SIDE = {"MethodDefinition": "Procedure", "Dataset": "Analysis"}
_BB_CACHE = {}


def _bb(name):
    """The generated building block's schema, or None if it was never built."""
    if name not in _BB_CACHE:
        p = os.path.join(BBDIR, dirname(name), "schema.yaml")
        _BB_CACHE[name] = yaml.safe_load(open(p, encoding="utf-8")) if os.path.exists(p) else None
    return _BB_CACHE[name]


def _manifest_entry(source_path):
    """The composed_tapps.json entry for a table, matched on FILENAME.

    The manifest records per-technique paths while a delivery may lay its tables out flat, so the
    literal path resolves against neither reliably.
    """
    mp = ts.manifest_path()
    if not mp:
        return None
    want = os.path.basename(str(source_path))
    for e in (json.load(open(mp, encoding="utf-8")).get("composed") or []):
        if os.path.basename(e.get("tapp", "")) == want:
            return e
    return None


def _blocks(name):
    """{block -> [field]} for a conditional module, else None."""
    p = os.path.join(ts.modules_dir(), f"Module_{name}.json")
    if not os.path.exists(p):
        return None
    j = json.load(open(p, encoding="utf-8"))
    if not j.get("conditional"):
        return None
    return {b["name"]: list(b.get("fields") or []) for b in j.get("blocks") or []}


def _is_composable(path):
    """True unless the path lands inside `schema:additionalProperty`.

    That one container cannot be composed through allOf. A technique constrains it as a CLOSED
    anyOf over the parameters it enumerates, and allOf makes every array element satisfy the
    technique's branch AND the module's — so a module parameter matches no technique branch, and a
    technique parameter fails the module's. Two universal constraints on one array cannot both hold
    unless each side already knows about the other, which defeats composing them.

    Everything else composes: top-level properties, the instrument tree, workflow steps, dqv
    measurements, the provenance activity.

    Parameters therefore stay with the technique, which is not harmful duplication: the technique
    enumerates which parameters exist — its own table lists them — and the module says what they
    mean. That is the owned-versus-overlay division the library already uses. Since the 2026-09
    delivery the same reasoning covers keyed-table column arrays and default-row arrays; the
    predicate lives in build_module_bb so this planner and that generator cannot drift apart.
    """
    return is_composable(path)


_EMITTED = None


def _module_placed(name):
    """{normalized field -> {roots where the module ACTUALLY carries it}}.

    Read from docs/modules/emitted.json, which build_module_bb writes in the same run that writes
    the schemas — NOT re-derived from the module sidecar. The two answer different questions: the
    sidecar says where a field SHOULD go, the built $def says where it DID, and they diverge for
    as long as a module BB has not been rebuilt since its sidecar changed.

    That divergence is not hypothetical. On 2026-09-03 two commits edited module sidecars without
    rebuilding the BBs; this function still read the sidecars, reported `Limit of Quantification
    (LOQ) Method` as covered, and simplify_sidecars duly blanked the row in all nine ICP-MS
    techniques while the stale $def carried nothing. The field vanished from nine schemas and
    validate_examples stayed green throughout, because dropping a constraint only makes a schema
    more permissive.

    Reading the manifest makes a stale build fail CLOSED: the manifest is as stale as the schema
    it was written beside, so the two agree, coverage is under-reported, and a technique keeps its
    own row. A missing manifest means the same — compose nothing.
    """
    global _EMITTED
    if _EMITTED is None:
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "docs", "modules", "emitted.json")
        try:
            with open(path, encoding="utf-8") as f:
                _EMITTED = json.load(f).get("modules") or {}
        except (OSError, ValueError):
            _EMITTED = {}
    return {k: set(v) for k, v in (_EMITTED.get(name) or {}).items()}


def plan(source_path):
    """([(module, [$def names]) ...], {root -> {normalized item}}) for one TAPP.

    The second element is what its overlay must stop emitting, per root.
    """
    entry = _manifest_entry(source_path)
    if not entry:
        return [], {"MethodDefinition": set(), "Dataset": set()}

    refs, covered = [], {"MethodDefinition": set(), "Dataset": set()}
    for m in entry.get("modules") or []:
        name = m.get("name")
        bb = _bb(name) if name else None
        if not bb:
            continue                      # module not built yet — compose nothing, keep every row
        defs = bb.get("$defs") or {}
        placed = _module_placed(name)
        blocks = _blocks(name)
        chosen = m.get("blocks")

        # which of the module's fields this consumer actually takes
        if blocks:
            if not chosen or str(chosen).strip() == "all":
                fields = [f for fs in blocks.values() for f in fs]
                names = ["AllBlocks"]
            else:
                want = {c.strip() for c in str(chosen).split(",") if c.strip()}
                fields = [f for k, fs in blocks.items() if k in want for f in fs]
                names = ["".join(w.capitalize() for w in k.split("_")) for k in blocks if k in want]
        else:
            fields = list(placed)          # non-conditional: everything it places
            names = ["ProcedureIdentification", "AnalysisIdentification"]

        got = []
        for base in names:
            for root, side in SIDE.items():
                dn = base if base.endswith(("Identification",)) else f"{base}_{side}"
                if base.endswith("Identification"):
                    dn = base
                    if SIDE[root] not in base:
                        continue
                if dn not in defs:
                    continue
                got.append(dn)
                # a row is only droppable where the module both PLACES it on this root and the
                # $def for that root exists
                for f in fields:
                    k = ms._norm(ms.rename(f))
                    if root in placed.get(k, set()):
                        covered[root].add(k)
        if got:
            refs.append((name, sorted(set(got))))
    return refs, covered


def ref_objects(refs, root, depth=4):
    """[{$ref: …}] for one side, as they appear in a technique schema's allOf.

    Four levels up from techniqueProfile/geochemProfile/<tech>/<bb>/ reaches _sources."""
    up = "../" * depth
    out = []
    for name, defs in refs:
        d = dirname(name)
        for dn in defs:
            if dn.endswith("Identification"):
                if SIDE[root] not in dn:
                    continue
            elif not dn.endswith(f"_{SIDE[root]}"):
                continue
            out.append({"$ref": f"{up}BaseSchema/modules/{d}/schema.yaml#/$defs/{dn}"})
    return out


if __name__ == "__main__":
    import build_tapp as b
    for t in sorted(b.TAPP_CONFIGS):
        b.configure(t)
        refs, covered = plan(b.XLSX)
        n = sum(len(d) for _, d in refs)
        print(f"{t:<22s} {len(refs)} module(s), {n:2d} $def(s)   "
              f"covers MD={len(covered['MethodDefinition']):2d} DS={len(covered['Dataset']):2d}")
        for name, defs in refs:
            print(f"      {name}: {', '.join(defs)}")


def param_refs(source_path, depth=4):
    """{(normalized item, root) -> {$ref}} for every PARAMETER a composed module supplies.

    A module publishes its parameters as separate Param_<Side>_<name> $defs, NOT inside its root
    $def - a module cannot constrain schema:additionalProperty, it can only offer a branch the
    technique unions into its own anyOf. So a parameter row that plan() reports as covered would,
    if simply dropped, vanish from the technique's schema altogether while its instances still carry
    it. This maps such a row to the module branch that replaces it.

    The $def name is derived the same way build_module_bb.emit_parameter_defs derives it: from the
    schema:name selector of the module sidecar's path, camelised.
    """
    import re
    entry = _manifest_entry(source_path)
    out = {}
    if not entry:
        return out
    for m in entry.get("modules") or []:
        name = m.get("name")
        bb = _bb(name) if name else None
        if not bb:
            continue
        defs = bb.get("$defs") or {}
        src = os.path.join(ts.modules_dir(), f"Module_{name}.csv")
        sc = schemapath_io.csv_path(src)
        if not os.path.exists(sc):
            continue
        for r in schemapath_io.read(sc):
            it = (r.get("Metadata Item") or "").strip()
            path = (r.get("Schema Path") or "").strip()
            if not it or not path:
                continue
            sel = re.search(r"schema:additionalProperty\[schema:name='([^']*)'\]", path)
            if not sel:
                continue                  # not a parameter placement
            root = "Dataset" if path.startswith("$Dataset") else "MethodDefinition"
            vname = re.sub(r"[^A-Za-z0-9]+", " ", sel.group(1)).title().replace(" ", "")
            vname = vname[:1].lower() + vname[1:]
            dn = f"Param_{SIDE[root]}_{vname}"
            if dn not in defs:
                continue
            up = "../" * depth
            out[(ms._norm(ms.rename(it)), root)] = {
                "$ref": f"{up}BaseSchema/modules/{dirname(name)}/schema.yaml#/$defs/{dn}"}
    return out
