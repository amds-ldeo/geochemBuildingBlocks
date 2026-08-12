#!/usr/bin/env python3
"""Read a TAPP source table, whichever format it is in.

The library moved from xlsx to CSV with the 2026-08-11 delivery, and the delivery README is
explicit that the CSV is the source of truth and the xlsx a generated artifact that should not be
parsed for content. The path-driven pipeline had three separate readers, each opening the workbook
with openpyxl and re-deriving the header layout — so switching source format meant changing the
same logic three times, in three slightly different forms.

This is the one primitive they all actually wanted: the TAPP sheet as a list of row tuples, header
first. Everything above it — locating columns, skipping group headers, finding the mode block —
stays where it was.

CSV rows are normalised to look exactly like openpyxl's: padded to the header width, and empty
cells returned as None rather than ''. Callers already treat both as absent (build_tapp.norm maps
each to ""), but matching openpyxl exactly means a reader cannot behave differently on one format
than the other.

Encoding is utf-8-sig: the library's CSVs carry a BOM, and their content includes superscripts and
Greek that must survive (²⁰⁶Pb/²³⁸U, δ⁵⁶Fe, J cm⁻²).
"""
import csv
import os


def rows(path):
    """The TAPP table as a list of row tuples, header first. Accepts .csv or .xlsx."""
    if str(path).lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8-sig") as f:
            raw = [list(r) for r in csv.reader(f)]
        if not raw:
            return []
        width = len(raw[0])
        return [tuple((c if c != "" else None) for c in (r + [""] * (width - len(r)))[:width])
                for r in raw]

    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    sheet = "TAPP" if "TAPP" in wb.sheetnames else wb.sheetnames[0]
    out = list(wb[sheet].iter_rows(values_only=True))
    wb.close()
    return out


def exists(path):
    return bool(path) and os.path.exists(path)
