#!/usr/bin/env python
"""Can a dataset's FILE KINDS determine its `ada:analyticalMode`? Measure it, per technique.

PROTOTYPE / REPORT ONLY. Writes nothing, changes no schema. It answers one question: for each
technique, which of its declared analytical modes could be read off the `ada:componentType` values
of the files in a distribution, and which could not.

Why this exists. The TAPP workbooks gate 213 field requirements on the analytical mode, and no ADA
record carries one -- 0 of 7,447, with no source field anywhere in 111,963 `record_subjects` (see
docs/ANALYTICAL_MODE.md). So a mode would have to be DERIVED. The only
record-side evidence with any discriminating power is the kind of file delivered, which ADA does
record as `ada:componentType`.

THE METHOD, AND ITS LIMIT. A mode name and a componentType name are both decomposed on two axes:

    DETECTOR   EDS, WDS, EELS, CL, SE, BSE      what measured the signal
    GEOMETRY   point, map, transect, image, ... how the measurement was laid out over the sample

A componentType WITNESSES a mode when neither axis contradicts, and at least one axis actually
matched. `ada:SEMEDSMap` witnesses `EDS Mapping` on both axes; `ada:EPMAImageMap` witnesses
`EDS Mapping` and `WDS Mapping` equally, because it carries no detector -- so it determines the
geometry and leaves the mode ambiguous.

**This is a heuristic over NAMES, not over file content.** It cannot see inside a file, and a
componentType whose name omits the detector is not evidence that no detector was used. Treat an
`UNREACHABLE` verdict as "the vocabulary cannot say", never as "the mode did not happen". The
report therefore separates three outcomes and never collapses them:

    DETERMINED    exactly one mode is witnessed -- a file kind that implies one mode
    AMBIGUOUS     several modes are witnessed -- narrows the answer without fixing it
    UNREACHABLE   no componentType witnesses the mode at all

Usage:
    python tools/infer_analytical_mode.py                 # per-technique table + summary
    python tools/infer_analytical_mode.py --technique semTAPP
    python tools/infer_analytical_mode.py --json          # machine-readable, for the ADA side
    python tools/infer_analytical_mode.py --vocab         # the axis tables, to review the heuristic
"""
import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b  # noqa: E402

# ---------------------------------------------------------------- the two axes
#
# Declared as DATA rather than buried in a regex, because the whole report is only as trustworthy
# as these tables and a reviewer has to be able to read them. Order matters within DETECTORS:
# "EELS" must be tested before "EDS" would match a substring, and "BSE" before "SE".
# ONE axis, not two. An earlier draft split "detector" (EDS/WDS/CL/SE/BSE) from the technique's own
# token, and that produced three wrong answers at once: `ada:EBSDMap` classified as detector-less,
# so it witnessed EDS Mapping, WDS Mapping and CL Mapping equally; `ada:SEMImage` likewise
# witnessed BSE Imaging; and the bare-acronym mode `EBSD` classified on NO axis, so it was reported
# UNREACHABLE while `ada:EBSDMap` sat in the same technique as its obvious witness. Collapsing both
# into SIGNAL -- "what produced this signal" -- fixes all three, because a signal mismatch then
# CONTRADICTS instead of being invisible.
#
# Tested in order: EELS before EDS, EBSD before BSE, STEM before TEM, BSE before SE.
SIGNALS = [
    ("EELS", r"EELS"),
    ("EBSD", r"EBSD"),
    ("WDS", r"WDS"),
    ("EDS", r"EDS|EDX"),
    ("HAADF", r"HAADF"),
    ("STEM", r"STEM"),
    ("BSE", r"BSE"),
    ("CL", r"\bCL|Cathodo"),
    # `ada:SEMImage` is read as a secondary-electron image. That is a CONVENTION of this
    # vocabulary, not something the name states -- it matters only because the same vocabulary
    # carries `ada:BSEImage` alongside it, so the unqualified form is the SE one by contrast.
    ("SE", r"\bSE\b|SEMImage|SecondaryElectron"),
    ("TEM", r"TEM"),
    ("CT", r"XCT|\bCT\b"),
]

# A mode and a componentType spell the same geometry differently -- a mode says "Point Analysis"
# where a componentType says "Tabular" or "PointData" -- so each vocabulary gets its own patterns.
# Keeping them separate is what stops a componentType's spelling being read as if the workbook had
# used it.
GEOMETRY_IN_MODE = [
    ("point", r"Point Analysis|Point spectrum|Spectral Point|\bSpot\b"),
    ("map", r"Mapping|Spectral Map"),
    ("transect", r"Transect"),
    ("image", r"Imaging|Overview Image|image stack|Reflectance imaging"),
    ("diffraction", r"[Dd]iffraction"),
    ("tomography", r"Tomography"),
    ("volume", r"Single-volume|Multi-volume"),
    ("flow", r"nebulisation|Flow injection"),
    # Sample preparation yields no analytical file, so nothing can witness it. Classified
    # explicitly so the verdict is UNREACHABLE for the right reason rather than because the
    # classifier found no axis.
    ("preparation", r"Sample Preparation"),
]
GEOMETRY_IN_COMPONENT = [
    ("point", r"PointData|Spectrum|Tabular|Plot|Point"),
    ("map", r"Map|Cube"),
    ("transect", r"Transect"),
    ("image", r"Image|Photography|QuickLook"),
    ("diffraction", r"DiffractionPattern|Diffractogram"),
    ("tomography", r"Tomo"),
    ("volume", r"Volume"),
]

# componentTypes that describe DELIVERY rather than measurement. They appear in nearly every
# technique and witness nothing: a report or a log file says nothing about how the sample was
# measured, and letting them match would manufacture evidence. docs/COMPONENTTYPE_VARIANTS.md records the same set as
# "live generic types ... they match everything and discriminate nothing" for profile selection.
NON_EVIDENTIAL = re.compile(
    r"methodDescription|report|logFile|analysisLocation|contextPhotography|quickLook"
    r"|instrumentMetadata|worldFile|calibrationFile|annotated|noComponentFiles"
    r"|supplementary|readme|checksum",
    re.I,
)


def _axis(text, table):
    for name, pattern in table:
        if re.search(pattern, text):
            return name
    return None


def classify_mode(mode):
    """(signal, geometry) a mode name asserts. Either may be None."""
    return _axis(mode, SIGNALS), _axis(mode, GEOMETRY_IN_MODE)


def classify_component(ct):
    """(signal, geometry) a componentType name carries. Either may be None."""
    return _axis(ct, SIGNALS), _axis(ct, GEOMETRY_IN_COMPONENT)


def witnesses(ct, mode):
    """True when `ct` is compatible with `mode` and actually says something about it.

    Compatible means neither axis CONTRADICTS. The second half is what stops a bare
    `ada:EPMAImage` witnessing every EPMA mode: a match on no axis at all is not evidence.
    """
    cs, cg = classify_component(ct)
    ms, mg = classify_mode(mode)
    # A signal the componentType names and the mode does not is a CONTRADICTION, not a silence:
    # an EBSD map is not evidence of CL mapping, however well the geometries agree. This is the
    # asymmetry the single-axis rewrite exists for, so it is deliberately stricter than the
    # geometry rule below.
    if cs and ms and cs != ms:
        return False
    if cs and not ms:
        return False
    if mg and cg and mg != cg:
        return False
    return bool((ms and cs == ms) or (mg and cg == mg))


def modes_for(tapp):
    """The technique's declared modes, from its workbook's `Analytical Mode` allowed-content cell.

    Returns (modes, notes). `notes` records cells this function had to clean, because a silently
    normalised oddity is one nobody fixes: four techniques quote their values and one joins two
    modes with a semicolon inside a single pipe-delimited field.
    """
    notes = []
    try:
        b.configure(tapp)
        rows = b.tapp_source.rows(b.XLSX)
    except Exception as exc:                      # a technique with no readable table
        return [], ["unreadable: %s: %s" % (type(exc).__name__, exc)]
    header = [b.norm(v) for v in rows[0]]
    try:
        col = header.index("Example / Allowed Content")
    except ValueError:
        return [], ["no 'Example / Allowed Content' column"]
    for row in rows[1:]:
        if b.norm(row[0]) != "Analytical Mode":
            continue
        raw = row[col] if col < len(row) else ""
        out = []
        for part in raw.split("|"):
            part = part.strip()
            if not part:
                continue
            if part != part.strip("'\""):
                notes.append("quoted value in the workbook cell: %r" % part)
                part = part.strip("'\"")
            if ";" in part:
                notes.append("semicolon-joined modes in one field: %r" % part)
                out.extend(p.strip() for p in part.split(";") if p.strip())
            else:
                out.append(part)
        return out, notes
    return [], ["no 'Analytical Mode' row"]


def mode_switches_schema(tapp):
    """(n_mode_columns, n_mixed_rows) -- does this technique's mode gate any field?

    THE FIRST QUESTION, ahead of determinability. A technique with no mode-flag columns between
    `Purpose` and `Literature Assessment` has nothing to switch: its `Analytical Mode` is
    INFORMATIONAL, reported on an analysis and affecting no constraint. Solution Q/SF/MC-ICP-MS are
    the clear case -- they declare `Solution nebulisation (continuous) | Flow injection` and no
    field's applicability varies between the two.

    Derived from `build_tapp.mode_columns()`, the same function the generator uses, rather than
    from a header pattern of this module's own. A hand-rolled header regex undercounted this:
    it reported 213 mixed rows across 11 workbooks where the authoritative answer is 284 across
    14 techniques, missing vnmirTAPP and semFibsemTAPP entirely.
    """
    try:
        b.configure(tapp)
        rows = b.tapp_source.rows(b.XLSX)
        cols = b.mode_columns(rows)
    except Exception:
        return 0, 0
    mixed = 0
    for row in rows[1:]:
        vals = [(b.norm(row[i]) if i < len(row) else "").upper() for i in cols]
        if any(v == "Y" for v in vals) and any(v == "N" for v in vals):
            mixed += 1
    return len(cols), mixed


def analyse(tapp):
    modes, notes = modes_for(tapp)
    n_cols, n_mixed = mode_switches_schema(tapp)
    cfg = b.TAPP_CONFIGS.get(tapp) or {}
    cts = list(cfg.get("component_types") or [])
    evidential = [c for c in cts if not NON_EVIDENTIAL.search(c)]
    by_mode = {m: sorted(c for c in evidential if witnesses(c, m)) for m in modes}
    # A componentType witnessing several modes narrows rather than decides; one witnessing exactly
    # one mode is the only case that can populate a value on its own.
    by_ct = collections.defaultdict(list)
    for m, wits in by_mode.items():
        for c in wits:
            by_ct[c].append(m)
    verdict = {}
    for m, wits in by_mode.items():
        if not wits:
            verdict[m] = "UNREACHABLE"
        elif any(len(by_ct[c]) == 1 for c in wits):
            verdict[m] = "DETERMINED"
        else:
            verdict[m] = "AMBIGUOUS"
    return {
        "tapp": tapp,
        "modes": modes,
        "component_types": cts,
        "evidential": evidential,
        "non_evidential": [c for c in cts if NON_EVIDENTIAL.search(c)],
        "witnesses": by_mode,
        "deciding": {c: ms for c, ms in sorted(by_ct.items()) if len(ms) == 1},
        "verdict": verdict,
        "notes": notes,
        "mode_columns": n_cols,
        "mixed_rows": n_mixed,
        # A mode that gates nothing does not need determining. Guessing one would still be a
        # factual claim about the acquisition, so the distinction is about whether the guess is
        # WORTH anything, not about whether it is safe.
        "affects_schema": n_cols > 0 and n_mixed > 0,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--technique", help="one TAPP key, e.g. semTAPP")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--vocab", action="store_true", help="print the axis tables and exit")
    args = ap.parse_args()

    if args.vocab:
        print("SIGNALS (tested in order):")
        for n, p in SIGNALS:
            print("  %-6s %s" % (n, p))
        print("\nGEOMETRY, as a MODE spells it:")
        for n, p in GEOMETRY_IN_MODE:
            print("  %-12s %s" % (n, p))
        print("\nGEOMETRY, as a componentType spells it:")
        for n, p in GEOMETRY_IN_COMPONENT:
            print("  %-12s %s" % (n, p))
        print("\nNON-EVIDENTIAL componentTypes:\n  %s" % NON_EVIDENTIAL.pattern)
        return 0

    keys = [args.technique] if args.technique else sorted(b.TAPP_CONFIGS)
    results = [analyse(k) for k in keys]
    results = [r for r in results if r["modes"]]

    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0

    tally = collections.Counter()
    tally_sw = collections.Counter()
    for r in results:
        print("=" * 78)
        gate = ("GATES %d field row(s) via %d mode column(s)" % (r["mixed_rows"], r["mode_columns"])
                if r["affects_schema"] else "INFORMATIONAL -- no mode columns, gates nothing")
        print("%s   %d mode(s), %d componentType(s) (%d evidential)"
              % (r["tapp"], len(r["modes"]), len(r["component_types"]), len(r["evidential"])))
        print("    %s" % gate)
        for m in r["modes"]:
            v = r["verdict"][m]
            tally[v] += 1
            if r["affects_schema"]:
                tally_sw[v] += 1
            wits = r["witnesses"][m]
            shown = ", ".join(wits[:3]) + (" …+%d" % (len(wits) - 3) if len(wits) > 3 else "")
            print("    %-12s %-28s %s" % (v, m[:28], shown or "-"))
        for n in r["notes"]:
            print("    note: %s" % n)

    print("=" * 78)
    sw = [r for r in results if r["affects_schema"]]
    tot_sw = sum(tally_sw.values())
    total = sum(tally.values())
    print("WHERE THE MODE GATES A FIELD -- the only population worth guessing for")
    print("  %d techniques, %d modes, %d gated field rows"
          % (len(sw), tot_sw, sum(r["mixed_rows"] for r in sw)))
    for v in ("DETERMINED", "AMBIGUOUS", "UNREACHABLE"):
        c = tally_sw[v]
        print("    %-12s %4d  %5.1f%%" % (v, c, (100.0 * c / tot_sw) if tot_sw else 0.0))
    print()
    print("ALL techniques, including those whose mode is informational")
    print("  %d techniques, %d modes" % (len(results), total))
    for v in ("DETERMINED", "AMBIGUOUS", "UNREACHABLE"):
        c = tally[v]
        print("    %-12s %4d  %5.1f%%" % (v, c, (100.0 * c / total) if total else 0.0))
    print()
    print("A technique with no mode-flag columns has nothing to switch: its Analytical Mode is")
    print("reported on an analysis and gates no constraint, so determining it buys nothing.")
    print("\nDETERMINED means a single file kind implies that mode and no other. AMBIGUOUS narrows")
    print("the answer without fixing it. UNREACHABLE means the componentType vocabulary cannot")
    print("express the distinction -- NOT that the mode did not occur.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
