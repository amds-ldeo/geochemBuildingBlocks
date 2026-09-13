#!/usr/bin/env python3
"""Blank the Schema Path on technique sidecar rows a composed module already places.

A module-covered row does not need its own path: schema_path_emitter drops it from the technique's
overlay and the module's $def supplies the field. Keeping the path is not merely redundant, it is a
place for the two to disagree silently -- the technique authors a placement, the generator discards
it, and nothing says so.

The ROW stays. migrate_sidecar diffs Metadata Items against the workbook, so deleting one brings it
back as "new (flagged)" at the next delivery. Only the path goes, replaced by a note naming the
module that now owns the placement.

DIVERGENT ROWS ARE LEFT ALONE AND REPORTED. Where the technique's authored path does not match the
module's, blanking it would destroy the authored decision and silently adopt the module's -- which
is the very failure this is meant to end. Those need the module fixed, or the divergence settled,
first.

    python tools/simplify_sidecars.py            # report
    python tools/simplify_sidecars.py --write
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import module_composition as mc
import normalize_schema_paths as norm
import schemapath_io



# Divergences the reviewer has SETTLED in the module's favour. Naming them here, rather than
# loosening the match, keeps the default safe: an unlisted divergence is still refused.
ADOPTED = {
    "Reported Variables and Units":
        "reviewer settled the reported-property list as $MethodDefinition.ada:reportedProperties[]",
    "Goodness-of-Fit or Dispersion Statistic":
        "reviewer's rule: dqv:hasQualityMeasurement by default, the reported-property "
        "variableMeasured list only when keyed and a reportedProperties list is defined",
    "Ablation Duration per Spot":
        "module places the direct ada: property its $def requires; the technique's parameter path "
        "was already discarded by the generator",
    "Ablation Pit Depth and Ablation Rate":
        "as Ablation Duration per Spot",
    "Raster Line Spacing (Mapping Only)":
        "as Ablation Duration per Spot",
}

def canon(p):
    try:
        return norm.mechanical(norm.preclean((p or "").strip()))
    except Exception:
        return (p or "").strip()


def module_paths(refs):
    """{normalised item -> {module: {canonical path}}} for the modules a technique composes."""
    out = {}
    for name, _ in refs:
        sc = schemapath_io.csv_path(os.path.join(mc.ts.modules_dir(), "Module_%s.csv" % name))
        if not os.path.exists(sc):
            continue
        for r in schemapath_io.read(sc):
            it, p = (r.get("Metadata Item") or "").strip(), (r.get("Schema Path") or "").strip()
            if it and p:
                out.setdefault(mc.ms._norm(mc.ms.rename(it)), {}).setdefault(name, set()).add(canon(p))
    return out


def _dedupe(rows):
    """Drop rows identical to one already kept, preserving order. Returns (rows, n_removed).

    Only EXACT duplicates go -- every field equal. Two rows for one item that still differ in
    Schema Path are the legitimate multi-placement case (a keyed row plus its unkeyed fallback,
    or a $MethodDefinition and a $Dataset home) and are left alone.
    """
    seen, out = set(), []
    for r in rows:
        k = tuple(sorted((k2, (v or "")) for k2, v in r.items()))
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out, len(rows) - len(out)


def run(tapp, write=False):
    b.configure(tapp)
    f = schemapath_io.csv_path(b.XLSX)
    if not os.path.exists(f):
        return 0, 0
    refs, covered = mc.plan(b.XLSX)
    mp = module_paths(refs)
    rows = schemapath_io.read(f)
    blanked, adopted, divergent = 0, 0, []
    for r in rows:
        it, p = (r.get("Metadata Item") or "").strip(), (r.get("Schema Path") or "").strip()
        if not it or not p:
            continue
        root = "Dataset" if p.startswith("$Dataset") else "MethodDefinition"
        k = mc.ms._norm(mc.ms.rename(it))
        if k not in covered[root]:
            continue
        owners = mp.get(k) or {}
        match = [m for m, paths in owners.items() if canon(p) in paths]
        if not match:
            # A DIVERGENT row: the technique authored a different placement from the module's.
            # Blanking it would adopt the module's and destroy the authored decision, so it is left
            # alone -- UNLESS the divergence has been settled and the item named in ADOPTED, in
            # which case the module is the agreed owner and the technique row is stale.
            if it in ADOPTED:
                r["Schema Path"] = ""
                r["Source"] = "module"
                r["Notes"] = "placement owned by Module %s (%s)" % (
                    (sorted(owners) or ["?"])[0], ADOPTED[it])
                adopted += 1
                continue
            divergent.append((it, p, sorted(owners)))
            continue
        r["Schema Path"] = ""
        r["Source"] = "module"
        r["Notes"] = "placement owned by Module %s" % match[0]
        blanked += 1

    # Blanking DESTROYS the only field that told two rows for the same item apart. A field that
    # carried four distinct placements becomes four byte-identical rows reading "placement owned
    # by Module X" -- a fossil of how many paths it used to have, and unreadable as anything else.
    # Harmless downstream (load_spec reads paths; four blank rows say what one says), but it is
    # what a human hits first: 945 such rows existed across the sidecars before this collapse ran.
    # Identical rows carry no distinct information, so keep the first and drop the rest.
    rows, removed = _dedupe(rows)

    if write and (blanked or adopted or removed):
        schemapath_io.write(f, rows)
    print("%-22s %3d blanked, %2d adopted, %2d deduped, %d divergent%s"
          % (tapp, blanked, adopted, removed, len(divergent), "" if write else "  (dry run)"))
    for it, p, owners in divergent:
        print("      DIVERGENT %-42s owned by %s" % (it[:42], ", ".join(owners) or "?"))
        print("                technique: %s" % p[:100])
    return blanked + adopted, len(divergent)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp", nargs="?")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    tot = div = 0
    for t in ([a.tapp] if a.tapp else sorted(b.TAPP_CONFIGS)):
        x, y = run(t, a.write)
        tot += x
        div += y
    print("\n%d path(s) blanked, %d divergent row(s) left for review%s"
          % (tot, div, "" if a.write else "   (dry run - pass --write)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
