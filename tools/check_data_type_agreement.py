#!/usr/bin/env python3
"""Fail when a sidecar's Data Type disagrees with its workbook's.

TWO FILES CARRY A Data Type COLUMN AND ONLY ONE IS READ. schema_path_emitter._load_rows and
build_tapp.unit both take `data type` from the WORKBOOK (draftTAPPs/<name>.csv, or the delivered
table under tapp/Current TAPPs/). docs/<name>.schemapaths.csv carries its own copy, which is read
for REPORTING only -- map_subject_keys.py DESCRIBE_FIELDS includes it -- and which no generator
ever consults.

THE SIDECAR COPY IS SEEDED FROM THE WORKBOOK AND THEN FROZEN, which is the whole mechanism of the
drift. bootstrap_schemapaths reads the workbook's column in load_rows and writes it into the
sidecar, but it preserves rows that already exist unless passed --reseed-all.
So the two start identical and nothing re-syncs them: one hand-edit of either file diverges them
permanently, and the editor gets no signal, because the value they can see is right there in the
file they opened.

So a sidecar edit can look applied, regenerate cleanly, and change nothing. That happened on
2026-10-10: Image Width/Height were set to `Integer (QuantitativeValue)` in the sidecar, the
pipeline ran green, and the emitted shape was still anyOf[integer, string] because the workbook
still said `Integer`. A green run that changes nothing is the hardest failure to notice, which is
the whole reason this check exists.

AND THE DRIFT IS NOT HYPOTHETICAL. Measured when this was written: 3460 items agree, 14 DIFFER and
3 differ only in spelling. The 14 are split 8 in EBSD_TAPP_draft_v2 and 6 in STEM_TAPP_draft_v2 --
a first count of this put all 17 in EBSD, which was wrong; the tool is what to trust here, not a
remembered figure. In each one the sidecar NAMES the unit (`Numeric (kV)`, `Numeric (nA)`,
`Numeric (deg)`) and the workbook only asserts one exists (`Number + unit`), where
build_tapp.unit() returns 'kV' for the first and UNIT_UNNAMED for the second.

WHAT THAT COST, stated accurately, because the obvious answer is wrong. It is tempting to say 14
properties emitted `schema:unitText: {type: string}` where `{const: "kV"}` was available. They did
not, and reconciling the 17 changed no emitted schema at all -- measured, not assumed. The const
is written by build_tapp.param_template_def, which fires only for an item placed on
`schema:additionalProperty` on the $MethodDefinition side; all 17 are placed instead on a direct
`ada:<name>Default` property, where schema_path_emitter.leaf_for ignores the unit entirely. Their
analysis-side placement does carry schema:unitText, but already required it before the change,
because UNIT_UNNAMED is truthy and param_value_def only tests for presence.

So the value here is not a shape that improved today. It is that the two files now say the same
thing, so a reader of either sees the right unit and a later --reseed-all cannot silently revert
the better value; and that the named unit is held in the file that IS read, so it survives any of
these items moving to an additionalProperty placement. The reason to keep the check is that the
drift is invisible either way -- which was true before anyone knew whether it mattered.

WHICH FILE WINS IS NOT DECIDED HERE, deliberately. For a delivered TAPP the workbook is the
delivery and authoritative; for a draft we author both are ours, and the sidecar may well hold the
better value -- it did in all 17 cases above. This check only insists they AGREE, which is true
under either answer and does not need the question settled first. Once they agree, a later
--reseed-all is a no-op rather than a silent revert, which is the second reason to keep them so.

Every reference above names a FUNCTION rather than a line, on the same principle
audit_ig_consistency.py matches its fixes on (check, guide, property): a line number is wrong as
soon as anything above it is edited. These were written as line numbers first and three went stale
within the hour, from edits made in this very change.

    python tools/check_data_type_agreement.py                      # report
    python tools/check_data_type_agreement.py --self-test          # prove it fires; run FIRST
    python tools/check_data_type_agreement.py --emitters           # + example vs schema
    python tools/check_data_type_agreement.py --emitters --strict  # the CI gate

Reads only.
"""
import argparse
import collections
import csv
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDECARS = os.path.join(ROOT, "docs", "*.schemapaths.csv")
# Where a sidecar's workbook lives, in the order tried. A draft we author first, then the delivery.
WORKBOOK_DIRS = [os.path.join(ROOT, "draftTAPPs"),
                 os.path.join(ROOT, "tapp", "Current TAPPs")]

# Equivalence is DERIVED from what the readers do, not hand-listed. build_tapp.jtype maps both
# "numeric" and "number" to "number", and build_tapp.unit keys off the parenthetical or
# a "+ unit" suffix and never off that word -- so the two spellings are interchangeable wherever
# they appear, and a hand-written pair set would only have covered the pairs someone thought of.
# The first version of this check listed {"number + unit", "numeric + unit"} and consequently
# reported three bare "Numeric" vs "Number" rows as real disagreements.
#
# Still reported, as a SPELLING VARIANT rather than silently folded into the agreement count: it
# changes nothing today, but it is a second spelling in a controlled vocabulary, and it stops being
# harmless the moment anything matches a Data Type cell exactly.
def canonical(v):
    return " ".join(v.lower().replace("numeric", "number").split())


def _column(path, want):
    """{item -> set of values} for one column of a CSV, or {} if it has no such column."""
    with io.open(path, encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return {}
    hdr = [h.strip().lower() for h in rows[0]]
    if want not in hdr:
        return {}
    i = hdr.index(want)
    out = collections.defaultdict(set)
    for r in rows[1:]:
        if r and r[0].strip() and len(r) > i:
            out[r[0].strip()].add(r[i].strip())
    return out


def workbook_for(sidecar):
    stem = os.path.basename(sidecar).split(".schemapaths")[0]
    for d in WORKBOOK_DIRS:
        p = os.path.join(d, stem + ".csv")
        if os.path.exists(p):
            return p
    return None


def _equivalent(a, b):
    """True when two sets of Data Type cells differ only in ways no reader can see."""
    return {canonical(x) for x in a} == {canonical(x) for x in b}


def compare(pattern=None):
    """(agree, hard, soft, unpaired) -- hard differences, and cosmetic ones, listed separately."""
    agree = 0
    hard, soft, unpaired = [], [], []
    for sc in sorted(glob.glob(pattern or SIDECARS)):
        wb = workbook_for(sc)
        name = os.path.basename(sc).split("_TAPP")[0]
        if not wb:
            unpaired.append(os.path.basename(sc))
            continue
        s, w = _column(sc, "data type"), _column(wb, "data type")
        for item, sv in sorted(s.items()):
            wv = w.get(item)
            if wv is None:
                continue          # a row the workbook does not have is a different question
            if sv == wv:
                agree += 1
            elif _equivalent(sv, wv):
                soft.append((name, item, sorted(sv), sorted(wv)))
            else:
                hard.append((name, item, sorted(sv), sorted(wv)))
    return agree, hard, soft, unpaired


def check_emitters(verbose=False):
    """Every distinct Data Type cell: does the EXAMPLE placeholder satisfy the SCHEMA leaf?

    A second way the one cell can be read inconsistently, and the one that actually shipped a
    failure. schema_path_emitter.leaf_for turns a cell into a schema; schema_path_example_emitter
    .placeholder turns the same cell into an instance. Nothing made them agree. Adding the
    QuantitativeValue Data Type taught the first that a cell could mean an OBJECT and left the
    second returning a bare 1, so STEM's -P0 shipped schema:width: 1 against a schema requiring an
    object -- an example failing the schema generated from the very same cell.

    Cheap to check exhaustively, because the interesting axis is the DISTINCT cell value and there
    are 52 of those across every workbook and sidecar, not thousands of rows.
    """
    import jsonschema
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import schema_path_emitter as e
    import schema_path_example_emitter as x

    seen = collections.Counter()
    for f in (glob.glob(os.path.join(ROOT, "draftTAPPs", "*.csv"))
              + glob.glob(os.path.join(ROOT, "tapp", "Current TAPPs", "*.csv"))
              + glob.glob(SIDECARS)):
        for item, vals in _column(f, "data type").items():
            for v in vals:
                if v:
                    seen[v] += 1

    bad = []
    for dt, n in seen.most_common():
        try:
            jsonschema.validate(x.placeholder({"dt": dt}, "Some Item", {}), e.leaf_for(None, dt))
        except jsonschema.ValidationError as ex:
            bad.append((dt, n, ex.message[:90]))
        except Exception as ex:
            bad.append((dt, n, "%s: %s" % (type(ex).__name__, str(ex)[:80])))
    print("distinct Data Type cells            : %d" % len(seen))
    print("cells whose example fails its schema: %d" % len(bad))
    for dt, n, msg in bad[:25]:
        print("  %-34s x%-5d %s" % (dt[:34], n, msg))
    if bad:
        print()
        print("The schema emitter and the example emitter disagree about what this cell asks for.")
        print("Fix whichever is wrong -- but import the shared predicate rather than restating it,")
        print("or the two drift apart again on the next Data Type that is added.")
    return len(bad)


def self_test():
    """Prove the check FIRES, on a synthetic pair with a known disagreement.

    The check reports 0 against the current corpus. A 0 from a check that cannot detect anything
    looks exactly like a 0 from a clean corpus -- this project has paid for that confusion more
    than once (a SHACL target selected by the property under test; a mirror sync whose missing
    secret skipped every step and still concluded success). So the 0 above means nothing unless
    this passes.

    Covers the three verdicts separately, because collapsing them is how a real disagreement gets
    reported as cosmetic and ignored.
    """
    import shutil
    import tempfile

    global WORKBOOK_DIRS
    keep = WORKBOOK_DIRS
    tmp = tempfile.mkdtemp(prefix="dtcheck-")
    try:
        wbdir = os.path.join(tmp, "wb")
        scdir = os.path.join(tmp, "sc")
        os.makedirs(wbdir)
        os.makedirs(scdir)
        WORKBOOK_DIRS = [wbdir]

        def write(path, rows):
            with io.open(path, "w", encoding="utf-8", newline="") as fh:
                csv.writer(fh, lineterminator=chr(10)).writerows(rows)

        name = "FAKE_TAPP_draft_v9"
        write(os.path.join(scdir, name + ".schemapaths.csv"), [
            ["Metadata Item", "Data Type"],
            ["Real Difference", "Numeric (kV)"],      # the unit is named on one side only
            ["Cosmetic Only", "Numeric + unit"],      # numeric/number: no reader can tell
            ["Already Agrees", "Integer"],
            ["Sidecar Only", "Text"],                 # absent from the workbook: not a verdict
        ])
        write(os.path.join(wbdir, name + ".csv"), [
            ["Metadata Item", "Data Type"],
            ["Real Difference", "Number + unit"],
            ["Cosmetic Only", "Number + unit"],
            ["Already Agrees", "Integer"],
        ])

        agree, hard, soft, unpaired = compare(os.path.join(scdir, "*.schemapaths.csv"))
        checks = [
            ("a named unit against an unnamed one is a REAL disagreement",
             [i for _, i, _, _ in hard] == ["Real Difference"]),
            ("numeric/number alone is reported as COSMETIC, not as a disagreement",
             [i for _, i, _, _ in soft] == ["Cosmetic Only"]),
            ("an identical cell counts as agreement", agree == 1),
            ("a row the workbook lacks is not a verdict either way",
             "Sidecar Only" not in [i for _, i, _, _ in hard + soft]),
            ("a sidecar whose workbook is missing is reported, not silently skipped",
             compare(os.path.join(scdir, "*.schemapaths.csv"))[3] == [] and
             len(compare(os.path.join(wbdir, "*.csv"))[3]) == 1),
        ]
    finally:
        WORKBOOK_DIRS = keep
        shutil.rmtree(tmp, ignore_errors=True)

    # The emitter-agreement check reports 0 too, so it needs the same proof. Put placeholder back
    # to the behaviour that actually shipped -- a bare scalar for a QuantitativeValue cell -- and
    # require that check_emitters notices.
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import schema_path_example_emitter as x
    keep_ph = x.placeholder
    try:
        x.placeholder = lambda m, item, sidecar: 1
        regressed = check_emitters()
    finally:
        x.placeholder = keep_ph
    checks.append(("a scalar example for a QuantitativeValue cell is CAUGHT", regressed > 0))
    checks.append(("and the real emitters agree", check_emitters() == 0))

    bad = 0
    for label, ok in checks:
        print("  %s  %s" % ("ok  " if ok else "FAIL", label))
        bad += not ok
    print("self-test: %d/%d" % (len(checks) - bad, len(checks)))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sidecars", help="glob for the sidecars (default: docs/*.schemapaths.csv)")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero on any disagreement, for use as a CI gate")
    ap.add_argument("--self-test", action="store_true",
                    help="prove the check fires, on a synthetic pair; run this FIRST")
    ap.add_argument("--emitters", action="store_true",
                    help="also check the example emitter agrees with the schema emitter")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    agree, hard, soft, unpaired = compare(a.sidecars)

    nbad = check_emitters() if a.emitters else 0
    if a.emitters:
        print()
    print("items whose Data Type agrees : %d" % agree)
    print("items that DISAGREE          : %d" % len(hard))
    print("cosmetic spelling variants   : %d" % len(soft))
    if unpaired:
        print("sidecars with no workbook    : %d (%s)"
              % (len(unpaired), ", ".join(unpaired[:4])))
    for label, rows in (("DISAGREE", hard), ("spelling variant", soft)):
        if not rows:
            continue
        print("\n%s:" % label)
        for name, item, sv, wv in rows[:40]:
            print("  %-20s %-38s sidecar=%s  workbook=%s" % (name, item[:38], sv, wv))
        if len(rows) > 40:
            print("  ... and %d more" % (len(rows) - 40))
    if hard:
        print("\nThe WORKBOOK is what schema_path_emitter._load_rows reads, so a sidecar-only")
        print("does not reach the build. Promote the value you want into the workbook -- and")
        print("refresh its .xlsx twin with make_draft_xlsx_twin.py --refresh <NAME> --write, or the")
        print("twin silently keeps the old one.")
    if a.strict and hard:
        sys.exit("%d item(s) disagree between sidecar and workbook" % len(hard))
    if a.strict and nbad:
        sys.exit("%d Data Type cell(s) whose example fails its own schema" % nbad)
    return 0


if __name__ == "__main__":
    sys.exit(main())
