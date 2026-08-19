#!/usr/bin/env python3
"""
validate_tapp.py — structural and convention linter for the TAPP library.

Checks every TAPP CSV against the invariants and cross-TAPP consistency rules in
`references/conventions.md`. Reports violations; changes nothing.

Usage
-----
    python3 validate_tapp.py                          # lint latest version of every TAPP
    python3 validate_tapp.py --root /path/to/TAPPs
    python3 validate_tapp.py --severity ERROR         # errors only
    python3 validate_tapp.py --all-versions           # include superseded versions
    python3 validate_tapp.py --file EPMA/EPMA_TAPP_v9.csv
    python3 validate_tapp.py --csv findings.csv       # also write findings to CSV

Severity
--------
    ERROR  Structural invariant violated. The TAPP is malformed.
    WARN   Convention violated (naming, controlled vocabulary, Rules 1/3/5).
    INFO   Possible cross-TAPP drift. Needs human judgement — may be intentional.

Exit status is 1 if any ERROR was found, else 0.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# Column layout
#
# conventions.md contains two conflicting column tables. The detailed table in
# the "Column structure" section (G=Comments, H=Last Update, mode flags after)
# matches every file in the library and is what this script enforces. The
# summary table in SKILL.md (G=Last update, mode flags from H) does not.
# ---------------------------------------------------------------------------
COL_ITEM, COL_DESC, COL_C, COL_D, COL_TYPE, COL_EXAMPLE, COL_COMMENT, COL_UPDATE = range(8)
COL_KEYEDBY = 8  # Rule 7
FIRST_MODE_COL = 9
SENTINEL_HEADER = "Literature Assessment"

VALID_C = {"Basic", "Advanced", "N/A"}
VALID_D = {"Read-Only", "Editable", "Basic", "Advanced"}
VALID_MODE_FLAG = {"Y", "N"}

VALID_DATA_TYPES = {
    "Text (free)", "Controlled list", "Numeric + unit", "Boolean", "Integer",
    "Date", "URI / DOI", "URI / IGSN", "Text / URI",
}
# "Numeric (unit)" is a family: Numeric (W), Numeric (Hz), Numeric (µm), ...
# "Numeric pair (...)" is in wide use for map dimensions and is treated as valid.
NUMERIC_UNIT_RE = re.compile(r"^Numeric(?: pair)? \(.+\)$")

# Drifted spellings of a type that already exists in the vocabulary.
DATATYPE_SYNONYMS = {
    "free text": "Text (free)",
    "text (free text)": "Text (free)",
    "controlled vocabulary": "Controlled list",
    "controlled vocabulary (list)": "Controlled list",
    "controlled list (controlled vocabulary)": "Controlled list",
    "uri": "URI / DOI",
    "numeric (unit)": "Numeric + unit",  # the doc placeholder, not a real type
}

# Ratified compound types: a vocabulary label, " / ", then a fallback label.
# See "Compound data types" in conventions.md.
_ATOMIC = (r"Controlled list|URI / DOI|URI / IGSN|Text / URI|Numeric \+ unit|"
           r"Numeric pair \([^)]+\)|Numeric \([^)]+\)|Integer|Boolean|Date")
_FALLBACK = r"Text|Text \(free\)|Numeric \+ unit|Numeric \([^)]+\)"
COMPOUND_RE = re.compile(rf"^(?:{_ATOMIC}) / (?:{_FALLBACK})$")

# Malformed near-compounds: right idea, wrong construction.
MALFORMED_COMPOUND = {
    "numeric or text": "Numeric + unit / Text",
    "numeric (ms) or text": "Numeric (ms) / Text",
    "uri / text (free)": "URI / IGSN for IGSN fields, else Text / URI",
    "numeric + label": "Text (free)",
}

EXPECTED_GROUPS = [
    "1. Procedure Identification",
    "2. Samples",
    "3. Instrument & Software",
    "4. Measurement Information",
    "5. Data Processing",
    "6. Quality Control & Uncertainty",
]

COUPLING_FIELDS = [
    "Coupled Technique(s)",
    "Coupling Description",
    "Coupled Procedure DOI",
    "Coupled Dataset or Publication Reference",
]

# Rule 1 — forbidden name -> required name
FORBIDDEN_NAMES = {
    "lod": "Detection Limit",
    "limit of detection": "Detection Limit",
    "precision": "Analytical Precision",
    "accuracy": "Analytical Accuracy",
    "primary standard": "Primary Calibration Standard Name",
    "calibration material": "Primary Calibration Standard Name",
    "secondary standard": "Secondary Reference Materials",
    "monitor material": "Secondary Reference Materials",
    "spectral interference correction": "Interference Corrections Applied",
    "counting error": "Counting Statistics Error",
    "statistical error": "Counting Statistics Error",
    "method name": "Procedure Name",
    "method doi": "Procedure DOI",
}

# Rule 1 — required tiers for named cross-TAPP fields
REQUIRED_TIERS = {
    "Acquisition Software": ("Basic", "Editable"),
    "Data Reduction Software": ("Basic", "Editable"),
    "Analytical Mode": ("Basic", "Read-Only"),
    "Constants and Reference Values Used": ("Basic", "Editable"),
}

# Level-encoding words banned from field names (conventions.md "Level-neutral naming")
LEVEL_WORDS = ["Default", "Achieved", "Typical", "Actual"]
TARGET_EXEMPT = {"Target Material", "Target Feature(s)", "Target Selection Criteria"}

# Unit-only parentheticals: the unit belongs in Column E, not the field name.
# "(s)" is excluded — it is the pervasive English plural convention
# ("Procedure Reference(s)", "Coupled Technique(s)"), not seconds.
UNIT_PAREN_RE = re.compile(
    r"\((?:"
    r"W|V|A|ns|fs|ps|ms|µs|us|Hz|kHz|MHz|K|°C|"
    r"µm|um|nm|mm|cm|m|Å|"
    r"g|mg|µg|ug|ng|pg|kg|"
    r"%|ppm|ppb|Ma|Ga|ka|yr|a|"
    r"L\s*min[⁻\-]?1|mL/min|L/min|mL\s*min[⁻\-]?1|"
    r"cm2|cm²|cm-2|cm⁻²|"
    r"nmol|mol|ncc|"
    r"[a-zA-Zµ°]{1,6}\s*[⁻\-]\s*\d"
    r")\)",
    re.IGNORECASE,
)

# Column B describes the FIELD. Text describing what a source paper happens to contain
# is literature-assessment commentary and belongs in a literature assessment column, not
# in the description. This pattern nearly caused a bad reconciliation call on 2026-08-08:
# two candidate descriptions looked longer and better, but the extra length was entirely
# provenance notes about Horstwood's Table 3.
#
# Deliberately narrow. A citation that attributes a METHOD ("following Mattinson, 2005")
# is legitimate and must not be flagged; only text describing a source document is.
DESC_LEAK_RE = re.compile(
    r"(?:"
    r"\bTable\s+\d|\bFigure\s+\d|\bFig\.\s*\d|"
    r"in the source(?:\s+\w+)?|"
    r"not (?:explicitly )?stated (?:for|in|by)|"
    r"as (?:described|listed|reported|given) in Table|"
    r"the (?:paper|source|reference)'s own"
    r")", re.IGNORECASE)

# --------------------------------------------------------------------------- #
# Rule 7 — Keyed By vocabulary
# --------------------------------------------------------------------------- #
KEY_ANCHORS = {"sampling unit", "reported property", "channel", "analyte"}
KEY_SECONDARY = {"standard", "conversion", "model component", "acquisition pass",
                 "preparation step", "background position"}
KEY_VOCAB = KEY_ANCHORS | KEY_SECONDARY
KEY_FORBIDDEN = {"mode"}          # carried by the mode flag columns (Rule 3)

# Technique-dependent key register (Rule 7.8.7). A field name normally carries the
# same Keyed By in every TAPP; these are the ones where the technique genuinely makes
# it differ. Each entry must carry a recorded rationale in precedents.md. Extend only
# by explicit decision — and only when the divergence is real, not anticipated.
KEYED_BY_TECHNIQUE_DEPENDENT = {
    "Detection Limit":                   "per spot in LA, per session in solution",
    "Primary Calibration Standard Name": "analyte in EPMA/SEM, reported property in isotope work",
    "Dwell Time per Pixel":              "analyte only where compositional mapping exists",
    "Beam Current":                      "per phase where composition is measured, scalar in imaging-only TAPPs",
    "Monitored Isotopes":                "defines: channel where there is no collector array; analyte where the cup array defines the channel",
}
KEYED_BY_EXCEPTIONS = set(KEYED_BY_TECHNIQUE_DEPENDENT)   # back-compat alias

# Compound-key separators. The cross-product `x` must be whitespace-delimited: with
# `\s*` it would split inside any key name containing an x ("flux" -> ["flu", ""]).
# No current key does, but a technique-specific one could, and it would fail silently.
KEY_SPLIT_RE = re.compile(r"\s*>\s*|\s+x\s+")

# Rules 8 and 9 — mandatory in every TAPP. Rule 10 is restricted in scope and is
# declared per TAPP in Phase 0, so its presence is not machine-enforced; when it is
# present its Keyed By is checked like any other field.
RULE8_FIELD = "Reported Variables and Units"
RULE9_FIELD = "Sampling Unit"
RULE11_FIELD = "Additional Notes"   # last field of the whole TAPP (Rule 11)


def parse_keyed_by(v):
    """Return (kind, [component keys]); kind in {none, defines, pair, plain}."""
    v = (v or "").strip()
    if v in ("(none)", ""):
        return "none", []
    m = re.match(r"^(defines|pair):\s*(.+)$", v)
    if m:
        return m.group(1), [x.strip() for x in KEY_SPLIT_RE.split(m.group(2)) if x.strip()]
    return "plain", [x.strip() for x in KEY_SPLIT_RE.split(v) if x.strip()]


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CONTROLLED_LIST_REQUIRED = ["N/A", "None", "Other: specify"]

# Controlled list fields exempt from the N/A | None | Other: specify requirement,
# because another rule binds their allowed values to an exact closed set.
# See the exemption table in the Data Type Vocabulary section of conventions.md.
# Closed list — extend only by explicit decision, documented there.
CONTROLLED_LIST_EXEMPT = {"Analytical Mode", "Technique"}


def _span(nums, limit=6):
    """Compact a row-number list for display: [2,3,4,9] -> '2-4, 9'."""
    if not nums:
        return ""
    runs, start, prev = [], nums[0], nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        runs.append((start, prev))
        start = prev = n
    runs.append((start, prev))
    parts = [str(a) if a == b else f"{a}-{b}" for a, b in runs]
    if len(parts) > limit:
        return ", ".join(parts[:limit]) + f", … (+{len(parts) - limit} more)"
    return ", ".join(parts)


class Finding:
    __slots__ = ("severity", "tapp", "row", "field", "check", "message")

    def __init__(self, severity, tapp, row, field, check, message):
        self.severity = severity
        self.tapp = tapp
        self.row = row
        self.field = field
        self.check = check
        self.message = message

    def as_tuple(self):
        return (self.severity, self.tapp, self.row, self.field, self.check, self.message)


class Tapp:
    """A parsed TAPP CSV."""

    def __init__(self, path, rows):
        self.path = path
        self.name = os.path.basename(path)
        self.rows = rows
        self.header = rows[0] if rows else []
        self.sentinel_idx = self._find_sentinel()
        self.mode_cols = (
            self.header[FIRST_MODE_COL:self.sentinel_idx]
            if self.sentinel_idx is not None
            else []
        )

    def _find_sentinel(self):
        for i, h in enumerate(self.header):
            if h.strip() == SENTINEL_HEADER:
                return i
        return None

    def cell(self, row, idx):
        return row[idx].strip() if idx < len(row) else ""

    def is_group_header(self, row):
        a = self.cell(row, COL_ITEM)
        return bool(a) and bool(re.match(r"^\d+\.\s", a))

    def is_separator(self, row):
        """A separator row has no Metadata Item.

        Separator rows in several TAPPs carry stray N values in the mode and
        literature-assessment columns, so emptiness is judged on columns A-H only.
        """
        return not any(self.cell(row, i) for i in range(COL_ITEM, COL_UPDATE + 1))

    def content_rows(self):
        """Yield (row_number_1_indexed, row, current_group) for content rows only."""
        group = None
        for n, row in enumerate(self.rows[1:], start=2):
            if self.is_separator(row):
                continue
            if self.is_group_header(row):
                group = self.cell(row, COL_ITEM)
                continue
            yield n, row, group


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_structure(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))

    if t.sentinel_idx is None:
        add("WARN", 1, "", "sentinel-column",
            f"No column headed '{SENTINEL_HEADER}'. Mode/literature boundary cannot be "
            f"determined reliably; export falls back to a length heuristic.")
    else:
        stray_n = []
        for n, row in enumerate(t.rows[1:], start=2):
            if t.is_separator(row):
                continue
            v = t.cell(row, t.sentinel_idx)
            item = t.cell(row, COL_ITEM)
            if t.is_group_header(row):
                if v != "N":
                    add("WARN", n, item, "sentinel-group-header",
                        f"Group header should have N in the sentinel column, found '{v or 'empty'}'.")
            elif v == "N":
                # Widespread convention drift: sentinel treated as another mode column.
                stray_n.append(n)
            elif v:
                add("ERROR", n, item, "sentinel-nonempty",
                    f"Sentinel column must be empty on data rows, found '{v}'. "
                    f"This shifts the mode/literature boundary for any consumer that reads it.")
        if stray_n:
            add("WARN", stray_n[0], "", "sentinel-stray-N",
                f"{len(stray_n)} data row(s) carry 'N' in the sentinel column "
                f"(rows {_span(stray_n)}); conventions require data rows to be empty. "
                f"Harmless to the current export script, but it makes the column "
                f"indistinguishable from a mode flag.")

    # Group presence and order
    found = [t.cell(r, COL_ITEM) for r in t.rows[1:] if t.is_group_header(r)]
    if found != EXPECTED_GROUPS:
        missing = [g for g in EXPECTED_GROUPS if g not in found]
        extra = [g for g in found if g not in EXPECTED_GROUPS]
        detail = []
        if missing:
            detail.append(f"missing {missing}")
        if extra:
            detail.append(f"unexpected {extra}")
        if not detail:
            detail.append(f"out of order: {found}")
        add("ERROR", 1, "", "group-structure",
            "Six-group structure violated: " + "; ".join(detail))

    # Consecutive separator rows
    blanks = 0
    for n, row in enumerate(t.rows[1:], start=2):
        if t.is_separator(row):
            blanks += 1
            if blanks == 2:
                add("WARN", n, "", "blank-rows",
                    "More than one consecutive blank row; conventions allow exactly one between groups.")
        else:
            blanks = 0

    # Duplicate field names within this TAPP
    seen = defaultdict(list)
    for n, row, _ in t.content_rows():
        seen[t.cell(row, COL_ITEM)].append(n)
    for name, lines in seen.items():
        if len(lines) > 1:
            add("ERROR", lines[0], name, "duplicate-field",
                f"Field name appears {len(lines)} times (rows {lines}).")


def check_tiers(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))
    for n, row, _ in t.content_rows():
        item = t.cell(row, COL_ITEM)
        c, d = t.cell(row, COL_C), t.cell(row, COL_D)

        if not c:
            add("ERROR", n, item, "tier-missing", "Procedure-Level Tier (column C) is empty.")
        elif c not in VALID_C:
            add("ERROR", n, item, "tier-invalid",
                f"Procedure-Level Tier '{c}' is not one of {sorted(VALID_C)}.")

        if not d:
            add("ERROR", n, item, "tier-missing", "Analysis-Level Tier (column D) is empty.")
        elif d == "N/A":
            add("ERROR", n, item, "tier-d-na",
                "D=N/A is not a valid analysis-level tier. Use Read-Only for procedure-only fields.")
        elif d not in VALID_D:
            add("ERROR", n, item, "tier-invalid",
                f"Analysis-Level Tier '{d}' is not one of {sorted(VALID_D)}.")

        if d in ("Read-Only", "Editable") and c == "N/A":
            add("ERROR", n, item, "tier-inconsistent",
                f"D={d} requires a procedure-level value, but C=N/A. "
                f"{d} means 'imported from the procedure' — there is nothing to import.")


def check_modes(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))
    if t.sentinel_idx is None or not t.mode_cols:
        return
    span = range(FIRST_MODE_COL, t.sentinel_idx)
    for n, row in enumerate(t.rows[1:], start=2):
        if t.is_separator(row):
            continue
        item = t.cell(row, COL_ITEM)
        header_row = t.is_group_header(row)
        for i in span:
            v = t.cell(row, i)
            label = t.header[i] if i < len(t.header) else f"col{i}"
            if header_row:
                if v != "N":
                    add("WARN", n, item, "mode-flag-group-header",
                        f"Group header should have N in mode column '{label}', "
                        f"found '{v or 'empty'}'. Cosmetic: an empty flag is not Y, so the "
                        f"header still stays out of mode-filtered views.")
            elif v not in VALID_MODE_FLAG:
                add("ERROR", n, item, "mode-flag-invalid",
                    f"Mode column '{label}' has '{v or 'empty'}'; only Y or N are valid. "
                    f"Applicability of this field to this mode is undefined.")

    # A field applicable to no mode at all is almost certainly an error
    for n, row, _ in t.content_rows():
        flags = [t.cell(row, i) for i in span]
        if flags and all(f == "N" for f in flags):
            add("WARN", n, t.cell(row, COL_ITEM), "mode-all-N",
                "Field is flagged N for every mode; it will not appear in any mode-filtered view.")


def check_data_types(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))
    for n, row, _ in t.content_rows():
        item = t.cell(row, COL_ITEM)
        dt = t.cell(row, COL_TYPE)
        if not dt:
            add("WARN", n, item, "datatype-missing", "Data Type (column E) is empty.")
            continue
        if (dt not in VALID_DATA_TYPES and not NUMERIC_UNIT_RE.match(dt)
                and not COMPOUND_RE.match(dt)):
            syn = DATATYPE_SYNONYMS.get(dt.lower())
            mal = MALFORMED_COMPOUND.get(dt.lower())
            if syn:
                add("WARN", n, item, "datatype-synonym",
                    f"Data Type '{dt}' is a drifted spelling of '{syn}'. Use '{syn}'.")
            elif mal:
                add("WARN", n, item, "datatype-malformed-compound",
                    f"Data Type '{dt}' is not a well-formed compound. Use '{mal}'. "
                    f"See 'Compound data types' in conventions.md.")
            else:
                add("WARN", n, item, "datatype-invalid",
                    f"Data Type '{dt}' is not in the controlled vocabulary.")
        if dt.startswith("Controlled list") and item not in CONTROLLED_LIST_EXEMPT:
            # A compound's "/ Text" component already permits an unlisted answer, so
            # "Other: specify" is not required there — only the absence values are.
            required = (CONTROLLED_LIST_REQUIRED if dt == "Controlled list"
                        else [v for v in CONTROLLED_LIST_REQUIRED if v != "Other: specify"])
            ex = t.cell(row, COL_EXAMPLE)
            missing = [v for v in required if v.lower() not in ex.lower()]
            if missing:
                add("WARN", n, item, "controlled-list-options",
                    f"Controlled list is missing required option(s) {missing} in column F.")


def check_naming(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))
    for n, row, _ in t.content_rows():
        item = t.cell(row, COL_ITEM)
        low = item.lower().strip()

        if low in FORBIDDEN_NAMES:
            add("WARN", n, item, "name-forbidden",
                f"Rule 1: use '{FORBIDDEN_NAMES[low]}' instead of '{item}'.")

        for w in LEVEL_WORDS:
            if re.search(rf"\b{w}\b", item):
                add("WARN", n, item, "name-level-encoding",
                    f"Field name contains '{w}'. Names must be level-neutral; "
                    f"the C/D columns encode level.")
                break

        if re.search(r"\bTarget\b", item) and item not in TARGET_EXEMPT:
            add("WARN", n, item, "name-level-encoding",
                "Field name contains 'Target'. Only 'Target Material' and "
                "'Target Feature(s)' are exempt from the level-neutral naming rule.")

        m = UNIT_PAREN_RE.search(item)
        if m:
            add("WARN", n, item, "name-unit-in-name",
                f"Field name embeds a unit '{m.group(0)}'. Units belong in Column E "
                f"(Data Type), e.g. 'Numeric (W)'.")

        if "element-specific" in low:
            add("WARN", n, item, "name-element-specific",
                "Use 'Analyte-Specific' rather than 'Element-Specific' (technique-agnostic).")

    # Column B describes the field, not the source paper
    for n, row, _ in t.content_rows():
        m = DESC_LEAK_RE.search(t.cell(row, COL_DESC))
        if m:
            add("WARN", n, t.cell(row, COL_ITEM), "description-source-leak",
                f"Description contains literature-assessment commentary ({m.group(0)!r}) — text about "
                f"what a source document contains belongs in a literature assessment column, not in "
                f"Column B. It also inflates the description, which can bias a reconciliation that "
                f"treats length as a quality signal.")

    # Column G should carry the Analyte-Specific label, not columns B or F
    for n, row, _ in t.content_rows():
        for col, letter in ((COL_DESC, "B"), (COL_EXAMPLE, "F")):
            if "element-specific" in t.cell(row, col).lower():
                add("WARN", n, t.cell(row, COL_ITEM), "name-element-specific",
                    f"Column {letter} uses 'Element-Specific'; the correct term is 'Analyte-Specific'.")


def check_rules(t: Tapp, out):
    """Rules 1, 3 and 5, plus the Group 1 coupling-field block."""
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))

    by_group = defaultdict(list)
    for n, row, group in t.content_rows():
        by_group[group].append((n, t.cell(row, COL_ITEM), t.cell(row, COL_C), t.cell(row, COL_D),
                                t.cell(row, COL_TYPE)))

    # Required tiers for named cross-TAPP fields
    for n, row, _ in t.content_rows():
        item = t.cell(row, COL_ITEM)
        if item in REQUIRED_TIERS:
            want_c, want_d = REQUIRED_TIERS[item]
            got_c, got_d = t.cell(row, COL_C), t.cell(row, COL_D)
            if (got_c, got_d) != (want_c, want_d):
                add("WARN", n, item, "rule-tier",
                    f"Expected C={want_c}, D={want_d}; found C={got_c}, D={got_d}.")

    # Rule 3 — Analytical Mode is the first field in Group 4
    g4 = by_group.get("4. Measurement Information", [])
    if not g4:
        add("ERROR", 1, "", "rule3", "Group 4 has no content rows.")
    elif g4[0][1] != "Analytical Mode":
        present = any(f[1] == "Analytical Mode" for f in g4)
        add("WARN", g4[0][0], g4[0][1], "rule3",
            f"Rule 3: 'Analytical Mode' must be the FIRST field in Group 4; "
            f"found '{g4[0][1]}'." + ("" if present else " Field is absent entirely."))

    # Rule 5 — Constants and Reference Values Used is the last field in Group 5
    g5 = by_group.get("5. Data Processing", [])
    if not g5:
        add("ERROR", 1, "", "rule5", "Group 5 has no content rows.")
    elif g5[-1][1] != "Constants and Reference Values Used":
        present = any(f[1] == "Constants and Reference Values Used" for f in g5)
        add("WARN", g5[-1][0], g5[-1][1], "rule5",
            f"Rule 5: 'Constants and Reference Values Used' must be the LAST field in Group 5; "
            f"found '{g5[-1][1]}'." + ("" if present else " Field is absent entirely."))

    # Group 1 must end with the four coupling fields, in order
    g1 = [f[1] for f in by_group.get("1. Procedure Identification", [])]
    if g1[-4:] != COUPLING_FIELDS:
        add("WARN", 1, "", "group1-coupling",
            f"Group 1 must end with {COUPLING_FIELDS} in that order; found {g1[-4:]}.")

    # Rule 5 / Rule 3 mode flags must be Y for every mode
    if t.sentinel_idx is not None and t.mode_cols:
        span = range(FIRST_MODE_COL, t.sentinel_idx)
        for n, row, _ in t.content_rows():
            item = t.cell(row, COL_ITEM)
            if item in ("Analytical Mode", "Constants and Reference Values Used"):
                flags = [t.cell(row, i) for i in span]
                if any(f != "Y" for f in flags):
                    add("WARN", n, item, "rule-mode-flags",
                        f"Must be Y for all modes (universal field); found {flags}.")


def check_keyed_by(t: Tapp, out):
    """Rule 7 — every field declares what its value repeats over."""
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))

    if t.header[COL_KEYEDBY].strip() != "Keyed By":
        add("ERROR", 1, "", "rule7-column",
            f"Column I must be headed 'Keyed By'; found "
            f"'{t.header[COL_KEYEDBY].strip()}'.")
        return

    used, defined, names = set(), __import__('collections').defaultdict(list), set()
    for n, row, _ in t.content_rows():
        item = t.cell(row, COL_ITEM)
        names.add(item)
        raw = t.cell(row, COL_KEYEDBY)

        if not raw.strip():
            add("ERROR", n, item, "rule7-blank",
                "Keyed By is blank. Every content row must declare a key, "
                "or '(none)' for a scalar field.")
            continue

        kind, parts = parse_keyed_by(raw)
        for k in parts:
            if k in KEY_FORBIDDEN:
                add("ERROR", n, item, "rule7-forbidden-key",
                    f"'{k}' is not a valid key — mode applicability is carried by "
                    f"the mode flag columns (Rule 3).")
            elif k not in KEY_VOCAB:
                add("WARN", n, item, "rule7-unknown-key",
                    f"'{k}' is not in the Rule 7 vocabulary. Declare technique-specific "
                    f"keys in Phase 0 and list them in the Legends sheet.")
        if kind == "defines":
            for k in parts: defined[k].append(item)
        else:
            used.update(parts)

    # Invariant 4 — EVERY key in use must have its domain enumerated somewhere.
    # Applies to secondary keys as well as anchors: a key whose domain is never
    # enumerated cannot be populated, whichever key it is.
    for k in sorted(used - set(defined)):
        add("ERROR", 1, "", "rule7-undefined-domain",
            f"Key '{k}' is used but no field declares 'defines: {k}'. A key whose "
            f"domain is never enumerated cannot be populated.")

    # Invariant 4b — exactly one definer per key. Two fields both claiming to
    # enumerate a domain leaves a consumer no way to know which builds the child table.
    for k, fields in sorted(defined.items()):
        if len(fields) > 1:
            add("ERROR", 1, fields[0], "rule7-multiple-definers",
                f"{len(fields)} fields declare 'defines: {k}' ({', '.join(fields)}). "
                f"Exactly one field may enumerate a key's domain; the others should be "
                f"keyed by it.")

    # Invariant 4c — a definer needs a consumer. 'defines: X' where nothing is keyed
    # by X declares a domain no field repeats over, which is a list, not a key.
    for k, fields in sorted(defined.items()):
        # Rules 8 and 9 make these mandatory for their own sake — Reported Variables and
        # Units declares the procedure's scope boundary, Sampling Unit declares the unit a
        # reported row corresponds to. Their definer role is secondary, so a TAPP with no
        # field keyed off them is not in error.
        if k not in used and not set(fields) & {RULE8_FIELD, RULE9_FIELD}:
            add("WARN", 1, fields[0], "rule7-unused-definer",
                f"'{fields[0]}' declares 'defines: {k}' but no field in this TAPP is "
                f"keyed by '{k}'. A field that merely holds a list is not a definer — "
                f"use '(none)'.")

    # Rules 8, 9 and 11 — mandatory fields.
    for fld, rule in ((RULE8_FIELD, "rule8"), (RULE9_FIELD, "rule9"), (RULE11_FIELD, "rule11")):
        if fld not in names:
            add("ERROR", 1, fld, rule, f"'{fld}' is mandatory in every TAPP.")

    # Rule 11 — Additional Notes is the LAST field of the whole TAPP, not merely the
    # last field of Group 6. Its scope is the document, and position is what says so.
    content = [t.cell(row, COL_ITEM) for _, row, _ in t.content_rows()]
    if content and RULE11_FIELD in content and content[-1] != RULE11_FIELD:
        add("ERROR", 1, content[-1], "rule11",
            f"Rule 11: '{RULE11_FIELD}' must be the last field of the TAPP; "
            f"found '{content[-1]}' after it.")

    # Comments must no longer duplicate mode applicability (Rule 7.6).
    modes = [h.strip() for h in t.header[FIRST_MODE_COL:t.sentinel_idx]]
    for n, row, _ in t.content_rows():
        c = t.cell(row, COL_COMMENT)
        if not c.strip():
            continue
        for mh in modes:
            if mh and mh.lower() in c.lower():
                add("WARN", n, t.cell(row, COL_ITEM), "rule7-comment-mode",
                    f"Comments names mode '{mh}', which the mode flag columns already "
                    f"carry. Remove it (Rule 7.6).")
                break


def check_dates(t: Tapp, out):
    add = lambda s, r, f, c, m: out.append(Finding(s, t.name, r, f, c, m))
    for n, row, _ in t.content_rows():
        v = t.cell(row, COL_UPDATE)
        if not v:
            add("INFO", n, t.cell(row, COL_ITEM), "date-missing",
                "Last Update (column H) is empty.")
        elif not DATE_RE.match(v):
            add("WARN", n, t.cell(row, COL_ITEM), "date-format",
                f"Last Update '{v}' is not YYYY-MM-DD.")


# ---------------------------------------------------------------------------
# Cross-TAPP checks
# ---------------------------------------------------------------------------

def normalize_name(s: str) -> str:
    """Collapse cosmetic differences so near-duplicates group together."""
    s = s.lower().strip()
    s = re.sub(r"\s*([/(),;:-])\s*", r"\1", s)   # spaces around punctuation
    s = re.sub(r"\s+", " ", s)
    return s


def check_cross_tapp(tapps, out):
    add = lambda s, tp, f, c, m: out.append(Finding(s, tp, "", f, c, m))

    variants = defaultdict(set)          # normalized -> {(tapp, raw_name)}
    tiers = defaultdict(set)             # raw name -> {(tapp, C, D)}

    for t in tapps:
        for _, row, _ in t.content_rows():
            raw = t.cell(row, COL_ITEM)
            variants[normalize_name(raw)].add((t.name, raw))
            tiers[raw].add((t.name, t.cell(row, COL_C), t.cell(row, COL_D)))

    # Near-duplicate spellings of the same field across TAPPs
    for _, entries in sorted(variants.items()):
        spellings = {raw for _, raw in entries}
        if len(spellings) > 1:
            detail = "; ".join(f"{tp}: '{raw}'" for tp, raw in sorted(entries))
            add("WARN", "(cross-TAPP)", sorted(spellings)[0], "name-variant",
                f"Same field spelled {len(spellings)} ways — {detail}. "
                f"Rule 1 requires identical names across TAPPs.")

    # Same field name, different tiers
    for raw, entries in sorted(tiers.items()):
        combos = {(c, d) for _, c, d in entries}
        if len(combos) > 1 and len(entries) > 1:
            detail = "; ".join(f"{tp}: C={c},D={d}" for tp, c, d in sorted(entries))
            add("INFO", "(cross-TAPP)", raw, "tier-divergence",
                f"Tier assignment differs across {len(entries)} TAPPs — {detail}. "
                f"Intentional divergence must be recorded in precedents.md (Rule 2/4).")


def check_group1_template(tapps, template_path, out):
    """Compare each TAPP's Group 1 against the canonical template (Rule 1)."""
    if not os.path.exists(template_path):
        out.append(Finding("WARN", "(template)", "", "", "group1-template",
                           f"Template not found at {template_path}; Group 1 comparison skipped."))
        return

    with open(template_path, newline="", encoding="utf-8-sig") as f:
        trows = list(csv.reader(f))

    tmpl = {}
    order = []
    for r in trows[1:]:
        a = r[0].strip() if r else ""
        if not a or re.match(r"^\d+\.\s", a):
            continue
        tmpl[a] = (r[COL_DESC].strip(), r[COL_C].strip(), r[COL_D].strip(), r[COL_TYPE].strip())
        order.append(a)

    for t in tapps:
        g1 = [(n, t.cell(row, COL_ITEM), t.cell(row, COL_DESC), t.cell(row, COL_C),
               t.cell(row, COL_D), t.cell(row, COL_TYPE))
              for n, row, g in t.content_rows() if g == "1. Procedure Identification"]
        names = [f[1] for f in g1]

        for missing in [k for k in order if k not in names]:
            out.append(Finding("WARN", t.name, "", missing, "group1-missing",
                               "Group 1 field present in the template is missing from this TAPP."))
        for extra in [k for k in names if k not in tmpl]:
            out.append(Finding("INFO", t.name, "", extra, "group1-extra",
                               "Group 1 field is not in the template."))

        if names and [k for k in names if k in tmpl] != [k for k in order if k in names]:
            out.append(Finding("WARN", t.name, "", "", "group1-order",
                               "Group 1 field order differs from the template."))

        for n, name, desc, c, d, dtype in g1:
            if name not in tmpl:
                continue
            t_desc, t_c, t_d, t_type = tmpl[name]
            if (c, d) != (t_c, t_d):
                out.append(Finding("WARN", t.name, n, name, "group1-tier",
                                   f"Tier differs from template: TAPP C={c},D={d} vs "
                                   f"template C={t_c},D={t_d}."))
            if t_type and dtype != t_type:
                out.append(Finding("WARN", t.name, n, name, "group1-datatype",
                                   f"Data Type differs from template: '{dtype}' vs '{t_type}'."))
            if t_desc and desc != t_desc:
                out.append(Finding("INFO", t.name, n, name, "group1-description",
                                   "Description differs from the template. Column B is "
                                   "template-owned; only Column F is technique-specific."))


# ---------------------------------------------------------------------------
# Discovery and reporting
# ---------------------------------------------------------------------------

def _excluded(dirname):
    """Directories whose TAPPs are not part of the live library.

    Pattern-based rather than a fixed list, so archiving a TAPP is a matter of moving it
    into a folder named Superseded/Archive rather than also editing this script.
    """
    if dirname.startswith("."):
        return True
    low = dirname.lower()
    return (dirname == "unpacked_tapp"
            or low.startswith("superseded")
            or "archive" in low)


def version_of(path):
    m = re.search(r"_v(\d+(?:\.\d+)?)\.csv$", os.path.basename(path))
    return float(m.group(1)) if m else -1.0


def discover(root, all_versions=False):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not _excluded(d)]
        for fn in filenames:
            if re.search(r"_TAPP_v\d+(\.\d+)?\.csv$", fn):
                found.append(os.path.join(dirpath, fn))
    if all_versions:
        return sorted(found)
    latest = {}
    for p in found:
        key = os.path.basename(p).rsplit("_v", 1)[0]
        if key not in latest or version_of(p) > version_of(latest[key]):
            latest[key] = p
    return [latest[k] for k in sorted(latest)]


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return Tapp(path, list(csv.reader(f)))


SEV_ORDER = {"ERROR": 0, "WARN": 1, "INFO": 2}


def collapse(findings, threshold=5):
    """Fold repetitive (tapp, check) groups into one summary finding.

    A check that fires on 80 rows of one file is one problem, not eighty.
    """
    groups = defaultdict(list)
    for f in findings:
        groups[(f.tapp, f.check, f.severity)].append(f)

    out = []
    for (tapp, check, sev), fs in groups.items():
        if len(fs) < threshold:
            out.extend(fs)
            continue
        rows = sorted(int(f.row) for f in fs if str(f.row).isdigit())
        fields = sorted({f.field for f in fs if f.field})
        shown = ", ".join(fields[:4]) + (f", … (+{len(fields) - 4} more)" if len(fields) > 4 else "")
        out.append(Finding(
            sev, tapp, rows[0] if rows else "", f"[{len(fs)} occurrences]", check,
            f"{fs[0].message} — affects {len(fs)} rows"
            + (f" ({_span(rows)})" if rows else "")
            + (f"; fields: {shown}" if fields else "")))
    return out


def report(findings, min_severity, out=sys.stdout, do_collapse=True):
    threshold = SEV_ORDER[min_severity]
    shown = [f for f in findings if SEV_ORDER[f.severity] <= threshold]
    if do_collapse:
        shown = collapse(shown)

    by_tapp = defaultdict(list)
    for f in shown:
        by_tapp[f.tapp].append(f)

    for tapp in sorted(by_tapp):
        fs = sorted(by_tapp[tapp], key=lambda x: (SEV_ORDER[x.severity], str(x.row), x.check))
        counts = defaultdict(int)
        for f in fs:
            counts[f.severity] += 1
        summary = "  ".join(f"{s}:{counts[s]}" for s in ("ERROR", "WARN", "INFO") if counts[s])
        print(f"\n{'=' * 100}", file=out)
        print(f"{tapp}   [{summary}]", file=out)
        print("=" * 100, file=out)
        for f in fs:
            loc = f"row {f.row}" if f.row else "—"
            head = f"  {f.severity:<5} {loc:<9} {f.check:<24}"
            print(f"{head} {f.field}", file=out)
            print(f"{' ' * len(head)} {f.message}", file=out)

    total = defaultdict(int)
    for f in findings:
        total[f.severity] += 1
    print(f"\n{'=' * 100}", file=out)
    print("SUMMARY", file=out)
    print("=" * 100, file=out)
    for s in ("ERROR", "WARN", "INFO"):
        print(f"  {s:<6} {total[s]}", file=out)
    print(f"  {'TOTAL':<6} {sum(total.values())}", file=out)

    by_check = defaultdict(int)
    for f in findings:
        if SEV_ORDER[f.severity] <= threshold:
            by_check[(f.severity, f.check)] += 1
    if by_check:
        print("\n  By check:", file=out)
        for (sev, check), n in sorted(by_check.items(), key=lambda x: (-x[1], x[0])):
            print(f"    {sev:<5} {check:<26} {n}", file=out)


def main():
    ap = argparse.ArgumentParser(description="Lint TAPP CSVs against conventions.md.")
    default_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    ap.add_argument("--root", default=default_root, help="TAPP library root directory")
    ap.add_argument("--file", action="append", help="Lint specific file(s) instead of discovering")
    ap.add_argument("--all-versions", action="store_true", help="Include superseded versions")
    ap.add_argument("--severity", choices=["ERROR", "WARN", "INFO"], default="INFO",
                    help="Minimum severity to display (default: INFO)")
    ap.add_argument("--csv", help="Also write findings to this CSV path")
    ap.add_argument("--no-cross", action="store_true", help="Skip cross-TAPP checks")
    ap.add_argument("--no-collapse", action="store_true",
                    help="List every occurrence instead of folding repetitive checks")
    args = ap.parse_args()

    if args.file:
        paths = [p if os.path.isabs(p) else os.path.join(args.root, p) for p in args.file]
    else:
        paths = discover(args.root, args.all_versions)

    if not paths:
        print(f"No TAPP CSVs found under {args.root}", file=sys.stderr)
        return 2

    tapps, findings = [], []
    for p in paths:
        try:
            t = load(p)
        except Exception as e:  # noqa: BLE001 - surface parse failures as findings
            findings.append(Finding("ERROR", os.path.basename(p), "", "", "unreadable", str(e)))
            continue
        tapps.append(t)
        for check in (check_structure, check_tiers, check_modes, check_data_types,
                      check_naming, check_rules, check_keyed_by, check_dates):
            check(t, findings)

    if not args.no_cross and len(tapps) > 1:
        check_cross_tapp(tapps, findings)
        # Group 1 is composed from Module_Group1 (Rule 6); that module is the source
        # of truth. The pre-migration template is only a fallback for libraries that
        # have not yet migrated.
        module_g1 = os.path.join(args.root, "Claude Skills for TAPP", "modules",
                                 "Module_Group1.csv")
        legacy_g1 = os.path.join(args.root, "Claude Skills for TAPP", "tapp_files",
                                 "Template TAPP Group 1.csv")
        check_group1_template(
            tapps,
            module_g1 if os.path.exists(module_g1) else legacy_g1,
            findings,
        )

    print(f"Linted {len(tapps)} TAPP file(s) under {args.root}")
    report(findings, args.severity, do_collapse=not args.no_collapse)

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["Severity", "TAPP", "Row", "Field", "Check", "Message"])
            w.writerows(f_.as_tuple() for f_ in sorted(
                findings, key=lambda x: (SEV_ORDER[x.severity], x.tapp, str(x.row))))
        print(f"\nFindings written to {args.csv}")

    return 1 if any(f.severity == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
