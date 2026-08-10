#!/usr/bin/env python3
"""Add the missing $Dataset counterpart to schema-path rows that should be dual-homed.

The tier matrix (docs/TierImplementationPatterns.xlsx) says four (Protocol, Analysis)
combinations carry BOTH a protocol-level default in the TAPP and a per-analysis value in the
detail. Most existing sidecar rows have only the TAPP half, so those values have nowhere to be
recorded per dataset.

bootstrap_schemapaths cannot fix that in place: its default mode preserves rows untouched (so no
partner is ever added) and --reseed re-derives them (which discards hand-authored modelling).
This pass threads between the two — it ONLY appends, never edits or removes an existing row.

The appended path mirrors any nesting on the TAPP side, via
bootstrap_schemapaths._dataset_counterpart:

  $MethodDefinition.schema:instrument[X].schema:additionalProperty[P].schema:defaultValue
    -> $Dataset.prov:wasGeneratedBy.prov:used[X].schema:additionalProperty[P].schema:value

An item is skipped when it already has a $Dataset row, and reported (not guessed at) when its
TAPP path is not a recognised default — e.g. one ending .schema:name or .schema:identifier, which
is identity rather than a parameter.

Writing is opt-in. Default is a report.

Usage:
    python tools/add_dual_home_rows.py                          # report across every sidecar
    python tools/add_dual_home_rows.py --write                  # apply to every sidecar
    python tools/add_dual_home_rows.py docs/SEM_TAPP_v4.xlsx --write   # one workbook
    python tools/add_dual_home_rows.py --verbose                # list each addition
"""
import argparse
import collections
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap_schemapaths as bs  # noqa: E402  (DUAL_HOMED + the nesting mirror)
import schemapath_io  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOTE = "dual-home counterpart (tier matrix)"


def plan(csv_path):
    """(additions, unresolved) for one sidecar. additions: [(after_index, new_row)]."""
    rows = schemapath_io.read(csv_path)
    by_item = collections.defaultdict(list)
    for i, r in enumerate(rows):
        item = (r.get("Metadata Item") or "").strip()
        if item:
            by_item[item].append((i, r))

    additions, unresolved = [], []
    for item, entries in by_item.items():
        first = entries[0][1]
        tiers = ((first.get("Protocol Tier") or "").strip(),
                 (first.get("Analysis Tier") or "").strip())
        if tiers not in bs.DUAL_HOMED:
            continue
        paths = [(r.get("Schema Path") or "").strip() for _, r in entries]
        if not any(p for p in paths):
            continue                                   # flagged row, nothing to pair
        if any(p.startswith("$Dataset.") for p in paths):
            continue                                   # already dual-homed
        if any(bs.is_analyte_template(p) for p in paths):
            continue        # analyte columns have no analysis-tier path at all; not a gap to fill

        partner = idx = None
        for i, r in entries:
            p = (r.get("Schema Path") or "").strip()
            cand = bs._dataset_counterpart(p, item) if p else None
            if cand:
                partner, idx = cand, i
                break
        if not partner:
            unresolved.append((item, tiers, paths[0] if paths else ""))
            continue

        template = dict(entries[0][1])
        template.update({"Schema Path": partner, "Source": "inferred",
                         "Scope": "", "Notes": NOTE})
        additions.append((idx, template))
    return rows, additions, unresolved


def apply(csv_path, rows, additions):
    """Splice each new row in directly after the row it partners, preserving order."""
    out, extra = [], {i: r for i, r in additions}
    for i, r in enumerate(rows):
        out.append(r)
        if i in extra:
            out.append(extra[i])
    schemapath_io.write(csv_path, out)
    return len(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("workbook", nargs="?", help="one workbook (default: every sidecar)")
    ap.add_argument("--write", action="store_true", help="apply; otherwise report only")
    ap.add_argument("--verbose", action="store_true", help="list every addition")
    args = ap.parse_args()

    if args.workbook:
        targets = [schemapath_io.csv_path(args.workbook if os.path.isabs(args.workbook)
                                          else os.path.join(ROOT, args.workbook))]
    else:
        targets = sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.csv")))

    tot_add = tot_unres = 0
    for csv_path in targets:
        if not os.path.exists(csv_path):
            print(f"  missing: {csv_path}")
            continue
        rows, additions, unresolved = plan(csv_path)
        tot_add += len(additions)
        tot_unres += len(unresolved)
        name = os.path.basename(csv_path)
        print(f"{name:<50s} +{len(additions):>3d} rows"
              + (f"   {len(unresolved)} unresolved" if unresolved else ""))
        if args.verbose:
            for _, r in additions:
                print(f"      + {r['Metadata Item']}")
                print(f"          {r['Schema Path']}")
            for item, tiers, p in unresolved:
                print(f"      ? {item}  [{tiers[0]}/{tiers[1]}] — TAPP path is not a default:")
                print(f"          {p}")
        if args.write and additions:
            n = apply(csv_path, rows, additions)
            print(f"      wrote {n} rows")

    print()
    print(f"total: +{tot_add} rows, {tot_unres} unresolved")
    if not args.write:
        print("report only — pass --write to apply")
    else:
        print("Scope is derived: re-run tools/mark_shared_mappings.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
