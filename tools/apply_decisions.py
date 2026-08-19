#!/usr/bin/env python3
"""Write the completed divergence decisions back into the schema-path sidecars.

docs/divergent-decisions.csv is a worklist: one row per (divergent item, sidecar, current path),
with a hand-authored `proposed Schema Path` saying what that path SHOULD be. This applies those
proposals — the last step of the divergence-resolution loop that mark_shared_mappings starts.

A decision is applied by matching the sidecar row on (Metadata Item, canonical current path) and
replacing its Schema Path. `Source` becomes `authored`, because a human decided it and re-seeding
must not overwrite it (bootstrap_schemapaths --reseed preserves only authored rows).

Refuses to write anything it cannot justify. Each of these is reported and SKIPPED, never guessed:

  ungrammatical   the proposal does not parse under docs/SCHEMA_PATH_GRAMMAR.md. Writing it would
                  put a path in the sidecar that no emitter can consume, so the row is left alone
  unmatched       no sidecar row has that (item, current path) any more — the sidecar moved on
                  since the worklist was generated, so re-run --decisions before applying
  collision       the edit would produce a row the sidecar already has. The key is (item, path),
                  NOT path alone — many distinct items share one path legitimately, since every
                  analyte column maps to the same bare `…ada:analyteColumns[]` leaf

`Scope` is derived, so re-run mark_shared_mappings.py afterwards.

Usage:
    python tools/apply_decisions.py                        # report what would change
    python tools/apply_decisions.py --write                # apply
    python tools/apply_decisions.py --verbose              # show every edit
    python tools/apply_decisions.py --skip-ungrammatical   # apply the rest, leave those (default)
    python tools/apply_decisions.py --allow-ungrammatical  # apply them anyway (you were warned)
"""
import argparse
import collections
import csv
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_schema_paths as norm  # noqa: E402
import schemapath_io  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECISIONS = os.path.join(ROOT, "docs", "divergent-decisions.csv")

NOTE = "divergence decision applied"


def _canon(p):
    return norm.mechanical(norm.preclean(p)) if p else ""


def plan(decisions_path, allow_ungrammatical=False):
    """{sidecar short: [(row_index, old, new)]}, plus the three skip buckets."""
    by_car = collections.defaultdict(list)
    for r in csv.DictReader(open(decisions_path, encoding="utf-8-sig")):
        prop = (r.get("proposed Schema Path") or "").strip()
        if not prop:
            continue
        by_car[(r.get("sidecar") or "").strip()].append(r)

    edits = collections.defaultdict(list)
    ungrammatical, unmatched, collisions, noop = [], [], [], 0

    for short, decisions in sorted(by_car.items()):
        csv_path = os.path.join(ROOT, "docs", short + ".schemapaths.csv")
        if not os.path.exists(csv_path):
            unmatched += [(short, d["Metadata Item"], "sidecar not found") for d in decisions]
            continue
        rows = schemapath_io.read(csv_path)
        # (item, canonical path) -> row indices; a sidecar may legitimately repeat an item
        index = collections.defaultdict(list)
        for i, row in enumerate(rows):
            key = ((row.get("Metadata Item") or "").strip(),
                   _canon((row.get("Schema Path") or "").strip()))
            index[key].append(i)

        # A duplicate is the same (item, path) twice — NOT the same path twice. Many distinct items
        # share one path legitimately: every analyte column maps to the bare
        # `…ada:analyteColumns[]` leaf, so a sidecar holds a dozen rows with that identical path.
        claimed = {((row.get("Metadata Item") or "").strip(),
                    _canon((row.get("Schema Path") or "").strip()))
                   for row in rows if (row.get("Schema Path") or "").strip()}

        for d in decisions:
            item = (d.get("Metadata Item") or "").strip()
            cur = _canon((d.get("current Schema Path") or "").strip())
            new = _canon(d["proposed Schema Path"].strip())

            if norm.recognize(new)[0] is None and not allow_ungrammatical:
                ungrammatical.append((short, item, new))
                continue
            if cur == new:
                noop += 1
                continue
            hits = index.get((item, cur))
            if not hits:
                unmatched.append((short, item, cur))
                continue
            if (item, new) in claimed:
                collisions.append((short, item, new, item))
                continue
            for i in hits:
                edits[short].append((i, rows[i].get("Schema Path", ""), d["proposed Schema Path"].strip()))
            claimed.add((item, new))

    return edits, ungrammatical, unmatched, collisions, noop


def apply(short, edits):
    csv_path = os.path.join(ROOT, "docs", short + ".schemapaths.csv")
    rows = schemapath_io.read(csv_path)
    for i, _old, new in edits:
        rows[i]["Schema Path"] = new
        rows[i]["Source"] = "authored"
        rows[i]["Scope"] = ""                    # derived; mark_shared_mappings recomputes it
        rows[i]["Notes"] = NOTE
    shutil.copy(csv_path, csv_path + ".bak")
    schemapath_io.write(csv_path, rows)
    return len(edits)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--decisions", default=DECISIONS, help="worklist CSV")
    ap.add_argument("--write", action="store_true", help="apply; otherwise report only")
    ap.add_argument("--verbose", action="store_true", help="show every edit")
    ap.add_argument("--allow-ungrammatical", action="store_true",
                    help="apply proposals that do not parse (they will break the emitters)")
    args = ap.parse_args()

    edits, ungrammatical, unmatched, collisions, noop = plan(
        args.decisions, allow_ungrammatical=args.allow_ungrammatical)

    total = sum(len(v) for v in edits.values())
    for short in sorted(edits):
        print(f"{short + '.schemapaths.csv':<50s} {len(edits[short]):>3d} edit(s)")
        if args.verbose:
            for _i, old, new in edits[short]:
                print(f"      - {old}")
                print(f"      + {new}")

    print()
    print(f"{total} edit(s) across {len(edits)} sidecar(s); {noop} already conform")
    for label, bucket in (("UNGRAMMATICAL (skipped)", ungrammatical),
                          ("UNMATCHED (skipped)", unmatched)):
        if bucket:
            print(f"\n{label} — {len(bucket)}:")
            for short, item, p in bucket:
                print(f"   {item} [{short}]")
                print(f"      {p}")
    if collisions:
        print(f"\nCOLLISION (skipped) — {len(collisions)}:")
        for short, item, p, owner in collisions:
            print(f"   {item} [{short}] would take a path already held by {owner!r}")
            print(f"      {p}")

    if not args.write:
        print("\nreport only — pass --write to apply")
        return 0

    for short in sorted(edits):
        n = apply(short, edits[short])
        print(f"  wrote {n} edit(s) to {short}.schemapaths.csv (backup at .bak)")
    print("\nScope is derived: re-run tools/mark_shared_mappings.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
