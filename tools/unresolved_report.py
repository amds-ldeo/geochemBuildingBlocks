#!/usr/bin/env python3
"""Worklists for the two remaining backlogs, grouped by SHAPE so they can be cleared in batches.

Both are long lists of individually-boring rows that collapse to a handful of causes, so the useful
unit of work is the shape, not the row. Emits a markdown summary for reading and one CSV per
backlog for working through.

  unrecognised   a sidecar Schema Path that normalize_schema_paths.recognize() rejects. Either the
                 path is wrong, or the grammar is missing a family that the sidecars already use —
                 the D/E gaps closed earlier were the latter, so check before assuming the former.
                 An emitter cannot consume these, so they are silently absent from generated schemas.

  dual-home      a (Protocol, Analysis) tier pair the matrix says carries BOTH a protocol default
                 and a per-analysis value, where add_dual_home_rows could not derive the $Dataset
                 counterpart. Two different things land here:
                   identity          not dual-homed at all — schema:name / schema:description /
                                     schema:location have no per-analysis counterpart to add
                   first-class pair  genuinely dual-homed, but through a property that exists under
                                     BOTH roots (Coupled Technique(s) -> schema:relatedLink), so
                                     there is no `Default` tail for the mirror to key on
                 Telling them apart is the judgement call; the shape grouping makes it one decision
                 per shape rather than 165.

Usage:
    python tools/unresolved_report.py                 # summary to stdout
    python tools/unresolved_report.py --write         # + docs/unresolved-*.csv
"""
import argparse
import collections
import csv
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import add_dual_home_rows as adh  # noqa: E402
import mark_shared_mappings as msm  # noqa: E402  (the workbook Analyte-Specific marker)
import normalize_schema_paths as norm  # noqa: E402
import schemapath_io  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UNREC_CSV = os.path.join(ROOT, "docs", "unresolved-paths.csv")
DUAL_CSV = os.path.join(ROOT, "docs", "unresolved-dualhome.csv")
UNREC_FIELDS = ["shape", "Metadata Item", "sidecar", "Protocol Tier", "Analysis Tier",
                "current Schema Path", "verdict", "corrected Schema Path", "note"]
DUAL_FIELDS = ["shape", "Metadata Item", "sidecar", "Protocol Tier", "Analysis Tier",
               "Analyte-Specific", "TAPP Schema Path", "verdict", "$Dataset counterpart", "note"]


def shape_of(path):
    """Collapse a path to its family shape: literals and ada: local names blanked."""
    if not path:
        return "(no path — flagged row)"
    s = re.sub(r"'[^']*'", "'…'", path)
    return re.sub(r"ada:[A-Za-z][A-Za-z0-9]*", "ada:*", s)


def collect():
    unrec, dual = [], []
    sidecars = sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.csv")))
    # A per-analyte property CANNOT be dual-homed: the analyte column carries read-only vs editable
    # on schema:readonlyValue, so there is no analysis-tier path to pair with. add_dual_home_rows
    # already skips items whose PATH is the analyte template — so a row that is marked here and
    # still unresolved has a mismatch: the workbook says per-analyte, the path says otherwise.
    marked = msm.analyte_specific_by_item(sidecars)
    for f in sidecars:
        short = os.path.basename(f).replace(".schemapaths.csv", "")
        for r in schemapath_io.read(f):
            p = (r.get("Schema Path") or "").strip()
            if not p:
                continue
            canon = norm.mechanical(norm.preclean(p))
            if norm.recognize(canon)[0] is None:
                unrec.append({"shape": shape_of(canon), "Metadata Item": r.get("Metadata Item", ""),
                              "sidecar": short, "Protocol Tier": r.get("Protocol Tier", ""),
                              "Analysis Tier": r.get("Analysis Tier", ""),
                              "current Schema Path": canon,
                              "verdict": "", "corrected Schema Path": "", "note": ""})
        _rows, _adds, unresolved = adh.plan(f)
        for item, tiers, p in unresolved:
            canon = norm.mechanical(norm.preclean(p)) if p else ""
            dual.append({"shape": shape_of(canon), "Metadata Item": item, "sidecar": short,
                         "Protocol Tier": tiers[0], "Analysis Tier": tiers[1],
                         "Analyte-Specific": "yes" if item in marked.get(short, ()) else "",
                         "TAPP Schema Path": canon,
                         "verdict": "", "$Dataset counterpart": "", "note": ""})
    return unrec, dual


def summarise(title, rows, key, blurb):
    by = collections.defaultdict(list)
    for r in rows:
        by[r["shape"]].append(r)
    out = [f"## {title} — {len(rows)} rows, {len(by)} shapes", "", blurb, ""]
    for shape, rs in sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        cars = sorted({r["sidecar"] for r in rs})
        items = sorted({r["Metadata Item"] for r in rs})
        spec = sorted({r["Metadata Item"] for r in rs if r.get("Analyte-Specific")})
        out += [f"### {len(rs)} rows — `{shape}`", "",
                f"- **sidecars** ({len(cars)}): {', '.join(cars)}",
                f"- **items** ({len(items)}): " + ", ".join(items[:8])
                + (" …" if len(items) > 8 else ""),
                f"- **example**: `{rs[0][key]}`"]
        if spec:
            out += [f"- **Analyte-Specific** ({len(spec)}): " + ", ".join(spec[:8])
                    + (" …" if len(spec) > 8 else "")
                    + " — cannot be dual-homed; belongs in the analyte column template"]
        out += [""]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="also write the two CSV worklists")
    args = ap.parse_args()

    unrec, dual = collect()
    lines = ["# Unresolved schema-path backlogs", "",
             "Generated by `tools/unresolved_report.py`. Grouped by shape: each heading is one",
             "decision, not one row.", ""]
    lines += summarise(
        "Unrecognised sidecar paths", unrec, "current Schema Path",
        "`recognize()` rejects these, so no emitter consumes them. For each shape decide whether "
        "the PATH is wrong (fix the sidecar) or the GRAMMAR is missing a family it already uses "
        "(add it to `recognize()` and `SCHEMA_PATH_GRAMMAR.md`). Fill `verdict` with "
        "`fix-path` or `add-family`.")
    lines += summarise(
        "Dual-home counterparts not derivable", dual, "TAPP Schema Path",
        "The tier matrix wants a `$Dataset` partner but the mirror could not build one. For each "
        "shape decide `identity` (no counterpart exists — nothing to do) or `first-class-pair` "
        "(a counterpart IS wanted; give the path). Fill `verdict` accordingly.")

    print("\n".join(lines))

    if args.write:
        for path, fields, rows in ((UNREC_CSV, UNREC_FIELDS, unrec),
                                   (DUAL_CSV, DUAL_FIELDS, dual)):
            rows.sort(key=lambda r: (r["shape"], r["Metadata Item"], r["sidecar"]))
            with open(path, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=fields)
                w.writeheader()
                w.writerows(rows)
            print(f"\nwrote {len(rows)} rows -> {os.path.relpath(path, ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
