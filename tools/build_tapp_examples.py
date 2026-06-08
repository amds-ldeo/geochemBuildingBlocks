#!/usr/bin/env python
"""Generic publication-derived example builder for tier-column TAPPs.

For a given <tappName>, reads the publication columns of its workbook (everything
after the 'Literature Assessment' separator) and emits one example TAPP instance per
publication, using the same routing as tools/build_tapp.py so the fields match the
generated schema exactly. Identity fields are placed by `schema path`; Basic props,
Advanced parameters (editable -> PropertyValueSpecification, read-only ->
PropertyValue), analyticalMode (list), and the analyteTemplate are populated from the
per-publication cell values.

Usage:  python tools/build_tapp_examples.py <tappName>
Run after tools/build_tapp.py <tappName>.
"""
import json, os, re, sys
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_tapp as bt  # noqa: E402

CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
       "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/", "bios": "https://bioschemas.org/"}
SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
       "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}


def norm(v):
    return " ".join(str(v).split()) if v is not None else ""


def meaningful(v):
    return bt.meaningful(v)


def cell(v):
    """A publication cell value, citations stripped, or None if not meaningful."""
    s = re.sub(r"\s*\[P[^\]]*\]", "", norm(v)).strip()
    return s if bt.meaningful(s) else None


def short_code(header, idx):
    m = re.search(r"([A-Z][A-Za-z]+)\s*(?:et al\.?)?\s*\(?(\d{4})", header)
    return (m.group(1) + m.group(2)) if m else f"P{idx}"


def parse_analytes(v):
    """Comma/pipe-delimited analyte list -> normalised isotope strings (³¹P -> 31P)."""
    toks = re.findall(r"([⁰¹²³⁴-⁹\d]{1,3})\s*([A-Z][a-z]?)", re.sub(r"\s*\[P[^\]]*\]", "", v))
    out, seen = [], set()
    for mass, el in toks:
        iso = "".join(SUP.get(c, c) for c in mass) + el
        if iso not in seen:
            seen.add(iso); out.append(iso)
    if out:
        return out
    return [a.strip() for a in re.split(r"[;,|]", v) if a.strip()]


def place_identity(inst, item, sp, v):
    """Place an inherited identity field's value into the JSON-LD envelope by schema path."""
    if "schema:measurementTechnique" in sp:
        inst["schema:measurementTechnique"] = {"@type": ["schema:DefinedTerm"],
                                               "schema:termCode": v, "schema:name": v}
    elif sp.endswith(".schema:name") and ".schema:creator" not in sp and ".schema:location" not in sp:
        inst["schema:name"] = v
    elif "schema:creator" in sp:
        inst["schema:creator"] = {"@type": ["schema:Person"], "schema:name": v}
    elif "schema:location" in sp and ("identifier" in sp.lower()):
        inst.setdefault("schema:location", {"@type": ["schema:Place"]})["schema:identifier"] = v
    elif "schema:location" in sp:
        loc = inst.setdefault("schema:location", {"@type": ["schema:Place"]})
        loc["schema:name"] = v
    elif "schema:datePublished" in sp:
        inst["schema:datePublished"] = v.split()[0]
    elif "schema:identifier" in sp:
        inst["schema:identifier"] = v
    elif "schema:funding" in sp:
        for f in [t.strip() for t in v.split("|") if t.strip()]:
            inst.setdefault("schema:funding", []).append(
                {"@type": ["schema:MonetaryGrant"], "schema:name": f})
    elif "schema:relatedLink" in sp:
        for u in [t.strip() for t in v.split("|") if t.strip()]:
            inst.setdefault("schema:relatedLink", []).append(
                {"@type": ["schema:CreativeWork"], "schema:url": u, "schema:name": "Protocol reference"})
    elif "schema:object" in sp:
        for m in [t.strip() for t in v.split("|") if t.strip()]:
            inst.setdefault("schema:object", []).append(
                {"@type": ["schema:DefinedTerm"], "schema:name": m})
    elif "bios:computationalTool" in sp:
        role = "reduction" if "reduction" in item.lower() else "acquisition"
        for tool in [t.strip() for t in v.split("|") if t.strip()]:
            inst.setdefault("bios:computationalTool", []).append(
                {"@type": ["schema:SoftwareApplication"], "schema:name": tool, "ada:toolRole": role})
    elif "schema:instrument" in sp:
        cur = inst.setdefault("schema:instrument", {
            "@type": ["schema:Thing", "schema:Product"],
            "schema:additionalType": ["nxs:BaseClass/NXinstrument"], "schema:name": ""})
        cur["schema:name"] = (cur.get("schema:name", "") + " " + v).strip()
    # other inherited fields (sample prep, references already handled) are skipped


def coerce(v, jtype):
    """Coerce a string cell value to the JSON type implied by the field's data type."""
    if jtype in ("number", "integer"):
        m = re.match(r"-?\d+(?:\.\d+)?", v)
        if m:
            x = m.group(0)
            return int(x) if jtype == "integer" or "." not in x else float(x)
    return v


def build_detail(tapp, code, pc, R, pubval, param_base, detail_name, component_types):
    """Build one analysis-level detail-block instance from a publication column:
    componentType + required analysis-level (detail_req) fields + per-dataset
    schema:PropertyValue entries (detail_addl). Pairs with the TAPP example by @id."""
    ct = component_types[0] if component_types else "ada:Tabular"
    inst = {"@context": {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"},
            "@id": f"ex:{detail_name}-{code}", "@type": [ct], "ada:componentType": ct,
            "schema:measurementTechnique": {"@id": f"ex:{tapp}-{code}"}}
    seen = set()
    for b in R["detail_req"]:
        if b["name"] in seen:
            continue
        seen.add(b["name"])
        key = "ada:" + b["name"]
        v = cell(pubval[b["item"]].get(pc))
        if v is not None:
            inst[key] = coerce(v, b["jtype"])
        elif not b["multivol_only"]:   # required -> sentinel
            inst[key] = (-9999 if b["jtype"] in ("number", "integer") else "missing")
    saps, seen_pv = [], set()
    for b in R["detail_addl"]:
        if b["name"] in seen_pv:
            continue
        v = cell(pubval[b["item"]].get(pc))
        if not v:
            continue
        seen_pv.add(b["name"])
        e = {"@id": f"{param_base}/{b['name']}", "@type": ["schema:PropertyValue"],
             "schema:propertyID": f"{param_base}/{b['name']}", "schema:name": b["item"],
             "schema:value": coerce(v, b["jtype"])}
        if b.get("unit") and b["unit"] != "free":
            e["schema:unitText"] = b["unit"]
        saps.append(e)
    if saps:
        inst["schema:additionalProperty"] = saps
    return inst


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: build_tapp_examples.py <tappName>")
    tapp = sys.argv[1]
    bt.configure(tapp)
    short = tapp.replace("TAPP", "")
    R = bt.route()
    ws = openpyxl.load_workbook(bt.XLSX, data_only=True, read_only=True)["TAPP"]
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    hdr = rows[0]
    H = [norm(h).lower() for h in hdr]
    lit = next((i for i, h in enumerate(H) if h == "literature assessment"), None)
    sp_col = next((i for i, h in enumerate(H) if h == "schema path"), None)
    pub_cols = [i for i in range(lit + 1, len(hdr)) if norm(hdr[i])] if lit is not None else []

    # per-item lookups: schema-path (for identity placement) + pub values
    sp_by_item, pubval = {}, {}
    for r in rows[1:]:
        item = norm(r[0])
        if not item or re.match(r"^\d+\.\s", item):
            continue
        sp_by_item[item] = norm(r[sp_col]) if sp_col is not None and sp_col < len(r) else ""
        pubval[item] = {i: (r[i] if i < len(r) else None) for i in pub_cols}

    inherited_items = {it for it, sp in sp_by_item.items()
                       if sp.startswith("$MethodDefinition") and ".ada:" not in sp
                       and "additionalProperty" not in sp and "schema:description" not in sp}
    analyte_row = next((it for it, sp in sp_by_item.items()
                        if "analyteTemplate.ada:defaultAnalytes" in sp or it == "Analyte"), None)
    acols = []
    for b in R["analyte_cols"]:
        for c in b["cols"]:
            if c not in acols:
                acols.append(c)

    TAPP_DIR = bt.TAPP_DIR
    PARAM_BASE = bt.PARAM_BASE
    DETAIL_DIR = bt.DETAIL_DIR
    detail_name = os.path.basename(DETAIL_DIR)
    component_types = bt.CFG.get("component_types") or []
    os.makedirs(DETAIL_DIR, exist_ok=True)
    written, detail_written = [], []
    for idx, pc in enumerate(pub_cols):
        hdr_txt = norm(hdr[pc])
        code = short_code(hdr_txt, idx)
        # de-dup codes
        base = code; k = 1
        while code in [w[0] for w in written]:
            k += 1; code = f"{base}-{k}"
        inst = {"@context": CTX, "@id": f"ex:{tapp}-{code}",
                "@type": ["cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"],
                "schema:name": "", "schema:description":
                    f"{tapp} instance derived from {hdr_txt} (publication column of {os.path.basename(bt.XLSX)})."}
        # identity
        for it in inherited_items:
            v = cell(pubval[it].get(pc))
            if v:
                place_identity(inst, it, sp_by_item[it], v)
        if not inst.get("schema:name"):
            inst["schema:name"] = f"{short} protocol — {code}"
        if "schema:measurementTechnique" not in inst:
            inst["schema:measurementTechnique"] = {"@type": ["schema:DefinedTerm"],
                                                   "schema:name": short, "schema:termCode": short}
        # Basic props
        mode_names = R.get("mode_names") or []
        for b in R["tapp_prop"]:
            key = "ada:" + b["name"] + ("Default" if b["A"] == "Editable" else "")
            v = cell(pubval[b["item"]].get(pc))
            if b["name"] == "analyticalMode":
                key = "ada:analyticalMode"  # never …Default
                if v:
                    matched = [m for m in mode_names if m.lower() in v.lower()]
                    inst[key] = matched if matched else ([] if b["cov"] > 0 else None)
                elif b["cov"] > 0:
                    inst[key] = []
                else:
                    inst[key] = None
                if inst.get(key) is None:
                    inst.pop(key, None)
                continue
            if v:
                inst[key] = v
            elif b["cov"] > 0:
                inst[key] = (-9999 if b["jtype"] in ("number", "integer") else "missing")
        # Advanced params
        saps = []
        for b in R["method_param"]:
            v = cell(pubval[b["item"]].get(pc))
            if not v:
                continue
            md = b["name"] + "Default"
            e = {"@id": f"{PARAM_BASE}/{md}", "@type": ["schema:PropertyValueSpecification"],
                 "schema:valueName": md, "schema:name": b["item"], "ada:dataType": b["jtype"],
                 "ada:fieldScope": "session", "schema:readonlyValue": False, "ada:tier": "R",
                 "schema:defaultValue": v}
            if b.get("unit") and b["unit"] != "free":
                e["schema:unitText"] = b["unit"]
            saps.append(e)
        for b in R["method_value"]:
            v = cell(pubval[b["item"]].get(pc))
            if not v:
                continue
            e = {"@id": f"{PARAM_BASE}/{b['name']}", "@type": ["schema:PropertyValue"],
                 "schema:propertyID": f"{PARAM_BASE}/{b['name']}", "schema:name": b["item"],
                 "schema:value": v}
            if b.get("unit") and b["unit"] != "free":
                e["schema:unitText"] = b["unit"]
            saps.append(e)
        if saps:
            inst["schema:additionalProperty"] = saps
        # analyteTemplate
        if acols and analyte_row:
            av = norm(pubval[analyte_row].get(pc))
            analytes = parse_analytes(av) if av else []
            if analytes:
                idcol = {"@type": ["schema:PropertyValueSpecification"],
                         "schema:name": "Analyzed constituent", "schema:valueName": "analyte",
                         "ada:dataType": "string", "schema:readonlyValue": True,
                         "schema:valueRequired": True, "ada:tier": "M"}
                inst["ada:analyteTemplate"] = {"ada:analyteColumns": [idcol],
                                               "ada:defaultAnalytes": [{"analyte": a} for a in analytes]}
        fp = os.path.join(TAPP_DIR, f"example{tapp}-{code}.json")
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(inst, f, indent=2, ensure_ascii=False)
            f.write("\n")
        written.append((code, hdr_txt))
        # paired analysis-level detail-block example
        dinst = build_detail(tapp, code, pc, R, pubval, PARAM_BASE, detail_name, component_types)
        with open(os.path.join(DETAIL_DIR, f"example{detail_name}-{code}.json"),
                  "w", encoding="utf-8", newline="\n") as f:
            json.dump(dinst, f, indent=2, ensure_ascii=False)
            f.write("\n")
        detail_written.append((code, hdr_txt))

    # examples.yaml
    import yaml
    entries = [{"title": f"{tapp} example {code}",
                "content": f"{tapp} instance derived from {lbl}.",
                "prefixes": CTX,
                "snippets": [{"language": "json", "ref": f"example{tapp}-{code}.json"}]}
               for code, lbl in written]
    with open(os.path.join(TAPP_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(entries, f, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    print(f"wrote {len(written)} {tapp} examples: {[c for c, _ in written]}")

    dentries = [{"title": f"{detail_name} example {code}",
                 "content": f"{detail_name} instance derived from {lbl}.",
                 "prefixes": {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"},
                 "snippets": [{"language": "json", "ref": f"example{detail_name}-{code}.json"}]}
                for code, lbl in detail_written]
    with open(os.path.join(DETAIL_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(dentries, f, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    print(f"wrote {len(detail_written)} {detail_name} examples")


if __name__ == "__main__":
    main()
