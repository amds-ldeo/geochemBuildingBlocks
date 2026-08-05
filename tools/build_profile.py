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

    python tools/build_profile.py <tapp>              # e.g. geochronTAPP
    python tools/build_profile.py <tapp> --validate
"""
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPROF = os.path.join(ROOT, "_sources", "techniqueProfile")
LAI = os.path.join(TPROF, "LA-ICPMS", "profile", "exampleadaICPMS.json")


def _profile_dir(tapp):
    return os.path.join(TPROF, b.TECH_DIR[tapp], "profile")

# per-TAPP profile config: dir name, detail short, conformsTo @id, additionalType product strings,
# titles. componentType enum is pulled from the TAPP CFG at build time.
PROFILES = {
    "geochronTAPP": dict(dir="Geochron", short="GEOCHRON", cid="adaGeochron",
        addtype=["Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry",
                 "Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry"],
        title="ADA LA-ICP-MS Geochronology Product Profile"),
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
}

CID_BASE = "https://w3id.org/geochem/metadata/profiles/"


def _schema(tapp, cfg, component_types):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": cfg["title"],
        "description": (f"Path-driven technique-specific profile for {cfg['title']}. Extends the base ADA "
                        f"product profile with the {cfg['short']} analysis-instance detail on the "
                        f"schema:Dataset root, narrows prov:used to the {tapp} protocol, and constrains "
                        f"valid component types on schema:distribution.hasPart."),
        "allOf": [
            {"$ref": "../../../BaseSchema/adaProduct/schema.yaml"},
            {"$ref": "../detail/schema.yaml"},
            {"type": "object", "properties": {
                "prov:wasGeneratedBy": {
                    "description": f"Narrow the base prov:used to the {tapp} definition — inline, or by node @id — alongside the instrument.",
                    "type": "array",
                    "items": {"type": "object", "properties": {"prov:used": {"type": "array", "items": {"anyOf": [
                        {"$ref": "../../../BaseSchema/instrument/schema.yaml"},
                        {"type": "object",
                         "description": f"Reference by node @id to a {tapp} definition object defined elsewhere.",
                         "properties": {"@id": {"type": "string", "format": "uri"}}, "required": ["@id"]},
                        {"$ref": "../tapp/schema.yaml"}]}}}}},
                "schema:additionalType": {
                    "description": f"Must include a {cfg['short']} product type identifier.",
                    "contains": {"enum": cfg["addtype"]}},
                "schema:distribution": {
                    "description": (f"Each distribution item is EITHER a monolithic single-file dataset whose "
                                    f"ada:componentType is a {cfg['short']}-specific or universal value (and may "
                                    f"carry cdi:isStructuredBy), OR a bundle whose schema:hasPart members each "
                                    f"carry such a componentType (the ADA/SAMIS archive form)."),
                    "type": "array",
                    "items": {"anyOf": [
                        # monolithic: the single file IS the dataset -> componentType on the distribution item
                        {"type": "object", "required": ["ada:componentType"],
                         "properties": {"ada:componentType": {"type": "string", "anyOf": [
                             {"$ref": "../../../BaseSchema/adaProduct/schema.yaml#/$defs/universalComponentType"},
                             {"enum": component_types}]}}},
                        # bundle: componentType on each hasPart member
                        {"type": "object", "required": ["schema:hasPart"],
                         "properties": {"schema:hasPart": {"items": {"type": "object", "anyOf": [
                             {"$ref": "../../../BaseSchema/adaProduct/schema.yaml#/$defs/universalComponentTypeBranch"},
                             {"properties": {"ada:componentType": {"type": "string", "enum": component_types}},
                              "required": ["ada:componentType"]}]}}}}]}},
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
    # retarget the TAPP linkage (measurementTechnique + prov:used @id refs) to this TAPP
    _swap_tapp(ex.get("schema:measurementTechnique"), tapp)
    _swap_tapp(ex.get("prov:wasGeneratedBy"), tapp)
    ex["schema:name"] = f"{cfg['title'].replace(' Product Profile','')} Example Product"
    ex["schema:description"] = (f"Example path-driven {cfg['short']} product record: dataset-level analysis "
                                f"detail plus technique component types on distribution.hasPart. Mock data.")
    ex["schema:additionalType"] = [cfg["addtype"][0], "ada:DataDeliveryPackage"]
    # swap distribution componentType -> this technique's first componentType
    for dist in ex.get("schema:distribution", []):
        for hp in dist.get("schema:hasPart", []):
            if isinstance(hp, dict) and "ada:componentType" in hp:
                hp["ada:componentType"] = component_types[0]
    # conformsTo: retarget technique @id (keep adaProduct + cdif classes), dedupe
    so = ex.get("schema:subjectOf")
    if isinstance(so, dict):
        ct = so.get("dcterms:conformsTo", [])
        ids = {x.get("@id") for x in ct if isinstance(x, dict)}
        # drop any prior technique-profile @id (keep adaProduct + cdif), then add ours
        ct = [x for x in ct if not (isinstance(x, dict) and x.get("@id", "").startswith(CID_BASE)
                                    and not x.get("@id", "").endswith("/adaProduct"))]
        if not any(isinstance(x, dict) and x.get("@id") == CID_BASE + cfg["cid"] for x in ct):
            ct.append({"@id": CID_BASE + cfg["cid"]})
        so["dcterms:conformsTo"] = ct
    return ex


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
                "cdif:name": v.get("schema:name", f"component_{i}")}
        if v.get("@id"):
            comp["cdif:isDefinedBy_RepresentedVariable"] = {"@id": v["@id"]}
        comps.append(comp)
    if not comps:
        comps = [{"@type": ["cdi:MeasureComponent"], "cdif:name": "measurement_value"}]
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
            "dateOfLastChange": "2026-08-04", "link": "https://github.com/usgin/geochemBuildingBlocks",
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


def build(tapp):
    cfg = PROFILES[tapp]
    cts = b.TAPP_CONFIGS[tapp]["component_types"]
    d = _profile_dir(tapp)
    os.makedirs(d, exist_ok=True)
    schema = _schema(tapp, cfg, cts)
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
