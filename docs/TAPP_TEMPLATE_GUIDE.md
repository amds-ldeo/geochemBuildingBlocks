# TAPP Template Workbook — User Guide

This guide explains how to fill in a TAPP template spreadsheet (xlsx) so the build pipeline can produce a complete technique-specific building-block stack: a TAPP definition, a per-dataset detail block, a dataset profile, and a dataset-entry xlsx template.

The canonical reference is **`docs/TAPP_EPMA_filled.xlsx`** — clone it as the starting point for any new technique (e.g. `docs/TAPP_XRD_filled.xlsx`, `docs/TAPP_LAICPMS_filled.xlsx`).

---

## Table of contents

1. [What is a TAPP?](#what-is-a-tapp)
2. [Workbook structure](#workbook-structure)
3. [Filling in the TAPP worksheet](#filling-in-the-tapp-worksheet)
4. [The implementation-notes column (the heart of the spec)](#the-implementation-notes-column-the-heart-of-the-spec)
5. [Where rows route to](#where-rows-route-to)
6. [Special CDIF-geochem schema path patterns](#special-cdif-geochem-schema-path-patterns)
7. [Vocabularies and term sets](#vocabularies-and-term-sets)
8. [Publication columns (worked-example data)](#publication-columns-worked-example-data)
9. [Running the build](#running-the-build)
10. [Sharing catalog entries with existing TAPPs](#sharing-catalog-entries-with-existing-tapps)
11. [End-to-end workflow checklist](#end-to-end-workflow-checklist)

---

## What is a TAPP?

A **Technique-Aligned Protocol Profile (TAPP)** is a registered specification of an analytical method — what kind of measurement is performed, what instruments / parameters / sample preparation steps are involved, and what variables are reported. The schema is `_sources/techniqueProtocols/tappDefinition/schema.yaml` (JSON-LD class `ada:TAPPDefinition`). A concrete TAPP profile (like `empaTAPP` for Electron Microprobe Analysis) extends `tappDefinition` via JSON Schema `allOf`, adding technique-specific top-level properties and constraining the `ada:methodParameters` and `ada:analyteTemplate.ada:analyteColumns` arrays to a curated catalog.

The template workbook is the **single source of truth** for what goes in the TAPP profile, the paired per-dataset detail block, and the corresponding dataset profile. Instead of authoring four building blocks by hand, you fill in one spreadsheet and the four `tools/build_*.py` scripts produce the rest.

---

## Workbook structure

The active worksheet is named **`TAPP`**. It uses fixed columns that the parser depends on — don't rename headers, reorder, or insert/remove columns from the structural region (A–J). Publication columns (K onward) are flexible: add as many as you have well-documented sources for, no upper bound.

```
A   Metadata Item                      ← human label (e.g. "Default Accelerating Voltage")
B   Description / Purpose              ← human description (used as schema:description)
C   Basic / Advanced                   ← informational, not consumed by the parser
D   Data Type                          ← e.g. "Numeric (kV)", "Text (free)", "Controlled list"
E   Example / Allowed Content          ← pipe-separated enum values for "Controlled list" rows
F   (last update / blank)              ← informational
G   Level of Completeness              ← informational
H   CDIF-geochem schema path           ← target path in the building-block schema
I   matchComment                       ← informational
J   implementation notes               ← THE TAGS — see the dedicated section below
K   P0                                 ← publication 0 — actual values from a real paper (or a synthetic comprehensive example)
L   P1                                 ← publication 1 …
…   …                                  … as many as you have data for
AA  P10plag                            ← (current EPMA template extends to col AA — 17 pubs)
```

> **Layout note (2026-04-29).** Earlier revisions of this template kept the structural columns (Level / CDIF path / matchComment / impl notes) in cols X–AA, after the pub block. They were moved to G–J so the pub block can grow rightward without disturbing anything else. If you have an older TAPP workbook in the X–AA layout, run `python tools/_reorder_tapp_columns.py <your.xlsx>` once to migrate it.

---

## Filling in the TAPP worksheet

Each row describes one fact or aspect of the protocol that needs to be specified in the implementation. The 'Metadata Item' is a user-friendly label for this protocol property, the 'Description/Purpose' provides an explanation of what it documents. The JSON  implementation of this protocol property is specified in the 'CDIF-geochem schema path' and 'implementation notes' columns. The implemenation notes have tags for protocol properties that are treated differently:

- A **property** of the TAPP definition (e.g. a default value baked into the protocol).
- A **parameter** (a knob — either a method-level constant or a per-dataset setting).
- An **analyteColumn** (a column in the per-element table of a TAPP analysis).

A single row may carry multiple tags — for example a row labelled "Default Accelerating Voltage" carries *both* a `property:` (the method-level constant) *and* a `parameter:` (the per-dataset value). Each tag has its own `readOnly` flag.

Rows that don't carry any of those three tags are processed by special-case logic in the example generator only (e.g. `Method Name`, `Method Author`, `Laboratory`, `Instrument Manufacturer`, `Instrument Model`).

---

## The implementation-notes column (the heart of the spec)

Column **J** carries one or more *tags* per row. Each tag declares what the row produces and supplies modifiers. The parser scans the cell text for these patterns:

### Tag syntax

```
property:    <name>
parameter:   <name>
analyteColumn: <name>
```

The `<name>` must start with an ASCII letter and may contain letters, digits, hyphens, and underscores. **No spaces, no special characters.** It will appear in URIs (e.g. `ada:parameter/empaTAPP/<name>`) so it must be URI-safe — see the `slugify_term_code` helper note in [Vocabularies](#vocabularies-and-term-sets) for what's allowed.

A row may carry **multiple tags**:

```
property:  acceleratingVoltageDefault
  dataType: schema:PropertyValue
  readOnly: true

parameter: acceleratingVoltage
  dataType: schema:PropertyValue
  readOnly: false
```

The parser slices the cell at each tag boundary, so each tag's modifier tokens (`dataType`, `readOnly`, `enum {…}`) are scoped to its own chunk — they don't leak across tags.

### Modifier tokens

Each tag may carry these modifiers in the lines that follow it (until the next tag or the end of the cell):

- `readOnly: true | false` — see [Where rows route to](#where-rows-route-to). Default is `false`.
- `dataType: <token>` — the JSON-Schema-flavoured type name. Common values: `schema:PropertyValue`, `string`, `number`, `integer`, `boolean`, `date`, `uri`. Unknown tokens fall back to `string`.
- `enum {A | B | C}` — pipe-separated allowed values. The first row that introduces a given enum becomes the canonical vocabulary file at `techniqueProtocols/vocab/<name>.json`; subsequent rows with the same enum reuse it.

### A complete row example

| Col | Value |
|---|---|
| A | Default Beam Diameter |
| B | Diameter of the focused or defocused electron beam in micrometers. |
| D | Numeric (μm) |
| H (cdif-path) | `$MethodDefinition.ada:beamDiameterDefault` |
| J (impl notes) | ```property: beamDiameterDefault```<br>```  readOnly: true```<br>```  dataType: schema:PropertyValue```<br>```parameter: beamDiameter```<br>```  dataType: schema:PropertyValue```<br>```  readOnly: false``` |
| L (P1) | `0 (focused)` |

What this produces:

- `ada:beamDiameterDefault` becomes a top-level property on the empaTAPP schema (string-typed).
- `parameterTemplates/beamDiameter.json` is **not** written (because `readOnly:false` routes parameters away from the TAPP); instead `parameterValues/beamDiameter.json` is written as a `schema:PropertyValue` with `schema:value: {type: number}` (numeric from "Numeric (μm)") and `schema:unitText: "μm"`.
- The detailEMPA `parametersConstraint.yaml` gets a `oneOf` branch for this PropertyValue.
- Each publication column with a value (e.g. P1's `"0 (focused)"`) appears as a `schema:additionalProperty` entry on the corresponding `exampledetailEMPA-P1.json` instance, with `schema:value` coerced to a number where possible (qualified strings like `"0 (focused)"` validate via the schema's `anyOf [number, string]` relaxation).

---

## Where rows route to

The build pipeline routes each row's outputs based on the tag kind and `readOnly` flag:

| Tag | readOnly | Output                                                                           | Lives at |
|---|---|---|---|
| `property:` | true | Top-level property block in TAPP `schema.yaml` (e.g. `ada:beamDiameterDefault`) | `_sources/techniqueProtocols/<TAPP>/schema.yaml` |
| `parameter:` | true | `PropertyValueSpecification` template (method-level constant)                   | `_sources/techniqueProtocols/parameterTemplates/<name>.json` (shared) |
| `parameter:` | false | `PropertyValue` instance (per-dataset reading)                                  | `_sources/techniqueProtocols/parameterValues/<name>.json` (shared) |
| `analyteColumn:` | (true) | `PropertyValueSpecification` per-element column template                        | `_sources/techniqueProtocols/analyteColumns/<name>.json` (shared) |
| any with `enum {…}` | — | `DefinedTermSet` vocabulary                                                     | `_sources/techniqueProtocols/vocab/<name>.json` (shared) |

**Special-case names handled in the property branch:**
- `property: analyteTemplate` — recognised but not emitted; refers to the inherited `ada:analyteTemplate` structure on `tappDefinition`.
- `property: description` — recognised but not emitted; refers to the inherited `schema:description`.

---

## Special CDIF-geochem schema path patterns

Most rows put text in column **H** (`CDIF-geochem schema path`) for documentation. One pattern is **machine-read** by the build pipeline:

```
$MethodDefinition.schema:instrument.schema:hasPart[].additionalType = '<XYZ>'
```

When a row has this pattern in column H, the build script generates a `oneOf` branch on the TAPP's `schema:instrument.schema:hasPart.items` constraint that pins `schema:additionalType` to contain `'<XYZ>'`. If the row's data type is `Controlled list`, column E's pipe-separated values become an enum constraint on `schema:name` for that branch.

For example (rows from the EMPA template):
- `Electron Source` → `additionalType: 'ElectronSource'` with `schema:name` enum from `Field Emission (FEG) | LaB6/CeB6 | Tungsten (W) | Other | Unknown`.
- `WDS Spectrometer Configuration` → `additionalType: 'wdsSpectrometer'` (no name enum).
- `EDS Detector Configuration` → `additionalType: 'edsDetector'` (no name enum).

The generator also emits a catch-all branch (`not: anyOf [contains: <known>...]`) so authors can attach instrument sub-components beyond the listed types, while still enforcing the name enum on known ones.

Other CDIF-geochem schema path values are informational — they document where the row's data should appear in the generated structure but don't drive code paths.

---

## Vocabularies and term sets

Any row whose impl-notes carries `enum {A | B | C}` introduces a controlled vocabulary. The first row to declare a given enum (compared by sorted set of values) names the vocabulary file. The vocabulary is emitted to `_sources/techniqueProtocols/vocab/<name>.json` as a `schema:DefinedTermSet` with one `schema:DefinedTerm` per value, where each term's `@id` is `ada:<slugify(termCode)>` (RFC 3986 unreserved characters only — special characters like `+`, `(`, ` ` are replaced with `_`).

Term values may include spaces, parentheses, slashes, etc.; the slugify helper handles URI-safety automatically. For example:
- `EPMA-WDS+EDS` → `@id: "ada:EPMA-WDS_EDS"`
- `PAP (Pouchou & Pichoir Full)` → `@id: "ada:PAP_Pouchou_Pichoir_Full"`
- `Si(Li)` → `@id: "ada:Si_Li"`

Each vocabulary file declares conformance to the upstream CDIF `definedTermSet` BB via `$schema`, and is used by reference (string URI in `schema:inDefinedTermSet`) from the parameter and analyteColumn catalog entries that share the term set.

---

## Publication columns (worked-example data) — your test suite

Columns **K onward** (P0, P1, …) carry actual values from real publications. Each column is one publication; the column header is something like `P3: Liu et al. 2016 (Tissint mineral chem., MAPS)`. The current EPMA template has 17 pubs running K..AA — add more by extending right past AA.

The pub-column label may carry a suffix to distinguish multiple subsets pulled from the same source paper (e.g. `P3sil` / `P3phos` for silicate vs. phosphate analyses in Liu et al. 2016, or `P10` / `P10plag` for whole-rock vs. plagioclase-only entries in Pang et al. 2016). The label is free-form; only the `^P\d` prefix is required for the parser to recognise the column.

> **This is how a new TAPP profile gets tested.** Each filled-in publication column becomes a *paired test instance* that the validator runs against the generated schemas. The publication examples are the primary mechanism for catching schema bugs, missing constraints, and impl-notes typos before the BB ships. **Fill in at least 2–3 publication columns with real data** before considering the TAPP profile ready.

For each non-empty publication column the build pipeline produces two paired files:

- `_sources/techniqueProtocols/<TAPP>/example<TAPP>-P{N}.json` — the TAPP definition populated with the protocol's method-level constants and `readOnly:true` parameters from column P{N}.
- `_sources/geochemProperties/detail<XXX>/exampledetail<XXX>-P{N}.json` — the per-dataset detail block populated with `readOnly:false` parameter values from the same column, pointing back at the empaTAPP example via `schema:measurementTechnique` `@id`.

`tools/validate_examples.py` validates every generated example against the schemas the build pipeline just wrote. If a publication column reveals a mismatch — a value the schema constraint rejects, a parameter the catalog hasn't defined yet, an enum entry that doesn't quite line up — validation fails on that example file. That's exactly the signal you want; it tells you what to fix in either the spreadsheet or the schema (whichever side is wrong).

### Per-publication generation behaviour

- **Empty cells skip the row.** A cell with no value contributes nothing — it doesn't produce an empty `additionalProperty` entry or a missing-required-field validation failure.
- **Enum mismatches skip the property.** When a publication's value for an enum-constrained property doesn't exactly match an enum entry (the publications often use free text where an enum is expected), the example generator skips that property rather than emit invalid data. So if validation passes but you don't see a property in an example, look at the spreadsheet's enum vs. what the publication actually wrote.
- **Numeric values can carry qualifiers.** Qualified strings like `"0 (focused)"` or `"1–2 μm focused; 5–10 μm defocused"` are accepted via the catalog's `schema:value: anyOf [number, string]` relaxation — fidelity to the source publication is preserved without loss to validation strictness for clean numeric data.
- **There's no fixed pub-column count.** Use as many as you have well-documented data for; leave the rest blank or trim them. Two or three diverse publications is usually enough to exercise most of a TAPP's surface area; the EPMA reference template ships with 17 to give the build pipeline a thorough workout.

### Picking publications for good coverage

Aim for diversity along the axes that vary across your TAPP:

- **Different value ranges** for parameters (e.g. low-vs-high accelerating voltage, focused-vs-defocused beam diameter) so range constraints get exercised.
- **Different enum picks** for controlled-list properties so each enum branch gets used in at least one example.
- **Different sample materials / instrument configurations** so any conditional constraints fire.

If you find yourself unable to fill in a parameter for any of the publications you have, that's often a sign the parameter row is too narrow / too wide and worth revisiting in the spreadsheet.

---

## Running the build

After filling in (or editing) the spreadsheet, run the four scripts. From the repo root:

```bash
# 1. Generate the TAPP BB + shared analyteColumns / parameterTemplates / vocab catalogs
python tools/build_TAPP_from_spreadsheet.py <TAPP_NAME> <docs/TAPP_<TECH>_filled.xlsx>

# 2. Generate the per-dataset detail BB (scaffolds <_sources/geochemProperties/detail<XXX>/>
#    on first run if it doesn't exist) plus parameterValues catalog + parametersConstraint.yaml
python tools/build_detail_BB.py <TAPP_NAME> <docs/TAPP_<TECH>_filled.xlsx>

# 3. (One-time per technique) Edit _sources/geochemProperties/detail<XXX>/schema.yaml
#    to fill in technique-specific ada:componentType enum (placeholder is "ada:TODO_ComponentType").

# 4. Scaffold the geochem profile (one-time per technique; idempotent thereafter)
python tools/build_profile_BB.py <TAPP_NAME>

# 5. Validate
python tools/resolve_schema.py --all
python tools/validate_examples.py

# 6. (Optional) Generate a dataset-entry xlsx template from a specific TAPP instance
python tools/build_dataset_template.py <path-to-TAPP-instance.json> <out.xlsx>
```

For empaTAPP all four scripts default to `empaTAPP` / `docs/TAPP_EPMA_filled.xlsx`, so a no-arg invocation regenerates the EPMA stack.

---

## Sharing catalog entries with existing TAPPs

The four catalog dirs at `techniqueProtocols/{analyteColumns,parameterTemplates,parameterValues,vocab}/` are **shared dictionary resources**. Multiple TAPP profiles can `$ref` the same files. The build pipeline enforces this via `share_or_write_catalog`:

- **File doesn't exist** → write normally (your TAPP originates the entry).
- **File exists, owned by your TAPP** (the existing `$id` contains `/<your-TAPP>/`) → overwrite freely. This is what happens when you edit the spreadsheet for an existing TAPP and re-run.
- **File exists, owned by another TAPP** (the existing `$id` contains a different TAPP name) → match content exactly to share, otherwise raise `ValueError`.

So if your new `xrdTAPP` defines `peakCountingTime` identically to the empaTAPP version, the regen reuses the empaTAPP-originated file (no new write, no error). If your `xrdTAPP` definition differs even slightly (e.g., different unit, different enum), the regen errors out with a "rename or reconcile" message — you'd then either rename the parameter in your spreadsheet (e.g. `xrdPeakCountingTime`) or update the spreadsheet to match the existing definition.

---

## End-to-end workflow checklist

For a brand-new technique TAPP (let's say XRD):

1. **Clone the template:** `cp docs/TAPP_EPMA_filled.xlsx docs/TAPP_XRD_filled.xlsx`.
2. **Fill in the TAPP worksheet:**
   - Rows for top-level properties (with `property:` impl-notes tag).
   - Rows for method parameters (with `parameter:` impl-notes tag, `readOnly` per case).
   - Rows for analyte columns (with `analyteColumn:` impl-notes tag).
   - Pipe-delimited enums in column E + `enum {…}` token in impl-notes for controlled lists.
   - The instrument hasPart pattern in column H for sub-components (electron source, detectors, …).
   - **Real publication data in at least 2–3 pub columns** (col K onward). This is the test suite for the new TAPP — every filled column becomes a paired example that the validator checks against the generated schemas. Aim for variety in parameter values and enum picks so coverage is broad. See [Publication columns](#publication-columns-worked-example-data--your-test-suite) for how to choose pubs.
3. **Run the TAPP build:** `python tools/build_TAPP_from_spreadsheet.py xrdTAPP docs/TAPP_XRD_filled.xlsx`.
   - Inspect the output: did all your parameters / analyteColumns / vocabs land in the right shared dirs? Any conflict errors with empaTAPP-originated entries?
4. **Run the detail build:** `python tools/build_detail_BB.py xrdTAPP docs/TAPP_XRD_filled.xlsx`. Then edit the scaffolded `_sources/geochemProperties/detailXRD/schema.yaml` to fill in the technique-specific `ada:componentType` enum.
5. **Run the profile scaffold:** `python tools/build_profile_BB.py xrdTAPP`. Edit `_sources/profiles/geochemProfiles/xrdProfile/schema.yaml` if you want extra profile-level constraints.
6. **Validate:** `python tools/resolve_schema.py --all && python tools/validate_examples.py`.
7. **Generate a dataset template** from one of the example TAPP instances: `python tools/build_dataset_template.py _sources/techniqueProtocols/xrdTAPP/exampleXRDTAPP-P1.json`.
8. **Iterate** by editing the spreadsheet and re-running steps 3–6. The reuse-detection means re-runs are idempotent for entries owned by your TAPP and surface conflicts for foreign-owned entries.

---

## Migrating an existing publication-style spreadsheet

If you're starting from an xlsx where the publication columns hold free-text descriptions instead of clean pipe-delimited data, the inference helper saves a lot of hand work:

```bash
# Preview only — writes a side xlsx + review JSON, does not touch the source
python tools/interpret_pub_analytes.py

# Apply — additionally rewrites rows 32 / 40 / 59 / 64 of the source xlsx
python tools/interpret_pub_analytes.py --apply
```

It scans every pub column and tries to recover the analyte axis from:

- **Row 32 (Target Element)** — used directly when explicitly populated (pipe- or comma-delim).
- **Row 59 (Primary Calibration Standard Name)** — entries like `"Anorthite (Si Kα, Al Kα, Ca Kα); Albite (Na Kα); …"` are parsed for `(element, x-ray line, standard)` triples.
- **Row 64 (Typical Detection Limit)** — `"Compound: value"` and `"<value> for X, Y, Z"` shapes are both recognised. Oxide formulas (`SiO2`, `Cr2O3`, `FeO`, `P2O5`, …) have the element extracted (the non-O part). The migrated cell preserves the full text segment per element (e.g. `"SiO2: 0.02 wt%"`, `"<0.03 wt% for TiO2"`) so context isn't lost.
- **Row 48 (Halogen Correction on Oxygen)** — mentions of `F`, `Cl`, `OH`, `CO2`, `S`, `H2O` get treated as additional analytes.

### Default mode (preview)

Writes side artifacts only — the source xlsx is untouched:

- `docs/TAPP_EPMA_filled-interp.xlsx` — a side workbook where each pub column is followed immediately by a `<pub>-interp` column carrying:
  - Row 32: inferred analyte list (pipe-delim).
  - Row 40: x-ray line per analyte.
  - Row 59: calibration standard per analyte.
  - Row 64: detection limit per analyte (full text segment).
  - All other rows: verbatim copy of the source pub.
- `build/interp-review/exampleempaTAPP-<pub>-interp.json` and `exampledetailEMPA-<pub>-interp.json` — paired JSON instances produced by feeding the interp column data through the regular `example_for_pub` builder.

Open both in Excel / your editor for side-by-side comparison. When satisfied, run with `--apply`.

### `--apply` mode (migrate)

Same outputs as default mode, **plus**: rewrites rows 32 / 40 / 59 / 64 of each pub column in `docs/TAPP_EPMA_filled.xlsx` to the pipe-delim format. The original publication-style free text is overwritten — git history preserves it. Excel must be closed on the source xlsx.

After `--apply`, the regular pipeline reproduces the same rich examples directly from the source — no interp loop or manual promotion needed:

```bash
python tools/build_TAPP_from_spreadsheet.py     # picks up the migrated rows
python tools/build_detail_BB.py                 # same
```

Pubs whose calibration-standard text is too generic (e.g. "natural and synthetic materials") to extract an element list produce an empty interp column and are skipped under `--apply` — their source rows stay as-is. Fill in their Target Element row manually before re-running the pipeline.

## Reference

- `tools/_tapp_lib.py` — the shared library; everything here is parameterized on `TAPP_NAME` set by `configure(tapp_name, xlsx)`.
- `_sources/techniqueProtocols/empaTAPP/` — the canonical example. Inspect alongside `docs/TAPP_EPMA_filled.xlsx` to see how spreadsheet rows map to BB outputs.
- `AGENTS.md` (repo root) — agent-oriented technical reference covering the wider building-block ecosystem, the catalog routing rules, and the deferred Phase D work in ada_metadata_forms.
