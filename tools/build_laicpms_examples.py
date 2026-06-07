#!/usr/bin/env python
"""Build publication-derived laicpmsTAPP examples (cols M..Y of LA-Q_SF-ICPMS_TAPP_v2.xlsx)
and one detailLAICPMS example, against the regenerated schema. Uses the same routing as
build_laicpms_from_spreadsheet.py so example fields match the schema exactly.
Run after build_laicpms_from_spreadsheet.py.
"""
import json, os, re, sys
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX = os.path.join(ROOT, "docs", "LA-Q_SF-ICPMS_TAPP_v2.xlsx")
TAPP_DIR = os.path.join(ROOT, "_sources", "techniqueProtocols", "laicpmsTAPP")
DETAIL_DIR = os.path.join(ROOT, "_sources", "analysisSpecificDetails", "detailLAICPMS")
PARAM_BASE = "ada:parameter/laicpmsTAPP"
CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
       "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/", "bios": "https://bioschemas.org/"}
CTX2 = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"}

CODES = {"M": "Zhang2022", "N": "Chernonozhkin2021olivmap", "O": "Chernonozhkin2021multirun",
         "P": "Chernonozhkin2021phosphate", "Q": "Mittlefehldt2024", "R": "Nakanishi2022",
         "S": "Navarro2024spot", "T": "Navarro2024map", "U": "Liu2024", "V": "Liu2025glass",
         "W": "Liu2025sulfide", "X": "Liu2016silicate", "Y": "Liu2016phosphate"}
SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
       "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}

# load routing from the unified generator (build_laicpms_from_spreadsheet.py was
# renamed to build_tapp.py in the stage-1 consolidation)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_tapp as blf  # noqa: E402
blf.configure("laicpmsTAPP")


def norm(v):
    return " ".join(str(v).split()) if v is not None else ""


def strip_citations(v):
    return re.sub(r"\s*\[P[^\]]*\]", "", v).strip()


def meaningful(v):
    v = strip_citations(v).strip()
    if v in ("", "N", "N/A"):
        return None
    m = re.match(r"^(N/A|N)\b\s*", v)
    if m:
        rest = v[m.end():]
        if rest.startswith("("):
            depth = 0
            for i, ch in enumerate(rest):
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        rest = rest[i + 1:]
                        break
        if re.fullmatch(r"[/;,\-\s]*", rest.strip()):
            return None
    return v


def parse_analytes(cell):
    c = strip_citations(cell)
    toks = re.findall(r"([⁰¹²³⁴-⁹\d]{1,3})\s*([A-Z][a-z]?)", c)
    out, seen = [], set()
    for mass, el in toks:
        iso = "".join(SUP.get(ch, ch) for ch in mass) + el
        if iso not in seen:
            seen.add(iso)
            out.append(iso)
    return out


IDENTIFIER_COL = {
    "@type": ["schema:PropertyValueSpecification"],
    "schema:name": "Analyzed constituent", "schema:valueName": "analyte",
    "schema:description": "Analyzed constituent (isotope) identified by the analyte row.",
    "ada:dataType": "string", "schema:readonlyValue": True, "schema:valueRequired": True,
    "ada:tier": "M", "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
}


def main():
    R = blf.route()
    ws = openpyxl.load_workbook(XLSX, data_only=True, read_only=True)["TAPP"]
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    hdr = rows[0]
    # publication columns follow the 'Literature Assessment' separator (robust to inserted
    # guidance columns). Logical codes M..Y map by position, not physical column letter.
    lit = [i for i, v in enumerate(hdr) if norm(v).lower() == "literature assessment"][0]
    pub_cols = {chr(ord("M") + k): lit + 1 + k for k in range(13)}
    pub_hdr = {L: norm(hdr[i]) for L, i in pub_cols.items()}
    table = {}
    for r in rows[1:]:
        item = norm(r[0])
        if item:
            table[item] = {L: norm(r[i]) for L, i in pub_cols.items()}

    def cell(item, L):
        return meaningful(table.get(item, {}).get(L, ""))

    written = []
    for L, code in CODES.items():
        name = cell("Protocol Name", L) or pub_hdr[L]
        technique = cell("Technique", L) or "LA-ICP-MS"
        inst = {
            "@context": CTX, "@id": f"ex:laicpmsTAPP-{code}",
            "@type": ["cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"],
            "schema:name": name,
            "schema:description": f"laicpmsTAPP instance derived from {pub_hdr[L]} (column {L} of "
                                  f"LA-Q_SF-ICPMS_TAPP_v2.xlsx 'TAPP' worksheet).",
            "schema:measurementTechnique": {"@type": ["schema:DefinedTerm"],
                                            "schema:termCode": technique, "schema:name": technique},
        }
        lab = cell("Laboratory", L)
        if lab:
            inst["schema:location"] = {"@type": ["schema:Place"], "schema:name": lab}
        target = cell("Target Material", L)
        if target:
            inst["schema:object"] = [target]
        sw = cell("Data Reduction Software", L)
        if sw:
            inst["bios:computationalTool"] = [{"@type": ["schema:SoftwareApplication"],
                                               "schema:name": sw, "ada:toolRole": "reduction"}]
        # Basic-protocol props: real value, else sentinel when required (some pubs report it),
        # else omit when optional (no publication reports it, cov == 0).
        for b in R["tapp_prop"]:
            key = "ada:" + b["name"] + ("Default" if b["A"] == "Editable" else "")
            v = cell(b["item"], L)
            if v:
                inst[key] = v
            elif b["cov"] > 0:
                inst[key] = (-9999 if b["jtype"] in ("number", "integer") else "missing")
            # else cov == 0 -> optional, omit
        # Advanced-protocol fields -> schema:additionalProperty[] of PropertyValueSpecification
        # (…Default name + readonlyValue:false when dual-homed; bare name + readonly:true if Read-Only)
        saps = []
        for b in R["method_param"]:
            v = cell(b["item"], L)
            if not v:
                continue
            dual = b["A"] in ("Basic", "Editable", "Advanced")
            mdname = b["name"] + ("Default" if dual else "")
            e = {"@id": f"{PARAM_BASE}/{mdname}", "@type": ["schema:PropertyValueSpecification"],
                 "schema:valueName": mdname, "schema:name": b["item"], "ada:dataType": b["jtype"],
                 "ada:fieldScope": "session", "schema:readonlyValue": (not dual), "ada:tier": "R",
                 "schema:defaultValue": v}
            if b.get("unit") and b["unit"] != "free":
                e["schema:unitText"] = b["unit"]
            saps.append(e)
        if saps:
            inst["schema:additionalProperty"] = saps
        # analyteTemplate: identifier column + defaultAnalytes (analyte list only)
        analytes = parse_analytes(table.get("Analyte", {}).get(L, ""))
        if analytes:
            inst["ada:analyteTemplate"] = {
                "ada:analyteColumns": [dict(IDENTIFIER_COL)],
                "ada:defaultAnalytes": [{"analyte": a} for a in analytes],
            }
        fp = os.path.join(TAPP_DIR, f"examplelaicpmsTAPP-{code}.json")
        json.dump(inst, open(fp, "w", encoding="utf-8", newline="\n"), indent=2, ensure_ascii=False)
        open(fp, "a", encoding="utf-8", newline="\n").write("\n")
        written.append((code, L, len(saps), len(analytes)))

    # ---- examples.yaml for laicpmsTAPP (publication examples only) ----
    import yaml
    entries = [{"title": f"laicpmsTAPP example {code}",
                "content": f"laicpmsTAPP instance derived from {pub_hdr[L]} (column {L} of "
                           f"LA-Q_SF-ICPMS_TAPP_v2.xlsx 'TAPP' worksheet).",
                "prefixes": CTX,
                "snippets": [{"language": "json", "ref": f"examplelaicpmsTAPP-{code}.json"}]}
               for L, code in CODES.items()]
    with open(os.path.join(TAPP_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(entries, f, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)

    # remove obsolete placeholder mode examples (old schema field names)
    for mode in ("Spot", "Transect", "Mapping"):
        old = os.path.join(TAPP_DIR, f"examplelaicpmsTAPP-{mode}.json")
        if os.path.exists(old):
            os.remove(old)
            print("removed obsolete", os.path.basename(old))

    # ---- detailLAICPMS example (synthetic P0) ----
    def sample_value(b):
        return {"date": "2022-04-22", "integer": 3, "number": 1.0,
                "boolean": True}.get(b["jtype"], f"example {b['name']}")

    detail = {"@context": CTX2, "@id": "ex:detailLAICPMS-P0", "@type": ["ada:LAICPMSTabular"],
              "ada:componentType": "ada:LAICPMSTabular",
              "schema:measurementTechnique": {"@id": "ex:laicpmsTAPP-Navarro2024spot"}}
    # only required (non-multivol) detail props, with representative values
    for b in R["detail_req"]:
        if b["multivol_only"]:
            continue
        detail["ada:" + b["name"]] = sample_value(b)
    # one additionalProperty from the parameterValues registry (first detail_addl)
    if R["detail_addl"]:
        b0 = R["detail_addl"][0]
        e = {"@id": f"{PARAM_BASE}/{b0['name']}", "@type": ["schema:PropertyValue"],
             "schema:propertyID": f"{PARAM_BASE}/{b0['name']}", "schema:name": b0["item"],
             "schema:value": f"example {b0['name']}"}
        if b0.get("unit") and b0["unit"] != "free":
            e["schema:unitText"] = b0["unit"]
        detail["schema:additionalProperty"] = [e]
    fp = os.path.join(DETAIL_DIR, "exampledetailLAICPMS-P0.json")
    json.dump(detail, open(fp, "w", encoding="utf-8", newline="\n"), indent=2, ensure_ascii=False)
    open(fp, "a", encoding="utf-8", newline="\n").write("\n")
    with open(os.path.join(DETAIL_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump([{"title": "detailLAICPMS example P0",
                         "content": "detailLAICPMS instance for an LA-ICP-MS tabular dataset.",
                         "prefixes": CTX2,
                         "snippets": [{"language": "json", "ref": "exampledetailLAICPMS-P0.json"}]}],
                       f, sort_keys=False, allow_unicode=True)

    print(f"wrote {len(written)} laicpmsTAPP examples + detailLAICPMS-P0:")
    for code, L, nmp, nan in written:
        print(f"  {L} -> examplelaicpmsTAPP-{code}.json (methodParameters: {nmp}, analytes: {nan})")


if __name__ == "__main__":
    main()
