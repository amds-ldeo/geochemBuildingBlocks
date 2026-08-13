#!/usr/bin/env python3
"""Give each composition module its own schema-path sidecar, seeded from the techniques.

A module field is shared by every table that composes the module — Group1's seventeen appear in all
sixteen delivery tables. Placing them per technique means reviewing the same decision sixteen times
and letting sixteen copies drift, which is the problem the modules exist to solve. So the module
gets ONE sidecar, beside its own CSV, and the technique sidecars keep only what they own.

Nothing here is invented. Every module field is already placed in the technique sidecars we curated,
so the seed is a vote across those, and the report says how strong each vote was:

  unanimous   every technique that places this field agrees        -> seeded, Source=authored
  majority    they disagree; the most common placement is taken    -> seeded, Source=inferred,
                                                                      Notes records the rivals
  unplaced    no technique places it                               -> flagged, blank path

Only `unanimous` is safe to take on trust. `majority` means the techniques genuinely disagree about
where a shared field lives, and that disagreement is the thing worth a human's attention — it is
recorded in the row rather than silently resolved.

    python tools/seed_module_sidecars.py            # report
    python tools/seed_module_sidecars.py --write
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import migrate_sidecar as ms
import schemapath_io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODDIR = os.path.join(ROOT, "TAPPS20260811", "Claude Skills for TAPP", "modules")


def technique_placements():
    """{normalized item -> {frozenset(paths) -> [tapp]}} from every curated sidecar."""
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for t in sorted(b.TAPP_CONFIGS):
        b.configure(t)
        p = schemapath_io.csv_path(b.XLSX)
        if not os.path.exists(p):
            continue
        per = collections.defaultdict(set)
        for r in schemapath_io.read(p):
            it = (r.get("Metadata Item") or "").strip()
            sp = (r.get("Schema Path") or "").strip()
            if it and sp:
                per[it].add(sp)
        for it, ps in per.items():
            out[ms._norm(ms.rename(it))][frozenset(ps)].append(t)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--module", action="append", help="limit to one module (repeatable)")
    a = ap.parse_args()

    placed = technique_placements()
    names = sorted(f[len("Module_"):-4] for f in os.listdir(MODDIR)
                   if f.startswith("Module_") and f.endswith(".csv"))
    if a.module:
        names = [n for n in names if n in a.module]

    tally = collections.Counter()
    for n in names:
        src = os.path.join(MODDIR, f"Module_{n}.csv")
        rows, report = [], []
        for item, P, A, dt in ms.source_items(src):
            # A module row with NEITHER tier is not a field this module owns — it is an overlay on
            # the Example / Allowed Content of a field owned elsewhere (Module_UPb carries twelve of
            # these, against Geochronology's and ReportingCore's fields, and supplies only U-Pb
            # examples for them). There is no placement to author: the owning module's sidecar
            # already says where the field lives, and a second row here would be a rival answer to a
            # question that is not being asked.
            if not P and not A:
                tally["overlay"] += 1
                continue
            variants = placed.get(ms._norm(ms.rename(item)))
            base = {"Metadata Item": item, "Protocol Tier": P, "Analysis Tier": A,
                    "Data Type": dt, "Scope": "module"}
            if not variants:
                rows.append({**base, "Schema Path": "", "Source": "flagged",
                             "Notes": "no technique places this field yet"})
                report.append(("unplaced", item, ""))
                tally["unplaced"] += 1
                continue
            # Rank by tier-correctness FIRST, popularity second. Counting alone picks the wrong
            # variant here: a dual-homed field that some techniques only half-placed has more
            # sidecars carrying the single-path version than the complete one, so the majority is
            # the incomplete answer. Arity is checkable against the matrix, so it outranks the vote.
            need = 2 if (P, A) in ms.DUAL_HOMED else 1
            ranked = sorted(variants.items(),
                            key=lambda kv: (abs(len(kv[0]) - need), -len(kv[1])))
            best, who = ranked[0]
            if len(ranked) == 1:
                note = f"unanimous across {len(who)} technique(s)"
                source = "authored"
                tally["unanimous"] += 1
                kind = "unanimous"
            else:
                rivals = "; ".join(f"{len(w)}x {sorted(v)[0]}" for v, w in ranked[1:])
                note = (f"majority {len(who)}/{sum(len(w) for _, w in ranked)} "
                        f"({', '.join(sorted(who))}); rivals: {rivals}")
                source = "inferred"
                tally["majority"] += 1
                kind = "majority"
            for sp in sorted(best):
                rows.append({**base, "Schema Path": sp, "Source": source, "Notes": note})
            report.append((kind, item, note))

        out_csv = schemapath_io.csv_path(src)
        u = sum(1 for k, _, _ in report if k == "unanimous")
        m = sum(1 for k, _, _ in report if k == "majority")
        f = sum(1 for k, _, _ in report if k == "unplaced")
        print(f"Module_{n:<20s} {len(report):3d} fields -> {len(rows):3d} rows   "
              f"unanimous {u:2d}   majority {m:2d}   unplaced {f:2d}")
        for kind, item, note in report:
            if kind != "unanimous":
                print(f"      [{kind}] {item}")
                if note:
                    print(f"               {note[:150]}")
        if a.write:
            schemapath_io.write(out_csv, rows)

    print(f"\nunanimous {tally['unanimous']}   majority {tally['majority']}   "
          f"unplaced {tally['unplaced']}")
    print("written" if a.write else "(dry run — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
