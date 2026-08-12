"""Read/write the per-workbook schema-path sidecar CSV — the hand-authored source of truth for the
TAPP-workbook → JSON-schema mapping.

One CSV per workbook, `docs/<workbook>.schemapaths.csv`, one row per (Metadata Item → canonical
schema path). A dual-homed editable parameter is two rows (its TAPP defaultValue + its detail value);
a row the generator can't place is a FLAGGED row with a blank Schema Path.

Columns:
    Metadata Item | Protocol Tier | Analysis Tier | Data Type | Schema Path | Source | Notes
`Source` is provenance: `authored` (human-set — preserved verbatim across re-seeds), `inferred`
(bootstrap best guess), `flagged` (needs a path). Tier/Data-Type columns are refreshed from the
workbook on re-seed and are context only; the authoritative content is (item, Schema Path).

`load_spec()` collapses the CSV to the machine form the emitters consume: {item: {path: str|list}}.
"""
import csv
import os

FIELDS = ["Metadata Item", "Protocol Tier", "Analysis Tier", "Data Type", "Schema Path", "Source",
          "Scope", "Notes"]
# `Scope` is DERIVED, not authored: mark_shared_mappings.py computes it across ALL sidecars at once
# (shared / divergent / blank = technique-specific) so a reviewer can skip the boilerplate rows.
# It is listed here so write() preserves it, but bootstrap_schemapaths rebuilds rows from the
# workbook and will drop it — re-run mark_shared_mappings.py after a re-seed.


DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")


def csv_path(source_path):
    """<any dir>/<wb>.{xlsx,csv} -> docs/<wb>.schemapaths.csv.

    Sidecars always live in docs/, whatever directory the source table sits in. That used to be the
    same statement — every source was docs/<wb>.xlsx, so appending to the source path worked — but
    the 2026-08 delivery lands its CSVs under TAPPS20260811/<technique>/, and a sidecar written
    beside them would put our hand-authored mapping inside a vendor drop, where the next delivery
    would orphan it. Resolving on the BASENAME keeps sources wherever they are shipped and sidecars
    where they are curated. Repo-relative docs/ sources resolve exactly as before.
    """
    stem = os.path.splitext(os.path.basename(source_path))[0]
    return os.path.join(DOCS, stem + ".schemapaths.csv")


def read(csv_file):
    """List of row dicts (raw), in file order. Tolerates the cp1252 encoding Excel writes by default."""
    for enc in ("utf-8-sig", "cp1252"):
        try:
            with open(csv_file, newline="", encoding=enc) as f:
                return list(csv.DictReader(f))
        except UnicodeDecodeError:
            continue
    with open(csv_file, newline="", encoding="utf-8", errors="replace") as f:
        return list(csv.DictReader(f))


def write(csv_file, rows):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: (r.get(k, "") or "") for k in FIELDS})


def load_spec(csv_file):
    """{item: {"path": str | [str, ...], "family": source}} for the schema/example emitters.
    Rows with a blank Schema Path (flagged) are skipped; multiple pathed rows for one item collapse
    into a list (dual-home). Each path is CANONICALISED (so hand-authored shorthand like `$.` or
    unquoted/space-y selectors work) — the raw CSV keeps whatever the author typed."""
    import normalize_schema_paths as norm  # lazy: keeps schemapath_io light for non-emitter users
    spec = {}
    for r in read(csv_file):
        item = (r.get("Metadata Item") or "").strip()
        path = (r.get("Schema Path") or "").strip()
        if not item or not path:
            continue
        e = spec.setdefault(item, {"path": [], "family": (r.get("Source") or "")})
        e["path"].append(norm.mechanical(norm.preclean(path)))
    for e in spec.values():
        if len(e["path"]) == 1:
            e["path"] = e["path"][0]
    return spec
