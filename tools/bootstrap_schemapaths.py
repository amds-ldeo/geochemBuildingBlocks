"""Bootstrap a workbook's schema-path placement spec (docs/<wb>.schemapaths.json) WITHOUT a hand-
authored `schema path` column, by combining:

  1. a path LIBRARY from an already-clean reference workbook (LA-Q_SF-ICPMS) — reused for rows whose
     Metadata Item matches (exactly, or via a Procedure<->Protocol rename);
  2. CONTENT inference for the rest — direct protocol props, method parameters, analyte columns, and
     the shared analysis-instance rows — from the tier + Data Type columns.

Every inferred path is canonicalised (normalize_schema_paths.mechanical) and parser-validated
(schema_path_parser); anything that can't be resolved is FLAGGED for a human (typically the
technique-specific instrument tree). Output feeds the existing path-driven generator unchanged.

    python tools/bootstrap_schemapaths.py <workbook.xlsx>            # write spec + coverage report
    python tools/bootstrap_schemapaths.py <workbook.xlsx> --dry-run
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import tapp_source
import normalize_schema_paths as norm
import schema_path_parser as spp
import schemapath_io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# the reference library is the (curated) LA-Q sidecar CSV
LIB_SPEC = schemapath_io.csv_path(os.path.join(ROOT, "docs", "LA-Q_SF-ICPMS_TAPP_v3.xlsx"))

# analysis-instance shared rows keyed by a normalized item token -> canonical $Dataset path.
# (identical technique-to-technique; sourced from the LA-Q reference.)
SHARED = {
    "analyst": "$Dataset.schema:contributor[schema:roleName='analyst'].schema:name",
    "analysis start date": "$Dataset.prov:wasGeneratedBy.schema:startDate",
    "analysis end date": "$Dataset.prov:wasGeneratedBy.schema:endDate",
    "funding source for analysis": "$Dataset.schema:funding",
}


def _norm(s):
    return " ".join(str(s).split()).lower()


def _aslist(p):
    return list(p) if isinstance(p, list) else [p]


def load_rows(path):
    rs = tapp_source.rows(path)            # .csv or .xlsx
    hdr = [(str(c).strip() if c is not None else "") for c in rs[0]]
    def col(*pfx):
        return next((i for i, h in enumerate(hdr) for p in pfx if h.lower().startswith(p)), None)
    ci = {"P": col("procedure-level", "protocol-level", "procedure", "protocol"),
          "A": col("analysis-level", "analysis"), "dt": col("data type"),
          "kb": col("keyed by", "keyed")}
    out = []
    for r in rs[1:]:
        it = (str(r[0]).strip() if r[0] else "")
        if not it or re.match(r"^\d+\.\s", it):
            continue
        g = lambda k: (str(r[ci[k]]).strip() if ci[k] is not None and ci[k] < len(r) and r[ci[k]] else "")
        out.append({"item": it, "P": g("P"), "A": g("A"), "dt": g("dt"), "kb": g("kb")})
    return out


_MD_DEFAULT_RE = re.compile(
    r"^\$MethodDefinition\.schema:additionalProperty\[schema:name='(.+?)'\]\.schema:defaultValue$")


# (Protocol tier, Analysis tier) pairs the canonical matrix (docs/TierImplementationPatterns.xlsx)
# says are DUAL-HOMED: a protocol-level default in the TAPP plus a per-analysis value in the detail.
# Advanced/Basic belongs here because the matrix requires a detail property for it; it previously
# fell through to the read-only branch and landed in the TAPP only.
DUAL_HOMED = {("Advanced", "Editable"), ("Advanced", "Advanced"), ("Advanced", "Basic"),
              ("Basic", "Editable")}

# Matching $Dataset counterpart for a direct ada: protocol property (the Basic tier shape).
_MD_ADA_DEFAULT_RE = re.compile(r"^\$MethodDefinition\.ada:(.+?)Default$")

# A TAPP path nested under an instrument or a workflow step. The tail may express its default
# either way, and both forms are in use:
#   …schema:instrument[X].schema:additionalProperty[P].schema:defaultValue   (Advanced shape)
#   …schema:instrument[X].ada:acceleratingVoltageDefault                     (Basic shape, nested)
_MD_NESTED_RE = re.compile(
    r"^\$MethodDefinition\.(schema:instrument\[[^\]]*\]|schema:actionProcess\.schema:step\[[^\]]*\])"
    r"\.(.+)$")
_ADA_DEFAULT_TAIL_RE = re.compile(r"^(ada:.+)Default$")


# Anything under ada:analyteTemplate — the per-analyte column definitions and the default analyte
# rows.
_ANALYTE_TEMPLATE_RE = re.compile(r"\bada:analyteTemplate\b")


def is_analyte_template(path):
    """True for a path targeting the analyte template, which is NEVER dual-homed.

    An analyteColumn is a column DEFINITION, not a value: the per-analyte values live in the rows —
    ada:defaultAnalytes on the TAPP side, and schema:variableMeasured on the dataset side. So there
    is nothing for a $Dataset schemapath to point at; the analysis-tier expression of an analyte
    column is a variableMeasured array that no schemapath row describes.

    Editable-vs-read-only is still carried, on the column's schema:readonlyValue (54 read-only /
    29 editable across the registry). AnalyteColumn does have a schema:defaultValue slot, but it is
    unused and means something different anyway — a default across ALL analyte rows, where the
    protocol's actual per-element defaults are the ada:defaultAnalytes rows themselves.

    Without this guard a Basic/Editable analyte column looks dual-homable on its tiers alone, and
    every pass would try to give it a $Dataset partner it must not have.
    """
    return bool(_ANALYTE_TEMPLATE_RE.search(path))


def _dataset_counterpart(path, item):
    if is_analyte_template(path):
        return None
    """The $Dataset partner for a TAPP-side default, MIRRORING any nesting.

    A nested default keeps its context on the dataset side rather than collapsing to a flat
    property, because the context is what says which instrument or which step the value belongs to:

      $MethodDefinition.schema:instrument[X].schema:additionalProperty[P].schema:defaultValue
        -> $Dataset.prov:wasGeneratedBy.prov:used[X].schema:additionalProperty[P].schema:value

      $MethodDefinition.schema:instrument[X].ada:acceleratingVoltageDefault
        -> $Dataset.prov:wasGeneratedBy.prov:used[X].ada:acceleratingVoltage

      $MethodDefinition.schema:actionProcess.schema:step[S]....schema:defaultValue
        -> $Dataset.prov:wasGeneratedBy.schema:actionProcess.schema:step[S]....schema:value

    schema:instrument maps to prov:used because that is where adaProduct's provenance activity
    carries the instrument. The Default marker is dropped on the dataset side — that value is the
    actual one, not a default. Un-nested defaults hang off prov:wasGeneratedBy too:

      $MethodDefinition.schema:additionalProperty[P].schema:defaultValue
        -> $Dataset.prov:wasGeneratedBy.schema:additionalProperty[P].schema:value
    """
    m = _MD_NESTED_RE.match(path)
    if m:
        head, tail = m.group(1), m.group(2)
        if tail.endswith(".schema:defaultValue"):
            tail = tail[: -len(".schema:defaultValue")] + ".schema:value"
        else:
            ada = _ADA_DEFAULT_TAIL_RE.match(tail)
            if not ada:
                return None      # nested but not a default (identity / read-only) -> no partner
            tail = ada.group(1)
        if head.startswith("schema:instrument["):
            head = "prov:used[" + head[len("schema:instrument["):]
        return f"$Dataset.prov:wasGeneratedBy.{head}.{tail}"
    # Un-nested defaults land on the provenance ACTIVITY, not the dataset itself: the value records
    # what this analysis session used, which is what prov:wasGeneratedBy denotes. A bare
    # `$Dataset.schema:additionalProperty[…]` is not a grammar family (SCHEMA_PATH_GRAMMAR.md lists
    # only `dataset-prov-parameter`), so emitting it produced rows no emitter could consume.
    if _MD_DEFAULT_RE.match(path):
        return (f"$Dataset.prov:wasGeneratedBy.schema:additionalProperty"
                f"[schema:name='{_MD_DEFAULT_RE.match(path).group(1)}'].schema:value")
    if _MD_ADA_DEFAULT_RE.match(path):
        return (f"$Dataset.prov:wasGeneratedBy.schema:additionalProperty"
                f"[schema:name='{item}'].schema:value")
    return None


def _dualize(paths, row):
    """Editable protocol parameters are DUAL-HOMED: the TAPP carries the protocol default and the
    detail carries the per-dataset value. For a dual-homed (Protocol, Analysis) row whose path is a
    recognised MethodDefinition DEFAULT, also emit the $Dataset counterpart (see
    _dataset_counterpart for the nesting mirror).

    Only paths that actually express a default are dualized — `…schema:defaultValue` or a direct
    `ada:{name}Default`. A nested path ending in `.schema:value`, `.schema:description` or
    `.schema:identifier` is the READ-ONLY shape or an identity field, so it is left alone rather
    than guessed at; that also keeps identity rows (schema:location, bios:computationalTool,
    schema:relatedLink) single-homed, which is correct — they are not per-analysis parameters.
    """
    if (row["P"], row["A"]) not in DUAL_HOMED:
        return paths
    if any(is_analyte_template(p) for p in paths):
        return paths            # analyte columns are never dual-homed — see is_analyte_template
    out = list(paths)
    if any(p.startswith("$Dataset.") for p in out):
        return out
    for p in paths:
        partner = _dataset_counterpart(p, row["item"])
        if partner:
            out.append(partner)
            break
    return out


_ISAMPLE = "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"


def keyed_path(row):
    """The canonical schema path(s) implied by the workbook's 'Keyed By' column, or None to fall
    through to content inference. `defines: X` rows are the template's list ROOT; the plain values
    are its per-member COLUMN family. Technique-scoped keys (channel — which needs a specific
    instrument component to host it — and the standard/combination keys) are left to inference or
    hand-authoring, so this only routes the technique-agnostic families."""
    kb = (row.get("kb") or "").strip().lower()
    it = row["item"]
    if not kb or kb == "(none)":
        return None
    routes = {
        "defines: analyte": ["$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes"],
        "analyte": ["$MethodDefinition.ada:analyteTemplate.ada:analyteColumns[]"],
        "defines: reported property": ["$MethodDefinition.ada:reportedProperties[]"],
        "reported property": [f"$MethodDefinition.schema:variableMeasured[schema:name='{it}'].schema:defaultValue",
                              f"$Dataset.schema:variableMeasured[schema:name='{it}'].schema:value"],
        "defines: sampling unit": ["$MethodDefinition.ada:samplingUnit"],
        "defines: sample": [f"$Dataset.prov:wasGeneratedBy.schema:object[@type='{_ISAMPLE}'].schema:name"],
        "sample": [f"$Dataset.prov:wasGeneratedBy.schema:object[@type='{_ISAMPLE}']"
                   f".schema:additionalProperty[schema:name='{it}'].schema:value"],
    }
    p = routes.get(kb)
    return (p, "keyed:" + kb.replace(" ", "-")) if p else None


def infer(row, lib, lib_norm, sidecar):
    """Return (paths_list, source) or (None, reason). paths_list is usually length 1, but 2 for a
    dual-homed editable protocol parameter (TAPP defaultValue + detail value)."""
    it, P, A, dt = row["item"], row["P"], row["A"], row["dt"]
    # 0. per-workbook override sidecar (hand-authored paths for rows content can't resolve)
    ov = sidecar.get(it)
    if ov:
        if ov.get("path"):
            return [ov["path"]], "sidecar"
        if ov.get("name"):  # a curated dataset-scalar name for an analysis-instance row
            return [f"$Dataset.ada:{ov['name']}"], "sidecar:name"
    # 0b. the workbook's Keyed By column routes template families to their canonical structure
    kp = keyed_path(row)
    if kp:
        return kp
    # 1. exact reference match (identity, instrument, params — path is exactly right for the same item)
    if it in lib:
        return _dualize(_aslist(lib[it]["path"]), row), "reuse"
    # 2. Procedure<->Protocol rename of a reference row (identity/shared rows carry no item name)
    alt = re.sub(r"\bProcedure\b", "Protocol", it)
    if alt != it and alt in lib:
        return _dualize(_aslist(lib[alt]["path"]), row), "reuse:proc->prot"
    n = _norm(it)
    if n in lib_norm:
        return _dualize(_aslist(lib_norm[n]["path"]), row), "reuse:norm"
    # 3. shared analysis-instance rows
    if n in SHARED:
        return [SHARED[n]], "shared"
    # 4. content inference
    name = b.camel(it)
    if not name:
        return None, "no-name"
    # The analysis-tier half hangs off prov:wasGeneratedBy, matching _dataset_counterpart: the value
    # records what THIS session used, which is what the provenance activity denotes. A bare
    # `$Dataset.schema:additionalProperty[…]` is not a grammar family — normalization does not
    # rescue it either — so inferring one produced rows no emitter could consume, silently dropping
    # the analysis-tier half of every dual-homed parameter.
    _ds_param = lambda i: f"$Dataset.prov:wasGeneratedBy.schema:additionalProperty[schema:name='{i}'].schema:value"
    if P == "Advanced":
        if (P, A) in DUAL_HOMED:  # dual-home: protocol default + per-dataset value
            return ([f"$MethodDefinition.schema:additionalProperty[schema:name='{it}'].schema:defaultValue",
                     _ds_param(it)], "infer:param-dual")
        # Read-Only / N/A analysis -> read-only protocol value in the TAPP only
        return [f"$MethodDefinition.schema:additionalProperty[schema:name='{it}'].schema:value"], "infer:param"
    if P == "Basic":
        # Matrix: Basic/Editable -> '{propertyName}Default' required in the TAPP, plus the
        # per-analysis value in the detail. Basic/Read-Only stays a single bare ada: property.
        if (P, A) in DUAL_HOMED:
            return ([f"$MethodDefinition.ada:{name}Default", _ds_param(it)],
                    "infer:direct-ada-dual")
        return [f"$MethodDefinition.ada:{name}"], "infer:direct-ada"
    # N/A protocol tier = analysis-instance we couldn't map -> flag
    return None, "analysis-instance (needs mapping)"


def _base(row):
    kb = (row.get("kb") or "").strip()
    return {"Metadata Item": row["item"], "Protocol Tier": row["P"],
            "Analysis Tier": row["A"], "Data Type": row["dt"],
            "Key by": "" if kb.lower() in ("", "(none)") else kb}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print("usage: bootstrap_schemapaths.py <workbook.xlsx> [--dry-run] [--reseed] [--reseed-all]\n"
              "  (default)     keep every existing row; infer only NEW workbook items\n"
              "  --reseed      re-infer everything EXCEPT Source=authored rows\n"
              "  --reseed-all  drop ALL existing rows and re-infer (destroys hand modelling)")
        return 1
    wb = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    # The reference library is optional: when it is absent, rows fall through to the Keyed By routing
    # and content inference (identity/instrument reuse is simply unavailable).
    lib = schemapath_io.load_spec(LIB_SPEC) if os.path.exists(LIB_SPEC) else {}
    lib_norm = {_norm(k): v for k, v in lib.items()}
    # legacy overrides sidecar is folded in on first seed (rows become Source=authored); optional
    sc_path = os.path.splitext(wb)[0] + ".overrides.json"
    sidecar = json.load(open(sc_path, encoding="utf-8")) if os.path.exists(sc_path) else {}
    rows = load_rows(wb)
    out_csv = schemapath_io.csv_path(wb)
    reseed = "--reseed" in sys.argv     # re-infer, but still keep Source=authored rows
    # By default PRESERVE every existing row verbatim (keyed by Metadata Item) so hand edits survive
    # a re-seed regardless of their Source; only NEW workbook items are inferred.
    #
    # --reseed re-infers everything EXCEPT rows marked Source=authored. It used to drop the file
    # wholesale, which silently destroyed hand-authored modelling: a reseed of SEM-FIBSEM flattened
    # 21 authored paths — the whole schema:instrument[...] tree and the ionMilling /
    # samplePreparation step nesting — into bare ada: properties. `authored` was only ever a
    # provenance label; nothing read it back, so the protection it implies did not exist. Now it
    # does, which is what makes --reseed usable for picking up generator improvements without
    # discarding hand modelling. Use --reseed-all for the old drop-everything behaviour.
    reseed_all = "--reseed-all" in sys.argv
    existing = schemapath_io.read(out_csv) if (os.path.exists(out_csv) and not reseed_all) else []
    if reseed:
        existing = [r for r in existing if (r.get("Source") or "").strip() == "authored"]
    keep = {}
    for r in existing:
        keep.setdefault((r.get("Metadata Item") or "").strip(), []).append(r)
    out_rows, flagged, sources = [], [], {}
    for row in rows:
        it = row["item"]
        if it in keep:                                  # keep the existing paths; refresh context columns
            for r in keep[it]:
                out_rows.append({**r, **_base(row)})
            sources["kept"] = sources.get("kept", 0) + 1
            continue
        paths, src = infer(row, lib, lib_norm, sidecar)
        canon = []
        if paths:
            try:
                canon = [norm.mechanical(norm.preclean(p)) for p in paths]
                for c in canon:
                    spp.parse(c)
            except spp.SchemaPathError as e:
                canon, src = [], f"parse-fail: {e}"
        if not canon:
            out_rows.append({**_base(row), "Schema Path": "", "Source": "flagged", "Notes": src})
            flagged.append((row["item"], row["P"], row["A"], src)); continue
        source = "authored" if src.startswith("sidecar") else "inferred"
        for c in canon:
            out_rows.append({**_base(row), "Schema Path": c, "Source": source, "Notes": ""})
        sources[source] = sources.get(source, 0) + 1
    # kept items no longer present in the workbook are retained but noted
    wb_items = {r["item"] for r in rows}
    for it, rs in keep.items():
        if it not in wb_items:
            for r in rs:
                out_rows.append({**r, "Notes": ((r.get("Notes") or "") + " [not in current workbook]").strip()})
    if not dry:
        schemapath_io.write(out_csv, out_rows)
    n_items = len({r["Metadata Item"] for r in out_rows if r.get("Schema Path")})
    print(f"{os.path.basename(wb)}: {n_items}/{len(rows)} placed, {len(flagged)} flagged"
          + ("" if dry else f"  -> {os.path.relpath(out_csv, ROOT)}"))
    print("  by source:", ", ".join(f"{k}={v}" for k, v in sorted(sources.items())))
    if flagged:
        print(f"\n  FLAGGED ({len(flagged)}) — author the schema path in the CSV (Source=authored):")
        for it, P, A, why in flagged:
            print(f"    [{P or '-':9}|{A or '-':9}] {it}   <- {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
