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
import glob, json, os, re, sys
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_tapp as bt  # noqa: E402
import schemapath_io  # noqa: E402
import schema_path_example_emitter as ex  # noqa: E402  (shared nested path interpreter)

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
    elif "prov:wasDerivedFrom" in sp:
        # Procedure Reference(s): the publication(s) the procedure was derived from, kept as a plain
        # string citation. Previously this row's sidecar path ended in a nested ...schema:target.schema:name,
        # which the greedy schema:name branch below grabbed for the TAPP's own name.
        inst["prov:wasDerivedFrom"] = v
    elif sp.strip() == "$MethodDefinition.schema:name":
        # The TAPP's own name (Procedure Name) is the ONLY row mapped to the top-level schema:name.
        # Match the exact top-level path: any nested ...schema:name (reference target, instrument
        # model, location) has its own branch and must not hijack the procedure name.
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
        token = m.group(1) if m else "nxs:base_classes/NXinstrument.html"
        # additionalType carries a URI-shaped value as a sealed reference
        # and a free label as a plain string -- the selector can name
        # either ('Laser Ablation System' is a label, not a term). The
        # token itself stays a string: instrument_id() slugifies it, and
        # a dict there would silently rewrite every instrument @id.
        addl = {"@id": token} if ":" in token else token
        arr = inst.setdefault("schema:instrument", [])
        cur = next((i for i in arr if addl in (i.get("schema:additionalType") or [])), None)
        if cur is None:
            cur = {"@id": ex.instrument_id(token),
                   "@type": ["schema:Product", "schema:Thing"],
                   "schema:additionalType": [addl, {"@id": WIKIDATA_INSTRUMENT}],
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


def structural_paths(sp_by_item):
    """sp_by_item PLUS the paths the composed modules own, for the three ensure_* helpers below.

    A module-covered row is blanked in the technique sidecar — the module owns the placement — so
    sp_by_item cannot see the workflow step, instrument or component the module's $def still
    asserts a `contains` for. EPMA is the case that surfaced it: `Sample Preparation Method` moved
    into Module_Core in the 2026-09 delivery, the technique row went blank, and every EPMA example
    stopped declaring the `Sample preparation` step the composed schema requires.

    Deliberately SEPARATE from sp_by_item rather than merged into it: identity placement,
    inherited_items and the analyte row all read sp_by_item and must keep seeing only what the
    technique itself places. This union is structural — which containers must exist — and nothing
    else.
    """
    import module_composition as mc
    out = dict(sp_by_item)
    try:
        refs, _ = mc.plan(bt.XLSX)
    except Exception:
        return out
    for name, _defs in refs:
        side = os.path.join(ROOT, "docs", "modules", f"Module_{name}.schemapaths.csv")
        if not os.path.exists(side):
            continue
        for row in schemapath_io.read(side):
            it = (row.get("Metadata Item") or "").strip()
            sp = (row.get("Schema Path") or "").strip()
            if it and sp and not out.get(it):
                out[it] = sp
    return out


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
        st = next((s for s in steps if s.get("schema:name") == name), None)
        if st is None:
            # the overlay pins each step's kind on additionalType (Sample preparation is a
            # bios:LabProcess); a step declared without it cannot satisfy the contains
            steps.append({"@type": ["cdi:Activity", "schema:Action"], "schema:name": name,
                          "schema:additionalType": ["bios:LabProcess"], "schema:position": 0})
        else:
            # a step the path interpreter already built (from a step-scoped parameter) carries its
            # name and parameters but not the structural @type/additionalType the contains demands
            st.setdefault("@type", ["cdi:Activity", "schema:Action"])
            at = st.setdefault("schema:additionalType", [])
            if "bios:LabProcess" not in at:
                at.append("bios:LabProcess")
    steps.sort(key=lambda s: (uniq.index(s["schema:name"]) if s.get("schema:name") in uniq else 99))
    for i, s in enumerate(steps, 1):
        s["schema:position"] = i


_HASPART_SEL = re.compile(r"schema:instrument\[\s*schema:additionalType\s*=\s*'([^']+)'\s*\]"
                          r"\.schema:hasPart\[\s*schema:additionalType\s*=\s*'([^']+)'")


_TEMPLATE_COLS = {"ada:analyteTemplate": "ada:analyteColumns",
                  "ada:channelTemplate": "ada:channelColumns",
                  "ada:reportedPropertyTemplate": "ada:reportedPropertyColumns"}


def populate_template_columns(inst, tapp_res):
    """A keyed-table template requires its columns array, and the columns are the schema-side column
    DEFINITIONS (an identifier column plus the technique's own columns). The path interpreter leaves
    them out (they carry no per-publication value), so instantiate each column def from the resolved
    schema (const -> its value) and fill the template's required columns array."""
    if not isinstance(tapp_res, dict):
        return
    defs = tapp_res.get("$defs", {})

    def resolve(node):
        seen = 0
        while isinstance(node, dict) and isinstance(node.get("$ref"), str) and "#/$defs/" in node["$ref"] and seen < 8:
            node = defs.get(node["$ref"].split("#/$defs/")[1], {}); seen += 1
        return node

    # The columns constraint is split across the resolved schema: the base carries the required
    # identifier column as `contains` (inlined, not a named $def), the overlay carries the technique
    # columns as items.anyOf. Accumulate BOTH across every occurrence of the columns property.
    found = {}   # columns-key -> {"contains": schema|None, "branches": [schema, ...]}

    def walk(n):
        if isinstance(n, dict):
            for ckey in set(_TEMPLATE_COLS.values()):
                sub = (n.get("properties") or {}).get(ckey)
                if isinstance(sub, dict):
                    f = found.setdefault(ckey, {"contains": None, "branches": []})
                    if f["contains"] is None and isinstance(sub.get("contains"), dict):
                        f["contains"] = sub["contains"]
                    items = sub.get("items") or {}
                    f["branches"].extend(items.get("anyOf") or ([items] if items else []))
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
    walk(tapp_res)
    for tkey, ckey in _TEMPLATE_COLS.items():
        tpl = inst.get(tkey)
        f = found.get(ckey)
        if not (isinstance(tpl, dict) and ckey not in tpl and f):
            continue
        built, seen = [], set()
        for br in ([f["contains"]] if f["contains"] else []) + f["branches"]:
            rb = resolve(br)
            if not (isinstance(rb, dict) and (rb.get("properties") or rb.get("allOf"))):
                continue
            obj = ex.instance_from_def(rb)
            if not isinstance(obj, dict):
                continue                 # a non-object branch (bare string item) — not a column def
            vn = obj.get("schema:valueName")
            if vn in seen:
                continue
            seen.add(vn)
            built.append(obj)
        if built:
            tpl[ckey] = built


def _channel_value(col, raw):
    """Set the value of one channel column from its publication cell, with two special cases the
    channels need: a numeric column reported as "<number> <unit> <prose>" (Integration Time) splits
    into schema:value/unitText/description; a delimited free-text column (Interfering Species) splits
    on ';' into a list. The value key is schema:value (PropertyValue) or schema:defaultValue (Spec)."""
    vk = "schema:value" if "schema:value" in col else ("schema:defaultValue" if "schema:defaultValue" in col else None)
    if vk is None:
        return
    if not raw:
        # no publication value for this channel -> the transcription sentinel, not a fake placeholder
        col[vk] = -9999 if col.get("ada:dataType") in ("number", "integer") else "missing"
        return
    if col.get("schema:name") == "Interfering Species":
        # the one column whose value is a discrete delimited list (isotope interference pairs);
        # the schema admits a literal-or-list here (the deliberate channel-value exception).
        parts = [p.strip() for p in raw.split(";") if p.strip()]
        col[vk] = parts if len(parts) > 1 else raw
        return
    num, desc = ex.numify(raw, col.get("ada:dataType"))
    col[vk] = num
    if desc:                               # a number reported with prose -> keep the full text
        col["schema:description"] = desc


def populate_collector_config(inst, tapp_res, values=None):
    """Populate ada:collectorConfiguration.ada:channelColumns on the ICP-MS Collector component.

    Unlike the analyte table (a top-level template), an MC-ICP-MS defines its channels as columns of
    a collectorConfiguration that hangs off instrument[ICPMS].hasPart[Collector]; each channel row is
    a PropertyValue/PropertyValueSpecification column def whose identity is the row label. The schema
    pins those columns via channelColumns.allOf[].contains, so instantiate each, fill its value from
    the matching publication cell, and attach them to the Collector.
    """
    values = values or {}
    if not isinstance(tapp_res, dict):
        return
    defs = tapp_res.get("$defs", {})

    def resolve(node):
        seen = 0
        while isinstance(node, dict) and isinstance(node.get("$ref"), str) and "#/$defs/" in node["$ref"] and seen < 8:
            node = defs.get(node["$ref"].split("#/$defs/")[1], {}); seen += 1
        return node

    sch = None
    def find(n):
        nonlocal sch
        if isinstance(n, dict):
            cc = (n.get("properties") or {}).get("ada:collectorConfiguration")
            if isinstance(cc, dict) and sch is None and cc.get("type") == "array":
                sch = cc            # collectorConfiguration IS the channel-column array schema
            for v in n.values():
                find(v)
        elif isinstance(n, list):
            for v in n:
                find(v)
    find(tapp_res)
    if not sch:
        return
    branches = [a["contains"] for a in (sch.get("allOf") or [])
                if isinstance(a, dict) and isinstance(a.get("contains"), dict)]
    branches += (sch.get("items") or {}).get("anyOf") or []
    built, seen = [], set()
    for br in branches:
        rb = resolve(br)
        if not (isinstance(rb, dict) and (rb.get("properties") or rb.get("allOf"))):
            continue
        obj = ex.instance_from_def(rb)
        if not isinstance(obj, dict):
            continue
        key = obj.get("schema:valueName") or obj.get("schema:name")
        if key in seen:
            continue
        seen.add(key)
        _channel_value(obj, values.get(obj.get("schema:name")))
        built.append(obj)
    if not built:
        return
    for insn in inst.get("schema:instrument", []) or []:
        for part in (insn.get("schema:hasPart", []) or []):
            if isinstance(part, dict) and "Collector" in (part.get("schema:additionalType") or []):
                part["ada:collectorConfiguration"] = built   # the array of channel columns, directly


def populate_reported_properties(inst, tapp_res, values):
    """Build schema:variableMeasured ONLY when the procedure enumerates 'Reported Variables and
    Units'. Each reported property becomes the PropertyValueSpecification / PropertyValue the overlay
    defines, its value taken from the matching publication cell. When the field is empty (Zhang), the
    property is left off schema:variableMeasured and its value stays on its workflow step (the
    interpreter used the non-'reported property' path instead)."""
    if not values.get("Reported Variables and Units") or not isinstance(tapp_res, dict):
        return
    defs = tapp_res.get("$defs", {})

    def resolve(node):
        seen = 0
        while isinstance(node, dict) and isinstance(node.get("$ref"), str) and "#/$defs/" in node["$ref"] and seen < 8:
            node = defs.get(node["$ref"].split("#/$defs/")[1], {}); seen += 1
        return node

    sch = None
    def find(n):
        nonlocal sch
        if isinstance(n, dict):
            vm = (n.get("properties") or {}).get("schema:variableMeasured")
            # the technique OVERLAY copy carries generated column defs (items.anyOf / allOf-contains);
            # the permissive base copy does not — pick the overlay.
            if isinstance(vm, dict) and sch is None and (
                    (vm.get("items") or {}).get("anyOf") or vm.get("allOf")):
                sch = vm
            for v in n.values():
                find(v)
        elif isinstance(n, list):
            for v in n:
                find(v)
    find(tapp_res)
    if not sch:
        return
    branches = [a["contains"] for a in (sch.get("allOf") or [])
                if isinstance(a, dict) and isinstance(a.get("contains"), dict)]
    branches += (sch.get("items") or {}).get("anyOf") or []
    built, seen = [], set()
    for br in branches:
        rb = resolve(br)
        if not (isinstance(rb, dict) and (rb.get("properties") or rb.get("allOf"))):
            continue
        obj = ex.instance_from_def(rb)
        if not isinstance(obj, dict):
            continue
        key = obj.get("schema:name")
        if key in seen:
            continue
        seen.add(key)
        raw = values.get(key)
        vk = "schema:value" if "schema:value" in obj else ("schema:defaultValue" if "schema:defaultValue" in obj else None)
        if vk and raw:
            num, desc = ex.numify(raw, obj.get("ada:dataType"))
            obj[vk] = num
            if desc:
                obj["schema:description"] = desc
        built.append(obj)
    if built:
        inst["schema:variableMeasured"] = built


def type_instrument_tree(inst):
    """Normalise the instrument tree. Delegates to the ONE shared implementation.

    This used to carry its own copy of the rules, and the synthetic-example builder carried another.
    They drifted: the other supplied @id but typed components ["schema:Thing"] alone, which failed
    the component branch requiring schema:Product, and every ICP-MS detail -P0 example broke. One
    rule, one place.
    """
    ex.normalize_instrument_tree(inst)


def ensure_required_hasparts(inst, sp_by_item):
    """Declare every instrument sub-component the overlay selects on, even when unreported.

    An instrument's hasPart is `contains`-constrained the same way the top-level instrument array is
    — a Basic parameter scoped to (say) the ICP-MS Collector requires the ICP-MS to CONTAIN a
    Collector component. When the publication reports no value for that component it is never built,
    so the contains fails; declare it with the sentinel name, mirroring ensure_required_instruments.
    """
    pairs = {(m.group(1), m.group(2)) for sp in sp_by_item.values()
             for m in _HASPART_SEL.finditer(sp or "")}
    if not pairs:
        return
    for host, comp in sorted(pairs):
        ins = next((i for i in inst.get("schema:instrument", [])
                    if host in (i.get("schema:additionalType") or [])), None)
        if ins is None:
            continue
        parts = ins.setdefault("schema:hasPart", [])
        if not any(comp in (p.get("schema:additionalType") or []) for p in parts):
            parts.append({"@type": ["schema:Product", "schema:Thing"],
                          "schema:additionalType": [comp, {"@id": WIKIDATA_INSTRUMENT}],
                          "schema:name": "missing"})


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
            arr.append({"@id": ex.instrument_id(token),
                        "@type": ["schema:Product", "schema:Thing"],
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
    if t == "boolean":
        return False        # a required boolean with no reported value defaults to false (not applied)
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


def _enum_of(sub):
    """The enum list a (possibly array/anyOf-wrapped) subschema constrains a value to, or None."""
    if not isinstance(sub, dict):
        return None
    if isinstance(sub.get("enum"), list):
        return sub["enum"]
    it = sub.get("items")
    if isinstance(it, dict):
        e = _enum_of(it)
        if e:
            return e
    for br in (sub.get("anyOf") or sub.get("oneOf") or []):
        e = _enum_of(br)
        if e:
            return e
    return None


def _snap_enum(v, enum):
    """Snap a free-text value onto a strict enum. Returns (snapped_or_None, dropped_text_or_None).

    A publication states a controlled value with extra detail — "Transect (continuous line scan at
    2-6 µm s⁻¹)" for the option "Transect (continuous line scan)". Match an option as a substring of
    the value (value = option + detail, keep the detail to fold into the description), else the value
    inside an option, else the option's leading label (text before the first "("). No match -> None,
    leaving the value for the required-field sentinel.
    """
    strs = [o for o in enum if isinstance(o, str)]
    if v in strs:
        return v, None
    low = v.strip().lower()
    for o in sorted(strs, key=len, reverse=True):
        if o.lower() in low:
            return o, v
    for o in strs:
        if low in o.lower():
            return o, None
    for o in sorted(strs, key=len, reverse=True):
        head = o.split("(")[0].strip().lower()
        if head and low.startswith(head):
            return o, v
    return None, None


def _is_bool(sub):
    """True if the subschema constrains a value to a boolean (directly or via array/anyOf)."""
    if not isinstance(sub, dict):
        return False
    if sub.get("type") == "boolean":
        return True
    it = sub.get("items")
    if isinstance(it, dict) and _is_bool(it):
        return True
    return any(_is_bool(br) for br in (sub.get("anyOf") or sub.get("oneOf") or []))


def _bool_from_text(v):
    """Extract a boolean from a prose cell — the first standalone yes/no gives the value, the rest is
    returned to fold into the description. (None, None) when neither word is present.
    e.g. "Yes — correction for doubly charged ions: …" -> (True, "correction for doubly charged …")."""
    m = re.search(r"\b(yes|no)\b", v, re.I)
    if not m:
        return None, None
    return m.group(1).lower() == "yes", ((v[:m.start()] + v[m.end():]).strip(" —-:;,.\t") or None)


def conform_enums(inst, tapp_dir, technique_enum):
    """Snap free-text publication values onto the strict schema constraints the path interpreter
    cannot honour on its own — the technique code (kept as schema:name), controlled enum fields, and
    boolean fields carrying prose. The dropped detail is folded into schema:description. Mirrors the
    old tier-code normalisation."""
    for mt in inst.get("schema:measurementTechnique", []) or []:
        tc = mt.get("schema:termCode")
        if isinstance(tc, str) and technique_enum and tc not in technique_enum:
            code = technique_code(tc, technique_enum)
            if code != tc:
                mt.setdefault("schema:name", tc)
                mt["schema:termCode"] = code
    notes, props = [], _required_scalar_props(tapp_dir)[1]
    for key, val in list(inst.items()):
        if not key.startswith(("ada:", "schema:")) or key == "schema:measurementTechnique":
            continue
        sub = props.get(key, {})
        if _is_bool(sub):
            # a Boolean field the publication reported as prose ("Yes — corrections applied for …"):
            # take the yes/no as the value, fold the rest into the description.
            seq = val if isinstance(val, list) else [val]
            out = []
            for v in seq:
                b, rest = _bool_from_text(v) if isinstance(v, str) else (None, None)
                if b is None:
                    out.append(v)
                else:
                    out.append(b)
                    if rest:
                        notes.append(f"{key} = {rest}")
            inst[key] = out if isinstance(val, list) else out[0]
            continue
        enum = _enum_of(sub)
        if not enum:
            continue
        seq = val if isinstance(val, list) else [val]
        out = []
        for v in seq:
            if not isinstance(v, str) or v in enum:
                out.append(v)
                continue
            snapped, dropped = _snap_enum(v, enum)
            out.append(snapped if snapped is not None else v)
            if dropped:
                notes.append(f"{key} = {dropped}")
        inst[key] = out if isinstance(val, list) else out[0]
    if notes:
        inst["schema:description"] = (inst.get("schema:description", "").rstrip()
                                      + " Reported detail: " + "; ".join(notes) + ".").strip()


def conform_nested_enums(inst, resolved_schema, max_passes=4):
    """Snap any string value that violates an enum AT ANY DEPTH onto a matching option — the same
    normalisation conform_enums does for top-level fields, but validator-driven so it reaches nested
    fields (an instrument component's controlled schema:description: a publication reporting an
    electron source as 'Other: FEG …' is snapped to the enum's catch-all). Prevents the downstream
    fill pass from over-wrapping the unmatched string into an array. Mutates inst; returns count."""
    from jsonschema import Draft202012Validator
    V = Draft202012Validator(resolved_schema)
    total = 0
    for _ in range(max_passes):
        changed = 0
        for e in V.iter_errors(inst):
            enum = None
            for c in [e] + list(e.context or []):
                if c.validator == "enum" and isinstance(c.instance, str):
                    enum = c.validator_value
                    path = list(c.absolute_path)
                    break
            if enum is None or not path:
                continue
            parent = inst
            for step in path[:-1]:
                try:
                    parent = parent[step]
                except (KeyError, IndexError, TypeError):
                    parent = None
                    break
            if not isinstance(parent, (dict, list)):
                continue
            val = parent[path[-1]]
            if not isinstance(val, str) or val in enum:
                continue
            snapped, _ = _snap_enum(val, enum)
            if snapped is None:
                snapped = next((o for o in ("Unknown", "N/A", "None", "missing") if o in enum), None)
            if snapped is not None and snapped != val:
                parent[path[-1]] = snapped
                changed += 1
        total += changed
        if not changed:
            break
    return total


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
        # Only a param whose canonical path is the detail-ROOT schema:additionalProperty belongs in
        # this array. Skip ones that live on a workflow step (Sample Preparation Method -> the step's
        # schema:description) or nested under another node (Sample Persistent Identifier ->
        # schema:object[...].schema:additionalProperty) — the detail schema does not enumerate them
        # here, so dumping them makes the whole additionalProperty array reject.
        _cp = canon_sp.get(b["item"], "")
        for _root in ("$Dataset.", "$MethodDefinition."):
            if _cp.startswith(_root):
                _cp = _cp[len(_root):]
                break
        if not _cp.startswith("schema:additionalProperty"):
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


def _prune(dirpath, prefix, keep):
    """Delete example files for publications the table no longer has.

    examples.yaml is rewritten from `written`, so a removed publication vanishes from the manifest
    -- but its example<TAPP>-<Pub>.json stayed on disk and kept being validated. When Ruolin
    narrowed the SEM sub-technique tables (SEM_Composition 35 publication columns -> 9, SEM_FIBSEM
    -> 8, SEM_Imaging -> 18, removing columns that belonged to other SEM techniques), 70 orphaned
    files survived and failed the analyticalMode enum with modes their own table no longer declares.
    The failure reads as a schema bug; it is an artifact nothing owns.

    -P0 is NOT ours -- build_pathdriven writes it -- so it is always kept.
    """
    gone = []
    for f in sorted(glob.glob(os.path.join(dirpath, "example%s-*.json" % prefix))):
        code = os.path.basename(f)[len("example%s-" % prefix):-len(".json")]
        if code == "P0" or code in keep:
            continue
        os.remove(f)
        gone.append(code)
    if gone:
        print("  pruned %d example(s) with no publication column: %s" % (len(gone), gone))
    return gone


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: build_tapp_examples.py <tappName>")
    tapp = sys.argv[1]
    bt.configure(tapp)
    short = tapp.replace("TAPP", "")
    R = bt.route()
    # The 2026-08 delivery moved the tables to CSV, but this builder reads publication columns
    # through openpyxl. Every delivered table ships an .xlsx twin beside the .csv, so resolve that
    # rather than teaching the whole publication-column reader a second input format.
    src = bt.XLSX
    if src.lower().endswith(".csv"):
        twin = os.path.splitext(src)[0] + ".xlsx"
        if not os.path.exists(twin):
            raise SystemExit("%s is a .csv and no .xlsx twin exists beside it; this builder needs "
                             "the workbook form to read publication columns" % src)
        src = twin
    ws = openpyxl.load_workbook(src, data_only=True, read_only=True)["TAPP"]
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
    # md_items = items that have a $MethodDefinition (procedure-level) home; an item with only a
    # $Dataset path is analysis-level and must NOT be emitted as a TAPP (procedure) method parameter
    # even if its Procedure tier routes it there.
    canon_sp = {}
    md_items = set()
    _side = schemapath_io.csv_path(bt.XLSX)
    if os.path.exists(_side):
        for _row in schemapath_io.read(_side):
            _it = (_row.get("Metadata Item") or "").strip()
            _p = (_row.get("Schema Path") or "").strip()
            if _it:
                canon_sp[_it] = _p
                if _p.startswith("$MethodDefinition"):
                    md_items.add(_it)

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
    _res_path = os.path.join(TAPP_DIR, "resolvedSchema.json")
    tapp_res = json.load(open(_res_path, encoding="utf-8")) if os.path.exists(_res_path) else None
    _dres_path = os.path.join(DETAIL_DIR, "resolvedSchema.json")
    detail_res = json.load(open(_dres_path, encoding="utf-8")) if os.path.exists(_dres_path) else None
    written, detail_written = [], []
    for idx, pc in enumerate(pub_cols):
        hdr_txt = norm(hdr[pc])
        code = short_code(hdr_txt, idx)
        # de-dup codes
        base = code; k = 1
        while code in [w[0] for w in written]:
            k += 1; code = f"{base}-{k}"
        # PATH-DRIVEN placement: every reported cell is placed at its canonical sidecar path by the
        # shared nested interpreter, so instrument models, hasPart component params, workflow-step
        # params, target material, funding, references and the procedure name all land at their real
        # nested homes — no tier-based ada:<name> flattening, and schema + example stay identical.
        values = {it: cell(pubval[it].get(pc)) for it in pubval if cell(pubval[it].get(pc))}
        # a publication that lists Reported Variables populates schema:variableMeasured from the
        # 'reported property' rows; otherwise those rows defer to their non-reported counterparts.
        emit_rp = bool(cell(pubval.get("Reported Variables and Units", {}).get(pc)))
        md = ex.build_example(tapp, values=values, emit_reported_property=emit_rp)["MethodDefinition"]
        md.pop("@type", None)                          # the envelope owns the TAPP @type
        name = md.pop("schema:name", "") or f"{short} protocol — {code}"
        inst = {"@context": CTX, "@id": f"ex:{tapp}-{code}",
                "@type": ["prov:Plan", "cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol"],
                "schema:name": name,
                "schema:description":
                    f"{tapp} instance derived from {hdr_txt} (publication column of {os.path.basename(bt.XLSX)}).",
                **md}
        if "schema:measurementTechnique" not in inst:
            inst["schema:measurementTechnique"] = [{"@type": ["schema:DefinedTerm"],
                                                    "schema:name": short, "schema:termCode": short}]
        conform_enums(inst, TAPP_DIR, technique_enum)
        struct_sp = structural_paths(sp_by_item)
        ensure_required_steps(inst, struct_sp)
        ensure_required_instruments(inst, struct_sp)
        ensure_required_hasparts(inst, struct_sp)
        type_instrument_tree(inst)
        if tapp_res is not None:
            populate_template_columns(inst, tapp_res)
            populate_collector_config(inst, tapp_res, values)
            populate_reported_properties(inst, tapp_res, values)
        # complete what a schema path cannot carry — @type discriminators on nested nodes, the
        # instrument's Wikidata term / placeholder name, array cardinality — read off the resolved
        # schema; then sentinel every still-absent required field.
        if tapp_res is not None:
            conform_nested_enums(inst, tapp_res)     # snap nested controlled values before wrapping
            ex.fill_required_types(inst, tapp_res)
            ex.fill_structural_gaps(inst, tapp_res)
        fill_required_sentinels(inst, TAPP_DIR)
        fp = os.path.join(TAPP_DIR, f"example{tapp}-{code}.json")
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(inst, f, indent=2, ensure_ascii=False)
            f.write("\n")
        written.append((code, hdr_txt))
        # paired analysis-level detail-block example — apply the same structural completion the TAPP
        # example gets: type the instrument tree, fill @type/structural gaps, then sentinel every
        # still-absent required analysis field (ada:stepSize et al.).
        dinst = build_detail(tapp, code, pc, R, pubval, PARAM_BASE, detail_name, component_types, canon_sp)
        type_instrument_tree(dinst)
        if detail_res is not None:
            conform_nested_enums(dinst, detail_res)
            ex.fill_required_types(dinst, detail_res)
            ex.fill_structural_gaps(dinst, detail_res)
        fill_required_sentinels(dinst, DETAIL_DIR)
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
    _prune(TAPP_DIR, tapp, {c for c, _ in written})

    dentries = [{"title": f"{detail_name} example {code}",
                 "content": f"{detail_name} instance derived from {lbl}.",
                 "prefixes": {"schema": "http://schema.org/", "ada": "https://ada.astromat.org/metadata/"},
                 "snippets": [{"language": "json", "ref": f"example{detail_name}-{code}.json"}]}
                for code, lbl in detail_written]
    with open(os.path.join(DETAIL_DIR, "examples.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(dentries, f, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    print(f"wrote {len(detail_written)} {detail_name} examples")
    _prune(DETAIL_DIR, detail_name, {c for c, _ in detail_written})


if __name__ == "__main__":
    main()
