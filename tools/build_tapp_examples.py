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
import schemapath_io  # noqa: E402

# schema.org-typed marker the instrument BB requires every instrument to carry
WIKIDATA_INSTRUMENT = "https://www.wikidata.org/wiki/Q3099911"

CTX = {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/",
       "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/", "bios": "https://bioschemas.org/", "prov": "http://www.w3.org/ns/prov#"}
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


def technique_code(v, allowed):
    """The controlled technique code inside a publication cell.

    Cells qualify the code with prose the enum cannot carry — "LA-ICP-MS (193 nm excimer laser +
    ICP-MS; top-level technique)", "LA-ICP-MS (same as silicate protocol)". The code is the leading
    token; the qualification stays in schema:name, which is free text. Longest match first so
    LA-MC-ICP-MS is not shortened to LA-ICP-MS by a prefix test.
    """
    if not allowed or v in allowed:
        return v
    # "fs-"/"ns-"/"ps-" is the laser pulse width, not the mass analyser, and is recorded elsewhere
    s = re.sub(r"^(?:fs|ns|ps)-", "", v)
    if s in allowed:
        return s
    for cand in sorted(allowed, key=len, reverse=True):
        if s.startswith(cand):
            return cand
    # The release Technique list is the generic family (LA-ICP-MS); the analyser is already carried
    # by which TAPP this is. Drop the analyser token only if that yields a member — LA-MC-ICP-MS is
    # itself a member and must survive.
    generic = re.sub(r"^LA-(?:Q|SF|HR)-", "LA-", s)
    return generic if generic in allowed else s


def place_identity(inst, item, sp, v, allowed_techniques=()):
    """Place an inherited identity field's value into the JSON-LD envelope by schema path."""
    if "schema:measurementTechnique" in sp:
        # 1..* -> always a JSON array, per the repo-wide cardinality policy
        inst["schema:measurementTechnique"] = [{"@type": ["schema:DefinedTerm"],
                                                "schema:termCode": technique_code(v, allowed_techniques),
                                                "schema:name": v}]
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
        # 0..* -> array (upstream cdifProvActivity is array-only for schema:instrument). The overlay
        # selects instruments BY schema:additionalType — an LA-ICP-MS declares a "Laser Ablation
        # System" and an "ICPMS" separately — so the selector in the path decides which instrument a
        # row describes. Merging both manufacturer rows into one untyped instrument left the overlay's
        # `contains` unsatisfiable. additionalType also carries the Wikidata scientific-instrument
        # term the instrument BB requires of every instrument.
        m = re.search(r"schema:instrument\[\s*schema:additionalType\s*=\s*'([^']+)'", sp)
        token = m.group(1) if m else "nxs:BaseClass/NXinstrument"
        arr = inst.setdefault("schema:instrument", [])
        cur = next((i for i in arr if token in (i.get("schema:additionalType") or [])), None)
        if cur is None:
            cur = {"@type": ["schema:Product", "schema:Thing"],
                   "schema:additionalType": [token, {"@id": WIKIDATA_INSTRUMENT}],
                   "schema:name": ""}
            arr.append(cur)
        cur["schema:name"] = (cur.get("schema:name", "") + " " + v).strip()
    # other inherited fields (sample prep, references already handled) are skipped


# schema paths that bind a schema:description to a specific bios:computationalTool instance,
# e.g. "$MethodDefinition.bios:computationalTool[].schema:name='3d image registration' schema:description".
# route() classifies these as role=description and skips them; here we honour the instance binding.
_TOOL_DESC_RE = re.compile(r"bios:computationalTool\[\][.\s]*schema:name\s*=\s*'([^']*)'")


def tool_desc_selector(sp):
    """If sp binds a schema:description to a named bios:computationalTool, return that name; else None."""
    m = _TOOL_DESC_RE.search(sp)
    return m.group(1) if (m and "schema:description" in sp) else None


_INSTRUMENT_SEL = re.compile(r"schema:instrument\[\s*schema:additionalType\s*=\s*'([^']+)'")


_STEP_SEL = re.compile(r"schema:actionProcess\.schema:step\[\s*schema:name\s*=\s*'([^']+)'")


def place_parameter(inst, entry, sp):
    """Attach one parameter where its schema path puts it, not blindly at the TAPP root.

    An LA parameter is often scoped to a part rather than the procedure: ICP Tuning and Memory Effect
    Mitigation hang off the ICP-MS instrument, Laser Energy off the laser, Spike/Outlier Filtering and
    Signal Smoothing off the 'Data reduction' workflow step. The root schema:additionalProperty is an
    anyOf enumerating only the parameters that genuinely live there, so root-placing a scoped
    parameter fails against every branch — this was the whole of the original 32-error report.
    Returns True when the parameter has been placed here.
    """
    if ".ada:analyteTemplate" in sp:
        return True          # an analyte-template column, emitted with the template, not as a parameter
    m = _INSTRUMENT_SEL.search(sp)
    if m:
        for i in inst.get("schema:instrument", []):
            if m.group(1) in (i.get("schema:additionalType") or []):
                i.setdefault("schema:additionalProperty", []).append(entry)
                return True
        return True          # selector declared but instrument absent: drop rather than misplace
    m = _STEP_SEL.search(sp)
    if m:
        proc = inst.setdefault("schema:actionProcess", {"@type": ["schema:HowTo"], "schema:step": []})
        steps = proc.setdefault("schema:step", [])
        step = next((s for s in steps if s.get("schema:name") == m.group(1)), None)
        if step is None:
            # $defs/WorkflowStep: @type must carry both cdi:Activity and schema:Action, and
            # schema:position is required — a step is an ordered activity, not a bare HowToStep.
            step = {"@type": ["cdi:Activity", "schema:Action"], "schema:name": m.group(1),
                    "schema:additionalType": ["bios:LabProcess"],
                    "schema:position": len(steps) + 1}
            steps.append(step)
        step.setdefault("schema:additionalProperty", []).append(entry)
        return True
    return False


def ensure_required_steps(inst, sp_by_item):
    """Declare every workflow step the sidecar selects on, in workbook order.

    Same reason as ensure_required_instruments: the overlay asserts `contains` a step of each name,
    which an absent step cannot satisfy, so a publication reporting no parameter for (say) sample
    preparation still has to declare the step. Order follows the procedure, not the alphabet.
    """
    wanted = [m for sp in sp_by_item.values() for m in _STEP_SEL.findall(sp or "")]
    if not wanted:
        return
    order = ["Sample preparation", "Data acquisition", "Data reduction"]
    uniq = sorted(set(wanted), key=lambda s: (order.index(s) if s in order else len(order), s))
    proc = inst.setdefault("schema:actionProcess", {"@type": ["schema:HowTo"], "schema:step": []})
    steps = proc.setdefault("schema:step", [])
    for name in uniq:
        if not any(s.get("schema:name") == name for s in steps):
            # the overlay pins each step's kind on additionalType (Sample preparation is a
            # bios:LabProcess); a step declared without it cannot satisfy the contains
            steps.append({"@type": ["cdi:Activity", "schema:Action"], "schema:name": name,
                          "schema:additionalType": ["bios:LabProcess"], "schema:position": 0})
    steps.sort(key=lambda s: (uniq.index(s["schema:name"]) if s.get("schema:name") in uniq else 99))
    for i, s in enumerate(steps, 1):
        s["schema:position"] = i


def ensure_required_instruments(inst, sp_by_item):
    """Declare every instrument the overlay selects on, even when no publication names it.

    The technique overlay asserts `contains` an instrument of each selected additionalType — an
    LA-ICP-MS must record both a laser ablation system and an ICP-MS. `contains` cannot be satisfied
    by an absent entry, so a publication that names only one of the two failed. The instrument is
    declared with the sentinel name, which says the source did not state the make and model rather
    than inventing one.
    """
    wanted = {m for sp in sp_by_item.values() for m in _INSTRUMENT_SEL.findall(sp or "")}
    if not wanted:
        return
    arr = inst.setdefault("schema:instrument", [])
    for token in sorted(wanted):
        if not any(token in (i.get("schema:additionalType") or []) for i in arr):
            arr.append({"@type": ["schema:Product", "schema:Thing"],
                        "schema:additionalType": [token, {"@id": WIKIDATA_INSTRUMENT}],
                        "schema:name": "missing"})


def place_tool_description(inst, item, selector, desc):
    """Attach an instance-bound description to the named bios:computationalTool: set it on an
    existing tool whose schema:name matches the selector (or the row label), else add a
    processing-tool entry named for the row carrying the description."""
    tools = inst.setdefault("bios:computationalTool", [])
    keys = {selector.strip().lower(), item.strip().lower()}
    for t in tools:
        if str(t.get("schema:name", "")).strip().lower() in keys:
            t["schema:description"] = desc
            return
    tools.append({"@type": ["schema:SoftwareApplication"], "schema:name": item,
                  "ada:toolRole": "reduction", "schema:description": desc})


_REQ_CACHE = {}


def _required_scalar_props(tapp_dir):
    """(required, all) maps of ada:/schema: property -> composed subschema, from resolvedSchema.json.

    A field a composition module owns is deliberately absent from the technique's own overlay, so it
    never reaches route()'s tapp_prop and the coverage-based sentinel cannot see it — yet the
    composed schema still requires it. Reading requiredness back off the built schema catches those
    (ablationSpotDuration, ablationPitDepthRate, carrierGasFlowRate and friends: 6 of every LA
    example's missing properties). The second map covers optional fields too, because conform() and
    the sentinel both need a property's declared shape whether or not it is required.
    """
    if tapp_dir in _REQ_CACHE:
        return _REQ_CACHE[tapp_dir]
    path = os.path.join(tapp_dir, "resolvedSchema.json")
    req, props = set(), {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)

        # Descend ONLY through composition keywords. Recursing into a property's own subschema
        # collects requiredness that belongs to a nested object — schema:geo, schema:latitude,
        # schema:termCode, ada:fieldScope — and hoists it to the TAPP root, which pollutes every
        # example with sentinels for properties the root never had. Requiredness is positional.
        COMPOSITION = ("allOf", "anyOf", "oneOf", "then", "else", "if")

        def walk(n):
            if isinstance(n, dict):
                for r in (n.get("required") or []):
                    if isinstance(r, str):
                        req.add(r)
                for k, v in (n.get("properties") or {}).items():
                    props.setdefault(k, v if isinstance(v, dict) else {})
                for k in COMPOSITION:
                    walk(n.get(k))
            elif isinstance(n, list):
                for v in n:
                    walk(v)
        walk(doc)
    out = ({k: props.get(k, {}) for k in req if k.startswith(("ada:", "schema:"))},
           {k: v for k, v in props.items() if k.startswith(("ada:", "schema:"))})
    _REQ_CACHE[tapp_dir] = out
    return out


def prop_schema(tapp_dir, key):
    """The composed subschema for one property, required or not."""
    return _required_scalar_props(tapp_dir)[1].get(key) or {}


def conform(value, sub):
    """Wrap a scalar in a list where the schema declares an array.

    Cardinality 1..*/0..* is always a JSON array in this repo, and the release moved several
    free-text fields to that shape (elementalFractionationCorrection, perAnalyteCalibrationStrategy).
    The publication columns hold one prose value per field, so a transcribed value has to be lifted
    into the array rather than assigned straight through.
    """
    if isinstance(sub, dict) and sub.get("type") == "array" and not isinstance(value, list):
        return [value]
    return value


def sentinel_for(sub):
    """The sentinel a subschema will actually accept, or None if no scalar can stand in.

    Follows the SCHEMA rather than the workbook's Data Type: the same field is a bare string in one
    TAPP and an array of strings in another (the 1..*/0..* cardinality policy makes every repeatable
    field an array), so a flat "missing" was landing in array-typed fields — perAnalyteCalibration-
    Strategy and elementalFractionationCorrection in every LA example. anyOf/oneOf are searched for a
    branch that is scalar or array, which is how the …Default numerics are declared.
    """
    if not isinstance(sub, dict):
        return None
    t = sub.get("type")
    if t == "array":
        inner = sentinel_for(sub.get("items") or {"type": "string"})
        return None if inner is None else [inner]
    if t in ("number", "integer"):
        return -9999
    if t == "string":
        return "missing"
    if t == "object":
        return None
    for branch in (sub.get("anyOf") or sub.get("oneOf") or []):
        got = sentinel_for(branch)
        if got is not None:
            return got
    return "missing" if t is None and not sub.get("properties") else None


def fill_required_sentinels(inst, tapp_dir):
    """Give every still-absent required field the transcription sentinel its schema accepts."""
    # sorted: the required set is a set, and unsorted iteration reordered keys on every rebuild,
    # producing a 385-line diff across the examples with no content change
    for key, sub in sorted(_required_scalar_props(tapp_dir)[0].items()):
        if key in inst:
            continue
        got = sentinel_for(sub)
        if got is not None:
            inst[key] = got


def coerce(v, jtype):
    """Coerce a string cell value to the JSON type implied by the field's data type."""
    if jtype in ("number", "integer"):
        m = re.match(r"-?\d+(?:\.\d+)?", v)
        if m:
            x = m.group(0)
            return int(x) if jtype == "integer" or "." not in x else float(x)
    return v


_SIMPLE_DATASET_LEAF = re.compile(r"^\$Dataset\.([A-Za-z]+:[A-Za-z0-9]+)$")


def build_detail(tapp, code, pc, R, pubval, param_base, detail_name, component_types, canon_sp=None):
    """Build one analysis-level detail-block instance from a publication column:
    componentType + required analysis-level (detail_req) fields + per-dataset
    schema:PropertyValue entries (detail_addl). Pairs with the TAPP example by @id."""
    canon_sp = canon_sp or {}
    ct = component_types[0] if component_types else "ada:Tabular"
    inst = {"@context": {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"},
            "@id": f"ex:{detail_name}-{code}", "@type": [ct], "ada:componentType": ct,
            "schema:measurementTechnique": [{"@id": f"ex:{tapp}-{code}"}]}
    seen = set()
    for b in R["detail_req"]:
        if b["name"] in seen:
            continue
        seen.add(b["name"])
        v = cell(pubval[b["item"]].get(pc))
        # Honor the canonical schema path for fields whose analysis-instance home is a SIMPLE
        # top-level $Dataset property, so the example key matches the (build_pathdriven) schema
        # exactly instead of the camelCase(item) fallback. This fixes drift such as
        # "Spot Diameter (Measured)" -> $Dataset.ada:spotDiameterMeasured (camel drops the
        # parenthetical to spotDiameter) and "Funding Source for Analysis" -> $Dataset.schema:funding
        # (the analysis-level grant, distinct from procedure funding $MethodDefinition.schema:funding;
        # ada:fundingSourceForAnalysis was a camelCase artifact). Nested / $MethodDefinition paths
        # keep the tolerated flat ada:<name> form (the schema does not require those keys).
        m = _SIMPLE_DATASET_LEAF.match(canon_sp.get(b["item"], ""))
        leaf = m.group(1) if m else None
        if leaf == "schema:funding":
            if v is not None:
                inst["schema:funding"] = [{"@type": ["schema:MonetaryGrant"], "schema:name": v}]
            elif not b["multivol_only"]:   # required -> sentinel
                inst["schema:funding"] = [{"@type": ["schema:MonetaryGrant"], "schema:name": "missing"}]
            continue
        key = leaf or ("ada:" + b["name"])
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
             # array form: schema:PropertyValue.propertyID is a list under additionalProperty /
             # variableMeasured, and a scalar only under schema:identifier (CDIF core guide)
             "schema:propertyID": [{"@id": f"{param_base}/{b['name']}"}], "schema:name": b["item"],
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

    # The release workbooks carry no `schema path` column — that placement moved out to the docs
    # sidecar, which is the whole point of the path-driven pipeline. Without this every identity
    # field silently fell back to a stub: schema:name became "<prefix> protocol — <code>" and
    # schema:measurementTechnique became {termCode: "laSficpms"}, the TAPP prefix rather than a
    # technique. Prefer the sidecar's $MethodDefinition path per item, keeping any in-workbook
    # column for the legacy workbooks that still have one.
    if sp_col is None:
        side = schemapath_io.csv_path(bt.XLSX)
        if os.path.exists(side):
            for row in schemapath_io.read(side):
                it, p = (row.get("Metadata Item") or "").strip(), (row.get("Schema Path") or "").strip()
                if it in sp_by_item and p.startswith("$MethodDefinition") and not sp_by_item[it]:
                    sp_by_item[it] = p

    # canonical schema paths (full sidecar map, all items) — authoritative for detail-key
    # placement so example keys match the build_pathdriven schema (which derives from these paths).
    canon_sp = {}
    _side = schemapath_io.csv_path(bt.XLSX)
    if os.path.exists(_side):
        for _row in schemapath_io.read(_side):
            _it = (_row.get("Metadata Item") or "").strip()
            if _it:
                canon_sp[_it] = (_row.get("Schema Path") or "").strip()

    inherited_items = {it for it, sp in sp_by_item.items()
                       if sp.startswith("$MethodDefinition") and ".ada:" not in sp
                       and "additionalProperty" not in sp and "schema:description" not in sp}
    # instance-bound tool descriptions (role=description rows targeting a named computationalTool)
    tool_desc_items = {it: sel for it, sp in sp_by_item.items()
                       if (sel := tool_desc_selector(sp)) is not None}
    analyte_row = next((it for it, sp in sp_by_item.items()
                        if "analyteTemplate.ada:defaultAnalytes" in sp or it == "Analyte"), None)
    acols = []
    for b in R["analyte_cols"]:
        for c in b["cols"]:
            if c not in acols:
                acols.append(c)

    TAPP_DIR = bt.TAPP_DIR
    PARAM_BASE = bt.PARAM_BASE
    # controlled technique codes, read off the composed schema so the cell prose can be reduced to
    # whatever this TAPP actually admits rather than a list hard-coded here
    # The property map keeps the first definition of a key it meets, which for measurementTechnique
    # is the permissive base anyOf; the technique overlay's narrowed copy carries the enum. Search
    # the composed document for it directly.
    _codes = []
    _rs = os.path.join(TAPP_DIR, "resolvedSchema.json")
    if os.path.exists(_rs):
        with open(_rs, encoding="utf-8") as _f:
            _doc = json.load(_f)

        def _find_codes(n):
            if isinstance(n, dict):
                sub = (((n.get("properties") or {}).get("schema:measurementTechnique") or {})
                       .get("items") or {})
                enum = ((sub.get("properties") or {}).get("schema:termCode") or {}).get("enum")
                if enum and not _codes:
                    _codes.extend(enum)
                for v in n.values():
                    _find_codes(v)
            elif isinstance(n, list):
                for v in n:
                    _find_codes(v)
        _find_codes(_doc)
    technique_enum = tuple(_codes)
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
                "@type": ["prov:Plan", "cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"],
                "schema:name": "", "schema:description":
                    f"{tapp} instance derived from {hdr_txt} (publication column of {os.path.basename(bt.XLSX)})."}
        # identity
        for it in sorted(inherited_items):   # sorted: inherited_items is a set; keep output deterministic
            v = cell(pubval[it].get(pc))
            if v:
                place_identity(inst, it, sp_by_item[it], v, allowed_techniques=technique_enum)
        for it, sel in sorted(tool_desc_items.items()):
            d = cell(pubval[it].get(pc))
            if d:
                place_tool_description(inst, it, sel, d)
        if not inst.get("schema:name"):
            inst["schema:name"] = f"{short} protocol — {code}"
        if "schema:measurementTechnique" not in inst:
            inst["schema:measurementTechnique"] = [{"@type": ["schema:DefinedTerm"],
                                                    "schema:name": short, "schema:termCode": short}]
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
                inst[key] = conform(v, prop_schema(TAPP_DIR, key))
            elif b["cov"] > 0 or b["P"] == "Basic":
                # A Basic procedure-tier field is required by the generated schema whether or not any
                # publication happens to report it, so `cov > 0` alone left every zero-coverage Basic
                # field absent and the example invalid against its own TAPP — 9 of the 11 missing
                # required properties per LA example. The sentinel says "the source does not state
                # this", which is what a transcription can honestly assert; omission cannot, since an
                # absent key is indistinguishable from not-applicable. Matches build_detail above.
                # The schema's own shape wins over the workbook Data Type — see sentinel_for.
                got = sentinel_for(prop_schema(TAPP_DIR, key))
                inst[key] = got if got is not None else (
                    -9999 if b["jtype"] in ("number", "integer") else "missing")
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
            if not place_parameter(inst, e, sp_by_item.get(b["item"], "")):
                saps.append(e)
        for b in R["method_value"]:
            v = cell(pubval[b["item"]].get(pc))
            if not v:
                continue
            e = {"@id": f"{PARAM_BASE}/{b['name']}", "@type": ["schema:PropertyValue"],
                 "schema:propertyID": [{"@id": f"{PARAM_BASE}/{b['name']}"}], "schema:name": b["item"],
                 "schema:value": v}
            if b.get("unit") and b["unit"] != "free":
                e["schema:unitText"] = b["unit"]
            if not place_parameter(inst, e, sp_by_item.get(b["item"], "")):
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
        ensure_required_steps(inst, sp_by_item)
        ensure_required_instruments(inst, sp_by_item)
        fill_required_sentinels(inst, TAPP_DIR)
        fp = os.path.join(TAPP_DIR, f"example{tapp}-{code}.json")
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(inst, f, indent=2, ensure_ascii=False)
            f.write("\n")
        written.append((code, hdr_txt))
        # paired analysis-level detail-block example
        dinst = build_detail(tapp, code, pc, R, pubval, PARAM_BASE, detail_name, component_types, canon_sp)
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
