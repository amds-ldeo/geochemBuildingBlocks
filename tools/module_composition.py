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
# module name -> building-block directory, mirroring build_module_bb.DIRNAME
DIRNAME = {"ReportingCore": "reportingCore", "LaserAblation": "laserAblation",
           "SolutionIntroduction": "solutionIntroduction", "MCICPMS": "mcIcpms",
           "UPb": "uPb", "Geochronology": "geochronology", "ArAr": "arAr", "Group1": "group1"}
SIDE = {"MethodDefinition": "Procedure", "Dataset": "Analysis"}
_BB_CACHE = {}


def _bb(name):
    """The generated building block's schema, or None if it was never built."""
    if name not in _BB_CACHE:
        p = os.path.join(BBDIR, DIRNAME.get(name, name.lower()), "schema.yaml")
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
    measurements, the provenance activity. 54 of the 105 module paths, and all 22 of Group1's.

    Parameters therefore stay with the technique, which is not harmful duplication: the technique
    enumerates which parameters exist — its own table lists them — and the module says what they
    mean. That is the owned-versus-overlay division the library already uses.
    """
    return "schema:additionalProperty" not in path


def _module_placed(name):
    """{normalized field -> {roots where the module can carry it}}."""
    src = os.path.join(ts.modules_dir(), f"Module_{name}.csv")
    sc = schemapath_io.csv_path(src)
    out = {}
    if not os.path.exists(sc):
        return out
    for r in schemapath_io.read(sc):
        it = (r.get("Metadata Item") or "").strip()
        p = (r.get("Schema Path") or "").strip()
        if not it or not p or not _is_composable(p):
            continue
        root = "Dataset" if p.startswith("$Dataset") else "MethodDefinition"
        out.setdefault(ms._norm(ms.rename(it)), set()).add(root)
    return out


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
        d = DIRNAME.get(name, name.lower())
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
