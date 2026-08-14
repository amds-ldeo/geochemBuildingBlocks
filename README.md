# ADA Geochemistry Building Blocks

Modular metadata schema components for documenting geochemical analytical Methods and Datasets.  Built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

The scheme involves three components:

1. A Technique-Aligned protocol (TAPP) that defines a analytical procedure, including kinds of samples used, target analytes, instruments used, sample preparation, analysis workflow and data reduction.  In the TAPP definition, some of these might be specified as fixed, some might have default values, and some are expected to be specified a the individual session level.  The fixed properties are the necessary properties that define the TAPP.  There are also properties that apply as the analytical session (or 'analysis event') level, and properties that are specific to the description of individual analytes. The authoritative protocol definition is in an Excel workbook.  For discussion purposes, the label 'property' is used for properties in the TAPP that are fixed, and 'parameter' for properties that may be adjusted at the session level. Parameters may have default values specified in the TAPP definition.

2. A building block JSON schema specific to the protocol. This protocol definition object is registered in a protocol registry and accessible via its URI. The TAPP definition is referenced as a measurementTechnique in dataset metadata. 

3. A technique-specific 'detail' building block JSON schema that defines the parameters that may be assigned values at the individual dataset level. There is one detail block per technique, at `_sources/techniqueProfile/geochemProfile/<TECH>/detail/`, not a single 'details' file. The content of this schema is included in the schema for dataset instances to create a metadata schema for Datasets conforming to the profile. Session-level and per-analyte parameters are defined once in a registered parameter registry (`parameterValues`) and referenced from the detail blocks by URI, so a parameter can be reused across detail definitions; the references are resolved inline into the published resolved schema.

## Structure

`_sources/` has three top-level areas: the shared base schemas, the shared registries, and one directory per analytical technique.

```
_sources/
  BaseSchema/           17 shared BBs: adaProduct, tappDefinition, instrument,
                        laboratory, the file-type blocks (image, imageMap,
                        tabularData, dataCube, collection, document,
                        supDocImage, otherFile, files), structuredData,
                        spatialRegistration, creativeWork, stringArray
  registry/
    analyteColumns/     registered BB: PropertyValueSpecification $defs per analyte column (34)
    parameterTemplates/ registered BB: PropertyValueSpecification $defs, editable params (178)
    parameterValues/    registered BB: schema:PropertyValue $defs, fixed values (432)
    vocab/              catalog: schema:DefinedTermSet files, by @id not $ref (162)
  techniqueProfile/     one directory per technique (44), under two roots:
    geochemProfile/     the 12 TAPP-aware techniques
      <TECH>/tapp/      the TAPP definition for that technique      (12 techniques)
      <TECH>/detail/    per-dataset analysis-instance detail        (12 techniques)
      <TECH>/profile/   path-driven product profile: adaProduct +
                        detail + TAPP linkage                        (10 techniques)
      <TECH>/profile-ada/ generic product profile, written by the
                        TAPP tooling                                  (4 techniques)
    adaProfile/         the other 32 techniques, untouched by the TAPP work
      <TECH>/profile-ada/ generic product profile: adaProduct +
                        componentType constraints only               (31 techniques)
      <TECH>/detail/    instrument-detail stub                       (14 techniques)
```

**Profile directory names are not profile names.** `EMPA/profile-ada` publishes `adaEMPA`; `SEM/profile` publishes `adaSEMFull`. A profile's canonical name is the `schema:subjectOf.dcterms:conformsTo` const inside its own schema — read it from there rather than inferring from the path.

### BaseSchema

Shared building blocks. `adaProduct` is the base product profile, composing the **CDIF v1.1** profile schemas via `allOf`:

- `cdifCore` — core metadata properties
- `cdifDataDescription` — variableMeasured with DDI-CDI extensions, `@id` requirement
- `cdifProvenance` — `prov:wasGeneratedBy` provenance activities
- `cdifManifest` — archive distribution with `hasPart` component files (was `cdifArchiveDistribution` in CDIF ≤1.0). Applied **conditionally**: the `if/then` fires only when a `schema:distribution` item carries `schema:Collection` in its `@type`, so a monolithic single-file distribution isn't held to the manifest rules.
- ADA-specific overlays: technique types, instrument/lab/sample, `ada:componentType`

Two BBs extend CDIF core BBs:
- **instrument** — extends core CDIF instrument; requires `schema:additionalType` (at least one entry, e.g. `nxs:BaseClass/NXinstrument` or a technique term like `ada:EPMAInstrument`)
- **laboratory** — extends core CDIF spatialExtent (`schema:Place` with `nxs:BaseClass/NXsource` in `additionalType`)

`tappDefinition` is documented in [its own section below](#tapp-definition-building-block).

### registry (shared catalogs)

`analyteColumns`, `parameterTemplates`, and `parameterValues` are each a **registered type-library building block** (`bblock.json` with `isTypeLibrary: true`): every entry lives as a named `$def` in the catalog's `schema.yaml`, and TAPP / detail blocks reference them by URI fragment (`$ref: …/<catalog>/schema.yaml#/$defs/<name>`). Because they are registered, the OGC bblocks `annotate` step resolves those refs **locally via the register** and inlines them into `resolvedSchema.json`. This matters: a *loose* helper file (a plain `<name>.json` not inside a registered BB) is instead fetched from the published gh-pages URL, which 404s on moved or unpublished paths (`process-bblocks.yml` sets `skip-pages: true`, so gh-pages never auto-updates) — that fragility is why the catalogs were promoted to registered BBs. `vocab/` is the exception: it stays a plain catalog of `schema:DefinedTermSet` files because it is referenced only by JSON-LD `@id` (`schema:inDefinedTermSet`), never by `$ref`, so the `annotate` step never fetches it.

The catalogs are **shared dictionary resources** — multiple TAPPs `$ref` the same `$defs` when their definitions match. `share_or_write_catalog` lets a TAPP regen overwrite its own entries (matched by `$id` ownership) but errors out on a collision with an entry originated by a different TAPP, so a new TAPP either reuses identical catalog entries or surfaces a renaming requirement.

`parameterTemplates` holds editable parameters (a `PropertyValueSpecification` with a default the analyst may override); `parameterValues` holds fixed protocol values (a `schema:PropertyValue`). That split — specification vs value — is how read-only-ness is expressed; `ada:methodParameters` was retired repo-wide in favour of `schema:additionalProperty`.

### techniqueProfile/geochemProfile/&lt;TECH&gt;

Eleven techniques have a `tapp/`: EMPA, Geochron, LA-ICPMS, SEM, SEM-Composition, SEM-FIBSEM, SEM-Imaging, Solution-Q-ICPMS, Solution-SF-ICPMS, TEM, XCT. Ten of those also publish a path-driven `profile/` (all but TEM).

- **`tapp/`** — the protocol definition. Extends `tappDefinition` via `allOf` with technique-specific top-level `ada:` properties, `schema:additionalProperty[]` entries, and `ada:analyteTemplate.ada:analyteColumns` constraints referencing the registry catalogs.
- **`detail/`** — the per-dataset analysis instance. **Placement is not uniform, and does not track whether the technique is path-driven.** Seven overlay the `schema:Dataset` **root** (analyst contributor, session dates, sample, funding, per-analysis parameter values): Basemap, EMPA, Geochron, SEM, SEM-Composition, Solution-Q-ICPMS, Solution-SF-ICPMS. The other eighteen pin `ada:componentType` and overlay a `schema:distribution.hasPart` item: ARGT, DSC, EAIRMS, ICPOES, L2MS, LA-ICPMS, LAF, NanoIR, NanoSIMS, PSFD, QRIS, SEM-FIBSEM, SEM-Imaging, SLS, TEM, VNMIR, XCT, XRD. Consumers cannot assume one placement.
- **`profile/`** — path-driven product profile: `adaProduct` + the `detail` block + `prov:used` narrowed to that technique's TAPP + the technique's `ada:componentType` enum on `hasPart`.
- **`profile-ada/`** — the generic product profile: `adaProduct` + `ada:componentType` constraints only, no TAPP linkage or detail block.

A dataset instance selects between the two profile variants by how it references its protocol: a bare `{"@id": …}` node reference in `schema:measurementTechnique` targets the path-driven profile, an inline `schema:DefinedTerm` targets the generic one.

## componentType architecture

Each archive `hasPart` item carries an `ada:componentType` (a single string like `ada:EMPAImageMap`) that classifies the file. The architecture enforces a two-level constraint:

1. **File type ↔ componentType mapping** — each file-type building block (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of valid componentType values. The enum is derived from the **Components worksheet** of `amds-ldeo/metadata/ADA-AnalyticalMethodsAndAttributes.xlsx` (the canonical mapping). E.g. `ada:EMPAImageMap` is valid only on parts whose `@type` includes `ada:imageMap`.

2. **Profile-level constraint** — a technique profile's `schema:distribution.items.schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref` to `adaProduct/schema.yaml#/$defs/universalComponentTypeBranch` (factored once, used everywhere) for universal componentTypes; (b) inline string-enum for technique-specific componentTypes; (c) for techniques whose `detail/` block is the older *hasPart-item* kind (XRD, ARGT, DSC, …), a `$ref` to that detail schema, which pins `ada:componentType` to its technique consts and contributes detail-specific sibling properties (e.g. `ada:geometry`) flat on the hasPart item — not nested inside componentType. Path-driven profiles do **not** use branch (c): their detail block overlays the dataset root instead, and `hasPart` gets only branches (a) and (b).

### Refreshing the mapping

After editing the Components worksheet:

```
python tools/apply_componentType_enums.py --refresh \
    --xlsx ../../amds-ldeo/metadata/ADA-AnalyticalMethodsAndAttributes.xlsx
python tools/regenerate_schema_json.py
python tools/resolve_schema.py --all
python tools/validate_examples.py
```

The cached mapping at `tools/componentType_enum_cache.json` is committed so the apply step works on a fresh clone without spreadsheet access.

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism. All external references use absolute URLs (`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`).

## Viewer

Browse the building blocks at: https://usgin.github.io/geochemBuildingBlocks/

## Tools

### TAPP / detail / profile generation pipeline

**[docs/TAPP-schema-generation-workflow.md](docs/TAPP-schema-generation-workflow.md) is the authoritative walkthrough** — written for three audiences (workbook author, pipeline maintainer, form builder) with a flowchart of the whole path from spreadsheet to validated schema. Read it first; the summary here is orientation only.

One hand-authored TAPP workbook per technique (`docs/<Technique>_TAPP_v#.xlsx`, worksheet `TAPP`) drives everything downstream. Nothing generated should ever be hand-edited — fix the workbook or a tool and regenerate.

```
python tools/bootstrap_schemapaths.py  <XLSX>        # 1. seed/refresh the schema-path sidecar
python tools/build_tapp.py             <TAPP_NAME>   # 2. registry catalogs + vocab
python tools/build_pathdriven.py       <TAPP_NAME>   # 3. tapp/ + detail/ schemas from the sidecar
python tools/build_profile.py          <TAPP_NAME>   # 4. profile/ schema
python tools/resolve_schema.py --all                 # 5. resolvedSchema.json everywhere
python tools/validate_examples.py                    # 6. check the examples still pass
```

The **schema-path sidecar** `docs/<workbook>.schemapaths.csv` is the hand-authored source of truth for the workbook → schema mapping: one row per (Metadata Item → canonical schema path), with a `Source` column marking each path `authored` (human-set, preserved verbatim across re-seeds), `inferred` (bootstrap's best guess), or `flagged` (needs a path). A dual-homed editable parameter is two rows — its TAPP default and its detail value. `tools/schemapath_io.py` reads and writes it; `tools/normalize_schema_paths.py` canonicalises selector names; the grammar is specified in [docs/SCHEMA_PATH_GRAMMAR.md](docs/SCHEMA_PATH_GRAMMAR.md).

`tools/build_dataset_template.py <tapp-instance.json> [out.xlsx]` generates an xlsx data-entry template from a TAPP instance — columns from `analyteColumns`, one row per default analyte.

> **Superseded drivers.** `build_TAPP_from_spreadsheet.py` and `build_detail_BB.py` were the earlier impl-tag/tier-matrix route and now delegate to `build_tapp.py` for empa; `build_profile_BB.py` scaffolded the old `profiles/geochemProfiles/` layout. `generate_profiles.py` is **deprecated and refuses to run** without `--force-deprecated` — its template emits the old object-form `ada:componentType`. Use the path-driven pipeline above for new work.

### Publication migration helper

```
python tools/interpret_pub_analytes.py            # preview only (review files)
python tools/interpret_pub_analytes.py --apply    # also rewrite source xlsx
```

Reads publication columns whose analyte axis isn't explicitly populated and infers it from rows 48 / 59 / 64 (Halogen Correction / Primary Calibration Standard / Typical Detection Limit). Default-mode outputs:
- `docs/TAPP_EPMA_filled-interp.xlsx` — side workbook with each `<pub>-interp` column inserted right after its source pub for side-by-side review.
- `build/interp-review/example<empaTAPP|detailEMPA>-<pub>-interp.json` — paired review JSON instances built from the inferred data.

With `--apply`, additionally rewrites rows 32 / 40 / 59 / 64 of each inferred pub column in `docs/TAPP_EPMA_filled.xlsx` to the pipe-delim convention. After migration, the regular pipeline (`build_TAPP_from_spreadsheet.py` etc.) reproduces the same rich examples directly from the source — no interp loop needed.

Detection-limit values keep their full text per element (e.g. `"SiO2: 0.02 wt%"`, `"<0.03 wt% for TiO2"`) so context isn't lost in the migration.

### Schema generation and resolution

- `tools/resolve_schema.py` — resolve all `$ref` into a structured `resolvedSchema.json` (`$defs` + internal `$ref`, recursion-safe and ~88–90% smaller than the old fully-inlined form, which is no longer emitted; `--structured` is now a no-op). This is the file downstream validators read — the old `*StructuredSchema.json` output is gone.
- `tools/regenerate_schema_json.py` — generate *Schema.json from schema.yaml sources (YAML→JSON + ref rewrite)
- `tools/schema_path_parser.py` / `schema_path_emitter.py` / `normalize_schema_paths.py` / `bootstrap_schemapaths.py` / `schemapath_io.py` — the schema-path layer (parse a canonical path, materialise the nested structure it implies, canonicalise selector names, seed and read the CSV sidecar)
- `tools/generate_profiles.py` — **deprecated**, refuses to run without `--force-deprecated`; its template emits the old object-form `ada:componentType`. `--list` still works for reference.

### Validation and auditing

- `tools/audit_building_blocks.py` — comprehensive audit: file completeness, schema consistency, resolvedSchema freshness (via the structured resolver), SHACL coverage. `isTypeLibrary` BBs (reusable `$defs` libraries with no instantiable root class, e.g. `stringArray`, `parameterValues`) are exempt from the standalone-example and SHACL-NodeShape requirements.
- `tools/audit_shacl_coverage.py` — check SHACL rules cover all schema.yaml properties; reports missing/extra shapes
- `tools/validate_examples.py` — validate example JSON files against resolved schemas
- `tools/validate_instance.py` — profile-aware validation of ADA metadata instances
- `tools/compare_schemas.py` — detect drift between schema.yaml and *Schema.json

### Data collection

- `tools/download_ecl_methods.py` — download analytical method Excel workbooks from the EarthChem Library. Reads methods list from Google Sheets, downloads available workbooks. Supports `--dry-run`, `--output-dir`.

### Build and deployment support

- `tools/augment_register.py` — add resolvedSchema URLs to build/register.json for the viewer
- `tools/generate_custom_report.py` — generate HTML validation report with granular SHACL severity breakdown
- `tools/cors_server.py` — local HTTP server with CORS headers for testing the viewer

### Tool provenance

`resolve_schema.py` and `regenerate_schema_json.py` are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally — update the canonical copy and run `python tools/sync_resolve_schema.py --apply` from the metadataBuildingBlocks repo. The audit, validation, and report tools were also sourced from that repository.

## TAPP Definition Building Block

The `tappDefinition` building block at `_sources/BaseSchema/tappDefinition/` defines a registry-backed Technique-Aligned Protocol Profile (TAPP) definition schema (v3). Was previously `methodDefinition`. A TAPP definition is modeled as a `prov:Plan` + `cdi:Activity` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol` — all five required in `@type`.

### The TAPP is a plan, not an occurrence (PROV alignment)

A TAPP definition is a **plan** — a reusable procedure that *prescribes* an analysis — **not** the analysis event itself. This distinction resolves an apparent conflict with the CDIF provenance model and drives how instrument/tool/reagent fields are placed.

- **Two PROV roles.** The analysis *occurrence* is a `prov:Activity` — it lives in `adaProduct.prov:wasGeneratedBy[]` (a `prov:Activity` + `schema:Action`, following `cdifDataType/cdifProvActivity`). That activity references the TAPP as one of its **`prov:used`** entities (`prov:wasGeneratedBy[].prov:used[] → tappDefinition`, alongside the actual instrument). The TAPP is therefore a **used entity**, and in PROV terms a plan used by an activity is a **`prov:Plan`** — hence `prov:Plan` in the TAPP `@type`.
- **`cdi:Activity` vs `prov:Activity`.** `prov:Activity` (W3C PROV) is an *occurrence* — something that happened, that `prov:used`/`prov:generated` entities. `cdi:Activity` (DDI-CDI process model) is a *design-level description* of a process/method — reusable, plan-like. The TAPP uses `cdi:Activity` (which aligns with `prov:Plan`) because it describes a method; it is **not** typed `prov:Activity`. The TAPP's `schema:actionProcess` (a `schema:HowTo` of `cdi:Activity` steps) is likewise a plan.
- **Why instrument/tool/reagent are direct properties (no `prov:used` on the TAPP).** In `cdifProvActivity`, an *activity's* instruments are `prov:used[].schema:instrument` entities — because an occurrence uses them. A *plan* does not "use" entities in the provenance sense; it *specifies* resources. So the TAPP carries `schema:instrument`, `bios:computationalTool`, `bios:reagent` as **direct properties** (the Bioschemas `LabProtocol` convention), and has **no `prov:used`**. The `prov:used` pattern operates one level up, on the `prov:Activity` in `adaProduct.prov:wasGeneratedBy`, which uses both the actual instrument and this plan.
- **Division of labour.** The TAPP (plan) fixes the reproducible aspects of the method; the analysis instance leaves the rest to `adaProduct.prov:wasGeneratedBy` and the technique's `techniqueProfile/geochemProfile/<TECH>/detail/` block (per-dataset values). Instrument-type terms populate `schema:category` (a controlled-vocabulary `schema:DefinedTerm`); standalone-vs-`schema:hasPart` placement of sub-components is a per-field decision recorded in the schema-path sidecar.

### Structure

- **TAPP identity** (top level) — `schema:name`, `schema:identifier` (DOI), `schema:version`, `schema:measurementTechnique` (an **array** of `schema:DefinedTerm`), `schema:object` (target materials), `schema:instrument` (one instrument or an **array** when the method uses several, e.g. LA-ICP-MS = ablation system + ICP-MS), `schema:location` (laboratory/facility — was `ada:laboratory`), `bios:computationalTool`, `bios:reagent`, `schema:creator` (was `schema:agent`), `schema:relatedLink`, `schema:funding`
- **Standard workflow** (`schema:actionProcess`) — a `schema:HowTo` containing ordered `cdi:Activity` + `schema:Action` steps: sample preparation, calibration, data acquisition, data processing, quality control. Exactly one step must be named `Sample preparation` and carry `bios:LabProcess` in `schema:additionalType`.
- **Parameters** (`schema:additionalProperty`, top level and per step — **replaces the retired `ada:methodParameters`**) — each entry is one of two shapes:
  - `MethodParameter`, a `schema:PropertyValueSpecification` for an **editable** parameter: `schema:defaultValue` plus `schema:valueRequired`, `schema:minValue`/`maxValue`, `schema:inDefinedTermSet`, and the required `ada:fieldScope` (method/session/element) and `ada:dataType` (string/number/integer/boolean/date/uri)
  - `MethodParameterValue`, a `schema:PropertyValue` for a **read-only** parameter, carrying the fixed protocol value in `schema:value`
- **Analyte template** (`ada:analyteTemplate`) — per-element column definitions (also `PropertyValueSpecification`) and default analyte rows. Exactly one column must be the `AnalyteIdentifierColumn`: `schema:valueName` = `analyte`, pinned to `ada:dataType: string`, `readonlyValue: true`, `valueRequired: true`, `ada:tier: M`.
- **Quality metrics** (`dqv:hasQualityMeasurement`) — at method level and on workflow steps
- **`@context`** — required, and the `schema` / `ada` / `cdi` prefixes are pinned to exact values (note `schema` is `http://schema.org/`, not https)

### Examples

Example files use the sibling `example<bbName>-<variant>.json` pattern (validated by `tools/validate_examples.py`):

- `exampletappDefinition-concord-glass-v1-0-6.json` — EPMA WDS tephra glass (Concord University)
- `exampletappDefinition-nmnh-spinel-oxybar-v1.json` — EPMA WDS spinel oxybarometry (Smithsonian NMNH)
- `exampletappDefinition-uoc-laicpms-glass-v1.json` — LA-ICP-MS volcanic glass trace elements (University of Cologne)

Each technique's `tapp/`, `detail/`, and `profile/` directories carry their own paired publication-derived examples (`exampleempaTAPP-P0.json`, `exampledetailEMPA-P0.json`, `exampleempaProfile.json`, …).

### Vocabularies used

- [W3C PROV-O](https://www.w3.org/TR/prov-o/) — `prov:Plan` (the TAPP is a plan; the analysis occurrence is a `prov:Activity` in `adaProduct.prov:wasGeneratedBy` that references the plan via `prov:used`)
- [Bioschemas](https://bioschemas.org/) — `bios:LabProtocol`, `bios:LabProcess`, `bios:computationalTool`, `bios:reagent`
- [DDI-CDI](https://ddialliance.org/Specification/DDI-CDI/1.0/) — `cdi:Activity` (design-level process description) for workflow steps
- [W3C DQV](https://www.w3.org/TR/vocab-dqv/) — `dqv:hasQualityMeasurement` for quality metrics
- [schema.org](https://schema.org/) — `PropertyValueSpecification` for parameter definitions, `Action`/`HowTo`/`HowToStep` for workflow

## License

[Apache 2.0](LICENSE)
