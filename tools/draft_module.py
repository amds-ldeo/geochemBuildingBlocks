#!/usr/bin/env python3
"""Draft candidate modules locally, to measure what modularising the LA family would save.

The six LA tables hold 115 fields common to all six; the existing modules cover 42. The rest are
duplicated six times over, which is the drift the module system exists to prevent — so before
authoring six near-identical sidecars, this builds the missing modules as DRAFTS and measures the
difference.

These are ours and provisional. They live under docs/modules/draft/ and are named `Draft_Module_*`
so nothing confuses them with the library's own modules, which are Ruolin's to author (see
docs/upstream-requests.md §1). If he adopts them, the real modules arrive in a delivery and these
are deleted.

Each field's definition is taken from the LA tables themselves rather than invented: description,
tiers, data type and Keyed By are copied from the tables that carry it. A field whose definition
DIFFERS between tables is refused, not averaged — three do, and all three are documented as
technique-dependent by design, so they stay per-table where they belong.

    python tools/draft_module.py                  # report what would be built
    python tools/draft_module.py --write
    python tools/draft_module.py --measure        # the saving, once built
"""
import argparse
import collections
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import migrate_sidecar as ms
import tapp_source as ts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFT = os.path.join(ROOT, "docs", "modules", "draft")
CUR = os.path.join(ts.current_delivery(), "Current TAPPs")

LA = ["LA-Q-ICP-MS_TAPP_v15.csv", "LA-SF-ICP-MS_TAPP_v16.csv", "LA-MC-ICPMS_TAPP_v13.csv",
      "LA-Q-ICP-MS_UPb_TAPP_v16.csv", "LA-SF-ICP-MS_UPb_TAPP_v17.csv", "LA-MC-ICPMS_UPb_TAPP_v13.csv"]

HEADER = ["Metadata Item", "Description / Purpose", "Procedure-Level Tier", "Analysis-Level Tier",
          "Data Type", "Example / Allowed Content", "Comments", "Last Update", "Keyed By"]

# The groupings proposed in docs/upstream-requests.md §1. Membership is a judgement about what
# belongs together; the field DEFINITIONS are not — those come from the tables.
GROUPS = {
    "ICPMSCore": [
        "ICP-MS Manufacturer & Model", "ICP-MS Type", "RF Power", "Coolant (Plasma) Gas Flow Rate",
        "Auxiliary Gas Flow Rate", "Carrier Gas and Flow Rate", "Torch Type", "Torch Depth",
        "Interface Cone Configuration", "Sampler and Skimmer Cone Material", "Guard Electrode",
        "Plasma Thermal Mode", "Detector Configuration", "Ion Counter Dead Time",
        "Sample Introduction", "Instrument Serial Number or Lab Identifier", "ICP Tuning",
        "Instrument Warm-up / Session Duration Limit", "Plasma / Make-up Gas Addition",
        "Sensitivity as Useful Yield",
    ],
    "CollisionReactionCell": [
        "Collision / Reaction Cell (CRC) Configuration", "Collision Gas Type",
        "Collision Gas Flow Rate", "Reaction Gas Type", "Reaction Gas Flow Rate",
        "Cell Exit Discrimination Voltage",
    ],
    "SignalAcquisition": [
        "Dwell Time per Mass", "Signal Integration Time", "Signal Integration Interval Method",
        "Total Integration Time per Output Data Point", "Background Count Time",
        "Number of Replicates", "Signal Smoothing", "Mass Resolution Assignment",
        "Multi-Run Sequential Analysis Design",
    ],
    "InterferenceHandling": [
        "Interfering Species", "Isobaric Interference Corrections Applied",
        "Interference Correction Method", "Oxide Production",
        "Oxide Production Method and Threshold", "Doubly-Charged Species Production",
        "Doubly-Charged Species Monitor",
    ],
    "CalibrationUncertainty": [
        "Detection Limit", "Detection Limit Method", "Limit of Quantification (LOQ) Method",
        "Within-Session Analytical Precision and Assessment Method",
        "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "Analytical Accuracy and Assessment Method", "Uncertainty Level",
        "Uncertainty Propagation Method", "Secondary Reference Materials",
        "Per-Analyte Calibration Strategy", "Internal Standard Approach",
        "Internal Standard Element", "Normalization / Standards-Based Correction",
        "Blank / Background Correction Method", "Calibration Standard Measurement Frequency",
        "Spike / Outlier Filtering Approach", "Elemental Fractionation Correction",
        "Mass Bias Correction Strategy", "Matrix Offset Correction (LIEF)",
        "Isotope Dilution Data Reduction Method", "Memory Effect Mitigation",
    ],
    "SampleSpecimen": [
        "Sample Name", "Sample Persistent Identifier", "Sample Form / Analytical Substrate",
        "Sample Preparation Method", "Target Material", "Sampling Unit", "Analysis Sequence",
        "Fusion Flux and Dilution Ratio",
    ],
}


def la_definitions():
    """{field -> (definition tuple, [tables])}; definition is (desc, P, A, dt, examples, keyed)."""
    seen = collections.defaultdict(lambda: collections.defaultdict(list))
    for f in LA:
        raw = ts.rows(os.path.join(CUR, f))
        for r in raw[1:]:
            it = " ".join(str(r[0]).split()) if r and r[0] else ""
            if not it or (it[0].isdigit() and ". " in it[:4]):
                continue
            g = lambda i: (" ".join(str(r[i]).split()) if i < len(r) and r[i] else "")
            # STRUCTURAL identity only: tiers, data type, cardinality. Column F (examples) is
            # consumer-owned, and the description is prose — six CRC fields carry identical
            # structure with wording tailored per instrument family, which is a thing for Ruolin to
            # reconcile when he adopts a module, not a reason the field cannot be one.
            seen[ms.rename(it)][(g(2), g(3), g(4), g(8))].append((f, g(1)))
    return seen


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--measure", action="store_true")
    a = ap.parse_args()

    defs = la_definitions()
    built, refused, missing, prose = {}, [], [], []
    for name, fields in GROUPS.items():
        rows = []
        for fld in fields:
            key = ms.rename(fld)
            if key not in defs:
                missing.append((name, fld))
                continue
            variants = defs[key]
            if len(variants) > 1:
                refused.append((name, fld, variants))
                continue
            (P, A, dt, keyed), tabs = next(iter(variants.items()))
            # most common wording wins; note it where the tables disagree
            byd = collections.Counter(d for _, d in tabs)
            desc = byd.most_common(1)[0][0]
            if len(byd) > 1:
                prose.append((name, fld, len(byd)))
            rows.append({"Metadata Item": fld, "Description / Purpose": desc,
                         "Procedure-Level Tier": P, "Analysis-Level Tier": A, "Data Type": dt,
                         "Example / Allowed Content": "", "Comments": "", "Last Update": "",
                         "Keyed By": keyed, "_tables": len(tabs)})
        built[name] = rows

    print(f"{'draft module':<34s} {'fields':>6s}  {'avg tables':>10s}")
    for name, rows in built.items():
        avg = sum(r["_tables"] for r in rows) / len(rows) if rows else 0
        print(f"  Draft_Module_{name:<20s} {len(rows):>6d}  {avg:>10.1f}")
    total = sum(len(r) for r in built.values())
    print(f"{'':<26s} {total:>6d} fields total")

    if refused:
        print(f"\nREFUSED — definition differs between LA tables, so it cannot be one module field:")
        for name, fld, variants in refused:
            print(f"  [{name}] {fld}")
            for (P, A, dt, keyed), tabs in variants.items():
                short = [t.replace("_TAPP", "").replace(".csv", "") for t, _ in tabs]
                print(f"      {P}/{A} · {dt} · Keyed By {keyed}  <- {', '.join(sorted(short))}")
    if prose:
        print(f"\n{len(prose)} field(s) structurally identical but WORDED differently between "
              f"tables.\nThe most common wording is used; Ruolin picks one when adopting:")
        for name, fld, n in prose:
            print(f"  [{name}] {fld}  ({n} variants)")
    if missing:
        print(f"\nNOT FOUND in the LA tables (check the name):")
        for name, fld in missing:
            print(f"  [{name}] {fld}")

    if a.write:
        os.makedirs(DRAFT, exist_ok=True)
        for name, rows in built.items():
            p = os.path.join(DRAFT, f"Draft_Module_{name}.csv")
            with open(p, "w", newline="", encoding="utf-8-sig") as fh:
                w = csv.DictWriter(fh, fieldnames=HEADER, extrasaction="ignore")
                w.writeheader()
                for r in rows:
                    w.writerow(r)
            print(f"  wrote {os.path.relpath(p, ROOT)}")

    if a.measure:
        measure(built)
    return 0


def measure(built):
    """Placements to author for the six LA tables, with and without these modules."""
    modfields = {ms.rename(r["Metadata Item"]) for rows in built.values() for r in rows}
    existing = set()
    md = ts.modules_dir()
    for f in os.listdir(md):
        if f.startswith("Module_") and f.endswith(".csv") and not f.endswith(".schemapaths.csv"):
            existing |= {ms.rename(i) for i, _, _, _ in ms.source_items(os.path.join(md, f))}

    per_table = {}
    for f in LA:
        items = {ms.rename(i) for i, _, _, _ in ms.source_items(os.path.join(CUR, f))}
        per_table[f] = items
    total_fields = sum(len(v) for v in per_table.values())
    covered_now = sum(len(v & existing) for v in per_table.values())
    covered_draft = sum(len(v & (existing | modfields)) for v in per_table.values())

    print("\n--- placements to author for the six LA tables ---")
    print(f"  field instances across the six tables      {total_fields:>5d}")
    print(f"  already covered by the library's modules   {covered_now:>5d}")
    print(f"  left to place per-table today              {total_fields - covered_now:>5d}")
    print(f"  covered if these drafts were modules       {covered_draft:>5d}")
    print(f"  left to place per-table then               {total_fields - covered_draft:>5d}")
    saved = covered_draft - covered_now
    print(f"\n  field instances that stop being repeated  {saved:>5d}")
    print(f"  authored ONCE in {len(built)} modules instead        {len(modfields):>5d}")
    print(f"  net reduction in placements               {saved - len(modfields):>5d}")


if __name__ == "__main__":
    sys.exit(main())
