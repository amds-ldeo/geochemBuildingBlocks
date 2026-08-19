#!/usr/bin/env python3
"""Write the completed dual-home decisions into the schema-path sidecars.

docs/unresolved-dualhome.csv is the worklist tools/unresolved_report.py produces: one row per
(item, sidecar) that the tier matrix says should be dual-homed but whose $Dataset counterpart
add_dual_home_rows could not derive. Two columns are authored by hand:

    verdict               the CORRECTED $MethodDefinition path
    $Dataset counterpart  the analysis-tier path to add

This applies both: the sidecar's TAPP row is repointed to `verdict`, and a new row carrying the
counterpart is spliced in directly after it. `Source` becomes `authored` on both, because a human
decided them and bootstrap_schemapaths --reseed preserves only authored rows.

Refuses to write anything it cannot justify. Each of these is reported and SKIPPED:

  ungrammatical   either path fails normalize_schema_paths.recognize(). Writing it would put a
                  path in the sidecar no emitter can consume
  unmatched       no sidecar row carries that (item, current TAPP path) any more — the sidecar
                  moved on since the worklist was generated, so regenerate it before applying
  duplicate       the sidecar already has that (item, path); nothing to do

Matching ignores a trailing `[]`, because a decision may legitimately change cardinality: a row
recorded as `ada:backgroundCountTime[]` whose verdict is `ada:backgroundCountTimeDefault` is
saying the property should not be list-valued. The verdict is the authored answer, so it decides;
every such change is reported under DE-ARRAYED rather than applied silently.

Writing is opt-in. Default is a report.

Usage:
    python tools/apply_dualhome.py                 # report
    python tools/apply_dualhome.py --write         # apply
    python tools/apply_dualhome.py --verbose       # show every edit
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
DECISIONS = os.path.join(ROOT, "docs", "unresolved-dualhome.csv")

NOTE_TAPP = "dual-home decision: protocol default"
NOTE_DS = "dual-home decision: analysis-tier value"


def _canon(p):
    return norm.mechanical(norm.preclean(p.strip())) if p else ""


def plan(decisions_path):
    """{sidecar: [(row_index, new_tapp_path, dataset_path)]}, plus the skip buckets."""
    by_car = collections.defaultdict(list)
    for r in csv.DictReader(open(decisions_path, encoding="utf-8-sig")):
        by_car[(r.get("sidecar") or "").strip()].append(r)

    edits = collections.defaultdict(list)
    ungrammatical, unmatched, duplicate, dearrayed = [], [], [], []

    def bare(p):
        return p[:-2] if p.endswith("[]") else p

    for short, decisions in sorted(by_car.items()):
        path = os.path.join(ROOT, "docs", short + ".schemapaths.csv")
        if not os.path.exists(path):
            unmatched += [(short, d["Metadata Item"], "sidecar not found") for d in decisions]
            continue
        rows = schemapath_io.read(path)
        # (item, canonical path with any trailing [] removed) -> row indices, so a repointed row is
        # found by what it was even if the decision changes its cardinality
        index = collections.defaultdict(list)
        have = set()
        actual = {}
        for i, row in enumerate(rows):
            item = (row.get("Metadata Item") or "").strip()
            p = _canon(row.get("Schema Path") or "")
            index[(item, bare(p))].append(i)
            actual[i] = p
            if p:
                have.add((item, p))

        for d in decisions:
            item = (d.get("Metadata Item") or "").strip()
            cur = _canon(d.get("TAPP Schema Path") or "")
            tapp = _canon(d.get("verdict") or "")
            ds = _canon(d.get("$Dataset counterpart") or "")
            bad = [p for p in (tapp, ds) if not p or norm.recognize(p)[0] is None]
            if bad:
                ungrammatical.append((short, item, bad[0]))
                continue
            hits = index.get((item, bare(cur)))
            if not hits:
                # already repointed by an earlier run? then there is nothing left to do
                if (item, tapp) in have and (item, ds) in have:
                    duplicate.append((short, item, tapp))
                else:
                    unmatched.append((short, item, cur))
                continue
            was = actual[hits[0]]
            if was.endswith("[]") != tapp.endswith("[]"):
                dearrayed.append((short, item, was, tapp))
            edits[short].append((hits[0], tapp, ds, (item, ds) in have))
    return edits, ungrammatical, unmatched, duplicate, dearrayed


def apply(short, edits):
    path = os.path.join(ROOT, "docs", short + ".schemapaths.csv")
    rows = schemapath_io.read(path)
    extra = {}
    for i, tapp, ds, ds_exists in edits:
        rows[i]["Schema Path"] = tapp
        rows[i]["Source"] = "authored"
        rows[i]["Scope"] = ""                 # derived; mark_shared_mappings recomputes it
        rows[i]["Notes"] = NOTE_TAPP
        if not ds_exists:
            new = dict(rows[i])
            new.update({"Schema Path": ds, "Source": "authored", "Scope": "", "Notes": NOTE_DS})
            extra[i] = new
    out = []
    for i, r in enumerate(rows):
        out.append(r)
        if i in extra:
            out.append(extra[i])
    shutil.copy(path, path + ".bak")
    schemapath_io.write(path, out)
    return len(edits), len(extra), len(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--decisions", default=DECISIONS)
    ap.add_argument("--write", action="store_true", help="apply; otherwise report only")
    ap.add_argument("--verbose", action="store_true", help="show every edit")
    args = ap.parse_args()

    edits, ungrammatical, unmatched, duplicate, dearrayed = plan(args.decisions)
    tot = sum(len(v) for v in edits.values())
    adds = sum(1 for v in edits.values() for e in v if not e[3])

    for short in sorted(edits):
        n_new = sum(1 for e in edits[short] if not e[3])
        print(f"{short + '.schemapaths.csv':<50s} {len(edits[short]):>3d} repointed, "
              f"+{n_new} $Dataset row(s)")
        if args.verbose:
            for _i, tapp, ds, exists in edits[short]:
                print(f"      TAPP  {tapp}")
                print(f"      {'have' if exists else ' new'}  {ds}")

    print(f"\n{tot} row(s) repointed, {adds} $Dataset row(s) added, across {len(edits)} sidecar(s)")
    for label, bucket in (("UNGRAMMATICAL (skipped)", ungrammatical),
                          ("UNMATCHED (skipped)", unmatched),
                          ("ALREADY APPLIED", duplicate)):
        if bucket:
            print(f"\n{label} — {len(bucket)}:")
            for short, item, p in bucket[:12]:
                print(f"   {item} [{short}]")
                print(f"      {p}")
            if len(bucket) > 12:
                print(f"   … +{len(bucket) - 12} more")

    if dearrayed:
        print(f"\nDE-ARRAYED — {len(dearrayed)} row(s) whose CARDINALITY the decision changes:")
        for short, item, was, now in dearrayed:
            print(f"   {item} [{short}]")
            print(f"      -  {was}")
            print(f"      +  {now}")

    if not args.write:
        print("\nreport only — pass --write to apply")
        return 0
    for short in sorted(edits):
        n, a, total = apply(short, edits[short])
        print(f"  {short}: {n} repointed, +{a} rows, {total} total (backup at .bak)")
    print("\nScope is derived: re-run tools/mark_shared_mappings.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
