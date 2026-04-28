"""One-shot: generate empaTAPP building block from the TAPP_EPMA_filled spreadsheet.

Reads docs/TAPP_EPMA_filled.xlsx (sheet 'TAPP') and emits, into
_sources/techniqueProtocols/empaTAPP/:

- vocab/<name>.json          one schema:DefinedTermSet per enum-typed row
- parameters/<Name>.json     one schema:PropertyValueSpecification per parameter row
- analyteColumns/<col>.json  one schema:PropertyValueSpecification per analyteColumn row
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
DETAIL_EMPA = REPO_ROOT / "_sources" / "geochemProperties" / DETAIL_NAME


def configure(tapp_name: str, xlsx_path: str | Path | None = None) -> None:
    """Set module globals for a build run. tapp_name like 'empaTAPP' / 'xrdTAPP'.
    The detail BB name is derived as 'detail' + uppercase(strip-'TAPP'(tapp_name))
    — e.g. 'empaTAPP' → 'detailEMPA', 'xrdTAPP' → 'detailXRD'."""
    global TAPP_NAME, DETAIL_NAME, XLSX, BB, DETAIL_EMPA
    TAPP_NAME = tapp_name
    short = tapp_name.replace("TAPP", "").upper()
    DETAIL_NAME = f"detail{short}"
    if xlsx_path is not None:
        p = Path(xlsx_path)
        XLSX = p if p.is_absolute() else REPO_ROOT / p
    BB = REPO_ROOT / "_sources" / "techniqueProtocols" / TAPP_NAME
    DETAIL_EMPA = REPO_ROOT / "_sources" / "geochemProperties" / DETAIL_NAME

# Phase 1 dictionary directories — analyteColumns/parameterTemplates/parameterValues/vocab
# live at the techniqueProtocols root so multiple TAPPs can reference the same catalog
# entries by $ref. The generator writes catalog files here; per-TAPP schema.yaml files
# point at them with relative paths (e.g. ../analyteColumns/<name>.json from a TAPP folder).
TECH_PROTOCOLS = REPO_ROOT / "_sources" / "techniqueProtocols"
ANALYTE_COLUMNS_DIR = TECH_PROTOCOLS / "analyteColumns"
PARAMETER_TEMPLATES_DIR = TECH_PROTOCOLS / "parameterTemplates"
PARAMETER_VALUES_DIR = TECH_PROTOCOLS / "parameterValues"
VOCAB_DIR = TECH_PROTOCOLS / "vocab"

# Column letters in the spreadsheet (1-indexed: A=1)
COL = {
    "item": 0, "desc": 1, "basic": 2, "dtype": 3, "example": 4,
    "p_start": 6,  # column G = index 6 (P0 — synthetic comprehensive example)
    "p_end": 16,   # column Q = index 16 (inclusive; P10)
    "level": 17, "cdif_path": 18, "matchComment": 19, "impl": 20,
}
PUBS = [
    ("P0", "Richard & Deng 2026 (synthetic comprehensive WDS example)"),
    ("P1", "Chi et al. 2015 (Tissintite, EPSL)"),
    ("P2", "Hu et al. 2020 (Coesite NWA8657, GCA)"),
    ("P3", "Liu et al. 2016 (Tissint mineral chem., MAPS)"),
    ("P4", "Ma et al. 2017 (Liebermannite, MAPS)"),
    ("P5", "Frank et al. 2023 (Ivuna CAI, MAPS)"),
    ("P6", "Broussard et al. 2026 (OC002 CI chondrite, MAPS)"),
    ("P7", "Seifert et al. 2026 (Bennu apatite, MAPS)"),
    ("P8", "Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.)"),
    ("P9", "McCoy et al. 2025 (Bennu evaporites, Nature)"),
    ("P10", "Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)"),
]

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
    rows = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        item = r[COL["item"]]
        impl = r[COL["impl"]]
        if item is None and impl is None:
            continue
        rec = {
            "item": str(item).strip() if item is not None else None,
            "desc": str(r[COL["desc"]]).strip() if r[COL["desc"]] is not None else None,
            "dtype_col": str(r[COL["dtype"]]).strip() if r[COL["dtype"]] is not None else None,
            "example": str(r[COL["example"]]).strip() if r[COL["example"]] is not None else None,
            "cdif_path": str(r[COL["cdif_path"]]).strip() if r[COL["cdif_path"]] is not None else None,
            "matchComment": str(r[COL["matchComment"]]).strip() if r[COL["matchComment"]] is not None else None,
            "impl": str(r[COL["impl"]]).strip() if r[COL["impl"]] is not None else None,
            "pubs": [r[i] for i in range(COL["p_start"], COL["p_end"] + 1)],
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

    new_id = data.get("$id", "") or ""
    existing_id = existing.get("$id", "") or ""

    # If the existing file is owned by THIS TAPP's regen, overwrite.
    if f"/{TAPP_NAME}/" in existing_id:
        write_json(path, data)
        return

    # Foreign owner — must match exactly to share.
    if existing == data:
        return

    raise ValueError(
        f"Catalog conflict at {path}:\n"
        f"  existing $id={existing_id!r} (owned by another TAPP)\n"
        f"  new      $id={new_id!r}\n"
        f"  Either change the spreadsheet to match the existing definition "
        f"(sharing) or rename the entry in the spreadsheet to avoid the "
        f"collision."
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
        ("@context", {"const": _ADA_CONTEXT}),
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
    spreadsheet's Data Type column. schema:unitText pinned when the dtype carries a
    parenthesised unit (e.g. 'Numeric (kV)' → unitText 'kV').
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
        ("@context", {"const": _ADA_CONTEXT}),
        ("@id", {"const": parameter_uri}),
        ("@type", {"const": ["schema:PropertyValue"]}),
        ("schema:propertyID", {"const": parameter_uri}),
        ("schema:name", {"const": label}),
        ("schema:value", value_schema),
    ])
    required = ["@id", "@type", "schema:propertyID", "schema:name", "schema:value"]
    if unit:
        properties["schema:unitText"] = {"const": unit}
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
        ("@context", {"const": _ADA_CONTEXT}),
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
    - For each spreadsheet row whose CDIF-geochem schema path matches
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
        cdif = row.get("cdif_path") or ""
        m = HASPART_RE.search(cdif)
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


def write_detail_empa_constraint(detail_param_names: list[str]) -> None:
    """Write _sources/geochemProperties/detailEMPA/parametersConstraint.yaml — a
    JSON Schema fragment carrying schema:additionalProperty.items.oneOf
    referencing each detailEMPA/parameters/<name>.json catalog file plus a
    catch-all branch so authors can attach arbitrary additional schema:PropertyValue
    entries beyond the spreadsheet-listed ones. detailEMPA/schema.yaml is expected
    to allOf this snippet alongside its hand-authored componentType constraints."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)

    out = DETAIL_EMPA / "parametersConstraint.yaml"
    if not detail_param_names:
        if out.exists():
            out.unlink()
        return

    branches = CommentedSeq()
    for n in sorted(detail_param_names):
        branches.append({"$ref": f"../../techniqueProtocols/parameterValues/{n}.json"})
    # Catch-all so an author can attach arbitrary other PropertyValue items
    catch_all = CommentedMap()
    catch_all["type"] = "object"
    catch_all["description"] = (
        "Catch-all for additional schema:PropertyValue entries beyond those "
        "enumerated in the empaTAPP-derived catalog above."
    )
    catch_all_props = CommentedMap()
    catch_all_props["@type"] = {
        "type": "array",
        "items": {"type": "string"},
        "contains": {"const": "schema:PropertyValue"},
    }
    catch_all_props["schema:propertyID"] = {
        "type": "string",
        "not": {
            "enum": [f"ada:parameter/{TAPP_NAME}/{n}" for n in sorted(detail_param_names)]
        },
    }
    catch_all["properties"] = catch_all_props
    catch_all["required"] = CommentedSeq(["@type", "schema:propertyID"])
    branches.append(catch_all)

    items = CommentedMap()
    items["oneOf"] = branches

    add_prop = CommentedMap()
    add_prop["type"] = "array"
    add_prop["description"] = (
        "Per-dataset schema:PropertyValue entries for this EMPA dataset. "
        "Each item is one of the empaTAPP-derived parameter types or "
        "(via the catch-all branch) any other PropertyValue."
    )
    add_prop["items"] = items

    doc = CommentedMap()
    doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    doc["title"] = "detailEMPA additionalProperty constraint (generated from empaTAPP spreadsheet)"
    doc["type"] = "object"
    doc["properties"] = CommentedMap([("schema:additionalProperty", add_prop)])

    DETAIL_EMPA.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        yaml.dump(doc, f)
    print(f"  wrote {out.relative_to(REPO_ROOT)} ({len(detail_param_names)} additionalProperty types)")


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


def cleanup_orphan_param_files(empa_param_names: list[str], detail_param_names: list[str]) -> None:
    """Delete *.json under techniqueProtocols/parameterTemplates/ or
    techniqueProtocols/parameterValues/ that don't correspond to a current
    spreadsheet parameter row in the appropriate bucket. Avoids stale
    orphans after spreadsheet edits or readOnly toggles."""
    keep_empa = set(empa_param_names)
    keep_detail = set(detail_param_names)
    if PARAMETER_TEMPLATES_DIR.exists():
        for fp in PARAMETER_TEMPLATES_DIR.glob("*.json"):
            if fp.stem not in keep_empa:
                fp.unlink()
                print(f"  deleted orphan {fp.relative_to(REPO_ROOT)}")
    if PARAMETER_VALUES_DIR.exists():
        for fp in PARAMETER_VALUES_DIR.glob("*.json"):
            if fp.stem not in keep_detail:
                fp.unlink()
                print(f"  deleted orphan {fp.relative_to(REPO_ROOT)}")


def build_schema_yaml(properties: list[tuple[str, dict]],
                      analyte_column_names: list[str],
                      parameter_names: list[str],
                      instrument_haspart: dict | None) -> None:
    """Rebuild empaTAPP/schema.yaml with the new property set in allOf[1].properties
    and oneOf constraints on ada:analyteColumns[] and ada:methodParameters[]
    referencing the catalog files."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)

    doc = CommentedMap()
    doc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    doc["title"] = "EMPA Technique-Aligned Protocol Profile (empaTAPP)"
    doc["description"] = (
        "EMPA-specific extension of the base TAPP definition. Adds top-level EPMA "
        "properties (beam mode, accelerating voltage default, matrix correction "
        "method, etc.), a parameter vocabulary in ada:methodParameters, and an "
        "analyte-column template covering EPMA per-element acquisition and "
        "reporting fields. Each ada:analyteColumns[] entry must match one of the "
        "catalog files in analyteColumns/ (or the inherited identifier column from "
        "tappDefinition); each catalog file is itself a JSON Schema whose "
        "examples[0] carries the canonical instance. Generated from "
        "docs/TAPP_EPMA_filled.xlsx by tools/build_empaTAPP_from_spreadsheet.py."
    )
    allof = CommentedSeq()
    allof.append({"$ref": "../tappDefinition/schema.yaml"})
    overlay = CommentedMap()
    overlay["type"] = "object"
    props = CommentedMap()
    for ada_prop, schema_block in properties:
        # convert OrderedDict (or any dict) to CommentedMap so ruamel.yaml emits plain mapping
        cm = CommentedMap()
        for k, v in schema_block.items():
            if isinstance(v, list):
                seq = CommentedSeq()
                for x in v:
                    seq.append(x)
                cm[k] = seq
            else:
                cm[k] = v
        props[ada_prop] = cm

    if analyte_column_names:
        anyof = CommentedSeq()
        anyof.append({"$ref": "../tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn"})
        for col_name in sorted(analyte_column_names):
            anyof.append({"$ref": f"../analyteColumns/{col_name}.json"})

        ac_items = CommentedMap()
        ac_items["anyOf"] = anyof

        # Per-catalog uniqueness: at most one occurrence of each column type.
        # (The identifier column's exactly-once constraint lives in tappDefinition
        # via contains + maxContains: 1.)
        ac_unique = CommentedSeq()
        for col_name in sorted(analyte_column_names):
            cm = CommentedMap()
            cm["contains"] = {"$ref": f"../analyteColumns/{col_name}.json"}
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
            mp_anyof.append({"$ref": f"../parameterTemplates/{param_name}.json"})

        mp_items = CommentedMap()
        mp_items["anyOf"] = mp_anyof

        mp_unique = CommentedSeq()
        for param_name in sorted(parameter_names):
            cm = CommentedMap()
            cm["contains"] = {"$ref": f"../parameterTemplates/{param_name}.json"}
            cm["minContains"] = 0
            cm["maxContains"] = 1
            mp_unique.append(cm)

        mp_array = CommentedMap()
        mp_array["type"] = "array"
        mp_array["items"] = mp_items
        mp_array["allOf"] = mp_unique

        props["ada:methodParameters"] = mp_array

    if instrument_haspart:
        props["schema:instrument"] = _to_commented(instrument_haspart)

    overlay["properties"] = props
    allof.append(overlay)
    doc["allOf"] = allof

    out = BB / "schema.yaml"
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
    `property:` tags + readOnly:true ada:methodParameters templates).
    detailEMPA carries the per-dataset values (schema:additionalProperty entries
    for readOnly:false parameters with a value in this publication's column),
    pointing back at the empaTAPP via schema:measurementTechnique by @id.
    """
    pub_code = PUBS[pub_index][0].lower()
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
    parts["schema:description"] = f"empaTAPP example derived from {pub_label}."
    parts["schema:measurementTechnique"] = {
        "@type": ["schema:DefinedTerm"],
        "schema:termCode": "EPMA-WDS",
        "schema:name": "Electron Microprobe Analysis - WDS",
    }

    detail = OrderedDict()
    detail["@context"] = dict(_ADA_CONTEXT)
    detail["@id"] = detail_id
    detail["@type"] = ["schema:Thing"]
    detail["ada:componentType"] = "ada:EMPAQEATabular"
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
                "schema:additionalType": ["nxs:BaseClass/NXinstrument", "ada:EPMAInstrument"],
                "schema:name": "EPMA instrument",
            })
            if item == "Instrument Manufacturer":
                inst["schema:manufacturer"] = {"@type": ["schema:Organization"], "schema:name": str(val).strip()}
            else:
                inst["schema:model"] = {"@type": ["schema:ProductModel"], "schema:name": str(val).strip()}
                inst["schema:name"] = inst.get("schema:manufacturer", {}).get("schema:name", "EPMA") + " " + str(val).strip()
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
                        ("@context", dict(_ADA_CONTEXT)),
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
        parts["ada:methodParameters"] = method_params
    if not parts["schema:name"]:
        parts["schema:name"] = f"EPMA TAPP example {PUBS[pub_index][0]}"

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
        # canonicals for each analyteColumn name actually used by this example.
        catalog_dir = ANALYTE_COLUMNS_DIR
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
                if tr["kind"] != "analytecolumn" or tr["name"] in seen:
                    continue
                seen.add(tr["name"])
                cf = catalog_dir / f'{tr["name"]}.json'
                if cf.exists():
                    cd = json.loads(cf.read_text(encoding="utf-8"))
                    ex = (cd.get("examples") or [{}])[0]
                    ex_clean = OrderedDict((k, v) for k, v in ex.items() if k != "@context")
                    analyte_cols.append(ex_clean)

        parts["ada:analyteTemplate"] = OrderedDict([
            ("ada:analyteColumns", analyte_cols),
            ("ada:defaultAnalytes", default_rows),
        ])

    return parts, detail


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
                    # only emitted when building the TAPP side.
                    if emit_tapp:
                        path = PARAMETER_TEMPLATES_DIR / f"{name}.json"
                        share_or_write_catalog(path, parameter_obj(name, row["item"], row["desc"], tag_dtype, vocab_name, ro))
                    parameter_names.append(name)
                    counts["parameter"] += 1
                else:
                    # readOnly:false → per-dataset value (PropertyValue);
                    # only emitted when building the detail side.
                    if emit_detail:
                        path = PARAMETER_VALUES_DIR / f"{name}.json"
                        share_or_write_catalog(path, additional_property_obj(
                            name, row["item"], row["desc"],
                            row.get("dtype_col"), vocab_name, tag_dtype,
                        ))
                    detail_param_names.append(name)
                    counts["detailParameter"] += 1
            elif kind == "analytecolumn":
                # analyteColumns are TAPP-side artifacts.
                if emit_tapp:
                    path = ANALYTE_COLUMNS_DIR / f"{name}.json"
                    share_or_write_catalog(path, analyte_column_obj(name, row["item"], row["desc"], tag_dtype, vocab_name, ro))
                counts["analyteColumn"] += 1
                analyte_column_names.append(name)
            elif kind == "property":
                # Skip non-property markers: "analyteTemplate" references the existing
                # ada:analyteTemplate structure inherited from tappDefinition (not a
                # new top-level property); "description" maps to the existing
                # schema:description (the cdif_path confirms this for the relevant row).
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


def build_tapp_artifacts() -> dict:
    """Generate the TAPP-side artifacts only:
    - shared catalog files in techniqueProtocols/{analyteColumns,parameterTemplates,vocab}/
    - TAPP BB schema.yaml at techniqueProtocols/<TAPP_NAME>/
    - per-publication TAPP examples + examples.yaml
    Per-tag readOnly:false rows are tracked but their PropertyValue catalog is NOT
    written (the detail-builder writes those). Returns the classification dict."""
    rows = read_rows()
    print(f"Read {len(rows)} non-empty rows from TAPP worksheet.")

    cls = _classify_rows(rows, emit_tapp=True, emit_detail=False)

    instrument_haspart = build_haspart_constraint(rows)
    build_schema_yaml(
        cls["schema_properties"], cls["analyte_column_names"],
        cls["parameter_names"], instrument_haspart,
    )

    # Orphan cleanup for templates only — keep parameterValues alone (detail-builder owns it).
    keep_templates = set(cls["parameter_names"])
    if PARAMETER_TEMPLATES_DIR.exists():
        for fp in PARAMETER_TEMPLATES_DIR.glob("*.json"):
            if fp.stem not in keep_templates:
                # Foreign-owned templates (other TAPPs) — never touch.
                try:
                    with open(fp, "r", encoding="utf-8") as f:
                        existing_id = (json.load(f) or {}).get("$id", "") or ""
                except (OSError, json.JSONDecodeError):
                    continue
                if f"/{TAPP_NAME}/" in existing_id:
                    fp.unlink()
                    print(f"  deleted orphan {fp.relative_to(REPO_ROOT)}")

    # Per-publication TAPP examples
    examples_yaml = []
    for i, (pcode, plabel) in enumerate(PUBS):
        empa_ex, _ = example_for_pub(i, plabel, rows)
        write_json(BB / f"example{TAPP_NAME}-{pcode}.json", empa_ex)
        examples_yaml.append((pcode, plabel))
    print(f"  wrote {len(PUBS)} per-publication {TAPP_NAME} examples")

    _write_examples_yaml(examples_yaml)
    print(f"\nCounts: {cls['counts']}")
    return cls


def build_detail_artifacts() -> dict:
    """Generate the detail-side artifacts only:
    - shared parameterValues/<name>.json catalog files
    - detailXXX/parametersConstraint.yaml ($ref'd by hand-authored detailXXX/schema.yaml)
    - per-publication detailXXX examples
    Returns the classification dict."""
    rows = read_rows()
    print(f"Read {len(rows)} non-empty rows from TAPP worksheet.")

    cls = _classify_rows(rows, emit_tapp=False, emit_detail=True)

    scaffold_detail_bb_if_missing()
    write_detail_empa_constraint(cls["detail_param_names"])

    # Orphan cleanup for parameterValues — only files owned by THIS TAPP get deleted.
    keep_values = set(cls["detail_param_names"])
    if PARAMETER_VALUES_DIR.exists():
        for fp in PARAMETER_VALUES_DIR.glob("*.json"):
            if fp.stem not in keep_values:
                try:
                    with open(fp, "r", encoding="utf-8") as f:
                        existing_id = (json.load(f) or {}).get("$id", "") or ""
                except (OSError, json.JSONDecodeError):
                    continue
                if f"/{TAPP_NAME}/" in existing_id:
                    fp.unlink()
                    print(f"  deleted orphan {fp.relative_to(REPO_ROOT)}")

    # Per-publication detail examples
    written = 0
    for i, (pcode, _plabel) in enumerate(PUBS):
        _, detail_ex = example_for_pub(i, _plabel, rows)
        if detail_ex.get("schema:additionalProperty"):
            write_json(DETAIL_EMPA / f"example{DETAIL_NAME}-{pcode}.json", detail_ex)
            written += 1
    print(f"  wrote {written} per-publication {DETAIL_NAME} examples")

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
