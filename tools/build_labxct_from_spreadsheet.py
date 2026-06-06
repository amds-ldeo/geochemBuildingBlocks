#!/usr/bin/env python
"""Generate labxctTAPP + detailLABXCT building blocks and their catalog/vocab
contributions from the Lab-XCT TAPP spreadsheet routing.

Unlike build_empaTAPP_from_spreadsheet.py (which keys off [schema path, matchComment,
impl notes] guidance columns), Ruolin's new TAPP workbooks lack those columns, so
routing is driven purely by the two tier columns per the documented rules:
  Protocol-Level Tier: Basic -> TAPP top-level property; Advanced -> ada:methodParameters template
  Analysis-Level Tier: Basic -> required property in detail BB; Read-Only -> (lives on TAPP);
                       Editable/Advanced -> schema:additionalProperty anyOf branch in detail BB
Controlled lists -> vocab/ DefinedTermSet reference data.
Routing precomputed in docs/new_tapps202606/labxct_routing.json.
"""
import json, os, re, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTING = os.path.join(ROOT, "docs", "new_tapps202606", "labxct_routing.json")
TP = os.path.join(ROOT, "_sources", "techniqueProtocols")
TAPP_DIR = os.path.join(TP, "labxctTAPP")
DETAIL_DIR = os.path.join(ROOT, "_sources", "analysisSpecificDetails", "detailLABXCT")
VOCAB_DIR = os.path.join(TP, "vocab")
PT = os.path.join(TP, "parameterTemplates", "schema.yaml")
PV = os.path.join(TP, "parameterValues", "schema.yaml")

TAPP = "labxctTAPP"
PARAM_BASE = "ada:parameter/" + TAPP
VOCAB_BASE = "ada:vocab/" + TAPP
CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"}

# componentType strings for XCT data products (proposed; need adding to the Components
# worksheet + base file-type BB enums to wire into profile-level validation).
COMPONENT_TYPES = [
    "ada:XCTVolume", "ada:XCTProjectionImageSet", "ada:XCTSegmentationVolume",
    "ada:XCTRenderedImage", "ada:XCTQuantitativeTabular",
]

routing = json.load(open(ROUTING, encoding="utf-8"))


def dump_yaml(obj):
    return yaml.safe_dump(obj, sort_keys=False, allow_unicode=True,
                          default_flow_style=False, width=100)


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", os.path.relpath(path, ROOT))


def def_key(bare, existing):
    """Bare parameter name is the registry key (reusable across techniques). Add the
    technique prefix only when that name already exists with an incompatible schema."""
    return ("labxct_" + bare) if bare in existing else bare


def is_dual(b):
    """Advanced-protocol field is dual-homed (method def + detail) when Analysis-Level
    Tier is Basic/Editable/Advanced; Read-Only fields live only in the method def."""
    return b["A"] in ("Basic", "Editable", "Advanced")


def methoddef_name(b):
    return b["name"] + ("Default" if is_dual(b) else "")


def param_template_def(b, existing):
    mdname = methoddef_name(b)
    name = def_key(mdname, existing)
    props = {
        "@id": {"const": PARAM_BASE + "/" + mdname},
        "@type": {"const": ["schema:PropertyValueSpecification"]},
        "schema:valueName": {"const": mdname},
        "schema:name": {"const": b["item"]},
        "ada:dataType": {"const": b["jtype"]},
        "ada:fieldScope": {"const": "session"},
        "schema:readonlyValue": {"const": not is_dual(b)},
        "ada:tier": {"const": "R"},
    }
    if b.get("unit") and b["unit"] != "free":
        props["schema:unitText"] = {"const": b["unit"]}
    return name, {name: {"title": b["item"], "description": b["desc"], "type": "object",
                         "properties": props,
                         "required": ["@id", "@type", "schema:valueName", "schema:name",
                                      "ada:dataType", "ada:fieldScope"]}}


def param_value_def(b, existing):
    bare = b["name"]
    name = def_key(bare, existing)
    has_unit = bool(b.get("unit") and b["unit"] != "free")
    props = {
        "@id": {"const": PARAM_BASE + "/" + bare},
        "@type": {"const": ["schema:PropertyValue"]},
        "schema:propertyID": {"const": PARAM_BASE + "/" + bare},
        "schema:name": {"const": b["item"]},
    }
    if b["jtype"] in ("number", "integer"):
        props["schema:value"] = {"anyOf": [{"type": "number"}, {"type": "string"}]}
    else:
        props["schema:value"] = {"type": "string"}
    req = ["@id", "@type", "schema:propertyID", "schema:name", "schema:value"]
    if has_unit:
        props["schema:unitText"] = {"type": "string"}
        req.append("schema:unitText")
    return name, {name: {"title": b["item"], "description": b["desc"], "type": "object",
                         "properties": props, "required": req}}


def remove_owned_blocks(path, owner_substr):
    """Drop $def blocks whose body references owner_substr (this TAPP's @id), preserving
    formatting of all other entries. Idempotent: regen removes the prior owned entries
    before re-appending, so re-runs don't duplicate."""
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    out, i, removed = [], 0, []
    defs_re = re.compile(r"^  (\S.*):\s*$")
    while i < len(lines):
        m = defs_re.match(lines[i])
        if m:
            j = i + 1
            block = [lines[i]]
            while j < len(lines) and not defs_re.match(lines[j]):
                block.append(lines[j])
                j += 1
            if owner_substr in "".join(block):
                removed.append(m.group(1))
            else:
                out.extend(block)
            i = j
        else:
            out.append(lines[i])
            i += 1
    open(path, "w", encoding="utf-8", newline="\n").write("".join(out))
    return removed


def append_defs(catalog_path, defs):
    frag = ""
    for name, body in defs.items():
        block = dump_yaml({name: body})
        frag += "\n" + "\n".join(("  " + ln) if ln else ln for ln in block.splitlines())
    with open(catalog_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(frag.rstrip("\n") + "\n")
    print("appended", len(defs), "$defs to", os.path.relpath(catalog_path, ROOT))


def write_vocab(b):
    terms = [{"@type": ["schema:DefinedTerm"], "schema:termCode": t, "schema:name": t}
             for t in b["terms"] if t not in ("N/A", "None")]
    obj = {
        "$schema": "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTermSet/schema.yaml",
        "@context": CTX,
        "@id": VOCAB_BASE + "/" + b["name"],
        "@type": ["schema:DefinedTermSet"],
        "schema:name": b["item"],
        "schema:description": b["desc"][:300],
        "schema:hasDefinedTerm": terms,
    }
    write(os.path.join(VOCAB_DIR, "labxct_" + b["name"] + ".json"),
          json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def existing_keys(path):
    d = yaml.safe_load(open(path, encoding="utf-8")) or {}
    return set((d.get("$defs") or {}).keys())


def main():
    for b in routing["vocab"]:
        write_vocab(b)

    # drop any prior labxct-owned entries first (idempotent regen; no duplicates)
    remove_owned_blocks(PT, PARAM_BASE + "/")
    remove_owned_blocks(PV, PARAM_BASE + "/")
    pt_existing = existing_keys(PT)
    pv_existing = existing_keys(PV)

    pt_defs, pt_names, pt_pref = {}, [], []
    for b in routing["method_param"]:
        n, d = param_template_def(b, pt_existing)
        pt_defs.update(d)
        pt_names.append(n)
        if n != b["name"]:
            pt_pref.append(n)
    append_defs(PT, pt_defs)

    # pv: bare-name @id for the catch-all not-enum; def key may be prefixed on collision
    pv_defs, pv_names, pv_ids, pv_pref, seen = {}, [], [], [], set()
    for b in routing["detail_addl"]:
        if b["name"] in seen:
            continue
        seen.add(b["name"])
        n, d = param_value_def(b, pv_existing)
        pv_defs.update(d)
        pv_names.append(n)
        pv_ids.append(PARAM_BASE + "/" + b["name"])
        if n != b["name"]:
            pv_pref.append(n)
    append_defs(PV, pv_defs)
    if pt_pref or pv_pref:
        print("  collision-prefixed (name already in registry, incompatible schema):",
              "templates=" + str(pt_pref), "values=" + str(pv_pref))

    BASE_ITEMS = {"Protocol Name", "Technique", "Protocol Author", "Laboratory",
                  "Protocol Start Date", "Funding Source for Protocol Development",
                  "Target Material", "CT System Manufacturer and Model",
                  "Protocol Reference(s)", "Laboratory ID", "Protocol DOI"}
    tapp_props = {}
    basic_required = []
    for b in routing["tapp_prop"]:
        if b["item"] in BASE_ITEMS:
            continue
        suffix = "Default" if b["A"] == "Editable" else ""
        key = "ada:" + b["name"] + suffix
        p = {"description": b["desc"], "type": "string"}
        if b["name"] == "analyticalMode":
            p["enum"] = ["Single-volume", "Multi-volume stitching",
                         "Single-volume; Multi-volume stitching"]
        tapp_props[key] = p
        basic_required.append(key)
    sap_refs = [{"$ref": "../parameterTemplates/schema.yaml#/$defs/" + n} for n in pt_names]
    sap_contains = [{"contains": {"$ref": "../parameterTemplates/schema.yaml#/$defs/" + n},
                     "minContains": 0, "maxContains": 1} for n in pt_names]
    tapp_props["schema:additionalProperty"] = {
        "type": "array",
        "description": ("Method-level parameter specifications (Advanced protocol tier). Each entry is "
                        "a schema:PropertyValueSpecification; dual-homed fields use the …Default name "
                        "here and carry the per-dataset value in the detail block."),
        "items": {"anyOf": sap_refs},
        "allOf": sap_contains,
    }
    tapp_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP)",
        "description": ("Laboratory X-ray computed tomography (polychromatic cone-beam) extension of "
                        "the base TAPP definition. Basic protocol-tier fields are required top-level "
                        "ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] "
                        "PropertyValueSpecification entries. XCT has no per-element analyte axis, so no "
                        "ada:analyteTemplate is defined. Generated from docs/Lab-XCT_TAPP_v8.xlsx by "
                        "tools/build_labxct_from_spreadsheet.py."),
        "allOf": [
            {"$ref": "../tappDefinition/schema.yaml"},
            {"type": "object", "properties": tapp_props, "required": basic_required},
        ],
    }
    write(os.path.join(TAPP_DIR, "schema.yaml"), dump_yaml(tapp_schema))

    detail_req_props, required = {}, ["ada:componentType"]
    for b in routing["detail_req"]:
        key = "ada:" + b["name"]
        jt = "string" if b["jtype"] in ("string", "date", "uri") else b["jtype"]
        detail_req_props[key] = {"description": b["desc"], "type": jt}
        if not b["multivol_only"]:
            required.append(key)
    block1_props = {
        "ada:componentType": {"anyOf": [{"const": c} for c in COMPONENT_TYPES]},
        "schema:measurementTechnique": {
            "type": "object",
            "description": "@id reference to a registered labxctTAPP TAPP definition.",
            "properties": {"@id": {"type": "string", "format": "uri"}},
            "required": ["@id"],
        },
    }
    block1_props.update(detail_req_props)
    pv_branches = [{"$ref": "../../techniqueProtocols/parameterValues/schema.yaml#/$defs/" + n}
                   for n in pv_names]
    catchall = {
        "type": "object",
        "description": "Catch-all for additional schema:PropertyValue entries beyond the labxctTAPP-derived catalog.",
        "properties": {
            "@type": {"type": "array", "items": {"type": "string"},
                      "contains": {"const": "schema:PropertyValue"}},
            "schema:propertyID": {"type": "string", "not": {"enum": pv_ids}},
        },
        "required": ["@type", "schema:propertyID"],
    }
    detail_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Lab-XCT Analysis Detail",
        "description": ("Detail block for Lab-XCT hasPart items. Discriminates on ada:componentType "
                        "(string), carries the analysis-level required properties (analyst, dates, "
                        "sample, VOI) and an @id reference to a registered labxctTAPP definition via "
                        "schema:measurementTechnique. Per-dataset schema:additionalProperty entries "
                        "are constrained inline via $refs to the parameterValues registry (one "
                        "schema:PropertyValue branch per session-editable labxctTAPP parameter, plus "
                        "a catch-all). Generated by tools/build_labxct_from_spreadsheet.py."),
        "allOf": [
            {"type": "object", "properties": block1_props, "required": required},
            {"type": "object", "properties": {"schema:additionalProperty": {
                "type": "array",
                "description": "Per-dataset schema:PropertyValue entries for this XCT dataset. All optional; include only parameters you have values for.",
                "items": {"anyOf": pv_branches + [catchall]},
            }}},
        ],
    }
    write(os.path.join(DETAIL_DIR, "schema.yaml"), dump_yaml(detail_schema))

    json.dump({"pt_names": pt_names, "pv_names": pv_names,
               "tapp_props": list(tapp_props.keys()),
               "detail_req": [b["name"] for b in routing["detail_req"]],
               "detail_req_multivol": [b["name"] for b in routing["detail_req"] if b["multivol_only"]],
               "component_types": COMPONENT_TYPES},
              open(os.path.join(ROOT, "docs", "new_tapps202606", "labxct_gen_index.json"), "w"), indent=1)
    print("DONE schemas + catalogs + vocab")


if __name__ == "__main__":
    main()
