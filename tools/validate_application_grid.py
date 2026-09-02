#!/usr/bin/env python3
"""Validate the application Y/N grid in the TAPP workbooks.

Each table carries a block of application columns between `Keyed By` and `Literature Assessment`
— the sub-types a protocol can serve (SE Imaging, EBSD, Spot, Transect, …). A Y means the row's
property applies to that application; an N means it is NOT APPLICABLE.

The span is read POSITIONALLY here, unlike `build_tapp.mode_columns`, which additionally requires
every cell in a column to be Y or N. That filter protects the generator from mistaking a stray
text column for a mode; applying it here would defeat the purpose, since a column holding one bad
value would silently vanish from the grid instead of being reported. What the generator skips,
this flags.

That prohibition is what makes the grid load-bearing. A mis-entered N does not merely relax a
requirement — it invalidates any instance carrying the property. So the grid needs checking before
it is enforced, which is what this does.

Checks, per workbook:

  blank        a data row with no value in an application column — ambiguous, and the generator
               would have to guess whether it means Y or N
  bad value    anything that is not Y or N
  dead row     a data row that is N for EVERY application — the property can never appear, so
               either an application column is missing or the row should be deleted
  unused app   an application column where no row is Y — the application is declared but nothing
               applies to it

Section headers ("1. Protocol Identification") are skipped, matching load_rows in
bootstrap_schemapaths: they are all-N by construction and are not properties.

Usage:
    python tools/validate_application_grid.py                       # every workbook
    python tools/validate_application_grid.py docs/SEM_TAPP_v4.xlsx # one
    python tools/validate_application_grid.py --verbose             # list every conditional row
"""
import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import tapp_source

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# the application block ends at whichever of these appears first
END_HEADERS = ("schema path", "literature assessment")
SECTION_RE = re.compile(r"^\d+\.\s")


def read_grid(path):
    """(applications, [(item, [values...]), ...]) — data rows only, section headers dropped."""
    rows = tapp_source.rows(path)
    if not rows:
        return None, None

    hdr = [(str(c).strip() if c is not None else "") for c in rows[0]]
    # The 2026-09 delivery inserted `Purpose` between `Keyed By` and the application block. It is a
    # guidance column, not an application, and reading positionally from `Keyed By` reported it as
    # a mode with prose in every cell. Anchor on whichever recognised guidance header sits LAST, so
    # the span still starts at a named boundary rather than a content filter — which is what the
    # docstring above turns on.
    lead = [i for i, h in enumerate(hdr)
            if h.lower() in ("keyed by", "purpose") or h.lower().startswith("last update")]
    start = max(lead) + 1 if lead else None
    end = next((i for i, h in enumerate(hdr) if h.lower() in END_HEADERS), None)
    if start is None or end is None or end <= start:
        return [], []            # no detectable application block

    apps = [h for h in hdr[start:end]]
    out = []
    for r in rows[1:]:
        item = (str(r[0]).strip() if r[0] else "")
        if not item or SECTION_RE.match(item):
            continue             # blank line or section header, not a property
        vals = [(str(r[i]).strip().upper() if i < len(r) and r[i] is not None else "")
                for i in range(start, end)]
        out.append((item, vals))
    return apps, out


def check(path, verbose=False):
    apps, rows = read_grid(path)
    name = os.path.basename(path)
    if apps is None:
        print(f"{name:<44s} empty table — skipped")
        return 0
    if not apps:
        print(f"{name:<44s} no application columns (unconditional technique)")
        return 0

    # A column block in this position is not necessarily an application grid. The superseded
    # TAPP_LAICPMS_filled workbook has a "Level of Completeness" column there holding tier words
    # (BASIC / READ-ONLY / EDITABLE), which would otherwise report as ~90 bad values. If nothing in
    # the block is Y or N, it is not a grid — say so once instead of flagging every cell.
    if not any(v in ("Y", "N") for _, vals in rows for v in vals):
        print(f"{name:<44s} block after 'Keyed By' holds no Y/N — not an application grid "
              f"({', '.join(apps)!r}); skipped")
        return 0

    blanks, bad, dead = [], [], []
    y_per_app = collections.Counter()
    uncond = cond = 0

    for item, vals in rows:
        for app, v in zip(apps, vals):
            if v == "":
                blanks.append((item, app))
            elif v not in ("Y", "N"):
                bad.append((item, app, v))
            elif v == "Y":
                y_per_app[app] += 1
        present = [v for v in vals if v in ("Y", "N")]
        if present and all(v == "N" for v in present):
            dead.append(item)
        elif present and all(v == "Y" for v in present):
            uncond += 1
        elif "Y" in present and "N" in present:
            cond += 1

    unused = [a for a in apps if not y_per_app[a]]
    issues = len(blanks) + len(bad) + len(dead) + len(unused)

    print(f"{name:<44s} {len(apps)} apps, {len(rows):>3d} rows  "
          f"({uncond} always, {cond} conditional)" + ("" if not issues else f"   {issues} ISSUE(S)"))
    for item, app in blanks:
        print(f"    BLANK      {item}  [{app}]")
    for item, app, v in bad:
        print(f"    BAD VALUE  {item}  [{app}] = {v!r}")
    for item in dead:
        print(f"    DEAD ROW   {item}  — N for every application, can never appear")
    for a in unused:
        print(f"    UNUSED APP {a!r} — declared but no row applies to it")
    if verbose:
        for item, vals in rows:
            present = [v for v in vals if v in ("Y", "N")]
            if "Y" in present and "N" in present:
                on = [a for a, v in zip(apps, vals) if v == "Y"]
                print(f"    conditional: {item}  -> {', '.join(on)}")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("table", nargs="?",
                    help="one table, or a TAPP name; default: every wired technique")
    ap.add_argument("--verbose", action="store_true", help="list each conditional row")
    args = ap.parse_args()

    # The tables are the CSVs the wired techniques actually build from — resolved through
    # TAPP_CONFIGS, so this checks the same revision the generator reads and never a superseded
    # one. It previously globbed docs/*.xlsx; those workbooks are gone, so it silently checked
    # NOTHING and reported a clean grid.
    if args.table and args.table in b.TAPP_CONFIGS:
        b.configure(args.table)
        targets = [b.XLSX]
    elif args.table:
        targets = [args.table if os.path.isabs(args.table)
                   else os.path.join(ROOT, args.table)]
    else:
        targets = []
        for _t in sorted(b.TAPP_CONFIGS):
            b.configure(_t)
            if b.XLSX not in targets:
                targets.append(b.XLSX)

    total = 0
    for t in targets:
        if not os.path.exists(t):
            print(f"missing: {t}")
            total += 1
            continue
        total += check(t, verbose=args.verbose)

    print()
    print(f"{total} issue(s)" if total else "grid is clean")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
