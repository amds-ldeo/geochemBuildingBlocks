# ADA Geochemistry Building Blocks -- Agent Guide

Technical reference for AI coding agents working in this repository.

## Repository purpose

Modular metadata schema components for the Astromat Data Archive (ADA), built on the OGC Building Blocks pattern. Defines JSON Schema building blocks for geochemistry analytical technique metadata, extending shared CDIF base schemas.

## Directory layout

Restructured 2026-06. `geochemProperties/`, `analysisSpecificDetails/`, `techniqueProtocols/`, and `profiles/` are **gone** — everything is now under `BaseSchema/`, `registry/`, or a per-technique directory.

```
_sources/
  BaseSchema/                17 shared BBs
    adaProduct/              base product profile (composes CDIF v1.1)
    tappDefinition/          base TAPP definition (was geochemProperties/methodDefinition)
    instrument/ laboratory/  extend the CDIF instrument / spatialExtent BBs
    image/ imageMap/ tabularData/ dataCube/ collection/ document/
    supDocImage/ otherFile/ files/            file-type BBs + the hasPart union
    structuredData/ spatialRegistration/ creativeWork/ stringArray/
  registry/                  shared catalogs (was techniqueProtocols/)
    analyteColumns/          registered BB (isTypeLibrary): PropertyValueSpecification $defs, 34
    parameterTemplates/      registered BB (isTypeLibrary): PropertyValueSpecification $defs, 178
    parameterValues/         registered BB (isTypeLibrary): PropertyValue $defs, 432
    vocab/                   catalog: DefinedTermSet files (by @id, not $ref), 162
  techniqueProfile/          43 technique dirs, each with up to four BBs
    <TECH>/tapp/             TAPP definition                    (11: EMPA, Geochron, LA-ICPMS,
                                                                 SEM, SEM-Composition, SEM-FIBSEM,
                                                                 SEM-Imaging, Solution-Q-ICPMS,
                                                                 Solution-SF-ICPMS, TEM, XCT)
    <TECH>/detail/           per-dataset analysis detail        (25)
    <TECH>/profile/          path-driven profile: adaProduct + detail + TAPP linkage (10)
    <TECH>/profile-ada/      generic profile: adaProduct + componentType only        (35)
build/                       Generated outputs (register.json, annotated schemas, RDF exports, reports)
tools/                       Python tooling for generation, validation, and auditing
docs/                        TAPP workbooks, schema-path sidecars, and the pipeline guides
.github/workflows/           CI: OGC postprocess, viewer deployment
```

**Directory names are not profile names.** `EMPA/profile-ada` publishes `adaEMPA`, `SEM/profile` publishes `adaSEMFull`, `XCT/profile` publishes `adaLabXCT`. The canonical name is the `schema:subjectOf.dcterms:conformsTo` const inside each schema — resolve it from there, never from the path.

**Detail blocks are not uniformly placed**, and placement does **not** track whether the technique is path-driven — SEM-FIBSEM and SEM-Imaging have path-driven profiles but hasPart-item details. Of the 25:

- **7 overlay the `schema:Dataset` root** (analyst contributor, session dates, sample, funding, per-analysis parameters), carrying no `ada:componentType`: Basemap, EMPA, Geochron, SEM, SEM-Composition, Solution-Q-ICPMS, Solution-SF-ICPMS.
- **18 pin `ada:componentType` and overlay a `schema:distribution.hasPart` item**: ARGT, DSC, EAIRMS, ICPOES, L2MS, LA-ICPMS, LAF, NanoIR, NanoSIMS, PSFD, QRIS, SEM-FIBSEM, SEM-Imaging, SLS, TEM, VNMIR, XCT, XRD.

Any consumer walking detail blocks must handle both. (`grep -L 'ada:componentType' _sources/techniqueProfile/*/detail/schema.yaml` re-derives the first list.)

## Building block structure

Each building block directory contains a standard set of files:

- `schema.yaml` -- canonical JSON Schema source (Draft 2020-12)
- `*Schema.json` -- generated JSON equivalent of schema.yaml (via `regenerate_schema_json.py`)
- `bblock.json` -- OGC Building Block metadata (name, status, version, tags)
- `description.md` -- human-readable documentation
- `examples.yaml` -- usage examples for validation testing
- `context.jsonld` -- JSON-LD context for RDF mapping
- `resolvedSchema.json` -- structured resolved schema (all $refs resolved into `$defs` + internal `$ref`, recursion-safe, ~88–90% smaller than the old fully-inlined form; via `resolve_schema.py`)
- `rules.shacl` -- SHACL validation shapes

Profiles additionally compose base schemas via `allOf` references.

## Schema composition pattern

- Property blocks define ADA-specific metadata elements
- `adaProduct` composes CDIF base schemas from mbb's `_sources/profiles/cdifProfile/` (CDIF **v1.1**) plus ADA overlays via `allOf`: `cdifCore`, `cdifDataDescription`, and `cdifProvenance` unconditionally; `cdifManifest` (was `cdifArchiveDistribution` in ≤1.0) behind an `if/then` that fires only when a `schema:distribution` item carries `schema:Collection` in `@type`, so monolithic single-file distributions aren't held to the manifest rules
- 35 `profile-ada` technique profiles extend `adaProduct` with technique-specific `ada:componentType` constraints; 10 `profile` technique profiles additionally compose the technique's `detail` block and narrow `prov:used` to its TAPP
- External schemas are referenced via full HTTP URLs to `cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/`
- Local schemas use relative `$ref` paths (e.g., `../stringArray/schema.yaml`)

## Key identifiers

- **Identifier prefix:** `ogch.` (e.g. `ogch.BaseSchema.instrument`, `ogch.techniqueProfile.EMPA.detail`, `ogch.BaseSchema.adaProduct`; was `ada.bbr.metadata.`)
- **Import source:** `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json`
- **Viewer URL:** `https://usgin.github.io/geochemBuildingBlocks/`

## componentType architecture (canonical mapping in spreadsheet)

`ada:componentType` is a **string** on each archive `hasPart` item (e.g. `"ada:EMPAImageMap"`). Two layers of constraint apply via `allOf`:

1. **Base BB enums** — each file-type building block (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares `ada:componentType: type: string, enum: [...]`. The enum is derived from the **Components worksheet** of `~/OneDrive/Documents/GithubC/amds-ldeo/metadata/ADA-AnalyticalMethodsAndAttributes.xlsx`. This enforces file-type ↔ componentType mapping (e.g. `ada:EMPAImageMap` only validates on parts whose `@type` includes `ada:imageMap`). Refresh via `python tools/apply_componentType_enums.py --refresh --xlsx <path>`; the cache `tools/componentType_enum_cache.json` is committed.
2. **Profile-level `anyOf`** — each technique profile's `schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref: '../adaProduct/schema.yaml#/$defs/universalComponentTypeBranch'` for universal componentTypes; (b) inline `properties.ada:componentType: {type: string, enum: [...]}` for technique-specific componentTypes that have no detail block; (c) `$ref: '../detail/schema.yaml'` for the 18 techniques whose detail block is the hasPart-item kind. Techniques whose detail overlays the dataset root instead (EMPA, SEM, Geochron, Solution-*, …) do not use branch (c) — their profile `$ref`s the detail at the top level. Detail schemas pin `ada:componentType` via `anyOf: [{const: "..."}]` consts and contribute detail-specific sibling properties (e.g. `ada:spectrometersUsed`, `ada:signalUsed`) on the same hasPart item — flat, not nested.

`files/schema.yaml`'s outer `anyOf` over base BBs has no permissive `schema:MediaObject` fallback — without it, parts whose `@type` doesn't match a specific BB will (correctly) fail validation.

## adaProduct → cdifProvActivity composition

`adaProduct.allOf` includes `cdifProvenance` (which $refs `cdifProvActivity`). adaProduct redefines `prov:wasGeneratedBy.items.properties` to add ADA-specific keys; via `allOf` merge the cdifProvActivity constraints still apply.

- `prov:used` is an **array**; each item is an `anyOf` of an `instrument` BB instance, an inline `tappDefinition` BB instance, or a bare `{"@id": …}` node reference to a TAPP defined elsewhere. Technique `profile` BBs narrow the TAPP branch to their own TAPP.
- `schema:location` (laboratory) — was renamed from `ada:laboratory`.
- `schema:object` (samples analyzed) — was renamed from `schema:mainEntity`. Requires upstream `cdifProvActivity.schema:object` to accept arrays of `schema:Thing` (extended in CDIF mbb to satisfy schema.org range = schema:Thing). `schema:result` extended symmetrically.

## Tools

### Schema generation and resolution

| Tool | Purpose |
|------|---------|
| `generate_profiles.py` | Generate technique profile building blocks from config data. Run with `--list` to see all profiles, or pass a profile name to regenerate one. |
| `regenerate_schema_json.py` | Sync `*Schema.json` from `schema.yaml` sources. Use `--dry-run` to preview. |
| `resolve_schema.py` | Resolve all `$ref` into a structured `resolvedSchema.json` (`$defs` + internal `$ref`, recursion-safe, ~88–90% smaller). The old fully-inlined output and separate `*StructuredSchema.json` files are gone; `--structured` is now a no-op. Supports `--all`, `--flatten-allof`. Canonical copy from metadataBuildingBlocks. |

### Validation and auditing

| Tool | Purpose |
|------|---------|
| `audit_building_blocks.py` | Comprehensive audit: file completeness, schema.yaml vs JSON consistency, resolvedSchema freshness (via the structured resolver), example validation, SHACL coverage. `isTypeLibrary` BBs (reusable `$defs` libraries with no instantiable root class, e.g. `stringArray`, `parameterValues`) are exempt from the standalone-example and SHACL-NodeShape requirements. Run with `--filter <name>` or `--json -o report.json`. |
| `audit_shacl_coverage.py` | Check SHACL rules cover all schema.yaml properties. Reports missing/extra shapes and severity mismatches. Use `--verbose` for detail. |
| `validate_examples.py` | Validate example JSON files against resolved schemas. Use `--filter` to target specific blocks. |
| `validate_instance.py` | Profile-aware validation of metadata instances. Auto-detects profile from `dcterms:conformsTo`. Supports `--dir`, `--profile`, `--termcode-fallback`. |
| `compare_schemas.py` | Detect drift between schema.yaml and *Schema.json (missing properties, type mismatches). |

### Data collection

| Tool | Purpose |
|------|---------|
| `download_ecl_methods.py` | Download analytical method Excel workbooks from the EarthChem Library. Reads the methods list from a Google Sheet, scrapes ECL record pages for filenames, and POSTs to `dl_multi.php` to download. Supports `--dry-run`, `--output-dir`, `--delay`. Skips already-downloaded files. |

### Build and deployment support

| Tool | Purpose |
|------|---------|
| `augment_register.py` | Add `resolvedSchema` URLs to `build/register.json`. Uses the `ogch.` identifier prefix. Run during CI before viewer deployment. |
| `generate_custom_report.py` | Generate HTML validation report with granular SHACL severity breakdown from OGC postprocess `report.json`. |
| `cors_server.py` | Local HTTP server with CORS headers for testing the viewer. Default port 8090. |

### Tool provenance

`resolve_schema.py` and `regenerate_schema_json.py` are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally. The audit, validation, and report tools were also sourced from that repository.

## CI/CD pipeline

1. **`process-bblocks.yml`** -- On push to main: runs OGC `bblocks-postprocess` validation, generates `build/register.json`, annotated schemas, RDF exports, `tests/report.json`
2. **`deploy-viewer.yml`** -- After postprocess completes: sets up Python 3.11, runs `augment_register.py` and `generate_custom_report.py`, generates viewer config, deploys to GitHub Pages

## Cross-repo relationships

- **metadataBuildingBlocks** (CDIF) -- upstream source for shared CDIF schemas and canonical tool copies. Schemas imported via OGC building blocks import mechanism.
- **CDIF profile release repos** (`profile-core`, `profile-discovery`, `profile-codelist`, `profile-datadescription`, `profile-manifest`, `profile-provenance`, `profile-conceptscheme`, `profile-datastructure`, under `C:\GithubC\CDIF\`) -- standalone repos with schemas, SHACL rules, and validated examples for each CDIF conformance class. Active revision work is on the `reviewRevision202606` branch. Conformance URIs (e.g. `https://w3id.org/cdif/core/1.1`) redirect to profile BBs in metadataBuildingBlocks via w3id.org.
- **ada_metadata_forms** (amds-ldeo) -- Django app that authors and validates ADA metadata, and hosts the TAPP (protocol) registry and editor. It reads this repo's `_sources/` directly: each profile's `resolvedSchema.json`, `BaseSchema/tappDefinition/resolvedSchema.json`, and the `registry/` catalogs (via its `sync_registries` command). Its `build.sh` shallow-clones `BaseSchema`, `techniqueProfile`, and `registry`. It builds a profile index by reading the `dcterms:conformsTo` const from each profile schema, and picks the path-driven vs generic variant per instance. Renaming a directory or changing a conformsTo const here will break it. The legacy monolithic `adaMetadata-SchemaOrgSchema-v3.json` is reference-only and no longer used for validation.
- **w3id.org/cdif** -- persistent identifier redirects for CDIF building blocks and conformance URIs. Maintained in smrgeoinfo/w3id.org fork.

## tappDefinition building block (v3)

Lives at `_sources/BaseSchema/tappDefinition/`. Was previously `geochemProperties/methodDefinition/`, then `techniqueProtocols/tappDefinition/`. Defines TAPP definitions as `prov:Plan` + `cdi:Activity` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol` — all five required in `@type` (`minItems: 5` plus a `contains` per term).

- **Identity:** `schema:name`, `schema:identifier`, `schema:version`, `schema:measurementTechnique`, `schema:object` (target materials), `schema:instrument`, `schema:location` (laboratory; was `ada:laboratory`), `bios:computationalTool`, `bios:reagent`, `schema:agent`
- **Workflow:** `schema:actionProcess` contains a `schema:HowTo` with ordered `cdi:Activity` + `schema:Action` steps (sample prep, calibration, acquisition, data processing, QC)
- **Parameters:** typed as `schema:PropertyValueSpecification` with `readonlyValue`, `valueRequired`, `defaultValue`, `minValue`/`maxValue`, `inDefinedTermSet`, `ada:fieldScope` (method/session/element). Step-level parameters use `schema:additionalProperty` (the `MethodParameter` shape); the old `StepParameter` $def and step-level `ada:methodParameters` were removed. TAPP-wide parameters are at top level.
- **Enumerations:** allowed-value lists are expressed via `schema:inDefinedTermSet`. Four shapes accepted: URI string, `{@id}` reference, `LabeledLink`, or an inline `{@type: schema:DefinedTermSet, schema:hasDefinedTerm: [{schema:DefinedTerm, schema:termCode}, ...]}`. The legacy `ada:enumeration` array property has been removed.
- **Analyte template:** `ada:analyteTemplate` with `PropertyValueSpecification`-typed columns and default analyte rows
- **Vocabularies:** Bioschemas (`bios:computationalTool`, `bios:reagent`, `bios:LabProcess`), DDI-CDI (`cdi:Activity`), DQV (`dqv:hasQualityMeasurement`), schema.org `DefinedTermSet`/`DefinedTerm`
- **Examples:** sibling `exampletappDefinition-<variant>.json` files: concord-glass-v1-0-6 (EPMA glass), nmnh-spinel-oxybar-v1 (EPMA spinel oxybarometry), uoc-laicpms-glass-v1 (LA-ICP-MS glass trace elements)
- **Used by:** `adaProduct.prov:wasGeneratedBy.items.prov:used.items.anyOf` accepts either an `instrument` BB instance or a `tappDefinition` BB instance.
- **Form integration:** Tab 3 of ada_metadata_forms consumes TAPP definitions from the registry

## TAPP / detail / profile pipeline (unified generator)

> **Read [docs/TAPP-schema-generation-workflow.md](docs/TAPP-schema-generation-workflow.md) first.** It is the current, authoritative end-to-end description of the pipeline (workbook → schema-path sidecar → BBs → resolved schemas → examples), with a flowchart and sections for the workbook author, the pipeline maintainer, and the form builder. The notes below cover implementation detail and the tier-matrix route that predates it.
>
> The current path for a new or regenerated TAPP is **schema-path driven**: `bootstrap_schemapaths.py` seeds `docs/<workbook>.schemapaths.csv` (the hand-authored source of truth — one row per Metadata Item → canonical schema path, with a `Source` column of `authored`/`inferred`/`flagged`), then `build_tapp.py` emits the registry catalogs and `build_pathdriven.py` emits `tapp/` and `detail/` from the sidecar. `schemapath_io.py` reads/writes the CSV, `normalize_schema_paths.py` canonicalises selector names, and the grammar is in `docs/SCHEMA_PATH_GRAMMAR.md`.

`tools/build_tapp.py <tapp_name>` is the **single generator** for all TAPPs (`empaTAPP`, `laicpmsTAPP`, `labxctTAPP`) — TAPP schema + shared catalogs (`analyteColumns`/`parameterTemplates`/`parameterValues`) + vocab + detail BB + per-publication examples. Routing follows the **canonical Protocol-Level × Analysis-Level matrix** (`docs/TierImplementationPatterns.xlsx`): Basic protocol → required top-level `ada:` property (`…Default` if editable at analysis); Advanced protocol → `schema:additionalProperty[]` `PropertyValueSpecification` (`…Default` + `readonlyValue:false` when dual-homed, bare + `readonly:true` if Read-Only); Analysis Basic → required detail property; Analysis Editable/Advanced → optional detail `PropertyValue`; Read-Only/N-A → absent from detail. Add a new TAPP by registering its knobs in `TAPP_CONFIGS`.

`tools/_tapp_lib.py` is now the **emitter/example library** (no longer a standalone router): `build_tapp.py` calls its `parameter_obj` / `additional_property_obj` / `analyte_column_obj` / `vocab_obj` emitters, `build_haspart_constraint`, the registry writers, `build_schema_yaml`, and the rich `example_for_pub` (now matrix-routed via a `route_map`). Its old impl-tag-kind routing (`_classify_rows`) is retired for current TAPPs.

- **empaTAPP** is the evolved-past prototype, **aligned to the matrix and folded into `build_tapp.py`** (2026-06). Its `schema path` column resolves the special roles (`$.ada:analyteTemplate.ada:analyteColumns…` → generated analyte column; `…ada:defaultAnalytes` → analyte identifier; `$.schema:description` → protocol description; `$MethodDefinition.*` non-`ada:` → inherited base field / instrument), tier columns drive home/cardinality, and impl-notes carry the base name + dtype/enum. `build_tapp.py` **generates** empa's analyteColumns from the workbook (reusing `_tapp_lib.analyte_column_obj`), keeps the hand-authored `detailEMPA` `allOf[0]` (`ada:spectrometersUsed`/`ada:signalUsed`/componentType) and only regenerates its `allOf[1]` `additionalProperty` constraint, and preserves param `enum`→vocab refs.
- Source workbook: `docs/TAPP_EPMA_filled-noInterp.xlsx` (annotated; guidance columns + impl-notes). `read_rows()` (`_detect_columns`) resolves columns by header name, handling both the empa layout (no `Literature Assessment` separator) and the newer Ruolin workbooks.

```
build_tapp.py            <tapp_name>                  # → TAPP BB + catalogs + vocab + detail + examples (empa/laicpms/labxct)
build_pathdriven.py      <tapp_name>                  # → techniqueProfile/<TECH>/{tapp,detail}/ from the schema-path sidecar
build_profile.py         <tapp_name>                  # → techniqueProfile/<TECH>/profile/
build_adaEMPA_examples.py [--pub P0]…                 # → EMPA profile-level dataset examples (empa only)
build_dataset_template.py <tapp-instance.json> [out]  # → xlsx columns from analyteColumns, rows from defaultAnalytes
```

The legacy `build_TAPP_from_spreadsheet.py` / `build_detail_BB.py` drivers now **delegate to `build_tapp.py` for `empaTAPP`** (matrix routing); they remain only for hypothetical impl-tag-style TAPPs. Templates + user-facing guide live in `docs/`:
- `docs/TAPP_EPMA_filled-noInterp.xlsx` — annotated canonical EMPA workbook.
- `docs/TierImplementationPatterns.xlsx` — the canonical tier matrix (authoritative routing rules).
- `docs/TAPP_TEMPLATE_GUIDE.md` — worksheet structure (column-by-column, schema-path role conventions, tier-matrix routing, hasPart additionalType pattern, vocab handling). *(Partially stale re: the retired impl-tag readOnly routing.)*

### Catalog routing rules

For each `parameter:<name>` impl-notes tag:
- `readOnly:true`  → a named `$def` in `registry/parameterTemplates/schema.yaml` (PropertyValueSpecification template), referenced by URI fragment (`…/parameterTemplates/schema.yaml#/$defs/<name>`) from the TAPP's `schema:additionalProperty`.
- `readOnly:false` → a named `$def` in `registry/parameterValues/schema.yaml` (PropertyValue instance shape with `@id == $id == schema:propertyID == ada:parameter/<TAPP>/<name>`), referenced by URI fragment from `techniqueProfile/<TECH>/detail/schema.yaml`'s inline `schema:additionalProperty` `anyOf` (the detail block now folds this constraint into its `allOf` directly — the old per-detail `parametersConstraint.yaml` file is gone).

For each `analyteColumn:<name>` impl-notes tag → a named `$def` in `registry/analyteColumns/schema.yaml`, referenced by URI fragment (`…/analyteColumns/schema.yaml#/$defs/<name>`) from the TAPP's `ada:analyteTemplate.ada:analyteColumns` `anyOf`. For each unique enum row → `registry/vocab/<name>.json` (vocab stays a plain catalog, referenced by JSON-LD `@id`, not `$ref`).

The parser fix on 2026-04-28 (`parse_impl()` → `tag_records`) extracts per-tag `readOnly` so a row carrying both a `property:` (readOnly:true) and a `parameter:` (readOnly:false) tag routes each correctly.

### Heuristic analyte-axis inference (publication migration helper)

`tools/interpret_pub_analytes.py` is a one-shot helper for migrating publication columns whose analyte axis isn't explicitly populated. It walks each pub column and tries to recover the analyte list from the cells that DO have signal:

- **Row 59 (Primary Calibration Standard Name)** — entries like `"Anorthite (Si Kα, Al Kα, Ca Kα); Albite (Na Kα); ..."` parsed for `(element, x-ray line, standard)` tuples.
- **Row 64 (Typical Detection Limit)** — both `"Compound: value"` and `"<value> for X, Y, Z"` shapes; oxide compounds (`SiO2`, `Cr2O3`, `FeO`) have the element extracted. Output preserves the full text segment per element (`"SiO2: 0.02 wt%"`, `"<0.03 wt% for TiO2"`) rather than reducing to bare numeric values.
- **Row 48 (Halogen Correction on Oxygen)** — `F`, `Cl`, `OH`, `CO2`, `S`, `H2O` mentions are treated as additional analytes.
- **Row 32 (Target Element)** — explicit pipe- or comma-delimited list takes precedence over inference when present.

Two modes:

- **Default (preview)** — writes `docs/TAPP_EPMA_filled-interp.xlsx` (side workbook with each `<pub>-interp` column inserted right after its source pub) and paired `build/interp-review/example<empaTAPP|detailEMPA>-<pub>-interp.json` review files. Source xlsx not touched.
- **`--apply` (migrate)** — additionally writes the inferred pipe-delim values back into rows 32 / 40 / 59 / 64 of each pub column in the source xlsx. Source must be closed in Excel. After migration, the regular pipeline (`build_TAPP_from_spreadsheet.py` etc.) reproduces the same rich examples directly from the source — the interp loop is no longer required for migrated pubs.

Pubs with no extractable signal (calibration text like "natural and synthetic materials") are skipped under either mode — fill in their Target Element row in the source xlsx manually before re-running the pipeline.

### Reuse-detection (`share_or_write_catalog`)

All catalog writes go through `share_or_write_catalog(path, data)` in `_tapp_lib.py`:
- File doesn't exist → write.
- Exists with `$id` containing `/<TAPP_NAME>/` → owned by this TAPP, overwrite freely (handles spreadsheet edits in the owner).
- Exists, foreign-owned (`$id` contains another TAPP name) → match content exactly to share, otherwise raise `ValueError` with rename-or-reconcile guidance.

This is why a future `xrdTAPP` regen can `$ref` empaTAPP-originated catalog entries that match its definitions but cannot silently overwrite them with different content.

## empaTAPP — first concrete TAPP profile (EMPA)

`_sources/techniqueProfile/EMPA/tapp/` extends `tappDefinition` (via `allOf`) with EPMA-specific top-level properties (`ada:beamMode`, `ada:beamDiameterDefault`, `ada:beamCurrentDefault`, `ada:matrixCorrectionMethod`, `ada:acceleratingVoltageDefault`) plus constraints on `schema:additionalProperty[]` and `ada:analyteTemplate.ada:analyteColumns[]` that reference the shared catalogs at `_sources/registry/`.

- **Spec source:** `docs/TAPP_EPMA_filled.xlsx`, sheet `TAPP`. Layout is A–F (item / desc / basic / dtype / example / Last update), G–J (Level / CDIF path / matchComment / impl notes), K..AA (pub columns P0..P10plag — extensible to the right). Each row's `implementation notes` column (column J) tags it as `property:`, `parameter:`, `analyteColumn:` (or combinations) and carries `readOnly`, `dataType`, optional `enum {...}`. Per-tag fields are scoped to the chunk of impl-notes between consecutive tags.
- **Generated by:** `tools/build_TAPP_from_spreadsheet.py` (TAPP side) + `tools/build_detail_BB.py` (detail side). Both read the same xlsx; the routing rule above splits parameters between empaTAPP and detailEMPA.
- **Currently emits:** 26 analyteColumns, 6 readOnly:true parameterTemplates, 4 readOnly:false parameterValues `$defs`, 12 vocabularies, the empaTAPP `schema.yaml`, the detailEMPA `schema:additionalProperty` constraint (inline in `detailEMPA/schema.yaml`), 17 paired `exampleempaTAPP-P{N}.json` + `exampledetailEMPA-P{N}.json` instances, plus the comprehensive hand-authored `exampleempaTAPP-all.json` + `exampledetailEMPA-all.json`. `tools/build_adaEMPA_examples.py` adds 17 paired `exampleadaEMPA-P{N}.json` profile-level Datasets (Phase D — see below).
- **Validation rule for per-pub examples:** when a publication's value for an enum-constrained property doesn't exactly match an enum entry, the generator skips that property in the example rather than emitting invalid data. For numeric `schema:value` fields, `additional_property_obj` uses `anyOf [<typed>, string]` so qualified publication-style values like `"0 (focused)"` validate alongside clean numbers.
- **Authoring gotchas:** `schema:inDefinedTermSet` is `{"@id": "..."}` (object), not a plain string; `schema:instrument.schema:identifier` is an array (per CDIF instrument BB); `schema:hasPart` items must contain `schema:Thing` in `@type`; `schema:location.schema:additionalType` must contain `nxs:BaseClass/NXsource`; `geosparql:asWKT` is `{@type:[geosparql:wktLiteral], @value:...}` and `geosparql:crs` is `{@id:...}`; `dqv:isMeasurementOf` is required on every quality measurement; `schema:relatedLink` items are `schema:CreativeWork`, not LinkRoles.

## detailEMPA — paired per-dataset detail block

`_sources/techniqueProfile/EMPA/detail/` carries per-dataset values that complement an empaTAPP TAPP definition. Schema is hand-authored (`ada:componentType` enum, `schema:measurementTechnique` requires an `@id` reference to a registered TAPP) plus an inline `schema:additionalProperty` constraint in its `allOf` whose `anyOf` branches `$ref` the `parameterValues` registry `$defs` (e.g. `../../../registry/parameterValues/schema.yaml#/$defs/acceleratingVoltage`). The separate `parametersConstraint.yaml` file was deleted.

- **Generated artifacts:** paired `exampledetailEMPA-P{N}.json` instances (one per pub), plus the structured `resolvedSchema.json` via `tools/resolve_schema.py`.
- **Hand-authored bits:** `schema.yaml`'s `ada:componentType` enum is user-maintained. The build_detail_BB.py scaffolder writes a stub on first run (when no `schema.yaml` exists yet) with placeholder `ada:TODO_ComponentType` consts.
- **measurementTechnique is `@id`-only.** A 2026-04-29 change dropped the inline empaTAPP-as-anyOf alternative — it inflated the resolved schema to 931 KB by inlining the entire TAPP. After the change it is <12 KB. Trade-off: detailEMPA records cannot self-contain a TAPP definition; consumers must resolve the TAPP by URI.

## Phase D (analytes → variableMeasured) — implemented

For each pub with paired (empaTAPP, detailEMPA) examples on disk, `tools/build_adaEMPA_examples.py` emits a profile-level `exampleadaEMPA-P{N}.json` whose `schema:variableMeasured[]` is derived from the empaTAPP's `ada:analyteTemplate.ada:defaultAnalytes[]`. Each defaultAnalyte becomes one `schema:PropertyValue + cdi:InstanceVariable` with per-analyte protocol detail (x-ray emission line, peak/background counting times, primary calibration standard) folded into `schema:description`. The detailEMPA fields land on a single tabular `schema:hasPart` that references the TAPP via `schema:measurementTechnique.@id`. Helper functions live in `_tapp_lib.py` (`variable_measured_from_default_analytes`, `profile_example_for_pub`, `build_profile_examples`) so any future TAPP can reuse the same pattern.

The same mapping is implemented on the consumer side in `ada_metadata_forms/core/services/tapp_service.py` (`variables_from_analyte_template`), generalised beyond EMPA: it resolves the analyte-identifier column rather than assuming a fixed key, and folds every other column of the row into `schema:description` using the column labels. If the analyte→variable mapping changes here, that is the counterpart to update.

## Common tasks

**Add a new TAPP-driven technique profile** — see docs/TAPP-schema-generation-workflow.md for the full walkthrough:
```bash
# 1. Author docs/<Technique>_TAPP_v#.xlsx (worksheet: TAPP).
#    See docs/TAPP_TEMPLATE_GUIDE.md for column conventions.
# 2. Seed the schema-path sidecar, then resolve any FLAGGED rows by hand
#    (blank Schema Path = the generator could not place the row):
python tools/bootstrap_schemapaths.py docs/<Technique>_TAPP_v#.xlsx
# 3. Registry catalogs + vocab:
python tools/build_tapp.py <tapp_name>
# 4. tapp/ and detail/ schemas from the sidecar:
python tools/build_pathdriven.py <tapp_name>
# 5. Edit _sources/techniqueProfile/<TECH>/detail/schema.yaml — fill in the
#    technique-specific ada:componentType enum (placeholder is "ada:TODO_ComponentType").
# 6. profile/ schema:
python tools/build_profile.py <tapp_name>
# 7. Validate everything:
python tools/resolve_schema.py --all
python tools/validate_examples.py
```

**Re-run after editing a workbook:**
```bash
python tools/bootstrap_schemapaths.py docs/<Technique>_TAPP_v#.xlsx  # authored rows preserved
python tools/build_tapp.py       <tapp_name>
python tools/build_pathdriven.py <tapp_name>
python tools/build_profile.py    <tapp_name>
python tools/resolve_schema.py --all
python tools/validate_examples.py
```

**Generate a dataset-entry xlsx from a TAPP instance:**
```bash
python tools/build_dataset_template.py _sources/techniqueProfile/EMPA/tapp/exampleempaTAPP-P0.json
# writes <input>-dataset-template.xlsx with one row per default analyte
```

**Add a new generic technique profile (no TAPP, profile-ada only):**
```bash
# Edit PROFILES dict in tools/generate_profiles.py, then:
python tools/generate_profiles.py adaNewTechnique
python tools/regenerate_schema_json.py
python tools/resolve_schema.py adaNewTechnique
```

**Audit all building blocks:**
```bash
python tools/audit_building_blocks.py _sources/
python tools/audit_shacl_coverage.py --verbose
python tools/validate_examples.py
```

**Check schema consistency after edits:**
```bash
python tools/compare_schemas.py
python tools/resolve_schema.py --all
```

**Run the viewer locally:**
```bash
python tools/cors_server.py 8090 build/
```
