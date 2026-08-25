# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repo is the ADA (Astromat Data Archive) building-blocks repo — modular JSON-Schema building blocks (OGC Building Blocks pattern) for geochemistry analytical-technique metadata, extending shared CDIF base schemas. It is one node in a larger CDIF-rooted ecosystem; sibling repos and the propagation pipeline are documented in auto-memory.

## Deeper references

- **`agents.md`** (lowercase — that is the tracked filename) — the authoritative, detailed agent guide (directory layout, every tool, the TAPP/detail/profile pipeline internals, the full componentType architecture). Read it when this file's summary isn't enough.
- **`README.md`** — human-facing overview; its generation-pipeline section is a good orientation.
- **`docs/TAPP-schema-generation-workflow.md`** — end-to-end walkthrough of workbook → validated schema.
- **`docs/SCHEMA_PATH_GRAMMAR.md`** — the canonical grammar for the schema-path sidecars.

## Commands

All tooling is `python tools/<name>.py`. There is **no** package manifest, build system, or pytest suite — the validation tools *are* the test suite.

Regenerate after any `_sources/**/schema.yaml` edit:

```
python tools/regenerate_schema_json.py        # *Schema.json from schema.yaml (--dry-run to preview)
python tools/resolve_schema.py --all          # resolvedSchema.json everywhere (downstream validators read this)
```

`resolve_schema.py` also accepts a single `<profile>` name or `--file <schema.yaml> -o <out>` to resolve just one — far faster than `--all` after a localized edit.

> **TAPP source = the `tapp/` git submodule** ([amds-ldeo/tapp](https://github.com/amds-ldeo/tapp)); `tools/tapp_source.py:current_delivery()` resolves to it. Clone with `--recursive` / `git submodule update --init` before regenerating. **Pending delivery migration:** the submodule is a *newer* drop than the committed schemas were built from — adopting it (repoint `TAPP_CONFIGS`, `migrate_sidecar`, regenerate) is deliberate work, see auto-memory `tapp_delivery_migration_202608`. (The earlier `resolve_schema.py --all` gh-pages blocker is now **lifted** — CDIF publishes `objectReference`; it runs clean.)

The migration tools, in run order: `python tools/intake_delivery.py <delivery>` (read-only first pass — what carries, what is renamed, what arrives **DROPPED** or flagged, what composing a module would change), then `python tools/migrate_sidecar.py <tapp> --source <table> [--seed <nearest tapp>] --write` (carries a sidecar onto a new revision; record non-mechanical renames in its `ALIASES` rather than losing the authored paths), then `python tools/fill_flagged.py --write`.

`TAPPS20260811/` and `TAPPS20260813/` at the repo root are **earlier inline drops**, not the source: `tapp_source.current_delivery()` prefers the `tapp/` submodule and only falls back to them. An unrecursed clone will silently build from the old drop — check the submodule is initialised before believing a regen.

Validate ("run the tests"):

```
python tools/validate_examples.py                 # validate all example*.json vs resolvedSchema.json
python tools/validate_examples.py --filter <name> # single BB/example — the "run one test" form
python tools/validate_instance.py --dir <dir>     # profile-aware (auto-detects dcterms:conformsTo)
python tools/audit_building_blocks.py             # completeness, schema<->JSON consistency, resolvedSchema freshness, SHACL
python tools/check_componentType.py               # componentType vocab/enum drift (annotation-only base layer, so JSON Schema alone misses it)
```

Local green ≠ CI green: `validate_examples.py` cannot catch the OGC bblocks-annotate dependency-resolution / dangling-`$ref` failures — only CI (or the branch `.github/workflows/validate-branch.yml`) runs the full postprocess.

Regenerate a TAPP technique from its source table (a CSV in the `tapp/` submodule's `Current TAPPs/`) — never hand-edit generated output; fix the table (upstream in amds-ldeo/tapp), the sidecar, or a tool and regenerate:

```
python tools/bootstrap_schemapaths.py <table.csv>  # 1. seed/refresh docs/<wb>.schemapaths.csv (hand-authored source of truth)
python tools/build_tapp.py         <TAPP_NAME>  # 2. registry catalogs + vocab
python tools/build_pathdriven.py   <TAPP_NAME>  # 3. tapp/ + detail/ schemas from the sidecar
python tools/build_profile.py      <TAPP_NAME>  # 4. profile/ schema
python tools/build_tapp_examples.py <TAPP_NAME> # 5. publication-derived example*.json
python tools/resolve_schema.py --all            # 6. resolve
python tools/validate_examples.py               # 7. verify
```

**Step 5 is easy to skip and its omission is silent.** The publication examples (`example<TAPP>-<Pub>.json`, one per column after `Literature Assessment`) are NOT rebuilt by `build_pathdriven`, so a sidecar change moves the schema while they keep the placement they were last generated with. Nothing complains until `validate_examples` runs, and the failure reads as a schema bug rather than a stale artifact — moving `Detection Limit` off `analyteColumns[]` produced 125 such failures that regeneration alone cleared. `build_tapp_examples` is not a second generator: it reads the workbook's publication columns for CONTENT and calls `schema_path_example_emitter.build_example(tapp, values=...)` -- the same emitter that writes the `-P0` files -- for PLACEMENT.

## Source vs generated

- **Hand-authored:** everything under `_sources/` (`schema.yaml`, `rules.shacl`, `example*.json`, etc.)
- **Generated:** everything under `build/` (resolved schemas, OAS3 downcompiles, JSONLD, register, tests).

When fixing a bug that surfaces in a generated artifact, **trace to the source generator/template/schema and regenerate** — never patch the build output directly. This is a standing rule across this ecosystem; it has its own feedback memory.

Two standing gotchas that bite spot regenerations:

- **The shared registries reformat wholesale on regen.** After regenerating one technique, `git checkout` `_sources/registry/parameterValues/schema.yaml` and `_sources/registry/parameterTemplates/schema.yaml` if you only meant to touch that technique — otherwise the diff carries unrelated reflow.
- **`tools/resolve_schema.py` and `tools/regenerate_schema_json.py` are synced copies** from `metadataBuildingBlocks/tools/`. Don't edit them here — fix the canonical copy upstream and re-sync (`python tools/sync_resolve_schema.py --apply` from that repo).

## Composition modules

`_sources/BaseSchema/modules/<name>/` (`core`, `targetSelection`, `analyte`, `aggregation`, `blank`, `calibrationFactor`, `laserAblation`, `mcIcpms`, `solutionIntroduction`, `geochronology`, `uPb`; plus `group1` and `reportingCore`, which the current manifest composes into nothing) factors fields shared across techniques into module building blocks. Each exposes up to two `$defs`, split by path root: **`ProcedureIdentification`** (from the module's `$MethodDefinition` paths, composed into `tapp/`) and **`AnalysisIdentification`** (from its `$Dataset` paths, composed into `detail/`); `reportingCore` is conditional and exposes one `$def` per block per side (see `docs/REPORTINGCORE_BLOCKS.md`). All 16 techniques in `tapp/composed_tapps.json` compose modules today; membership is matched on the table's **filename**.

A row covered by a module is **dropped from the technique's own overlay** — otherwise the shared field is defined twice and the technique's copy silently wins on any divergence. `tools/module_composition.py` makes that call, and only when the module `$def` demonstrably provides the field (module has it, the field has a placement in the module sidecar, and the `$def` exists).

```
python tools/seed_module_sidecars.py --write   # fill docs/modules/Module_*.schemapaths.csv from technique consensus
python tools/module_conflict_check.py          # preview: TIGHTENS / LOOSENS / ABSENT / ADDS for consumers
python tools/build_module_bb.py --write        # module BB from its CSV (tapp/ submodule) + sidecar
python tools/draft_module.py --measure         # draft candidate modules, measure what they'd save
```

A module with no placed root fields still emits a BB when it publishes parameters — `blank` is the
only one left in that state (`calibrationFactor` was too, until its keyed `variableMeasured` rows
were added). What it must never do is emit an *empty* root `$def`,
which would wrongly assert that a conforming procedure carries nothing.

### Module parameters: shape and identity

A module publishes parameters as `Param_<Side>_<name>` `$defs`. **Do not restate the parameter
shape there** — `build_module_bb.emit_parameter_defs()` delegates to the two canonical emitters in
`build_tapp.py`, chosen by side:

| side | emitter | `@type` | carries |
|---|---|---|---|
| `Procedure` (`$MethodDefinition` paths) | `param_template_def` | `schema:PropertyValueSpecification` | `schema:valueName`, `ada:dataType`, `ada:fieldScope`, `schema:readonlyValue`, `ada:tier` |
| `Analysis` (`$Dataset` paths) | `param_value_def` | `schema:PropertyValue` | `schema:propertyID`, `schema:value` |

Both add **`schema:unitText` whenever the Data Type column names a unit** — required on the value
side, a `const` on the template side. A hand-rolled variant that emitted a hybrid of the two made
every module parameter differ structurally from the technique parameter it duplicates: 181 apparent
conflicts that were one defect. `python tools/module_conflict_check.py --parameters` is the check.

**Identity.** A technique mints `ada:parameter/<TAPP>/<name>`, so one logical parameter exists once
per consuming TAPP. A module-owned parameter instead gets a single identity,
`ada:parameter/module/<Module>/<name>` — deliberately, so the shared parameter is one thing. The
module and technique `$defs` should therefore differ **only** in that `@id`.

> **Module `$ref` depth (`e3a3968d`).** Modules sit at `_sources/BaseSchema/modules/<name>/` — two hops shallower than a technique schema at `_sources/techniqueProfile/geochemProfile/<TECH>/tapp/` — but `build_module_bb.py` reuses `schema_path_emitter`'s technique-depth `REF_MAP`. A BaseSchema target written as `../../../../BaseSchema/X` climbs past the repo root and must be `../../X`; `build_module_bb._reref_module_depth()` does that rewrite. Only the full CI postprocess catches this class of break — `validate_examples.py` does not.

### Module ownership, and the rules it implies

**Where a module covers a field, the module owns the placement — in the schema AND in the generated
examples.** `module_composition.plan()` decides coverage; the technique's row is dropped from its
overlay, and the example emitter drops it too (only the PARAMETER path: the module's `$def` still
requires the composable placement, so dropping the item outright strips required properties out of
the example). "A technique's own row wins" was right while modules only ADDED fields and wrong the
moment one covered a field.

Consequently a module-covered technique sidecar row carries **no Schema Path** — `Source = module`
plus a note naming the owner. The row stays, because `migrate_sidecar` diffs Metadata Items against
the workbook. `python tools/simplify_sidecars.py --write` does this and REFUSES divergent rows,
where the technique's authored path differs from the module's: blanking there would adopt the
module's placement and destroy an authored decision. ~40 such rows are open for review.

**A module must not hardcode an instrument selector it cannot guarantee.** `core` composes into
every technique; when it placed `Instrument Manufacturer` under
`schema:instrument[schema:additionalType='SEM']` (a `seed_module_sidecars` consensus, SEM winning
only on numbers), every ICP-MS, TEM, XCT and EPMA procedure got its instrument metadata on an SEM
node. A family module naming its own component (`laserAblation` → `Laser Ablation System`) is fine.

**`Goodness-of-Fit` placement rule.** It sits in `dqv:hasQualityMeasurement` UNLESS it is keyed as a
reported property AND the procedure defines a reportedProperties list, in which case it is in the
reported-property `variableMeasured` list. `Aggregation` carries both rows: `variableMeasured` keyed
`reported property`, and the unkeyed `dqv` default.

### Instruments and keyed-table columns

**`@id` is REQUIRED on an instrument and on an inline `schema:hasPart` component.** A monitored
species has to be able to name the device — or the part — that reports it. Generated identifiers are
`ex:instrument/<Token>` and `ex:instrument/<Token>/part/<Component>`, derived from the
`schema:additionalType` token so they are stable across regenerations.
`tools/add_instrument_ids.py` backfills the `adaProfile` and hand-authored BaseSchema examples that
no pipeline regenerates; anything the pipeline owns must come from the generator, not that script.

**A keyed-table column is always a `schema:PropertyValueSpecification` on the procedure side.**
Read-only is an attribute of the specification (`schema:readonlyValue`), not a different type; the
base `KeyedTableColumn` requires the specification form, so emitting `schema:PropertyValue` there
produced an `allOf` no instance could satisfy. The value form is right on `$Dataset` alone.

**Selector tokens are vocabulary-backed.** `ada:vocab/instrumentType` and
`ada:vocab/instrumentComponentType` are generated from the WIRED sidecars by
`tools/build_instrument_codelist.py` and referenced by `schema:inDefinedTermSet`, the same
annotation convention `componentType` uses.

## componentType architecture (source of truth: spreadsheet)

`ada:componentType` is a **string** on each archive `hasPart` item, classifying the file (e.g. `ada:EMPAImageMap`). Two layers of constraint apply via `allOf`:

1. **Base BB enums.** Each file-type BB (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of allowed componentType strings — derived from the **Components worksheet** of `C:\GithubC\amds-ldeo\metadata\ADA-AnalyticalMethodsAndAttributes.xlsx`. This enforces that `ada:EMPAImageMap` only validates on parts whose `@type` includes `ada:imageMap`. The cached mapping lives at `tools/componentType_enum_cache.json` and is applied via `python tools/apply_componentType_enums.py`. Run with `--refresh --xlsx PATH` after editing the spreadsheet.

2. **Profile/detail layer.** A technique profile's `schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref: '../adaProduct/schema.yaml#/$defs/universalComponentTypeBranch'` for universal componentTypes (factored from per-profile boilerplate); (b) inline `properties.ada:componentType: {type: string, enum: [...]}` for technique-specific componentTypes that have no detail block; (c) `$ref: '../detail/schema.yaml'` (the technique's own detail block) for detail-bearing componentTypes. Detail schemas pin `ada:componentType` via `anyOf: [{const: "..."}]` consts AND contribute detail-specific sibling properties (e.g. `ada:spectrometersUsed`, `ada:signalUsed`) — flat on the hasPart item, NOT nested inside componentType.

## adaProduct extension over cdifProvActivity

`adaProduct` redefines `prov:wasGeneratedBy.items.properties` with ADA-specific keys; via `allOf` merge, the upstream `cdifProvActivity` constraints still apply. Recent renames/extensions:

- `prov:used` accepts `anyOf [instrument | tappDefinition]` (used to be just instrument; tappDefinition was previously named methodDefinition and lived under geochemProperties/, now at `_sources/BaseSchema/tappDefinition/`; JSON-LD class is `ada:TAPPDefinition`).
- `schema:location` (was `ada:laboratory`) — laboratory $ref.
- `schema:object` (was `schema:mainEntity`) — array of MaterialSample objects (samples analyzed). Required CDIF mbb to extend `cdifProvActivity.schema:object` to also accept arrays of `schema:Thing` per schema.org range; `schema:result` extended symmetrically. Both extensions landed via the propagate-schema run on 2026-04-26.

**Do not re-introduce object-form componentType** (the old design where componentType was `{"@type": "...", ...nested-detail-props...}`). The reverse migration to strings was deliberate; details now sit as siblings.

`files/schema.yaml`'s outer `anyOf` over base BBs intentionally has no permissive `schema:MediaObject` fallback — without it, parts whose `@type` doesn't match a specific BB will (correctly) fail validation.

## Multi-repo schema propagation

A project slash command `/propagate-schema [--dry-run] <change description>` lives at `.claude/commands/propagate-schema.md`. It orchestrates schema/URI/naming changes across the CDIF + ADA + DDE building-block ecosystem (this repo + `metadataBuildingBlocks` + `ddeBuildingBlocks` + four CDIF release repos + `w3id.org` redirects), using parallel per-repo subagents in git worktrees with an all-green gate before any commit and draft PRs only (no auto-merge).

Slash commands are indexed at session startup, so a freshly added command needs a session restart before it appears.

When a request crosses repo boundaries, prefer invoking that command over hand-rolling the orchestration. If it needs adjustment, edit the command file rather than working around it.

## Where the related repos live

See auto-memory `reference_related_repos.md` / `ecosystem_ci_and_w3id.md` for the full list with absolute paths (real tree is `C:\GithubC`, **not** OneDrive — the propagate-schema registry table is stale on this). Summary:
- CDIF upstream (`metadataBuildingBlocks`) and the CDIF profile release repos (named `profile-*`) under `C:\GithubC\CDIF\`
- DDE sibling (`ddeBuildingBlocks`) under `C:\GithubC\USGIN\`
- w3id.org redirects under `C:\GithubC\smrgeoinfo\w3id.org\`
- amds-ldeo / ada_metadata_forms (Django app under `C:\GithubC\amds-ldeo\`; `amds-ldeo/metadata` is itself a git repo, the parent is not; monolithic schema not yet derived from BBs)

## Recurring consistency-bug patterns to watch for

These are real past incidents, not hypothetical:
- Trailing slash in `https://w3id.org/cdif/.../"` URIs (CDIF commit `fcb291eb9`)
- camelCase/underscore drift in conformance class names (e.g. `dataDescription` vs `data_description`)
- Const-concatenation regex artifacts in YAML→JSON (geochem commit `f1e2218a` — last `const` value bleeds into next property)
- Self-referential `$defs` causing `RecursionError` in `resolve_schema.py` (CDIF commit `2f402f6e0`)
- Stale `register.json` entries vs `_sources/` directory listing

The propagate-schema command runs all of these as part of its consistency audit; if you're working outside that pipeline, run them by hand on touched paths.
