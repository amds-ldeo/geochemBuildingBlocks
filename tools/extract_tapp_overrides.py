"""Step 1 of the minimal-annotation path: EXTRACTOR.

Reads the current annotated docs workbooks and, for every row, computes the generator's
annotation-derived decisions (property/parameter NAME, analyte-column membership, and
special-role SKIP) using build_tapp's OWN functions. It then records only the RESIDUAL —
the part that a content-only generator could not derive from the plain content columns
(Protocol/Analysis tier, Data Type, Example/Allowed Content, mode columns) — into a
per-workbook sidecar `docs/<workbook>.overrides.json`.

Rows whose annotated decision already equals the content-only default (name = camelCase of
the Metadata Item, not an analyte column, not a special skip) produce NO entry. The printed
stats quantify how much annotation is genuinely irreducible.

Scope: the 5 tier-column TAPPs routed by build_tapp.route(). empaTAPP uses the separate
route_empa path (impl-heavy) and is handled separately.

    python tools/extract_tapp_overrides.py            # write sidecars + stats
    python tools/extract_tapp_overrides.py --dry-run  # stats only

Layer C can equivalently live as an `Overrides` worksheet in the workbook; the JSON sidecar
is used here because it is git-diffable and drives the verify harness. The loader in
verify_tapp_overrides.py reads whichever exists.
"""
import json
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import _tapp_lib as L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIER_TAPPS = ["laicpmsTAPP", "labxctTAPP", "temTAPP", "semImagingTAPP", "semFibsemTAPP"]
CENTRAL_ROLES_FILE = os.path.join(ROOT, "tools", "tapp_role_items.json")


def norm_item(s):
    return " ".join(str(s).split()).lower()


def load_central_roles():
    """Layer B: {normalized Metadata Item -> role}. Empty if not yet generated."""
    if os.path.exists(CENTRAL_ROLES_FILE):
        with open(CENTRAL_ROLES_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def preserved_file_keys(sidecar_path):
    """File-level directives are keyed by a leading underscore (e.g. `_tappDescription`), which no
    workbook Metadata Item ever produces. They are hand-authored, not derivable from the workbook,
    so carry them forward across a re-extract instead of clobbering them."""
    if not os.path.exists(sidecar_path):
        return {}
    with open(sidecar_path, encoding="utf-8") as f:
        existing = json.load(f)
    return {k: v for k, v in existing.items() if k.startswith("_")}


def load_rows(tapp):
    """Per-row view mirroring build_tapp.route()'s column detection exactly."""
    b.configure(tapp)
    ws = openpyxl.load_workbook(b.XLSX, data_only=True, read_only=True)["TAPP"]
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    hdr = rows[0]
    H = [b.norm(v).lower() for v in hdr]
    sp_col = next((i for i, v in enumerate(H) if v == "schema path"), None)
    impl_col = next((i for i, v in enumerate(H) if v.startswith("implementation note")), None)
    comment_col = next((i for i, v in enumerate(H) if v.startswith("comment")), None)
    mode_cols = []
    if comment_col is not None and sp_col is not None:
        for i in range(comment_col + 1, sp_col):
            vals = [b.norm(rr[i]).upper() for rr in rows[1:] if i < len(rr) and b.norm(rr[i])]
            if vals and all(v in ("Y", "N") for v in vals):
                mode_cols.append(i)
    out = []
    for r in rows[1:]:
        item = b.norm(r[0])
        if not item or re.match(r"^\d+\.\s", item):
            continue
        out.append({
            "item": item,
            "desc": b.norm(r[1]),
            "P": b.norm(r[2]),
            "A": b.norm(r[3]),
            "dt": b.norm(r[4]),
            "sp": b.norm(r[sp_col]) if sp_col is not None and sp_col < len(r) else "",
            "impl": b.norm(r[impl_col]) if impl_col is not None and impl_col < len(r) else "",
        })
    return out


def skip_role(sp):
    """Special-role skip a row's schema path signals (mirrors route() lines 456-462)."""
    if not sp:
        return None
    if (sp.startswith("$MethodDefinition") and "ada:" not in sp
            and "additionalProperty" not in sp and "schema:description" not in sp):
        return "inherited"
    if "analyteTemplate.ada:defaultAnalytes" in sp:
        return "analyteIdentifier"
    if "schema:description" in sp and "additionalProperty" not in sp:
        return "description"
    return None


def annotated_decision(row):
    """(name, analyte_cols|None, skipped_bool) as build_tapp.route() derives it from
    the schema-path / implementation-notes annotations."""
    item, sp, impl = row["item"], row["sp"], row["impl"]
    parsed = L.parse_impl(impl)
    name = b.field_name(item, sp, parsed)
    amap = b.CFG.get("analyte_map") or {}
    analyte = None
    if "analyteTemplate.ada:analyteColumns" in sp:
        # per-column dtype/readOnly are impl-driven and can differ from the content Data Type
        # column, so they are part of the residual (mirrors route() lines 437-446).
        cols = []
        for tr in parsed["tag_records"]:
            if tr["kind"] != "analytecolumn":
                continue
            ro = tr["readOnly"] if tr["readOnly"] is not None else (row["A"] == "Read-Only")
            cols.append({"name": tr["name"], "dtype": tr["dtype"] or row["dt"], "readOnly": ro})
        if not cols and item in amap:
            cols = [{"name": n, "dtype": row["dt"], "readOnly": (row["A"] == "Read-Only")}
                    for n in amap[item]]
        analyte = cols
    skipped = bool(skip_role(sp)) or (item in b.CFG["base_items"])
    return name, analyte, skipped


def content_default(row):
    """(name, analyte, skipped) a content-only generator gets with NO annotation."""
    item = row["item"]
    return b.camel(item), None, (item in b.CFG["base_items"])


def derive_override(row, central_roles=None):
    """The residual for one row: the fields where the annotated decision differs from the
    content-only default AND from Layer-B central config. Returns {} when the row is fully
    derivable from content + central roles."""
    central_roles = central_roles or {}
    item = row["item"]
    a_name, a_analyte, a_skip = annotated_decision(row)
    c_name, _, c_skip = content_default(row)
    skipped = a_skip or (norm_item(item) in central_roles)
    ov = {}
    # A name override matters only for a row that is actually routed as a property. On a
    # skipped/role row (inherited base field, schema:description, analyte identifier) the
    # annotated "name" is dead weight, so don't record it.
    if a_name != c_name and not skipped:
        ov["name"] = a_name
    if a_analyte is not None:
        ov["analyteColumn"] = a_analyte
    # a role override is only needed if content (base_items) AND Layer-B (central_roles)
    # both fail to reproduce the skip.
    if a_skip and not c_skip and norm_item(item) not in central_roles:
        ov["role"] = skip_role(row["sp"]) or "skip"
    return ov


def main():
    dry = "--dry-run" in sys.argv
    central = load_central_roles()
    grand = {"rows": 0, "override": 0, "name": 0, "analyte": 0, "role": 0}
    if central:
        print(f"(Layer B: {len(central)} central role/skip items loaded from tapp_role_items.json)\n")
    for tapp in TIER_TAPPS:
        rows = load_rows(tapp)
        overrides = {}
        counts = {"name": 0, "analyte": 0, "role": 0}
        for row in rows:
            ov = derive_override(row, central)
            if ov:
                overrides[row["item"]] = ov
                for k in counts:
                    if k in ov or (k == "analyte" and "analyteColumn" in ov):
                        counts[k] += 1
        docs_name = os.path.basename(b.XLSX)
        out = os.path.join(ROOT, "docs", os.path.splitext(docs_name)[0] + ".overrides.json")
        # carry forward hand-authored file-level `_`-keys (e.g. _tappDescription), first so they
        # stay at the top of the file; row-derived item entries follow. Kept out of `overrides`
        # so the printed stats still count only row-level overrides.
        merged = {**preserved_file_keys(out), **overrides}
        if not dry:
            with open(out, "w", encoding="utf-8") as f:
                json.dump(merged, f, indent=2, ensure_ascii=False)
                f.write("\n")
        n = len(rows)
        print(f"{tapp:16s} rows={n:3d}  need-override={len(overrides):3d} "
              f"({100*len(overrides)//max(n,1):2d}%)  "
              f"[name={counts['name']} analyteCol={counts['analyte']} role/skip={counts['role']}]"
              + ("" if dry else f"  -> {os.path.relpath(out, ROOT)}"))
        grand["rows"] += n
        grand["override"] += len(overrides)
        grand["name"] += counts["name"]
        grand["analyte"] += counts["analyte"]
        grand["role"] += counts["role"]
    print(f"\nTOTAL rows={grand['rows']}  need-override={grand['override']} "
          f"({100*grand['override']//max(grand['rows'],1)}%)  "
          f"[name={grand['name']} analyteCol={grand['analyte']} role/skip={grand['role']}]")
    print(f"=> {grand['rows']-grand['override']} of {grand['rows']} rows are fully content-derivable "
          f"(no annotation needed).")


if __name__ == "__main__":
    main()
