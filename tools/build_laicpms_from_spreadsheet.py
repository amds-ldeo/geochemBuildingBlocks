#!/usr/bin/env python
"""Full regeneration of laicpmsTAPP + detailLAICPMS from LA-Q_SF-ICPMS_TAPP_v2.xlsx.

v2 is treated as the authoritative update of the workbook that generated the original
laicpmsTAPP. Routing (no impl columns) follows the documented tier rules:
  Protocol-Level Tier: Basic -> TAPP top-level ada: property (…Default if editable at analysis);
                       Advanced -> ada:methodParameters template
  Analysis-Level Tier: Basic -> required property in detailLAICPMS; Read-Only -> lives on TAPP;
                       Editable/Advanced -> schema:additionalProperty branch in detailLAICPMS
  Analyte-specific rows -> ada:analyteTemplate.ada:analyteColumns (reusing existing analyteColumns $defs)
Old laicpmsTAPP-owned parameterTemplates $defs are removed and regenerated. analyteColumns are
reused as-is. Run build_laicpms_examples.py afterwards to (re)build the publication examples.
"""
import json, os, re, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX = os.path.join(ROOT, "docs", "LA-Q_SF-ICPMS_TAPP_v2.xlsx")
TP = os.path.join(ROOT, "_sources", "techniqueProtocols")
TAPP_DIR = os.path.join(TP, "laicpmsTAPP")
DETAIL_DIR = os.path.join(ROOT, "_sources", "analysisSpecificDetails", "detailLAICPMS")
VOCAB_DIR = os.path.join(TP, "vocab")
PT = os.path.join(TP, "parameterTemplates", "schema.yaml")
PV = os.path.join(TP, "parameterValues", "schema.yaml")

TAPP = "laicpmsTAPP"
PARAM_BASE = "ada:parameter/" + TAPP
VOCAB_BASE = "ada:vocab/" + TAPP
CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"}
COMPONENT_TYPES = ["ada:LAICPMSTabular", "ada:LAICPMSMap", "ada:LAICPMSImage", "ada:LAICPMSTransect"]

# Analyte-specific rows -> existing analyteColumns $def names (reused, not regenerated)
ANALYTE_MAP = {
    "Spectrometer Dwell Time": ["spectrometerDwellTime"],
    "Detection Limit": ["detectionLimit"],
    "Detection Limit Method": ["detectionLimitMethod"],
    "Limit of Quantification (LOQ) Method": ["limitOfQuantification"],
    "Within-Session Analytical Precision and Assessment Method":
        ["withinSessionReproducibility", "withinSessionReproducibilityMethod"],
    "Between-Session (Long-Term) Analytical Precision and Assessment Method":
        ["betweenSessionReproducibility", "betweenSessionReproducibilityMethod"],
    "Analytical Accuracy and Assessment Method": ["analyticalAccuracy", "analyticalAccuracyMethod"],
    "Interfering Species": ["interferingSpecies"],
    "Interference Correction Method": ["IsobaricInterferenceCorrectionMethod"],
    "Isobaric Interference Corrections Applied": ["IsobaricInterferenceCorrection"],
}
# Rows that populate inherited base-TAPP identity fields (no new ada: property)
BASE_ITEMS = {"Protocol Name", "Technique", "Protocol Author", "Laboratory", "Protocol Start Date",
              "Funding Source for Protocol Development", "Target Material", "Protocol Reference(s)",
              "Protocol DOI", "Laboratory ID", "Analyte"}


def norm(v):
    return " ".join(str(v).split()) if v is not None else ""


def camel(s):
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^A-Za-z0-9 ]", " ", s).strip()
    parts = s.split()
    return (parts[0].lower() + "".join(p.capitalize() for p in parts[1:])) if parts else "x"


def jtype(dt):
    d = dt.lower()
    if "integer" in d:
        return "integer"
    if "numeric" in d or "number" in d:
        return "number"
    if "boolean" in d:
        return "boolean"
    if d.startswith("date"):
        return "date"
    if "uri" in d or "doi" in d:
        return "uri"
    return "string"


def unit(dt):
    m = re.search(r"\(([^)]+)\)", dt)
    return m.group(1) if m else None


def dump_yaml(obj):
    return yaml.safe_dump(obj, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", os.path.relpath(path, ROOT))


# ---------- routing ----------
def route():
    wb = yaml  # placeholder to satisfy linters
    import openpyxl
    ws = openpyxl.load_workbook(XLSX, data_only=True, read_only=True)["TAPP"]
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    hdr = rows[0]
    lit = [i for i, v in enumerate(hdr) if norm(v).lower() == "literature assessment"][0]

    def meaningful(v):
        v = re.sub(r"\s*\[P[^\]]*\]", "", v).strip()
        if v in ("", "N", "N/A"):
            return False
        m = re.match(r"^(N/A|N)\b\s*", v)
        if m:
            rest = v[m.end():]
            if rest.startswith("("):
                depth = 0
                for i, ch in enumerate(rest):
                    depth += (ch == "(") - (ch == ")")
                    if ch == ")" and depth == 0:
                        rest = rest[i + 1:]
                        break
            if re.fullmatch(r"[/;,\-\s]*", rest.strip()):
                return False
        return True

    buckets = {"tapp_prop": [], "method_param": [], "detail_req": [], "detail_addl": [],
               "analyte_cols": [], "vocab": []}
    for r in rows[1:]:
        item = norm(r[0])
        if not item or re.match(r"^\d+\.\s", item):
            continue
        P, A, dt, ex = norm(r[2]), norm(r[3]), norm(r[4]), norm(r[5])
        modes = [norm(hdr[i]) for i in range(8, lit) if norm(r[i]) in ("Y", "y")]
        cov = sum(1 for i in range(lit + 1, len(r)) if meaningful(norm(r[i])))
        rec = {"item": item, "name": camel(item), "P": P, "A": A, "jtype": jtype(dt),
               "unit": unit(dt), "desc": norm(r[1]), "allowed": ex,
               "multivol_only": (modes == ["Mapping"]), "cov": cov}
        if item in ANALYTE_MAP:
            buckets["analyte_cols"].append({**rec, "cols": ANALYTE_MAP[item]})
            continue
        if item in BASE_ITEMS:
            continue
        if "controlled" in dt.lower() or dt.lower().startswith("boolean"):
            terms = (["Yes", "No"] if dt.lower().startswith("boolean")
                     else [p.strip().strip("'\"") for p in ex.split("|")
                           if p.strip() and not p.strip().lower().startswith("e.g")
                           and "specify" not in p.strip().lower()])
            if terms:
                buckets["vocab"].append({**rec, "terms": terms})
        if P == "Basic":
            buckets["tapp_prop"].append(rec)
        elif P == "Advanced":
            buckets["method_param"].append(rec)
        if A == "Basic":
            buckets["detail_req"].append(rec)
        elif A in ("Editable", "Advanced"):
            buckets["detail_addl"].append(rec)
    return buckets


# ---------- catalog helpers ----------
def def_key(bare, existing):
    return ("laicpms_" + bare) if bare in existing else bare


def is_dual(b):
    """An Advanced-protocol field is dual-homed (appears in BOTH the method definition
    and the detail) when its Analysis-Level Tier is Basic/Editable/Advanced. Read-Only
    fields live only in the method definition."""
    return b["A"] in ("Basic", "Editable", "Advanced")


def methoddef_name(b):
    """Name of the Advanced-protocol field's PropertyValueSpecification in the method
    definition: <name>Default when dual-homed (a per-dataset value also exists in the
    detail), else bare <name> (Read-Only constant)."""
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
        # constant (read-only) only when there is no editable per-dataset counterpart
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
    props["schema:value"] = ({"anyOf": [{"type": "number"}, {"type": "string"}]}
                             if b["jtype"] in ("number", "integer") else {"type": "string"})
    req = ["@id", "@type", "schema:propertyID", "schema:name", "schema:value"]
    if has_unit:
        props["schema:unitText"] = {"type": "string"}
        req.append("schema:unitText")
    return name, {name: {"title": b["item"], "description": b["desc"], "type": "object",
                         "properties": props, "required": req}}


def existing_keys(path):
    d = yaml.safe_load(open(path, encoding="utf-8")) or {}
    return set((d.get("$defs") or {}).keys())


def remove_owned_blocks(path, owner_substr):
    """Surgically drop $def blocks whose body references owner_substr (e.g. the TAPP @id),
    preserving formatting of all other blocks. Returns removed def names."""
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    # find the start of $defs blocks (2-space indented keys)
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


def append_defs(path, defs):
    frag = ""
    for name, body in defs.items():
        block = dump_yaml({name: body})
        frag += "\n" + "\n".join(("  " + ln) if ln else ln for ln in block.splitlines())
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(frag.rstrip("\n") + "\n")


def write_vocab(b):
    terms = [{"@type": ["schema:DefinedTerm"], "schema:termCode": t, "schema:name": t}
             for t in b["terms"] if t not in ("N/A", "None")]
    obj = {
        "$schema": "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTermSet/schema.yaml",
        "@context": CTX, "@id": VOCAB_BASE + "/" + b["name"], "@type": ["schema:DefinedTermSet"],
        "schema:name": b["item"], "schema:description": b["desc"][:300],
        "schema:hasDefinedTerm": terms,
    }
    write(os.path.join(VOCAB_DIR, "laicpms_" + b["name"] + ".json"),
          json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def main():
    R = route()
    os.makedirs(DETAIL_DIR, exist_ok=True)

    for b in R["vocab"]:
        write_vocab(b)

    # ---- parameterTemplates: drop old laicpms, append new ----
    removed_pt = remove_owned_blocks(PT, PARAM_BASE + "/")
    pt_existing = existing_keys(PT)
    pt_defs, pt_keys = {}, []
    for b in R["method_param"]:
        n, d = param_template_def(b, pt_existing)
        pt_defs.update(d); pt_keys.append(n); pt_existing.add(n)
    append_defs(PT, pt_defs)

    # ---- parameterValues: drop old laicpms (if any), append new ----
    remove_owned_blocks(PV, PARAM_BASE + "/")
    pv_existing = existing_keys(PV)
    pv_defs, pv_keys, pv_ids, seen = {}, [], [], set()
    for b in R["detail_addl"]:
        if b["name"] in seen:
            continue
        seen.add(b["name"])
        n, d = param_value_def(b, pv_existing)
        pv_defs.update(d); pv_keys.append(n); pv_ids.append(PARAM_BASE + "/" + b["name"]); pv_existing.add(n)
    append_defs(PV, pv_defs)

    # ---- analyteColumns referenced (reuse existing $defs) ----
    acols = []
    for b in R["analyte_cols"]:
        for c in b["cols"]:
            if c not in acols:
                acols.append(c)

    # ---- laicpmsTAPP/schema.yaml ----
    # Basic-protocol fields -> top-level ada: properties, REQUIRED (…Default when editable
    # at analysis, i.e. dual-homed with a per-dataset value in the detail).
    tapp_props = {}
    basic_required = []
    for b in R["tapp_prop"]:
        key = "ada:" + b["name"] + ("Default" if b["A"] == "Editable" else "")
        if b["jtype"] in ("number", "integer"):
            tapp_props[key] = {"description": b["desc"],
                               "anyOf": [{"type": "number"}, {"type": "string"}]}
        else:
            tapp_props[key] = {"description": b["desc"], "type": "string"}
        # Basic = required, EXCEPT fields no publication reports (cov == 0) -> optional
        if b["cov"] > 0:
            basic_required.append(key)
    # analyteTemplate
    ac_refs = [{"$ref": "../tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn"}] + \
              [{"$ref": "../analyteColumns/schema.yaml#/$defs/" + c} for c in acols]
    ac_contains = [{"contains": {"$ref": "../analyteColumns/schema.yaml#/$defs/" + c},
                    "minContains": 0, "maxContains": 1} for c in acols]
    tapp_props["ada:analyteTemplate"] = {
        "type": "object",
        "properties": {"ada:analyteColumns": {"type": "array", "items": {"anyOf": ac_refs},
                                              "allOf": ac_contains}},
    }
    # Advanced-protocol fields -> schema:additionalProperty[] of PropertyValueSpecification
    # (replaces ada:methodParameters). Names carry the …Default suffix when dual-homed.
    sap_refs = [{"$ref": "../parameterTemplates/schema.yaml#/$defs/" + n} for n in pt_keys]
    sap_contains = [{"contains": {"$ref": "../parameterTemplates/schema.yaml#/$defs/" + n},
                     "minContains": 0, "maxContains": 1} for n in pt_keys]
    tapp_props["schema:additionalProperty"] = {
        "type": "array",
        "description": ("Method-level parameter specifications (Advanced protocol tier). Each entry is "
                        "a schema:PropertyValueSpecification; dual-homed fields use the …Default name "
                        "here and carry the per-dataset value in the detail block."),
        "items": {"anyOf": sap_refs}, "allOf": sap_contains,
    }
    tapp_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP)",
        "description": ("LA-ICP-MS (incl. LA-Q-ICP-MS and LA-SF-ICP-MS) extension of the base TAPP "
                        "definition. Basic protocol-tier fields are required top-level ada: properties; "
                        "Advanced protocol-tier fields are schema:additionalProperty[] "
                        "PropertyValueSpecification entries; an ada:analyteTemplate carries the "
                        "per-element columns. Regenerated from docs/LA-Q_SF-ICPMS_TAPP_v2.xlsx by "
                        "tools/build_laicpms_from_spreadsheet.py."),
        "allOf": [{"$ref": "../tappDefinition/schema.yaml"},
                  {"type": "object", "properties": tapp_props, "required": basic_required}],
    }
    write(os.path.join(TAPP_DIR, "schema.yaml"), dump_yaml(tapp_schema))

    # ---- detailLAICPMS/schema.yaml ----
    req = ["ada:componentType"]
    block1 = {
        "ada:componentType": {"anyOf": [{"const": c} for c in COMPONENT_TYPES]},
        "schema:measurementTechnique": {"type": "object",
            "description": "@id reference to a registered laicpmsTAPP TAPP definition.",
            "properties": {"@id": {"type": "string", "format": "uri"}}, "required": ["@id"]},
    }
    for b in R["detail_req"]:
        key = "ada:" + b["name"]
        block1[key] = {"description": b["desc"],
                       "type": "string" if b["jtype"] in ("string", "date", "uri") else b["jtype"]}
        if not b["multivol_only"]:
            req.append(key)
    pv_branches = [{"$ref": "../../techniqueProtocols/parameterValues/schema.yaml#/$defs/" + n}
                   for n in pv_keys]
    catchall = {"type": "object",
        "description": "Catch-all for additional schema:PropertyValue entries beyond the laicpmsTAPP-derived catalog.",
        "properties": {"@type": {"type": "array", "items": {"type": "string"},
                                 "contains": {"const": "schema:PropertyValue"}},
                       "schema:propertyID": {"type": "string", "not": {"enum": pv_ids}}},
        "required": ["@type", "schema:propertyID"]}
    detail = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "LA-ICPMS Analysis Detail",
        "description": ("Detail block for LA-ICP-MS hasPart items. Discriminates on ada:componentType, "
                        "carries analysis-level required properties and an @id reference to a registered "
                        "laicpmsTAPP definition, and per-dataset schema:additionalProperty entries "
                        "constrained via $refs to the parameterValues registry plus a catch-all. "
                        "Generated by tools/build_laicpms_from_spreadsheet.py."),
        "allOf": [{"type": "object", "properties": block1, "required": req},
                  {"type": "object", "properties": {"schema:additionalProperty": {
                      "type": "array",
                      "description": "Per-dataset schema:PropertyValue entries. All optional.",
                      "items": {"anyOf": pv_branches + [catchall]}}}}],
    }
    write(os.path.join(DETAIL_DIR, "schema.yaml"), dump_yaml(detail))

    json.dump({"tapp_props": list(tapp_props.keys()), "pt_keys": pt_keys, "pv_keys": pv_keys,
               "analyte_cols": acols, "detail_req": [b["name"] for b in R["detail_req"]],
               "detail_req_multivol": [b["name"] for b in R["detail_req"] if b["multivol_only"]],
               "component_types": COMPONENT_TYPES, "removed_old_templates": removed_pt,
               "basic_required": basic_required,
               "basic_props": [{"key": "ada:" + b["name"] + ("Default" if b["A"] == "Editable" else ""),
                                "item": b["item"], "jtype": b["jtype"], "cov": b["cov"],
                                "required": b["cov"] > 0} for b in R["tapp_prop"]]},
              open(os.path.join(ROOT, "docs", "new_tapps202606", "laicpms_gen_index.json"), "w"), indent=1)
    print(f"removed old laicpms templates: {removed_pt}")
    print(f"tapp_props={len(R['tapp_prop'])} method_param={len(pt_keys)} "
          f"detail_req={len(R['detail_req'])} detail_addl={len(pv_keys)} "
          f"analyteCols={len(acols)} vocab={len(R['vocab'])}")
    print("DONE")


if __name__ == "__main__":
    main()
