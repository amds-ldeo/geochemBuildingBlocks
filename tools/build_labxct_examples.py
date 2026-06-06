#!/usr/bin/env python
"""Build representative example instances for labxctTAPP + detailLABXCT and their
examples.yaml. Entries that reference the parameter registries are reconstructed from
the routing so their const-pinned fields match exactly. Run after
build_labxct_from_spreadsheet.py.
"""
import json, os, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs", "new_tapps202606")
routing = json.load(open(os.path.join(DOCS, "labxct_routing.json"), encoding="utf-8"))
TAPP_DIR = os.path.join(ROOT, "_sources", "techniqueProtocols", "labxctTAPP")
DETAIL_DIR = os.path.join(ROOT, "_sources", "analysisSpecificDetails", "detailLABXCT")
PARAM_BASE = "ada:parameter/labxctTAPP"
CTX_FULL = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
            "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
            "bios": "https://bioschemas.org/"}
CTX_DETAIL = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"}

by_name_mp = {b["name"]: b for b in routing["method_param"]}
by_name_pv = {}
for b in routing["detail_addl"]:
    by_name_pv.setdefault(b["name"], b)

# representative values for ada: top-level props / detail_req
VAL = {
    "targetFeature": "Opaque phase (FeNi metal, sulfide) 3D distribution",
    "applicableSampleDimensionRange": "Single-volume: max 20 mm in all dimensions at 7.6 um voxel",
    "xRaySourceConfiguration": "Reflection target, microfocal",
    "detectorType": "Flat-panel (amorphous silicon, a-Si)",
    "acquisitionSoftware": "CT Agent Pro 3D v3.8 (Nikon)",
    "reconstructionSoftware": "CT Pro 3D v3.8 (Nikon)",
    "segmentationAndAnalysisSoftware": "Avizo 9.2 (Thermo Fisher)",
    "analyticalMode": "Single-volume; Multi-volume stitching",
    "acceleratingVoltage": "160 kV", "tubeCurrent": "180 uA", "xRayPreFilter": "1 mm Cu",
    "voxelSize": "7.63 um", "rotationRange": "360", "numberOfProjections": "2046",
    "exposureTimePerProjection": "1.42 s", "flatFieldCorrection": "Yes",
    "rotationMode": "Step rotation (stop-and-shoot)", "minimumSubVolumeOverlap": "500",
    "reconstructionAlgorithm": "FDK (Feldkamp-Davis-Kress, cone-beam)",
    "beamHardeningCorrectionMethod": "Hardware pre-filtering only (no software correction)",
    "outputDataFormat": "TIFF image stack", "segmentationMethod": "Multi-threshold (separate CT number range per phase)",
    "subVolumeStitchingAndRegistrationMethod": "Automated stitching, VGStudio Max",
    "analyst": "J. Smith (ORCID: 0000-0001-2345-6789)",
    "analysisStartDate": "2022-04-22", "analysisEndDate": "2022-04-22",
    "protocolDoi": "http://doi.org/10.60520/IEDA/114187",
    "fundingSourceForAnalysis": "NASA 80NSSC21K0153",
    "sampleDimensions": "12 x 8 x 5 mm", "sampleName": "NWA 10597",
    "voiApplied": "Cylindrical VOI, radius = 85% of sample radius, full height",
}


def tapp_prop_key(b):
    suffix = "Default" if b["A"] == "Editable" else ""
    return "ada:" + b["name"] + suffix


def mp_entry(name):
    b = by_name_mp[name]
    e = {"@id": PARAM_BASE + "/" + name,
         "@type": ["schema:PropertyValueSpecification"], "schema:valueName": name,
         "schema:name": b["item"], "ada:dataType": b["jtype"], "ada:fieldScope": "session",
         "schema:readonlyValue": True, "ada:tier": "R"}
    if b.get("unit") and b["unit"] != "free":
        e["schema:unitText"] = b["unit"]
    return e


def pv_entry(name, value):
    b = by_name_pv[name]
    e = {"@id": PARAM_BASE + "/" + name,
         "@type": ["schema:PropertyValue"], "schema:propertyID": PARAM_BASE + "/" + name,
         "schema:name": b["item"], "schema:value": value}
    if b.get("unit") and b["unit"] != "free":
        e["schema:unitText"] = b["unit"]
    return e


def build_tapp():
    inst = {
        "@context": CTX_FULL, "@id": "ex:labxctTAPP-P0",
        "@type": ["cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"],
        "schema:name": "Lab-XCT Meteorite 3D Characterization v1.0",
        "schema:identifier": "http://doi.org/10.60520/IEDA/114187",
        "schema:version": "1.0",
        "schema:datePublished": "2022-04-22",
        "schema:measurementTechnique": {"@type": ["schema:DefinedTerm"], "schema:termCode": "XCT",
                                        "schema:name": "XCT (laboratory, polychromatic cone-beam)"},
        "schema:creator": {"@id": "https://ror.org/00hj54h04"},
        "schema:object": ["Chondrite meteorite"],
        "schema:funding": [],
    }
    inst.pop("schema:funding")
    for b in routing["tapp_prop"]:
        if b["name"] in VAL:
            inst[tapp_prop_key(b)] = VAL[b["name"]]
    inst["ada:methodParameters"] = [mp_entry("xRayPower"), mp_entry("detectorPixelSize"),
                                    mp_entry("sourceToObjectDistance")]
    # minimal valid workflow with required sample-preparation step
    inst["schema:actionProcess"] = {
        "@type": ["schema:HowTo"], "schema:name": "Lab-XCT acquisition workflow",
        "schema:step": [{
            "@type": ["cdi:Activity", "schema:Action"], "schema:name": "Sample preparation",
            "schema:position": 1, "schema:additionalType": ["bios:LabProcess"],
            "schema:description": "Mount the meteorite fragment free-standing on the stage pin; no surface preparation (non-destructive)."
        }, {
            "@type": ["cdi:Activity", "schema:Action"], "schema:name": "Data acquisition",
            "schema:position": 2,
            "schema:description": "Acquire 2046 projections over 360 degrees at 160 kV / 180 uA, 7.63 um voxel."
        }],
    }
    return inst


def build_detail():
    inst = {
        "@context": CTX_DETAIL, "@id": "ex:detailLABXCT-P0", "@type": ["ada:XCTVolume"],
        "ada:componentType": "ada:XCTVolume",
        "schema:measurementTechnique": {"@id": "ex:labxctTAPP-P0"},
        "ada:analyst": VAL["analyst"], "ada:analysisStartDate": VAL["analysisStartDate"],
        "ada:analysisEndDate": VAL["analysisEndDate"], "ada:protocolDoi": VAL["protocolDoi"],
        "ada:fundingSourceForAnalysis": VAL["fundingSourceForAnalysis"],
        "ada:sampleDimensions": VAL["sampleDimensions"], "ada:sampleName": VAL["sampleName"],
        "ada:voiApplied": VAL["voiApplied"],
        "schema:additionalProperty": [
            pv_entry("voxelSize", 7.63), pv_entry("acceleratingVoltage", 160),
            pv_entry("tubeCurrent", 180), pv_entry("numberOfProjections", 2046),
            pv_entry("spatialResolution", "~22 um effective (3x voxel size; not formally measured)"),
        ],
    }
    return inst


def examples_yaml(title, content, prefixes, ref):
    return [{"title": title, "content": content, "prefixes": prefixes,
             "snippets": [{"language": "json", "ref": ref}]}]


def main():
    tapp = build_tapp()
    detail = build_detail()
    json.dump(tapp, open(os.path.join(TAPP_DIR, "examplelabxctTAPP-P0.json"), "w",
                         encoding="utf-8", newline="\n"), indent=2, ensure_ascii=False)
    json.dump(detail, open(os.path.join(DETAIL_DIR, "exampledetailLABXCT-P0.json"), "w",
                           encoding="utf-8", newline="\n"), indent=2, ensure_ascii=False)
    yaml.safe_dump(
        examples_yaml("labxctTAPP example P0 (synthetic comprehensive Lab-XCT example)",
                      "labxctTAPP instance exercising the XCT protocol-level defaults and a sample of method parameters. Values are illustrative, taken from the allowed-content guidance of the Lab-XCT_TAPP_v8.xlsx 'TAPP' worksheet.",
                      CTX_FULL, "examplelabxctTAPP-P0.json"),
        open(os.path.join(TAPP_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n"),
        sort_keys=False, allow_unicode=True)
    yaml.safe_dump(
        examples_yaml("Lab-XCT Analysis Detail example P0",
                      "detailLABXCT instance for a single-volume reconstructed XCT volume (ada:XCTVolume), with required analysis-level properties and a sample of per-dataset PropertyValue entries.",
                      CTX_DETAIL, "exampledetailLABXCT-P0.json"),
        open(os.path.join(DETAIL_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n"),
        sort_keys=False, allow_unicode=True)
    print("wrote examples + examples.yaml for labxctTAPP and detailLABXCT")


if __name__ == "__main__":
    main()
