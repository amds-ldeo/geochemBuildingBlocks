"""Layer B: derive the central, technique-independent role/skip list.

A role/skip row (inherited base field, protocol description, analyte identifier) is safe to
recognize CENTRALLY — by Metadata Item name, once, instead of per workbook — only when it is:
  1. recurring: appears as the same role in >= 2 workbooks, AND
  2. consistent: never assigned a different role, AND
  3. unambiguous: never ALSO routed as a real property in some other technique.

Rule 3 is the important safety net — e.g. `SE/BSE Detector Type` is an inherited skip in FIB-SEM
but a routed property in SEM Imaging, so it must stay per-workbook. Items failing any rule remain
in the per-workbook sidecar.

Writes `tools/tapp_role_items.json` ({normalized Metadata Item -> role}) consumed by the
extractor (to suppress redundant per-workbook role overrides) and the harness (to reconstruct
the skip). Non-destructive: no generator or workbook change.

    python tools/extract_central_roles.py
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
from extract_tapp_overrides import ROOT, TIER_TAPPS, load_rows, skip_role, norm_item

OUT = os.path.join(ROOT, "tools", "tapp_role_items.json")


def main():
    role_by_item = defaultdict(dict)   # norm item -> {tapp: role}
    routed_item = defaultdict(set)     # norm item -> {tapps routed as property}
    label = {}
    for tapp in TIER_TAPPS:
        rows = load_rows(tapp)
        R = b.route()
        routed = set()
        for bkt in ("tapp_prop", "method_param", "method_value", "detail_req", "detail_addl"):
            routed.update(norm_item(rec["item"]) for rec in R[bkt])
        for row in rows:
            n = norm_item(row["item"])
            label[n] = row["item"]
            r = skip_role(row["sp"])
            if r and row["item"] not in b.CFG["base_items"]:
                role_by_item[n][tapp] = r
            if n in routed:
                routed_item[n].add(tapp)

    central, kept = {}, 0
    for n, tr in role_by_item.items():
        roles = set(tr.values())
        if not routed_item[n] and len(tr) >= 2 and len(roles) == 1:
            central[n] = next(iter(roles))
        else:
            kept += len(tr)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(central, f, indent=2, ensure_ascii=False)
        f.write("\n")

    instances = sum(len(role_by_item[n]) for n in central)
    print(f"central role/skip items: {len(central)}  (absorb {instances} per-workbook override instances)")
    for n, r in sorted(central.items(), key=lambda kv: -len(role_by_item[kv[0]])):
        print(f"  [{r:12}] x{len(role_by_item[n])}  {label[n]}")
    print(f"remaining per-workbook role/skip instances: {kept}")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
