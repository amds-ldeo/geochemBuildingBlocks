"""Write a 'SchemaPaths' worksheet into a copy of a TAPP workbook, showing the canonical schema path
bootstrap_schemapaths.py infers for each row (and FLAGGING rows it can't resolve).

Reuses the exact bootstrap inference (library reuse + content inference + overrides sidecar), so the
sheet is a faithful preview of what feeds the path-driven generator. Writes to a sibling copy by
default (the originals are working files, often open); pass --inplace to modify the workbook itself.

    python tools/write_schemapath_sheet.py docs/EPMA_TAPP_v7.xlsx
    python tools/write_schemapath_sheet.py docs/EPMA_TAPP_v7.xlsx --inplace
"""
import json
import os
import sys

import openpyxl
from openpyxl.styles import Font, PatternFill

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bootstrap_schemapaths as bs
import normalize_schema_paths as norm
import schema_path_parser as spp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def infer_rows(wb_path):
    lib = json.load(open(bs.LIB_SPEC, encoding="utf-8"))
    lib_norm = {bs._norm(k): v for k, v in lib.items()}
    sc = os.path.splitext(wb_path)[0] + ".overrides.json"
    sidecar = json.load(open(sc, encoding="utf-8")) if os.path.exists(sc) else {}
    out = []
    for row in bs.load_rows(wb_path):
        path, src = bs.infer(row, lib, lib_norm, sidecar)
        canon, status = "", ""
        if path:
            canon = norm.mechanical(norm.preclean(path))
            try:
                spp.parse(canon)
                status = src
            except spp.SchemaPathError as e:
                canon, status = "", f"FLAGGED: parse-fail ({e})"
        else:
            status = f"FLAGGED: {src}"
        out.append((row["item"], row["P"], row["A"], canon, status))
    return out


def write_sheet(wb_path, inplace=False):
    rows = infer_rows(wb_path)
    wb = openpyxl.load_workbook(wb_path)          # data_only=False -> preserves formulas/values
    if "SchemaPaths" in wb.sheetnames:
        del wb["SchemaPaths"]
    ws = wb.create_sheet("SchemaPaths")
    hdr = ["Metadata Item", "Protocol Tier", "Analysis Tier", "Inferred Canonical Path", "Source / Status"]
    ws.append(hdr)
    for c in ws[1]:
        c.font = Font(bold=True)
    flag_fill = PatternFill("solid", fgColor="FFF3B0")   # highlight flagged rows
    for r in rows:
        ws.append(list(r))
        if r[4].startswith("FLAGGED"):
            for c in ws[ws.max_row]:
                c.fill = flag_fill
    for col, w in zip("ABCDE", (46, 14, 14, 60, 40)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A2"
    out = wb_path if inplace else os.path.splitext(wb_path)[0] + "_withpaths.xlsx"
    wb.save(out)
    n_flag = sum(1 for r in rows if r[4].startswith("FLAGGED"))
    print(f"{os.path.relpath(out, ROOT)}: {len(rows)} rows, {n_flag} flagged (highlighted) -> 'SchemaPaths' sheet")
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit("usage: write_schemapath_sheet.py <workbook.xlsx> [--inplace]")
    wb = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    write_sheet(wb, inplace="--inplace" in sys.argv)
