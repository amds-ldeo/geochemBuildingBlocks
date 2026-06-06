"""One-shot: generate empaTAPP building block from the TAPP_EPMA_filled spreadsheet.

Reads docs/TAPP_EPMA_filled.xlsx (sheet 'TAPP') and emits, into
_sources/techniqueProtocols/empaTAPP/:

- vocab/<name>.json          one schema:DefinedTermSet per enum-typed row
- parameterTemplates/schema.yaml  registered collection BB: one $def per
                              readOnly:true method-parameter template
- analyteColumns/schema.yaml      registered collection BB: one $def per
                              analyteColumn row (schema:PropertyValueSpecification)
- schema.yaml properties     one entry per property-tagged row (overwrites the existing
                              POC schema.yaml's allOf[1].properties block)

Then generates 10 example empaTAPP instances (exampleempaTAPP-P1..P10.json) using
the publication columns H..Q. Each row's value in a given publication column populates
either the top-level property, a methodParameters entry (as schema:defaultValue), or a
defaultAnalytes hint.

Run from repo root: python tools/_build_empaTAPP.py
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from collections import OrderedDict
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

REPO_ROOT = Path(__file__).resolve().parent.parent

# Module-level configuration set by configure(). Defaults target empaTAPP for
# backward-compat — new TAPP profiles call configure(tapp_name, xlsx_path)
# before invoking build_tapp_artifacts() or build_detail_artifacts().
TAPP_NAME = "empaTAPP"
DETAIL_NAME = "detailEMPA"
XLSX = REPO_ROOT / "docs" / "TAPP_EPMA_filled.xlsx"
BB = REPO_ROOT / "_sources" / "techniqueProtocols" / TAPP_NAME
# Detail BBs were relocated from geochemProperties/ to analysisSpecificDetails/.
DETAIL_EMPA = REPO_ROOT / "_sources" / "analysisSpecificDetails" / DETAIL_NAME


# ---------- per-TAPP configuration ----------
# Each entry holds the technique-specific knobs. configure() copies the matching
# entry into CFG so the rest of the module can read CFG[...] without having to
# care which TAPP is being built. Default behavior is empaTAPP, so existing
# callers that don't set configure() still get bit-identical EMPA output.

TAPP_PROFILES: dict[str, dict] = {
    "empaTAPP": {
        "pubs": [
            ("P0", "Richard & Deng 2026 (synthetic comprehensive WDS example)"),
            ("P1", "Chi et al. 2015 (Tissintite, EPSL)"),
            ("P2", "Hu et al. 2020 (Coesite NWA8657, GCA)"),
            ("P3sil", "Liu et al. 2016 (Tissint silicate mineral chem., MAPS)"),
            ("P3phos", "Liu et al. 2016 (Tissint phosphate mineral chem., MAPS)"),
            ("P4", "Ma et al. 2017 (Liebermannite, MAPS)"),
            ("P5", "Frank et al. 2023 (Ivuna CAI, MAPS)"),
            ("P6", "Broussard et al. 2026 (OC002 CI chondrite, MAPS)"),
            ("P7", "Seifert et al. 2026 (Bennu apatite, MAPS)"),
            ("P8sil", "Zega et al. 2025 (Bennu silicates, Nat. Geosci.)"),
            ("P8carb", "Zega et al. 2025 (Bennu carbonates, Nat. Geosci.)"),
            ("P8phos", "Zega et al. 2025 (Bennu phosphates, Nat. Geosci.)"),
            ("P9sil", "McCoy et al. 2025 (Bennu silicates, Nature)"),
            ("P9carb", "McCoy et al. 2025 (Bennu carbonates, Nature)"),
            ("P9phos", "McCoy et al. 2025 (Bennu phosphates, Nature)"),
            ("P10", "Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)"),
            ("P10plag", "Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.)"),
        ],
        "p_end_col": 26,
        "instrument_addl_type": ["nxs:BaseClass/NXinstrument", "ada:EPMAInstrument"],
        "instrument_name_default": "EPMA instrument",
        "instrument_name_short": "EPMA",
        "termcode": "EPMA-WDS",
        "termname": "Electron Microprobe Analysis - WDS",
        "example_name_template": "EPMA TAPP example {code}",
        "detail_componenttype_default": "ada:EMPAQEATabular",
        "schema_title": "EMPA Technique-Aligned Protocol Profile (empaTAPP)",
        "schema_description": (
            "EMPA-specific extension of the base TAPP definition. Adds top-level EPMA "
            "properties (beam mode, accelerating voltage default, matrix correction "
            "method, etc.), Advanced-protocol parameter specifications in schema:additionalProperty, and an "
            "analyte-column template covering EPMA per-element acquisition and "
            "reporting fields. Each ada:analyteColumns[] entry must match one of the "
            "catalog files in analyteColumns/ (or the inherited identifier column from "
            "tappDefinition); each catalog file is itself a JSON Schema whose "
            "examples[0] carries the canonical instance. Generated from "
            "docs/TAPP_EPMA_filled.xlsx by tools/build_empaTAPP_from_spreadsheet.py."
        ),
        "detail_constraint_title": "detailEMPA additionalProperty constraint (generated from empaTAPP spreadsheet)",
        "detail_constraint_catchall_desc": (
            "Catch-all for additional schema:PropertyValue entries beyond those "
            "enumerated in the empaTAPP-derived catalog above."
        ),
        "detail_constraint_addprop_desc": (
            "Per-dataset schema:PropertyValue entries for this EMPA dataset. "
            "Each item is any of the empaTAPP-derived parameter types or "
            "(via the catch-all branch) any other PropertyValue. All entries "
            "are optional — include only the parameters you have values for."
        ),
        "example_description_template": "empaTAPP example derived from {pub_label}.",
        "has_wds_config": True,
        "emit_profile_examples": True,
    },
    "laicpmsTAPP": {
        "pubs": [
            ("Spot", "LA-ICPMS spot analysis mode"),
            ("Transect", "LA-ICPMS transect / line-scan mode"),
            ("Mapping", "LA-ICPMS 2-D mapping mode"),
        ],
        "p_end_col": 12,  # column M (Mapping) — only K, L, M used
        "instrument_addl_type": ["nxs:BaseClass/NXinstrument", "ada:LAICPMSInstrument"],
        "instrument_name_default": "LA-ICPMS instrument",
        "instrument_name_short": "LA-ICPMS",
        "termcode": "LA-ICPMS",
        "termname": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
        "example_name_template": "LA-ICPMS TAPP example {code}",
        "detail_componenttype_default": "ada:LAICPMSTabular",
        "schema_title": "LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP)",
        "schema_description": (
            "LA-ICPMS-specific extension of the base TAPP definition. Adds top-level "
            "LA-ICPMS properties, Advanced-protocol parameters in schema:additionalProperty, and "
            "an analyte-column template covering LA-ICPMS per-element acquisition and "
            "reporting fields. Each ada:analyteColumns[] entry must match one of the "
            "catalog files in analyteColumns/ (or the inherited identifier column from "
            "tappDefinition); each catalog file is itself a JSON Schema whose "
            "examples[0] carries the canonical instance. Generated from "
            "docs/TAPP_LAICPMS_filled.xlsx by tools/build_TAPP_from_spreadsheet.py."
        ),
        "detail_constraint_title": "detailLAICPMS additionalProperty constraint (generated from laicpmsTAPP spreadsheet)",
        "detail_constraint_catchall_desc": (
            "Catch-all for additional schema:PropertyValue entries beyond those "
            "enumerated in the laicpmsTAPP-derived catalog above."
        ),
        "detail_constraint_addprop_desc": (
            "Per-dataset schema:PropertyValue entries for this LA-ICPMS dataset. "
            "Each item is any of the laicpmsTAPP-derived parameter types or "
            "(via the catch-all branch) any other PropertyValue. All entries "
            "are optional — include only the parameters you have values for."
        ),
        "example_description_template": "laicpmsTAPP example for {pub_label}.",
        "has_wds_config": False,
        "emit_profile_examples": False,
    },
}

# Active per-TAPP configuration. Defaults to empaTAPP for backward-compat.
CFG: dict = dict(TAPP_PROFILES["empaTAPP"])

# Catalog conflicts encountered during this build run. Surfaced as warnings
# by share_or_write_catalog() instead of aborting the build, so a multi-TAPP
# regen can still emit per-TAPP artifacts when the shared catalog already
# owns an entry with semantically different content. Cleared at the start
# of each top-level build (build_tapp_artifacts / build_detail_artifacts).
CATALOG_CONFLICTS: list[dict] = []

# In-memory cache of the full analyteColumn catalog objects (incl. examples[0])
# keyed by name, populated by _classify_rows(emit_tapp=True). example_for_pub()
# reads canonical instances from here instead of the former flat per-name files
# (now collapsed into the analyteColumns registry schema.yaml $defs, which strip
# examples). Cleared/repopulated on each classify run.
ANALYTE_COLUMN_OBJS: "OrderedDict[str, dict]" = OrderedDict()


def configure(tapp_name: str, xlsx_path: str | Path | None = None) -> None:
    """Set module globals for a build run. tapp_name like 'empaTAPP' / 'laicpmsTAPP'.
    The detail BB name is derived as 'detail' + uppercase(strip-'TAPP'(tapp_name))
    — e.g. 'empaTAPP' → 'detailEMPA', 'laicpmsTAPP' → 'detailLAICPMS'.

    Looks up the per-TAPP knobs in TAPP_PROFILES and copies them into CFG so
    other functions can read CFG[...] without caring which TAPP is active."""
    global TAPP_NAME, DETAIL_NAME, XLSX, BB, DETAIL_EMPA, CFG
    TAPP_NAME = tapp_name
    short = tapp_name.replace("TAPP", "").upper()
    DETAIL_NAME = f"detail{short}"
    if xlsx_path is not None:
        p = Path(xlsx_path)
        XLSX = p if p.is_absolute() else REPO_ROOT / p
    BB = REPO_ROOT / "_sources" / "techniqueProtocols" / TAPP_NAME
    DETAIL_EMPA = REPO_ROOT / "_sources" / "analysisSpecificDetails" / DETAIL_NAME
    if tapp_name not in TAPP_PROFILES:
        raise ValueError(
            f"Unknown TAPP {tapp_name!r}. Add an entry to TAPP_PROFILES in "
            f"tools/_tapp_lib.py. Known: {sorted(TAPP_PROFILES)}"
        )
    CFG = dict(TAPP_PROFILES[tapp_name])

# Phase 1 dictionary directories — analyteColumns/parameterTemplates/parameterValues/vocab
# live at the techniqueProtocols root so multiple TAPPs can reference the same catalog
# entries by $ref. The generator writes catalog files here; per-TAPP schema.yaml files
# point at them with relative paths (e.g. ../analyteColumns/<name>.json from a TAPP folder).
TECH_PROTOCOLS = REPO_ROOT / "_sources" / "techniqueProtocols"
ANALYTE_COLUMNS_DIR = TECH_PROTOCOLS / "analyteColumns"
PARAMETER_TEMPLATES_DIR = TECH_PROTOCOLS / "parameterTemplates"
PARAMETER_VALUES_DIR = TECH_PROTOCOLS / "parameterValues"
VOCAB_DIR = TECH_PROTOCOLS / "vocab"

# Column indices in the spreadsheet (0-indexed; openpyxl uses 1-indexed +1).
# Layout (post-2026-04-29 reorder): structural columns are now adjacent to the
# A-F metadata block, so pub columns can grow at the end without disturbing
# anything else.
#   A-E (0..4):  item / desc / basic / dtype / example
#   F   (5):     "Last update" header (no data)
#   G-J (6..9):  level / schema_path / matchComment / impl
#   K-AA (10..26): P0..P10plag (17 pubs; can extend right indefinitely)
COL = {
    "item": 0, "desc": 1, "basic": 2, "dtype": 3, "example": 4,
    "level": 6, "schema_path": 7, "matchComment": 8, "impl": 9,
    "p_start": 10,  # column K = index 10 (first publication / mode column)
    # p_end is per-TAPP; read from CFG["p_end_col"] (26 for empaTAPP, 12 for laicpmsTAPP).
}


def _detect_columns(header_row) -> dict:
    """Resolve logical column -> 0-based index BY HEADER NAME, so a single reader
    handles both the empa-filled(-noInterp) layout (A-F, G=Level, H=schema path,
    I=matchComment, J=implementation notes, K+=pubs) and the newer Ruolin workbook
    layout (…Spot/Transect/Mapping, schema path/matchComment/implementation notes,
    Literature Assessment, then pubs). Publication columns are everything after the
    'Literature Assessment' separator when present, else everything after
    'implementation notes'."""
    def norm(v):
        return " ".join(str(v).split()).lower() if v is not None else ""
    H = [norm(v) for v in header_row]

    def find(pred, label, required=True):
        for i, h in enumerate(H):
            if pred(h):
                return i
        if required:
            raise ValueError(
                f"TAPP sheet header missing column for {label}. Headers seen: "
                f"{[h for h in H if h]}"
            )
        return None

    cols = {
        "item": find(lambda h: h == "metadata item", "Metadata Item"),
        "desc": find(lambda h: h.startswith("description"), "Description"),
        "dtype": find(lambda h: h == "data type", "Data Type"),
        "example": find(lambda h: h.startswith("example"), "Example/Allowed Content"),
        "schema_path": find(lambda h: h == "schema path", "schema path", required=False),
        "matchComment": find(lambda h: h.replace(" ", "") == "matchcomment", "matchComment", required=False),
        "impl": find(lambda h: h.startswith("implementation note"), "implementation notes"),
    }
    lit = find(lambda h: h == "literature assessment", "Literature Assessment", required=False)
    cols["p_start"] = (lit + 1) if lit is not None else (cols["impl"] + 1)
    return cols


def _pubs() -> list[tuple[str, str]]:
    """Return the active TAPP's publication-column list (code, label)."""
    return CFG["pubs"]


def _p_end() -> int:
    """Return the active TAPP's last publication-column index (inclusive)."""
    return CFG["p_end_col"]

# ---------- impl-notes parser ----------

# Each ROW may have one or more (kind, name) tags.
TAG_RE = re.compile(r"\b(property|parameter|analyteColumn)\s*:\s*([A-Za-z][A-Za-z0-9_-]+)", re.IGNORECASE)
DTYPE_RE = re.compile(r"\b(?:dataType|datatype|data:type)\s*:?\s*([A-Za-z:][A-Za-z0-9:_-]+)", re.IGNORECASE)
ENUM_RE = re.compile(r"enum\s*\{([^}]+)\}", re.IGNORECASE)
READONLY_RE = re.compile(r"\breadOnly\s*:?\s*(true|false)", re.IGNORECASE)
HASPART_RE = re.compile(
    r"schema:instrument\.schema:hasPart\[\]\.additionalType\s*=\s*['\"]([A-Za-z0-9_]+)['\"]"
)


def parse_impl(impl: str) -> dict:
    """Parse an impl-notes cell into a list of per-tag records.

    A single cell can carry multiple (kind, name) tags, each with its own
    readOnly / dtype / enum tokens in the chunk of text up to the next tag.
    Returns:
      {
        "tags": [(kind, name), ...],         # back-compat list
        "tag_records": [{"kind", "name", "readOnly", "dtype", "enum"}, ...],
        "dtype": <first row-level dtype>,    # back-compat for non-tag rows
        "enum":  <first row-level enum>,
        "readOnly": <first row-level readOnly>,
      }
    Per-tag fields are scoped to the substring of impl from the tag's start
    up to the next tag's start (or end of cell). This fixes the bug where
    a `property: X readonly:true` line on the same row as
    `parameter: Y readOnly:false` would clobber Y's readOnly value.
    """
    if not impl:
        return {"tags": [], "tag_records": [], "dtype": None, "enum": None, "readOnly": None}

    matches = list(TAG_RE.finditer(impl))

    def _scan_chunk(chunk: str) -> tuple[str | None, list[str] | None, bool | None]:
        dt = DTYPE_RE.search(chunk)
        dtype = dt.group(1).strip() if dt else None
        em = ENUM_RE.search(chunk)
        enum_vals = [v.strip() for v in em.group(1).split("|") if v.strip()] if em else None
        ro_m = READONLY_RE.search(chunk)
        ro = ro_m.group(1).lower() == "true" if ro_m else None
        return dtype, enum_vals, ro

    tag_records = []
    for i, m in enumerate(matches):
        kind = m.group(1).lower()
        name = m.group(2)
        chunk_end = matches[i + 1].start() if i + 1 < len(matches) else len(impl)
        chunk = impl[m.start():chunk_end]
        dtype, enum_vals, ro = _scan_chunk(chunk)
        tag_records.append({
            "kind": kind,
            "name": name,
            "dtype": dtype,
            "enum": enum_vals,
            "readOnly": ro,
        })

    # Row-level fallbacks for anything that scans the whole cell (legacy callers).
    row_dtype, row_enum, row_ro = _scan_chunk(impl)
    return {
        "tags": [(t["kind"], t["name"]) for t in tag_records],
        "tag_records": tag_records,
        "dtype": row_dtype,
        "enum": row_enum,
        "readOnly": row_ro,
    }


# ---------- spreadsheet reader ----------

def read_rows() -> list[dict]:
    import openpyxl
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    ws = wb["TAPP"]
    all_rows = list(ws.iter_rows(min_row=1, values_only=True))
    C = _detect_columns(all_rows[0])
    p_start = C["p_start"]
    p_end = p_start + len(_pubs())  # exclusive; one column per CFG["pubs"] entry

    def cell(r, key):
        idx = C.get(key)
        if idx is None or idx >= len(r) or r[idx] is None:
            return None
        return str(r[idx]).strip()

    rows = []
    for r in all_rows[1:]:
        item = cell(r, "item")
        impl = cell(r, "impl")
        if item is None and impl is None:
            continue
        rec = {
            "item": item,
            "desc": cell(r, "desc"),
            "dtype_col": cell(r, "dtype"),
            "example": cell(r, "example"),
            "schema_path": cell(r, "schema_path"),
            "matchComment": cell(r, "matchComment"),
            "impl": impl,
            "pubs": [r[i] if i < len(r) else None for i in range(p_start, p_end)],
        }
        rec["parsed"] = parse_impl(rec["impl"])
        rows.append(rec)
    return rows


# ---------- emit helpers ----------

def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def share_or_write_catalog(path: Path, data: dict) -> None:
    """Phase 3 reuse-detection. The shared catalog dirs at
    techniqueProtocols/{analyteColumns,parameterTemplates,parameterValues,vocab}/
    can be written by any TAPP's regen. Ownership is implied by the catalog
    file's $id: if the existing $id contains '/<this TAPP>/' the regen owns
    the entry and overwrites freely (handles spreadsheet edits in the owning
    TAPP). Otherwise the entry was originated by another TAPP — the new
    content must match exactly (sharing) or the regen errors out (collision).
    """
    if not path.exists():
        write_json(path, data)
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except (OSError, json.JSONDecodeError):
        # Unreadable existing file — overwrite.
        write_json(path, data)
        return

    # Ownership marker lives on $id for parameter/analyte catalog entries and on
    # @id (JSON-LD) for vocab DefinedTermSet entries — check both.
    new_id = (data.get("$id") or data.get("@id") or "")
    existing_id = (existing.get("$id") or existing.get("@id") or "")

    # If the existing file is owned by THIS TAPP's regen, overwrite.
    if f"/{TAPP_NAME}/" in existing_id:
        write_json(path, data)
        return

    # Foreign owner — must match exactly to share.
    if existing == data:
        return

    # Soft-share: catalog entries that differ ONLY in their TAPP-namespace
    # @id/$id/propertyID token (e.g. `ada:vocab/empaTAPP/Technique` vs
    # `ada:vocab/laicpmsTAPP/Technique`) are still semantically equal. Strip
    # the TAPP segment from any ada:vocab|parameter|analyteColumn URI in both
    # records and compare. If equal, leave the existing (foreign-owned) file
    # untouched — both TAPPs reference it via the same catalog filename.
    def _normalize(d):
        import copy
        d2 = copy.deepcopy(d)
        def walk(v):
            if isinstance(v, dict):
                for k in list(v.keys()):
                    if k in ("@id", "$id", "schema:propertyID") and isinstance(v[k], str):
                        v[k] = re.sub(
                            r"(ada:(?:vocab|parameter|analyteColumn)/)[A-Za-z0-9_]+/",
                            r"\1__/", v[k])
                    else:
                        walk(v[k])
            elif isinstance(v, list):
                for x in v:
                    walk(x)
        walk(d2)
        return d2
    if _normalize(existing) == _normalize(data):
        return

    # Surface as a warning rather than aborting the build — the existing
    # foreign-owned file stays put; this TAPP's regen keeps going. Authors
    # can reconcile the conflict by editing the spreadsheet (match the
    # existing definition to share, or rename the entry to claim a separate
    # catalog file).
    CATALOG_CONFLICTS.append({
        "path": str(path),
        "existing_id": existing_id,
        "new_id": new_id,
    })
    print(
        f"  CATALOG CONFLICT (skipped write) at {path.relative_to(REPO_ROOT)}:\n"
        f"    existing id={existing_id!r}\n"
        f"    new      id={new_id!r}"
    )


DEFINED_TERM_SET_SCHEMA_URI = (
    "https://cross-domain-interoperability-framework.github.io/"
    "metadataBuildingBlocks/_sources/schemaorgProperties/definedTermSet/schema.yaml"
)

_ADA_CONTEXT = OrderedDict([
    ("schema", "http://schema.org/"),
    ("ada", "https://ada.astromat.org/metadata/"),
])


def slugify_term_code(t: str) -> str:
    """Make a termCode string safe to embed in a URI fragment after `ada:`.

    Replaces any character outside the RFC 3986 unreserved set
    (ALPHA / DIGIT / `-` / `.` / `_` / `~`) with `_`, collapses runs of `_`,
    and strips leading/trailing `_`. The original termCode value is kept
    intact in schema:termCode; only the @id derived from it is slugified.
    """
    s = re.sub(r'[^A-Za-z0-9._~-]', '_', t)
    s = re.sub(r'_+', '_', s)
    return s.strip('_')


def vocab_obj(vname: str, label: str, desc: str, terms: list[str]) -> dict:
    """Canonical schema:DefinedTermSet instance, declaring conformance to the
    upstream CDIF schemaorgProperties/definedTermSet schema via $schema.

    Each term is a schema:DefinedTerm with its own @id of the form
    `ada:{slugify(termCode)}` (placeholder until the project adopts a real
    IRI scheme), schema:termCode (preserving the original spelling, including
    any special characters), and schema:name. Data producers supplement
    schema:name (human-readable label) and schema:description per term.

    @type fields use the array form to match the upstream schema's contains
    constraint on schema:DefinedTermSet / schema:DefinedTerm.
    """
    return OrderedDict([
        ("$schema", DEFINED_TERM_SET_SCHEMA_URI),
        ("@context", {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
        }),
        ("@id", f"ada:vocab/{TAPP_NAME}/{vname}"),
        ("@type", ["schema:DefinedTermSet"]),
        ("schema:name", label),
        ("schema:description", desc or f"Allowed values for {label}."),
        ("schema:hasDefinedTerm", [
            OrderedDict([
                ("@type", ["schema:DefinedTerm"]),
                ("@id", f"ada:{slugify_term_code(t)}"),
                ("schema:termCode", t),
                ("schema:name", t),
            ])
            for t in terms
        ]),
    ])


def map_dtype(dtype: str | None) -> str:
    """Map spreadsheet dataType to ada:dataType enum value (string|number|integer|boolean|date|uri)."""
    if not dtype:
        return "string"
    d = dtype.lower()
    if d in ("number", "numeric", "float", "decimal"):
        return "number"
    if d in ("integer", "int", "positive"):
        return "integer"
    if d in ("boolean", "bool"):
        return "boolean"
    if d in ("date",):
        return "date"
    if d in ("uri", "url"):
        return "uri"
    # schema:PropertyValue, enum, text, etc. → string
    return "string"


def parameter_obj(name: str, label: str, desc: str, dtype: str, enum_vname: str | None,
                  readOnly: bool | None, tier: str = "R") -> dict:
    """Hybrid JSON Schema + canonical instance for one method parameter.

    Pins ada:fieldScope to "session" (the conventional default for empaTAPP
    method parameters). The parent MethodParameter shape is enforced via
    the empaTAPP wrapper schema's items: $ref: MethodParameter that
    applies alongside this catalog file's discriminator constraints in
    the wrapper's oneOf — so the catalog file itself stays self-contained
    (no cross-folder $ref that the OGC bblocks postprocessor mishandles).
    """
    dt = map_dtype(dtype)
    ro = bool(readOnly) if readOnly is not None else False

    canonical = OrderedDict([
        ("@context", {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
        }),
        ("@id", f"ada:parameter/{TAPP_NAME}/{name}"),
        ("@type", ["schema:PropertyValueSpecification"]),
        ("schema:name", label),
        ("schema:valueName", name),
        ("schema:description", desc or label),
        ("ada:dataType", dt),
        ("ada:fieldScope", "session"),
        ("schema:readonlyValue", ro),
        ("ada:tier", tier),
    ])
    if enum_vname:
        canonical["schema:inDefinedTermSet"] = {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}

    properties = OrderedDict([
        ("@id", {"const": f"ada:parameter/{TAPP_NAME}/{name}"}),
        ("@type", {"const": ["schema:PropertyValueSpecification"]}),
        ("schema:valueName", {"const": name}),
        ("schema:name", {"const": label}),
        ("ada:dataType", {"const": dt}),
        ("ada:fieldScope", {"const": "session"}),
        ("schema:readonlyValue", {"const": ro}),
        ("ada:tier", {"const": tier}),
    ])
    if enum_vname:
        properties["schema:inDefinedTermSet"] = {
            "const": {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}
        }

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"ada:parameter/{TAPP_NAME}/{name}"),
        ("title", label),
        ("description", desc or label),
        ("type", "object"),
        ("properties", properties),
        ("required", [
            "@id", "@type",
            "schema:valueName", "schema:name", "ada:dataType", "ada:fieldScope",
        ]),
        ("examples", [canonical]),
    ])


def _value_type_for(dtype_col: str | None) -> tuple[str | list[str], str | None]:
    """Map the spreadsheet's Data Type column ('Numeric (kV)', 'Text (free)', ...) to a JSON Schema
    type for schema:value, plus an optional unit token (e.g. 'kV') extracted from parens."""
    if not dtype_col:
        return "string", None
    s = dtype_col.strip()
    unit = None
    m = re.search(r"\(([^)]+)\)", s)
    if m:
        unit = m.group(1).strip()
    low = s.lower()
    if "numeric" in low or "number" in low or "decimal" in low or "float" in low:
        return "number", unit
    if "integer" in low or low.startswith("int"):
        return "integer", unit
    if "boolean" in low or low.startswith("bool"):
        return "boolean", unit
    if "date" in low:
        return "date", unit
    return "string", unit


def additional_property_obj(name: str, label: str, desc: str, dtype_col: str | None,
                            enum_vname: str | None, dtype_impl: str | None) -> dict:
    """Hybrid JSON Schema + canonical instance for one detailEMPA additionalProperty.

    Models a schema:PropertyValue entry that carries an actual reading (per-dataset)
    rather than a parameter template. Pinned: @type, @context, schema:propertyID
    (= ada:parameter/empaTAPP/<name>), schema:name. schema:value type comes from the
    spreadsheet's Data Type column. schema:unitText is required (when the dtype
    carries a parenthesised unit like 'Numeric (kV)') but only type-checked as
    string — different authors may write 'µm' / 'um' / 'micrometer' / 'µm × µm'
    etc. The canonical form lives in the example instance, not as a const.
    """
    val_type, unit = _value_type_for(dtype_col)
    canonical_value = {
        "number": 0,
        "integer": 0,
        "boolean": False,
        "date": "1970-01-01",
        "string": "",
    }.get(val_type, "")

    parameter_uri = f"ada:parameter/{TAPP_NAME}/{name}"

    canonical = OrderedDict([
        ("@context", {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
        }),
        ("@id", parameter_uri),
        ("@type", ["schema:PropertyValue"]),
        ("schema:propertyID", parameter_uri),
        ("schema:name", label),
        ("schema:description", desc or label),
        ("schema:value", canonical_value),
    ])
    if unit:
        canonical["schema:unitText"] = unit
    if enum_vname:
        canonical["schema:inDefinedTermSet"] = {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}

    # schema.org's PropertyValue.value is a union of Number/Boolean/StructuredValue/Text.
    # For numeric/integer we accept either a typed number OR a string (publication-style
    # qualified values like "0 (focused)" or "1-2 um defocused" appear regularly in the
    # source data). Authors providing clean machine-readable instances should use the
    # numeric form; qualified-text form is allowed for fidelity to source publications.
    if val_type in ("number", "integer"):
        value_schema = {"anyOf": [{"type": val_type}, {"type": "string"}]}
    elif val_type == "date":
        value_schema = {"type": "string", "format": "date"}
    elif val_type == "boolean":
        value_schema = {"type": "boolean"}
    else:
        value_schema = {"type": "string"}

    properties = OrderedDict([
        ("@id", {"const": parameter_uri}),
        ("@type", {"const": ["schema:PropertyValue"]}),
        ("schema:propertyID", {"const": parameter_uri}),
        ("schema:name", {"const": label}),
        ("schema:value", value_schema),
    ])
    required = ["@id", "@type", "schema:propertyID", "schema:name", "schema:value"]
    if unit:
        # type-only (not const): authors often render the same unit different ways
        # ("µm" vs "um" vs "micrometer", "µm × µm" vs "µm x µm", etc.). The canonical
        # form is captured in the example instance below.
        properties["schema:unitText"] = {"type": "string"}
        required.append("schema:unitText")
    if enum_vname:
        properties["schema:inDefinedTermSet"] = {
            "const": {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}
        }

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", parameter_uri),
        ("title", label),
        ("description", desc or label),
        ("type", "object"),
        ("properties", properties),
        ("required", required),
        ("examples", [canonical]),
    ])


def analyte_column_obj(name: str, label: str, desc: str, dtype: str, enum_vname: str | None,
                       readOnly: bool | None, tier: str = "M") -> dict:
    """Hybrid JSON Schema + canonical instance for one analyte column.

    Top-level keywords form a JSON Schema constraining how this column must
    appear in a TAPP instance's ada:analyteColumns[]. The standard `examples`
    annotation carries the canonical JSON-LD instance — authoring apps read
    examples[0] to pre-fill forms; validators apply the schema body.
    """
    dt = map_dtype(dtype)
    ro = bool(readOnly) if readOnly is not None else True

    canonical = OrderedDict([
        ("@context", {
            "schema": "http://schema.org/",
            "ada": "https://ada.astromat.org/metadata/",
        }),
        ("@id", f"ada:analyteColumn/{TAPP_NAME}/{name}"),
        ("@type", ["schema:PropertyValueSpecification"]),
        ("schema:name", label),
        ("schema:valueName", name),
        ("schema:description", desc or label),
        ("ada:dataType", dt),
        ("schema:readonlyValue", ro),
        ("ada:tier", tier),
    ])
    if enum_vname:
        canonical["schema:inDefinedTermSet"] = {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}

    properties = OrderedDict([
        ("@id", {"const": f"ada:analyteColumn/{TAPP_NAME}/{name}"}),
        ("@type", {"const": ["schema:PropertyValueSpecification"]}),
        ("schema:valueName", {"const": name}),
        ("schema:name", {"const": label}),
        ("ada:dataType", {"const": dt}),
        ("schema:readonlyValue", {"const": ro}),
        ("ada:tier", {"const": tier}),
    ])
    if enum_vname:
        properties["schema:inDefinedTermSet"] = {
            "const": {"@id": f"ada:vocab/{TAPP_NAME}/{enum_vname}"}
        }

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"ada:analyteColumn/{TAPP_NAME}/{name}"),
        ("title", label),
        ("description", desc or label),
        ("type", "object"),
        ("properties", properties),
        ("required", [
            "@id", "@type",
            "schema:valueName", "schema:name", "ada:dataType",
        ]),
        ("examples", [canonical]),
    ])


# ---------- schema.yaml writer ----------

def _to_commented(obj):
    """Recursively convert nested dicts/lists into CommentedMap/CommentedSeq so
    ruamel.yaml emits them as plain YAML mappings/sequences instead of !!python tags."""
    if isinstance(obj, dict):
        cm = CommentedMap()
        for k, v in obj.items():
            cm[k] = _to_commented(v)
        return cm
    if isinstance(obj, list):
        cs = CommentedSeq()
        for x in obj:
            cs.append(_to_commented(x))
        return cs
    return obj


def _split_pipe_enum(s: str | None) -> list[str]:
    """Parse a 'A | B | C' style example value into a list of options."""
    if not s:
        return []
    return [v.strip() for v in s.split("|") if v.strip()]


def _haspart_known_branch(addtype: str, enum_vals: list[str] | None) -> dict:
    """Build one explicit oneOf branch for a spreadsheet-listed hasPart type."""
    props = OrderedDict([
        ("@type", {
            "type": "array",
            "items": {"type": "string"},
            "contains": {"const": "schema:Thing"},
        }),
        ("schema:additionalType", {
            "type": "array",
            "items": {"type": "string"},
            "contains": {"const": addtype},
        }),
    ])
    required = ["@type", "schema:additionalType"]
    if enum_vals:
        props["schema:name"] = {"type": "string", "enum": list(enum_vals)}
        required.append("schema:name")
    return OrderedDict([
        ("type", "object"),
        ("properties", props),
        ("required", required),
    ])


def _haspart_catchall_branch(known_addtypes: list[str]) -> dict:
    """Build the catch-all oneOf branch for sub-component types not enumerated
    above. Explicitly excludes the known types via `not: anyOf [contains: ...]`
    so it can't bypass the name-enum constraints carried by the known
    branches (oneOf requires mutually exclusive matches)."""
    return OrderedDict([
        ("type", "object"),
        ("description", (
            "Catch-all for instrument sub-component types not enumerated above. "
            "Authors may use any schema:additionalType outside the known set; "
            "schema:name is unconstrained on this branch."
        )),
        ("properties", OrderedDict([
            ("@type", {
                "type": "array",
                "items": {"type": "string"},
                "contains": {"const": "schema:Thing"},
            }),
            ("schema:additionalType", OrderedDict([
                ("type", "array"),
                ("items", {"type": "string"}),
                ("minItems", 1),
                ("not", OrderedDict([
                    ("anyOf", [{"contains": {"const": at}} for at in known_addtypes]),
                ])),
            ])),
        ])),
        ("required", ["@type", "schema:additionalType"]),
    ])


def build_haspart_constraint(rows: list[dict]) -> dict | None:
    """Build the empaTAPP overlay's schema:instrument.schema:hasPart constraint.

    Strategy:
    - For each spreadsheet row whose schema path matches
      "schema:instrument.schema:hasPart[].additionalType = '<X>'" emit an
      explicit oneOf branch pinning schema:additionalType to contain <X>
      (helps UI/forms tooling enumerate the known sub-component types).
      Rows whose Data Type is "Controlled list" with a pipe-delimited example
      additionally pin schema:name to that enum.
    - Append a catch-all oneOf branch that matches sub-components whose
      schema:additionalType contains NONE of the known consts. This lets
      authors add custom sub-component types we haven't thought of, without
      letting them bypass the known-branch name enums (mutual exclusion via
      `not: anyOf [...]`).
    """
    rows_meta = []
    for row in rows:
        schema_path = row.get("schema_path") or ""
        m = HASPART_RE.search(schema_path)
        if not m:
            continue
        addtype = m.group(1)
        enum_vals = None
        dtype_col = (row.get("dtype_col") or "").lower()
        if "controlled" in dtype_col:
            enum_vals = _split_pipe_enum(row.get("example")) or None
        rows_meta.append((addtype, enum_vals))

    if not rows_meta:
        return None

    branches = [_haspart_known_branch(at, ev) for at, ev in rows_meta]
    branches.append(_haspart_catchall_branch([at for at, _ in rows_meta]))

    return OrderedDict([
        ("type", "object"),
        ("properties", OrderedDict([
            ("schema:hasPart", OrderedDict([
                ("type", "array"),
                ("description", (
                    "Instrument sub-components. Each item is a schema:Thing "
                    "with at least one schema:additionalType. Spreadsheet-"
                    "known types: " + ", ".join(sorted(at for at, _ in rows_meta))
                    + ". Other additionalType values are accepted via the "
                    "catch-all branch."
                )),
                ("items", OrderedDict([("oneOf", branches)])),
            ])),
        ])),
    ])


def _write_catalog_registry(
    catalog_dir: Path,
    new_defs: "OrderedDict[str, dict]",
    *,
    owned_marker: str,
    title: str,
    description: str,
    bblock_name: str,
    bblock_abstract: str,
    bblock_tags: list[str],
) -> int:
    """Generic registered-collection-BB writer.

    Writes a $defs library at <catalog_dir>/schema.yaml plus a sibling
    bblock.json so the entries resolve locally through the building-block
    register (instead of being fetched as plain helper files). Each $def is the
    entry's JSON Schema body with $schema/$id/examples stripped
    (title/description/type/properties/required retained). Existing $defs owned
    by another TAPP are preserved (multi-TAPP union); $defs whose @id const
    starts with `owned_marker` belong to the active TAPP and are overwritten
    /inserted, with stale owned entries (no longer in `new_defs`) dropped.

    Returns the number of $defs contributed by this TAPP."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    # Emit identical inline mappings repeatedly rather than YAML anchors/aliases —
    # JSON Schema $defs are read by json/yaml.safe_load consumers that don't want
    # &id/*id references.
    yaml.representer.ignore_aliases = lambda *_args: True

    def _plain(v):
        """Recursively convert OrderedDict/dict → CommentedMap and list →
        CommentedSeq so ruamel.yaml emits plain mappings/sequences (no !!omap)."""
        if isinstance(v, dict):
            cm = CommentedMap()
            for k, vv in v.items():
                cm[k] = _plain(vv)
            return cm
        if isinstance(v, (list, tuple)):
            seq = CommentedSeq()
            for x in v:
                seq.append(_plain(x))
            return seq
        return v

    catalog_dir.mkdir(parents=True, exist_ok=True)
    out = catalog_dir / "schema.yaml"

    # Load any existing registry so multi-TAPP regen accumulates $defs (union).
    existing_defs: "OrderedDict[str, dict]" = OrderedDict()
    if out.exists():
        try:
            with open(out, "r", encoding="utf-8") as f:
                existing = YAML(typ="safe").load(f) or {}
            for k, v in (existing.get("$defs") or {}).items():
                existing_defs[k] = v
        except Exception:
            existing_defs = OrderedDict()

    def _is_owned(defn: dict) -> bool:
        try:
            return defn.get("properties", {}).get("@id", {}).get("const", "").startswith(owned_marker)
        except AttributeError:
            return False

    def _normalize_def(d):
        """Strip the TAPP-namespace token from any ada:vocab|parameter|analyteColumn
        URI const so two TAPPs' definitions of the same entry compare equal even
        though their @id/$id/propertyID/inDefinedTermSet differ only by the TAPP
        segment. Mirrors share_or_write_catalog._normalize so a shared catalog
        entry keeps a single owner (the first TAPP to define it) instead of being
        clobbered by a later build of an equivalent entry."""
        import copy
        d2 = copy.deepcopy(d)

        def walk(v):
            if isinstance(v, dict):
                for k in list(v.keys()):
                    if k in ("@id", "$id", "schema:propertyID") and isinstance(v[k], str):
                        v[k] = re.sub(
                            r"(ada:(?:vocab|parameter|analyteColumn)/)[A-Za-z0-9_]+/",
                            r"\1__/", v[k])
                    else:
                        walk(v[k])
            elif isinstance(v, list):
                for x in v:
                    walk(x)
        walk(d2)
        return d2

    # Start from ALL existing $defs (both this TAPP's prior entries and other
    # TAPPs' entries). This TAPP's own stale entries are pruned below; foreign
    # entries are preserved (union across TAPPs).
    merged: "OrderedDict[str, dict]" = OrderedDict(existing_defs)
    # Drop this TAPP's previously-owned entries so spreadsheet deletions/renames
    # don't leave stale $defs; they're re-added from new_defs if still present.
    for k in list(merged.keys()):
        if _is_owned(merged[k]):
            del merged[k]

    # Merge in this TAPP's $defs (strip $schema/$id/examples). Ownership semantics
    # mirror share_or_write_catalog: an entry whose name collides with a
    # foreign-owned $def is SHARED if the bodies normalize-equal (TAPP token
    # ignored) — keep the existing owner's $def; or a CONFLICT if they differ —
    # keep the existing owner's $def and warn (the first TAPP to define a name
    # owns it; the later TAPP must reconcile via the spreadsheet).
    for name, defn in new_defs.items():
        body = OrderedDict()
        for key, val in defn.items():
            if key in ("$schema", "$id", "examples"):
                continue
            body[key] = val
        existing_same = merged.get(name)
        if existing_same is not None:
            # existing_same is foreign-owned (this TAPP's own entries were dropped
            # above). Keep it; share silently if equal, warn if it conflicts.
            if _normalize_def(existing_same) != _normalize_def(body):
                ex_id = ((existing_same.get("properties") or {}).get("@id") or {}).get("const", "")
                new_id = ((body.get("properties") or {}).get("@id") or {}).get("const", "")
                CATALOG_CONFLICTS.append({
                    "path": str(out), "existing_id": ex_id, "new_id": new_id,
                })
                print(
                    f"  CATALOG CONFLICT (kept existing $def {name!r}) in "
                    f"{out.relative_to(REPO_ROOT)}:\n"
                    f"    existing id={ex_id!r}\n    new      id={new_id!r}"
                )
            continue
        merged[name] = body

    doc = CommentedMap()
    doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    doc["title"] = title
    doc["description"] = description
    doc["type"] = "object"
    defs_map = CommentedMap()
    for k, v in merged.items():
        defs_map[k] = _plain(v)
    doc["$defs"] = defs_map

    with open(out, "w", encoding="utf-8") as f:
        yaml.dump(doc, f)

    # Write resolvedSchema.json. These registries are self-contained $defs
    # libraries with no external $refs, so the resolved form is identical to
    # schema.yaml (resolve_schema.py --all skips them, and its --file mode strips
    # un-promoted inline $defs). The build owns this file so the audit's
    # "MISSING generated file: resolvedSchema.json" check passes and the resolved
    # form stays in lockstep with the source. Mirrors parameterValues.
    resolved = json.loads(json.dumps(doc))  # CommentedMap → plain dict
    resolved_path = catalog_dir / "resolvedSchema.json"
    with open(resolved_path, "w", encoding="utf-8") as f:
        json.dump(resolved, f, indent=4, ensure_ascii=False)
        f.write("\n")

    # Ensure the collection is a registered BB (bblock.json) so $refs resolve
    # locally via the register. Created once; left untouched if present.
    bblock_path = catalog_dir / "bblock.json"
    if not bblock_path.exists():
        bblock = OrderedDict([
            ("$schema", "metaschema.yaml"),
            ("name", bblock_name),
            ("abstract", bblock_abstract),
            ("isTypeLibrary", True),
            ("status", "under-development"),
            ("dateTimeAddition", "2026-05-20T00:00:00Z"),
            ("itemClass", "schema"),
            ("register", "cdif-building-block-register"),
            ("version", "0.1"),
            ("dateOfLastChange", "2026-05-20"),
            ("link", "https://github.com/usgin/geochemBuildingBlocks"),
            ("maturity", "draft"),
            ("scope", "unstable"),
            ("tags", bblock_tags),
            ("sources", [
                {"title": "ADA Metadata Schema v3",
                 "link": "https://github.com/amds-ldeo/metadata"},
            ]),
        ])
        write_json(bblock_path, bblock)
        print(f"  wrote {bblock_path.relative_to(REPO_ROOT)}")

    print(f"  wrote {out.relative_to(REPO_ROOT)} "
          f"({len(new_defs)} $defs for {TAPP_NAME}, {len(merged)} total)")
    return len(new_defs)


def write_parameter_values_registry(param_value_defs: "OrderedDict[str, dict]") -> None:
    """Write the registered parameterValues collection BB ($defs library) at
    _sources/techniqueProtocols/parameterValues/schema.yaml — one entry per
    readOnly:false parameter (keyed by name). Detail BBs reference these via
    fragment $refs (schema.yaml#/$defs/<name>) so they resolve locally through
    the register. Existing $defs owned by other TAPPs are preserved."""
    _write_catalog_registry(
        PARAMETER_VALUES_DIR, param_value_defs,
        owned_marker=f"ada:parameter/{TAPP_NAME}/",
        title="ADA Analytical Parameter Value Registry",
        description=(
            "Registry of reusable schema:PropertyValue parameter-value definitions "
            "derived from technique TAPP spreadsheets. Each $def constrains one "
            "per-dataset schema:PropertyValue entry. Detail building blocks reference "
            "these definitions via fragment $refs (schema.yaml#/$defs/<name>) so they "
            "resolve locally through the building-block register. The root only hosts "
            "$defs; it has no instantiable properties of its own."
        ),
        bblock_name="Analytical Parameter Value Registry",
        bblock_abstract=(
            "Registry of reusable schema:PropertyValue parameter-value "
            "definitions derived from technique TAPP spreadsheets. Hosts one "
            "$def per per-dataset parameter value. Detail building blocks "
            "reference these definitions via fragment $refs so they resolve "
            "locally through the register."
        ),
        bblock_tags=["ada", "astromat", "tapp", "parameter", "registry"],
    )


def write_analyte_columns_registry(analyte_column_defs: "OrderedDict[str, dict]") -> None:
    """Write the registered analyteColumns collection BB ($defs library) at
    _sources/techniqueProtocols/analyteColumns/schema.yaml — one entry per
    analyteColumn (keyed by name). TAPP BBs reference these via fragment $refs
    (schema.yaml#/$defs/<name>) so they resolve locally through the register.
    Existing $defs owned by other TAPPs are preserved (union)."""
    _write_catalog_registry(
        ANALYTE_COLUMNS_DIR, analyte_column_defs,
        owned_marker=f"ada:analyteColumn/{TAPP_NAME}/",
        title="ADA Analyte-Column Specification Registry",
        description=(
            "Registry of reusable schema:PropertyValueSpecification analyte-column "
            "definitions derived from technique TAPP spreadsheets. Each $def "
            "constrains one analyte-table reporting column (e.g. detectionLimit, "
            "xrayEmissionLine). TAPP building blocks reference these definitions via "
            "fragment $refs (schema.yaml#/$defs/<name>) so they resolve locally "
            "through the building-block register. The root only hosts $defs; it has "
            "no instantiable properties of its own."
        ),
        bblock_name="Analyte-Column Specification Registry",
        bblock_abstract=(
            "Registry of reusable schema:PropertyValueSpecification analyte-column "
            "definitions derived from technique TAPP spreadsheets. Hosts one $def "
            "per analyte-table reporting column. TAPP building blocks reference "
            "these definitions via fragment $refs so they resolve locally through "
            "the register."
        ),
        bblock_tags=["ada", "astromat", "tapp", "analyteColumn", "registry"],
    )


def write_parameter_templates_registry(parameter_template_defs: "OrderedDict[str, dict]") -> None:
    """Write the registered parameterTemplates collection BB ($defs library) at
    _sources/techniqueProtocols/parameterTemplates/schema.yaml — one entry per
    readOnly:true method parameter (keyed by name). TAPP BBs reference these via
    fragment $refs (schema.yaml#/$defs/<name>) so they resolve locally through
    the register. Existing $defs owned by other TAPPs are preserved (union)."""
    _write_catalog_registry(
        PARAMETER_TEMPLATES_DIR, parameter_template_defs,
        owned_marker=f"ada:parameter/{TAPP_NAME}/",
        title="ADA Method-Parameter Template Registry",
        description=(
            "Registry of reusable schema:PropertyValueSpecification method-parameter "
            "templates derived from technique TAPP spreadsheets. Each $def constrains "
            "one method-level (readOnly:true) parameter template (e.g. DriftCorrection, "
            "massAbsorptionCoefficients). TAPP building blocks reference these "
            "definitions via fragment $refs (schema.yaml#/$defs/<name>) so they resolve "
            "locally through the building-block register. The root only hosts $defs; it "
            "has no instantiable properties of its own."
        ),
        bblock_name="Method-Parameter Template Registry",
        bblock_abstract=(
            "Registry of reusable schema:PropertyValueSpecification method-parameter "
            "template definitions derived from technique TAPP spreadsheets. Hosts one "
            "$def per method-level parameter template. TAPP building blocks reference "
            "these definitions via fragment $refs so they resolve locally through the "
            "register."
        ),
        bblock_tags=["ada", "astromat", "tapp", "parameter", "template", "registry"],
    )


def write_detail_empa_constraint(detail_param_names: list[str]) -> None:
    """No-op for the constraint snippet: the per-dataset additionalProperty
    constraint now lives INLINE in the hand-authored detail schema.yaml's allOf,
    referencing the parameterValues registry $defs (schema.yaml#/$defs/<name>).
    The detail schema.yaml is hand-authored and never regenerated here, so this
    function only cleans up the legacy generated parametersConstraint.yaml if a
    stale copy is still present."""
    stale = DETAIL_EMPA / "parametersConstraint.yaml"
    if stale.exists():
        stale.unlink()
        print(f"  removed legacy {stale.relative_to(REPO_ROOT)} (constraint now inline in schema.yaml)")


def scaffold_detail_bb_if_missing() -> None:
    """Phase 4: when a brand-new detail BB directory has no schema.yaml or
    bblock.json yet, scaffold them so build_detail_artifacts() has somewhere
    to write parametersConstraint.yaml. Existing files are never overwritten —
    the user maintains the hand-authored componentType enum and any
    technique-specific properties on schema.yaml directly."""
    DETAIL_EMPA.mkdir(parents=True, exist_ok=True)
    schema_path = DETAIL_EMPA / "schema.yaml"
    if not schema_path.exists():
        yaml = YAML()
        yaml.preserve_quotes = True
        yaml.width = 4096
        yaml.indent(mapping=2, sequence=4, offset=2)
        doc = CommentedMap()
        doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        doc["title"] = f"{DETAIL_NAME} Instrument Detail"
        doc["description"] = (
            f"Detail block for {DETAIL_NAME} hasPart items. Discriminates on "
            f"ada:componentType (string). schema:measurementTechnique points "
            f"at the {TAPP_NAME} TAPP definition either by @id reference or "
            f"inline. Per-dataset schema:additionalProperty entries are "
            f"constrained by the generated parametersConstraint.yaml."
        )
        allof = CommentedSeq()
        # Hand-authored slot: componentType + measurementTechnique. componentType
        # enum is a TODO placeholder — fill in technique-specific values.
        hand = CommentedMap()
        hand["type"] = "object"
        props = CommentedMap()
        ct = CommentedMap()
        ct["description"] = (
            "Technique-specific component-type identifier. Replace this list "
            "with the actual ada:<technique>... consts for this BB."
        )
        ct["anyOf"] = CommentedSeq([{"const": "ada:TODO_ComponentType"}])
        props["ada:componentType"] = ct
        mt = CommentedMap()
        mt["description"] = (
            f"The {TAPP_NAME} TAPP definition this detail conforms to. Either "
            f"an @id reference or an inline definition."
        )
        mt_anyof = CommentedSeq()
        ref_branch = CommentedMap()
        ref_branch["type"] = "object"
        ref_props = CommentedMap()
        ref_props["@id"] = {"type": "string", "format": "uri"}
        ref_branch["properties"] = ref_props
        ref_branch["required"] = CommentedSeq(["@id"])
        mt_anyof.append(ref_branch)
        mt_anyof.append({"$ref": f"../../techniqueProtocols/{TAPP_NAME}/schema.yaml"})
        mt["anyOf"] = mt_anyof
        props["schema:measurementTechnique"] = mt
        hand["properties"] = props
        hand["required"] = CommentedSeq(["ada:componentType"])
        allof.append(hand)
        allof.append({"$ref": "parametersConstraint.yaml"})
        doc["allOf"] = allof
        with open(schema_path, "w", encoding="utf-8") as f:
            yaml.dump(doc, f)
        print(f"  scaffolded {schema_path.relative_to(REPO_ROOT)} (fill in ada:componentType)")

    bblock_path = DETAIL_EMPA / "bblock.json"
    if not bblock_path.exists():
        bblock = OrderedDict([
            ("$schema", "metaschema.yaml"),
            ("name", f"{DETAIL_NAME} Detail"),
            ("abstract", (
                f"Detail block for {DETAIL_NAME} hasPart items. Carries "
                f"per-dataset schema:additionalProperty entries (constrained "
                f"by parametersConstraint.yaml, generated from the {TAPP_NAME} "
                f"spreadsheet) and references the {TAPP_NAME} TAPP definition "
                f"via schema:measurementTechnique."
            )),
            ("status", "under-development"),
            ("itemClass", "schema"),
            ("register", "ada-building-block-register"),
            ("version", "0.1"),
            ("maturity", "draft"),
            ("scope", "unstable"),
            ("tags", ["ada", "geochem", DETAIL_NAME.lower()]),
        ])
        write_json(bblock_path, bblock)
        print(f"  scaffolded {bblock_path.relative_to(REPO_ROOT)}")


def _cleanup_legacy_flat_catalog(catalog_dir: Path, dir_basename: str) -> None:
    """Delete legacy flat per-name <name>.json catalog files owned by THIS TAPP
    under a now-registered collection BB dir. Preserves the registry artifacts
    (schema.yaml, bblock.json) and the generated derivatives
    (<dir>Schema.json, resolvedSchema.json). Foreign-owned flat files (other
    TAPPs not yet migrated) are left untouched. A flat file is identified by a
    top-level $id (per-name catalog entry); the registry/generated files don't
    carry a per-name $id of that form."""
    if not catalog_dir.exists():
        return
    protected = {"bblock.json", f"{dir_basename}Schema.json", "resolvedSchema.json"}
    for fp in catalog_dir.glob("*.json"):
        if fp.name in protected:
            continue
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f) or {}
        except (OSError, json.JSONDecodeError):
            continue
        existing_id = data.get("$id", "") or ""
        # Only legacy flat per-name catalog files carry an ada:.../<TAPP>/<name>
        # $id. The generated *Schema.json carries the registry's bblock $id form
        # (no per-name token), so it won't match this TAPP's ownership marker.
        if f"/{TAPP_NAME}/" in existing_id and "$defs" not in data:
            fp.unlink()
            print(f"  deleted legacy flat {fp.relative_to(REPO_ROOT)} (now a $def)")


def cleanup_orphan_param_files(empa_param_names: list[str], detail_param_names: list[str]) -> None:
    """Delete *.json under techniqueProtocols/parameterTemplates/ or
    techniqueProtocols/parameterValues/ that don't correspond to a current
    spreadsheet parameter row in the appropriate bucket. Avoids stale
    orphans after spreadsheet edits or readOnly toggles."""
    keep_empa = set(empa_param_names)
    if PARAMETER_TEMPLATES_DIR.exists():
        for fp in PARAMETER_TEMPLATES_DIR.glob("*.json"):
            if fp.stem not in keep_empa:
                fp.unlink()
                print(f"  deleted orphan {fp.relative_to(REPO_ROOT)}")
    # parameterValues is now a registered collection BB (schema.yaml $defs +
    # bblock.json), not a directory of flat per-name JSON files. Stale-$def
    # pruning happens inside write_parameter_values_registry; nothing to glob here.


def build_schema_yaml(properties: list[tuple[str, dict]],
                      analyte_column_names: list[str],
                      parameter_names: list[str],
                      instrument_haspart: dict | None,
                      required_props: list[str] | None = None) -> None:
    """Rebuild <TAPP>/schema.yaml with the new property set in allOf[1].properties
    and uniqueness constraints on ada:analyteColumns[] and schema:additionalProperty[]
    referencing the catalog files. Basic-protocol (property:) fields are listed in
    overlay.required (canonical dual-home model); Advanced-protocol (readOnly:true
    parameter:) fields are schema:additionalProperty[] PropertyValueSpecification entries
    (replacing the former ada:methodParameters)."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)

    doc = CommentedMap()
    doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    doc["title"] = CFG["schema_title"]
    doc["description"] = CFG["schema_description"]
    allof = CommentedSeq()
    allof.append({"$ref": "../tappDefinition/schema.yaml"})
    overlay = CommentedMap()
    overlay["type"] = "object"
    req_set = set(required_props or [])
    props = CommentedMap()
    for ada_prop, schema_block in properties:
        # convert OrderedDict (or any dict) to CommentedMap so ruamel.yaml emits plain mapping
        cm = CommentedMap()
        for k, v in schema_block.items():
            if isinstance(v, list):
                vals = list(v)
                # required enum props may be sentinel-filled with "missing" when a
                # publication doesn't report them -> the sentinel must be a valid term.
                if k == "enum" and ada_prop in req_set and "missing" not in vals:
                    vals.append("missing")
                seq = CommentedSeq()
                for x in vals:
                    seq.append(x)
                cm[k] = seq
            else:
                cm[k] = v
        props[ada_prop] = cm

    if analyte_column_names:
        anyof = CommentedSeq()
        anyof.append({"$ref": "../tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn"})
        for col_name in sorted(analyte_column_names):
            anyof.append({"$ref": f"../analyteColumns/schema.yaml#/$defs/{col_name}"})

        ac_items = CommentedMap()
        ac_items["anyOf"] = anyof

        # Per-catalog uniqueness: at most one occurrence of each column type.
        # (The identifier column's exactly-once constraint lives in tappDefinition
        # via contains + maxContains: 1.)
        ac_unique = CommentedSeq()
        for col_name in sorted(analyte_column_names):
            cm = CommentedMap()
            cm["contains"] = {"$ref": f"../analyteColumns/schema.yaml#/$defs/{col_name}"}
            cm["minContains"] = 0
            cm["maxContains"] = 1
            ac_unique.append(cm)

        ac_columns = CommentedMap()
        ac_columns["type"] = "array"
        ac_columns["items"] = ac_items
        ac_columns["allOf"] = ac_unique

        ac_template_props = CommentedMap()
        ac_template_props["ada:analyteColumns"] = ac_columns

        ac_template = CommentedMap()
        ac_template["type"] = "object"
        ac_template["properties"] = ac_template_props

        props["ada:analyteTemplate"] = ac_template

    if parameter_names:
        mp_anyof = CommentedSeq()
        for param_name in sorted(parameter_names):
            mp_anyof.append({"$ref": f"../parameterTemplates/schema.yaml#/$defs/{param_name}"})

        mp_items = CommentedMap()
        mp_items["anyOf"] = mp_anyof

        mp_unique = CommentedSeq()
        for param_name in sorted(parameter_names):
            cm = CommentedMap()
            cm["contains"] = {"$ref": f"../parameterTemplates/schema.yaml#/$defs/{param_name}"}
            cm["minContains"] = 0
            cm["maxContains"] = 1
            mp_unique.append(cm)

        mp_array = CommentedMap()
        mp_array["type"] = "array"
        mp_array["items"] = mp_items
        mp_array["allOf"] = mp_unique

        props["schema:additionalProperty"] = mp_array

    if instrument_haspart:
        props["schema:instrument"] = _to_commented(instrument_haspart)

    overlay["properties"] = props
    if required_props:
        rq = CommentedSeq()
        for k in sorted(required_props):
            rq.append(k)
        overlay["required"] = rq
    allof.append(overlay)
    doc["allOf"] = allof

    out = BB / "schema.yaml"
    BB.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        yaml.dump(doc, f)
    print(f"  wrote {out.relative_to(REPO_ROOT)} ({len(properties)} properties, "
          f"{len(analyte_column_names)} analyte columns, "
          f"{len(parameter_names)} parameters)")


# ---------- example builder ----------

def looks_like_number(s: str) -> bool:
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


def _coerce_value(val, dtype_col: str | None):
    """Coerce a spreadsheet cell value to the JSON type implied by Data Type."""
    if val is None:
        return None
    s = str(val).strip()
    if not s:
        return None
    val_type, _ = _value_type_for(dtype_col)
    try:
        if val_type == "integer":
            return int(s)
        if val_type == "number":
            try:
                return int(s)
            except ValueError:
                return float(s)
        if val_type == "boolean":
            return s.lower() in ("true", "yes", "1")
    except ValueError:
        pass
    return s


def example_for_pub(pub_index: int, pub_label: str, rows: list[dict]) -> tuple[dict, dict]:
    """Build a paired (empaTAPP, detailEMPA) example from one publication column.

    empaTAPP carries the protocol definition (top-level ada:* properties from
    `property:` tags + readOnly:true schema:additionalProperty templates).
    detailEMPA carries the per-dataset values (schema:additionalProperty entries
    for readOnly:false parameters with a value in this publication's column),
    pointing back at the empaTAPP via schema:measurementTechnique by @id.
    """
    pub_code = _pubs()[pub_index][0].lower()
    empa_id = f"ex:{TAPP_NAME}-{pub_code}"
    detail_id = f"ex:{DETAIL_NAME}-{pub_code}"

    parts = OrderedDict()
    parts["@context"] = {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "bios": "https://bioschemas.org/",
    }
    parts["@id"] = empa_id
    parts["@type"] = [
        "cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol",
    ]
    parts["schema:name"] = ""
    parts["schema:description"] = CFG["example_description_template"].format(pub_label=pub_label)
    parts["schema:measurementTechnique"] = {
        "@type": ["schema:DefinedTerm"],
        "schema:termCode": CFG["termcode"],
        "schema:name": CFG["termname"],
    }

    detail = OrderedDict()
    detail["@context"] = dict(_ADA_CONTEXT)
    detail["@id"] = detail_id
    detail["@type"] = ["schema:Thing"]
    detail["ada:componentType"] = CFG["detail_componenttype_default"]
    detail["schema:measurementTechnique"] = {"@id": empa_id}
    detail["schema:additionalProperty"] = []

    method_params = []

    for row in rows:
        val = row["pubs"][pub_index] if pub_index < len(row["pubs"]) else None
        if val is None or (isinstance(val, str) and not val.strip()):
            continue
        item = row["item"]
        if not item:
            continue
        if item == "Method Name":
            parts["schema:name"] = str(val).strip()
            continue
        if item == "Method Author":
            parts["schema:creator"] = {
                "@type": ["schema:Person"],
                "schema:name": str(val).strip(),
            }
            continue
        if item == "Laboratory":
            parts["schema:location"] = {
                "@type": ["schema:Place"],
                "schema:name": str(val).strip(),
            }
            continue
        if item == "Instrument Manufacturer" or item == "Instrument Model":
            inst = parts.setdefault("schema:instrument", {
                "@type": ["schema:Thing", "schema:Product", "https://w3id.org/nfdi4ing/metadata4ing#Instrument"],
                "schema:additionalType": list(CFG["instrument_addl_type"]),
                "schema:name": CFG["instrument_name_default"],
            })
            if item == "Instrument Manufacturer":
                inst["schema:manufacturer"] = {"@type": ["schema:Organization"], "schema:name": str(val).strip()}
            else:
                inst["schema:model"] = {"@type": ["schema:ProductModel"], "schema:name": str(val).strip()}
                inst["schema:name"] = inst.get("schema:manufacturer", {}).get("schema:name", CFG["instrument_name_short"]) + " " + str(val).strip()
            continue
        if item == "Electron Source":
            inst = parts.setdefault("schema:instrument", {"@type": ["schema:Thing"]})
            inst.setdefault("schema:hasPart", []).append({
                "@type": ["schema:Thing", "schema:Product"],
                "schema:additionalType": ["ElectronSource"],
                "schema:name": str(val).strip(),
            })
            continue
        if item == "WDS Spectrometer Configuration":
            if not CFG.get("has_wds_config", False):
                # Non-EMPA TAPPs have no WDS spectrometers; skip silently.
                continue
            inst = parts.setdefault("schema:instrument", {"@type": ["schema:Thing"]})
            inst.setdefault("schema:hasPart", []).extend(_parse_wds_table(val))
            continue
        if item == "EDS Detector Configuration":
            # Per current spec, blank EDS cells stay out of the JSON.
            # Non-blank values get one hasPart entry of additionalType "edsDetector".
            inst = parts.setdefault("schema:instrument", {"@type": ["schema:Thing"]})
            inst.setdefault("schema:hasPart", []).append({
                "@type": ["schema:Thing"],
                "schema:additionalType": ["edsDetector"],
                "schema:name": str(val).strip().split("\n")[0],
                "schema:description": str(val).strip(),
            })
            continue
        if item == "Target Material":
            for m in [t.strip() for t in str(val).split("|") if t.strip()]:
                parts.setdefault("schema:object", []).append({
                    "@type": ["schema:DefinedTerm"], "schema:name": m,
                })
            continue
        if item == "Method Start Date":
            parts["schema:datePublished"] = str(val).strip().split(" ")[0]
            continue
        if item == "Funding Source":
            for f in [t.strip() for t in str(val).split("|") if t.strip()]:
                parts.setdefault("schema:funding", []).append({
                    "@type": ["schema:MonetaryGrant"], "schema:name": f,
                })
            continue
        if item == "Method Reference(s)":
            for url in [t.strip() for t in str(val).split("|") if t.strip()]:
                parts.setdefault("schema:relatedLink", []).append({
                    "@type": ["schema:CreativeWork"],
                    "schema:url": url,
                    "schema:name": "Method reference",
                })
            continue
        if item == "Analytical Software":
            for tool in [t.strip() for t in str(val).split("|") if t.strip()]:
                parts.setdefault("bios:computationalTool", []).append({
                    "@type": ["schema:SoftwareApplication"],
                    "schema:name": tool,
                    "ada:toolRole": "acquisition",
                })
            continue
        if item == "Data Reduction Software":
            for tool in [t.strip() for t in str(val).split("|") if t.strip()]:
                parts.setdefault("bios:computationalTool", []).append({
                    "@type": ["schema:SoftwareApplication"],
                    "schema:name": tool,
                    "ada:toolRole": "reduction",
                })
            continue

        # Use per-tag records so a row's property: and parameter: tags get the right readOnly each.
        for tr in row["parsed"]["tag_records"]:
            kind = tr["kind"]
            name = tr["name"]
            ro = tr["readOnly"]
            tag_dtype = tr["dtype"] or row["parsed"]["dtype"]
            tag_enum = tr["enum"] or row["parsed"]["enum"]

            if kind == "property":
                if name in ("analyteTemplate", "description"):
                    continue
                key = f"ada:{name}"
                v = str(val).strip()
                if tag_enum and v not in tag_enum:
                    continue
                parts[key] = v
            elif kind == "parameter":
                if ro:
                    method_params.append(OrderedDict([
                        ("@id", f"ada:parameter/{TAPP_NAME}/{name}"),
                        ("@type", ["schema:PropertyValueSpecification"]),
                        ("schema:name", item),
                        ("schema:valueName", name),
                        ("schema:description", row["desc"] or item),
                        ("ada:dataType", map_dtype(tag_dtype)),
                        ("ada:fieldScope", "session"),
                        ("schema:readonlyValue", True),
                        ("ada:tier", "R"),
                        ("schema:defaultValue", str(val).strip()),
                    ]))
                else:
                    coerced = _coerce_value(val, row.get("dtype_col"))
                    if coerced is None:
                        continue
                    val_type, unit = _value_type_for(row.get("dtype_col"))
                    entry = OrderedDict([
                        ("@id", f"ada:parameter/{TAPP_NAME}/{name}"),
                        ("@type", ["schema:PropertyValue"]),
                        ("schema:propertyID", f"ada:parameter/{TAPP_NAME}/{name}"),
                        ("schema:name", item),
                        ("schema:value", coerced),
                    ])
                    if unit:
                        entry["schema:unitText"] = unit
                    detail["schema:additionalProperty"].append(entry)

    if method_params:
        parts["schema:additionalProperty"] = method_params
    if not parts["schema:name"]:
        parts["schema:name"] = CFG["example_name_template"].format(code=_pubs()[pub_index][0])

    # ---- Build ada:analyteTemplate.ada:defaultAnalytes from per-analyte data ----
    # The "Target Element" row's column value defines the analyte axis (pipe-delim
    # list, e.g. "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn"). Each analyteColumn row's column
    # value is parsed by parse_per_analyte() — single value applies to all
    # analytes; pipe-delim list maps positionally; missing or empty entries
    # leave the field absent on that row.
    analyte_names: list[str] = []
    for row in rows:
        if row.get("item") == "Target Element":
            v = row["pubs"][pub_index] if pub_index < len(row["pubs"]) else None
            if v is not None and isinstance(v, str) and v.strip():
                sep = "|" if "|" in v else ","
                analyte_names = [a.strip() for a in v.split(sep) if a.strip()]
            break

    if analyte_names:
        n = len(analyte_names)
        default_rows = [OrderedDict([("analyte", a)]) for a in analyte_names]
        for row in rows:
            for tr in row["parsed"]["tag_records"]:
                if tr["kind"] != "analytecolumn":
                    continue
                col_name = tr["name"]
                cell = row["pubs"][pub_index] if pub_index < len(row["pubs"]) else None
                per_a = parse_per_analyte(cell, n)
                for i, v in enumerate(per_a):
                    if v is None:
                        continue
                    v2 = v
                    if isinstance(v, str):
                        try:
                            v2 = int(v)
                        except ValueError:
                            try:
                                v2 = float(v)
                            except ValueError:
                                pass
                    default_rows[i][col_name] = v2

        # Build the analyteColumns array: identifier-column first, then catalog
        # canonicals for ONLY the analyteColumns that have at least one value
        # populated across the defaultAnalytes rows. Columns with no values in
        # this example are omitted to keep the analyteTemplate focused on the
        # protocol's actual reporting axis for this dataset.
        used_col_names: set[str] = set()
        for r in default_rows:
            used_col_names.update(k for k in r.keys() if k != "analyte")

        analyte_cols = [OrderedDict([
            ("@type", ["schema:PropertyValueSpecification"]),
            ("schema:name", "Analyzed constituent"),
            ("schema:valueName", "analyte"),
            ("schema:description", "Analyzed constituent identified by the analyte row."),
            ("ada:dataType", "string"),
            ("schema:readonlyValue", True),
            ("schema:valueRequired", True),
            ("ada:tier", "M"),
            ("ada:cdifPropertyPath", "#/schema:variableMeasured/schema:name"),
        ])]
        seen: set[str] = set()
        for row in rows:
            for tr in row["parsed"]["tag_records"]:
                name = tr["name"]
                if tr["kind"] != "analytecolumn" or name in seen:
                    continue
                seen.add(name)
                if name not in used_col_names:
                    continue  # skip columns with no value in any defaultAnalytes row
                # Pull the canonical instance from the in-memory analyteColumn
                # cache (populated by _classify_rows). The registry schema.yaml
                # $defs strip examples, so the cache is the source of truth for
                # example construction.
                cd = ANALYTE_COLUMN_OBJS.get(name)
                if cd:
                    ex = (cd.get("examples") or [{}])[0]
                    ex_clean = OrderedDict((k, v) for k, v in ex.items() if k != "@context")
                    analyte_cols.append(ex_clean)

        parts["ada:analyteTemplate"] = OrderedDict([
            ("ada:analyteColumns", analyte_cols),
            ("ada:defaultAnalytes", default_rows),
        ])

    return parts, detail


# ---------- profile-level (adaEMPA) example builder ----------

def variable_measured_from_default_analytes(pub_label: str, default_analytes: list,
                                             unit_text: str = "wt%") -> list:
    """Map a TAPP's ada:defaultAnalytes -> profile-level schema:variableMeasured.

    Each defaultAnalytes entry becomes one schema:PropertyValue+cdi:InstanceVariable.
    Per-analyte protocol detail (x-ray emission line, counting times, calibration
    standard) folds into schema:description so the variable's measurement context
    is preserved without forcing a consumer to read both the profile record and
    the TAPP definition.

    Defaults to 'wt%' for schema:unitText (EMPA QEA convention). Other techniques
    pass their own unit (e.g. 'ppm' for trace LA-ICP-MS).
    """
    out = []
    for da in default_analytes:
        analyte = da.get("analyte", "?")
        bits = []
        if da.get("xrayEmissionLine"):
            bits.append(f"{da['xrayEmissionLine']} emission line")
        if da.get("peakCountingTime") is not None:
            bits.append(f"{da['peakCountingTime']} s peak counting")
        if da.get("backgroundCountingTime") is not None:
            bits.append(f"{da['backgroundCountingTime']} s background counting")
        if da.get("primaryCalibrationStandard"):
            bits.append(f"calibrated against {da['primaryCalibrationStandard']}")
        detail = "; ".join(bits)
        desc = f"{analyte} abundance measured by EMPA WDS"
        if detail:
            desc += f" ({detail})"
        desc += "."
        out.append(OrderedDict([
            ("@id", f"ex:adaEMPA-{pub_label}-var-{analyte}"),
            ("@type", ["schema:PropertyValue", "cdi:InstanceVariable"]),
            ("schema:name", analyte),
            ("schema:description", desc),
            ("schema:propertyID", [f"https://ada.astromat.org/vocabulary/analytes/{analyte}"]),
            ("schema:unitText", unit_text),
            ("cdi:intendedDataType", "https://www.w3.org/TR/xmlschema-2/#decimal"),
            ("cdif:physicalDataType", "https://www.w3.org/TR/xmlschema-2/#double"),
            ("cdi:role", "MeasureComponent"),
            ("cdi:simpleUnitOfMeasure", unit_text),
        ]))
    return out


def _instrument_for_provused(tapp_instrument: dict | None) -> dict:
    """Adapt a TAPP-level schema:instrument record into a prov:used entry. Adds
    schema:Thing + schema:Product to @type and ensures the additionalType
    contains the instrument-class markers expected by the profile schema."""
    # NOTE: this is only invoked from the empaTAPP profile-example builder
    # (build_adaEMPA_example / emit_adaEMPA_examples), which is gated by
    # CFG["emit_profile_examples"] = True for empaTAPP only. The literal
    # "EMPA Instrument" preserves the legacy adaEMPA profile-example output.
    base = OrderedDict([
        ("@type", ["schema:Thing", "schema:Product"]),
        ("schema:additionalType", [
            "nxs:BaseClass/NXinstrument", "ada:EMPAInstrument",
        ]),
        ("schema:name", "EMPA Instrument"),
        ("schema:identifier", ["ex:instrument-empa-001"]),
    ])
    if isinstance(tapp_instrument, dict):
        if tapp_instrument.get("schema:name"):
            base["schema:name"] = tapp_instrument["schema:name"]
        manuf = tapp_instrument.get("schema:manufacturer")
        if isinstance(manuf, dict) and manuf.get("schema:name"):
            base["schema:manufacturer"] = manuf
    return base


def _location_for_provused(tapp_location: dict | None) -> dict:
    """Adapt schema:Place from the TAPP into a profile-level prov:wasGeneratedBy
    schema:location entry. Profile schema requires NXsource in additionalType."""
    name = "Analytical Sciences Laboratory"
    if isinstance(tapp_location, dict) and tapp_location.get("schema:name"):
        name = tapp_location["schema:name"]
    return OrderedDict([
        ("@type", ["schema:Place"]),
        ("schema:name", name),
        ("schema:additionalType", ["nxs:BaseClass/NXsource"]),
    ])


def _sample_for_provused(tapp_object_first: dict | None, pub_label: str) -> dict:
    """Build a single MaterialSample for prov:wasGeneratedBy.schema:object.
    The TAPP's schema:object describes the sample type (DefinedTerm); the
    profile-level needs a concrete instance with an @id, igsn, etc."""
    desc = "Material sample analyzed in this protocol session."
    if isinstance(tapp_object_first, dict) and tapp_object_first.get("schema:name"):
        desc = f"Sample of: {tapp_object_first['schema:name']}"
    return OrderedDict([
        ("@type", [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        ]),
        ("schema:additionalType", ["MaterialSample"]),
        ("schema:name", f"Sample analyzed in {pub_label}"),
        ("schema:identifier", [f"igsn:10.60471/PLACEHOLDER-{pub_label}"]),
        ("schema:description", desc),
    ])


_REQUIRED_CONFORMS_TO = [
    "https://w3id.org/cdif/core/1.0",
    "https://w3id.org/cdif/discovery/1.0",
    "https://w3id.org/cdif/data_description/1.0",
    "https://w3id.org/cdif/provenance/1.0",
    "https://w3id.org/cdif/manifest/1.0",
    "https://w3id.org/geochem/metadata/profiles/adaEMPA",
    "https://w3id.org/geochem/metadata/profiles/adaProduct",
]


def profile_example_for_pub(pub_label: str, pub_citation: str,
                            tapp_ex: dict, detail_ex: dict) -> dict:
    """Build an adaEMPA profile-level schema:Dataset example for one publication.

    Composes:
      - schema:variableMeasured: derived from tapp.ada:analyteTemplate.ada:defaultAnalytes
      - prov:wasGeneratedBy[].prov:used: from tapp.schema:instrument
      - prov:wasGeneratedBy[].schema:location: from tapp.schema:location
      - prov:wasGeneratedBy[].schema:object: synthesized MaterialSample referencing tapp.schema:object
      - schema:distribution[].schema:hasPart[]: an EMPAQEATabular file carrying
        the detailEMPA fields (componentType, spectrometersUsed, signalUsed,
        schema:additionalProperty, schema:measurementTechnique → tapp_ex.@id)
      - schema:subjectOf: catalog-record metadata with the required dcterms:conformsTo URIs

    Synthetic placeholders (not derivable from TAPP+detail data alone): DOI,
    schema:url, file size, checksum, dates. These are clearly marked as
    placeholders so authors can override them per-pub.
    """
    da_list = tapp_ex.get("ada:analyteTemplate", {}).get("ada:defaultAnalytes", [])
    variable_measured = variable_measured_from_default_analytes(pub_label, da_list)

    tapp_id = tapp_ex.get("@id", f"ex:{TAPP_NAME}-{pub_label.lower()}")

    detail_componenttype = detail_ex.get("ada:componentType", "ada:EMPAQEATabular")
    detail_spectrometers = detail_ex.get("ada:spectrometersUsed", "5x WDS")
    detail_signal = detail_ex.get("ada:signalUsed", "Kα x-ray lines")
    detail_addprops = detail_ex.get("schema:additionalProperty", [])

    haspart = OrderedDict([
        ("@id", f"ex:adaEMPA-{pub_label}-data-001"),
        ("@type", ["ada:tabularData", "cdi:TabularTextDataSet", "schema:Thing"]),
        ("schema:name", f"adaEMPA-{pub_label}-data.csv"),
        ("schema:description", f"Per-point quantitative EMPA analyses ({pub_citation})."),
        ("schema:additionalType", ["ada:EMPAQEATabular"]),
        ("schema:encodingFormat", ["text/csv"]),
        ("cdi:isDelimited", True),
        ("cdi:isFixedWidth", False),
        ("csvw:delimiter", ","),
        ("csvw:header", True),
        ("ada:componentType", detail_componenttype),
        ("ada:spectrometersUsed", detail_spectrometers),
        ("ada:signalUsed", detail_signal),
        ("schema:measurementTechnique", {"@id": tapp_id}),
        ("schema:additionalProperty", detail_addprops),
    ])

    # Build top-level Dataset
    out = OrderedDict()
    out["@context"] = OrderedDict([
        ("schema", "http://schema.org/"),
        ("ada", "https://ada.astromat.org/metadata/"),
        ("cdi", "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"),
        ("csvw", "http://www.w3.org/ns/csvw#"),
        ("prov", "http://www.w3.org/ns/prov#"),
        ("spdx", "http://spdx.org/rdf/terms#"),
        ("nxs", "http://purl.org/nexusformat/definitions/"),
        ("dcterms", "http://purl.org/dc/terms/"),
        ("ex", "https://example.org/"),
        ("dcat", "http://www.w3.org/ns/dcat#"),
    ])
    out["@id"] = f"ex:adaEMPA-{pub_label}"
    out["@type"] = ["schema:Dataset", "schema:Product"]
    out["schema:name"] = f"adaEMPA dataset for {pub_label} ({pub_citation})"
    out["schema:description"] = (
        f"Auto-generated adaEMPA profile-level Dataset for publication {pub_label}: "
        f"{pub_citation}. The schema:hasPart entry under schema:distribution "
        f"carries detailEMPA fields and points at the empaTAPP TAPP definition "
        f"({tapp_id}); schema:variableMeasured is derived from the TAPP's "
        f"ada:defaultAnalytes."
    )
    out["schema:additionalType"] = [
        "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage",
    ]
    out["schema:identifier"] = OrderedDict([
        ("@type", ["schema:PropertyValue"]),
        ("schema:propertyID", "https://registry.identifiers.org/registry/doi"),
        ("schema:value", f"10.PLACEHOLDER/adaempa-{pub_label.lower()}"),
    ])
    out["schema:url"] = f"https://astromat.org/products/adaempa-{pub_label.lower()}"
    out["schema:dateModified"] = "2026-04-29"
    out["schema:version"] = "0.1"
    out["schema:license"] = ["https://creativecommons.org/licenses/by/4.0/"]
    out["schema:creativeWorkStatus"] = "Draft"
    out["schema:measurementTechnique"] = OrderedDict([
        ("@type", ["schema:DefinedTerm"]),
        ("schema:name", "Electron Microprobe Analysis (EMPA)"),
        ("schema:identifier", "https://ada.astromat.org/vocabulary/techniques/EMPA"),
    ])
    tapp_object_first = (tapp_ex.get("schema:object") or [None])[0]
    out["prov:wasGeneratedBy"] = [OrderedDict([
        ("@type", ["prov:Activity", "schema:Action"]),
        ("schema:identifier", f"session-empa-{pub_label.lower()}"),
        ("schema:startDate", "2026-04-29"),
        ("prov:used", [_instrument_for_provused(tapp_ex.get("schema:instrument"))]),
        ("schema:location", _location_for_provused(tapp_ex.get("schema:location"))),
        ("schema:object", [_sample_for_provused(tapp_object_first, pub_label)]),
    ])]
    out["schema:variableMeasured"] = variable_measured
    out["schema:distribution"] = [OrderedDict([
        ("@type", ["schema:DataDownload"]),
        ("schema:name", f"adaEMPA-{pub_label}-archive.zip"),
        ("schema:description", f"Archive containing tabular EMPA data for {pub_label}."),
        ("schema:contentUrl", f"https://astromat.org/downloads/adaempa-{pub_label.lower()}.zip"),
        ("schema:encodingFormat", ["application/zip"]),
        ("spdx:checksum", OrderedDict([
            ("@type", ["spdx:Checksum"]),
            ("spdx:algorithm", "SHA256"),
            ("spdx:checksumValue", "0" * 64),
        ])),
        ("schema:size", OrderedDict([
            ("@type", ["schema:QuantitativeValue"]),
            ("schema:value", 1048576),
            ("schema:unitText", "byte"),
        ])),
        ("schema:hasPart", [haspart]),
    ])]
    out["schema:subjectOf"] = OrderedDict([
        ("@type", ["schema:Dataset"]),
        ("schema:additionalType", ["dcat:CatalogRecord"]),
        ("@id", f"ex:adaEMPA-{pub_label}-metadata"),
        ("schema:about", {"@id": f"ex:adaEMPA-{pub_label}"}),
        ("schema:dateModified", "2026-04-29"),
        ("dcterms:conformsTo", [{"@id": uri} for uri in _REQUIRED_CONFORMS_TO]),
        ("schema:maintainer", OrderedDict([
            ("@type", ["schema:Organization"]),
            ("schema:name", "Astromat Data Archive"),
        ])),
        ("schema:sdDatePublished", "2026-04-29T12:00:00Z"),
    ])
    return out


def build_profile_examples(pub_filter: list[str] | None = None) -> dict:
    """For each pub with a paired (empaTAPP, detailEMPA) example pair on disk,
    emit _sources/profiles/adaProfiles/adaEMPA/exampleadaEMPA-<pub>.json. Returns
    a counts dict {written: int, skipped: int}.

    EMPA-only — emits nothing when CFG["emit_profile_examples"] is False
    (e.g. for laicpmsTAPP)."""
    if not CFG.get("emit_profile_examples", False):
        return {"written": 0, "skipped": 0}
    profile_dir = REPO_ROOT / "_sources" / "profiles" / "adaProfiles" / "adaEMPA"
    profile_dir.mkdir(parents=True, exist_ok=True)
    tapp_dir = REPO_ROOT / "_sources" / "techniqueProtocols" / TAPP_NAME
    detail_dir = REPO_ROOT / "_sources" / "geochemProperties" / DETAIL_NAME

    written, skipped = 0, 0
    for pub_code, pub_citation in _pubs():
        if pub_filter and pub_code not in pub_filter:
            continue
        tapp_path = tapp_dir / f"example{TAPP_NAME}-{pub_code}.json"
        detail_path = detail_dir / f"example{DETAIL_NAME}-{pub_code}.json"
        if not tapp_path.exists() or not detail_path.exists():
            skipped += 1
            continue
        tapp_ex = json.loads(tapp_path.read_text(encoding="utf-8"))
        detail_ex = json.loads(detail_path.read_text(encoding="utf-8"))
        profile_ex = profile_example_for_pub(pub_code, pub_citation, tapp_ex, detail_ex)
        out_path = profile_dir / f"exampleadaEMPA-{pub_code}.json"
        out_path.write_text(json.dumps(profile_ex, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
        written += 1
    return {"written": written, "skipped": skipped}


def _parse_wds_table(text) -> list:
    """Parse the WDS Spectrometer Configuration cell into a list of hasPart
    entries. The cell is a multi-line pipe-delimited table whose header row
    names the target field per column. Each subsequent line is one
    wdsSpectrometer instance.

    Header tokens supported:
      - bare names: 'name', 'description', 'additionalType' map to
        schema:<token> directly
      - 'additionalProperty/name=<X>' maps the column's value into a
        schema:additionalProperty entry as a PropertyValue with
        schema:name=<X> and schema:value=<cell>.
      - any other token is dropped into the entry under that token name
    """
    if text is None:
        return []
    lines = [ln for ln in str(text).split("\n") if ln.strip()]
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split("|")]

    entries = []
    for line in lines[1:]:
        cells = [c.strip() for c in line.split("|")]
        entry = OrderedDict([
            ("@type", ["schema:Thing"]),
            ("schema:additionalType", ["wdsSpectrometer"]),
        ])
        for h, v in zip(headers, cells):
            if not v:
                continue
            if h in ("name", "description"):
                entry[f"schema:{h}"] = v
            elif h == "additionalType":
                entry["schema:additionalType"] = list(set(entry["schema:additionalType"] + [v]))
            elif h.startswith("additionalProperty/name="):
                ap_name = h[len("additionalProperty/name="):]
                entry.setdefault("schema:additionalProperty", []).append(OrderedDict([
                    ("@type", ["schema:PropertyValue"]),
                    ("schema:name", ap_name),
                    ("schema:value", v),
                ]))
            else:
                entry[h] = v
        entries.append(entry)
    return entries


def parse_per_analyte(cell_value, n: int) -> list:
    """Parse a per-analyte cell value into a list of N positional values.

    - empty cell → all None (caller skips fields with None)
    - single value (no pipe) → repeated N times (applies to every analyte)
    - pipe-delimited list → one value per position; missing positions and
      empty entries within the list → None on those rows
    """
    if cell_value is None:
        return [None] * n
    s = str(cell_value).strip()
    if not s:
        return [None] * n
    if "|" not in s:
        return [s] * n
    parts = [p.strip() for p in s.split("|")]
    return [(parts[i] if i < len(parts) and parts[i] else None) for i in range(n)]


# ---------- main ----------

def _classify_rows(rows, *, emit_tapp: bool, emit_detail: bool):
    """Walk parsed rows, emit catalog files to the appropriate shared dirs, and
    return (schema_properties, analyte_column_names, parameter_names,
    detail_param_names, counts). Toggle emit_tapp / emit_detail to skip writing
    the side that's not needed by the caller (TAPP-builder vs. detail-builder)
    while still tracking names for downstream constraint generation."""
    schema_properties: list[tuple[str, dict]] = []
    analyte_column_names: list[str] = []
    parameter_names: list[str] = []
    detail_param_names: list[str] = []
    # readOnly:false parameter-value schemas collected for the parameterValues
    # registry schema.yaml $defs (keyed by name). Only populated when emit_detail.
    param_value_defs: "OrderedDict[str, dict]" = OrderedDict()
    # readOnly:true method-parameter templates and analyteColumn specs collected
    # for their registry schema.yaml $defs (keyed by name). Only populated when
    # emit_tapp. These replace the former flat per-name catalog files.
    parameter_template_defs: "OrderedDict[str, dict]" = OrderedDict()
    analyte_column_defs: "OrderedDict[str, dict]" = OrderedDict()
    if emit_tapp:
        ANALYTE_COLUMN_OBJS.clear()
    enum_to_vocab_name: dict[tuple[str, ...], str] = {}
    counts = {"vocab": 0, "parameter": 0, "detailParameter": 0, "analyteColumn": 0, "property": 0}

    # Deduplicate vocab by (sorted enum tuple)
    for row in rows:
        p = row["parsed"]
        if not p["enum"]:
            continue
        # Choose vocab name from the first tag of any kind, or the first valueName-ish token
        name = None
        for kind, n in p["tags"]:
            name = n
            break
        if not name and row["item"]:
            name = re.sub(r"[^A-Za-z0-9]+", "_", row["item"]).strip("_")
        if not name:
            continue
        key = tuple(sorted(p["enum"]))
        if key in enum_to_vocab_name:
            continue
        enum_to_vocab_name[key] = name
        # Write vocab file (or share with an existing one matching this content).
        # Vocabs are referenced from both TAPP and detail catalogs, so emit them
        # whenever either side is being built.
        path = VOCAB_DIR / f"{name}.json"
        if emit_tapp or emit_detail:
            share_or_write_catalog(path, vocab_obj(name, row["item"] or name, row["desc"], p["enum"]))
        counts["vocab"] += 1

    def vocab_for(p):
        if not p["enum"]:
            return None
        return enum_to_vocab_name.get(tuple(sorted(p["enum"])))

    # Emit parameter and analyteColumn JSON, and collect properties for schema.yaml.
    # Use per-tag records so a row carrying both `property: X readOnly:true` and
    # `parameter: Y readOnly:false` gets the right value applied to each tag.
    for row in rows:
        p = row["parsed"]
        for tr in p["tag_records"]:
            kind = tr["kind"]
            name = tr["name"]
            ro = tr["readOnly"]
            tag_dtype = tr["dtype"] or p["dtype"]
            tag_enum = tr["enum"] or p["enum"]
            vocab_name = enum_to_vocab_name.get(tuple(sorted(tag_enum))) if tag_enum else None

            if kind == "parameter":
                if ro:
                    # readOnly:true → method-level template (PropertyValueSpecification);
                    # only emitted when building the TAPP side. Collected into the
                    # parameterTemplates registry schema.yaml $defs (one $def per name)
                    # instead of a flat per-name file.
                    if emit_tapp:
                        parameter_template_defs[name] = parameter_obj(
                            name, row["item"], row["desc"], tag_dtype, vocab_name, ro)
                    parameter_names.append(name)
                    counts["parameter"] += 1
                else:
                    # readOnly:false → per-dataset value (PropertyValue).
                    # No longer written as a flat per-name file; instead collected
                    # into the parameterValues registry schema.yaml $defs (one $def
                    # per name) by build_detail_artifacts → write_parameter_values_registry.
                    if emit_detail:
                        param_value_defs[name] = additional_property_obj(
                            name, row["item"], row["desc"],
                            row.get("dtype_col"), vocab_name, tag_dtype,
                        )
                    detail_param_names.append(name)
                    counts["detailParameter"] += 1
            elif kind == "analytecolumn":
                # analyteColumns are TAPP-side artifacts. Collected into the
                # analyteColumns registry schema.yaml $defs (one $def per name)
                # instead of a flat per-name file.
                if emit_tapp:
                    analyte_column_defs[name] = analyte_column_obj(
                        name, row["item"], row["desc"], tag_dtype, vocab_name, ro)
                    # Cache the full object (incl. examples) for example_for_pub.
                    ANALYTE_COLUMN_OBJS[name] = analyte_column_defs[name]
                counts["analyteColumn"] += 1
                analyte_column_names.append(name)
            elif kind == "property":
                # Skip non-property markers: "analyteTemplate" references the existing
                # ada:analyteTemplate structure inherited from tappDefinition (not a
                # new top-level property); "description" maps to the existing
                # schema:description (the schema_path confirms this for the relevant row).
                if name in ("analyteTemplate", "description"):
                    continue
                # Build schema.yaml property block
                block = OrderedDict()
                if row["desc"]:
                    block["description"] = row["desc"]
                if tag_enum:
                    block["type"] = "string"
                    block["enum"] = list(tag_enum)
                else:
                    block["type"] = map_dtype(tag_dtype) if map_dtype(tag_dtype) != "string" else "string"
                schema_properties.append((f"ada:{name}", block))
                counts["property"] += 1

    # Dedupe properties by ada:<name>, last one wins (for repeated tags)
    seen = OrderedDict()
    for prop_name, block in schema_properties:
        seen[prop_name] = block
    schema_properties = list(seen.items())

    return {
        "schema_properties": schema_properties,
        "analyte_column_names": analyte_column_names,
        "parameter_names": parameter_names,
        "detail_param_names": detail_param_names,
        "param_value_defs": param_value_defs,
        "parameter_template_defs": parameter_template_defs,
        "analyte_column_defs": analyte_column_defs,
        "counts": counts,
    }


def _write_examples_yaml(examples_yaml: list[tuple[str, str]]) -> None:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    ex_doc = CommentedSeq()
    for pcode, plabel in examples_yaml:
        e = CommentedMap()
        e["title"] = f"{TAPP_NAME} example {pcode}: {plabel}"
        e["content"] = (
            f"{TAPP_NAME} instance derived from publication {plabel}. Property and parameter values "
            f"taken from the corresponding column of the {XLSX.name} 'TAPP' worksheet."
        )
        e["prefixes"] = {
            "ada": "https://ada.astromat.org/metadata/",
            "schema": "http://schema.org/",
            "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
            "bios": "https://bioschemas.org/",
        }
        snip = CommentedMap()
        snip["language"] = "json"
        snip["ref"] = f"example{TAPP_NAME}-{pcode}.json"
        e["snippets"] = [snip]
        ex_doc.append(e)
    with open(BB / "examples.yaml", "w", encoding="utf-8") as f:
        yaml.dump(ex_doc, f)
    print(f"  wrote examples.yaml with {len(examples_yaml)} entries")


def _pub_meaningful(v) -> bool:
    """True if a publication cell carries real content, not 'N'/'N/A'/'N (explanation)'."""
    if v is None:
        return False
    v = re.sub(r"\s*\[P[^\]]*\]", "", str(v).strip()).strip()
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


def build_tapp_artifacts(pub_filter: list[str] | None = None) -> dict:
    """Generate the TAPP-side artifacts only:
    - shared catalog files in techniqueProtocols/{analyteColumns,parameterTemplates,vocab}/
    - TAPP BB schema.yaml at techniqueProtocols/<TAPP_NAME>/
    - per-publication TAPP examples + examples.yaml
    pub_filter, if given, restricts which publication codes (e.g. ['P0']) get
    their example regenerated; the others are left untouched. Schema/catalog
    artifacts are always rebuilt regardless of pub_filter.
    Per-tag readOnly:false rows are tracked but their PropertyValue catalog is NOT
    written (the detail-builder writes those). Returns the classification dict."""
    CATALOG_CONFLICTS.clear()
    rows = read_rows()
    print(f"Read {len(rows)} non-empty rows from TAPP worksheet.")

    cls = _classify_rows(rows, emit_tapp=True, emit_detail=False)

    # Canonical dual-home model: Basic (property:) fields are required EXCEPT those no
    # publication reports (coverage 0) -> optional. Coverage from the publication columns.
    prop_type = {k: (b.get("type") if isinstance(b, dict) else None)
                 for k, b in cls["schema_properties"]}
    prop_cov = {}
    for row in rows:
        cov = sum(1 for v in (row.get("pubs") or []) if _pub_meaningful(v))
        for tr in row["parsed"]["tag_records"]:
            if tr["kind"] == "property" and tr["name"] not in ("analyteTemplate", "description"):
                key = "ada:" + tr["name"]
                prop_cov[key] = max(prop_cov.get(key, 0), cov)
    required_props = [k for k, _ in cls["schema_properties"] if prop_cov.get(k, 0) > 0]
    required_set = set(required_props)

    instrument_haspart = build_haspart_constraint(rows)
    build_schema_yaml(
        cls["schema_properties"], cls["analyte_column_names"],
        cls["parameter_names"], instrument_haspart, required_props=required_props,
    )

    # Write the registered analyteColumns + parameterTemplates collection BBs
    # ($defs libraries). Multi-TAPP runs accumulate the UNION of $defs; this
    # TAPP's owned entries are overwritten/inserted and stale owned entries
    # pruned, while other TAPPs' $defs are preserved.
    write_analyte_columns_registry(cls["analyte_column_defs"])
    write_parameter_templates_registry(cls["parameter_template_defs"])

    # Clean up any legacy flat per-name catalog files owned by THIS TAPP — they
    # are superseded by schema.yaml $defs. Foreign-owned flat files (other TAPPs
    # not yet migrated) are left untouched. The registry schema.yaml/bblock.json
    # and the generated *Schema.json/resolvedSchema.json are never deleted here.
    _cleanup_legacy_flat_catalog(ANALYTE_COLUMNS_DIR, "analyteColumns")
    _cleanup_legacy_flat_catalog(PARAMETER_TEMPLATES_DIR, "parameterTemplates")

    # Per-publication TAPP examples — pub_filter restricts which to regen
    examples_yaml = []
    written = 0
    for i, (pcode, plabel) in enumerate(_pubs()):
        if pub_filter and pcode not in pub_filter:
            examples_yaml.append((pcode, plabel))
            continue
        empa_ex, _ = example_for_pub(i, plabel, rows)
        # canonical model: required props get a real value or a sentinel; non-meaningful
        # values ("N") are cleaned (sentinel if required, dropped if optional).
        for key, _b in cls["schema_properties"]:
            present = key in empa_ex
            ok = present and _pub_meaningful(empa_ex[key])
            if key in required_set:
                if not ok:
                    empa_ex[key] = (-9999 if prop_type.get(key) in ("number", "integer")
                                    else "missing")
            elif present and not ok:
                del empa_ex[key]
        write_json(BB / f"example{TAPP_NAME}-{pcode}.json", empa_ex)
        examples_yaml.append((pcode, plabel))
        written += 1
    print(f"  wrote {written} per-publication {TAPP_NAME} examples"
          + (f" (filtered to {pub_filter})" if pub_filter else ""))

    _write_examples_yaml(examples_yaml)
    print(f"\nCounts: {cls['counts']}")
    if CATALOG_CONFLICTS:
        print(f"\n{len(CATALOG_CONFLICTS)} catalog conflict(s) skipped — see warnings above.")
    return cls


def build_detail_artifacts(pub_filter: list[str] | None = None) -> dict:
    """Generate the detail-side artifacts only.
    pub_filter, if given, restricts which publication codes get their example
    regenerated; the others are left untouched. Schema/catalog artifacts are
    always rebuilt regardless of pub_filter."""
    rows = read_rows()
    print(f"Read {len(rows)} non-empty rows from TAPP worksheet.")

    cls = _classify_rows(rows, emit_tapp=False, emit_detail=True)

    scaffold_detail_bb_if_missing()
    # Write the registered parameterValues collection BB ($defs library).
    write_parameter_values_registry(cls["param_value_defs"])
    # Clean up the legacy generated parametersConstraint.yaml (constraint is now
    # inline in the hand-authored detail schema.yaml).
    write_detail_empa_constraint(cls["detail_param_names"])

    # Clean up any legacy flat parameterValues/<name>.json files owned by THIS
    # TAPP — they are superseded by schema.yaml $defs. Foreign-owned flat files
    # (other TAPPs not yet migrated) are left untouched. The registry schema.yaml
    # and bblock.json are never deleted here.
    if PARAMETER_VALUES_DIR.exists():
        for fp in PARAMETER_VALUES_DIR.glob("*.json"):
            if fp.name == "bblock.json":
                continue
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    existing_id = (json.load(f) or {}).get("$id", "") or ""
            except (OSError, json.JSONDecodeError):
                continue
            if f"/{TAPP_NAME}/" in existing_id:
                fp.unlink()
                print(f"  deleted legacy flat {fp.relative_to(REPO_ROOT)} (now a $def)")

    # Per-publication detail examples — pub_filter restricts which to regen
    written = 0
    for i, (pcode, _plabel) in enumerate(_pubs()):
        if pub_filter and pcode not in pub_filter:
            continue
        _, detail_ex = example_for_pub(i, _plabel, rows)
        if detail_ex.get("schema:additionalProperty"):
            write_json(DETAIL_EMPA / f"example{DETAIL_NAME}-{pcode}.json", detail_ex)
            written += 1
    print(f"  wrote {written} per-publication {DETAIL_NAME} examples"
          + (f" (filtered to {pub_filter})" if pub_filter else ""))

    print(f"\nCounts: {cls['counts']}")
    return cls


def build_profile_BB() -> None:
    """Phase 5: scaffold _sources/profiles/geochemProfiles/<short>Profile/
    referencing the detail BB and the TAPP definition. Existing files are
    never overwritten — re-runs are no-ops once the user starts editing.

    The profile schema extends the base ada product profile with two
    technique-specific constraints:
      - schema:measurementTechnique anyOf [{@id ref}, inline TAPP]
      - schema:distribution[*].schema:hasPart[*] anyOf includes detailXXX
    """
    short = TAPP_NAME.replace("TAPP", "")  # e.g. "empa", "xrd"
    profile_dir = REPO_ROOT / "_sources" / "profiles" / "geochemProfiles" / f"{short}Profile"
    profile_dir.mkdir(parents=True, exist_ok=True)

    schema_path = profile_dir / "schema.yaml"
    if not schema_path.exists():
        yaml = YAML()
        yaml.preserve_quotes = True
        yaml.width = 4096
        yaml.indent(mapping=2, sequence=4, offset=2)
        doc = CommentedMap()
        doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        doc["title"] = f"{short.upper()} Geochem Profile"
        doc["description"] = (
            f"Geochem dataset profile for {short.upper()}. Extends adaProduct "
            f"with a {DETAIL_NAME} detail block and a schema:measurementTechnique "
            f"that points at a {TAPP_NAME} TAPP definition."
        )
        allof = CommentedSeq()
        allof.append({"$ref": "../../adaProfiles/adaProduct/schema.yaml"})
        overlay = CommentedMap()
        overlay["type"] = "object"
        ovprops = CommentedMap()
        # measurementTechnique points at the TAPP
        mt = CommentedMap()
        mt["description"] = f"TAPP definition reference or inline."
        mt_anyof = CommentedSeq()
        ref_branch = CommentedMap()
        ref_branch["type"] = "object"
        ref_branch["properties"] = CommentedMap([("@id", {"type": "string", "format": "uri"})])
        ref_branch["required"] = CommentedSeq(["@id"])
        mt_anyof.append(ref_branch)
        mt_anyof.append({"$ref": f"../../../techniqueProtocols/{TAPP_NAME}/schema.yaml"})
        mt["anyOf"] = mt_anyof
        ovprops["schema:measurementTechnique"] = mt
        # distribution.hasPart includes the detail BB
        dist = CommentedMap()
        dist["type"] = "array"
        dist_items = CommentedMap()
        dist_items["type"] = "object"
        dist_props = CommentedMap()
        hp = CommentedMap()
        hp["items"] = CommentedMap([("anyOf", CommentedSeq([
            {"$ref": "../../adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentTypeBranch"},
            {"$ref": f"../../../geochemProperties/{DETAIL_NAME}/schema.yaml"},
        ]))])
        dist_props["schema:hasPart"] = hp
        dist_items["properties"] = dist_props
        dist["items"] = dist_items
        ovprops["schema:distribution"] = dist
        overlay["properties"] = ovprops
        allof.append(overlay)
        doc["allOf"] = allof
        with open(schema_path, "w", encoding="utf-8") as f:
            yaml.dump(doc, f)
        print(f"  scaffolded {schema_path.relative_to(REPO_ROOT)}")
    else:
        print(f"  {schema_path.relative_to(REPO_ROOT)} already exists — skipping")

    bblock_path = profile_dir / "bblock.json"
    if not bblock_path.exists():
        bblock = OrderedDict([
            ("$schema", "metaschema.yaml"),
            ("name", f"{short.upper()} Geochem Profile"),
            ("abstract", (
                f"Technique-specific dataset profile for {short.upper()}. "
                f"Extends adaProduct with constraints on schema:measurementTechnique "
                f"(pointing at {TAPP_NAME}) and schema:distribution.schema:hasPart "
                f"(allowing {DETAIL_NAME} entries)."
            )),
            ("status", "under-development"),
            ("itemClass", "schema"),
            ("register", "ada-building-block-register"),
            ("version", "0.1"),
            ("maturity", "draft"),
            ("scope", "unstable"),
            ("tags", ["ada", "geochem", "profile", short.lower()]),
        ])
        write_json(bblock_path, bblock)
        print(f"  scaffolded {bblock_path.relative_to(REPO_ROOT)}")
    else:
        print(f"  {bblock_path.relative_to(REPO_ROOT)} already exists — skipping")


def main():
    """Backward-compat: run both sides and write examples.yaml."""
    build_tapp_artifacts()
    build_detail_artifacts()


if __name__ == "__main__":
    main()
