#!/usr/bin/env python3
"""Does composing a module change what its consuming tables actually require?

`allOf` intersects constraints and cannot relax them. So once a technique composes a module and
stops declaring the module's fields itself, the module's tiers govern — and wherever the module and
the table disagree about a field, the composed schema stops matching the table. Two directions, and
they fail differently:

  TIGHTENS  module says Basic, table does not
            allOf makes the field required for a technique whose own table calls it optional.
            Loud: instances the table considers valid now fail validation.

  LOOSENS   table says Basic, module does not
            the technique's own `required` goes away with its row, and the module does not replace
            it. Silent: nothing fails, the schema just stops enforcing something it used to.

  ABSENT    the module places the field on a side the table marks N/A
            composing adds a property the table says does not exist there.

Tier pairs are compared per side, since a field can agree on the procedure and disagree on the
analysis. Only the module's OWNED fields are checked — a tier-less module row is an example overlay
and carries no requirement.

    python tools/module_conflict_check.py
    python tools/module_conflict_check.py --module MCICPMS --verbose
"""
import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import migrate_sidecar as ms

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DELIV = os.path.join(ROOT, "TAPPS20260811")
MODDIR = os.path.join(DELIV, "Claude Skills for TAPP", "modules")


def tiers(path):
    """{normalized item -> (P, A)}"""
    return {ms._norm(ms.rename(i)): (P, A) for i, P, A, _ in ms.source_items(path)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    man = json.load(open(os.path.join(DELIV, "composed_tapps.json"), encoding="utf-8"))
    consumers = collections.defaultdict(list)
    for entry in man.get("composed") or []:
        for m in entry.get("modules") or []:
            if m.get("name"):
                consumers[m["name"]].append(entry["tapp"])

    names = a.module or sorted(consumers)
    grand = collections.Counter()
    for name in names:
        src = os.path.join(MODDIR, f"Module_{name}.csv")
        if not os.path.exists(src):
            continue
        mod = {k: v for k, v in tiers(src).items() if v[0] or v[1]}   # owned rows only
        label = {k: i for i, _, _, _ in ms.source_items(src) for k in [ms._norm(ms.rename(i))]}
        findings = []
        for rel in consumers[name]:
            p = os.path.join(DELIV, rel.replace("/", os.sep))
            if not os.path.exists(p):
                continue
            tab = tiers(p)
            for k, (mP, mA) in mod.items():
                if k not in tab:
                    # The manifest says this table composes the module, but the table does not carry
                    # the field. Composing therefore ADDS it — which for a Basic field means adding a
                    # requirement the table never stated. Not a disagreement (there is nothing to
                    # disagree with) but a change of scope, so it is reported rather than skipped:
                    # skipping it is how a check like this reports a comfortable zero.
                    findings.append(("ADDS", label[k], "both", f"{mP or '-'}/{mA or '-'}", "absent",
                                     os.path.basename(rel)))
                    grand["ADDS"] += 1
                    continue
                tP, tA = tab[k]
                for side, mt, tt in (("procedure", mP, tP), ("analysis", mA, tA)):
                    if mt == tt:
                        continue
                    if mt == "Basic" and tt != "Basic":
                        kind = "TIGHTENS"
                    elif tt == "Basic" and mt != "Basic":
                        kind = "LOOSENS"
                    elif mt and mt != "N/A" and tt == "N/A":
                        kind = "ABSENT"
                    else:
                        continue          # Advanced vs Editable etc: no requirement either way
                    findings.append((kind, label[k], side, mt, tt, os.path.basename(rel)))
                    grand[kind] += 1

        by_kind = collections.Counter(f[0] for f in findings)
        print(f"{name:<22s} {len(mod):2d} owned fields x {len(consumers[name]):2d} tables   "
              f"TIGHTENS {by_kind['TIGHTENS']:3d}  LOOSENS {by_kind['LOOSENS']:3d}  "
              f"ABSENT {by_kind['ABSENT']:3d}  ADDS {by_kind['ADDS']:3d}")
        if findings:
            # collapse: the same disagreement usually repeats across every consuming table
            grouped = collections.defaultdict(list)
            for kind, item, side, mt, tt, tab in findings:
                grouped[(kind, item, side, mt, tt)].append(tab)
            for (kind, item, side, mt, tt), tabs in sorted(grouped.items()):
                print(f"      [{kind}] {item} ({side}): module {mt or '-'} vs table {tt or '-'} "
                      f"— {len(tabs)} table(s)")
                if a.verbose:
                    for t in tabs:
                        print(f"                {t}")

    print(f"\nTOTAL   TIGHTENS {grand['TIGHTENS']}   LOOSENS {grand['LOOSENS']}   "
          f"ABSENT {grand['ABSENT']}   ADDS {grand['ADDS']}")
    print("\nTIGHTENS breaks instances the table calls valid; LOOSENS silently drops enforcement;")
    print("ABSENT adds a property the table says is not on that side; ADDS gives a table a field it")
    print("never carried at all, which for a Basic field is a requirement it never stated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
