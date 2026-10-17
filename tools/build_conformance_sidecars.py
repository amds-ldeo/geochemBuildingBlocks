"""Generate the stage-2 `conformance.json` sidecar beside every profile block.

Stage 1 (CDIF/validation `detect_cdif_conformance`) decides the CDIF module URIs from
metadataBuildingBlocks' sidecars. Stage 2 decides `geochemProduct`, `adaProduct` and the technique
profile from sidecars that live HERE, generated from each profile's own schema so the declaration
rule cannot drift from the schema it describes. Authoritative format:
`CDIF/validation/docs/CDIF-Conformance-Declaration-Convention.md`, "Stage 2 — domain profiles".

Six fields, nothing else: conformsTo, presence, validityShapes, requires, exclusiveGroup, priority.

WHAT THIS REPLACES. The same decision is hand-coded today in amds-ldeo/metadata --
`schema_registry.profile_for_component_type()` plus the adaProduct routing of commit 8470122.
Generating it beside the schema means the rule and the schema are produced by one build.

`requires` IS DERIVED, NEVER HAND-LISTED
Read off each profile's own `allOf`: the CDIF module URIs it composes UNCONDITIONALLY. An
`if/then` composition is NOT a flat require -- stage 1 declares that module on its own when its
trigger content appears -- and a nested `$defs` `$ref` is not an inherited profile.

That derivation gives geochemProduct **core + provenance**, and getting there corrected two
written sources, so it is worth recording why. Validation's convention doc lists four (core,
discovery, data_description, provenance) with `discovery` annotated "entailed by
data_description"; the brief for this work listed three (core, discovery, provenance) after
data_description went conditional. Measured: the CDIF module sidecars in metadataBuildingBlocks
carry `requires: None` -- they are independent yes/no classes, so nothing is entailed by anything
in any machine-readable sense -- `cdifCore` does not compose `cdifDiscovery`, and geochemProduct
does not mention `cdifDiscovery` at all (0 occurrences). Discovery was never composed; it was
carried by a comment. Nothing is lost: stage 1 declares discovery on its own when a record has
discovery metadata, exactly as it does for manifest and data_description. Over-stating `requires`
would instead block a record from geochemProduct for a reason its schema never asserted.

THE EXCLUSION SET IS THE VOCABULARY, NOT A COPIED LIST
A technique's `presence` tests only componentTypes that DISCRIMINATE it. Universal types
(methodDescription, plot, logFile, ...) appear on every kind of product. The set comes from
`registry/vocab/componentType.json` minus `nil:` sentinels -- 22 terms, matching
`schema_registry.UNIVERSAL_COMPONENT_TYPES` EXACTLY (measured 2026-10-16).

Deriving it rather than copying matters. The brief named four generics (analysisLocation, report,
contextPhotography, quickLook), a SUBSET of the 22. Nine universals appear in TAPP_CONFIGS; five
fall outside those four, and two -- `ada:processingMethod` and `ada:shapefile` -- are claimed by
exactly ONE TAPP. A universal type with a single claimant LOOKS discriminating, so those profiles
would have matched every record carrying a processing-method or shapefile part. Counting
collisions cannot find that; only the vocabulary can.

TWO SOURCES FOR THE COMPONENT LIST, AND THEY ARE DISJOINT
- TAPP-backed blocks (`geochemProfile/<TECH>/profile`): from
  `build_tapp.TAPP_CONFIGS[<tapp>]["component_types"]`. These schemas carry ZERO inline
  componentType enums -- their types arrive by `$ref` -- so the config is the only source.
- Legacy blocks (`*/profile-ada`): 28 have no TAPP at all, so from the block's own inline
  `properties.ada:componentType` enums, which is what the reference registry reads.

The RESOLVED schema is never used for this. Every profile `$ref`s adaProduct's
universalComponentTypeBranch and the base file-type blocks, so resolution inlines the whole sealed
set: a walk finds 238 types with 225 "claimed" by ~74 profiles each. That is the universal enum,
not a collision, and a resolved-schema rule would select every profile for every record.

TIES ARE DECLARED, NOT RANKED
Technique profiles share one `exclusiveGroup`. Members that componentType cannot separate get
EQUAL priority, so the engine reports a tie and declares none -- the honest answer, and what the
reference registry does when it logs "asserting no technique profile". The LA/Solution ICP-MS
families are permanently in that state (the Mc/Q/Sf difference is procedure-side and never
reaches the file; see CLAUDE.md). `adaSEMFull` is the one genuine ranking: an UMBRELLA over the
SEM family, mirroring `schema_registry.UMBRELLA_PROFILES`, so it outranks its members.

COUNTS ARE SNAPSHOTS; RULES ARE NOT
The ADA corpus is edited while this runs -- "no product type" measured 12 records at 15:40 and 8
an hour later, moving the adaProduct exclusion from 11 to 7 with no rule change. Sidecars encode
rules, never counts.

    python tools/build_conformance_sidecars.py            # report
    python tools/build_conformance_sidecars.py --write
"""
import argparse
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_sources")
sys.path.insert(0, os.path.join(ROOT, "tools"))

VALIDATION_DIR = os.environ.get("CDIF_VALIDATION_DIR", r"C:\GithubC\CDIF\validation")
GEOCHEM_BASE = "https://w3id.org/geochem/metadata/profiles/"
CDIF = "https://w3id.org/cdif/%s/1.1"

#: CDIF block name -> the module URI composing it implies. One each: the modules are independent
#: classes with no `requires` of their own, so composing one implies exactly itself.
CDIF_MODULE = {
    "cdifCore": CDIF % "core",
    "cdifDiscovery": CDIF % "discovery",
    "cdifDataDescription": CDIF % "data_description",
    "cdifProvenance": CDIF % "provenance",
    "cdifManifest": CDIF % "manifest",
}

CID_RE = re.compile(re.escape(GEOCHEM_BASE) + r"([A-Za-z0-9_-]+)")
UMBRELLA = {"adaSEM"}            # mirrors schema_registry.UMBRELLA_PROFILES
# "The most specific (highest priority) wins" -- so an UMBRELLA, being the LEAST specific member
# of its family, ranks BELOW the specific profiles, not above. Set the other way round (20) it
# beat its own members: adaSEM shares BSEImage/EBSDMap/SEMEDSMap/SEMEDSSpectrum with
# adaSEMImaging and adaSEMComposition, so four examples declaring the specific profile were
# detected as the superset. The umbrella now wins only when nothing more specific matches, which
# is what a superset is for.
# Four tiers, and the order is the whole design:
#   LEGACY   3  a profile-ada block never beats a TAPP one
#   UMBRELLA 5  a superset is the LEAST specific of its family, so it loses to its own members
#               and wins only when nothing more specific matches
#   MEMBER  10  an ordinary TAPP technique profile
#   TAPP    15  the TAPP half of a forked pair, which supersedes its legacy twin
PRIORITY_LEGACY, PRIORITY_UMBRELLA, PRIORITY_MEMBER, PRIORITY_TAPP = 3, 5, 10, 15
GROUP = "geochem-technique"

#: Forked TECHNIQUE pairs: one technique with two generations under different cids, the TAPP
#: `profile/` and its legacy `profile-ada/` twin. Both match the same componentTypes, so at equal
#: priority they tie. Steve's call (2026-10-16): one label per technique, the NEW block wins, so
#: the TAPP member is ranked above its legacy twin and a record citing the legacy cid resolves to
#: the new profile.
#:
#: SEM IS DELIBERATELY EXCLUDED, because its cids are INVERTED relative to these five and the rule
#: would invert its meaning. Here the TAPP block holds the bare `ada<TECH>` that records actually
#: cite (adaXANES 245, adaVNMIR 183, adaXRD 66, adaQRIS 13, adaRAMAN 8) while the legacy holds
#: `ada<TECH>Full`, which ZERO records cite -- so ranking TAPP first resolves records to what they
#: already declare and migrates nothing. SEM is the other way round: TAPP = adaSEMFull (0 records)
#: and legacy = adaSEM (2,918). Applying the rule there would route the largest technique in the
#: corpus to a cid nothing cites. CLAUDE.md records the inversion; it needs its own decision,
#: either ranking adaSEM first or correcting the cid assignment so SEM matches these five.
#:
#: Note SEM already resolves to adaSEMFull regardless, because UMBRELLA gives it priority 20 --
#: a pre-existing consequence of mirroring schema_registry.UMBRELLA_PROFILES, not of this ranking.
FORKED_TECHNIQUE_DIRS = {"XANES", "QRIS", "RAMAN", "VNMIR", "XRD"}

# geochemProduct marks an analytical product: every one of the 7,447 ADA records carries
# prov:wasGeneratedBy, and a record without an analysis activity is not one.
GEOCHEMPRODUCT_ASK = (
    "ASK { ?d <http://www.w3.org/ns/prov#wasGeneratedBy> ?a }"
)
# adaProduct, per amds-ldeo/metadata commit 8470122: a record naming NO technique AND claiming NO
# ADA product type does not declare adaProduct. The EXCLUSION is the conjunction, so presence is
# the disjunction. Either half alone misroutes records whose metadata is merely incomplete -- the
# commit measured 14 moved by the technique half alone (including three ANGSA XCT collections that
# lost their technique name) and 12 by the product-type half alone (including a Murchison study
# whose additionalType is the placeholder 'specific type missing').
# The ADA marker is required too, and it is the schema's own answer rather than an invented one:
# gBB #136 made ada:submissionType a REQUIRED property of adaProduct, so a record without it
# cannot be an adaProduct whatever else it carries. Without this clause the geochemProduct fixture
# -- an ICP-MS product with no submissionType and no DataDeliveryPackage -- matched adaProduct on
# its measurementTechnique alone. It costs nothing on the ADA corpus, where all 7,447 records
# carry ada:submissionType (backfilled 2026-10-16), so commit 8470122's conjunction still decides
# which ADA records are excluded; this only keeps NON-ADA products out.
ADAPRODUCT_ASK = (
    "ASK {\n"
    "  ?d <https://ada.astromat.org/metadata/submissionType> ?st .\n"
    "  {\n"
    "    { ?d <http://schema.org/measurementTechnique> ?t .\n"
    "      ?t <http://schema.org/name> ?tn . FILTER (STR(?tn) != \"\") }\n"
    "    UNION\n"
    "    { ?d <http://schema.org/additionalType> ?pt . FILTER (isLiteral(?pt)) }\n"
    "  }\n"
    "}"
)


def universal_component_types():
    with io.open(os.path.join(SRC, "registry", "vocab", "componentType.json"),
                 encoding="utf-8") as fh:
        voc = json.load(fh)
    return {c["@id"] for c in voc.get("skos:hasTopConcept") or []
            if c.get("@id") and not c["@id"].startswith("nil:")}


def declared_cid(text):
    hits = sorted(set(CID_RE.findall(text)))
    return hits[0] if hits else None


def requires_from_allof(doc):
    out = []
    for branch in doc.get("allOf") or []:
        if not isinstance(branch, dict):
            continue
        ref = branch.get("$ref")       # a conditional branch has if/then, not $ref
        if not isinstance(ref, str):
            continue
        for name, uri in CDIF_MODULE.items():
            if "/%s/" % name in ref and uri not in out:
                out.append(uri)
    return out


def inline_component_enums(node, out):
    """componentType values stated inline in this schema -- the legacy blocks' only source.

    THREE shapes pin ada:componentType in this repository and all three must be read. Until
    2026-10-17 this read two of them, and the omission was invisible because a sidecar whose
    presence ASK is too NARROW still validates, still regenerates byte-identically, and still
    reports a plausible componentType list -- it simply fails to match records.

      enum: [a, b]              a profile's hasPart branch
      anyOf: [{const: a}, ...]  a detail block pinning several
      const: a                  a detail block pinning exactly ONE   <-- was dropped

    The bare const is the detail blocks' idiom when a block describes one component kind, and 8
    schemas use it: ARGT, DSC, EAIRMS, L2MS, NanoIR, PSFD and XRD under adaProfile/*/detail/,
    plus geochemProfile/XCT/detail-legacy/. Dropping it had two consequences worth recording,
    because both were reported as facts about the CORPUS before being traced to this function.

    PSFD was reported as "a profile that describes no distinguishing content" and skipped. It
    carries ada:PSFDTabular and produces a sidecar; the skip was this bug. Any count of
    "blocks with no discriminator" taken before this fix is an artefact.

    And the four legacy enum widenings in #149 -- ARGTDocument, DSCHeatTabular, NanoIRBackground,
    EAIRMSCollection added by hand to four profile schemas -- were unnecessary. Every one of those
    terms was ALREADY declared in the sibling detail block, ARGT's since 2026-08-14. The widenings
    were a symptom fix for this defect and are left in place only because a profile enum stating
    what it covers is independently correct.
    """
    if isinstance(node, dict):
        ct = node.get("properties", {}).get("ada:componentType")
        if isinstance(ct, dict):
            out.update(v for v in (ct.get("enum") or []) if isinstance(v, str))
            if isinstance(ct.get("const"), str):
                out.add(ct["const"])
            for b in ct.get("anyOf") or []:
                if isinstance(b, dict) and isinstance(b.get("const"), str):
                    out.add(b["const"])
        for v in node.values():
            inline_component_enums(v, out)
    elif isinstance(node, list):
        for v in node:
            inline_component_enums(v, out)


def _priority(cid, rec):
    """Rank within the technique exclusiveGroup.

    Equal priority is a declared TIE, which is the right answer when componentType genuinely
    cannot separate two members (the ICP-MS families). A higher rank is only correct where one
    member is the agreed winner: the adaSEMFull umbrella, and the five forked technique pairs
    where the TAPP generation supersedes its legacy twin.
    """
    # LEGACY first: a profile-ada block never outranks a TAPP one, whatever else it is. Without
    # this the renamed legacy SEM profile (adaSEMFull) sat at member rank and TIED with the
    # specific TAPP profiles adaSEMImaging and adaSEMComposition.
    if rec["kind"] == "technique" and rec["rel"].endswith("/profile-ada"):
        return PRIORITY_LEGACY
    if cid in UMBRELLA:
        return PRIORITY_UMBRELLA
    tech = rec["rel"].split("/")[2] if rec["kind"] == "technique" else None
    if tech in FORKED_TECHNIQUE_DIRS and rec["rel"].endswith("/profile"):
        return PRIORITY_TAPP
    return PRIORITY_MEMBER


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    import yaml
    import build_tapp
    import build_profile

    sys.path.insert(0, VALIDATION_DIR)
    try:
        from detect_conformance import build_component_presence_ask
    except ImportError as exc:
        print("ERROR: cannot import detect_conformance.build_component_presence_ask from %s (%s).\n"
              "The ASK is built by CDIF/validation deliberately -- this generator passes a\n"
              "componentType list and never hand-writes SPARQL. Set CDIF_VALIDATION_DIR."
              % (VALIDATION_DIR, exc), file=sys.stderr)
        return 2

    universal = universal_component_types()
    tapp_for_dir = {v["dir"]: t for t, v in getattr(build_profile, "PROFILES", {}).items()
                    if v.get("dir")}

    # --- collect every candidate block -----------------------------------------------------
    blocks = []                                   # (dir, relpath, kind)
    for name in ("geochemProduct", "adaProduct"):
        blocks.append((os.path.join(SRC, "BaseSchema", name), "BaseSchema/" + name, "base"))
    for fam in ("geochemProfile", "adaProfile"):
        base = os.path.join(SRC, "techniqueProfile", fam)
        if not os.path.isdir(base):
            continue
        for tech in sorted(os.listdir(base)):
            for variant in ("profile", "profile-ada"):
                d = os.path.join(base, tech, variant)
                if os.path.isfile(os.path.join(d, "schema.yaml")):
                    blocks.append((d, "techniqueProfile/%s/%s/%s" % (fam, tech, variant),
                                   "technique"))

    # --- first pass: cid, requires, component list -----------------------------------------
    recs = []
    for d, rel, kind in blocks:
        r_dir = d
        text = io.open(os.path.join(d, "schema.yaml"), encoding="utf-8").read()
        doc = yaml.safe_load(text) or {}
        cid = declared_cid(text) or os.path.basename(os.path.dirname(d))
        tech_dir = rel.split("/")[2] if kind == "technique" else None
        tapp = tapp_for_dir.get(tech_dir) if tech_dir else None
        comps, source = set(), None
        if kind == "technique":
            if tapp:
                comps = set(build_tapp.TAPP_CONFIGS.get(tapp, {}).get("component_types") or [])
                source = "TAPP_CONFIGS[%s]" % tapp
            # UNION with the inline enum, not a fall-through -- for the same reason the detail
            # read below is a union, which this line failed to follow until 2026-10-17.
            #
            # tapp_for_dir is keyed by the technique DIRECTORY, so BOTH SEM/profile and
            # SEM/profile-ada resolve to semTAPP. Taking the TAPP vocabulary and then skipping the
            # inline read because `comps` was non-empty gave the LEGACY block the CURRENT
            # generation's componentTypes and dropped its own. For adaSEMFull the two sets were
            # entirely DISJOINT -- 6 TAPP names against the 14 ADA names its schema declares -- so
            # its presence ASK could not match any of the 2,912 records that cite it. Reported by
            # the metadata forms session, which measured the overlap before wiring detection in.
            before_inline = len(comps)
            inline_component_enums(doc, comps)
            if len(comps) > before_inline:
                source = "inline enums" if not before_inline else (source + " + inline")
            # UNION with the detail block, not a fall-through. NanoSIMS shows why: its inline
            # enum names NanoSIMSImage, which ZERO records carry, while its detail block pins the
            # three types all 38 records actually use. Falling through only when inline is empty
            # would have left NanoSIMS detecting on the one value that never appears.
            if True:
                # THIRD source, and for the legacy adaProfile blocks it is the RIGHT one. Their
                # profile reaches components through `$ref: ../detail/schema.yaml` rather than an
                # inline enum, and those detail blocks are the hasPart-ITEM kind, which pins
                # ada:componentType -- unlike the geochemProfile detail blocks, where CLAUDE.md
                # measured 0 of 59 constraining it. Missing this read is what made ICPOES, LAF and
                # PSFD look like profiles with nothing to distinguish them.
                #
                # NanoSIMS is the proof that the detail block is authoritative rather than merely
                # another place to look: its detail pins Collection/ImageCollection/Tabular, which
                # is exactly what the 38 records carry, while the profile's inline NanoSIMSImage
                # appears in ZERO records. Widening the profile enum would have corrected the
                # wrong file.
                det = os.path.join(os.path.dirname(r_dir), "detail", "schema.yaml")
                if os.path.isfile(det):
                    before = len(comps)
                    inline_component_enums(yaml.safe_load(io.open(det, encoding="utf-8").read()),
                                           comps)
                    if len(comps) > before:
                        source = "detail block" if not before else (source + " + detail")
        recs.append(dict(dir=d, rel=rel, kind=kind, cid=cid, doc=doc,
                         comps=sorted(comps - universal), source=source,
                         requires=requires_from_allof(doc)))

    # --- one sidecar per DISTINCT conformsTo -----------------------------------------------
    # A forked cid (a TAPP profile/ and its legacy profile-ada/ twin both declaring it) must not
    # yield two classes with the same URI: the engine would see one class twice. The TAPP-based
    # block wins, being the current generation; the twin is skipped and reported.
    by_cid = {}
    for r in recs:
        prev = by_cid.get(r["cid"])
        if prev is None or (prev["rel"].endswith("profile-ada") and r["rel"].endswith("/profile")):
            by_cid[r["cid"]] = r
    forks = [c for c in by_cid if sum(1 for r in recs if r["cid"] == c) > 1]

    emitted = empty = 0
    for cid, r in sorted(by_cid.items()):
        if r["kind"] == "base":
            presence = GEOCHEMPRODUCT_ASK if cid.endswith("geochemProduct") else ADAPRODUCT_ASK
            requires = ([] if cid.endswith("geochemProduct")
                        else [GEOCHEM_BASE + "geochemProduct"])
            if cid.endswith("geochemProduct"):
                requires = r["requires"]
            sidecar = {"conformsTo": GEOCHEM_BASE + cid, "presence": presence,
                       "validityShapes": None, "requires": requires}
        else:
            if not r["comps"]:
                empty += 1
                print("  SKIP  %-56s no discriminating componentType (%s)"
                      % (r["rel"], r["source"] or "no source"))
                continue
            sidecar = {
                "conformsTo": GEOCHEM_BASE + cid,
                "presence": build_component_presence_ask(r["comps"]),
                "validityShapes": None,
                "requires": [GEOCHEM_BASE + "adaProduct"],
                "exclusiveGroup": GROUP,
                "priority": _priority(cid, r),
            }
        emitted += 1
        if a.write:
            with io.open(os.path.join(r["dir"], "conformance.json"), "w",
                         encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(sidecar, indent=2, ensure_ascii=False) + "\n")

    print("\nblocks scanned            : %d" % len(recs))
    print("distinct conformsTo cids  : %d" % len(by_cid))
    print("  forked (twin skipped)   : %d  %s" % (len(forks), ", ".join(sorted(forks)[:6])))
    print("sidecars %-16s : %d" % ("written" if a.write else "would write", emitted))
    print("skipped, no discriminator : %d" % empty)
    if not a.write and emitted:
        print("\nnothing written; pass --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
