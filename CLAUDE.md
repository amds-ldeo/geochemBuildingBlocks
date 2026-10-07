# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repo is the ADA (Astromat Data Archive) building-blocks repo — modular JSON-Schema building blocks (OGC Building Blocks pattern) for geochemistry analytical-technique metadata, extending shared CDIF base schemas. It is one node in a larger CDIF-rooted ecosystem; sibling repos and the propagation pipeline are documented in auto-memory.

## Deeper references

- **`agents.md`** (lowercase — that is the tracked filename) — the authoritative, detailed agent guide (directory layout, every tool, the TAPP/detail/profile pipeline internals, the full componentType architecture). Read it when this file's summary isn't enough.
- **`README.md`** — human-facing overview; its generation-pipeline section is a good orientation.
- **`docs/TAPP-schema-generation-workflow.md`** — end-to-end walkthrough of workbook → validated schema.
- **`docs/SCHEMA_PATH_GRAMMAR.md`** — the canonical grammar for the schema-path sidecars.
- **`docs/SILENT_SUCCESS.md`** — six incidents in which a check, a generator or a workflow reported success while not doing its job, each with what exposed it and the rule that follows. The validator passing while content vanishes, a generator whose output varies per process, auto-merge walking past a red non-required check, a required check that can never run, a deploy that skipped the event it was given a trigger for. Read it before changing a check, a trigger or a required-status-check set.
- **`docs/README.md`** — what is in `docs/`: the sidecar format, its five `Source` values, and the maintenance tools around it.
- **`docs/modules/MODULE_CONSOLIDATION_STATUS.md`** — **state, not design**: how far module consolidation has got (25% of technique parameters composed — 242 against 694 still minted per technique), what is decided, and what is open. Read it before drafting a module. Measure `tapp/`, never `registry/`: the registries are `isTypeLibrary` and per-technique by construction, so measuring them yields a true-but-meaningless 87% duplication.

## Commands

All tooling is `python tools/<name>.py`. There is no build system and no pytest suite — the validation tools *are* the test suite. Dependencies ARE pinned, in `requirements.txt` (`pip install -r requirements.txt`), with the database driver split into `requirements-db.txt` so CI and anyone regenerating schemas does not need psycopg2. The pins are exact, not bounded, because the output of these tools is committed and diffed: PyYAML's line-wrapping changed between versions and reflowed 2764 lines of `registry/parameterTemplates` and `registry/parameterValues` with no semantic change, twice. Do not "fix" a pin to a newer release without regenerating and confirming an empty diff. `openpyxl==3.2.0b1` is deliberately a PRE-RELEASE — it is what the committed artifacts were built with.

Regenerate after any `_sources/**/schema.yaml` edit:

```
python tools/regenerate_schema_json.py        # *Schema.json from schema.yaml (--dry-run to preview)
python tools/resolve_schema.py --all          # resolvedSchema.json everywhere (downstream validators read this)
```

`resolve_schema.py` also accepts a single `<profile>` name or `--file <schema.yaml> -o <out>` to resolve just one — far faster than `--all` after a localized edit.

> **TAPP source = the `tapp/` git submodule** ([amds-ldeo/tapp](https://github.com/amds-ldeo/tapp)); `tools/tapp_source.py:current_delivery()` resolves to it. Clone with `--recursive`, then `git submodule update --init --checkout` — the `--checkout` is REQUIRED because `.gitmodules` sets `update = none`. That setting exists to stop OGC's reusable postprocess workflow, which runs `git submodule update --recursive --remote` and then commits everything, from silently advancing the pointer to whatever is at the tip of tapp's default branch (it did exactly that in `c0194f7e4`, which broke `TAPP_CONFIGS` for 13 of 16 techniques on main). Bumping the delivery is therefore a deliberate act: check out the revision you want and `git add tapp`. CI does not need the submodule populated — nothing under `_sources/` references it and `bblocks-config.yaml` imports only CDIF's remote register. (The earlier `resolve_schema.py --all` gh-pages blocker is now **lifted** — CDIF publishes `objectReference`; it runs clean.)

The migration tools, in run order: `python tools/intake_delivery.py <delivery>` (read-only first pass — what carries, what is renamed, what arrives **DROPPED** or flagged, what composing a module would change), then `python tools/migrate_sidecar.py <tapp> --source <table> [--seed <nearest tapp>] --write` (carries a sidecar onto a new revision; record non-mechanical renames in its `ALIASES` rather than losing the authored paths), then `python tools/fill_flagged.py --write`.

`TAPPS20260811/` and `TAPPS20260813/` at the repo root are **earlier inline drops**, not the source: `tapp_source.current_delivery()` prefers the `tapp/` submodule and only falls back to them. An unrecursed clone will silently build from the old drop — check the submodule is initialised before believing a regen.

Validate ("run the tests"):

```
python tools/validate_examples.py                 # validate all example*.json vs resolvedSchema.json
python tools/validate_examples.py --filter <name> # single BB/example — the "run one test" form
python tools/validate_instance.py --dir <dir>     # profile-aware (auto-detects dcterms:conformsTo)
python tools/audit_building_blocks.py             # completeness, schema<->JSON consistency, resolvedSchema freshness, SHACL
python tools/check_componentType.py               # componentType vocab/enum drift (annotation-only base layer, so JSON Schema alone misses it)
python tools/constraint_census.py                 # did a regeneration LOSE a constraint? (validate_examples cannot see that)
python tools/validate_counterexamples.py           # do instances that MUST fail still fail? (the other half)
```

`resolve_schema.py` REFUSES to write a schema whose refs did not resolve, and exits 1 naming each
one and its JSON path. `--allow-unresolved` writes anyway, leaving placeholders where the content
should be; reach for it only to get past a known-broken ref deliberately. The check exists because
`validate_examples` reads `resolvedSchema.json`, so a schema quietly missing a branch makes the
examples that should have failed pass instead — and because a transient file-read error in an
earlier stage would otherwise become a permanently degraded artifact on the next run.

**`constraint_census.py` answers the question `validate_examples` structurally cannot.** A
schema is a set of restrictions, so deleting one makes it more PERMISSIVE and every instance that
validated still validates — no corpus of positive examples can detect a loss, however large. The
census counts the constraints themselves (`required` names, `enum` members, `const`, `$ref`
targets, closed objects, branch counts — 1,299,304 of them across 242 blocks) and compares the
counts to `docs/constraint_census.json`. Counts give magnitude and direction; a per-block digest
catches a SWAP that leaves counts equal, which a count alone cannot see.

It is NOT a stage of `regenerate.py`, deliberately — a baseline rewritten on every run agrees with
whatever just happened and records nothing, the same reasoning as `docs/modules/emitted.json`. A
deliberate constraint change is therefore two steps: regenerate, then `--write` and commit the
manifest in the same PR, where the diff shows which constraints moved. Array indices are elided
from its pointers, so `allOf`/`anyOf` reordering does not register (branch order carries no
meaning, and the upstream postprocess is known to reorder lists —
opengeospatial/bblocks-postprocess#91). It runs as a step of `check-schema-drift.yml`, after
regeneration, rather than as its own required check.

**`validate_counterexamples.py` is the other half, and the two catch different bugs.** The census
sees a constraint disappear from the SCHEMA. This sees a constraint that is still there but no
longer BITES — a conditional whose `if` stopped matching, a branch moved into an `anyOf` where it
constrains nothing, a `$ref` that now resolves somewhere more permissive. 13 cases in
`docs/counterexamples.json`, each a single MUTATION of a real example (`remove`/`set`/`add` at a
JSON pointer) which must be REJECTED.

Three properties are deliberate. The mutation is applied to the LIVE example rather than stored as
an invalid document, because examples are regenerated and a stored counterexample drifts out of
shape and starts failing for an unrelated reason — which still looks like a pass. `expect` is
mandatory: the rejection must mention the named thing, or the case is reported as
failing-for-the-wrong-reason, since a case that fails for the wrong reason tells you nothing about
the constraint it was written for. And a pointer that no longer resolves is a HARD FAILURE, never
a skip — a silently skipped case is lost coverage, which is the exact failure mode the file
exists to prevent. All three are verified: dropping `schema:name` from 48 `required` lists turns
`tappdef-requires-name` red.

Render the human-readable pages (dataset record + TAPP definition, into `build/htmlViews/`):

```
python tools/build_html_views.py --source examples --all    # the 97 schema examples
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

## CI: four workflows, three of them required

| workflow | check name | trigger |
|---|---|---|
| `validate-branch.yml` | `Validate and annotate (no pages)` | push (not main), PR |
| `check-schema-drift.yml` | `Regenerate and diff` | every PR |
| `check-determinism.yml` | `Regenerate twice and compare` | every PR |
| `process-bblocks.yml` | — | push to main |

The first three are **required** in branch protection. Two rules follow from that and both were
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

`build/` IS committed, and `deploy-viewer.yml` depends on that: it checks main out, reads
`build/register.json` and `build/tests/report.json`, and uploads the tree to Pages **without
regenerating them**. So build output cannot just stop being committed.

But branch protection declines a push from the postprocess (`GH006 ... 3 of 3 required status
checks are expected`), and it cannot be exempted: the GitHub Actions app can only be a bypass
actor on an **organization** ruleset, and a repository ruleset rejects it outright, accepting only
deploy-key and repository-role bypasses — GITHUB_TOKEN is neither. So `process-bblocks.yml`:

1. closes any superseded build PR, then force-resets **`bblocks-build`** to main;
2. runs the reusable postprocess with `ref: bblocks-build`, so its commit lands there;
3. opens a PR from that branch using **`BBLOCKS_PR_TOKEN`** and arms auto-merge.

The PAT (Contents:read + PullRequests:write, this repo only) exists for ONE reason: a PR opened by
GITHUB_TOKEN would get no checks, per the rule above, and would sit open forever. It grants no
bypass — the build PR merges through the same three checks as anything else.

- **`bblocks-build` is machine-owned.** It is force-reset on every run. Never branch from it,
  never commit to it, never base work on it.
- **A loop-breaker guards step 1**: the run is skipped when its triggering commit message starts
  `Building blocks postprocessing`. Without it, merging the build PR starts the workflow again.
  It also bounds the damage if OGC's postprocess ever stops being deterministic — our determinism
  check covers OUR generators, not theirs.
- `deploy-viewer.yml` therefore also triggers on `push` to main under `paths: build/**`. The
  postprocess run that OPENS the build PR finishes before it merges, and the run after the merge
  is skipped by the loop-breaker (so concludes `skipped`, never `success`) — without the push
  trigger Pages would sit permanently one change behind. A `paths:` filter is safe here only
  because this is a deploy, not a required check.
- `validate-branch.yml`'s dedupe guard carries a third clause for `bblocks-build`. The guard skips
  the `pull_request` run for same-repo PRs and relies on the push run; the build commit is made by
  GITHUB_TOKEN, so no push run exists, and without the clause `Validate and annotate` would never
  report on the build PR.

## Source vs generated

**`_sources/` is NOT "the source" and `build/` is NOT "the generated output".** That two-way
split was stated here until 2026-10-07 and it is wrong in the direction that causes damage: most
of `_sources/` is generated, and reading it as hand-authored invites editing a file that the next
regeneration overwrites. The question a label has to answer is **"if this is wrong, do I edit it
or fix a generator?"** — so the taxonomy is by WHAT WRITES IT, measured, not by directory:

| path | 242 `schema.yaml` | written by |
|---|---|---|
| `techniqueProfile/geochemProfile/*/tapp/` | 59 | `build_tapp` + `build_pathdriven` |
| `techniqueProfile/geochemProfile/*/detail/` | 59 | `build_pathdriven` |
| `techniqueProfile/geochemProfile/*/profile/` | 29 | `build_profile` |
| `BaseSchema/modules/*/` | 16 | `build_module_bb` |
| `registry/*/` | 6 | `build_tapp` |
| `BaseSchema/*` (non-module) | 18 | **nobody — edit directly** |
| `techniqueProfile/adaProfile/*/` | 45 | **nobody — edit directly** (`generate_profiles.py` is deprecated and refuses to run) |
| `techniqueProfile/geochemProfile/*/profile-ada/` | 9 | unclear — see the caveat below |
| `techniqueProfile/geochemProfile/*/detail-legacy/` | 1 | unclear |

So ~169 of 242 `schema.yaml` under `_sources/` are generated. The same applies to everything
beside them: all 242 `resolvedSchema.json` (`resolve_schema.py`), all 242 `<name>Schema.json`
(`regenerate_schema_json.py`), and the generated `example*.json` (`build_tapp_examples` — but see
the three categories of example below, because the static and source-derived ones are NOT
regenerated).

`build/` is genuinely generated, by the OGC postprocess — and it is **committed**, because
`deploy-viewer.yml` reads `build/register.json` and `build/tests/report.json` out of main and
publishes them without regenerating. The one part not committed is `build/htmlViews/`.

> **Two stale counts, flagged rather than silently rewritten.** The Composition-modules section
> below says `_tapp_lib.py` generates "the 16 under `geochemProfile/`" and that "the 32 under
> `adaProfile/`" are hand-maintained. Measured 2026-10-07: there are **9** `profile-ada` schemas
> under `geochemProfile/` and **45** under `adaProfile/`, and `_tapp_lib.TAPP_PROFILES` holds
> **2** entries, not 16. `write_profile_ada_companions` demonstrably writes the four companion
> files; which `profile-ada` SCHEMAS any generator owns was not established. Establish it before
> relying on either number, and do not assume a `profile-ada` schema is regenerated.

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

**Not every source file has a generator.** `profile-ada/` schemas split by whether the technique
has a TAPP: `_tapp_lib.py` generates the 16 under `geochemProfile/`, while the 32 under
`adaProfile/` are hand-maintained — `generate_profiles.py` knows them but is deprecated and refuses
to run (it emits the old object-form `ada:componentType`), so nothing regenerates those files. Edit
them directly, and expect no regeneration to correct a mistake: `adaProfile/QRIS` named a detail
block in its description and referenced it nowhere for as long as the file existed, because no
generator run would ever have noticed (fixed 2026-09-05, `1db480deb`).

**"detail" means two different things, and they compose at different nodes.** A dataset-root
detail block overlays `schema:Dataset` and belongs as a top-level `allOf` entry beside the base
product; a hasPart-item block pins `ada:componentType`, describes a data component, and belongs as
an `anyOf` branch on `schema:distribution.hasPart`. `agents.md` has the authoritative split and the
grep that re-derives it — the two kinds do **not** follow the `adaProfile` / `geochemProfile`
grouping, so do not infer placement from the directory.

Measure before relocating one of these `$ref`s. Moving the twelve `adaProfile` hasPart-item blocks
to the top level was tried on a copy on 2026-09-05 and failed **all 218** records of the affected
profiles on a missing `ada:componentType` — the reasoning that motivated it (EPMA's description
says "Dataset-level analysis-instance detail ... on the schema:Dataset root") generalised from the
wrong family.

This mismatch is the NORM, not four exceptions. Measured 2026-10-06, after this paragraph claimed
TEM, XCT, SEM-FIBSEM and SEM-Imaging were the only inconsistent ones:

  29 of 29  `profile/` schemas compose `../detail/schema.yaml` as a top-level `allOf` entry,
            i.e. on the `schema:Dataset` root
  47 of 59  detail blocks describe themselves as "Detail block for <TECH> hasPart items"
   0 of 59  detail blocks CONSTRAIN `ada:componentType` anywhere — in XCT's it appears only in
            its own description, and EPMA's does not mention it at all
  29 of 29  `profile/` descriptions say they constrain "valid component types on
            schema:distribution.hasPart", and NONE of them constrains `schema:hasPart` at all —
            in XCT's profile the word appears once, in that sentence
   0 of 59  detail blocks constrain anything at the hasPart level either, so nothing in a
            technique profile reaches a component. The sealed componentType enums live in the
            base file-type BBs (image, imageMap, tabularData, …), which is layer 1 above

**The composition is right and the DESCRIPTIONS are wrong — not the other way round.** A technique's
detail must apply to a monolithic dataset, one reconstructed volume with no `hasPart` collection, as
well as to a component collection. Dataset-root composition covers both; pinning
`ada:componentType` would break the monolithic case outright, because there is no hasPart item to
carry it. So `0 of 59` is the correct design, and the 47 descriptions that call themselves
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

Reproduce
with: parse each `profile/schema.yaml`, check whether any `allOf` entry `$ref`s `../detail/schema.yaml`;
then dump each `detail/schema.yaml` with its `description` and `title` removed and grep for
`componentType`. Do NOT grep the file whole — the description says the word, which is exactly how
this went unnoticed.

The consequence is scope, not failure: a `$Dataset.schema:distribution…` path in a detail block
constrains EVERY distribution item of a conforming dataset rather than only the components whose
`ada:componentType` the block names. Nothing is invalid today, because no record exercises the
narrowing that was never built.

Measure before relocating any of it. The twelve `adaProfile` hasPart-item blocks were moved to the
top level on a copy on 2026-09-05 and failed all 218 records of the affected profiles; the reverse
move is equally capable of surprising, and it would now touch 47 blocks rather than four.

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

**A `schema:step` selector literal is sentence-case** — `'Data reduction'`, `'Sample preparation'`,
`'Data acquisition'`, `'Sample digestion'`, `'Ion milling'`. The literal IS the node's identity, so
Title Case builds a second, separate step: eight such rows made a technique row read as diverging
from the module that placed it identically.

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
                 Describe these as source-derived, and name the source; "hand-authored" implies a
                 person edited the JSON, which is not what happened.

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

## componentType architecture (source of truth: spreadsheet)

`ada:componentType` is a **string** on each archive `hasPart` item, classifying the file (e.g. `ada:EPMAImageMap`). Two layers of constraint apply via `allOf`:

1. **Base BB enums.** Each file-type BB (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of allowed componentType strings — derived from the **Components worksheet** of `C:\GithubC\amds-ldeo\metadata\ADA-AnalyticalMethodsAndAttributes.xlsx`. This enforces that `ada:EPMAImageMap` only validates on parts whose `@type` includes `ada:imageMap`. The cached mapping lives at `tools/componentType_enum_cache.json` and is applied via `python tools/apply_componentType_enums.py`. Run with `--refresh --xlsx PATH` after editing the spreadsheet.

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

### The collector: a string, a table, and the N=1 fallback (E1)

`schema:instrument.schema:hasPart[additionalType 'Collector']` carries two properties, defined on
the **instrument** building block so every technique with a Collector part inherits them. They come
from our instrument representation, not from a delivered TAPP table — Ruolin's E1 answer says so
explicitly — which is why they are not generated from a sidecar row.

  `ada:collectorConfiguration`  the assignment as the SOURCE states it, free text
  `ada:collectors`              the collector table, `schema:name` the referenceable label

They are not the same information twice: the string is the claim, the table is the reading of it.

**The table follows Decision 6 (`TAPP-keyed-values-design.md` §1.1), not a second fallback shape.**
"Rather than admit two shapes, always emit the table: a declaration that does not parse into members
yields a one-row table whose row key is the text as written. The fallback is then not a separate
branch but N=1." So: one member per position when the string parses; ONE member carrying the text
when it does not, with the source fields riding in `schema:additionalProperty` as name/value pairs.
A consumer reads one shape either way. Parsing these strings to individual collectors is not
tractable in general — they are written for a person — so **N=1 is the expected case**.

**An N=1 member names no cup, so it makes no per-cup claim.** That is deliberate and load-bearing:
the resistor values are attested per MASS (`Proposal_Monitored_Property_2026-09-10` §10), and a
fallback that quietly moved them onto the collector axis would undo the withdrawal §10 argued for.

**`ada:collectorConfiguration` is NOT a keyed table, and was until 2026-09-27.** It was registered in
`KEYED_TABLES` as the monitored-property column array itself, which made one property the container
for eight unrelated items — each emitted as a `PropertyValueSpecification` column with a pinned
`schema:valueName` — while its own sidecar row declared it `Text (free)`. Declared type and emitted
shape contradicted each other from the start. The seven other items are now ordinary
`schema:additionalProperty` entries on the Collector, `@type` `schema:PropertyValue`: a column
DEFINITION specifies, a property on a part RECORDS.

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
- **A conditional whose `if` is too broad fires on things it was never meant to pin.**
  `geochemProduct`'s TAPP conditional keyed on `@type` containing `ada:TAPPDefinition` alone, so it
  held every `{@id, @type}` *reference* to the whole TAPP schema and failed it on the four
  properties a reference does not carry. Guarding the `if` with `schema:name` separates inline plan
  from reference. The mirror-image failure is the same conditional being too NARROW: a mis-named
  workflow step matches no `if`, so its constraints are silently absent and the record validates
  clean. Whenever you add an `if`, ask what it matches that you did not intend AND what it now fails
  to match.
- **A generated node that is complete by construction must be emitted AFTER the fill passes.**
  `build_profile._name_procedure()` writes the `prov:used` TAPP reference — `{@id, @type}` and
  nothing else. Run before `_fill_required()`, the sentinel and typing passes could not tell it
  from an object they were meant to finish and padded `schema:instrument: "missing"` plus four
  `{"@id": "nil:missing"}` members into its `@type`, failing 58 of 97 examples.

The propagate-schema command runs all of these as part of its consistency audit; if you're working outside that pipeline, run them by hand on touched paths.
