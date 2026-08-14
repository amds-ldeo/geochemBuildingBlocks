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
import tapp_source

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DELIV = tapp_source.current_delivery()
MODDIR = os.path.join(DELIV, "Claude Skills for TAPP", "modules")


_INDEX = {}


def _table(root, rel):
    """Resolve a manifest `tapp` entry to a real file, by BASENAME within the delivery.

    The manifest records per-technique paths (EPMA/EPMA_TAPP_v20.csv) but a delivery may lay the
    tables out differently — 2026-08-13 puts them all in a flat `Current TAPPs/`. Joining the
    literal relative path then resolves NOTHING: all sixteen tables are skipped, no field is
    compared, and the run reports a clean zero for work it never did. That is precisely the
    silent-skip this tool exists to catch, so resolution is by filename and anything still unfound
    is reported rather than passed over.
    """
    if root not in _INDEX:
        idx = {}
        for base, _, files in os.walk(root):
            for f in files:
                if f.endswith(".csv") and not f.endswith(".schemapaths.csv"):
                    idx.setdefault(f, os.path.join(base, f))
        _INDEX[root] = idx
    return _INDEX[root].get(os.path.basename(rel))


def blocks_of(name):
    """{block name -> {normalized field}} for a conditional module, else None.

    A conditional module does not contribute all its fields to every consumer: ReportingCore's six
    are grouped into five blocks, each with an `applies_when`, and a TAPP selects only the blocks
    that apply — `Procedural Blank Level` is absent from TEM because TEM has no analytical blank.
    Comparing the whole module against every consumer therefore reports 18 fields as missing when
    the block conditions say they should be, which is the module working rather than a defect.

    The mapping is DECLARED in the module's own .json, so it is read rather than inferred.
    """
    p = os.path.join(MODDIR, f"Module_{name}.json")
    if not os.path.exists(p):
        return None
    j = json.load(open(p, encoding="utf-8"))
    if not j.get("conditional"):
        return None
    return {b["name"]: {ms._norm(ms.rename(f)) for f in b.get("fields") or []}
            for b in j.get("blocks") or []}


def selected_fields(blocks, chosen):
    """The fields a consumer actually takes, given its `blocks` entry ('all' or a comma list)."""
    if blocks is None:
        return None                      # not conditional: every field applies
    if not chosen or str(chosen).strip() == "all":
        return set().union(*blocks.values()) if blocks else set()
    want = {c.strip() for c in str(chosen).split(",") if c.strip()}
    return set().union(*(v for k, v in blocks.items() if k in want)) if want else set()


def tiers(path):
    """{normalized item -> (P, A)}"""
    return {ms._norm(ms.rename(i)): (P, A) for i, P, A, _ in ms.source_items(path)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    # The manifest's `tapp` entries are paths INSIDE the delivery that shipped it, so they resolve
    # against that delivery — not the current one, whose layout may differ (2026-08-13 moved every
    # table into a flat `Current TAPPs/` folder). Modules still come from the current drop.
    manifest = tapp_source.manifest_path()
    if not manifest:
        raise SystemExit("no composed_tapps.json in any delivery — nothing declares what composes what")
    man_root = os.path.dirname(manifest)
    if os.path.basename(man_root) != os.path.basename(DELIV):
        print(f"note: {os.path.basename(DELIV)} ships no composed_tapps.json; using the one from "
              f"{os.path.basename(man_root)}, and resolving its table paths there.\n")
    man = json.load(open(manifest, encoding="utf-8"))
    consumers = collections.defaultdict(list)
    for entry in man.get("composed") or []:
        for m in entry.get("modules") or []:
            if m.get("name"):
                consumers[m["name"]].append((entry["tapp"], m.get("blocks")))

    names = a.module or sorted(consumers)
    grand = collections.Counter()
    missing = set()      # manifest tables absent from the delivery — reported, never passed over
    skipped = 0          # (field x table) pairs a conditional module's blocks legitimately exclude
    for name in names:
        src = os.path.join(MODDIR, f"Module_{name}.csv")
        if not os.path.exists(src):
            continue
        mod = {k: v for k, v in tiers(src).items() if v[0] or v[1]}   # owned rows only
        label = {k: i for i, _, _, _ in ms.source_items(src) for k in [ms._norm(ms.rename(i))]}
        findings = []
        blocks = blocks_of(name)
        for rel, chosen in consumers[name]:
            applies = selected_fields(blocks, chosen)
            p = _table(man_root, rel)
            if not p:
                missing.add(rel)
                continue
            tab = tiers(p)
            for k, (mP, mA) in mod.items():
                if applies is not None and k not in applies:
                    skipped += 1     # this consumer's blocks exclude the field; absence is correct
                    continue
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

    if missing:
        print(f"\n{len(missing)} table(s) the manifest names were NOT found in the delivery, so "
              f"their fields\nwent unchecked — the totals below do not cover them:")
        for x in sorted(missing):
            print(f"    {x}")
    if skipped:
        print(f"\n{skipped} (field x table) pair(s) not compared: a conditional module's blocks\n"
              f"exclude them from that consumer. See docs/REPORTINGCORE_BLOCKS.md.")
    print(f"\nTOTAL   TIGHTENS {grand['TIGHTENS']}   LOOSENS {grand['LOOSENS']}   "
          f"ABSENT {grand['ABSENT']}   ADDS {grand['ADDS']}")
    print("\nTIGHTENS breaks instances the table calls valid; LOOSENS silently drops enforcement;")
    print("ABSENT adds a property the table says is not on that side; ADDS gives a table a field it")
    print("never carried at all, which for a Basic field is a requirement it never stated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
