#!/usr/bin/env python3
"""Mark which schema-path sidecar rows are shared boilerplate, so a review can skip them.

Most Metadata Items in the Procedure Identification, Samples and Instrument & Software sections
are not technique-specific — `Analyst`, `Laboratory`, `Technique`, `Analysis Start Date` and the
like map the same way in every TAPP. Reviewing them once per sidecar is wasted effort.

This fills the derived `Scope` column in every docs/*.schemapaths.csv:

    shared      the item appears in 2+ sidecars and they ALL agree on the same canonical path
                -> already settled elsewhere; skip it
    divergent   the item appears in 2+ sidecars with DIFFERENT paths
                -> either a real technique difference or an inconsistency; worth a look
    (blank)     the item appears in only one sidecar -> technique-specific, review normally

Comparison is on the CANONICAL path (normalize_schema_paths.mechanical), so `$.` shorthand and
stray whitespace do not make two identical mappings look different.

Scope is derived, never authored. bootstrap_schemapaths rebuilds rows from the workbook and drops
it, so re-run this after any re-seed.

Usage:
    python tools/mark_shared_mappings.py --dry-run     # summary + the divergent list, writes nothing
    python tools/mark_shared_mappings.py               # fill the Scope column in every sidecar
    python tools/mark_shared_mappings.py --list-shared # print the shared items and their path
"""
import argparse
import collections
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_schema_paths as norm  # noqa: E402
import schemapath_io  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SHARED = "shared"
DIVERGENT = "divergent"


def _canon(path):
    return norm.mechanical(norm.preclean(path))


def classify(sidecars):
    """{item: (scope, {canonical path: {sidecar, ...}})} across every sidecar.

    Agreement is compared per sidecar as a SET of paths, not path-by-path: an item that is
    dual-homed (a TAPP `…schema:defaultValue` plus the matching `$Dataset…schema:value`) has two
    paths in every sidecar that carries it, and that is agreement, not divergence. Only a
    difference in the set itself counts as divergent.
    """
    per_file = collections.defaultdict(dict)     # item -> {sidecar: frozenset(paths)}
    seen = collections.defaultdict(lambda: collections.defaultdict(set))
    for path in sidecars:
        name = os.path.basename(path)
        rows = collections.defaultdict(set)
        for row in schemapath_io.read(path):
            item = (row.get("Metadata Item") or "").strip()
            sp = (row.get("Schema Path") or "").strip()
            if not item or not sp:
                continue          # flagged rows carry no mapping to compare
            canon = _canon(sp)
            rows[item].add(canon)
            seen[item][canon].add(name)
        for item, paths in rows.items():
            per_file[item][name] = frozenset(paths)

    out = {}
    for item, by_file in per_file.items():
        paths = seen[item]
        if len(by_file) < 2:
            out[item] = ("", paths)                      # one sidecar -> technique-specific
        elif len(set(by_file.values())) == 1:
            out[item] = (SHARED, paths)                  # every sidecar maps it identically
        else:
            out[item] = (DIVERGENT, paths)               # the mapping genuinely differs
    return out


def apply_scope(sidecars, scopes, dry_run=False):
    changed = 0
    for path in sidecars:
        rows = schemapath_io.read(path)
        dirty = False
        for row in rows:
            item = (row.get("Metadata Item") or "").strip()
            want = scopes.get(item, ("", None))[0] if item else ""
            if (row.get("Scope") or "") != want:
                row["Scope"] = want
                dirty = True
        if dirty:
            changed += 1
            if not dry_run:
                schemapath_io.write(path, rows)
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report only; write nothing")
    ap.add_argument("--list-shared", action="store_true", help="also list the shared items")
    args = ap.parse_args()

    sidecars = sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.csv")))
    if not sidecars:
        raise SystemExit("no docs/*.schemapaths.csv found")
    scopes = classify(sidecars)

    shared = sorted(i for i, (s, _) in scopes.items() if s == SHARED)
    divergent = sorted(i for i, (s, _) in scopes.items() if s == DIVERGENT)
    specific = sorted(i for i, (s, _) in scopes.items() if s == "")

    print(f"{len(sidecars)} sidecars, {len(scopes)} distinct Metadata Items")
    print(f"  shared     {len(shared):>4d}  (2+ sidecars agree — skip these)")
    print(f"  divergent  {len(divergent):>4d}  (2+ sidecars disagree — worth a look)")
    print(f"  (blank)    {len(specific):>4d}  (single sidecar — technique-specific)")

    if args.list_shared:
        print("\nshared:")
        for item in shared:
            path = next(iter(scopes[item][1]))
            print(f"  {item}\n      {path}")

    if divergent:
        print("\ndivergent — same item, different mappings:")
        for item in divergent:
            print(f"  {item}")
            for path, files in sorted(scopes[item][1].items(), key=lambda kv: -len(kv[1])):
                tags = ", ".join(sorted(f.replace(".schemapaths.csv", "") for f in files))
                print(f"      [{len(files)}] {path}")
                print(f"           {tags}")

    changed = apply_scope(sidecars, scopes, dry_run=args.dry_run)
    print()
    if args.dry_run:
        print(f"dry run: {changed} sidecar(s) would gain/change a Scope value")
    else:
        print(f"wrote Scope into {changed} sidecar(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
