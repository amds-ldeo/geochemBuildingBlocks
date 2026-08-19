"""Backfill the 'Key by' column across all docs/*.schemapaths.csv sidecars.

The workbook 'Keyed By' declaration routes a template-family row to its canonical Schema Path
(see bootstrap_schemapaths.keyed_path) and marks the row Source=keyed. bootstrap emits a 'Key by'
column recording the declaration, but the older sidecars were generated before that column existed,
so only LA-MC-ICPMS carries it. This makes the column uniform: every sidecar gets it, and for a
Source=keyed row whose declaration is recoverable from the routed path, the value is filled in.
Rows already carrying a Key by value (hand-authored, e.g. LA-MC's 'channel') are left untouched.

Line-preserving: appends one field to each raw line rather than rewriting the CSV, so quoting,
BOM and CRLF are unchanged and the diff is purely the new column.

    python tools/backfill_keyby.py            # write
    python tools/backfill_keyby.py --dry-run
"""
import csv, glob, io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# routed Schema Path -> the 'Keyed By' declaration that produces it (inverse of keyed_path's routes).
# Only the technique-agnostic families keyed_path handles are recoverable; channel / standard keys
# are not routed (they fall through to inference), so they cannot be reconstructed here.
def kb_from_path(p):
    if "ada:analyteTemplate.ada:defaultAnalytes" in p:
        return "defines: analyte"
    if "ada:analyteTemplate.ada:analyteColumns" in p:
        return "analyte"
    if "ada:reportedPropertyTemplate.ada:defaultReportedProperties" in p or p.endswith("ada:reportedProperties[]"):
        return "defines: reported property"
    if "schema:variableMeasured[" in p:
        return "reported property"
    if p.endswith("ada:samplingUnit"):
        return "defines: sampling unit"
    if "schema:object[" in p and p.endswith(".schema:name"):
        return "defines: sample"
    if "schema:object[" in p and ".schema:additionalProperty[" in p:
        return "sample"
    return ""


def fields(line):
    return next(csv.reader(io.StringIO(line)))


def process(path, dry):
    with open(path, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    # keepends split; a trailing newline yields a final empty piece we drop
    lines = raw.splitlines(keepends=True)
    if not lines:
        return 0
    hdr = fields(lines[0])
    if "Key by" in hdr:
        return 0                                        # already uniform (LA-MC-ICPMS)
    try:
        i_src = hdr.index("Source"); i_path = hdr.index("Schema Path")
    except ValueError:
        return 0
    filled = 0
    out = []
    for n, ln in enumerate(lines):
        body = ln.rstrip("\r\n"); eol = ln[len(body):]
        if n == 0:
            out.append(body + ",Key by" + eol); continue
        if not body.strip():
            out.append(ln); continue
        row = fields(body)
        kb = ""
        if len(row) > max(i_src, i_path) and row[i_src].strip() == "keyed":
            kb = kb_from_path(row[i_path].strip())
            if kb:
                filled += 1
        out.append(body + "," + kb + eol)
    if not dry:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("".join(out))
    return filled


def main():
    dry = "--dry-run" in sys.argv
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.csv"))):
        filled = process(f, dry)
        print(f"{os.path.basename(f):42} +Key by  filled={filled}")


if __name__ == "__main__":
    main()
