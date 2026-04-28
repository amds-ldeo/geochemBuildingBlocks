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
XLSX = REPO_ROOT / "docs" / "TAPP_EPMA_filled.xlsx"
BB = REPO_ROOT / "_sources" / "techniqueProtocols" / "empaTAPP"

# Column letters in the spreadsheet (1-indexed: A=1)
COL = {
    "item": 0, "desc": 1, "basic": 2, "dtype": 3, "example": 4,
    "p_start": 7,  # column H = index 7
    "p_end": 16,   # column Q = index 16 (inclusive)
    "level": 17, "cdif_path": 18, "matchComment": 19, "impl": 20,
}
PUBS = [
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


def parse_impl(impl: str) -> dict:
    """Return {tags: [(kind, name), ...], dtype: str|None, enum: [str]|None, readOnly: bool|None}."""
    if not impl:
        return {"tags": [], "dtype": None, "enum": None, "readOnly": None}
    tags = [(k.lower(), n) for k, n in TAG_RE.findall(impl)]
    dt = DTYPE_RE.search(impl)
    dtype = dt.group(1).strip() if dt else None
    em = ENUM_RE.search(impl)
    enum_vals = None
    if em:
        enum_vals = [v.strip() for v in em.group(1).split("|") if v.strip()]
    ro = READONLY_RE.search(impl)
    read_only = None
    if ro:
        read_only = ro.group(1).lower() == "true"
    return {"tags": tags, "dtype": dtype, "enum": enum_vals, "readOnly": read_only}


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


DEFINED_TERM_SET_SCHEMA_URI = (
    "https://cross-domain-interoperability-framework.github.io/"
    "metadataBuildingBlocks/_sources/schemaorgProperties/definedTermSet/schema.yaml"
)


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
        ("@id", f"ada:vocab/empaTAPP/{vname}"),
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
        ("@id", f"ada:parameter/empaTAPP/{name}"),
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
        canonical["schema:inDefinedTermSet"] = {"@id": f"ada:vocab/empaTAPP/{enum_vname}"}

    properties = OrderedDict([
        ("schema:valueName", {"const": name}),
        ("schema:name", {"const": label}),
        ("ada:dataType", {"const": dt}),
        ("ada:fieldScope", {"const": "session"}),
        ("schema:readonlyValue", {"const": ro}),
        ("ada:tier", {"const": tier}),
    ])
    if enum_vname:
        properties["schema:inDefinedTermSet"] = {
            "const": {"@id": f"ada:vocab/empaTAPP/{enum_vname}"}
        }

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"ada:parameter/empaTAPP/{name}"),
        ("title", label),
        ("description", desc or label),
        ("type", "object"),
        ("properties", properties),
        ("required", ["schema:valueName", "schema:name", "ada:dataType", "ada:fieldScope"]),
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
        ("@id", f"ada:analyteColumn/empaTAPP/{name}"),
        ("@type", ["schema:PropertyValueSpecification"]),
        ("schema:name", label),
        ("schema:valueName", name),
        ("schema:description", desc or label),
        ("ada:dataType", dt),
        ("schema:readonlyValue", ro),
        ("ada:tier", tier),
    ])
    if enum_vname:
        canonical["schema:inDefinedTermSet"] = {"@id": f"ada:vocab/empaTAPP/{enum_vname}"}

    properties = OrderedDict([
        ("schema:valueName", {"const": name}),
        ("schema:name", {"const": label}),
        ("ada:dataType", {"const": dt}),
        ("schema:readonlyValue", {"const": ro}),
        ("ada:tier", {"const": tier}),
    ])
    if enum_vname:
        properties["schema:inDefinedTermSet"] = {
            "const": {"@id": f"ada:vocab/empaTAPP/{enum_vname}"}
        }

    return OrderedDict([
        ("$schema", "https://json-schema.org/draft/2020-12/schema"),
        ("$id", f"ada:analyteColumn/empaTAPP/{name}"),
        ("title", label),
        ("description", desc or label),
        ("type", "object"),
        ("properties", properties),
        ("required", ["schema:valueName", "schema:name", "ada:dataType"]),
        ("examples", [canonical]),
    ])


# ---------- schema.yaml writer ----------

def build_schema_yaml(properties: list[tuple[str, dict]],
                      analyte_column_names: list[str],
                      parameter_names: list[str]) -> None:
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
        oneof = CommentedSeq()
        oneof.append({"$ref": "../tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn"})
        for col_name in sorted(analyte_column_names):
            oneof.append({"$ref": f"analyteColumns/{col_name}.json"})

        ac_items = CommentedMap()
        ac_items["oneOf"] = oneof

        ac_columns = CommentedMap()
        ac_columns["type"] = "array"
        ac_columns["items"] = ac_items

        ac_template_props = CommentedMap()
        ac_template_props["ada:analyteColumns"] = ac_columns

        ac_template = CommentedMap()
        ac_template["type"] = "object"
        ac_template["properties"] = ac_template_props

        props["ada:analyteTemplate"] = ac_template

    if parameter_names:
        mp_oneof = CommentedSeq()
        for param_name in sorted(parameter_names):
            mp_oneof.append({"$ref": f"parameters/{param_name}.json"})

        mp_items = CommentedMap()
        mp_items["oneOf"] = mp_oneof

        mp_array = CommentedMap()
        mp_array["type"] = "array"
        mp_array["items"] = mp_items

        props["ada:methodParameters"] = mp_array

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


def example_for_pub(pub_index: int, pub_label: str, rows: list[dict]) -> dict:
    """Build one empaTAPP instance from publication column data."""
    parts = OrderedDict()
    parts["@context"] = {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "bios": "https://bioschemas.org/",
    }
    pub_code = PUBS[pub_index][0].lower()
    parts["@id"] = f"ex:empaTAPP-{pub_code}"
    parts["@type"] = [
        "cdi:Activity", "schema:Action", "ada:TAPPDefinition", "bios:LabProtocol",
    ]
    parts["schema:name"] = ""  # filled below if Method Name present
    parts["schema:description"] = f"empaTAPP example derived from {pub_label}."
    parts["schema:measurementTechnique"] = {
        "@type": ["schema:DefinedTerm"],
        "schema:termCode": "EPMA-WDS",
        "schema:name": "Electron Microprobe Analysis - WDS",
    }
    method_params = []
    for row in rows:
        val = row["pubs"][pub_index] if pub_index < len(row["pubs"]) else None
        if val is None or (isinstance(val, str) and not val.strip()):
            continue
        item = row["item"]
        if not item:
            continue
        # Method Name special-case
        if item == "Method Name":
            parts["schema:name"] = str(val).strip()
            continue
        if item == "Method Author":
            parts["schema:agent"] = {
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
        # Now process by impl tag
        for kind, name in row["parsed"]["tags"]:
            if kind == "property":
                if name in ("analyteTemplate", "description"):
                    continue
                # Set top-level ada:<name>. Keep value as string (the schema declares
                # type: string for these). For enum-constrained properties, only emit
                # the value if it matches the enum; otherwise skip (publication data is
                # often free-text rather than a clean enum match).
                key = f"ada:{name}"
                v = str(val).strip()
                allowed = row["parsed"]["enum"]
                if allowed and v not in allowed:
                    # value doesn't match the strict enum — skip rather than fail validation
                    continue
                parts[key] = v
            elif kind == "parameter":
                # add a methodParameters entry referencing the parameter template
                method_params.append({
                    "@type": ["schema:PropertyValueSpecification"],
                    "schema:name": item,
                    "schema:valueName": name,
                    "schema:description": row["desc"] or item,
                    "ada:dataType": map_dtype(row["parsed"]["dtype"]),
                    "ada:fieldScope": "session",
                    "schema:readonlyValue": bool(row["parsed"]["readOnly"]) if row["parsed"]["readOnly"] is not None else False,
                    "ada:tier": "R",
                    "schema:defaultValue": str(val).strip(),
                })
            # analyteColumn: per-element data not in the publication columns; skip for examples
    if method_params:
        parts["ada:methodParameters"] = method_params
    if not parts["schema:name"]:
        parts["schema:name"] = f"EPMA TAPP example {PUBS[pub_index][0]}"
    return parts


# ---------- main ----------

def main():
    rows = read_rows()
    print(f"Read {len(rows)} non-empty rows from TAPP worksheet.")

    schema_properties: list[tuple[str, dict]] = []
    analyte_column_names: list[str] = []
    parameter_names: list[str] = []
    enum_to_vocab_name: dict[tuple[str, ...], str] = {}
    counts = {"vocab": 0, "parameter": 0, "analyteColumn": 0, "property": 0}

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
        # Write vocab file
        path = BB / "vocab" / f"{name}.json"
        write_json(path, vocab_obj(name, row["item"] or name, row["desc"], p["enum"]))
        counts["vocab"] += 1

    def vocab_for(p):
        if not p["enum"]:
            return None
        return enum_to_vocab_name.get(tuple(sorted(p["enum"])))

    # Emit parameter and analyteColumn JSON, and collect properties for schema.yaml
    for row in rows:
        p = row["parsed"]
        for kind, name in p["tags"]:
            if kind == "parameter":
                path = BB / "parameters" / f"{name}.json"
                write_json(path, parameter_obj(name, row["item"], row["desc"], p["dtype"], vocab_for(p), p["readOnly"]))
                counts["parameter"] += 1
                parameter_names.append(name)
            elif kind == "analytecolumn":
                path = BB / "analyteColumns" / f"{name}.json"
                write_json(path, analyte_column_obj(name, row["item"], row["desc"], p["dtype"], vocab_for(p), p["readOnly"]))
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
                if p["enum"]:
                    block["type"] = "string"
                    block["enum"] = list(p["enum"])
                else:
                    block["type"] = map_dtype(p["dtype"]) if map_dtype(p["dtype"]) != "string" else "string"
                schema_properties.append((f"ada:{name}", block))
                counts["property"] += 1

    # Dedupe properties by ada:<name>, last one wins (for repeated tags)
    seen = OrderedDict()
    for prop_name, block in schema_properties:
        seen[prop_name] = block
    schema_properties = list(seen.items())

    build_schema_yaml(schema_properties, analyte_column_names, parameter_names)

    # Generate examples for each publication
    examples_dir = BB
    examples_yaml = []
    for i, (pcode, plabel) in enumerate(PUBS):
        ex = example_for_pub(i, plabel, rows)
        path = examples_dir / f"exampleempaTAPP-{pcode}.json"
        write_json(path, ex)
        examples_yaml.append((pcode, plabel))
    print(f"  wrote {len(PUBS)} per-publication examples")

    # Update examples.yaml
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    ex_doc = CommentedSeq()
    for pcode, plabel in examples_yaml:
        e = CommentedMap()
        e["title"] = f"empaTAPP example {pcode}: {plabel}"
        e["content"] = (
            f"empaTAPP instance derived from publication {plabel}. Property and parameter values "
            "taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet."
        )
        e["prefixes"] = {
            "ada": "https://ada.astromat.org/metadata/",
            "schema": "http://schema.org/",
            "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
            "bios": "https://bioschemas.org/",
        }
        snip = CommentedMap()
        snip["language"] = "json"
        snip["ref"] = f"exampleempaTAPP-{pcode}.json"
        e["snippets"] = [snip]
        ex_doc.append(e)
    with open(BB / "examples.yaml", "w", encoding="utf-8") as f:
        yaml.dump(ex_doc, f)
    print(f"  wrote examples.yaml with {len(PUBS)} entries")

    print(f"\nCounts: {counts}")


if __name__ == "__main__":
    main()
