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


def refresh(tapp, write=False, force=False, source=None, add_keyed=False):
    """Re-sync one sidecar's Key by. `source` overrides the table, for MODULE sidecars, whose
    source is tapp/Claude Skills for TAPP/modules/Module_<Name>.csv rather than a TAPP workbook."""
    if source is None:
        b.configure(tapp)
        source = b.XLSX
    csv_path = schemapath_io.csv_path(source)
    if not os.path.exists(csv_path):
        print(f"{tapp:<22s} no sidecar at {os.path.relpath(csv_path)}")
        return 0, 0
    table_kb = ms.source_keyedby(source)
    if not table_kb:
        print(f"{tapp:<22s} source table declares no Keyed By column")
        return 0, 0

    rows = schemapath_io.read(csv_path)
    filled, conflicts, cleared, alternates = 0, [], 0, 0
    missing = {}

    def canon(p):
        try:
            return norm.mechanical(norm.preclean((p or "").strip()))
        except Exception:
            return (p or "").strip()

    def route_for(r):
        want = table_kb.get((r.get("Metadata Item") or "").strip(), "")
        if not want:
            return None
        return boot.keyed_path({"item": (r.get("Metadata Item") or "").strip(), "kb": want,
                                "P": (r.get("Protocol Tier") or ""),
                                "A": (r.get("Analysis Tier") or "")})

    # Which items ALREADY have a row sitting on the keyed route. An off-route row is an ALTERNATE
    # only if that keyed twin exists; where NOTHING sits on the route the keyed row is simply
    # MISSING, and treating its fallback as an alternate (the original behaviour) left the column
    # permanently unfillable - every Geochronology row reported `alternate-left-blank` forever.
    placed = set()
    for _r in rows:
        _rt = route_for(_r)
        if _rt and canon(_r.get("Schema Path")) in [canon(x) for x in _rt[0]]:
            placed.add((_r.get("Metadata Item") or "").strip())

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
            route = route_for(r)
            if route:
                on_route = [canon(x) for x in route[0]]
                if canon(r.get("Schema Path")) not in on_route:
                    if item in placed:
                        alternates += 1
                    else:
                        missing.setdefault(item, (route[0], want))
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

    added = 0
    if missing and add_keyed:
        for item, (paths, want) in missing.items():
            idx = max(i for i, r in enumerate(rows)
                      if (r.get("Metadata Item") or "").strip() == item)
            tmpl = rows[idx]
            have_paths = [canon(r.get("Schema Path")) for r in rows
                          if (r.get("Metadata Item") or "").strip() == item]
            for path in paths:
                if canon(path) in have_paths:
                    continue
                # An item whose only row carries no path at all is UNPLACED, not an alternate:
                # fill it in place rather than leaving a blank row beside a new keyed one.
                blank = next((r for r in rows
                              if (r.get("Metadata Item") or "").strip() == item
                              and not (r.get("Schema Path") or "").strip()), None)
                if blank is not None:
                    blank["Schema Path"] = path
                    blank["Key by"] = want
                else:
                    row = dict(tmpl)
                    row["Schema Path"] = path
                    row["Key by"] = want
                    row["Notes"] = "keyed route added by refresh_keyby"
                    idx += 1
                    rows.insert(idx, row)
                added += 1

    print(f"{tapp:<22s} {os.path.basename(csv_path):<34s} "
          f"filled {filled:<4d} conflict {len(conflicts):<4d} cleared {cleared:<4d} "
          f"alternate-left-blank {alternates:<4d} missing-keyed-row {len(missing)}"
          f"{f' (+{added} added)' if added else ''}")
    for item, have, want in conflicts[:10]:
        print(f"      CONFLICT {item!r}: sidecar={have!r} table={want!r}")
    for item, (paths, want) in missing.items():
        print(f"      MISSING KEYED ROW {item!r} (Keyed By {want!r}) - no row on:")
        for path in paths:
            print(f"          {path}")
    if (filled or cleared or added or (conflicts and force)) and write:
        schemapath_io.write(csv_path, rows)
        print(f"      wrote {os.path.relpath(csv_path)}")
    return filled, len(conflicts)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp", nargs="?", help="one TAPP name; omit (or --all) for every one")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--modules", action="store_true",
                    help="refresh the MODULE sidecars (docs/modules/) instead of the techniques'. "
                         "Their Key by column was never mirrored from the module CSVs at all.")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--add-keyed", action="store_true",
                    help="ADD the keyed row for an item that has no row on its domain route at "
                         "all. A keyed field carries two placements - the keyed one on the route, "
                         "and an unkeyed fallback for when the TAPP supplies no member list - and "
                         "this bootstraps the former where only the latter was ever authored.")
    ap.add_argument("--force", action="store_true",
                    help="also overwrite a Key by that disagrees with the table")
    a = ap.parse_args()

    tot_f = tot_c = 0
    if a.modules:
        import glob
        import module_composition as mc
        for src in sorted(glob.glob(os.path.join(mc.ts.modules_dir(), "Module_*.csv"))):
            name = os.path.basename(src)[len("Module_"):-len(".csv")]
            if a.tapp and a.tapp != name:
                continue
            f, c = refresh(name, a.write, a.force, source=src, add_keyed=a.add_keyed)
            tot_f += f
            tot_c += c
    else:
        targets = [a.tapp] if a.tapp else sorted(b.TAPP_CONFIGS)
        for t in targets:
            f, c = refresh(t, a.write, a.force, add_keyed=a.add_keyed)
            tot_f += f
            tot_c += c
    print(f"\n{tot_f} value(s) filled, {tot_c} conflict(s)"
          f"{'' if a.write else '   (dry run - pass --write)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
