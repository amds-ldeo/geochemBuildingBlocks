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
          "Scope", "Notes", "Key by"]
# `Key by` mirrors the workbook's `Keyed By` declaration, which routes a template-family row to its
# canonical Schema Path (bootstrap_schemapaths.keyed_path). It was missing from this list, so every
# write through here SILENTLY DROPPED it — which is why bootstrap builds the value and it never
# reaches disk, why 13 of 16 sidecars carry an empty column against source tables that declare 348
# values, and why backfill_keyby.py had to append the field line-by-line instead of writing rows.
# `Scope` is DERIVED, not authored: mark_shared_mappings.py computes it across ALL sidecars at once
# (shared / divergent / blank = technique-specific) so a reviewer can skip the boilerplate rows.
# It is listed here so write() preserves it, but bootstrap_schemapaths rebuilds rows from the
# workbook and will drop it — re-run mark_shared_mappings.py after a re-seed.


DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")


def csv_path(source_path):
    """<anywhere>/<wb>.{xlsx,csv} -> docs/<wb>.schemapaths.csv (docs/modules/ for a module).

    Sidecars live in docs/ because they are OURS. The TAPPS<date>/ folders are Ruolin's library,
    cached locally for reference and never modified — a sidecar written into one puts our
    hand-authored mapping inside somebody else's tree, which is exactly the boundary
    .github/CODEOWNERS draws. Resolving on the BASENAME lets a source sit wherever the delivery
    happens to put it (2026-08-13 moved every table into a flat `Current TAPPs/`) while its sidecar
    stays where it is curated.

    Module sidecars go to docs/modules/ so the technique folder does not mix the two: a module
    sidecar is shared by every TAPP that composes it, a technique sidecar belongs to one table.
    """
    stem = os.path.splitext(os.path.basename(source_path))[0]
    sub = "modules" if stem.startswith("Module_") else ""
    return os.path.join(DOCS, sub, stem + ".schemapaths.csv")


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
    # utf-8-SIG: these are opened and edited in Excel, which needs the BOM to read the file as UTF-8
    # — without it the superscripts and Greek in this content (²⁰⁶Pb/²³⁸U, δ⁵⁶Fe) come back as
    # cp1252 mojibake. Excel also writes the BOM on save, so matching it stops every tool write and
    # every hand edit from flipping the first three bytes back and forth in the diff.
    with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
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
