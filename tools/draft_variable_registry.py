#!/usr/bin/env python
"""PROTOTYPE: factor the per-technique parameter registries into a variable registry.

Writes `docs/variable_registry_draft.json`. Report-only -- NOTHING consumes it, no schema changes,
no generator is wired to it. It exists to answer "is this feasible, and what does it cost" with
measurements instead of estimates, in the shape of CODATA's variable index
(https://ai.codata.org/variableindex).

WHAT THE REGISTRIES LOOK LIKE TODAY. Six collections under `_sources/registry/` hold 1893 `$defs`
between them, every one minted per consuming technique: the `$def` key carries a technique prefix
(`epma_detectionLimitDefault`) and the `@id` const is `ada:parameter/<tapp>TAPP/<name>`. The
LOGICAL variable is neither of those -- it is the `schema:name` const, the TAPP workbook's Metadata
Item, and there are 267 distinct ones. So one logical variable such as `Pre-Analysis Imaging and
Screening` exists 116 times over, once per technique that consumes it.

THE TARGET SHAPE IS ALREADY DEFINED UPSTREAM, which is what makes this tractable. CDIF publishes
`cdifDataType/cdifRepresentedVariable` and `cdifDataType/cdifInstanceVariable`, and the latter
carries `cdif:isDefinedBy_RepresentedVariable` -- "the RepresentedVariable this InstanceVariable
instantiates". The relation this registry needs is therefore a vendored CDIF property, not an
extension we have to propose upstream:

    267 x cdi:RepresentedVariable      the concept + value domain, not dataset-bound
    1893 x the existing registry defs  each referencing its RepresentedVariable

Two things an earlier pass got wrong, measured here instead:

  * `schema:propertyID` is NOT patchily present. It partitions CLEANLY by side -- 1233
    analysis-side defs carry it and none carry `schema:valueName`; 660 procedure-side defs carry
    `valueName` and none carry `propertyID`; 0 defs carry both, 0 carry neither. There is no
    coverage gap and no branch is needed. CDIF documents `cdif:uses` as "essentially the same as
    schema:propertyID", so the analysis side already carries the link in all but name.
  * The name belongs in `cdif:name` and the definition in `cdif:definition`, per the vendored
    `cdifRepresentedVariable` schema. `cdi:measures` is a different property -- it points at the
    CONCEPT measured, not at the variable's label.

THE REAL COST IS DEFINITIONAL, NOT MECHANICAL. 31 of the 267 logical names carry more than one
`description` across their defs, and only 2 of those reduce to the procedure/analysis side split
(where two descriptions of one concept at two levels is correct, and is precisely the
RepresentedVariable/InstanceVariable distinction this registry is built on). The other 29 conflict
WITHIN a side: the same workbook label means subtly different things per technique. `Detection
Limit` has 5 variants across 23 defs -- a procedure-typical estimate, a session value in ug/g, a
method detection limit at 99% confidence, an elemental limit with units specified, and one
carrying an isotope-dilution caveat. That is not wording drift.

So each of the 29 is a decision nobody can automate: ONE RepresentedVariable whose definition is
chosen and whose per-technique nuance moves onto the usage, or SEVERAL because the label is
overloaded. This tool refuses to pick. It emits them under `conflicts` with every variant and the
defs behind it, and mints a RepresentedVariable only where the definition is already unanimous.

Usage:
    python tools/draft_variable_registry.py           # measure and report
    python tools/draft_variable_registry.py --write   # write docs/variable_registry_draft.json
"""
import argparse
import collections
import io
import json
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join("docs", "variable_registry_draft.json")

# Every collection build_tapp writes a parameter or column def into. The side is derived PER DEF
# from which identity property it carries, never from the collection: monitoredPropertyColumns
# holds 62 procedure-side defs and 1 analysis-side one, so a per-collection assumption mis-sides
# that one.
COLLECTIONS = ("parameterTemplates", "parameterValues", "targetSpeciesColumns",
               "monitoredPropertyColumns", "targetMaterialColumns", "reportedPropertyColumns")


# The workbooks' own section headers, which are rows carrying a string in `Metadata Item` and
# nothing else. `schema_path_emitter._load_rows` already recognises and skips them
# (`re.match(r"^\d+\.\s", item)`), so they are structure rather than fields.
#
# 252 Purpose texts cite a section by its NUMBER -- "also recorded in the Group 1 coupling
# fields", "documented in Group 3 and Group 4" -- which is meaningless to anyone reading a
# definition outside the workbook it came from. Substituting the section name makes the reference
# say something, which is the point even though it does not become a resolvable link.
#
# Derived from all 61 workbooks on 2026-10-23, not assumed: sections 1-6 are IDENTICAL in every
# one. Section 7 exists in exactly two (`EBSD Acquisition and Indexing`, `STEM Acquisition`) and
# is therefore technique-specific, which is why it is absent here -- and no definition cites a
# Group 7, nor a Group 5, so every one of the 252 references resolves against this map alone.
# Re-derive with: for each TAPP, scan tapp_source.rows() for `Metadata Item` matching ^(\d+)\.\s
_SECTIONS = {
    "1": "Procedure Identification",
    "2": "Samples",
    "3": "Instrument & Software",
    "4": "Measurement Information",
    "5": "Data Processing",
    "6": "Quality Control & Uncertainty",
}


def resolve_group_refs(text):
    """Replace `Group N` with the workbook section name N refers to. See _SECTIONS."""
    return re.sub(r"\bGroup\s+(\d+)\b",
                  lambda m: _SECTIONS.get(m.group(1), m.group(0)), text or "")


# Label names that still contain `Analyte` and are PROTECTED from the sweep below. A definition
# citing one of these is citing a name, and rewriting a name invents a reference. Three of them
# have no current workbook row at all -- `Analyte Estimation Method` is `Target Species Estimation
# Method` today and `Mass Resolution per Analyte` is `Mass Resolution Assignment` -- so their defs
# look like residue from an earlier delivery, but a full regeneration reproduces them, so they are
# derived from something not yet located. Protected either way: the sweep is not the place to
# resolve that.
# British/American spelling, as an EXPLICIT word list derived from the corpus rather than a
# generic suffix rule. American chosen (Stephen, 2026-10-23, "use volatilization");
# `volatilisation` vs `volatilization` was the whole of the difference between the SEM and EPMA
# readings of Time-Dependent Intensity Correction.
#
# A generic `ising -> izing` rule stood here first and was WRONG: it rewrites `arising` to
# `arizing`. That did no visible damage while these patterns only fed the equality test, but it
# would have corrupted emitted text the moment the sweep began applying them. Only three words in
# the whole corpus carry the -isation/-ised/-ising axis -- characterisation x118, volatilisation
# x6, linearisation x1 -- so enumerating them is both safe and auditable.
#
# `metres -> meter` and `centre -> center` stood here too and are deliberately absent: those are
# unit names (micrometres x19, nanometres x6, millimetres x4) and a term of art
# (`centre-to-centre`), a different axis from a spelling convention, and nobody has ruled on them.
_SPELLING = (
    (r"\bvolatilisation\b", "volatilization"),
    (r"\bcharacterisation\b", "characterization"),
    (r"\blinearisation\b", "linearization"),
)

_PROTECTED = (
    "Per-Analyte Calibration Strategy",
    "Mass Resolution per Analyte",
    "Analyte Estimation Method",
    "Technique per Analyte",
)


def canonicalise(text):
    """Definition text with `analyte` swept to `target species`, and section numbers resolved.

    `target species` REPLACED `analyte` in recent TAPP updates (Stephen, 2026-10-23), so this
    applies the surviving term to the text a consumer reads. It is a CONSUMER-SIDE sweep by
    necessity: the definitions come from the TAPP workbooks (`build_tapp` takes `desc` straight
    from the row) and those are read-only to this repo, so the only alternative is upstream.
    The sidecars cannot carry it either -- they have no text column at all.

    Two things it deliberately does NOT do. It does not touch label NAMES, only prose: 16
    definitions cite `the Analyte field`, which has no row today, and sweeping the prose repoints
    those to `the Target Species field` -- but rewriting a name that still exists would invent a
    dangling reference, which is why _PROTECTED is masked out first. And it preserves case, so a
    mid-sentence `analyte` and a cited `Analyte` both land correctly.
    """
    text = text or ""
    masks = {}
    for i, name in enumerate(_PROTECTED):
        if name in text:
            key = "\x00%d\x00" % i
            masks[key] = name
            text = text.replace(name, key)

    def sub(m):
        w = m.group(0)
        return "Target Species" if w[:1].isupper() else "target species"

    text = re.sub(r"\bAnalytes?\b|\banalytes?\b", sub, text)
    for key, name in masks.items():
        text = text.replace(key, name)

    # American spelling, decided for `volatilization` (Stephen, 2026-10-23) and applied to the
    # whole -isation axis for consistency: leaving `normalization` x62 beside `characterisation`
    # x118 in one registry is the inconsistency this exists to remove. Only the three words
    # enumerated in _SPELLING are touched -- see the note there on why a generic suffix rule is
    # not safe, and why the metre/centre axis is excluded.
    for pat, rep in _SPELLING:
        text = re.sub(pat, rep, text)
    return resolve_group_refs(text)


def _camel(label):
    """A stable @id token from a workbook label. Lower camel, per the repo's naming decision.

    A trailing optional-plural `(s)` is dropped rather than folded in: four labels carry one
    (`Data Processing Software(s)`, `Background Position(s)`, `EDS Calibration Standard(s)`,
    `Spectroscopic Detector(s)`) and keeping it yields `dataProcessingSoftwareS`, which reads as
    a typo. Verified not to collide with any other label's token after stripping. Parentheses
    elsewhere hold an acronym or a qualifier and ARE folded in, which is why this is a suffix
    rule and not a general paren rule.
    """
    label = re.sub(r"\(s\)\s*$", "", label, flags=re.I)
    parts = [p for p in re.split(r"[^0-9A-Za-z]+", label) if p]
    if not parts:
        return "unnamed"
    head = parts[0]
    head = head.lower() if head.isupper() and len(head) > 1 else head[:1].lower() + head[1:]
    return head + "".join(p[:1].upper() + p[1:] for p in parts[1:])


def _live_labels():
    """Metadata Items that exist in the CURRENT sources, keyed case- and space-insensitively.

    `registry/` is `isTypeLibrary`, so a def whose row has been renamed away is not removed -- it
    simply stops being referenced. Measured 2026-10-23: 37 of the 1893 defs (2.0%) carry a label
    present in neither the current workbooks nor the module sidecars, and nothing outside
    `registry/` references any of them -- 0 hits across every tapp/, detail/ and profile/ schema,
    resolved or otherwise. They are inert, which is why no gate notices them.

    They are NOT inert to this prototype, though, which counted them as variables. They produced
    3 phantom conflicts and 4 phantom "duplicate label pairs" -- every pair turning out to be a
    retired label sitting beside its replacement (`Analyte Estimation Method` beside `Target
    Species Estimation Method`, `Isobaric Interference Corrections Applied` beside `Spectral
    Interference Corrections Applied`). So the filter exists to keep the measurement honest, not
    to fix anything in the schemas.

    Matched case- and space-insensitively: checked for re-casing drift and found none, but an
    exact match would report a re-cased label as retired, which is a failure mode worth not
    having.
    """
    def key(s):
        return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

    import csv
    import glob
    import build_tapp as bt
    import tapp_source

    live = {}
    for tapp in sorted(bt.TAPP_CONFIGS):
        try:
            bt.configure(tapp)
            rows = tapp_source.rows(bt.XLSX)
        except Exception:
            continue
        for r in rows[1:]:
            item = bt.norm(r[0]) if r else ""
            if item and not re.match(r"^\d+\.\s", item):
                live.setdefault(key(item), item)
    for f in glob.glob(os.path.join("docs", "modules", "Module_*.schemapaths.csv")):
        for r in csv.DictReader(io.open(f, encoding="utf-8-sig")):
            item = (r.get("Metadata Item") or "").strip()
            if item:
                live.setdefault(key(item), item)
    return live, key


def load_defs():
    """Every registry $def, with the fields a variable registry would need from it."""
    # `lkey`, not `key`: the loop below binds `key` to each $def name and would shadow it.
    live, lkey = _live_labels()
    out = []
    for coll in COLLECTIONS:
        path = os.path.join(ROOT, "_sources", "registry", coll, "schema.yaml")
        doc = yaml.safe_load(io.open(path, encoding="utf-8")) or {}
        for key, sub in (doc.get("$defs") or {}).items():
            props = sub.get("properties") or {}

            def const(name, _p=props):
                return (_p.get(name) or {}).get("const")

            out.append({
                "collection": coll,
                "def": key,
                # The side is the identity property, measured per def. See COLLECTIONS.
                "side": "analysis" if "schema:propertyID" in props else "procedure",
                "id": const("@id"),
                "name": const("schema:name"),
                # Canonicalised here, so every consumer of a definition -- the conflict triage as
                # well as the emitted registry -- sees the same text.
                "definition": canonicalise((sub.get("description") or "").strip()),
                "dataType": const("ada:dataType"),
                "unitText": const("schema:unitText"),
                # Does a row with this label still exist? See _live_labels.
                "live": lkey(const("schema:name")) in live,
            })
    return out


def build(defs):
    """({variable @id -> node}, [conflict, ...]) grouped on the logical name."""
    by_name = collections.defaultdict(list)
    for d in defs:
        # Retired labels are EXCLUDED, not silently dropped: main() reports them under
        # `retired_labels` with their def counts. A silent skip is lost coverage, which is the
        # habit docs/SILENT_SUCCESS.md exists to break.
        if d["name"] and d.get("live", True):
            by_name[d["name"]].append(d)

    variables, conflicts = {}, []
    for name in sorted(by_name):
        rows = by_name[name]
        variants = collections.defaultdict(list)
        for r in rows:
            variants[r["definition"]].append(r["def"])

        # Does the divergence reduce to the side split? Two descriptions of one concept, one per
        # side, is CORRECT -- it is the level distinction, not a disagreement. Anything beyond
        # that is a genuine conflict.
        per_side = {s: {r["definition"] for r in rows if r["side"] == s}
                    for s in ("procedure", "analysis")}
        side_only = all(len(v) <= 1 for v in per_side.values())

        vid = "ada:variable/" + _camel(name)

        if len(variants) > 1 and not side_only:
            # Emitted as a QUESTION, not a variable. Taking the most common definition here would
            # bury four other readings of `Detection Limit` behind a majority vote.
            conflicts.append({
                "proposed@id": vid,
                "cdif:name": name,
                "defs": len(rows),
                "why": ("more than one definition within a single side, so this label is either "
                        "overloaded -- several RepresentedVariables -- or needs one definition "
                        "chosen and the per-technique nuance moved onto the usage"),
                "variants": [{"definition": d, "defs": sorted(ks)}
                             for d, ks in sorted(variants.items(), key=lambda kv: -len(kv[1]))],
            })
            continue

        node = {
            "@id": vid,
            "@type": ["cdi:RepresentedVariable"],
            "cdif:name": name,
            # Where the only divergence IS the side split, both readings are kept, keyed by side,
            # rather than collapsed: the procedure side defines what will be recorded, the
            # analysis side what was.
            "cdif:definition": (sorted(variants)[0] if len(variants) == 1
                                else {s: sorted(v)[0] for s, v in per_side.items() if v}),
            "ada:usageCount": len(rows),
            "ada:usages": [{"@id": r["id"], "def": r["def"], "collection": r["collection"],
                            "side": r["side"]} for r in sorted(rows, key=lambda r: r["def"])],
        }
        dtypes = sorted({r["dataType"] for r in rows if r["dataType"]})
        units = sorted({r["unitText"] for r in rows if r["unitText"]})
        if dtypes:
            node["cdi:hasIntendedDataType"] = dtypes[0] if len(dtypes) == 1 else dtypes
        if units:
            node["cdi:describedUnitOfMeasure"] = units[0] if len(units) == 1 else units
        variables[vid] = node

    return variables, conflicts


# ---------------------------------------------------------------------------
# Conflict triage
#
# The 29 within-side conflicts are not one kind of problem, and treating them as one would put a
# spelling difference in the same queue as two different physical measurands. The classes below
# are ordered by how much judgement they need, and the first two need NONE.
#
# This is TRIAGE, not a verdict: it narrows what a person has to read, and the hardest classes are
# deliberately the ones it refuses to resolve.
# ---------------------------------------------------------------------------

# Applied to both definitions before comparing them. If two definitions become equal under
# normalisation, they never disagreed -- the vocabulary did.
_NORMALISERS = _SPELLING + (
    # The analyte / target-species axis. These name the same set -- several sidecar rows say so
    # outright ("one per analyte, these being the same set"). It is the entire difference for
    # Calibration Factor and Determination Method (59 defs, the largest conflict in the registry)
    # and for Mass Resolution Assignment.
    #
    # NORMALISE TOWARD `target species`: it REPLACED `analyte` in recent TAPP updates (Stephen,
    # 2026-10-23), so `analyte` is the retired term. The direction does not change WHICH conflicts
    # are detected -- this normaliser only answers "does the difference vanish", which is symmetric
    # -- but it records which term survives, and the first version of this list pointed the wrong
    # way. That matters when the normalisation is applied to the sidecars, and it matters for
    # choosing a surviving wording, because MAJORITY COUNT GETS IT BACKWARDS here: Calibration
    # Factor's `analyte` variant has 45 defs against `target species`' 14, since the 45 are the
    # un-migrated long tail of techniques and the 14 are the migrated core. Measured 2026-10-23:
    # 155 defs say target species, 73 say analyte, and 45 of those 73 are that one row.
    (r"\banalytes?\b", "target species"), (r"\btarget-species\b", "target species"),
)

_SIGNALS = (
    # A different physical measurand or signal chain -- the strongest case for SPLITTING a label
    # into several RepresentedVariables rather than reconciling one definition.
    ("different measurand",
     {"bremsstrahlung", "polychromatic", "tube", "ion-beam", "fib-sem", "milling",
      "d-stem", "stem-eels"}),
     # `magnet` and `sector` were here and are NOT measurand signals: a sector-field magnet is the
     # instrument performing the SAME measurement. Including them mis-split Mass Resolution per
     # Analyte, whose variants differ only in how much mechanism they describe.
    # A different statistic for the same quantity. Genuinely contested: a method detection limit
    # at 99% confidence is not a procedure-typical estimate, and no normalisation reconciles them.
    ("different statistic",
     {"confidence", "reproducibility", "deviation", "sd", "se", "ci", "statistics"}),
    # Same quantity, different unit convention. Units belong on the USAGE
    # (cdi:describedUnitOfMeasure), not in the shared definition.
    ("unit convention",
     {"kev", "kv", "kilovolts", "nanoamperes", "microseconds", "milliseconds", "ms",
      "micrometres", "micrometers", "nanometres", "wt%", "ng", "g/g", "g/l", "percent"}),
    # An applicability restriction rather than a different concept -- also usage-level.
    ("scope conditional", {"applicable", "mandatory", "required", "n/a", "unless"}),
)

_STOP = set("""a an and are as at be been both but by can each either for from had has have how
if in into is it its may more must no none not of on one only or other over per rather same see
so some such than that the their then there these they this those to under use used using was
were what when where whether which while who with would""".split())


def classify(variants):
    """(class, note) for one conflict's variants. See _SIGNALS for what each class means."""
    def norm(t):
        t = t.lower()
        for pat, rep in _NORMALISERS:
            t = re.sub(pat, rep, t)
        # Hyphens are KEPT. Stripping them split `mc-icp-ms` into `mc icp ms`, and the
        # stray `ms` matched the millisecond unit signal -- so Interfering Species and Isobaric
        # Interference Corrections Applied were both triaged as a unit-convention difference on
        # the strength of a mass-spectrometer acronym.
        return re.sub(r"[^a-z0-9%/ -]+", " ", t)

    def words(t):
        return set(re.findall(r"[a-z0-9][a-z0-9%/-]*", norm(t)))

    texts = [v["definition"] for v in variants]
    # Equal after normalisation? Then the definitions never disagreed.
    if len({re.sub(r"\s+", " ", norm(t)).strip() for t in texts}) == 1:
        return "terminology drift", "identical once spelling and analyte/target-species are normalised"

    sets = [words(t) for t in texts]
    common = set.intersection(*sets)
    differing = (set.union(*sets) - common) - _STOP
    if not differing:
        return "wording only", "no content word distinguishes them"
    for name, signal in _SIGNALS:
        hit = sorted(differing & signal)
        if hit:
            return name, "distinguished by: " + ", ".join(hit[:6])
    # One variant's content is a superset of the others': the same concept, said at more length.
    if any(all(s <= big for s in sets) for big in sets):
        return "elaboration", "one variant's wording contains the others'"
    return "unclassified", "differs in substantive wording with no signal term"


def group_conflicts(conflicts):
    """Conflicts bucketed by class, worst-to-triage last."""
    order = ["terminology drift", "wording only", "elaboration", "unit convention",
             "scope conditional", "different statistic", "different measurand", "unclassified"]
    out = collections.OrderedDict((k, []) for k in order)
    for c in conflicts:
        cls, note = classify(c["variants"])
        c = dict(c, triage=cls, triage_note=note)
        out[cls].append(c)
    return collections.OrderedDict((k, v) for k, v in out.items() if v)


_VERDICT = {
    "terminology drift": "ONE variable, no decision needed -- normalise the wording in the sidecars",
    "wording only": "ONE variable, no decision needed -- keep the fullest definition",
    "elaboration": "ONE variable -- keep the fullest definition, move technique detail to the usage",
    "unit convention": "ONE variable -- units belong on the usage, not the definition",
    "scope conditional": "ONE variable -- the restriction belongs on the usage",
    "different statistic": "DECISION NEEDED -- these are different quantities under one label",
    "different measurand": "SPLIT -- a different device or signal chain, so several variables",
    "unclassified": "READ IT -- no signal term; a person has to judge",
}


def report(defs, variables, conflicts):
    sides = collections.Counter(d["side"] for d in defs)
    retired = collections.Counter(d["name"] for d in defs if d["name"] and not d.get("live", True))
    names = {d["name"] for d in defs if d["name"] and d.get("live", True)}
    if retired:
        print("retired labels EXCLUDED               : %d defs across %d label(s)"
              % (sum(retired.values()), len(retired)))
        for n, c in retired.most_common():
            print("    %-46s %d defs" % (n[:46], c))
        print()
    print("registry $defs                       : %d" % len(defs))
    print("  procedure side (schema:valueName)  : %d" % sides["procedure"])
    print("  analysis side  (schema:propertyID) : %d" % sides["analysis"])
    print("distinct logical variables           : %d" % len(names))
    print("  mintable now (definition agreed)   : %d" % len(variables))
    print("  blocked on a definitional decision : %d" % len(conflicts))
    dedup = len(defs) - len(names)
    print("\ndefs that would become usages of a shared variable: %d (%.0f%% of the registry)"
          % (dedup, 100.0 * dedup / max(len(defs), 1)))
    print("\nmost-reused variables:")
    for vid, n in sorted(((v["@id"], v["ada:usageCount"]) for v in variables.values()),
                         key=lambda kv: -kv[1])[:8]:
        print("   %-52s %d usages" % (vid[:52], n))
    if conflicts:
        print("\nblocked -- each needs a human decision, worst first:")
        for c in sorted(conflicts, key=lambda c: -len(c["variants"]))[:10]:
            print("   %-46s %d variants, %d defs"
                  % (c["cdif:name"][:46], len(c["variants"]), c["defs"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="write %s" % OUT)
    ap.add_argument("--group-conflicts", action="store_true",
                    help="triage the within-side conflicts by what actually differs")
    args = ap.parse_args()

    defs = load_defs()
    variables, conflicts = build(defs)

    if args.group_conflicts:
        groups = group_conflicts(conflicts)
        print("%d within-side conflicts, %d defs behind them\n"
              % (len(conflicts), sum(c["defs"] for c in conflicts)))
        for cls, items in groups.items():
            print("%s  (%d conflict%s, %d defs)"
                  % (cls.upper(), len(items), "" if len(items) == 1 else "s",
                     sum(c["defs"] for c in items)))
            print("    -> %s" % _VERDICT[cls])
            for c in sorted(items, key=lambda c: -c["defs"]):
                print("       %-48s %2d variants, %3d defs"
                      % (c["cdif:name"][:48], len(c["variants"]), c["defs"]))
                print("         %s" % c["triage_note"][:110])
            print()
        need = sum(len(v) for k, v in groups.items()
                   if k in ("different statistic", "different measurand", "unclassified"))
        print("needing a human decision : %d of %d" % (need, len(conflicts)))
        print("resolvable mechanically  : %d" % (len(conflicts) - need))
        return 0

    report(defs, variables, conflicts)

    doc = {
        "generator": "tools/draft_variable_registry.py",
        "status": ("DRAFT / PROTOTYPE. Nothing reads this, no schema references it, and no "
                   "generator emits from it. It is a feasibility measurement, not a deliverable."),
        "modelled_on": "https://ai.codata.org/variableindex",
        "target_shape": {
            "represented_variable": ("CDIF's vendored cdifDataType/cdifRepresentedVariable -- the "
                                     "concept plus value domain, not bound to any dataset"),
            "usage": ("each existing registry $def, referencing its variable through "
                      "cdif:isDefinedBy_RepresentedVariable, a vendored CDIF property on "
                      "cdifInstanceVariable, so no upstream extension is needed"),
            "name_carrier": ("cdif:name, with cdif:definition for the definition. NOT cdi:measures, "
                             "which points at the concept measured rather than at the label."),
            "propertyID": ("no branch needed: propertyID and valueName partition cleanly by side "
                           "(0 defs carry both, 0 carry neither), and CDIF documents cdif:uses as "
                           "'essentially the same as schema:propertyID'"),
            "open": ("whether a procedure-side schema:PropertyValueSpecification should be typed "
                     "cdi:InstanceVariable at all -- a specification is not an instance. The "
                     "reference to the RepresentedVariable is right either way, so this draft "
                     "records the usages without asserting an @type on them."),
        },
        # Reported, not silently dropped. See _live_labels for why they exist and why nothing in
        # the schemas is affected by them.
        "retired_labels": dict(collections.Counter(
            d["name"] for d in defs if d["name"] and not d.get("live", True))),
        "counts": {
            "registry_defs": len(defs),
            "registry_defs_live": sum(1 for d in defs if d.get("live", True)),
            "distinct_logical_variables": len(
                {d["name"] for d in defs if d["name"] and d.get("live", True)}),
            "mintable_now": len(variables),
            "blocked_on_a_definition": len(conflicts),
        },
        "conflicts": sorted(conflicts, key=lambda c: (-len(c["variants"]), c["cdif:name"])),
        "variables": variables,
    }
    if args.write:
        io.open(OUT, "w", encoding="utf-8", newline="\n").write(
            json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
        print("\nwrote %s" % OUT)
    else:
        print("\ndry run; --write to emit %s" % OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
