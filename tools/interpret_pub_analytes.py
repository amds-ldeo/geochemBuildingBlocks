"""Heuristic analyte-axis inference for the publication columns of the TAPP
spreadsheet. For each pub column, parses:

  Row 59 — Primary Calibration Standard Name. Standard entries shaped like
           "Anorthite (Si Kα, Al Kα, Ca Kα); Albite (Na Kα); ..." are split
           on `;` (or `,` when there's no `;`); each entry's parenthetical
           is parsed for element symbols (and optional X-ray line tags) so
           we get {element: (line, standard)}.
  Row 64 — Typical Detection Limit. Two patterns supported:
             * "<Compound>: <value>; <Compound>: <value>; …"  (per-compound)
             * "<value> for <Compound>, <Compound>, …; <value> for …"
           Compounds are either bare element symbols (Si, Mg, …) or oxide
           formulas (SiO2, Al2O3, Cr2O3, FeO, …) — the element is extracted
           from the oxide.
  Row 48 — Halogen Correction on Oxygen. F, Cl, OH, CO2, S mentions are
           treated as analytes when present.

Outputs `<pub>-interp` columns at the right edge of the worksheet. The
interp column carries:
  - row 32 (Target Element) → pipe-delim inferred analyte list
  - row 40 (X-ray Line) → pipe-delim per-analyte (empty entries permitted)
  - row 59 (Calibration Standard) → pipe-delim per-analyte standards
  - row 60 (Secondary Reference) → verbatim from source pub (single value
    applies to all; we don't try to align)
  - row 64 (Detection Limit) → pipe-delim per-analyte limits
  - all other rows → verbatim copy of the source pub cell

Writes to docs/TAPP_EPMA_filled-interp.xlsx (a side file) so Excel's lock
on the source doesn't matter; review and merge into the source when ready.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from shutil import copyfile

import openpyxl

# Force UTF-8 stdout on Windows so we can print α/β safely.
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError):
    pass

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "docs" / "TAPP_EPMA_filled.xlsx"
OUT = REPO / "docs" / "TAPP_EPMA_filled-interp.xlsx"

# Periodic-table-ish set of element symbols we recognise.
KNOWN_ELEMENTS = set("""
H He Li Be B C N O F Ne
Na Mg Al Si P S Cl Ar
K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe
Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
Fr Ra Ac Th Pa U Np Pu
""".split())

# Volatiles / non-element analytes treated as such per user note (row 48).
VOLATILES = ("F", "Cl", "OH", "CO2", "S", "H2O")

# Match a "Standard (...)" entry: name (left) + parenthetical content (right).
ENTRY_RE = re.compile(r"([^();,]+?)\s*\(([^)]+)\)")

# Match an element symbol optionally followed by an X-ray line designation.
EL_LINE_RE = re.compile(
    r"([A-Z][a-z]?)"
    r"(?:\s+(K\s*[αβaαβalphaαβ]|L\s*[αβalphabetaαβ]|"
    r"K\s*alpha|K\s*beta|L\s*alpha|L\s*beta|Kα|Kβ|Lα|Lβ))?"
)

# Oxide pattern: element + optional digit + O + optional digit
OXIDE_RE = re.compile(r"\b([A-Z][a-z]?)\d*O\d*\b")

# Limit pattern A: "<value> for X, Y, Z" — value first, then "for" and a list.
LIMIT_FOR_RE = re.compile(r"([^;]*?)\s+for\s+([^;]+)", re.IGNORECASE)
# Limit pattern B: "Compound: value" or "Compound = value"
LIMIT_KV_RE = re.compile(r"\b([A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)?)\s*[:=]\s*([^;,]+)")


def parse_calibration(text: str) -> list[tuple[str, str | None, str]]:
    """Returns [(element, xray_line_or_None, standard_name), ...] in document order."""
    if not text:
        return []
    out = []
    seen = set()
    # Try splitting on `;` first; if there's none, try `,` as separator between entries.
    # ENTRY_RE handles either since it stops at `()` boundaries.
    for m in ENTRY_RE.finditer(text):
        standard = m.group(1).strip(" ;,").strip()
        if standard.lower().startswith("for "):
            # avoid matching "for SiO2" as the standard — usually a detection-limit phrasing
            continue
        inner = m.group(2)
        for piece in re.split(r"[,;]", inner):
            piece = piece.strip()
            em = EL_LINE_RE.match(piece)
            if not em:
                continue
            element = em.group(1)
            if element not in KNOWN_ELEMENTS:
                continue
            line = em.group(2)
            if line:
                line = line.strip().replace("alpha", "α").replace("beta", "β").replace("a", "α") if line.lower().endswith("alpha") else line.strip()
            key = (element, standard)
            if key in seen:
                continue
            seen.add(key)
            out.append((element, line, standard))
    return out


def parse_detection_limits(text: str) -> list[tuple[str, str]]:
    """Returns [(element, detection_limit_string), ...] in document order.
    Element may come from an oxide formula (Cr extracted from Cr2O3) or
    a bare element symbol."""
    if not text:
        return []
    out = []
    seen = set()
    # Pattern B first ("Compound: value")
    for m in LIMIT_KV_RE.finditer(text):
        compound = m.group(1).strip()
        value = m.group(2).strip()
        # Try as oxide
        ox = OXIDE_RE.match(compound)
        if ox and ox.group(1) in KNOWN_ELEMENTS:
            element = ox.group(1)
        elif compound in KNOWN_ELEMENTS:
            element = compound
        else:
            continue
        if element in seen:
            continue
        seen.add(element)
        out.append((element, value))
    # Pattern A ("<value> for X, Y, Z")
    for m in LIMIT_FOR_RE.finditer(text):
        value = m.group(1).strip(" ;,")
        compounds_str = m.group(2)
        for piece in re.split(r"[,;]", compounds_str):
            piece = piece.strip()
            ox = OXIDE_RE.match(piece)
            if ox and ox.group(1) in KNOWN_ELEMENTS:
                element = ox.group(1)
            elif piece in KNOWN_ELEMENTS:
                element = piece
            else:
                continue
            if element in seen:
                continue
            seen.add(element)
            out.append((element, value))
    return out


def parse_volatiles_row(text: str) -> list[str]:
    """Scan free text for mentions of F, Cl, OH, CO2, S, H2O."""
    if not text:
        return []
    out = []
    for v in VOLATILES:
        # word-boundary-ish match
        if re.search(rf"(?<![A-Za-z]){re.escape(v)}(?![A-Za-z0-9])", text):
            out.append(v)
    return out


def merge_analytes(*lists: list) -> list[str]:
    """Combine multiple element/volatile lists, preserving order of first appearance."""
    out = []
    seen = set()
    for lst in lists:
        for el in lst:
            if el not in seen:
                seen.add(el)
                out.append(el)
    return out


def main():
    if not SRC.exists():
        sys.exit(f"source not found: {SRC}")

    # Copy source so we can write without conflicting with any Excel lock on original.
    copyfile(SRC, OUT)
    wb = openpyxl.load_workbook(OUT)
    ws = wb["TAPP"]

    # Discover pub columns by header pattern (row 1 starts with "P<digit>")
    pub_cols = []
    for c in range(7, ws.max_column + 1):
        h = ws.cell(row=1, column=c).value
        if h and isinstance(h, str) and re.match(r"^P\d", h.strip()):
            label = h.split("\n", 1)[0].split(":", 1)[0].strip()
            pub_cols.append((c, label, h))

    print(f"Found {len(pub_cols)} pub columns: {[p[1] for p in pub_cols]}")

    # Identify the relevant rows by label (locate by item label, not row number, in case of moves)
    label_to_row = {}
    for r in range(2, ws.max_row + 1):
        item = ws.cell(row=r, column=1).value
        if isinstance(item, str):
            label_to_row[item.strip()] = r
    rN = lambda lbl: label_to_row.get(lbl)

    R_TARGET = rN("Target Element")
    R_XRAY = rN("X-ray Line")
    R_HALOGEN = rN("Halogen Correction on Oxygen")
    R_CALIB = rN("Primary Calibration Standard Name")
    R_SECONDARY = rN("Secondary Reference Materials")
    R_DETLIM = rN("Typical Detection Limit")

    # Find first empty column at the right edge to start interp columns.
    insert_col = ws.max_column + 1

    print()
    for i, (src_col, label, full_header) in enumerate(pub_cols):
        cal_text = ws.cell(row=R_CALIB, column=src_col).value if R_CALIB else None
        det_text = ws.cell(row=R_DETLIM, column=src_col).value if R_DETLIM else None
        hal_text = ws.cell(row=R_HALOGEN, column=src_col).value if R_HALOGEN else None
        tgt_text = ws.cell(row=R_TARGET, column=src_col).value if R_TARGET else None

        cal_entries = parse_calibration(str(cal_text) if cal_text else "")
        det_entries = parse_detection_limits(str(det_text) if det_text else "")
        vol_entries = parse_volatiles_row(str(hal_text) if hal_text else "")

        # If the user has populated Target Element explicitly (pipe- or comma-delim),
        # use that as the primary analyte axis. Otherwise, infer from cal/det/vol.
        explicit = []
        if tgt_text:
            sep = "|" if "|" in str(tgt_text) else ","
            explicit = [a.strip() for a in str(tgt_text).split(sep) if a.strip()]
        if explicit:
            analyte_list = merge_analytes(explicit)
        else:
            analyte_list = merge_analytes(
                [e for e, _, _ in cal_entries],
                [e for e, _ in det_entries],
                vol_entries,
            )

        # Build maps from element → value for each interp row
        line_map = {e: ln for e, ln, _ in cal_entries}
        std_map = {e: std for e, _, std in cal_entries}
        det_map = {e: dl for e, dl in det_entries}

        # Build the interp column
        ic = insert_col + i
        ws.cell(row=1, column=ic, value=f"{label}-interp")

        # Copy verbatim from source pub for every row
        for r in range(2, ws.max_row + 1):
            v = ws.cell(row=r, column=src_col).value
            if v is not None:
                ws.cell(row=r, column=ic, value=v)

        # Override the analyte-axis rows with the inferred mappings (pipe-delim)
        if analyte_list:
            ws.cell(row=R_TARGET, column=ic, value="|".join(analyte_list))
            if R_XRAY:
                ws.cell(row=R_XRAY, column=ic,
                        value="|".join(line_map.get(e) or "" for e in analyte_list))
            if R_CALIB:
                ws.cell(row=R_CALIB, column=ic,
                        value="|".join(std_map.get(e) or "" for e in analyte_list))
            if R_DETLIM:
                ws.cell(row=R_DETLIM, column=ic,
                        value="|".join(det_map.get(e) or "" for e in analyte_list))

        print(f"  {label}: analytes = {analyte_list}")
        if cal_entries:
            print(f"    calib: {[(e, ln, st[:25]) for e, ln, st in cal_entries[:6]]}{'...' if len(cal_entries) > 6 else ''}")
        if det_entries:
            print(f"    detlim: {dict(det_entries[:6])}{'...' if len(det_entries) > 6 else ''}")

    wb.save(OUT)
    print(f"\nwrote {OUT}")
    print(f"  {len(pub_cols)} interp columns appended at columns {insert_col}..{insert_col + len(pub_cols) - 1}")
    print(f"\nReview the side file in Excel; merge interp columns into the source when satisfied.")


if __name__ == "__main__":
    main()
