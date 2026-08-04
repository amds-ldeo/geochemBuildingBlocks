"""Phase 0 of the nested-interpreter work: normalize TAPP workbook `schema path` values to the
canonical grammar in docs/SCHEMA_PATH_GRAMMAR.md.

Auto-fixes the mechanical cases (scheme:->schema:, dot->colon, selector unification, relatedLink
restructure, known typos) and emits a per-workbook machine-readable placement spec
`docs/<workbook>.schemapaths.json` ({Metadata Item -> {path, family}}). Everything it cannot
confidently normalize is FLAGGED (never guessed) and printed for human review.

    python tools/normalize_schema_paths.py           # write specs + review report
    python tools/normalize_schema_paths.py --dry-run # report only
"""
import json, os, re, sys
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schema_path_parser as spp
from extract_tapp_overrides import TIER_TAPPS


def _parses(canon):
    """A path is only truly canonical if the Phase-1 parser accepts it (keeps the normalizer's
    'canonical' verdict honest — a loose family recognizer can't smuggle a malformed path through)."""
    try:
        spp.parse(canon); return True
    except spp.SchemaPathError:
        return False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME_TYPOS = {"measuremnttechnique": "measurementTechnique",
              "phaseidentificatonmethod": "phaseIdentificationMethod",
              "meanangulardeviaton": "meanAngularDeviation",
              "laserflueence": "laserFluence"}
FIELDS = "(name|value|defaultValue|description|identifier|termCode|url|object)"


def preclean(s):
    s = " ".join(str(s).split())
    s = s.replace("scheme:", "schema:").replace("additiional", "additional").replace("Schema:", "schema:")
    # $cdif<Module> roots (cdifCore, cdifDiscovery, cdifProvenance, ...) all denote the product
    # document root -> alias to $Dataset so the dataset-side family recognizers apply (confirmed
    # with the author: cdifCore/cdifDiscovery/Dataset are the same technique-product-document root).
    s = re.sub(r"^\$cdif[A-Za-z]+\b", "$Dataset", s)
    for bad, good in NAME_TYPOS.items():
        s = re.sub(bad, good, s, flags=re.I)
    return s


def has_multitarget(s):
    # a top-level , | or " and " (outside [...] and '...') means the row sets several targets
    depth = 0; inq = False; i = 0
    while i < len(s):
        c = s[i]
        if c == "'": inq = not inq
        elif not inq and c == "[": depth += 1
        elif not inq and c == "]": depth -= 1
        elif not inq and depth == 0:
            if c == "," or c == "|": return True
            if s[i:i+5].lower() == " and ": return True
        i += 1
    return False


def malformed(s):
    if "special handling" in s.lower(): return "free-text"
    if s.count("[") != s.count("]"): return "unbalanced brackets"
    if s.rstrip().endswith(".") or s.rstrip().endswith("]."): return "trailing '.' / missing terminal"
    if "$type" in s or "@type =" in s or '@type ="' in s: return "@type selector (needs manual mapping)"
    return None


def mechanical(s):
    if s.startswith("$."):
        s = "$MethodDefinition" + s[1:]
    s = re.sub(r"\s+\.", ".", s)     # spaces around the '.' navigation separator
    s = re.sub(r"\.\s+", ".", s)
    s = re.sub(r"\s+\[", "[", s)     # space before a selector bracket
    s = s.replace("schema.additionalProperty", "schema:additionalProperty")  # dot -> colon before container
    s = re.sub(r"schema[.:]defaultvalue\b", "schema:defaultValue", s, flags=re.I)  # field-name case
    s = re.sub(r"schema\.(?=" + FIELDS + r"\b)", "schema:", s)   # dot -> colon before a field
    # additionalProperty comma-value shorthand: [].schema:name:'X' , schema:value -> [schema:name='X'].schema:value
    s = re.sub(r"\[\]\.schema:name[:=]'([^']*)'\s*,\s*schema:value", r"[schema:name='\1'].schema:value", s)
    s = re.sub(r"\[\s*", "[", s)
    s = re.sub(r"\s*\]", "]", s)
    # selector colon -> equals: [curie:'value'] -> [curie='value'] (e.g. [schema:roleName:'analyst'])
    s = re.sub(r"\[([a-z][A-Za-z]*:[A-Za-z]+):'", r"[\1='", s)
    s = re.sub(r"\s*=\s*", "=", s)
    # selector unification -> [schema:name='X']
    s = re.sub(r"\[\]\.schema:name[:=]'([^']*)'", r"[schema:name='\1']", s)
    s = re.sub(r"bios:computationalTool\[\]\.schema:name='([^']*)'", r"bios:computationalTool[schema:name='\1']", s)
    s = re.sub(r"schema:relatedLink\[\]\.schema:linkRelationship\[(?:schema:)?name='([^']*)'\]",
               r"schema:relatedLink[schema:linkRelationship='\1']", s)
    s = re.sub(r"schema:step\[\]\[(schema:(?:name|additionalType)='[^']*')\]", r"schema:step[\1]", s)
    s = re.sub(r"schema:additionalProperty\['([^']*)'\]", r"schema:additionalProperty[schema:name='\1']", s)
    s = re.sub(r"schema:additionalProperty\[name='([^']*)'\]", r"schema:additionalProperty[schema:name='\1']", s)
    s = re.sub(r"schema:additionalProperty\[([A-Za-z][A-Za-z0-9]*)\]", r"schema:additionalProperty[schema:name='\1']", s)
    # dqv inline selector -> array selector
    s = re.sub(r"dqv:hasQualityMeasurement\.dqv:isMeasurementOf='([^']*)'",
               r"dqv:hasQualityMeasurement[dqv:isMeasurementOf='\1']", s)
    # schema:object @type-list selector (the iSample MaterialSample) -> canonical additionalType selector
    s = re.sub(r"schema:object\[@type[^\]]*materialsample[^\]]*\]",
               r"schema:object[schema:additionalType='materialsample']", s)
    # space-before-terminal: "...] schema:description" -> "...].schema:description"
    s = re.sub(r"\]\s+(schema:(?:description|value|name))\b", r"].\1", s)
    # #3: additionalProperty terminal convention -> .schema:value (name-terminal or missing terminal)
    s = re.sub(r"(schema:additionalProperty\[schema:name='[^']*'\])\.schema:name$", r"\1.schema:value", s)
    s = re.sub(r"(schema:additionalProperty\[schema:name='[^']*'\])$", r"\1.schema:value", s)
    return s


# canonical-form family recognizers (return (canonical, family) or None)
SEL = r"\[(?:[a-z]+:[A-Za-z]+='[^']*')?\]|\[[a-z]+:[A-Za-z]+='[^']*'\]"
def recognize(s):
    root = "Dataset" if s.startswith("$Dataset") else ("MethodDefinition" if s.startswith("$MethodDefinition") else None)
    if root is None and s.startswith("$."):
        s = "$MethodDefinition" + s[1:]; root = "MethodDefinition"
    if root is None:
        return None, "no recognizable root"
    fams = [
        (r"^\$MethodDefinition\.ada:[A-Za-z][A-Za-z0-9]*(\[\])?$", "direct-ada"),
        (r"^\$Dataset\.ada:[A-Za-z][A-Za-z0-9]*(\[\])?$", "dataset-scalar"),
        (r"^\$MethodDefinition\.ada:analyteTemplate\.ada:analyteColumns\[\]$", "analyte-template"),
        (r"^\$MethodDefinition\.schema:description$", "protocol-description"),
        (r"^\$MethodDefinition\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:(value|defaultValue)$", "method-parameter"),
        (r"^\$MethodDefinition\.bios:computationalTool\[schema:name='[^']*'\](\.schema:description)?$", "computational-tool"),
        (r"^\$MethodDefinition\.bios:computationalTool\[\]$", "computational-tool-list"),
        (r"^\$MethodDefinition\.schema:relatedLink\[schema:linkRelationship='[^']*'\]\.schema:target(\.schema:(name|description|url))?$", "related-link"),
        (r"^\$MethodDefinition\.schema:actionProcess\.schema:step\[schema:(name|additionalType)='[^']*'\](\.schema:(name|description))?$", "workflow-step"),
        (r"^\$MethodDefinition\.schema:actionProcess\.schema:step\[schema:(name|additionalType)='[^']*'\]\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:value$", "workflow-step-parameter"),
        (r"^\$MethodDefinition\.schema:(name|identifier|datePublished)$", "inherited-identity"),
        (r"^\$MethodDefinition\.schema:object\[schema:additionalType='materialsample'\]\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:(value|defaultValue)(\[\])?$", "protocol-sample-parameter"),
        # instrument: a typed instrument array (selector=additionalType), optional component hasPart
        # (also selector=additionalType), carrying identity fields, direct ada: props, or parameters.
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.schema:(model|manufacturer)(\.schema:[A-Z][A-Za-z]*)?\.schema:name$", "instrument-identity"),
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.schema:(name|identifier|additionalType)$", "instrument-identity"),
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.ada:[A-Za-z][A-Za-z0-9]*(\[\])?$", "instrument-direct-ada"),
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:(value|defaultValue)$", "instrument-parameter"),
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.schema:hasPart\[schema:additionalType='[^']*'\]\.schema:(name|identifier)$", "instrument-component"),
        (r"^\$MethodDefinition\.schema:instrument\[schema:additionalType='[^']*'\]\.schema:hasPart\[schema:additionalType='[^']*'\]\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:(value|defaultValue)$", "instrument-component-parameter"),
        (r"^\$MethodDefinition\.schema:(creator|location|measurementTechnique|object|funding)\b.*", "inherited-identity"),
        # dataset side (belongs on the analysis session / detail, not the reusable protocol)
        (r"^\$Dataset\.schema:contributor\[schema:roleName='[^']*'\](\.schema:(name|identifier))?$", "dataset-contributor"),
        (r"^\$Dataset\.schema:measurementTechnique(\.schema:DefinedTerm)?\.schema:identifier$", "dataset-measurement-technique"),
        (r"^\$Dataset\.prov:wasGeneratedBy\.schema:(startDate|endDate)$", "dataset-provenance"),
        (r"^\$Dataset\.prov:wasGeneratedBy\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:value$", "dataset-prov-parameter"),
        (r"^\$Dataset\.prov:wasGeneratedBy\.schema:object\[schema:additionalType='materialsample'\]\.schema:(name|identifier)$", "dataset-sample"),
        (r"^\$Dataset\.prov:wasGeneratedBy\.schema:object\[schema:additionalType='materialsample'\]\.schema:additionalProperty\[schema:name='[^']*'\]\.schema:value$", "dataset-sample-parameter"),
        (r"^\$Dataset\.schema:funding$", "dataset-funding"),
        (r"^\$Dataset\.schema:relatedLink\[schema:linkRelationship='[^']*'\]\.schema:target(\.schema:(name|url|description))?$", "dataset-related-link"),
        (r"^\$Dataset\.dqv:hasQualityMeasurement\[dqv:isMeasurementOf='[^']*'\]\.dqv:value$", "dataset-quality"),
    ]
    for pat, fam in fams:
        if re.match(pat, s):
            return s, fam
    return None, "unrecognized after normalization"


# #2: multi-target rows resolved to a single primary canonical target (per user direction).
# The row's one value populates the primary; genuinely-secondary targets (e.g. ada:ablationMode,
# ada:sliceCount, an agent identifier) would need a separate workbook row and are not invented here.
MULTI_RESOLVE = {
    "Protocol Author": "$MethodDefinition.schema:creator.schema:name",
    "Analyst": "$Dataset.prov:wasGeneratedBy.schema:agent.schema:name",
    "Protocol DOI": "$Dataset.schema:measurementTechnique.schema:identifier",
    "Laser Spot Path / Ablation Mode": "$MethodDefinition.ada:spotPath",
    "Voxel Size and Image Stack Dimensions": "$Dataset.ada:voxelSize",
}


def special_resolve(item, s, reason):
    """Item-aware resolutions for #2/#3/#5. Returns (canonical, family) or (None, None)."""
    il = item.strip().lower()
    if il == "analyte":                                            # #5
        return "$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes[]", "analyte-identifier"
    if reason == "multi-target (split into separate rows)" and item in MULTI_RESOLVE:  # #2
        return MULTI_RESOLVE[item], "multi-target-primary"
    # #3: workflow-step additionalProperty with no selector -> the parameter is named for the row
    m = re.match(r"^(\$MethodDefinition\.schema:actionProcess\.schema:step\[schema:(?:name|additionalType)='[^']*'\])"
                 r"\.schema:additionalProperty\.schema:name$", s)
    if m:
        return f"{m.group(1)}.schema:additionalProperty[schema:name='{item}'].schema:value", "workflow-step-parameter"
    return None, None


def normalize(sp):
    s = mechanical(preclean(sp))
    if s.count("$MethodDefinition") + s.count("$Dataset") > 1:   # two roots => two targets
        return None, None, "multi-target (split into separate rows)"
    if has_multitarget(s):
        return None, None, "multi-target (split into separate rows)"
    m = malformed(s)
    if m:
        return None, None, m
    canon, fam = recognize(s)
    if canon and not _parses(canon):
        return None, None, "parser rejected after normalization"
    if canon:
        return canon, fam, None
    return None, None, fam  # fam holds the reason string here


def main():
    dry = "--dry-run" in sys.argv
    total_ok = total_flag = 0
    flagged = []
    for tapp in TIER_TAPPS:
        b.configure(tapp)
        ws = openpyxl.load_workbook(b.XLSX, data_only=True, read_only=True)["TAPP"]
        rows = list(ws.iter_rows(values_only=True))
        H = [b.norm(v).lower() for v in rows[0]]
        spc = next((i for i, v in enumerate(H) if v == "schema path"), None)
        spec = {}
        ok = flag = 0
        for r in rows[1:]:
            item = b.norm(r[0])
            if not item or re.match(r"^\d+\.\s", item):
                continue
            sp = b.norm(r[spc]) if spc is not None and spc < len(r) else ""
            if not sp:
                continue
            canon, fam, reason = normalize(sp)
            if not canon:
                canon, fam = special_resolve(item, mechanical(preclean(sp)), reason)
                if canon and not _parses(canon):
                    canon, fam = None, None
            if canon:
                spec[item] = {"path": canon, "family": fam}
                ok += 1
            else:
                flag += 1
                flagged.append((tapp, item, sp, reason))
        out = os.path.join(ROOT, "docs", os.path.splitext(os.path.basename(b.XLSX))[0] + ".schemapaths.json")
        if not dry:
            with open(out, "w", encoding="utf-8") as f:
                json.dump(spec, f, indent=2, ensure_ascii=False); f.write("\n")
        print(f"{tapp:16} canonical={ok:3}  flagged={flag:3}" + ("" if dry else f"  -> {os.path.relpath(out, ROOT)}"))
        total_ok += ok; total_flag += flag
    print(f"\nTOTAL canonical={total_ok}  flagged={total_flag}\n")
    print("=== FLAGGED FOR REVIEW (grouped by reason) ===")
    from collections import defaultdict
    byreason = defaultdict(list)
    for tapp, item, sp, reason in flagged:
        byreason[reason].append(f"[{tapp}] {item}: {sp}")
    for reason in sorted(byreason):
        print(f"\n-- {reason} ({len(byreason[reason])}) --")
        for line in byreason[reason][:40]:
            print(f"   {line}")


if __name__ == "__main__":
    main()
