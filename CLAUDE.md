# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repo is the ADA (Astromat Data Archive) building-blocks repo — modular JSON-Schema building blocks (OGC Building Blocks pattern) for geochemistry analytical-technique metadata, extending shared CDIF base schemas. It is one node in a larger CDIF-rooted ecosystem; sibling repos and the propagation pipeline are documented in auto-memory.

## Deeper references

- **`agents.md`** (lowercase — that is the tracked filename) — the authoritative, detailed agent guide (directory layout, every tool, the TAPP/detail/profile pipeline internals, the full componentType architecture). Read it when this file's summary isn't enough.
- **`README.md`** — human-facing overview; its generation-pipeline section is a good orientation.
- **`docs/TAPP-schema-generation-workflow.md`** — end-to-end walkthrough of workbook → validated schema.
- **`docs/SCHEMA_PATH_GRAMMAR.md`** — the canonical grammar for the schema-path sidecars.
- **`docs/SILENT_SUCCESS.md`** — thirteen incidents in which a check, a generator or a workflow reported success while not doing its job. Read it before changing a check, a trigger, a required-status-check set or a source-resolution fallback, before combining two sources in a generator, and whenever you loosen a constraint: ask which direction of change each check can see, measure coverage per RECORD rather than per aggregate, resolve by cid rather than by directory — and, for any check, run it and read `$?`.
- **`docs/README.md`** — what is in `docs/`: the sidecar format, its five `Source` values, and the maintenance tools around it. Note **"sidecar" is overloaded**: in `docs/` it means the `*.schemapaths.csv` files, while `<block>/conformance.json` is the unrelated conformance sidecar — see "Conformance sidecars" below.
- **`docs/modules/MODULE_CONSOLIDATION_STATUS.md`** — **state, not design**: how far module consolidation has got, what is decided, and what is open. Re-measure before quoting its percentage. Read it before drafting a module. Measure `tapp/`, never `registry/`: the registries are `isTypeLibrary` and per-technique by construction, so measuring them yields a true-but-meaningless 87% duplication.

Passages that used to live here and record measurements, decisions and history rather than working rules (moved 2026-10-25; read the one that matches what you are touching):

| file | read before |
|---|---|
| `docs/VALIDATION_GATES.md` | changing the audit baseline, the constraint census, the counterexamples, or refreshing vendored remote schemas |
| `docs/CI.md` | changing a workflow, the required-check set, or the build-PR mechanism |
| `docs/LEGACY_PROFILES_AND_CIDS.md` | touching a `profile-ada`/`adaProfile` block, a profile `cid`, a `build_profile.PROFILES` entry, or the nil-token convention |
| `docs/DETAIL_BLOCK_PLACEMENT.md` | relocating a detail block's `$ref` or editing detail-block descriptions |
| `docs/ANALYTICAL_MODE.md` | anything involving `ada:analyticalMode`, the workbook mode-flag columns, or the bare-`[]` requiredness defect |
| `docs/COMPONENTTYPE_VARIANTS.md` | proposing per-variant componentTypes, or detecting Mc/Q/Sf variants |
| `docs/CONFORMANCE_SIDECARS.md` | changing `build_conformance_sidecars.py` or any `conformance.json` |
| `docs/COLLECTOR.md` | the Collector part, `ada:collectorConfiguration` or `ada:collectors` |
| `docs/SHARED_CHECKOUT.md` | committing anything regenerated, or working in the main checkout |

## Commands

All tooling is `python tools/<name>.py`. There is no build system and no pytest suite — the validation tools *are* the test suite. Dependencies ARE pinned, in `requirements.txt` (`pip install -r requirements.txt`), with the database driver split into `requirements-db.txt` so CI and anyone regenerating schemas does not need psycopg2. The pins are exact, not bounded, because the output of these tools is committed and diffed: PyYAML's line-wrapping changed between versions and reflowed 2764 lines of `registry/parameterTemplates` and `registry/parameterValues` with no semantic change, twice. Do not "fix" a pin to a newer release without regenerating and confirming an empty diff. `openpyxl==3.2.0b1` is deliberately a PRE-RELEASE — it is what the committed artifacts were built with.

Regenerate after any `_sources/**/schema.yaml` edit:

```
python tools/regenerate_schema_json.py        # *Schema.json from schema.yaml (--dry-run to preview)
python tools/resolve_schema.py --all          # resolvedSchema.json everywhere (downstream validators read this)
```

`resolve_schema.py` also accepts a single `<profile>` name or `--file <schema.yaml> -o <out>` to resolve just one — far faster than `--all` after a localized edit.

> **TAPP source = the `tapp/` git submodule** ([amds-ldeo/tapp](https://github.com/amds-ldeo/tapp)); `tools/tapp_source.py:current_delivery()` resolves to it. Clone with `--recursive`, then `git submodule update --init --checkout` — the `--checkout` is REQUIRED because `.gitmodules` sets `update = none`. That setting exists to stop OGC's reusable postprocess workflow, which runs `git submodule update --recursive --remote` and then commits everything, from silently advancing the pointer to whatever is at the tip of tapp's default branch (it did exactly that in `c0194f7e4`, which broke `TAPP_CONFIGS` for 13 of 16 techniques on main). Bumping the delivery is therefore a deliberate act: check out the revision you want and `git add tapp`. **Two CI jobs DO need the submodule populated**, and both populate it themselves with the explicit `--checkout` (`submodules: true` on `actions/checkout` is not enough — it honours `update = none` and leaves the submodule empty): `check-determinism.yml`, which regenerates the example stage twice, and `check-schema-drift.yml`, which regenerates the WHOLE chain as of 2026-10-16. The other two jobs do not, since nothing under `_sources/` references the submodule and `bblocks-config.yaml` imports only CDIF's remote register. (The earlier `resolve_schema.py --all` gh-pages blocker is now **lifted** — CDIF publishes `objectReference`; it runs clean.)

The migration tools, in run order: `python tools/intake_delivery.py <delivery>` (read-only first pass — what carries, what is renamed, what arrives **DROPPED** or flagged, what composing a module would change), then `python tools/migrate_sidecar.py <tapp> --source <table> [--seed <nearest tapp>] --write` (carries a sidecar onto a new revision; record non-mechanical renames in its `ALIASES` rather than losing the authored paths), then `python tools/fill_flagged.py --write`.

`TAPPS20260811/` and `TAPPS20260813/` at the repo root are **earlier inline drops**, not the source: `tapp_source.current_delivery()` prefers the `tapp/` submodule and only falls back to them. That fallback used to be silent, so an unrecursed clone — or a fresh git worktree, since `update = none` leaves both empty — would build from the old drop and report everything green; it is now a **refusal**. `tapp_source.require_delivery()` raises `StaleDeliveryError` naming the drop it would have used and the fix, `current_delivery()` and `manifest_path()` both call it, and `regenerate.py` calls it as a preflight before its first stage. Set `ADA_ALLOW_STALE_TAPP_DROP=1` to take the old drop deliberately (warning on stderr), the same way `resolve_schema.py --allow-unresolved` is the deliberate override for its refusal. See `docs/SILENT_SUCCESS.md` #7.

Validate ("run the tests"):

```
python tools/validate_examples.py                 # validate all example*.json vs resolvedSchema.json
python tools/validate_examples.py --filter <name> # single BB/example — the "run one test" form
python tools/validate_instance.py --dir <dir>     # profile-aware (auto-detects dcterms:conformsTo)
python tools/audit_building_blocks.py             # completeness, schema<->JSON consistency, resolvedSchema freshness, SHACL
python tools/audit_building_blocks.py --write     # accept its current failures as the baseline (see below)
python tools/check_componentType.py               # componentType vocab/enum drift (annotation-only base layer, so JSON Schema alone misses it)
python tools/constraint_census.py                 # did a regeneration LOSE a constraint? (validate_examples cannot see that)
python tools/validate_counterexamples.py           # do instances that MUST fail still fail? (the other half)
```

**The audit is baselined, and it gates.** It exits 1 on any issue not recorded in
`docs/audit_baseline.json`, and runs as a step of `check-schema-drift.yml`. The 5 accepted
failures are the legacy `profile-ada` blocks for QRIS, RAMAN, VNMIR, XANES and XRD (no examples).
A deliberate change is two steps: fix or accept, then `--write` and commit the baseline in the
same PR. A vocabulary `@id` collision is fatal and NOT baselineable. Details, including which
`--checks` CI runs and why: `docs/VALIDATION_GATES.md`.

`resolve_schema.py` REFUSES to write a schema whose refs did not resolve, and exits 1 naming each
one and its JSON path. `--allow-unresolved` writes anyway, leaving placeholders where the content
should be; reach for it only to get past a known-broken ref deliberately. The check exists because
`validate_examples` reads `resolvedSchema.json`, so a schema quietly missing a branch makes the
examples that should have failed pass instead — and because a transient file-read error in an
earlier stage would otherwise become a permanently degraded artifact on the next run.

**A vendored remote schema can stay stale through `--refresh-remote`.** A relative `$ref` inside
`vendor/remote/` is read off disk and never re-fetched — delete the vendored file to force the
miss. And re-run `resolve_schema.py --all` after the vendored file really changes, before
believing any count. See `docs/VALIDATION_GATES.md`.

**`constraint_census.py` and `validate_counterexamples.py` catch what `validate_examples` cannot.**
Deleting a constraint makes a schema more PERMISSIVE, so no corpus of positive examples can see
the loss. The census counts the constraints themselves against `docs/constraint_census.json`
(with a per-block digest to catch a SWAP); the counterexamples (`docs/counterexamples.json`, each
a mutation of a live example that MUST be rejected, with a mandatory `expect`) catch a constraint
that is still present but no longer bites. Neither is a stage of `regenerate.py`: a deliberate
constraint change is regenerate, then `--write` and commit the census manifest in the same PR. Both
run as steps of `check-schema-drift.yml`. Design rationale: `docs/VALIDATION_GATES.md`.

Regenerate the conformance sidecars after any change to a profile's componentTypes, its cid, or
`TAPP_CONFIGS` — they are committed and `Regenerate and diff` will catch a stale one:

```
python tools/build_conformance_sidecars.py            # dry run; prints UNION and SKIP lines
python tools/build_conformance_sidecars.py --write    # 71 conformance.json
```

Render the human-readable pages (dataset record + TAPP definition, into `build/htmlViews/`):

```
python tools/build_html_views.py --source examples --all    # the 657 committed examples
python tools/build_html_views.py --source ada2 --limit 50   # real ADA holdings from public.json_table
```

`--source ada2` connects with `ADA_NAME` / `DB_2024_USER` / `DB_2024_PASSWORD` / `DB_2024_HOST` /
`DB_2024_PORT` — the same variables the `metadata` repo's loaders use. It is **not** reached
through `PGSERVICEFILE` or `.pgpass`; testing those and concluding the database is unreachable is a
mistake already made once.

Local green ≠ CI green: `validate_examples.py` cannot catch the OGC bblocks-annotate dependency-resolution / dangling-`$ref` failures — only CI (or the branch `.github/workflows/validate-branch.yml`) runs the full postprocess.

**Regenerate through `tools/regenerate.py`, not the individual tools.** The stages are a
dependency chain, not a checklist, and running them out of order fails SILENTLY — both known
instances produced a green `validate_examples`, because dropping a constraint only makes a schema
more permissive:

- **modules before simplify.** `simplify_sidecars` blanks a technique row when a module covers the
  field. Deciding that against module BBs not rebuilt since their sidecars changed deleted
  `Limit of Quantification (LOQ) Method` from nine ICP-MS schemas (2026-09-03).
- **resolve before `build_profile`'s second pass.** `build_profile` backfills its examples'
  `variableMeasured` entries by reading `profile/resolvedSchema.json` for the variables the
  COMPOSED schema pins; run before the resolve it reads the previous one and misses whatever the
  composition just added.

```
python tools/regenerate.py                 # everything, in order
python tools/regenerate.py --tapp semTAPP  # one technique (shared stages still run)
python tools/regenerate.py --dry-run       # print the plan
python tools/regenerate.py --from resolve  # resume at a stage
```

**Use `--tapp`; do NOT call a stage tool directly for one technique.**
`python tools/build_pathdriven.py <tapp>` looks self-contained — it resolves its own schemas and
writes its own `-P0` examples — but it produces a POORER `-P0` than the same stage produces inside
`regenerate.py`, because the shared stages that run first are load-bearing. Measured 2026-09-13 on
`solutionSficpmsTAPP`: the standalone run dropped the whole `schema:actionProcess` subtree — 74
JSON paths, -305/+85 lines — and dropped it identically with the sidecar reverted to HEAD, which is
what proves it is the invocation and not the input. `validate_examples` stayed at 614/26
throughout, because losing content only makes an instance smaller and more permissively valid.
This has the same signature as the two ordering hazards above: silent loss under a green
validator. Audit regenerated examples for LOST JSON paths, never for a passing count alone.

**`docs/modules/emitted.json` records what the built module `$defs` ACTUALLY carry**, written by
`build_module_bb --write` in the same run that writes the schemas. `module_composition.plan()`
reads it rather than re-deriving coverage from the module sidecars — the sidecar says where a
field *should* go, the built `$def` says where it *did*, and the two diverge whenever a module BB
is stale. Reading the manifest makes that fail closed: a stale build yields a stale manifest that
agrees with it, coverage is under-reported, and a technique keeps its own row instead of losing
the field. Never hand-edit it; a missing manifest means "compose nothing".

Regenerate a TAPP technique from its source table (a CSV in the `tapp/` submodule's `Current TAPPs/`) — never hand-edit generated output; fix the table (upstream in amds-ldeo/tapp), the sidecar, or a tool and regenerate:

```
python tools/bootstrap_schemapaths.py <table.csv>  # 1. seed/refresh docs/<wb>.schemapaths.csv (the source of truth)
python tools/build_tapp.py         <TAPP_NAME>  # 2. registry catalogs + vocab
python tools/build_pathdriven.py   <TAPP_NAME>  # 3. tapp/ + detail/ schemas from the sidecar
python tools/build_profile.py      <TAPP_NAME>  # 4. profile/ schema
python tools/build_tapp_examples.py <TAPP_NAME> # 5. publication-derived example*.json
python tools/resolve_schema.py --all            # 6. resolve
python tools/validate_examples.py               # 7. verify
```

**Step 5 is easy to skip and its omission is silent.** The publication examples (`example<TAPP>-<Pub>.json`, one per column after `Literature Assessment`) are NOT rebuilt by `build_pathdriven`, so a sidecar change moves the schema while they keep the placement they were last generated with. Nothing complains until `validate_examples` runs, and the failure reads as a schema bug rather than a stale artifact — moving `Detection Limit` off `targetSpeciesColumns[]` produced 125 such failures that regeneration alone cleared. `build_tapp_examples` is not a second generator: it reads the workbook's publication columns for CONTENT and calls `schema_path_example_emitter.build_example(tapp, values=...)` -- the same emitter that writes the `-P0` files -- for PLACEMENT.

## CI: six workflows, four of them required

| workflow | check name | trigger | required? |
|---|---|---|---|
| `validate-branch.yml` | `Validate and annotate (no pages)` | push (not main), PR | yes |
| `check-schema-drift.yml` | `Regenerate and diff` | every PR | yes |
| `check-determinism.yml` | `Regenerate twice and compare` | every PR | yes |
| `check-examples.yml` | `Validate committed examples` | every PR | yes (2026-10-16) |
| `process-bblocks.yml` | — | push to main | — |
| `deploy-viewer.yml` | — | `workflow_run`; push to main under `build/**` | — |

**The check name is the JOB name, never the workflow's `name:`.** Every context above is a job
name and three of the six workflows are *titled* something else — `check-schema-drift.yml` is
named "Check generated schemas are current" and reports "Regenerate and diff". Requiring a
workflow title adds a context no run can report, which is pending forever, which is the deadlock
the ordering rule below exists to prevent. Read the name from a real check-run before requiring
it: `gh api repos/<owner>/<repo>/commits/<sha>/check-runs --jq '.check_runs[].name'`.

**`Regenerate and diff` regenerates all nine stages**, so a sidecar edit committed without
regenerating, or a schema built from a superseded delivery, turns it red. A full `regenerate.py`
over clean `main` changes zero files, which is what makes the comparison meaningful. The history
of what became required and when is in `docs/CI.md`.

These four are **required** in branch protection. Two rules follow from that and both were
learned the hard way:

**Never add a `paths:` filter to a required workflow.** A required check that does not RUN is not
"skipped", it is pending forever, and the PR can never merge — including the PR that would remove
the filter. `check-schema-drift.yml` had one; dropping it (#38) is what let it become required.
Affordable only because caching the parsed source files took that job from 59m to 3m37s and a full
`resolve_schema.py --all` from ~62 minutes to under 6.

**Auto-merge waits only on REQUIRED checks.** It will merge straight past a red non-required one.
That is how #31 landed with a failing determinism check and #32 landed with failing drift, leaving
main red for two days. Arm auto-merge only when the failing checks are ones you have read.

### A GITHUB_TOKEN push triggers NO workflow

This is load-bearing, not trivia, and it is observable in main's own history: the three
`Building blocks postprocessing` commits have no push-triggered run against them, only the chained
`workflow_run` for deploy-viewer. Anything that needs checks to fire must be done by another
identity.

### build/ reaches main as a pull request

`build/` IS committed (`deploy-viewer.yml` publishes it without regenerating), but branch
protection declines the postprocess's push. So `process-bblocks.yml` force-resets
**`bblocks-build`** to main, runs the postprocess there, and opens a PR with `BBLOCKS_PR_TOKEN`
(a PAT, so the PR gets checks) with auto-merge armed. **`bblocks-build` is machine-owned** —
never branch from it, commit to it, or base work on it. A loop-breaker skips runs whose
triggering commit starts `Building blocks postprocessing`. Full mechanism: `docs/CI.md`.

## Source vs generated

**`_sources/` is NOT "the source" and `build/` is NOT "the generated output".** That two-way
split was stated here until 2026-10-07 and it is wrong in the direction that causes damage: most
of `_sources/` is generated, and reading it as hand-authored invites editing a file that the next
regeneration overwrites. The question a label has to answer is **"if this is wrong, do I edit it
or fix a generator?"** — so the taxonomy is by WHAT WRITES IT, measured, not by directory:

| path | 257 `schema.yaml` | written by |
|---|---|---|
| `techniqueProfile/geochemProfile/*/tapp/` | 61 | `build_tapp` + `build_pathdriven` |
| `techniqueProfile/geochemProfile/*/detail/` | 61 | `build_pathdriven` |
| `techniqueProfile/geochemProfile/*/profile/` | 34 | `build_profile` |
| `BaseSchema/modules/*/` | 16 | `build_module_bb` |
| `registry/*/` | 6 | `build_tapp` |
| `BaseSchema/*` (non-module) | 18 | **nobody — edit directly** |
| `techniqueProfile/adaProfile/*/` | 45 | **nobody — edit directly** (`generate_profiles.py` is deprecated and refuses to run) |
| `techniqueProfile/geochemProfile/*/profile-ada/` | 9 | **nobody — LEGACY, see below** |
| `techniqueProfile/geochemProfile/*/detail-legacy/` | 1 | **nobody — legacy** |
| `adaSubjects/*/` | 6 | **nobody here** — derived from pinned `metadata` commits; NOT register blocks (no `bblock.json`), see its `README.md` |

So 178 of 257 `schema.yaml` under `_sources/` are generated (counted 2026-10-25). The same applies to everything
beside them: all 257 `resolvedSchema.json` (`resolve_schema.py`), all 257 `<name>Schema.json`
(`regenerate_schema_json.py`), and the generated `example*.json` (`build_tapp_examples` — but see
the three categories of example below, because the static and source-derived ones are NOT
regenerated).

`build/` is genuinely generated, by the OGC postprocess — and it is **committed**, because
`deploy-viewer.yml` reads `build/register.json` and `build/tests/report.json` out of main and
publishes them without regenerating. The one part not committed is `build/htmlViews/`.

### `profile-ada` and `adaProfile` are the PRE-TAPP generation, and the goal is to retire them

They predate the TAPP pipeline (SAMIS-era work), and nothing regenerates them:
`generate_profiles.py` is deprecated and refuses to run, so no regeneration will ever correct a
mistake in one — edit them directly. There are **9** `profile-ada` schemas under
`geochemProfile/` and **32** technique directories under `adaProfile/` holding **45**
`schema.yaml`. (`_tapp_lib.write_profile_ada_companions` writes the four companion files beside a
block; it does not generate these schemas.) All 9 `geochemProfile` techniques now have a
TAPP-based `profile/` beside the legacy one.

Rules to carry, with the measurements behind them in `docs/LEGACY_PROFILES_AND_CIDS.md`:

- **Give a TAPP profile a DIFFERENT `cid` from its legacy twin** (`ada<TECH>` against
  `ada<TECH>Full`). A forked cid makes `build_conformance_sidecars` discard one block's
  componentType vocabulary.
- **`addtype[0]` in a `build_profile.PROFILES` entry must be answered from the corpus** — the
  head label real records carry, from adaProduct's controlled list.
- **A record's profile URI is DERIVED from its content by the ADA loader, not cited.** Retiring or
  renaming a cid moves every record that derives to it, and no gBB check reads ADA records.
  Find which block pins a cid with an ANCHORED pattern:
  `grep -rlE "profiles/<cid>([^A-Za-z0-9]|$)" --include=schema.yaml _sources/`.
- **EPMA and TEM records now derive the TAPP cid; SEM deliberately does not.** The loader's
  `preserve` overrides the conformance priorities on purpose; do not describe those priorities as
  vestigial or tidy them away. Flipping SEM needs its own measurement and nil-token pass first.
- **The resolution for a pin legacy records cannot satisfy is a NIL TOKEN, not a relaxed
  constraint**: the expanded IRI `http://www.opengis.net/def/nil/OGC/0/unknown` as a string, in a
  four-property `variableMeasured` member. The loader emits it; no gBB generator does. Do not cite
  it as precedent for relaxing a TAPP constraint, and do not add a second sentinel.

### Labels, generator determinism, and what "detail" means

**Terminology.** Use `authored` for a file or placement a person decided and no generator
rewrites, and `generated by <tool>` otherwise. Do NOT write "hand-authored" — it was swept out of
the repo in 2026-09 because it reads as "the maintainer typed this content in", which is not how
most of this material came to exist (much of it was drafted with AI assistance against the TAPP
workbooks). That provenance is worth recording once; it is not the operative label, because it
does not tell you whether to edit the file or fix the generator.

When fixing a bug that surfaces in a generated artifact, **trace to the source generator/template/schema and regenerate** — never patch the build output directly. This is a standing rule across this ecosystem; it has its own feedback memory.

**Generated output is a function of its source, not of when it ran.** Two generators broke that
and both were fixed on 2026-09-05: `build_module_bb` stamped `date.today()` into every module
`bblock.json`, walking `core`'s `dateTimeAddition` from its real 2026-08-21 to 2026-09-04 over six
regenerations (it is the date the block was ADDED — written once, carried forward; `dateOfLastChange`
moves only when the schema content changes, and the OGC postprocess recomputes it for
`build/register.json` anyway); and the shared registries recorded which techniques were regenerated
LAST, because `remove_owned_blocks` + `append_defs` rewrites a technique's entries at the end of the
file. `build_tapp.sort_defs()` now orders them by key, so a `--tapp` spot regen and a full run
produce the same bytes. Keep it that way: a generator that varies by run date or invocation order
cannot be diffed, which forecloses any CI check that regenerates and compares.

**"detail" means two different things, and they compose at different nodes.** A dataset-root
detail block overlays `schema:Dataset` and belongs as a top-level `allOf` entry beside the base
product; a hasPart-item block pins `ada:componentType`, describes a data component, and belongs as
an `anyOf` branch on `schema:distribution.hasPart`. `agents.md` has the authoritative split and the
grep that re-derives it — the two kinds do **not** follow the `adaProfile` / `geochemProfile`
grouping, so do not infer placement from the directory.

**The composition is right and the DESCRIPTIONS are wrong — not the other way round.** A technique's
detail must apply to a monolithic dataset, one reconstructed volume with no `hasPart` collection, as
well as to a component collection. Dataset-root composition covers both; pinning
`ada:componentType` would break the monolithic case outright, because there is no hasPart item to
carry it. So the measured `0 of 61` (no geochemProfile detail block constrains
`ada:componentType`; see `docs/DETAIL_BLOCK_PLACEMENT.md`) is the correct design, and the 49 descriptions that call themselves
hasPart-item blocks are the error. Do not "fix" the pin.

The monolithic case is barely exercised, which is why the descriptions survived: of 7446 ADA
records, 7442 carry `hasPart` and 4 are monolithic. Rare is not optional.

**Three levels, and only one works both ways.** When placing a property, this is the choice:

  dataset root   `$Dataset.<prop>`                                     both
  distribution   `$Dataset.schema:distribution[].<prop>`               both — the volume when
                                                                       monolithic, the collection
                                                                       when not
  hasPart        `$Dataset.schema:distribution[].schema:hasPart[].…`   COLLECTION ONLY; there is no
                                                                       such node in a monolithic
                                                                       dataset

Anything that must hold either way belongs at the root or on the distribution. Put a property on
hasPart only when it genuinely VARIES per component, and then the monolithic equivalent still has
to exist at distribution level or the fact becomes unsayable. `Output Data Format` is the worked
example: `$Dataset.schema:distribution[].schema:encodingFormat[]`, unselected, so it holds for a
lone volume and for a collection alike. A `[@type = schema:Collection]` selector would exclude the
monolithic case, which is the one to be careful of.

Measure before relocating any detail-block `$ref`: moving the twelve `adaProfile` hasPart-item
blocks to the top level failed all 218 records of the affected profiles. The measurements, and how
to reproduce them, are in `docs/DETAIL_BLOCK_PLACEMENT.md`.

One standing gotcha bites spot regenerations:

- **`tools/resolve_schema.py` and `tools/regenerate_schema_json.py` are synced copies** from `metadataBuildingBlocks/tools/`. Don't edit them here — fix the canonical copy upstream and re-sync (`python tools/sync_resolve_schema.py --apply` from that repo).

## Composition modules

`_sources/BaseSchema/modules/<name>/` (`core`, `samplingUnitSelection`, `analyte`, `aggregation`, `blank`, `calibrationFactor`, `laserAblation`, `mcIcpms`, `solutionIntroduction`, `geochronology`, `uPb`, plus `icpms`, `collisionCell` and `compositionQC` added by the 2026-09 delivery; plus `reportingCore`, which the current manifest composes into nothing — `group1` was in that state too and is now archived to `archive/modules/`, `a1ba43b19`. `targetSelection` was renamed `samplingUnitSelection` and `arAr` retired upstream, both in `af3f7bc`) factors fields shared across techniques into module building blocks. Each exposes up to two `$defs`, split by path root: **`ProcedureIdentification`** (from the module's `$MethodDefinition` paths, composed into `tapp/`) and **`AnalysisIdentification`** (from its `$Dataset` paths, composed into `detail/`); `reportingCore` is conditional and exposes one `$def` per block per side (see `docs/REPORTINGCORE_BLOCKS.md`). All 16 techniques in `tapp/composed_tapps.json` compose modules today; membership is matched on the table's **filename**.

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

**A module cannot constrain three containers, all for one reason.** `allOf` intersects, and the
consuming technique already constrains each of these as a CLOSED shape from its own table, so two
universal constraints on one array can never both hold: `schema:additionalProperty` (a closed
`anyOf` over the table's parameters), a **keyed-table COLUMN array** (`ada:targetSpeciesColumns`,
`ada:monitoredPropertyColumns`, `ada:reportedPropertyColumns` — narrowed to the
technique's generated column defs), and a **default-ROW array** (`ada:defaultTargetSpecies`,
`ada:defaultMonitoredProperties`). `build_module_bb.is_composable()` is the single predicate;
`module_composition._is_composable` delegates to it so the generator and the planner cannot drift.
The column case arrived with `Module_ICPMS` and broke 96 examples — a row ending at
`…ada:targetSpeciesColumns[]` carries the COLUMN's scalar Data Type, so composing it emitted
`items: {type: string}` against the technique's `items: {anyOf: […column objects…]}`.

**`Source = unplaced` in a module sidecar is a REFUSAL, not a gap.** `seed_module_sidecars` fills
blank paths from technique consensus; a row deliberately left blank (Core's `Instrument
Manufacturer`/`Instrument Model`, which must not hardcode an instrument selector) was re-inferred
onto `schema:instrument[additionalType='SEM']` by a re-seed — the same defect as the rule above it,
arriving a second time by the same route. The seeder now keeps an `unplaced` row like any authored
one.

**Anything checking a RAW sidecar cell must normalise first.** `schemapath_io.load_spec()` runs
`norm.mechanical(norm.preclean(path))` before the emitter parses, and `mechanical()` expands
supported author shorthand — `prov:used[sel]` → `prov:used.<kind>[sel]`, doubled dots, `Schema:`.
`intake_delivery`'s grammar check read the raw cell and reported 14 canonical-equivalent rows as
broken. `schema:used` is the one that really is an error (schema.org has no `used` property);
nothing normalises it and `schema_path_parser` now rejects it.

**A `schema:step` selector literal is sentence-case** — `'Data processing'`, `'Sample preparation'`,
`'Data acquisition'`, `'Sample digestion'`, `'Ion milling'`. The literal IS the node's identity, so
Title Case builds a second, separate step: eight such rows made a technique row read as diverging
from the module that placed it identically.

**`'Data processing'` is the canonical name for that step, and `'Data reduction'` is retired**
(2026-10-12). Two names for one concept is the defect, not a convenience: the step constraints are
`if`/`then`, so a workflow using the other spelling does not fail — in the 3 profiles with no
`contains` pin it silently skips the constants requirement entirely. ADA's authored method
registry settled it, 83 of 89 workflows calling it "Data processing" against 4 "Data reduction",
and gBB's own plan side already agreed (step 4 of `tappDefinition/description.md`). The rename ran
through the SIDECARS, which is the only place that works: the emitter builds the schema
conditional AND the example step from one selector, so all three layers move together or none do.
137 selectors across 24 sidecars; the census reported it as a SWAP with counts unchanged in 50
blocks, which is the case its per-block digest exists for.

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
`tools/add_instrument_ids.py` backfills the `adaProfile` and static BaseSchema examples that no
pipeline regenerates; anything the pipeline owns must come from the generator, not that script.

**Three categories of example, and they are produced differently.** Saying an example was
"hand-authored" has been misleading: nobody types these.

  generated      the great majority — `build_tapp_examples` renders one per publication column of
                 a TAPP workbook. Regenerated every run; never edit them.
  static         the BaseSchema fixtures and the `adaProfile` profile-ada examples. No pipeline
                 regenerates them, which is why `add_instrument_ids.py` has to backfill their ids.
                 One static example lives in a GENERATED directory and is easy to mistake for its
                 neighbours: `XRD/detail/exampledetailXRD-identifierOnlySample.json`, the positive
                 half of the `schema:name` -> `schema:identifier` substitute line (its negative
                 half is `docs/counterexamples.json`'s `sample-needs-name-or-identifier`). Nothing
                 else in the repo carries an identifier WITHOUT a name, so losing the relaxation
                 is invisible to every other check — `docs/SILENT_SUCCESS.md` #8. Its filename
                 sits outside both generators' namespaces on purpose; its `.provenance.md` holds
                 the rebuild recipe, and adding `schema:name` back is NOT the repair.
  SOURCE-DERIVED assembled from primary sources rather than from a workbook column, and kept
                 because a generator cannot invent their content. Each carries a
                 `<example>.provenance.md` BESIDE it in the same building-block directory,
                 recording where every field came from:
                   exampleadaSolutionMCICPMS-ETHZ-20240903  the deposited Neptune .exp/.log files
                                                            plus the ADA record
                   exampleadaEPMA-UAZ-20260131 (+ -points)  a real UAZ session, its method
                                                            description, and the nearest paper
                   exampleadaLAMCICPMSUPb-Sundell2021       Sundell, Gehrels & Pecha 2021,
                                                            doi:10.1111/ggr.12355
                   exampleebsdTAPP-P0 + exampledetail-P0   14 Curtin method-description
                                                            documents behind 4,305 references
                   examplestemTAPP-HF5000 (+ detail)        HyperSpy exports from a Hitachi
                                                            HF5000 at the University of Arizona
                   examplestemTAPP-P1 (+ detail)            .ser files from an FEI TitanX at
                                                            Lawrence Berkeley
                 Describe these as source-derived, and name the source; "hand-authored" implies a
                 person edited the JSON, which is not what happened.

**A source-derived block is NOT fixable by regenerating it, and the loss is silent.** The four STEM
and EBSD blocks carry protocol constants read out of method-description documents and instrument
exports, which no generator can invent from a sidecar. Measured 2026-10-08 with the sanctioned
`regenerate.py --tapp`: `ebsdTAPP` loses **15 JSON paths** of its `-P0` example
(`ada:ebsdCameraGain`, `ada:beamCurrentDefault`, `ada:crystalStructureFileSourcesDefault`, …) and
**81** schema paths, `stemTAPP` loses **41**, and generic scaffolding arrives in their place while
`validate_examples` stays green -- because losing content only makes an instance smaller and more
permissively valid. Each example's `.provenance.md` carries its own measurement. Read it before
regenerating anything under STEM or EBSD.

**Two words, two meanings — use them precisely.** *Source-derived* is for content assembled from
primary sources (the examples above). *Authored* is for a placement or a schema fragment a person
decided and no generator rewrites — the sidecar's own `Source=authored` value means exactly this,
"human-set, preserved verbatim across re-seeds". Neither is "hand-authored", which was swept out of
the repo in 2026-09 because it reads as "the maintainer typed this content in", and he did not.

**A keyed-table column is always a `schema:PropertyValueSpecification` on the procedure side.**
Read-only is an attribute of the specification (`schema:readonlyValue`), not a different type; the
base `KeyedTableColumn` requires the specification form, so emitting `schema:PropertyValue` there
produced an `allOf` no instance could satisfy. The value form is right on `$Dataset` alone.

**Selector tokens are vocabulary-backed.** `ada:vocab/instrumentType` and
`ada:vocab/instrumentComponentType` are generated from the WIRED sidecars by
`tools/build_instrument_codelist.py` and referenced by `schema:inDefinedTermSet`, the same
annotation convention `componentType` uses.

## Analytical mode: designed upstream, unusable today

The TAPP workbooks' per-field mode-flag columns are read by no tool, and ADA records no acquisition
mode or detector anywhere, so a mode-conditional cannot be built. `$Dataset.ada:analyticalMode[]`
exists and is deliberately optional. If a mode is ever emitted, write conditionals in POSITIVE
polarity — **a conditional you cannot evaluate must degrade to optional, never to required** — and
design them per `schema:hasPart`. The interim answer is the nil token.

**A known emitter defect is NOT fixed**: `schema_path_emitter.insert()`'s bare-`[]` terminal branch
records no requiredness, and `build_module_bb` inherits it. A first fix was reverted after it
destroyed 257,052 constraints with every example gate green (`docs/SILENT_SUCCESS.md` #13). Redo it
one defect at a time with `constraint_census.py` read line by line.

The measurements, the three dead anchors, and the `ada:analyticalMode` nil-token rule:
`docs/ANALYTICAL_MODE.md`.

## componentType architecture (source of truth: spreadsheet)

`ada:componentType` is a **string** on each archive `hasPart` item, classifying the file (e.g. `ada:EPMAImageMap`). Two layers of constraint apply via `allOf`:

1. **Base BB enums.** Each file-type BB (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of allowed componentType strings — derived from the **Components worksheet** of `C:\GithubC\amds-ldeo\metadata\ADA-AnalyticalMethodsAndAttributes.xlsx`. This enforces that `ada:EPMAImageMap` only validates on parts whose `@type` includes `ada:imageMap`. The cached mapping lives at `tools/componentType_enum_cache.json` and is applied via `python tools/apply_componentType_enums.py`. Run with `--refresh --xlsx PATH` after editing the spreadsheet.

2. **Profile/detail layer.** A technique profile's `schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref: '../adaProduct/schema.yaml#/$defs/universalComponentTypeBranch'` for universal componentTypes (factored from per-profile boilerplate); (b) inline `properties.ada:componentType: {type: string, enum: [...]}` for technique-specific componentTypes that have no detail block; (c) `$ref: '../detail/schema.yaml'` (the technique's own detail block) for detail-bearing componentTypes. Detail schemas pin `ada:componentType` via `anyOf: [{const: "..."}]` consts AND contribute detail-specific sibling properties (e.g. `ada:spectrometersUsed`, `ada:signalUsed`) — flat on the hasPart item, NOT nested inside componentType.

**One componentType per product kind — the instrument variant rides on the TAPP, not the type.**
Mc/Q/Sf variants share one componentType (`ada:LAICPMSMap` is the map, whichever mass spectrometer
produced it). Refuse a delivery proposing variant componentTypes; the variant lives on the TAPP
reference (`prov:used`), which JSON Schema cannot dereference. A per-profile componentType list
comes from `build_tapp.TAPP_CONFIGS[<tapp>]["component_types"]`, never from a resolved schema
(resolution inlines the universal enum). See `docs/COMPONENTTYPE_VARIANTS.md`.

## Conformance sidecars — how a record is matched to a profile

`<block>/conformance.json` (71, one per DISTINCT cid, generated by `build_conformance_sidecars.py`)
tells CDIF's detection engine which profile URIs a record conforms to; the ADA loader derives
`conformsTo` from them. Nothing in this repo validates against them, so a wrong sidecar shows up
only as a mis-profiled record in ADA. Key rules, detailed in `docs/CONFORMANCE_SIDECARS.md`:

- `requires` (implication, member → umbrella) and `exclusiveGroup` (mutual exclusion between
  members) are not interchangeable; an umbrella's presence is the UNION of its family.
- A superseded legacy cid that never matches is CORRECT supersession, not the #152 bug — check
  whether its presence ASK is disjoint from the records (defect) or it loses a priority contest
  (correct) before "repairing" it.
- componentTypes come from three sources UNIONED, never falling through. A too-narrow ASK is
  invisible to every check here; check presence per RECORD, not per profile.

## adaProduct extension over cdifProvActivity

`adaProduct` redefines `prov:wasGeneratedBy.items.properties` with ADA-specific keys; via `allOf` merge, the upstream `cdifProvActivity` constraints still apply. Recent renames/extensions:

- `prov:used` relates the activity to what it used through ROLE-KEYED properties, one per role:
  `schema:instrument`, `bios:computationalTool`, `prov:reagent`, and — since #190 —
  **`ada:tappDefinition`**, whose value is either a closed `{@id}` reference or the plan inline
  (`_sources/BaseSchema/tappDefinition/`; JSON-LD class `ada:TAPPDefinition`; previously named
  methodDefinition, under geochemProperties/). The role is read off the property NAME, not off
  `@type` — an inline `prov:Entity` carries `ada:TAPPDefinition` in its `@type` too, so `@type`
  could never separate the role from the class. CDIF admits the role-wrapper SHAPE generically
  (mbb#52: `propertyNames` over a CURIE pattern, deliberately permissive) and geochemProduct
  CLOSES the set to the role it defines — base permissive, profile restrictive, which `allOf`
  composes correctly because an intersection can only narrow.
  **BOTH superseded spellings are now REJECTED — reference and inline alike (2026-10-24).** The
  reference form `{@id, @type: [… ada:TAPPDefinition]}` stayed valid until then, deliberately,
  because 7,263 of 7,447 ADA records linked their TAPP that way and a schema that rejects the
  corpus it describes is one nobody can deploy. The migration retired that reason: the old form
  reads **zero in ada_subjects AND in production ada2**, every reference now role-keyed. The
  sequence is the lesson — **the corpus moved first, then the schema**. Pinned by two
  counterexamples, `tappdef-old-reference-form-is-closed-off` and
  `tappdef-inline-old-spelling-is-closed-off`; the first is the one that matters most, because the
  reference form is what every pre-migration record carried, so re-accepting it would silently
  re-admit a whole generation of records. It is also the tripwire for a store restored from a
  pre-migration backup — the one situation where nobody would otherwise be told.
- `schema:location` (was `ada:laboratory`) — laboratory $ref.
- `schema:object` (was `schema:mainEntity`) — array of MaterialSample objects (samples analyzed). Required CDIF mbb to extend `cdifProvActivity.schema:object` to also accept arrays of `schema:Thing` per schema.org range; `schema:result` extended symmetrically. Both extensions landed via the propagate-schema run on 2026-04-26.

**Do not re-introduce object-form componentType** (the old design where componentType was `{"@type": "...", ...nested-detail-props...}`). The reverse migration to strings was deliberate; details now sit as siblings.

**`ada:procedureAuthorDescription` is DEPRECATED — use
`$MethodDefinition.schema:creator.schema:description`.** Who produced a procedure description, and
how, belongs on the creator, which is where the sidecars already path *Procedure Author Description*
and where every draft instance carries it. The flat `ada:` property was a second home for the same
fact: it reached `main` in #63 required by STEM and EBSD alone (2 of 59 `tapp` blocks), carried by no
example in the repo, and minted by no tool — so every example of both blocks failed its own schema
until #65 removed it. Do not re-add it, and do not satisfy it by writing the description twice.

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

The Collector part's `ada:collectorConfiguration` (free text) and `ada:collectors` (a table that is
N=1 when the string does not parse) are described in `docs/COLLECTOR.md`.

## Recurring consistency-bug patterns to watch for

These are real past incidents, not hypothetical. The CI-side counterparts — where the *check* rather than the schema is what failed silently — are in **`docs/SILENT_SUCCESS.md`**, with the measurements behind each:
- Trailing slash in `https://w3id.org/cdif/.../"` URIs (CDIF commit `fcb291eb9`)
- camelCase/underscore drift in conformance class names (e.g. `dataDescription` vs `data_description`)
- Const-concatenation regex artifacts in YAML→JSON (geochem commit `f1e2218a` — last `const` value bleeds into next property)
- Self-referential `$defs` causing `RecursionError` in `resolve_schema.py` (CDIF commit `2f402f6e0`)
- Stale `register.json` entries vs `_sources/` directory listing
- A `$ref` that exists but sits at the wrong node — present to `grep`, invisible to a reader
  scanning `allOf`, and in an `anyOf` it constrains nothing at all
- **A count taken against a technique's own overlay is not a count of what the technique has.**
  Checking whether a placement change had lost seven fields, they read 0/7 and 4/7 in the
  techniques' `tapp/schema.yaml` — gone. They had not gone: four are module-owned, so the generator
  emits a `$ref` into the module rather than restating them, and they arrive by composition. The
  composed artifact is `resolvedSchema.json`, and that is where a placement question has to be
  asked. The overlay count would have justified reverting a correct change.
- **Two files, one `@id`, is a fork — and which one wins is read order.** Nothing `$ref`s a
  vocabulary FILE; consumers resolve the `@id`. Seven epmaTAPP vocabularies existed twice with
  DIFFERENT terms (`Raster` vs `Rastered`) after a filename convention changed without removing
  what it superseded. The ADA registry ingests sorted by filename and upserts on `@id`, so the
  alphabetically last file won and four of the seven resolved to the stale fork.
  `audit_building_blocks.check_vocab_identifier_collisions` now fails on a repeat; it runs once over
  the catalog, because a collision is a relationship BETWEEN files that no per-block check can see.
  That sentence was true about the intent and false about the code until 2026-10-16: the check
  printed `FAIL  registry/vocab: N identifier collision(s)` into a `main()` that had no exit-code
  path at all, so the whole audit returned 0 either way. It is fatal now, verified by forking an
  `@id` on purpose, and it is the one audit failure the baseline will not accept.
- **A conditional whose `if` is too broad fires on things it was never meant to pin.**
  `geochemProduct`'s TAPP conditional keyed on `@type` containing `ada:TAPPDefinition` alone, so it
  held every `{@id, @type}` *reference* to the whole TAPP schema and failed it on the four
  properties a reference does not carry. Guarding the `if` with `schema:name` separated inline plan
  from reference. **That conditional is GONE as of #190** — the role moved to a property name and
  the guard went with it — so read this as the lesson it is, not as a description of the schema;
  the `schema:name` guard survives only in the narrow branch that closes off the inline old
  spelling, where it does the same job for the same reason. The mirror-image failure is the same conditional being too NARROW: a mis-named
  workflow step matches no `if`, so its constraints are silently absent and the record validates
  clean. Whenever you add an `if`, ask what it matches that you did not intend AND what it now fails
  to match.
- **A generated node that is complete by construction must be emitted AFTER the fill passes.**
  `build_profile._name_procedure()` writes the `prov:used` TAPP reference — `{@id, @type}` and
  nothing else. Run before `_fill_required()`, the sentinel and typing passes could not tell it
  from an object they were meant to finish and padded `schema:instrument: "missing"` plus four
  `{"@id": "nil:missing"}` members into its `@type`, failing 58 of 97 examples.

- **An `anyOf` failure's MESSAGE names an arbitrary branch, so classify from the part, not
  from the message.** When a `schema:hasPart` item matches no branch of `files/schema.yaml`'s
  file-type `anyOf`, the top-level error is only "is not valid under any of the given schemas"
  with an EMPTY instance path. Underneath it sit one sub-error per branch -- measured, **40** of
  them for a single unmatched part -- and which one a tool surfaces depends entirely on how it
  picks: `best_match`, the first in `context`, or a sort by path each give a different answer.
  For an `.obj` shape model typed `ada:noComponentFiles`, the sub-errors led with three
  `@type` complaints and the one that actually explains the failure -- `'ada:noComponentFiles'
  is not one of [...]` -- came fourth.

  This has already cost a wrong conclusion. The metadata session read the surfaced message,
  `'cdif:hasPhysicalMapping' is a required property OR 'cdi:isStructuredBy' is a required`
  -- which is `tabularData`'s requirement -- and classified **70 records** as tabular parts
  missing their column structure. Not one of them was tabular: one was that `.obj`, another a
  part typed `noComponentFiles`. The message named the branch the reporter happened to pick,
  not the branch the part was trying to be.

  So read the `@type` and `ada:componentType` of the part the error path points at and find
  which branch it MEANT to match; the fix is almost always that the part is typed wrongly or
  its componentType is absent from the enum of the block that governs its file kind. Counting
  error messages across parts groups them by the reporter's choice, which is not a property of
  the data.

The propagate-schema command runs all of these as part of its consistency audit; if you're working outside that pipeline, run them by hand on touched paths.

## Committing in a shared checkout

**This checkout is used by several sessions at once.** The incidents behind these rules are in
`docs/SHARED_CHECKOUT.md`.

- **Ask the commit, not the working tree.** Any count that drives a commit comes from a committed
  ref: `git grep -l '<pattern>' HEAD -- '*resolvedSchema.json'`.
- **Never `git add <directory>`.** Stage explicit paths, then assert the size before pushing:
  `git show --name-only --format= HEAD | wc -l` must equal the number you intended. A file listed
  in a commit with 0 changed lines is the symptom of an under-capture.
- **Probe for contention before committing anything regenerated:**
  `find _sources tools -newermt '-5 minutes' -type f | wc -l`. Non-zero and not yours means stop
  and work in an isolated worktree.
- **"Contains" is not "changes."** Judge a branch by
  `git diff --name-only $(git merge-base <branch> origin/main) <branch>`.
- **One worktree per session, never reused**, and at most one session in the main checkout.
- **Populate the submodule in every new worktree** before regenerating:
  `git submodule update --init --checkout tapp`.
- A worktree does not isolate the shared `ada2` database, hot files like this one at merge time,
  or `main` moving underneath a branch.
- **A quiet tree is not a finished job.** Wait for the process's own exit status before believing
  any measurement taken from the tree.
