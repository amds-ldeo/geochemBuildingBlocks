#!/usr/bin/env python3
"""Re-sync a sidecar's `Key by` column from its source TAPP table.

`Key by` MIRRORS the table's `Keyed By` declaration — it is not authored here. It is also the
column most easily lost: it sits last, so a round-trip through Excel or a hand edit that rewrites
the file can drop or blank it without touching anything else, and nothing downstream complains
because a blank Key by simply means "no keyed routing for this row". EPMA_TAPP_v25 lost all 39 of
its values that way.

migrate_sidecar refreshes this column too, but only when migrating onto a NEW table revision.
This is the standalone repair for a sidecar that is already on the right revision.

Fills blanks and reports them. A row whose Key by disagrees with the table is a CONFLICT and is
left alone unless --force: the table is authoritative for the column, but silently overwriting a
value someone deliberately changed is how curation gets lost.

    python tools/refresh_keyby.py                    # report every sidecar
    python tools/refresh_keyby.py empaTAPP --write
    python tools/refresh_keyby.py --all --write
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap_schemapaths as boot
import build_tapp as b
import migrate_sidecar as ms
import normalize_schema_paths as norm
import schemapath_io


def refresh(tapp, write=False, force=False):
    b.configure(tapp)
    csv_path = schemapath_io.csv_path(b.XLSX)
    if not os.path.exists(csv_path):
        print(f"{tapp:<22s} no sidecar at {os.path.relpath(csv_path)}")
        return 0, 0
    table_kb = ms.source_keyedby(b.XLSX)
    if not table_kb:
        print(f"{tapp:<22s} source table declares no Keyed By column")
        return 0, 0

    rows = schemapath_io.read(csv_path)
    filled, conflicts, cleared, alternates = 0, [], 0, 0

    def canon(p):
        try:
            return norm.mechanical(norm.preclean((p or "").strip()))
        except Exception:
            return (p or "").strip()

    for r in rows:
        item = (r.get("Metadata Item") or "").strip()
        want = table_kb.get(item, "")
        have = (r.get("Key by") or "").strip()

        # ALTERNATE PLACEMENTS. A field keyed to a domain can carry two rows: the keyed one, whose
        # path is the domain route, and an unkeyed alternate used when the TAPP does not supply the
        # domain's member list (no `defines: …` field populated). Only the row that actually sits on
        # the route carries the key; filling the alternate from the table would collapse the two
        # into one and silently delete the fallback placement.
        if want and not have:
            route = boot.keyed_path({"item": item, "kb": want,
                                         "P": (r.get("Protocol Tier") or ""),
                                         "A": (r.get("Analysis Tier") or "")})
            if route:
                on_route = [canon(x) for x in route[0]]
                if canon(r.get("Schema Path")) not in on_route:
                    alternates += 1
                    continue
        if ms._norm(have) == ms._norm(want):
            continue
        if not have:
            if want:
                r["Key by"] = want
                filled += 1
        elif not want:
            # the table no longer declares one; only --force clears a value that is there
            if force:
                r["Key by"] = ""
                cleared += 1
            else:
                conflicts.append((item, have, "(none)"))
        else:
            if force:
                r["Key by"] = want
            conflicts.append((item, have, want))

    print(f"{tapp:<22s} {os.path.basename(csv_path):<34s} "
          f"filled {filled:<4d} conflict {len(conflicts):<4d} cleared {cleared:<4d} "
          f"alternate-left-blank {alternates}")
    for item, have, want in conflicts[:10]:
        print(f"      CONFLICT {item!r}: sidecar={have!r} table={want!r}")
    if (filled or cleared or (conflicts and force)) and write:
        schemapath_io.write(csv_path, rows)
        print(f"      wrote {os.path.relpath(csv_path)}")
    return filled, len(conflicts)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp", nargs="?", help="one TAPP name; omit (or --all) for every one")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="also overwrite a Key by that disagrees with the table")
    a = ap.parse_args()

    targets = [a.tapp] if a.tapp else sorted(b.TAPP_CONFIGS)
    tot_f = tot_c = 0
    for t in targets:
        f, c = refresh(t, a.write, a.force)
        tot_f += f
        tot_c += c
    print(f"\n{tot_f} value(s) filled, {tot_c} conflict(s)"
          f"{'' if a.write else '   (dry run - pass --write)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
