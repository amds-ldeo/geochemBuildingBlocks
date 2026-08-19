#!/usr/bin/env python3
"""Carry a schema-path sidecar from one revision of a TAPP source table to the next.

A sidecar is hand-curated — 996 paths across nine techniques, many of them corrected by a human
after the bootstrap guessed wrong. When the library ships a new revision of a workbook, almost all
of that work still applies: the 2026-08 delivery renames Protocol to Procedure and adds rows, but it
does not re-plan where anything lives. Re-bootstrapping would throw the corrections away, so this
carries them across instead, and flags only what is genuinely new.

Three things move, and they must move together:

  Metadata Item   renamed by the delivery's own rules (Protocol -> Procedure, slash spacing)
  Schema Path     selector literals quote the item name, e.g.
                    schema:additionalProperty[schema:name='Cross Validation Protocol Requirement']
                  so a renamed item whose selector is left alone silently splits into two parameters
  tiers/Data Type refreshed from the new source (context columns, not authoritative)

Matching is tried exact, then by rename rule, then normalized (case- and punctuation-insensitive) —
the last because selectors and item names have drifted apart on punctuation already: the XCT item is
`Cross-Validation Protocol Requirement` while its own selector reads `Cross Validation …`.

`Source` and `Notes` are preserved verbatim: they record WHY a path is what it is, and a migration
is not new evidence. New rows arrive as `flagged` with a blank path, which is the existing signal
for "a human still has to place this".

    python tools/migrate_sidecar.py <tapp> --source <new table>          # report only
    python tools/migrate_sidecar.py <tapp> --source <new table> --write
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schemapath_io
import tapp_source


# Renames the mechanical rules cannot see, confirmed one at a time against the new table's own
# Description column. Without these the old item looks deleted and its authored paths are discarded,
# which is the one outcome this tool exists to prevent — so a rename is only listed here once the
# new row is confirmed to describe the same thing.
ALIASES = {
    # generalised: "International Geo Sample Number (IGSN) or other persistent identifier"
    "Sample IGSN": "Sample Persistent Identifier",
    # "Description of the measurement order within a session: how samples, blanks … are ordered"
    "Sample Sequence Design": "Analysis Sequence",
    # "Target thickness of the electron-transparent TEM lamella after final FIB polishing"
    "Target Foil Thickness": "Foil Thickness",
    # 2026-08-13 delivery MERGES two Lab-XCT resolution fields into one, confirmed by Stephen. Both
    # carried the same tiers (N/A/Advanced) and the same dataset-parameter shape, so the merge is
    # clean — but two olds mapping to one new is why migrate() de-duplicates: each old path names
    # its own item in a selector literal, and rewriting both produces the identical row twice.
    "Spatial Resolution": "Effective Spatial Resolution (PSF/MTF)",
    "Minimum Resolvable Feature Size": "Effective Spatial Resolution (PSF/MTF)",
    # Solution SF-ICP-MS: "Mass resolution mode assigned to each acquired mass" — same Basic/Read-Only
    # tiers and the same analyte-column placement as the old per-analyte field. Not to be confused
    # with `Mass Resolution Setting`, which is Basic/Editable and states the procedure's mode.
    "Mass Resolution per Analyte": "Mass Resolution Assignment",
}


# What a merged field is CALLED in the schema, where that should differ from the table's label. The
# Metadata Item must stay whatever the source table says or the row matches nothing, but the
# selector literal is the parameter's own name and need not carry a table's parenthetical. Both
# Lab-XCT resolution fields merge onto one parameter named `Spatial Resolution`; forcing the same
# literal for both is also what lets the two rewritten rows collapse into one.
SELECTOR_NAME = {
    "Effective Spatial Resolution (PSF/MTF)": "Spatial Resolution",
}


# The tier pairs the matrix says are dual-homed: a procedure default plus a per-analysis value.
# Mirrors bootstrap_schemapaths.DUAL_HOMED; kept here so callers that only need the rule do not
# have to import the bootstrapper.
DUAL_HOMED = {("Advanced", "Editable"), ("Advanced", "Advanced"), ("Advanced", "Basic"),
              ("Basic", "Editable")}


def _norm(s):
    """Case- and punctuation-insensitive form, for matching names that have drifted."""
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def rename(s):
    """The delivery's own two rules."""
    out = re.sub(r"\bProtocol\b", "Procedure", str(s))
    out = re.sub(r"\s*/\s*", " / ", out)
    return " ".join(out.split())


def source_items(path):
    """[(item, procedure tier, analysis tier, data type)] from a TAPP table, in file order."""
    rows = tapp_source.rows(path)
    hdr = [b.norm(v).lower() for v in rows[0]]

    def col(*pfx):
        return next((i for i, h in enumerate(hdr) for p in pfx if h.startswith(p)), None)

    ci = {"P": col("procedure-level", "protocol-level"), "A": col("analysis-level"),
          "dt": col("data type")}
    out = []
    for r in rows[1:]:
        it = b.norm(r[0]) if r and r[0] else ""
        if not it or re.match(r"^\d+\.\s", it):      # group header, e.g. "3. Instrument Setup"
            continue
        g = lambda k: (b.norm(r[ci[k]]) if ci[k] is not None and ci[k] < len(r) else "")
        out.append((it, g("P"), g("A"), g("dt")))
    return out


def build_rename_map(old_items, new_items):
    """{old item -> new item} plus the old items with no counterpart."""
    new_exact = {i: i for i in new_items}
    new_norm = {}
    for i in new_items:
        new_norm.setdefault(_norm(i), i)

    mapping, dropped = {}, []
    for o in old_items:
        if o in ALIASES and ALIASES[o] in new_exact:
            mapping[o] = ALIASES[o]
        elif o in new_exact:
            mapping[o] = o
        elif rename(o) in new_exact:
            mapping[o] = new_exact[rename(o)]
        elif _norm(rename(o)) in new_norm:
            mapping[o] = new_norm[_norm(rename(o))]
        elif _norm(o) in new_norm:
            mapping[o] = new_norm[_norm(o)]
        else:
            dropped.append(o)
    return mapping, dropped


def rewrite_selectors(path, by_norm):
    """Rewrite quoted selector literals that name a renamed item.

    Only literals matching an old item are touched — vocabulary tokens like
    schema:linkRelationship='coupledProtocol' are values in a controlled list, not item names, and
    renaming those would change the vocabulary rather than follow it.
    """
    if not path:
        return path, 0
    n = [0]

    def sub(m):
        lit = m.group(1)
        tgt = by_norm.get(_norm(lit))
        if tgt and tgt != lit:
            n[0] += 1
            return f"'{tgt}'"
        return m.group(0)

    return re.sub(r"'([^']*)'", sub, path), n[0]


def migrate(tapp, new_source, write=False, seed=None):
    b.configure(tapp)
    old_csv = schemapath_io.csv_path(b.XLSX)
    if seed:
        # Seed from ANOTHER technique's sidecar. A table new to the pipeline has no prior sidecar of
        # its own, but it is rarely new content: SEM v17 shares 70% of its fields with EPMA, Solution
        # MC 76% with Solution Q. Starting from the nearest curated neighbour carries those
        # placements instead of re-deriving them, and the report still shows every rename and every
        # row left flagged, so nothing arrives unexamined.
        b.configure(seed)
        old_csv = schemapath_io.csv_path(b.XLSX)
        b.configure(tapp)
        print(f"  seeded from {seed} ({os.path.basename(old_csv)})")
    new_csv = schemapath_io.csv_path(new_source)
    if not os.path.exists(old_csv):
        print(f"{tapp}: no existing sidecar at {os.path.relpath(old_csv)}")
        return 1

    rows = schemapath_io.read(old_csv)
    new_rows_src = source_items(new_source)
    new_meta = {i: (p, a, dt) for i, p, a, dt in new_rows_src}
    new_order = [i for i, _, _, _ in new_rows_src]

    old_items = []
    for r in rows:
        it = (r.get("Metadata Item") or "").strip()
        if it and it not in old_items:
            old_items.append(it)
    mapping, dropped = build_rename_map(old_items, new_order)

    # selector rewriting keys on the OLD name, normalized, so drifted punctuation still matches
    by_norm = {_norm(o): SELECTOR_NAME.get(mapping[o], mapping[o])
               for o in mapping if mapping[o] != o}

    renamed = {o: v for o, v in mapping.items() if v != o}
    sel_hits = 0
    out = []
    for r in rows:
        it = (r.get("Metadata Item") or "").strip()
        if it in dropped:
            continue
        new_it = mapping.get(it, it)
        row = dict(r)
        row["Metadata Item"] = new_it
        p, k = rewrite_selectors((r.get("Schema Path") or "").strip(), by_norm)
        row["Schema Path"] = p
        sel_hits += k
        if new_it in new_meta:                       # refresh the context columns
            tp, ta, tdt = new_meta[new_it]
            row["Protocol Tier"], row["Analysis Tier"], row["Data Type"] = tp, ta, tdt
        out.append(row)

    # Two items merging onto one produce the same row twice, once their selectors are rewritten to
    # the same literal. Collapse on (item, path); the first row keeps its Notes, which record why
    # the placement is what it is.
    seen, deduped = set(), []
    for r in out:
        key = (r["Metadata Item"], (r.get("Schema Path") or "").strip())
        if key[1] and key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    merged = len(out) - len(deduped)
    out = deduped

    carried = {r["Metadata Item"] for r in out}
    added = [i for i in new_order if i not in carried]
    for i in added:
        tp, ta, tdt = new_meta[i]
        out.append({"Metadata Item": i, "Protocol Tier": tp, "Analysis Tier": ta, "Data Type": tdt,
                    "Schema Path": "", "Source": "flagged", "Scope": "",
                    "Notes": "new in this revision (needs mapping)"})

    print(f"=== {tapp}: {os.path.basename(b.XLSX)} -> {os.path.basename(new_source)} ===")
    print(f"  rows        {len(rows)} -> {len(out)}")
    print(f"  items       {len(old_items)} carried, {len(renamed)} renamed, "
          f"{len(dropped)} dropped, {len(added)} new (flagged)")
    print(f"  selectors   {sel_hits} literal(s) rewritten")
    if merged:
        print(f"  merged      {merged} duplicate row(s) collapsed by an alias merge")
    for o in sorted(renamed):
        print(f"      rename  {o!r} -> {renamed[o]!r}")
    for d in dropped:
        # In seed mode these are simply fields the neighbour has and this technique does not, which
        # is expected and not a loss. Saying "confirm this item really is gone" there would send a
        # reviewer chasing thirteen phantom deletions, so the two cases are worded apart.
        if seed:
            print(f"      seed-only {d!r}  (not in this table; nothing carried)")
        else:
            print(f"      DROPPED {d!r}  (paths discarded — confirm this item really is gone)")
    for a in added:
        print(f"      new     {a!r}")

    if write:
        schemapath_io.write(new_csv, out)
        print(f"  wrote {os.path.relpath(new_csv)}")
    else:
        print("  (dry run — pass --write to create the sidecar)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tapp")
    ap.add_argument("--source", required=True, help="the new TAPP table (.csv or .xlsx)")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--seed", help="take the starting sidecar from this TAPP instead")
    a = ap.parse_args()
    if a.tapp not in b.TAPP_CONFIGS:
        raise SystemExit(f"unknown tapp {a.tapp!r}; one of {', '.join(sorted(b.TAPP_CONFIGS))}")
    if not os.path.exists(a.source):
        raise SystemExit(f"no such source table: {a.source}")
    return migrate(a.tapp, a.source, a.write, a.seed)


if __name__ == "__main__":
    sys.exit(main())
