#!/usr/bin/env python3
"""Fill flagged sidecar rows by copying an item's placement from the sidecar that already solved it.

A flagged row is a Metadata Item with no Schema Path: the generator emits nothing for it. Most
flagged rows are not open questions — the same item is already placed in another technique's
sidecar, because these tables share a large identity/QA core. Copying is then a mechanical act, and
doing it by hand across eight files is how drift starts.

What this deliberately does NOT do is guess. Every fill is an explicit entry below naming the SOURCE
sidecar and why it wins, because "some other sidecar has a path" is not sufficient on its own:

  - several items have TWO placements in circulation, and the tie is broken by provenance
    (Source=authored beats Source=inferred) plus tier agreement, not by counting;
  - a path bootstrap inferred is not independent evidence — it is the rule set agreeing with itself,
    so an item whose only precedent is a freshly bootstrapped technique stays flagged.

Tiers and Data Type come from the TARGET row, never the source: the same item can sit at different
tiers in different techniques, and the tier drives requiredness downstream.

    python tools/fill_flagged.py                 # report what would be filled
    python tools/fill_flagged.py --write
    python tools/fill_flagged.py --item "Sample Name" --write
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schemapath_io

# item -> (source TAPP, why that source, note recorded on each filled row)
FILLS = {
    "Sample Name": (
        "empaTAPP",
        "identical in all 8 sidecars that place it",
        "shared analysis-instance row"),
    "Analytical Mode": (
        "empaTAPP",
        "identical in all 8 sidecars that place it",
        "shared procedure row"),
    "Additional Notes": (
        "empaTAPP",
        "identical in all 8 sidecars that place it",
        "dual-home decision: procedure default + analysis-tier value"),
    "Constants and Reference Values Used": (
        "geochronTAPP",
        "authored, and Basic/Editable like every target; the competing temTAPP variant is "
        "bootstrap-inferred",
        "data-reduction step parameter, following geochronTAPP"),
    # --- wave-1 triage, reviewer-decided 2026-08-20. Each was flagged in SEM_Composition and
    # --- already placed elsewhere; the two that had rival placements were decided explicitly.
    "Analysis Inclusion and Rejection Criteria": (
        "empaTAPP",
        "reviewer: the EPMA/SEM data-reduction step parameter is correct; TEM's bare "
        "ada:analysisInclusionAndRejectionCriteria was bootstrap-inferred and has been realigned",
        "data-reduction step parameter"),
    "EDS Dead Time": (
        "temTAPP",
        "reviewer tie-break between two authored placements: TEM's ada:deadTime wins over the "
        "additionalProperty form, which has been realigned in EPMA and SEM",
        "analysis-instance dead time, following temTAPP"),
    "EDS Map Dimensions": (
        "semTAPP",
        "the only placement, authored",
        "map dimensions on the dataset"),
    "Map Area": (
        "empaTAPP",
        "identical authored placement in empaTAPP and semTAPP",
        "shared analysis-instance row"),
    "Procedural Blank Level": (
        "empaTAPP",
        "identical authored placement in empaTAPP and semTAPP",
        "shared analysis-instance row"),
    "Session Identifier": (
        "semTAPP",
        "reviewer's standing rule: the session identifier is always the analysis activity's own "
        "schema:identifier, in every technique",
        "analysis-session identifier"),
    "Target Selection Criteria": (
        "empaTAPP",
        "authored by hand in empaTAPP, semTAPP and labxctTAPP with the identical path; the only "
        "competing variant is the bootstrap-inferred dual-home pair in the LA family and temTAPP, "
        "and an inferred path is not independent evidence",
        "procedure default, following the authored empaTAPP/semTAPP placement"),
    "Reported Variables and Units": (
        "geochronTAPP",
        "the only placement; authored as the reported-property pilot",
        "follows the geochronTAPP reported-property pilot — revisit with that workstream"),
}


def sidecars():
    out = {}
    for t in sorted(b.TAPP_CONFIGS):
        b.configure(t)
        p = schemapath_io.csv_path(b.XLSX)
        if os.path.exists(p):
            out[t] = p
    return out


def paths_for(csv_file, item):
    """The item's paths in file order, de-duplicated."""
    seen, out = set(), []
    for r in schemapath_io.read(csv_file):
        if (r.get("Metadata Item") or "").strip() != item:
            continue
        p = (r.get("Schema Path") or "").strip()
        if p and p not in seen:
            seen.add(p)
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--item", action="append", help="limit to one item (repeatable)")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    files = sidecars()
    wanted = a.item or list(FILLS)
    unknown = [i for i in wanted if i not in FILLS]
    if unknown:
        raise SystemExit(f"no FILLS entry for: {', '.join(unknown)}")

    plan = collections.defaultdict(list)      # tapp -> [(item, [paths], note)]
    for item in wanted:
        src, why, note = FILLS[item]
        if src not in files:
            print(f"SKIP {item!r}: source {src} has no sidecar")
            continue
        ps = paths_for(files[src], item)
        if not ps:
            print(f"SKIP {item!r}: {src} has no path for it")
            continue
        print(f"{item!r}\n    from {src} ({why})")
        for p in ps:
            print(f"      {p}")
        for t, f in files.items():
            if t == src:
                continue
            if any((r.get("Metadata Item") or "").strip() == item
                   and not (r.get("Schema Path") or "").strip()
                   for r in schemapath_io.read(f)):
                plan[t].append((item, ps, note))
        print(f"    -> {', '.join(sorted(plan[t][-1][0] and t for t in plan if plan[t] and plan[t][-1][0] == item)) or '(none flagged)'}\n")

    total = 0
    for t, jobs in sorted(plan.items()):
        rows = schemapath_io.read(files[t])
        fill = {item: (ps, note) for item, ps, note in jobs}
        out, done = [], set()
        for r in rows:
            it = (r.get("Metadata Item") or "").strip()
            if it in fill and not (r.get("Schema Path") or "").strip():
                if it in done:
                    continue
                done.add(it)
                ps, note = fill[it]
                for p in ps:
                    n = dict(r)
                    n["Schema Path"] = p
                    n["Source"] = "authored"
                    n["Notes"] = note
                    out.append(n)
                total += len(ps)
                continue
            out.append(r)
        print(f"  {t:<22s} {len(rows):3d} -> {len(out):3d} rows   filled {', '.join(sorted(done))}")
        if a.write:
            schemapath_io.write(files[t], out)

    print(f"\n{total} row(s) {'written' if a.write else 'would be written'} "
          f"across {len(plan)} sidecar(s)")
    if not a.write:
        print("(dry run — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
