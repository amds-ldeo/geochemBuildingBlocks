#!/usr/bin/env python
"""Publish what the ADA loader needs to choose a nil REASON per gated field.

Writes `docs/mode_applicability.json`. gBB owns the workbooks' applicability; the loader owns the
record. This is the contract between them, and it exists so ADA does not hard-code 284 Y/N rules
that live in Ruolin's tables.

WHY A REASON AND NOT A MODE. No ADA record carries an analytical mode -- 0 of 7,447, with no source
field anywhere in 111,963 `record_subjects` (CLAUDE.md, analytical-mode section). A mode written
into a record would therefore be a GUESS asserted as fact. Choosing between two nil reasons is a
much weaker claim, and a wrong guess mislabels why a value is absent instead of inventing a
measurement:

    http://www.opengis.net/def/nil/OGC/0/unknown        a value exists but ADA was never sent it
    http://www.opengis.net/def/nil/OGC/0/inapplicable   this mode has no such value to send

THE RULE, and its asymmetry is the point:

    implied modes = union of the witnesses of the record's own ada:componentType values
    (`infer_analytical_mode.witnesses`), intersected with this technique's declared modes.

    no implied modes                         -> unknown
    field is "N" in EVERY implied mode       -> inapplicable
    anything else, including a mixed answer  -> unknown

`inapplicable` is a positive claim -- "there is no such value" -- so it requires unanimity among
the implied modes. `unknown` is true whenever ADA simply holds nothing, which is why it is the
default and the fallback. A technique whose mode gates nothing never reaches this rule at all.

SCOPE. Only the 14 of 61 techniques with mode-flag columns gate anything; for the other 47 the
`Analytical Mode` is informational. Of the 284 gated field rows, those with a `$Dataset` path are
the ones a RECORD can carry a reason for; `$MethodDefinition` rows live in the TAPP definition, a
different document, and are emitted separately so nobody mistakes one for the other.

Usage:
    python tools/build_mode_applicability.py            # dry run, prints the summary
    python tools/build_mode_applicability.py --write    # writes docs/mode_applicability.json
"""
import argparse
import collections
import glob
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b                      # noqa: E402
import schemapath_io                        # noqa: E402
import infer_analytical_mode as inf         # noqa: E402

OUT = os.path.join("docs", "mode_applicability.json")

NIL = "http://www.opengis.net/def/nil/OGC/0/"


def _sidecar_spec(xlsx):
    """The schema-path spec for the sidecar that mirrors this workbook, or {}."""
    stem = os.path.basename(xlsx).rsplit(".", 1)[0]
    path = os.path.join("docs", "%s.csv" % stem)
    try:
        return schemapath_io.load_spec(schemapath_io.csv_path(path))
    except Exception:
        return {}


def gated_rows(tapp):
    """Every field row whose applicability VARIES across this technique's mode columns.

    Returns (modes, rows). A row with uniform Y (or uniform N) is not gated: the mode makes no
    difference to it, so no reason can be derived from the mode either.
    """
    b.configure(tapp)
    rows = b.tapp_source.rows(b.XLSX)
    cols = b.mode_columns(rows)
    if not cols:
        return [], []
    header = [b.norm(v) for v in rows[0]]
    modes = [header[i] for i in cols]
    spec = _sidecar_spec(b.XLSX)
    out = []
    for row in rows[1:]:
        item = b.norm(row[0])
        if not item:
            continue
        vals = [(b.norm(row[i]) if i < len(row) else "").upper() for i in cols]
        if not (any(v == "Y" for v in vals) and any(v == "N" for v in vals)):
            continue
        entry = spec.get(item, {}) or {}
        paths = entry.get("path")
        paths = [paths] if isinstance(paths, str) else list(paths or [])
        out.append({
            "item": item,
            "applicability": dict(zip(modes, vals)),
            "dataset_paths": sorted(p for p in paths if p.startswith("$Dataset")),
            "procedure_paths": sorted(p for p in paths if p.startswith("$MethodDefinition")),
            # A module-owned row has no path of its own here; the module places it. Recorded so a
            # consumer can tell "no path" from "not gated" rather than inferring from an absence.
            "module_owned": not paths,
        })
    return modes, out


def build():
    techniques = {}
    for tapp in sorted(b.TAPP_CONFIGS):
        try:
            modes, rows = gated_rows(tapp)
        except Exception as exc:
            techniques[tapp] = {"error": "%s: %s" % (type(exc).__name__, exc)}
            continue
        if not rows:
            continue                        # gates nothing: informational mode, or no mode columns
        cts = [c for c in (b.TAPP_CONFIGS[tapp].get("component_types") or [])
               if not inf.NON_EVIDENTIAL.search(c)]
        witnesses = {}
        for ct in sorted(cts):
            implied = sorted(m for m in modes if inf.witnesses(ct, m))
            if implied:
                witnesses[ct] = implied
        techniques[tapp] = {
            "modes": modes,
            # componentType -> the modes it is evidence for. A componentType implying ONE mode
            # fixes it; implying several only narrows, which the reason rule handles by requiring
            # unanimity before it will say `inapplicable`.
            "witnesses": witnesses,
            "gated_fields": sorted(rows, key=lambda r: r["item"]),
        }
    return {
        "generator": "tools/build_mode_applicability.py",
        # The mode PROPERTY itself, as distinct from the fields it gates. Recorded here because the
        # loader needs both and the two take DIFFERENT reasons.
        "mode_property": {
            "property": "ada:analyticalMode",
            "reason": "unknown",
            "form": "a string element, the expanded OGC IRI",
            "why_not_inapplicable": (
                "every analysis has an analytical mode; ADA simply does not record which. "
                "`inapplicable` asserts that no such value exists, which is false for every "
                "record. `inapplicable` is for a GATED FIELD in a mode that excludes it, which "
                "is what `techniques[].gated_fields` is for."),
            "where": (
                "the DATASET side only. detail/ places the property with no enum, so a nil IRI "
                "validates; tapp/ constrains items to the technique's mode enum for the 14 "
                "gating techniques, so a nil IRI would VIOLATE it there. That asymmetry is "
                "correct: a record may not know its mode, but a procedure that cannot say which "
                "modes it runs is not a procedure."),
            "not_required": (
                "ada:analyticalMode is declared and OPTIONAL everywhere -- 0 required sites "
                "repo-wide -- because the emitter does not record requiredness for a path ending "
                "in a bare []. So nothing currently demands a value and nothing needs filling. A "
                "correct fix emits `required` AND `minItems: 1`: measured across the tapp blocks, "
                "2135 required arrays already carry minItems and 279 do not, and `required` alone "
                "is satisfied by an empty array."),
        },
        "source": "the TAPP workbooks' mode-flag columns, via build_tapp.mode_columns()",
        "nil_reasons": {"unknown": NIL + "unknown", "inapplicable": NIL + "inapplicable"},
        "reason_rule": [
            "implied modes = union of witnesses of the record's ada:componentType values",
            "no implied modes -> unknown",
            "field is N in EVERY implied mode -> inapplicable",
            "anything else, including a mixed answer -> unknown",
            "inapplicable is a positive claim and needs unanimity; unknown is the safe default",
        ],
        "caveat": ("witnesses are derived from componentType NAMES, not from file contents; an "
                   "absent witness means the vocabulary cannot say, never that the mode did not "
                   "occur"),
        "techniques": techniques,
    }


def reason_for(field, implied):
    """The nil reason for one gated field given the implied modes. THE rule, in one place.

    Asymmetric on purpose: `inapplicable` asserts that no such value exists, so every implied
    mode has to agree; `unknown` merely says ADA holds nothing, which is true whenever the
    evidence is absent or mixed.
    """
    if not implied:
        return "unknown", "no componentType implies a mode"
    verdicts = {field["applicability"].get(m) for m in implied}
    if verdicts == {"N"}:
        return "inapplicable", "N in every implied mode"
    if "N" in verdicts:
        return "unknown", "mixed across implied modes"
    return "unknown", "applicable, but ADA holds no value"


def explain(tapp, cts, doc):
    """Walk the rule for one technique and one record's componentTypes."""
    t = (doc["techniques"] or {}).get(tapp)
    if not t:
        print("%s gates nothing (informational mode, or no mode columns)" % tapp)
        return 1
    implied = sorted({m for ct in cts for m in (t["witnesses"].get(ct) or [])})
    print("technique      %s" % tapp)
    print("componentTypes %s" % ", ".join(cts))
    print("implied modes  %s" % (", ".join(implied) or "(none)"))
    print()
    print("  %-46s %-14s %s" % ("gated $Dataset field", "nil reason", "why"))
    shown = 0
    for f in t["gated_fields"]:
        if not f["dataset_paths"]:
            continue
        reason, why = reason_for(f, implied)
        print("  %-46s %-14s %s" % (f["item"][:46], reason, why))
        shown += 1
    if not shown:
        print("  (this technique gates no $Dataset field, so no record-level reason applies)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write %s" % OUT)
    ap.add_argument("--explain", nargs="+", metavar="TAPP COMPONENTTYPE",
                    help="walk the rule: a TAPP key then the componentTypes a record carries")
    args = ap.parse_args()

    if args.explain:
        return explain(args.explain[0], args.explain[1:], build())

    doc = build()
    techs = doc["techniques"]
    n_fields = sum(len(t.get("gated_fields") or []) for t in techs.values())
    n_ds = sum(1 for t in techs.values() for f in (t.get("gated_fields") or [])
               if f["dataset_paths"])
    n_pd = sum(1 for t in techs.values() for f in (t.get("gated_fields") or [])
               if f["procedure_paths"])
    n_mod = sum(1 for t in techs.values() for f in (t.get("gated_fields") or [])
                if f["module_owned"])

    print("techniques whose mode gates a field : %d" % len(techs))
    print("gated field rows                    : %d" % n_fields)
    print("  with a $Dataset path (record-side): %d   <- a record can carry a reason for these" % n_ds)
    print("  with a $MethodDefinition path     : %d   (the TAPP definition, not the record)" % n_pd)
    print("  module-owned, no path here        : %d" % n_mod)

    # How often can the rule actually reach `inapplicable`? A technique with no deciding
    # componentType can only ever return `unknown`, and saying so is the point of the report.
    reach = collections.Counter()
    for tapp, t in sorted(techs.items()):
        wit = t.get("witnesses") or {}
        deciding = [c for c, ms in wit.items() if len(ms) == 1]
        reach["has a deciding componentType" if deciding else "unknown-only"] += 1
        print("  %-22s %2d gated, %2d witnessing componentType(s), %2d deciding"
              % (tapp, len(t.get("gated_fields") or []), len(wit), len(deciding)))
    print()
    for k, v in sorted(reach.items()):
        print("  %-30s %d technique(s)" % (k, v))

    if args.write:
        io.open(OUT, "w", encoding="utf-8", newline="\n").write(
            json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
        print("\nwrote %s" % OUT)
    else:
        print("\ndry run; --write to emit %s" % OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
