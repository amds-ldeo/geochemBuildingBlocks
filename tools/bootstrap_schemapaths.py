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
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
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
    ws = openpyxl.load_workbook(path, data_only=True, read_only=True)["TAPP"]
    rs = list(ws.iter_rows(values_only=True))
    hdr = [(str(c).strip() if c is not None else "") for c in rs[0]]
    def col(*pfx):
        return next((i for i, h in enumerate(hdr) for p in pfx if h.lower().startswith(p)), None)
    ci = {"P": col("procedure-level", "protocol-level", "procedure", "protocol"),
          "A": col("analysis-level", "analysis"), "dt": col("data type")}
    out = []
    for r in rs[1:]:
        it = (str(r[0]).strip() if r[0] else "")
        if not it or re.match(r"^\d+\.\s", it):
            continue
        g = lambda k: (str(r[ci[k]]).strip() if ci[k] is not None and ci[k] < len(r) and r[ci[k]] else "")
        out.append({"item": it, "P": g("P"), "A": g("A"), "dt": g("dt")})
    return out


_MD_DEFAULT_RE = re.compile(
    r"^\$MethodDefinition\.schema:additionalProperty\[schema:name='(.+?)'\]\.schema:defaultValue$")


def _dualize(paths, row):
    """Editable protocol parameters are DUAL-HOMED: the TAPP carries the schema:PropertyValueSpecification
    (schema:defaultValue = protocol default), and the detail carries a schema:PropertyValue
    (schema:value = the per-dataset editable value). So for a Protocol=Advanced ∧ Analysis=Editable/Advanced
    row whose path is a MethodDefinition additionalProperty defaultValue, also emit the $Dataset value
    counterpart. Applies to reused and content-inferred rows alike."""
    if row["P"] != "Advanced" or row["A"] not in ("Editable", "Advanced"):
        return paths
    out = list(paths)
    if any(p.startswith("$Dataset.schema:additionalProperty") for p in out):
        return out
    for p in paths:
        m = _MD_DEFAULT_RE.match(p)
        if m:
            out.append(f"$Dataset.schema:additionalProperty[schema:name='{m.group(1)}'].schema:value")
            break
    return out


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
    if P == "Advanced":
        if A in ("Editable", "Advanced"):  # dual-home: protocol default + per-dataset editable value
            return ([f"$MethodDefinition.schema:additionalProperty[schema:name='{it}'].schema:defaultValue",
                     f"$Dataset.schema:additionalProperty[schema:name='{it}'].schema:value"], "infer:param-dual")
        # Read-Only / N/A analysis -> read-only protocol value in the TAPP only
        return [f"$MethodDefinition.schema:additionalProperty[schema:name='{it}'].schema:value"], "infer:param"
    if P == "Basic":
        return [f"$MethodDefinition.ada:{name}"], "infer:direct-ada"
    # N/A protocol tier = analysis-instance we couldn't map -> flag
    return None, "analysis-instance (needs mapping)"


def _base(row):
    return {"Metadata Item": row["item"], "Protocol Tier": row["P"],
            "Analysis Tier": row["A"], "Data Type": row["dt"]}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print("usage: bootstrap_schemapaths.py <workbook.xlsx> [--dry-run]"); return 1
    wb = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    lib = schemapath_io.load_spec(LIB_SPEC)
    lib_norm = {_norm(k): v for k, v in lib.items()}
    # legacy overrides sidecar is folded in on first seed (rows become Source=authored); optional
    sc_path = os.path.splitext(wb)[0] + ".overrides.json"
    sidecar = json.load(open(sc_path, encoding="utf-8")) if os.path.exists(sc_path) else {}
    rows = load_rows(wb)
    out_csv = schemapath_io.csv_path(wb)
    # preserve any human-authored rows verbatim, keyed by Metadata Item
    existing = schemapath_io.read(out_csv) if os.path.exists(out_csv) else []
    authored = {}
    for r in existing:
        if (r.get("Source") or "").strip() == "authored":
            authored.setdefault((r.get("Metadata Item") or "").strip(), []).append(r)
    out_rows, flagged, sources = [], [], {}
    for row in rows:
        it = row["item"]
        if it in authored:                              # keep the human paths; refresh context columns
            for r in authored[it]:
                out_rows.append({**r, **_base(row)})
            sources["authored"] = sources.get("authored", 0) + 1
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
    # authored items no longer present in the workbook are kept but noted
    wb_items = {r["item"] for r in rows}
    for it, rs in authored.items():
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
