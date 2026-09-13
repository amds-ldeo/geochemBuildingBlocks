"""Build a path-driven geochem product profile for a TAPP, mirroring geochemProfiles/LA-ICPMS:

  geochemProfiles/<dir>/schema.yaml =
    allOf:[ adaProduct,
            detail<SHORT> (the schema:Dataset analysis-instance overlay),
            { prov:wasGeneratedBy.prov:used narrowed to the <tapp> definition,
              schema:additionalType contains a technique product-type enum,
              schema:distribution.hasPart.items componentType enum (technique-specific),
              schema:subjectOf.dcterms:conformsTo contains the profile @id } ]

The componentType enum comes from the TAPP's CFG (build_tapp.TAPP_CONFIGS[...]["component_types"]).
The example is synthesised by overlaying the technique's detail -P0 (which satisfies the detail
overlay) onto the adaProduct scaffolding of the LA-ICPMS example, then swapping the technique-specific
componentType / additionalType / conformsTo.

    python tools/build_profile.py <tapp>              # e.g. semTAPP
    python tools/build_profile.py <tapp> --validate
"""
import copy
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPROF = os.path.join(ROOT, "_sources", "techniqueProfile", "geochemProfile")
# Scaffold for _example(): a valid, structurally-complete product example (bundle distribution
# with schema:hasPart, prov:wasGeneratedBy, instrument). The retargeting below swaps the
# technique-specific bits. Was LA-ICPMS/profile/exampleadaICPMS.json, retired in the LA split;
# now the canonical adaProduct example, which is technique-neutral apart from a componentType
# the retargeting overwrites.
LAI = os.path.join(ROOT, "_sources", "BaseSchema", "adaProduct", "exampleadaProduct.json")


def _profile_dir(tapp):
    return os.path.join(TPROF, b.TECH_DIR[tapp], "profile")

# per-TAPP profile config: dir name, detail short, conformsTo @id, additionalType product strings,
# titles. componentType enum is pulled from the TAPP CFG at build time.
PROFILES = {
    "labxctTAPP": dict(dir="Lab-XCT", short="LABXCT", cid="adaLabXCT",
        addtype=["X-ray Computed Tomography (XCT) Image Collection", "X-ray computed tomography"],
        title="ADA Lab-XCT Product Profile"),
    "semImagingTAPP": dict(dir="SEM-Imaging", short="SEMIMAGING", cid="adaSEMImaging",
        addtype=["Scanning Electron Microscopy (SEM) Image", "Scanning electron microscopy"],
        title="ADA SEM Imaging Product Profile"),
    "semFibsemTAPP": dict(dir="SEM-FIBSEM", short="SEMFIBSEM", cid="adaSEMFIBSEM",
        addtype=["Focused ion beam-scanning electron microscopy", "Scanning electron microscopy"],
        title="ADA FIB-SEM Product Profile"),
    "semCompositionTAPP": dict(dir="SEM-Composition", short="SEMCOMPOSITION", cid="adaSEMComposition",
        addtype=["Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS) Point Data",
                 "Scanning electron microscopy"],
        title="ADA SEM Composition (EDS/WDS) Product Profile"),
    "semTAPP": dict(dir="SEM", short="SEM", cid="adaSEMFull",
        addtype=["Scanning Electron Microscopy (SEM) Image", "Scanning electron microscopy",
                 "Focused ion beam-scanning electron microscopy"],
        title="ADA SEM (superset) Product Profile"),
    "solutionQicpmsTAPP": dict(dir="Solution-Q-ICPMS", short="SOLUTIONQICPMS", cid="adaSolutionQICPMS",
        addtype=["Quadrupole Inductively Coupled Plasma Mass Spectrometry (QICPMS) Processed",
                 "Quadrupole Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA Solution Q-ICP-MS Product Profile"),
    "solutionSficpmsTAPP": dict(dir="Solution-SF-ICPMS", short="SOLUTIONSFICPMS", cid="adaSolutionSFICPMS",
        addtype=["High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed",
                 "High-resolution inductively coupled plasma mass spectrometry"],
        title="ADA Solution SF-ICP-MS Product Profile"),
    # --- Laser-ablation and Solution MC profiles (added 2026-08-21) ------------------------------
    # addtype[0] is written into the generated example's schema:additionalType, so every value here
    # must already exist in adaProduct's controlled list - these are taken from it verbatim, not
    # coined. NOTE: that list has no laser-ablation MC product string, so LA-MC and Solution-MC both
    # take the generic MCICPMS one; they stay distinct by conformsTo, componentType and detail.
    "laQicpmsTAPP": dict(dir="LA-Q-ICPMS", short="LAQICPMS", cid="adaLAQICPMS",
        addtype=["Laser Ablation Inductively coupled plasma mass spectrometry",
                 "Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry (LAQICPMS) Processed", "Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-Q-ICP-MS Product Profile"),
    "laSficpmsTAPP": dict(dir="LA-SF-ICPMS", short="LASFICPMS", cid="adaLASFICPMS",
        addtype=["Laser Ablation Inductively coupled plasma mass spectrometry",
                 "Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry (LASFICPMS) Processed", "Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-SF-ICP-MS Product Profile"),
    "laMcicpmsTAPP": dict(dir="LA-MC-ICPMS", short="LAMCICPMS", cid="adaLAMCICPMS",
        # addtype[0] is what the generated example declares, so it should be a value real
        # records of this technique carry. "Multi-Collector Inductively Coupled Plasma Mass
        # Spectrometry" is on 90 published records; the laser-ablation string is on 8 and is
        # no more specific to MC, so it stays in the enum but not at the head.
        addtype=["Multi-Collector Inductively Coupled Plasma Mass Spectrometry",
                 "Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) processed", "Laser Ablation Inductively coupled plasma mass spectrometry", "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-MC-ICP-MS Product Profile"),
    "laQicpmsUPbTAPP": dict(dir="LA-Q-ICPMS-UPb", short="LAQICPMSUPB", cid="adaLAQICPMSUPb",
        addtype=["Laser Ablation Inductively coupled plasma mass spectrometry",
                 "Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry (LAQICPMS) Processed", "Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-Q-ICP-MS U-Pb Geochronology Product Profile"),
    "laSficpmsUPbTAPP": dict(dir="LA-SF-ICPMS-UPb", short="LASFICPMSUPB", cid="adaLASFICPMSUPb",
        addtype=["Laser Ablation Inductively coupled plasma mass spectrometry",
                 "Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry (LASFICPMS) Processed", "Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-SF-ICP-MS U-Pb Geochronology Product Profile"),
    "laMcicpmsUPbTAPP": dict(dir="LA-MC-ICPMS-UPb", short="LAMCICPMSUPB", cid="adaLAMCICPMSUPb",
        # addtype[0] is what the generated example declares, so it should be a value real
        # records of this technique carry. "Multi-Collector Inductively Coupled Plasma Mass
        # Spectrometry" is on 90 published records; the laser-ablation string is on 8 and is
        # no more specific to MC, so it stays in the enum but not at the head.
        addtype=["Multi-Collector Inductively Coupled Plasma Mass Spectrometry",
                 "Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) processed", "Laser Ablation Inductively coupled plasma mass spectrometry", "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-MC-ICP-MS U-Pb Geochronology Product Profile"),
    # EPMA and TEM predate the generator: EPMA already has a hand-made profile/ (cid adaEMPA, kept
    # verbatim so its published conformsTo URI does not move) and TEM has none yet. Adding them here
    # brings both under the generator, so a technique regen keeps its profile in step with its own
    # detail and tapp - EPMA's profile had gone stale against them precisely because it was skipped.
    "empaTAPP": dict(dir="EMPA", short="EMPA", cid="adaEMPA",
        # adaProduct's controlled list pairs each technique: a Title Case name carrying the
        # acronym, and a sentence-case name without it. 19 of the 20 multi-value profiles here
        # carry both halves. EMPA carried two ACRONYM forms instead -- two products -- and never
        # picked up its sentence-case partner, which is the value every published ADA EMPA record
        # actually writes. Without it the profile rejects its own records.
        addtype=["Electron Microprobe Analysis (EMPA)",
                 "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
                 "Electron microprobe analysis"],
        title="ADA EPMA Product Profile"),
    "temTAPP": dict(dir="TEM", short="TEM", cid="adaTEM",
        addtype=["Transmission Electron Microscopy",
                 "Scanning Transmission Electron Microscopy (STEM) Image",
                 "Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy "
                 "(STEMEDS) Tabular"],
        title="ADA TEM Product Profile"),
    "solutionMcicpmsTAPP": dict(dir="Solution-MC-ICPMS", short="SOLUTIONMCICPMS", cid="adaSolutionMCICPMS",
        addtype=["Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) processed", "Multi-Collector Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA Solution MC-ICP-MS Product Profile"),

    # --- TEMPLATES: the thirteen techniques with no product-type labels anywhere -------------
    # Every draft needs a PROFILES entry to get a geochem profile (geochemProduct + the technique
    # tapp + its detail). Thirty of the forty-three already have labels to harvest -- in
    # generate_profiles.PROFILES, or baked into a profile-ada/schema.yaml on disk. These thirteen
    # have neither, and `addtype` is a curation decision about what a technique's PRODUCTS are
    # called, not something derivable from the TAPP. So it is left EMPTY on purpose: build() skips
    # a template rather than emitting `contains: {enum: []}`, which matches nothing.
    #
    # dir/short/cid/title follow the conventions above. The raw material for each addtype is on the
    # comment line: the technique's own declared full name, then its component_types, which say
    # what product kinds exist. Compare the shape already in use, e.g. XRD:
    #     ["X-ray Diffraction (XRD) Tabular", "X-ray diffraction"]
    "capdTAPP": dict(dir="CAPD", short="CAPD", cid="adaCAPD", addtype=["Capacitance Dilatometry",
                 "Capacitance Dilatometry (CAPD)"],
        title="ADA Capacitance Dilatometry Product Profile"),                    # Capacitance Dilatometry | CAPDRawTabular
    "cpdTAPP": dict(dir="CPD", short="CPD", cid="adaCPD", addtype=["Curation Photo-Documentation",
                 "Curation Photo-Documentation (CPD)"],
        title="ADA Curation Photo-Documentation Product Profile"),                     # Curation Photo-Documentation | CPDImage
    "dssmTAPP": dict(dir="DSSM", short="DSSM", cid="adaDSSM", addtype=["Direct Shear Strength Measurement",
                 "Direct Shear Strength Measurement (DSSM)"],
        title="ADA Direct Shear Strength Product Profile"),                    # Direct Shear Strength Measurement | DSSMTabular, UCSTabular
    "finesseTAPP": dict(dir="FINESSE", short="FINESSE", cid="adaFINESSE", addtype=["Stepped Heating Carbon and Nitrogen Isotopic Compositions",
                 "Elemental Analyzer Stepped Heating C N Isotope (FINESSE)"],
        title="ADA FINESSE Product Profile"),                 # Stepped Heating Carbon and Nitrogen Isotopic Compositions | FINESSECollection, FINESSETabular
    "gcCIrmsTAPP": dict(dir="GC-C-IRMS", short="GCCIRMS", cid="adaGCCIRMS",
                        # "icMsTAPP (GCCIRMS)" was a TAPP key leaked into a human-readable
                        # label -- and the wrong TAPP's key at that. Removed. The published
                        # value, already named in the trailing comment below, was missing.
                        addtype=["Gas Chromatography-Combustion-Isotopic Ratio Mass Spectrometry",
                                 "Combustion gas chromatography isotopic ratio mass spectrometry",
                                 "C-GC-IR-MS"],
        title="ADA GC-C-IRMS Product Profile"),               # Gas Chromatography-Combustion-Isotopic Ratio Mass Spectrometry | GCCIRMSDataCollection, GCCIRMSOrbitrapCollection, GCCIRMSTabularIsotopicValues
    # Neither previous value matched a published record. "Ion Chromatography-Mass Spectrometry"
    # (47 records) and "Ion Chromatography" (12) are the spellings in use. LC-MS is kept on the
    # reviewer's reading that ion chromatography IS liquid chromatography -- but note ADA treats
    # LC-MS as a technique of its own (ada:LCMSCollection, 75 records) with no profile, so those
    # records will now validate here.
    "icMsTAPP": dict(dir="IC-MS", short="ICMS", cid="adaICMS", addtype=["Ion Chromatography-Mass Spectrometry",
                                                                        "Ion Chromatography-Mass Spectrometry (ICMS)",
                                                                        "Ion Chromatography",
                                                                        "Liquid Chromatography-Mass Spectrometry"],
        title="ADA Ion Chromatography-Mass Spectrometry Product Profile"),                   # Ion Chromatography-Mass Spectrometry | ICMSCollection
    "niMiTAPP": dict(dir="NI-MI", short="NIMI", cid="adaNIMI", addtype=["Nanoindentation and Microindentation",
                 "Nanoindentation and microindentation (NI-MI)"],
        title="ADA NI-MI Product Profile"),                   # Nanoindentation and Microindentation | NIMICollection
    "pcdAfmTAPP": dict(dir="PCD-AFM", short="PCDAFM", cid="adaPCDAFM", addtype=["Particle cohesion determination with AFM",
                 "Particle cohesion determination with AFM (PCDAFM)"],
        title="ADA PCD-AFM Product Profile"),                 # Particle cohesion determination with AFM | PCDAFMCollection
    "sXrfTAPP": dict(dir="S-XRF", short="SXRF", cid="adaSXRF",
                     # "Synchrotron" was misspelled two different ways here, "Synchroton" and
                     # "Synchotron". Neither variant is used by any published record, so
                     # correcting them is safe. The value 325 S-XRF records actually carry --
                     # already named in the trailing comment below -- was missing.
                     addtype=["Synchrotron-based X-ray Fluorescence Spectroscopy",
                              "Synchrotron-based X-ray Fluorescence Spectroscopy (S-XRF)",
                              "Synchrotron X-ray fluorescence spectrometry",
                              "Synchrotron X-Ray Fluorescence Analysis", "SYNCHXRF"],
        title="ADA S-XRF Product Profile"),                   # Synchrotron-based X-ray Fluorescence Spectroscopy | SXRF2DImage, SXRFPointTabular
    "semClTAPP": dict(dir="SEM-CL", short="SEMCL", cid="adaSEMCL", addtype=["Scanning electron microscopy",
                 "SEM Cathodoluminescence Spectroscopy (SEMCL)"],
        title="ADA SEM-CL Product Profile"),                  # SEM Cathodoluminescence Spectroscopy | SEMHRCLTabular, SEMHRCLCube
    "sthmAfmTAPP": dict(dir="STHM-AFM", short="STHMAFM", cid="adaSTHMAFM", addtype=["Scanning Thermal Microscopy with AFM",
                 "Scanning Thermal Microscopy with AFM (STHMAFM)"],
        title="ADA STHM-AFM Product Profile"),                # Scanning Thermal Microscopy with AFM | SThMCollection
    "tdmTAPP": dict(dir="TDM", short="TDM", cid="adaTDM", addtype=["Temperature-Dependent Magnetization",
                 "Temperature-Dependent Magnetization (TDM)"],
        title="ADA TDM Product Profile"),                     # Temperature-Dependent Magnetization | TDMRawTabular
    "timsTAPP": dict(dir="TIMS", short="TIMS", cid="adaTIMS", addtype=["Thermal ionization mass spectrometry",
                 "Thermal ionization mass spectrometry (TIMS)"],
        title="ADA TIMS Product Profile"),                    # Thermal ionization mass spectrometry | TIMSProcessedTabular, TIMSRawCollection
}

CID_BASE = "https://w3id.org/geochem/metadata/profiles/"


def _schema(tapp, cfg):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": cfg["title"],
        "description": (f"Path-driven technique-specific profile for {cfg['title']}. Extends the base ADA "
                        f"product profile with the {cfg['short']} analysis-instance detail on the "
                        f"schema:Dataset root, narrows prov:used to the {tapp} protocol, and constrains "
                        f"valid component types on schema:distribution.hasPart."),
        "allOf": [
            {"$ref": "../../../../BaseSchema/geochemProduct/schema.yaml"},
            {"$ref": "../detail/schema.yaml"},
            {"type": "object", "properties": {
                "prov:wasGeneratedBy": {
                    "description": (f"Pin the {tapp} definition and the instrument where prov:used carries them. "
                                    f"Constraint-only if/then, never a narrowed anyOf: prov:used items are "
                                    f"role-keyed wrappers, and an anyOf here would allOf-merge with the base "
                                    f"union and exclude item shapes the base allows."),
                    "type": "array",
                    "items": {"type": "object", "properties": {"prov:used": {"type": "array", "items": {"allOf": [
                        {"if": {"type": "object", "required": ["schema:instrument"]},
                         "then": {"properties": {"schema:instrument": {
                             "type": "array", "minItems": 1,
                             "items": {"$ref": "../../../../BaseSchema/instrument/schema.yaml"}}}}},
                        {"if": {"type": "object",
                                "properties": {"@type": {"contains": {"const": "ada:TAPPDefinition"}}},
                                "required": ["@type"]},
                         "then": {"$ref": "../tapp/schema.yaml"}}]}}}}},
                "schema:additionalType": {
                    "description": f"Must include a {cfg['short']} product type identifier.",
                    "contains": {"enum": cfg["addtype"]}},
                # NO schema:distribution / ada:componentType constraint here. componentType is a
                # controlled VOCABULARY referenced by annotation (schema:inDefinedTermSet ->
                # ada:vocab/componentType), deliberately not a hard JSON-Schema enum -- adaProduct
                # says so in as many words ("conformance is advisory ... not hard-enumerated in
                # JSON Schema"), and check_componentType.py exists precisely to enforce it outside
                # JSON Schema. Emitting `required: [ada:componentType]` plus an enum here
                # contradicted both, and made every geochem technique profile demand an ADA-specific
                # property -- wrong for the general drafts, which carry geochemProduct + tapp +
                # detail and should not require an ADA file classification.
                #
                # Dropped whole rather than enum-only: without the enums the monolithic branch
                # degenerates to {"type": "object"}, which matches everything, so the anyOf becomes
                # vacuously true. A clause that constrains nothing while looking like enforcement is
                # worse than no clause -- the same trap an unresolvable $ref sets when it resolves
                # to {}.
                "schema:subjectOf": {"properties": {"dcterms:conformsTo": {"contains": {
                    "type": "object", "properties": {"@id": {"const": CID_BASE + cfg["cid"]}}}}}},
            }},
        ],
    }


def _swap_tapp(node, tapp):
    """Retarget any @id that references laicpmsTAPP (the template's TAPP) to this TAPP."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "@id" and isinstance(v, str) and "laicpmsTAPP" in v:
                node[k] = v.replace("laicpmsTAPP", tapp)
            else:
                _swap_tapp(v, tapp)
    elif isinstance(node, list):
        for v in node:
            _swap_tapp(v, tapp)


def _example(tapp, cfg, component_types):
    """Base the example on the adaProduct-compliant LA-ICPMS example (which satisfies adaProduct + the
    generic CDIF-slot shapes the detail overlays also require), then graft the technique-specific bits:
    componentType, additionalType, conformsTo, the TAPP linkage, and the target detail's required
    ada: props + dqv measurement (copied from that detail's own -P0, which carries valid values)."""
    b.configure(tapp)
    lai = json.load(open(LAI, encoding="utf-8"))
    det = json.load(open(os.path.join(TPROF, b.TECH_DIR[tapp], "detail",
                                      f"exampledetail{cfg['short']}-P0.json"), encoding="utf-8"))
    ex = copy.deepcopy(lai)                       # adaProduct-compliant scaffolding + generic detail slots
    ex["@id"] = f"ex:{cfg['cid']}-example-001"
    ex["@type"] = ["schema:Dataset", "schema:Product"]
    # graft the technique's REQUIRED direct ada: props + its dqv measurement from the detail -P0
    for k, v in det.items():
        if k.startswith("ada:") or k == "dqv:hasQualityMeasurement":
            ex[k] = copy.deepcopy(v)
    # the profile requires a schema:contributor with the analyst role; keep the scaffold's full
    # CDIF schema:Role structure but retarget its role from principal-investigator to analyst.
    for c in ex.get("schema:contributor", []):
        if isinstance(c, dict) and "schema:roleName" in c:
            c["schema:roleName"] = "analyst"
            break
    # retarget the TAPP linkage (measurementTechnique + prov:used @id refs) to this TAPP
    _swap_tapp(ex.get("schema:measurementTechnique"), tapp)
    _swap_tapp(ex.get("prov:wasGeneratedBy"), tapp)
    ex["schema:name"] = f"{cfg['title'].replace(' Product Profile','')} Example Product"
    ex["schema:description"] = (f"Example path-driven {cfg['short']} product record: dataset-level analysis "
                                f"detail plus technique component types on distribution.hasPart. Mock data.")
    ex["schema:additionalType"] = [cfg["addtype"][0], "ada:DataDeliveryPackage"]
    # The scaffolding is the LA-ICPMS example, so its prov:used instrument is an ICPMS. Retarget it
    # to whatever THIS technique's detail selects on, or every profile example claims an ICP-MS --
    # an EPMA record asserting it used a mass spectrometer. A laser-ablation technique legitimately
    # names two (Laser Ablation System + ICPMS); both go on the one instrument, which is what
    # satisfies a `contains` per token.
    _retarget_instrument(ex, _instrument_tokens(tapp))
    # swap distribution componentType -> this technique's first componentType, and mark each
    # BUNDLE distribution (one with schema:hasPart) as a schema:Collection so it is recognized as
    # an archive and held to the manifest profile (symmetric with the monolithic cdi:PhysicalDataSet).
    for dist in ex.get("schema:distribution", []):
        if "schema:hasPart" in dist:
            at = dist.setdefault("@type", [])
            if "schema:Collection" not in at:
                at.append("schema:Collection")
        for hp in dist.get("schema:hasPart", []):
            if isinstance(hp, dict):
                if "ada:componentType" in hp:
                    hp["ada:componentType"] = component_types[0]
                # the scaffold classifies a member via schema:additionalType too (e.g. the
                # generic componentType vocab); retarget it to this technique's componentType so
                # no scaffold-technique token leaks through.
                if isinstance(hp.get("schema:additionalType"), list):
                    hp["schema:additionalType"] = [component_types[0]]
    # conformsTo: retarget technique @id (keep adaProduct + cdif classes), dedupe
    so = ex.get("schema:subjectOf")
    if isinstance(so, dict):
        ct = so.get("dcterms:conformsTo", [])
        ids = {x.get("@id") for x in ct if isinstance(x, dict)}
        # drop any prior technique-profile @id (keep adaProduct + cdif), then add ours
        ct = [x for x in ct if not (isinstance(x, dict) and x.get("@id", "").startswith(CID_BASE)
                                    and not x.get("@id", "").endswith(("/adaProduct", "/geochemProduct")))]
        # geochemProfile profiles are based on geochemProduct: the record must declare that base
        # profile (the generic scaffold only declares adaProduct).
        for pid in (CID_BASE + "geochemProduct", CID_BASE + cfg["cid"]):
            if not any(isinstance(x, dict) and x.get("@id") == pid for x in ct):
                ct.append({"@id": pid})
        so["dcterms:conformsTo"] = ct
    _add_required_variables(ex, tapp, cfg)
    _fill_required(ex, tapp)
    return ex


def _fill_required(ex, tapp):
    """Sentinel the required properties a generated profile example cannot know.

    Delegates to build_tapp_examples.fill_nested_required -- the SAME pass the tapp/ and detail/
    examples already get (80f696008). This module used to carry its own parallel version, which
    was worse in ways that commit had already found and fixed: it stubbed a required object from a
    hardcoded HowTo shape instead of building the smallest instance the schema accepts, and it set
    @type itself, which breaks array cardinality -- @type and @id are structural, not transcription
    gaps, and belong to the typing pass that runs after the fill.

    Why profile/ examples were missed: fill_nested_required covers what build_tapp_examples writes,
    and profile/ examples are generated here instead.

    JTYPE_BY_PROP is populated from the workbook during that tool's own run, so it is empty here.
    That only costs the URI sentinel hint; sentinel_by_jtype falls back to the schema otherwise.
    """
    path = os.path.join(_profile_dir(tapp), "resolvedSchema.json")
    if not os.path.exists(path):
        return 0                    # first build: resolve, then re-run to pick these up
    sch = json.load(open(path, encoding="utf-8"))
    import build_tapp_examples as bte
    import schema_path_example_emitter as spe
    n = bte.fill_nested_required(ex, sch, bte.JTYPE_BY_PROP)
    n += bte.sentinel_pinned_members(ex, sch)
    spe.fill_required_types(ex, sch)   # re-type what the fill created
    return n


def _add_required_variables(ex, tapp, cfg):
    """Add the reported-property variables the profile `contains`-requires.

    A Basic-tier reported property is required like any other Basic field, so the emitter gives it a
    hard `contains` on schema:variableMeasured. The scaffold example carries only generic dataset
    variables (measurement_value, position_x), which satisfy the array's item constraints but not
    those `contains` clauses.

    Build each variable from the `contains` schema ITSELF. That schema is the analysis VALUE form
    (schema:PropertyValue) and carries every const the instance must match - unlike the sibling
    items.anyOf branches, which at the dataset root are the $MethodDefinition TEMPLATE forms
    (schema:PropertyValueSpecification) and would produce a variable that fails the base shape.

    The const-pinned fields are overlaid onto a clone of a variable the scaffold already carries, so
    the result also satisfies the base CDIF variable shape (schema:description and friends) without
    restating it here."""
    path = os.path.join(_profile_dir(tapp), "resolvedSchema.json")
    if not os.path.exists(path):
        return                      # first build: resolve, then re-run to pick these up
    sch = json.load(open(path, encoding="utf-8"))

    required = {}                   # name -> the contains schema that pins it

    def walk(node, key=""):
        if isinstance(node, dict):
            if key == "schema:variableMeasured":
                for a in (node.get("allOf") or []):
                    c = a.get("contains")
                    if not isinstance(c, dict):
                        continue
                    nm = ((c.get("properties") or {}).get("schema:name") or {}).get("const")
                    if not nm:
                        continue
                    # A name can be pinned twice: the $MethodDefinition TEMPLATE form
                    # (schema:PropertyValueSpecification, e.g. detectionLimitDefault) and the
                    # $Dataset VALUE form. A profile example is a dataset record, and only the value
                    # form satisfies the base variable shape - so the value form always wins.
                    t = ((c.get("properties") or {}).get("@type") or {}).get("const") or []
                    is_value = "schema:PropertyValue" in (t if isinstance(t, list) else [t])
                    if nm not in required or is_value:
                        if nm in required and not is_value:
                            continue
                        required[nm] = c
            for k, v in node.items():
                walk(v, k)
        elif isinstance(node, list):
            for v in node:
                walk(v, key)

    walk(sch)
    vm = ex.get("schema:variableMeasured") or []
    if not required or not vm:
        return
    template = vm[0]
    have = {v.get("schema:name") for v in vm if isinstance(v, dict)}

    for nm, c in required.items():
        if nm in have:
            continue
        var = copy.deepcopy(template)
        var["schema:description"] = "%s reported for this dataset. Example value." % nm
        var.pop("schema:alternateName", None)
        for k, v in (c.get("properties") or {}).items():
            if isinstance(v, dict) and "const" in v:
                var[k] = copy.deepcopy(v["const"])
        var.setdefault("schema:name", nm)
        var["@id"] = var.get("@id") if isinstance(var.get("@id"), str) else "ex:var"
        ex.setdefault("schema:variableMeasured", []).append(var)


def _example_monolithic(ex, cfg, component_types):
    """Derive a MONOLITHIC single-file variant from the bundle example `ex`: one schema:DataDownload
    (typed cdi:PhysicalDataSet) that IS the dataset, carrying ada:componentType + cdi:isStructuredBy,
    with no schema:hasPart. Not an archive, so manifest/1.1 is dropped from conformsTo and
    data_structure/1.1 added."""
    m = copy.deepcopy(ex)
    m["@id"] = f"ex:{cfg['cid']}-monolithic-001"
    m["schema:name"] = m.get("schema:name", cfg["title"]) + " (single-file dataset)"
    m["schema:description"] = (f"Monolithic single-file {cfg['short']} dataset: one schema:DataDownload that "
                               f"is the dataset, with ada:componentType and cdi:isStructuredBy on the "
                               f"distribution and no schema:hasPart. Mock data.")
    # structure components reference the example's measured variables where available
    comps = []
    for i, v in enumerate((m.get("schema:variableMeasured") or [])[:2]):
        if not isinstance(v, dict):
            continue
        comp = {"@type": ["cdi:MeasureComponent" if i == 0 else "cdi:DimensionComponent"],
                "cdif:name": [v.get("schema:name", f"component_{i}")]}  # cdif:name is array-valued
        if v.get("@id"):
            # cdif:isDefinedBy_Variable, NOT _RepresentedVariable: upstream CDIF renamed it on
            # data structure components (which these are) because the old name implied only the
            # superclass was allowed, while an InstanceVariable satisfies it too. The same-named
            # property on cdifInstanceVariable was deliberately NOT renamed and means something
            # narrower, so this is not a global search-and-replace. It is `required` on every
            # component, so the old name fails validation outright.
            comp["cdif:isDefinedBy_Variable"] = {"@id": v["@id"]}
        comps.append(comp)
    if not comps:
        comps = [{"@type": ["cdi:MeasureComponent"], "cdif:name": ["measurement_value"]}]
    m["schema:distribution"] = [{
        "@type": ["schema:DataDownload", "cdi:PhysicalDataSet"],
        "schema:name": f"{cfg['cid']}-monolithic.dat",
        "schema:description": f"Single {cfg['short']} data file (the whole dataset).",
        "schema:contentUrl": f"https://astromat.org/downloads/{cfg['cid']}-monolithic-001.dat",
        "schema:encodingFormat": ["application/x-hdf5"],
        "spdx:checksum": {"@type": ["spdx:Checksum"], "spdx:algorithm": "SHA256",
                          "spdx:checksumValue": "c3d4e5f6" * 8},
        "schema:size": {"@type": ["schema:QuantitativeValue"], "schema:value": 1048576, "schema:unitText": "byte"},
        "ada:componentType": component_types[0],
        "cdi:isStructuredBy": {
            "@id": f"ex:{cfg['cid']}-struct-001",
            "@type": ["cdi:DimensionalDataStructure"],
            "schema:name": f"{cfg['short']} single-file data structure",
            "cdi:has_DataStructureComponent": comps}}]
    so = m.get("schema:subjectOf")
    if isinstance(so, dict):
        so = copy.deepcopy(so)
        so["@id"] = f"ex:{cfg['cid']}-monolithic-metadata-001"
        so["schema:about"] = {"@id": m["@id"]}
        ct = [x for x in so.get("dcterms:conformsTo", [])
              if not (isinstance(x, dict) and x.get("@id") == "https://w3id.org/cdif/manifest/1.1")]
        if not any(isinstance(x, dict) and x.get("@id") == "https://w3id.org/cdif/data_structure/1.1" for x in ct):
            ct.append({"@id": "https://w3id.org/cdif/data_structure/1.1"})
        so["dcterms:conformsTo"] = ct
        m["schema:subjectOf"] = so
    return m


def _bblock(cfg):
    return {"$schema": "metaschema.yaml", "name": cfg["title"],
            "abstract": f"Path-driven ADA product profile for {cfg['title']}.",
            "status": "under-development", "dateTimeAddition": "2026-08-04T00:00:00Z",
            "itemClass": "schema", "register": "cdif-building-block-register", "version": "0.1",
            "dateOfLastChange": "2026-08-04", "link": "https://github.com/amds-ldeo/geochemBuildingBlocks",
            "maturity": "draft", "scope": "unstable",
            "tags": ["ada", "astromat", "profile", "geochem", "path-driven"]}


def _examples_yaml(cfg):
    return ("- title: " + cfg["title"] + " Example\n"
            "  content: |-\n"
            f"    Example path-driven {cfg['short']} product record with dataset-level analysis detail\n"
            "    and technique component types on the archive distribution. Mock data for validation.\n"
            "  prefixes:\n    schema: http://schema.org/\n    ada: https://ada.astromat.org/metadata/\n"
            "    cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/\n    prov: http://www.w3.org/ns/prov#\n"
            "    dcterms: http://purl.org/dc/terms/\n  snippets:\n    - language: json\n"
            f"      ref: example{cfg['cid']}.json\n")


def _bundled(node):
    """schema.yaml -> OGC bundled *Schema.json form: each `$ref X/schema.yaml` -> `X/<lastseg>Schema.json`."""
    import re
    if isinstance(node, dict):
        return {k: (re.sub(r'([^/"#]+)/schema\.yaml', r'\1/\1Schema.json', v)
                    if k == "$ref" and isinstance(v, str) else _bundled(v)) for k, v in node.items()}
    if isinstance(node, list):
        return [_bundled(v) for v in node]
    return node


def _instrument_tokens(tapp):
    """The schema:additionalType tokens this technique's detail requires on a prov:used instrument.

    Read from the generated detail schema rather than a second hand-maintained table, so the example
    cannot drift from the constraint it has to satisfy."""
    import yaml
    d = os.path.join(TPROF, b.TECH_DIR[tapp], "detail", "schema.yaml")
    if not os.path.exists(d):
        return []
    doc = yaml.safe_load(open(d, encoding="utf-8"))
    toks, seen = [], set()

    def walk(n, under_instr):
        if isinstance(n, dict):
            for k, v in n.items():
                # a sub-component (Torch, ICP Source, ...) is typed on schema:hasPart, not on the
                # instrument itself, so its subtree contributes no instrument-level token
                if k == "schema:hasPart":
                    continue
                if under_instr and k == "schema:additionalType" and isinstance(v, dict):
                    c = v.get("contains")
                    if isinstance(c, dict) and isinstance(c.get("const"), str) and c["const"] not in seen:
                        seen.add(c["const"]); toks.append(c["const"])
                walk(v, under_instr or k == "schema:instrument")
        elif isinstance(n, list):
            for v in n:
                walk(v, under_instr)

    walk(doc, False)
    return toks


def _retarget_instrument(ex, tokens):
    """Put `tokens` on every prov:used instrument, replacing the scaffolding's own technique token."""
    if not tokens:
        return
    keep_prefixes = ("nxs:",)

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "schema:instrument":
                    for e in (v if isinstance(v, list) else [v]):
                        if not isinstance(e, dict):
                            continue
                        at = e.get("schema:additionalType") or []
                        kept = [a for a in at if not isinstance(a, str) or a.startswith(keep_prefixes)]
                        e["schema:additionalType"] = kept[:1] + list(tokens) + kept[1:]
                walk(v)
        elif isinstance(x, list):
            for i in x:
                walk(i)

    walk(ex)


def build(tapp):
    cfg = PROFILES[tapp]
    if not cfg.get("addtype"):
        # A TEMPLATE entry: everything derivable is filled in, but the product-type labels are a
        # curation decision and have not been made. Refuse rather than emit, because an empty
        # addtype becomes `contains: {enum: []}` -- a clause that matches NOTHING, so every example
        # for the technique would fail against a profile that looks complete. Skipping is not a
        # failure: the entry is deliberately unfinished and says so.
        print(f"SKIP {tapp} -> template: addtype not authored "
              f"(product-type labels for {cfg.get('short', tapp)})")
        return 0
    cts = b.TAPP_CONFIGS[tapp]["component_types"]
    d = _profile_dir(tapp)
    os.makedirs(d, exist_ok=True)
    schema = _schema(tapp, cfg)
    b.write(os.path.join(d, "schema.yaml"), b.dump_yaml(schema))
    ex = _example(tapp, cfg, cts)
    _wj(os.path.join(d, "example" + cfg["cid"] + ".json"), ex)
    _wj(os.path.join(d, "example" + cfg["cid"] + "-monolithic.json"), _example_monolithic(ex, cfg, cts))
    _wj(os.path.join(d, "bblock.json"), _bblock(cfg))
    with open(os.path.join(d, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(_examples_yaml(cfg))
    print(f"DONE {tapp} -> techniqueProfile/{b.TECH_DIR[tapp]}/profile (conformsTo {cfg['cid']}, {len(cts)} componentTypes)")


def _wj(path, obj):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False); f.write("\n")


def validate(tapp):
    import jsonschema
    cfg = PROFILES[tapp]
    d = _profile_dir(tapp)
    schema = json.load(open(os.path.join(d, "resolvedSchema.json"), encoding="utf-8"))
    V = jsonschema.Draft202012Validator(schema)
    rc = 0
    for suffix, label in [("", "bundle"), ("-monolithic", "monolithic")]:
        path = os.path.join(d, "example" + cfg["cid"] + suffix + ".json")
        if not os.path.exists(path):
            continue
        errs = sorted(V.iter_errors(json.load(open(path, encoding="utf-8"))), key=lambda e: list(e.path))
        if errs:
            rc = 1
            print(f"{cfg['dir']} [{label}]: {len(errs)} error(s)")
            for e in errs[:12]:
                print(f"  /{'/'.join(map(str, e.path))}: {e.message[:110]}")
        else:
            print(f"{cfg['dir']} [{label}]: GREEN")
    return rc


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit(f"usage: build_profile.py <tapp> [--validate]   known: {sorted(PROFILES)}")
    sys.exit(validate(args[0]) if "--validate" in sys.argv else (build(args[0]) or 0))
