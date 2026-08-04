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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_SPEC = os.path.join(ROOT, "docs", "LA-Q_SF-ICPMS_TAPP_v3.schemapaths.json")

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


def infer(row, lib, lib_norm, sidecar):
    """Return (path, source) or (None, reason)."""
    it, P, A, dt = row["item"], row["P"], row["A"], row["dt"]
    # 0. per-workbook override sidecar (hand-authored paths for rows content can't resolve)
    ov = sidecar.get(it)
    if ov:
        if ov.get("path"):
            return ov["path"], "sidecar"
        if ov.get("name"):  # a curated dataset-scalar name for an analysis-instance row
            return f"$Dataset.ada:{ov['name']}", "sidecar:name"
    # 1. exact reference match (identity, instrument, params — path is exactly right for the same item)
    if it in lib:
        return lib[it]["path"], "reuse"
    # 2. Procedure<->Protocol rename of a reference row (identity/shared rows carry no item name)
    alt = re.sub(r"\bProcedure\b", "Protocol", it)
    if alt != it and alt in lib:
        return lib[alt]["path"], "reuse:proc->prot"
    n = _norm(it)
    if n in lib_norm:
        return lib_norm[n]["path"], "reuse:norm"
    # 3. shared analysis-instance rows
    if n in SHARED:
        return SHARED[n], "shared"
    # 4. content inference
    name = b.camel(it)
    if not name:
        return None, "no-name"
    if P == "Advanced":
        term = "defaultValue" if A in ("Editable", "Advanced") else "value"
        return f"$MethodDefinition.schema:additionalProperty[schema:name='{it}'].schema:{term}", "infer:param"
    if P == "Basic":
        return f"$MethodDefinition.ada:{name}", "infer:direct-ada"
    # N/A protocol tier = analysis-instance we couldn't map -> flag
    return None, "analysis-instance (needs mapping)"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print("usage: bootstrap_schemapaths.py <workbook.xlsx> [--dry-run]"); return 1
    wb = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    lib = json.load(open(LIB_SPEC, encoding="utf-8"))
    lib_norm = {_norm(k): v for k, v in lib.items()}
    sc_path = os.path.splitext(wb)[0] + ".overrides.json"
    sidecar = json.load(open(sc_path, encoding="utf-8")) if os.path.exists(sc_path) else {}
    rows = load_rows(wb)
    spec, flagged, sources = {}, [], {}
    for row in rows:
        path, src = infer(row, lib, lib_norm, sidecar)
        if path:
            canon = norm.mechanical(norm.preclean(path))
            try:
                spp.parse(canon)
                spec[row["item"]] = {"path": canon, "family": src}
                sources[src] = sources.get(src, 0) + 1
                continue
            except spp.SchemaPathError as e:
                src = f"parse-fail: {e}"
        flagged.append((row["item"], row["P"], row["A"], src))
    out = os.path.join(ROOT, "docs", os.path.splitext(os.path.basename(wb))[0] + ".schemapaths.json")
    if not dry:
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            json.dump(spec, f, indent=2, ensure_ascii=False); f.write("\n")
    print(f"{os.path.basename(wb)}: {len(spec)}/{len(rows)} inferred, {len(flagged)} flagged"
          + ("" if dry else f"  -> {os.path.relpath(out, ROOT)}"))
    print("  by source:", ", ".join(f"{k}={v}" for k, v in sorted(sources.items())))
    if flagged:
        print(f"\n  FLAGGED ({len(flagged)}) — author the schema path (mostly instrument/technique rows):")
        for it, P, A, why in flagged:
            print(f"    [{P or '-':9}|{A or '-':9}] {it}   <- {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
