#!/usr/bin/env python3
"""Report what a new TAPP delivery would change, before anything is applied.

Ruolin authors the tables; we author where their fields live. The two never touch the same file, so
the collaboration risk is not merge conflicts — it is DRIFT: a rename or a re-tier upstream silently
invalidates sidecar rows keyed on Metadata Item, and the failure is quiet. This runs the three
checks that turn that drift into something reviewable, in the order the answers are needed:

  1. per technique   what migrate_sidecar would carry, rename, DROP or newly flag
  2. across modules  tier disagreements, and fields composition would add
  3. across all      paths that no longer resolve to a grammar family

Read-only. Nothing here writes: it is the report you read BEFORE running migrate_sidecar --write,
re-pointing TAPP_CONFIGS, and rebuilding.

DROPPED is the line to read closely. An item that looks deleted is usually renamed beyond the
mechanical rules, and its authored paths go with it — that is how Sample IGSN -> Sample Persistent
Identifier nearly lost its placement. Confirm against the new table's own Description, then add a
migrate_sidecar.ALIASES entry rather than letting the paths be discarded.

    python tools/intake_delivery.py TAPPS20260901          # a new delivery folder
    python tools/intake_delivery.py TAPPS20260901 --map empaTAPP=EPMA/EPMA_TAPP_v14.csv
    python tools/intake_delivery.py --checks-only          # just re-run 2 and 3 on what is here
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import migrate_sidecar as ms
import normalize_schema_paths as norm
import schemapath_io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")


def rule(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")
    # subprocesses write straight to the terminal, so anything still sitting in our buffer would
    # surface after their output and file the results under the wrong heading
    sys.stdout.flush()


def guess_map(delivery):
    """{tapp -> new table} by matching each TAPP's current source basename stem, loosely.

    Deliberately a guess with the evidence shown, not a silent mapping: a delivery can rename or
    split a table (LA-Q_SF-ICPMS became two), and a wrong guess would migrate a sidecar onto the
    wrong technique. Anything unmatched is reported for --map.
    """
    tables = []
    for base, _, files in os.walk(os.path.join(ROOT, delivery)):
        for f in files:
            if f.endswith(".csv") and not f.endswith(".schemapaths.csv") and "_TAPP_" in f:
                tables.append(os.path.relpath(os.path.join(base, f), os.path.join(ROOT, delivery)))
    out, unmatched = {}, list(tables)
    for t in sorted(b.TAPP_CONFIGS):
        b.configure(t)
        stem = ms._norm(os.path.splitext(os.path.basename(b.XLSX))[0].split("_TAPP")[0])
        hits = [x for x in tables if ms._norm(os.path.basename(x).split("_TAPP")[0]) == stem]
        if len(hits) == 1:
            out[t] = hits[0]
            if hits[0] in unmatched:
                unmatched.remove(hits[0])
    return out, unmatched


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("delivery", nargs="?", help="new delivery folder, e.g. TAPPS20260901")
    ap.add_argument("--map", action="append", default=[], metavar="TAPP=REL/PATH.csv",
                    help="pin a technique to a table when the guess is wrong (repeatable)")
    ap.add_argument("--checks-only", action="store_true",
                    help="skip the migration preview; just re-run the module and grammar checks")
    a = ap.parse_args()

    if a.delivery and not a.checks_only:
        d = os.path.join(ROOT, a.delivery)
        if not os.path.isdir(d):
            raise SystemExit(f"no such delivery folder: {a.delivery}")
        mapping, unmatched = guess_map(a.delivery)
        for m in a.map:
            k, _, v = m.partition("=")
            mapping[k] = v

        rule(f"1. MIGRATION PREVIEW — {a.delivery}")
        print("Which curation carries across, and what needs a human. Nothing is written.\n")
        for t in sorted(mapping):
            src = os.path.join(d, mapping[t].replace("/", os.sep))
            if not os.path.exists(src):
                print(f"{t:<22s} SKIP — no such table: {mapping[t]}")
                continue
            subprocess.run([sys.executable, os.path.join(TOOLS, "migrate_sidecar.py"), t,
                            "--source", src], cwd=ROOT)
        if unmatched:
            print("\nTables in the delivery matched to no technique — pin with --map if one of these")
            print("replaces an existing TAPP, or they are genuinely new scope:")
            for u in sorted(unmatched):
                print(f"    {u}")

    rule("2. MODULE COMPOSITION — what composing would change for consumers")
    subprocess.run([sys.executable, os.path.join(TOOLS, "module_conflict_check.py")], cwd=ROOT)

    rule("3. GRAMMAR — paths that no longer resolve")
    tot = bad = 0
    for label, path in _all_sidecars():
        for r in schemapath_io.read(path):
            p = (r.get("Schema Path") or "").strip()
            if not p:
                continue
            tot += 1
            if norm.recognize(p)[0] is None:
                bad += 1
                print(f"    UNRECOGNISED [{label}] {r['Metadata Item']}: {p[:100]}")
    print(f"\n{tot} paths, {bad} unrecognised")
    if not bad:
        print("(a clean sweep here is necessary but not sufficient — recognize() accepts some paths")
        print(" the emitter drops; confirm anything newly authored actually emits.)")

    rule("NEXT")
    print("  migrate_sidecar.py <tapp> --source <table> --write   per technique, once the report reads right")
    print("  seed_module_sidecars.py --write                      module sidecars, if modules changed")
    print("  edit build_tapp.TAPP_CONFIGS                         point each TAPP at its new table")
    print("  build_tapp.py <t> && build_pathdriven.py <t>          then --validate; expect GREEN")
    print("  commit in three: import, sidecars, regeneration")
    return 0


def _all_sidecars():
    out = []
    for t in sorted(b.TAPP_CONFIGS):
        b.configure(t)
        p = schemapath_io.csv_path(b.XLSX)
        if os.path.exists(p):
            out.append((t, p))
    for base, _, files in os.walk(ROOT):
        if ".git" in base:
            continue
        for f in files:
            if f.startswith("Module_") and f.endswith(".schemapaths.csv"):
                out.append(("mod:" + f[7:-16], os.path.join(base, f)))
    return out


if __name__ == "__main__":
    sys.exit(main())
