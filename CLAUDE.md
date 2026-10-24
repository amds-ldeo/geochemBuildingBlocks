# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repo is the ADA (Astromat Data Archive) building-blocks repo — modular JSON-Schema building blocks (OGC Building Blocks pattern) for geochemistry analytical-technique metadata, extending shared CDIF base schemas. It is one node in a larger CDIF-rooted ecosystem; sibling repos and the propagation pipeline are documented in auto-memory.

## Deeper references

- **`agents.md`** (lowercase — that is the tracked filename) — the authoritative, detailed agent guide (directory layout, every tool, the TAPP/detail/profile pipeline internals, the full componentType architecture). Read it when this file's summary isn't enough.
- **`README.md`** — human-facing overview; its generation-pipeline section is a good orientation.
- **`docs/TAPP-schema-generation-workflow.md`** — end-to-end walkthrough of workbook → validated schema.
- **`docs/SCHEMA_PATH_GRAMMAR.md`** — the canonical grammar for the schema-path sidecars.
- **`docs/SILENT_SUCCESS.md`** — thirteen incidents in which a check, a generator or a workflow reported success while not doing its job, each with what exposed it and the rule that follows. The validator passing while content vanishes, a generator whose output varies per process, auto-merge walking past a red non-required check, a required check that can never run, a deploy that skipped the event it was given a trigger for, a pipeline silently substituting a superseded TAPP delivery for the one it was pinned to, and a whole check suite structurally unable to observe one direction of a change — a relaxation whose loss makes the schema STRICTER, so the examples, the counterexamples and the census were each blind to it for a different reason; an audit that printed its own failure count and exited 0 while nothing in CI ran it at all; a conformance sidecar listing plausible componentTypes that matched no record, because the only consumer that could tell lives in another repository; a Pages deploy that cancelled itself on every build-PR merge, both of its runs concluding non-red; and a merged change whose JUSTIFYING RECORD COUNT was measured against the wrong resolution route — counted by profile directory rather than by the cid records resolve to, so the figure described nothing, and no check could see it because the change itself was correct; and a generator change that destroyed 257,052 constraints across 161 blocks while every example gate stayed green, whose detector had already exited 1 and been read as paperwork. Read it before changing a check, a trigger, a required-status-check set or a source-resolution fallback, before combining two sources in a generator, and whenever you loosen a constraint: ask which direction of change each check can see, measure coverage per RECORD rather than per aggregate, resolve by cid rather than by directory — and, for any check, run it and read `$?`.
- **`docs/README.md`** — what is in `docs/`: the sidecar format, its five `Source` values, and the maintenance tools around it. Note **"sidecar" is overloaded**: in `docs/` it means the `*.schemapaths.csv` files, while `<block>/conformance.json` is the unrelated conformance sidecar — see "Conformance sidecars" below.
- **`docs/modules/MODULE_CONSOLIDATION_STATUS.md`** — **state, not design**: how far module consolidation has got, what is decided, and what is open. Its own figure is **73% composed** (651 against 231 still minted per technique) after the 2026-09-02 delivery, not the 25% this pointer claimed until 2026-10-18 — and even the 73% predates the 2026-10-01 manifest, so re-measure before quoting either. Read it before drafting a module. Measure `tapp/`, never `registry/`: the registries are `isTypeLibrary` and per-technique by construction, so measuring them yields a true-but-meaningless 87% duplication.

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

**The audit is baselined, and it gates.** Until 2026-10-16 it printed
`Summary: 246 passed, 5 failed` and exited **0**, and no workflow ran it — a failure report nothing
could act on (`docs/SILENT_SUCCESS.md` #9). It now exits 1 on any issue not recorded in
`docs/audit_baseline.json`, and runs as a step of `check-schema-drift.yml`.

The 5 accepted failures are the legacy `profile-ada` blocks for QRIS, RAMAN, VNMIR, XANES and XRD,
each on `No example files found`. Nothing regenerates a `profile-ada` block, so those examples have
to be authored or the blocks retired — and retirement is blocked on ADA-side record migration, not
on schema work. Making the audit fatal outright would have built a check that can never pass.

Three things to know before touching it:

- **A deliberate change is two steps, as with the census**: fix or accept, then `--write` and commit
  `docs/audit_baseline.json` in the same PR, where the diff shows which block moved. Clearing debt
  is also a baseline change — a resolved issue left in the manifest keeps absorbing the next
  regression at that block, so a full run fails until it is removed.
- **The baseline records which `--checks` wrote it.** CI runs
  `--checks files,schema-json,shacl,coverage`: measured on `a1cb6fbdb8`, that subset and the full
  six-check audit report the SAME five failures and both exit 0 against the baseline, the subset
  takes 13.6s against the full audit's 11m25s, and the two omitted checks each duplicate a
  stricter check that already runs
  (`resolved` compares only top-level property keys, where `Regenerate and diff` byte-diffs a full
  nine-stage regeneration; `examples` is `validate_examples.py`, run by `check-examples.yml`). A run
  narrower than its manifest says so and declines to call anything resolved.
- **A vocabulary `@id` collision is fatal and NOT baselineable**; `--write` refuses it.

`resolve_schema.py` REFUSES to write a schema whose refs did not resolve, and exits 1 naming each
one and its JSON path. `--allow-unresolved` writes anyway, leaving placeholders where the content
should be; reach for it only to get past a known-broken ref deliberately. The check exists because
`validate_examples` reads `resolvedSchema.json`, so a schema quietly missing a branch makes the
examples that should have failed pass instead — and because a transient file-read error in an
earlier stage would otherwise become a permanently degraded artifact on the next run.

**Two ways a vendored upstream schema stays stale through a `--refresh-remote`.** `vendor/remote/`
plus `vendor/remote-lock.json` pin every remote `$ref` so a build cannot absorb an upstream change
unannounced, and `--refresh-remote` is the deliberate act of taking one. Neither link below is a
defect in that design; both are consequences of it that present as "the refresh did not work", and
both cost a wrong conclusion on 2026-10-22.

- **The flag re-fetches what is reached by a URL, and a relative `$ref` inside the vendored tree is
  not.** `_fetch_relative_in_cache` converts a cache path back to a URL **only when the file is
  absent**; an existing one is read off disk, so the URL is never visited and the pinned copy is
  served however many times the flag is passed. `provProperties/generatedBy` is reached exactly
  that way — `../../provProperties/generatedBy/schema.yaml` from each `cdifProfile` file — so it
  had a lock entry, a correct digest, and stale content. Force the miss: delete the vendored file,
  then re-run with `--refresh-remote`.
- **Refreshing and resolving are two jobs even in one command.** `--all` re-resolves every block and
  compares bytes, so `already current` is truthful — but it is a statement about the inputs that run
  actually had. A run that resolved while the vendored copy was still stale reports every dependent
  block current, correctly, and 24 of them did. Once the vendored file really changes, run
  `resolve_schema.py --all` AGAIN before believing any count: the second pass is what carried the
  new base into all 34 profile blocks and took `validate_examples` to 657/657.

**`constraint_census.py` answers the question `validate_examples` structurally cannot.** A
schema is a set of restrictions, so deleting one makes it more PERMISSIVE and every instance that
validated still validates — no corpus of positive examples can detect a loss, however large. The
census counts the constraints themselves (`required` names, `enum` members, `const`, `$ref`
targets, closed objects, branch counts — 1,459,863 of them across 251 blocks) and compares the
counts to `docs/constraint_census.json`. Counts give magnitude and direction; a per-block digest
catches a SWAP that leaves counts equal, which a count alone cannot see.

It is NOT a stage of `regenerate.py`, deliberately — a baseline rewritten on every run agrees with
whatever just happened and records nothing, the same reasoning as `docs/modules/emitted.json`. A
deliberate constraint change is therefore two steps: regenerate, then `--write` and commit the
manifest in the same PR, where the diff shows which constraints moved. Array indices are elided
from its pointers, so `allOf`/`anyOf` reordering does not register (branch order carries no
meaning, and the upstream postprocess is known to reorder lists —
opengeospatial/bblocks-postprocess#91). It runs as a step of `check-schema-drift.yml`, after
regeneration, rather than as its own required check. `validate_counterexamples.py` and
`audit_building_blocks.py` are steps of the same job, for the same reason: a new required context is
the thing that sits pending forever, and none of the three needs a separate signal. That job is
required; `Check examples validate` is not, and a red non-required check does not delay auto-merge
at all.

**`validate_counterexamples.py` is the other half, and the two catch different bugs.** The census
sees a constraint disappear from the SCHEMA. This sees a constraint that is still there but no
longer BITES — a conditional whose `if` stopped matching, a branch moved into an `anyOf` where it
constrains nothing, a `$ref` that now resolves somewhere more permissive. 26 cases in
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

Regenerate the conformance sidecars after any change to a profile's componentTypes, its cid, or
`TAPP_CONFIGS` — they are committed and `Regenerate and diff` will catch a stale one:

```
python tools/build_conformance_sidecars.py            # dry run; prints UNION and SKIP lines
python tools/build_conformance_sidecars.py --write    # 71 conformance.json
```

Render the human-readable pages (dataset record + TAPP definition, into `build/htmlViews/`):

```
python tools/build_html_views.py --source examples --all    # the 648 committed examples
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

**`Validate committed examples` became required on 2026-10-16**, and for eight days before that
it was not. It is the check written to close #63's gap — a schema requiring a property no example
carried, merged green because nothing validated an example — and an unrequired gate is one
auto-merge merges straight past when red, which is how #31 and #32 landed broken. Requiring it was
gated on the ordering rule below, verified first rather than assumed: no `paths:` filter, no
job-level `if:`, zero skipped runs in its last 40, and it reports on the `bblocks-build` PR
without needing `validate-branch.yml`'s third guard clause (that clause carves an exception out of
a dedupe guard, and there is no guard here). `docs/SILENT_SUCCESS.md` §4 carries the measurement.

The PATCH used the `checks` form rather than the legacy `contexts` array, because each existing
context is pinned to `app_id: 15368` (GitHub Actions) and a `contexts`-only write drops that
pinning, letting any app satisfy the check.

**`Regenerate and diff` regenerates all nine stages, not the last two.** Until 2026-10-16 it ran
only `resolve_schema.py --all` and `regenerate_schema_json.py`, so it re-derived
`resolvedSchema.json` and `*Schema.json` from `schema.yaml` and stopped — while ~178 of the 251
`schema.yaml` are themselves generated from the TAPP tables and the sidecars. A sidecar edit
committed without regenerating, or a schema built from a superseded delivery, passed every check in
the repository. Enabling it was gated on a measurement, not an assumption: a full `regenerate.py`
over clean `main` (`752a236a7b`) changes **zero** files, so the comparison is meaningful rather than
permanently red. It costs ~17 minutes against the previous ~5, which does not move total PR wall
clock because `Validate and annotate` already takes 16–22 in parallel.

The STEM/EBSD caveat below still stands and is NOT contradicted by that zero: the content loss
belongs to the per-technique `regenerate.py --tapp <ONE>` path, which this job does not use.

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

`build/` IS committed, and `deploy-viewer.yml` depends on that: it checks main out, reads
`build/register.json` and `build/tests/report.json`, and uploads the tree to Pages **without
regenerating them**. So build output cannot just stop being committed.

But branch protection declines a push from the postprocess (`GH006 ... 3 of 3 required status
checks are expected` — quoted as observed; that number is the size of the required set, so it
reads `4 of 4` since `Validate committed examples` was required on 2026-10-16), and it cannot be
exempted: the GitHub Actions app can only be a bypass
actor on an **organization** ruleset, and a repository ruleset rejects it outright, accepting only
deploy-key and repository-role bypasses — GITHUB_TOKEN is neither. So `process-bblocks.yml`:

1. closes any superseded build PR, then force-resets **`bblocks-build`** to main;
2. runs the reusable postprocess with `ref: bblocks-build`, so its commit lands there;
3. opens a PR from that branch using **`BBLOCKS_PR_TOKEN`** and arms auto-merge.

The PAT (Contents:read + PullRequests:write, this repo only) exists for ONE reason: a PR opened by
GITHUB_TOKEN would get no checks, per the rule above, and would sit open forever. It grants no
bypass — the build PR merges through the same required checks as anything else.

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

| path | 251 `schema.yaml` | written by |
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

So ~178 of 251 `schema.yaml` under `_sources/` are generated. The same applies to everything
beside them: all 251 `resolvedSchema.json` (`resolve_schema.py`), all 251 `<name>Schema.json`
(`regenerate_schema_json.py`), and the generated `example*.json` (`build_tapp_examples` — but see
the three categories of example below, because the static and source-derived ones are NOT
regenerated).

`build/` is genuinely generated, by the OGC postprocess — and it is **committed**, because
`deploy-viewer.yml` reads `build/register.json` and `build/tests/report.json` out of main and
publishes them without regenerating. The one part not committed is `build/htmlViews/`.

### `profile-ada` and `adaProfile` are the PRE-TAPP generation, and the goal is to retire them

No generator owns them **by history, not by mystery**: they predate the TAPP pipeline. They came
from the earlier work that generated schemas for metadata describing **SAMIS** datasets (source
material lives on Google Drive under `Astromat\metadata` and
`Astromat\SpecificationDocs\AstromatDataDeliveryMetadata`), and the intent is to supersede them
with the TAPP-based collection under `techniqueProfile/geochemProfile/<TECH>/`.
`generate_profiles.py` knows them but is deprecated and refuses to run — it emits the retired
object-form `ada:componentType` — so **nothing** regenerates these and no regeneration will ever
correct a mistake in one. `adaProfile/QRIS` named a detail block in its description and
referenced it nowhere for as long as the file existed, for exactly that reason (fixed 2026-09-05,
`1db480deb`).

Where the supersession has reached: **all 9 now have a TAPP-based `profile/`** — EPMA, SEM, TEM
and XCT already did, and QRIS, RAMAN, VNMIR, XANES and XRD were generated 2026-10-07. Nothing had
been missing but a `build_profile.PROFILES` entry; all five already had `tapp/`, `detail/` and
`component_types`, and PROFILES membership is the only gate (`regenerate.py` skips
profile-1/profile-2 for a technique with no entry). Repo-wide that takes TAPP-based `profile/`
from 29 to **34 of 59** techniques.

So every `profile-ada` under `geochemProfile/` now has a replacement, and what remains before any
of them can be retired is the record-migration question below — not schema work. The 32
`adaProfile/` technique directories are a separate and larger job.

> **`addtype` is the real decision in a PROFILES entry, and it must be answered from the corpus.**
> `addtype[0]` is written into the generated example, so a profile whose head label no record
> carries rejects its own records — which is what EPMA did by holding two acronym forms and never
> its sentence-case partner. Harvest candidates from the legacy `profile-ada`, filter to values
> that exist in adaProduct's controlled list (coining one is inventing a product type), then order
> by record count. Counted over 7446 rows of `public.json_table` on 2026-10-07, the head label is
> `X-ray diffraction` (66) not `X-ray Diffraction (XRD) Tabular` (0),
> `X-ray absorption near edge structure (XANES) spectroscopy` (245) not the Image Stack form (0),
> and `Visible, near-, and mid-infrared spectroscopy` (183) not any acronym form (0) — the
> sentence-case name every time.
>
> **Give the TAPP profile a DIFFERENT `cid` from the legacy one.** These five take `ada<TECH>`
> against the legacy `ada<TECH>Full`. Two schemas claiming one `conformsTo` URI is a fork whose
> winner is read order. **All nine `geochemProfile` techniques now comply**: SEM was corrected in
> #149 and EPMA and TEM in #157, which were the last two sharing a cid between their `profile/`
> and their `profile-ada/`.
>
> A fork is not only an ambiguity for readers, it silently breaks conformance detection.
> `build_conformance_sidecars` must emit one sidecar per DISTINCT cid, so a forked cid makes it
> keep one block and discard the other — taking that block's `ada:componentType` vocabulary with
> it. For `adaTEM` the discarded twin held 7 types that no other sidecar accepted
> (`TEMPatternsImage`, `STEMEDSCube`, `TEMEDSImageCollection`, `STEMEELSCube`, `STEMEDSTabular`,
> `STEMEELSTabular`, `STEMEDSTomo`), so 257 ADA records resolved to no technique profile at all.
> EPMA lost nothing only because its TAPP block happened to cover the same types.
>
> **Five cross-tree forks remain and are harmless**: `adaQRIS`, `adaRAMAN`, `adaVNMIR`,
> `adaXANES` and `adaXRD` are each claimed by an `adaProfile/<TECH>/profile-ada` as well as the
> `geochemProfile/<TECH>/profile`. They lose nothing, because the `geochemProfile` legacy block
> already carries `ada<TECH>Full` and its sidecar keeps the vocabulary. Judge a fork by whether
> any componentType becomes unreachable, not by the fork alone.

**These profiles are not CITED — their URI is DERIVED from record content.** Corrected
2026-10-20, and two earlier versions of this paragraph were both wrong. The first said no record
declares `dcterms:conformsTo` at all (0 of 7446), which had been measured at the record ROOT
only. The second said records "cite" these profiles and that citation and content-detection
disagree for 4,217 records. **There is no citation route at all.** The loader ASSIGNS
`schema:subjectOf.dcterms:conformsTo` from content — `record_items.py:715`,
`base_conformance_uris(...)` — so a count of that field is a count of DERIVATIONS, and a derived
field cannot preserve a stale label across a re-run. Every record carries one, 7,447 of 7,447,
at that nested path.

**35 distinct profile cids are derived.** Measured 2026-10-20 via the loader's static path:

| cid | records | holder |
|---|---|---|
| `geochemProduct`, `adaProduct` | 7,447 each | the base products |
| `adaSEMFull` | **2,918** | the LEGACY `geochemProfile/SEM/profile-ada` |
| `adaTEMFull` | **870** | the LEGACY `geochemProfile/TEM/profile-ada` |
| `adaEPMAFull` | **436** | the LEGACY `geochemProfile/EPMA/profile-ada` |
| `adaSEM`, `adaEPMA`, `adaSEMComposition`, `adaXCT`, `adaLabXCT` | **0 each** | the TAPP `profile/` blocks — reached by NO record |
| `adaXANES` 245, `adaVNMIR` 183, `adaXRD` 66 | | `adaProfile/*/profile-ada` — legacy |
| `adaLIT` 137, `adaICPMS` 112, `adaARGT` 97, `adaFTICRMS` 89, `adaLCMS`/`adaGCMS` 75 … | | all legacy |

**#149 was a SWAP, not a rename, and the records followed the BLOCK rather than the label.**
`SEM/profile` went `adaSEMFull` -> `adaSEM` and `SEM/profile-ada` took the reverse
(`ccb49db80f`, 2026-10-17); #157 un-forked EPMA and TEM the same way (`e6f2772c43`, 2026-10-18).
An earlier table here recorded `adaSEM` 2,912 / `adaTEM` 870 / `adaEPMA` 435, measured
2026-10-15 — those were CORRECT derivations against the cid assignment of that day, when each
bare `ada<TECH>` was the legacy block's label. Because the field is derived, re-derivation moved
the same records onto the `Full` labels. Do not read the old counts as a disagreement that needs
reconciling; there was never a stale citation to disagree with.

**The loader's static path and the CDIF engine DISAGREE, and that is open.** `detect_domain_
conformance` resolves these same records to the TAPP cid — verified on a real record, which
returns `adaEPMA` — because the legacy and TAPP cids share one `exclusiveGroup` and TAPP
priority 10 outranks LEGACY 3, with no fall-back. So completing the engine rollout FLIPS them,
and **the flip is a REVALIDATION, not a relabelling**: the TAPP profiles require record-side
names the legacy ones do not, and measured 2026-10-20, **1,306 of 1,306** EPMA and TEM records
FAIL against their TAPP profile — 436 of 436 and 870 of 870, zero passes. The blockers are
`ada:deadTime` (both), `ada:proceduralBlankLevel` (EPMA only), and two `schema:variableMeasured`
`contains` pins requiring variables named `Sampling Unit Name` and `Detection Limit` that NO
record carries. Do not treat the rollout as a labelling change.

**Those two are the pins the CORPUS FAILS, not the pins that exist, and the difference is two
orders of magnitude.** Measured 2026-10-23 on the resolved schemas: `EPMA/profile` pins **46**
`variableMeasured` names through `contains` and `TEM/profile` pins **50**, against **1** in each
`profile-ada` (`Sample preparation`). So the flip's constraint SURFACE is 45 and 49 newly pinned
names; the claim behind the "two" is that every other one is already satisfied by real record
content. Read as "only two pins exist" it badly understates what a flipped record must carry —
a mistake made once from this paragraph's earlier wording. Before building nil-token members,
RE-MEASURE which pins the corpus fails rather than reusing the figure: it was taken against the
schema of 2026-10-20, and building for two when the real set is larger ships records that still
fail. Derive the lists from the resolved schema, by walking every `contains` for a
`properties.schema:name.const`.

> **The resolution is a NIL TOKEN, not a relaxed constraint** (Steve, 2026-10-20). The TAPP
> workbooks are Ruolin's and the ADA corpus predates TAPP generation, so the pins stay and the
> records DECLARE the absence. The agreed token is the OGC nil reason `unknown`, written as the
> **expanded IRI, as a string**:
>
>     http://www.opengis.net/def/nil/OGC/0/unknown
>
> Expanded rather than the compact `nil:unknown` because nothing guarantees a consumer applies
> ADA's `adaJSONLD.json` context (which does bind `nil:`) before reading a scalar. `unknown`
> rather than `missing` because ADA holds no record of a value that does not exist, only of one
> no submitter sent. Where a field accepts a REFERENCE the object form `{"@id": "nil:unknown"}`
> remains correct and is already in use for `cdif:physicalDataType`; the string form is only for
> the scalar-typed fields.
>
> **No gBB constraint changes, and that is the point.** `ada:deadTime` is
> `anyOf: [{number}, {string}]` and `ada:proceduralBlankLevel` is `{type: string}`, so an IRI
> string already validates; the two FAILING `variableMeasured` `contains` pins (two of 46 and 50 —
> see the correction above) require `schema:name` ALONE, so the member must exist and be named
> exactly, with the token as its `schema:value`.
> An `{"@id": …}` OBJECT does **not** work in the scalar fields — it fails both — which is why
> the string form was chosen over the object form the question was first asked about.
>
> **The member needs FOUR properties, not three — `schema:description` is also required.**
> Corrected 2026-10-21, after the forms session tested the three-property shape this section
> first specified and found it BREAKS a record that currently validates. The requirement is
> record-side and unconditional in both generations, which is why it bites immediately rather
> than only after a flip:
>
>     EPMA/profile       /properties/schema:variableMeasured/items/allOf[0]
>     EPMA/profile-ada   /allOf[0]/allOf[4]/properties/schema:variableMeasured/items
>
> So the member is `{"@type": […], "schema:name": "<the pinned name>",
> "schema:description": "<text>", "schema:value": "<the nil IRI>"}`. Note the legacy path: a
> check of the ROOT `properties.schema:variableMeasured.items` alone finds the TAPP requirement
> and misses the legacy one, which sits two `allOf` levels down — the same top-level-only
> mistake that this file warns about for counts.
>
> **The four-property member is CONFIRMED, and there is no third blocker.** An earlier version of
> this note carried residual `dcterms:conformsTo` `contains` errors as an unresolved risk. They
> were an artifact of the trial method: patching a STORED document and revalidating skips
> `detect_and_apply`, and `conformsTo` is DERIVED, so the added members obliged a CDIF module
> that detection would have supplied. Run properly — four-property member, then detect-and-apply
> to re-derive `conformsTo`, then validate — a real EPMA record gives **0 errors** against
> `adaEPMA`. **The general rule: a trial that mutates a stored document is not a valid test of
> anything DERIVED from that document's content.** Regenerate; do not patch JSON.
>
> Still predicted rather than measured for the full 1,306 records — one record validated
> correctly is not the corpus — and that number comes from a regeneration when the flip lands.
>
> **The remaining blocker is scope, and the convention is not buildable until it resolves.**
> **The token must only go on records whose technique profile requires it** — asserting
> `ada:deadTime` on a photograph would be false — but the requiring profiles are the TAPP
> variants while records resolve to the `Full` ones, so the correct scope IS the flip decision
> above. Nothing in the corpus fails these pins today, so there is nothing to repair yet and no
> scope to build against.
>
> **Verified end-to-end, not predicted.** A real flipped EPMA record carrying the token as a
> string in both properties, and a named `variableMeasured` member carrying it in `schema:value`
> for each pin, validates against `EPMA/profile/resolvedSchema.json` with **0 errors** — measured
> by the Validation session 2026-10-20, against the schema as authored. The object form's failure
> in those same fields was confirmed independently on the same record.
>
> **`ada:analyticalMode` takes `unknown`, as a STRING, on the dataset side only** (Stephen,
> 2026-10-22). Distinct from the gated fields above and easy to conflate with them:
>
>   the mode PROPERTY     `unknown` -- every analysis HAS a mode; ADA does not record which
>   a GATED FIELD         `inapplicable` where the implied mode excludes it, else `unknown`
>
> `inapplicable` on the mode itself would assert the analysis had no mode, which is false for
> every record. The form is a string element carrying the expanded IRI, because the schema asks
> for one: `detail/` places the property with `items: {type: string}` and no enum, so a nil IRI
> validates, while `tapp/` constrains items to the technique's mode enum for the 14 gating
> techniques and a nil IRI would VIOLATE it there. That asymmetry is correct rather than an
> oversight -- a record may not know its mode, but a procedure that cannot say which modes it runs
> is not a procedure. No schema widening is needed, and the object form
> `{"@id": "nil:unknown"}` would NOT validate here.
>
> Nothing demands the value today: `ada:analyticalMode` is declared and optional everywhere, 0
> required sites repo-wide, because of the bare-`[]` requiredness defect below. **And a correct
> fix for that emits `required` AND `minItems: 1`, not `required` alone** -- `required` by itself
> is satisfied by an empty array, which asserts nothing. Measured across the `tapp` blocks, 2,135
> required array properties already carry `minItems` and 279 do not, so the pairing is the
> established convention and the 279 are the anomaly.
>
> `tools/build_mode_applicability.py` carries all of this as `mode_property` in
> `docs/mode_applicability.json`, so the loader reads it rather than re-deriving it.

> **Recorded as a deliberate trade, not a fix.** A required pin satisfied by a placeholder passes
> while conveying no measurement — the vacuous-validation shape `docs/SILENT_SUCCESS.md` and the
> `adaSubjects` work both circle. It is accepted because an explicit machine-readable `unknown`
> lets a consumer distinguish *declared absent* from *present*, which nothing can do today, and
> because the alternative was loosening authored workbooks to fit legacy data. Do not cite it as
> precedent for relaxing a TAPP constraint, and do not add a second sentinel beside it — the
> examples already carry 1,090+ `"no value available: X"` strings from the generators, and a
> third convention would make absence unreadable. The loader emits this; no gBB generator does.

Do NOT read this table as "the legacy profile owns the records" any more. Ask which block pins
the cid today — `grep -rlE "profiles/<cid>([^A-Za-z0-9]|$)" --include=schema.yaml _sources/` —
because the answer moved twice in two days. **Anchor that pattern.** An unanchored
`profiles/adaSEM` also matches `adaSEMFull`, silently merging a cid with its legacy twin, which
is exactly the distinction that matters here; a first pass without the anchor reported zero
forks repo-wide against the five that exist.

So retiring or renaming a legacy profile moves every record that derives to it, and nothing in
gBB would notice: no gBB check reads ADA records. But it does not ORPHAN them, and the earlier
wording here said it did. Because the field is derived rather than stored, a renamed cid is
simply re-derived on the next loader run — which is exactly what #149's swap did to 2,918 SEM
records without touching one of them. What a rename changes is which SCHEMA those records are
then judged against, so sequence it as: decide the cids, confirm the new target ACCEPTS the
records, then deprecate. Judge the move by validation, not by citation.

`adaTEM` and `adaEPMA` were **ambiguous** URIs until #157, each claimed by two schemas. They now
resolve to one block apiece — the TAPP `profile/` — so the ambiguity is gone, and the open
question is the one above: the loader's static path derives the `Full` cid for these records
while the CDIF engine derives the TAPP one, and the records fail the TAPP schema if flipped.

The risk compounds through a second route. The ADA loader **derives** `conformsTo` from record
CONTENT (via the CDIF validation repo's `detect_conformance`), so a record is matched to a
profile by what it carries, not by what it cites — and the matched profile's constraints then
have to accept it. That is why relocating the twelve `adaProfile` hasPart-item detail blocks to
the top level, tried on a copy on 2026-09-05, failed **all 218** records of the affected profiles
on a missing `ada:componentType`: those records never mentioned the profile, they were matched
into it. So there are TWO questions to ask before retiring a profile, and the correction above
means the first one is about DERIVATION, not citation: **"which cid does the loader derive for
these records today?"** — measured per cid at `schema:subjectOf.dcterms:conformsTo`, which is
`adaSEMFull` 2,918 and `adaSEM` **zero** — and **"what would `detect_conformance` match here
instead, and would that schema accept these records?"** Both questions are now known to have
different answers, which is the divergence recorded above.

> **One stale count nearby.** The Composition-modules section below says `_tapp_lib.py` generates
> "the 16 under `geochemProfile/`" and that "the 32 under `adaProfile/`" are hand-maintained.
> Measured 2026-10-07: **9** `profile-ada` schemas under `geochemProfile/`, **32** technique
> directories under `adaProfile/` holding **45** `schema.yaml`, and `_tapp_lib.TAPP_PROFILES`
> holds **2** entries, not 16. `write_profile_ada_companions` writes the four companion files
> beside a block; it does not generate these schemas.

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

  34 of 34  `profile/` schemas compose `../detail/schema.yaml` as a top-level `allOf` entry,
            i.e. on the `schema:Dataset` root
  49 of 61  detail blocks describe themselves as "Detail block for <TECH> hasPart items"
   0 of 61  GEOCHEMPROFILE detail blocks CONSTRAIN `ada:componentType` anywhere — in XCT's it
            appears only in its own description, and EPMA's does not mention it at all
  13 of 14  adaProfile detail blocks DO constrain it, almost all as a bare `const` — the
            asymmetry is real and load-bearing, see below
  34 of 34  `profile/` descriptions say they constrain "valid component types on
            schema:distribution.hasPart", and NONE of them constrains `schema:hasPart` at all —
            in XCT's profile the word appears once, in that sentence
   0 of 61  geochemProfile detail blocks constrain anything at the hasPart level either, so
            nothing in a technique profile reaches a component. The sealed componentType enums
            live in the base file-type BBs (image, imageMap, tabularData, …), layer 1 above

**Counts re-measured 2026-10-18** (they read 29/47/59 here until then, from 2026-10-06; the repo
has since grown to 61 techniques and 34 TAPP profiles). The `0 of` conclusion is unchanged.

**The `0 of 61` applies to `geochemProfile` ONLY, and the adaProfile row is why that matters.**
`build_conformance_sidecars` reads a profile's componentTypes from three unioned sources, and for
the legacy `adaProfile` blocks the DETAIL block is the authoritative one — its `profile-ada`
reaches components through `$ref: ../detail/schema.yaml` rather than an inline enum. Those detail
blocks pin `ada:componentType` as a bare `const`, a shape the sidecar generator did not read
until 2026-10-18, which made ICPOES, LAF, PSFD and L2MS look like profiles with nothing to
distinguish them. Reading this section as "no detail block anywhere constrains componentType" is
what hid that for weeks.

**The composition is right and the DESCRIPTIONS are wrong — not the other way round.** A technique's
detail must apply to a monolithic dataset, one reconstructed volume with no `hasPart` collection, as
well as to a component collection. Dataset-root composition covers both; pinning
`ada:componentType` would break the monolithic case outright, because there is no hasPart item to
carry it. So `0 of 61` is the correct design, and the 49 descriptions that call themselves
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

## Analytical mode and the per-field mode flags: designed upstream, UNUSABLE today

The TAPP workbooks carry a complete conditional design that gBB does not act on, and the reason
is not a missing generator — it is missing data. Measured 2026-10-21; do not re-derive it.

**What the workbooks declare.** Every workbook has mode-flag columns (`EDS Point Analysis`,
`WDS Mapping`, `SE Imaging`, `Transect`, `Electron Diffraction`, …) whose values are `Y`/`N` per
FIELD, plus an `Analytical Mode` row whose allowed content IS the set of those column headers.
Ruolin's own Purpose cell states the split: *"the procedure-level declaration of measurement
type, distinct from the mode flag columns, which state per-field applicability."* So
`EDS Dead Time` is `Y` for the two EDS modes and `N` for both WDS modes.

**What gBB does with that: nothing.** No tool reads the mode-flag columns. Consequently **284
field rows across 14 techniques have mixed `Y`/`N` applicability**, and they sit at a tier the
emitter turns into an unconditional `required` — so those properties are demanded of records the
workbook says they do not apply to. `semTAPP` alone has 84, `temTAPP` 46, `semCompositionTAPP` 30,
`epmaTAPP` 29.

**And the FIRST question is whether a technique's mode gates anything at all.** Only **14 of 61**
techniques have mode-flag columns between `Purpose` and `Literature Assessment`. For the other
**47** the `Analytical Mode` is **INFORMATIONAL**: reported on an analysis, gating no constraint.
Solution Q/SF/MC-ICP-MS are the clear case — they declare
`Solution nebulisation (continuous) | Flow injection` and no field's applicability varies between
them. Determining a mode there buys nothing, so any effort to derive one belongs to the 14.

> Corrected 2026-10-22. This section first said "213 rows across 11 workbooks", from a header
> regex written here rather than from `build_tapp.mode_columns()`, which is what the generator
> uses. That undercount missed `vnmirTAPP` and `semFibsemTAPP` entirely. Use
> `tools/infer_analytical_mode.py`, which derives both figures from that function.

**Why the conditional cannot be built, measured on the live corpus:**

| | |
|---|---|
| `ada:analyticalMode` in the 7,447 records | **0**, at the dataset root or anywhere else |
| any key containing "mode" in 111,963 `record_subjects` | **0** — there is no SOURCE field |
| `componentType` naming EDS | 502 records, all SEM/STEM/TEM |
| `componentType` naming WDS | **0** |
| EPMA records with any EDS signal in `componentType` | **0 of 436** |

So this is not "the loader does not emit a mode yet". **ADA records no acquisition mode and no
detector anywhere**, so a mode would have to be DERIVED, and for EPMA — the case that motivated
the whole exercise — there is nothing to derive it from. A conditional in any polarity leaves
those 436 records exactly as they are. **The blocker is upstream of both repositories**: ADA does
not record which detector was used. That is a question for ADA and its submitters, not a schema
change, and not a TAPP change either.

**Three anchors were tried and all three are dead.** Do not retry them:

  instrument components   `schema:instrument.schema:hasPart[].schema:additionalType` -- 0 of 7,447
                          records carry ANY instrument part. `adaInstrumentComponentType` has the
                          right terms (`EDS Detector`, `WDS Spectrometer`) and gBB's own generated
                          examples populate them (78 / 56), but gBB examples are generated from
                          workbooks and say nothing about ADA's holdings.
  instrument additionalType  present on all 7,447 and useless: ONE distinct value,
                          `nxs:base_classes/NXinstrument.html`.
  the TAPP reference      7,263 of 7,447 DO carry `prov:used` -> `{@id, @type}` typed
                          `ada:TAPPDefinition`, so the variant's real axis is referenced -- but the
                          `@id` is an opaque per-lab procedure URI and JSON Schema cannot
                          dereference it. (This also corrects an older claim that 0 records carry a
                          TAPP reference; see the note on the `schema:name` guard below.)

**What DID land, and it is worth keeping.** `$Dataset.ada:analyticalMode[]`, one row in
`docs/modules/Module_Core.schemapaths.csv` (`7b0488060e`). The procedure side already declared the
modes a procedure PERMITS; this is the analysis side declaring the mode(s) actually USED, which is
the only place a JSON Schema conditional could read. Deliberately **optional** — the tier
arithmetic gives that for free, since `require = (A == "Basic")` on a `$Dataset` path and the
Analysis tier is `Read-Only`. Census: +188, all `type`, **0 decreases**, 657 examples passing.

**If a mode is ever emitted, write the conditionals in POSITIVE polarity** (Stephen, 2026-10-21):

    dead time is NOT required by default
      if analyticalMode contains 'EDS Point Analysis' or 'EDS Mapping' -> require it

not "required by default, excused when WDS". The inverted form needs the anchor to be MANDATORY: an
absent mode fires no `if`, nothing is excused, and the requirement stands against a record whose
mode cannot be determined. Positive polarity degrades to optional when the anchor is absent, which
is the only safe direction and the general rule here — **a conditional you cannot evaluate must
degrade to optional, never to required.**

**And design it per `schema:hasPart`, not at the dataset root.** 264 records have MIXED EDS and
non-EDS parts in one distribution, so a dataset-root mode genuinely cannot describe them. That
makes the per-part reading correct rather than hypothetical — but note the three-levels rule above:
`hasPart` exists only for a collection, so the monolithic case needs the mode at the dataset root
or on the distribution, and a mixed-mode monolithic dataset is unsayable by construction.

**The interim answer for the motivating case is the nil token, not a conditional.** EPMA's 436
records carry `http://www.opengis.net/def/nil/OGC/0/unknown` for `ada:deadTime`, which these
measurements make literally true: ADA holds no record of a dead time that does not exist, only of
one nobody sent. The conditionals were an attempt to avoid the placeholder; the placeholder is the
honest answer while the information is absent.

### A related emitter defect, real and NOT fixed

`schema_path_emitter.insert()`'s bare-`[]` terminal branch returns without recording requiredness,
and `build_module_bb.py:207` excludes `is_array` from its own required list to MIRROR that
condition — so it inherited the same omission. Measured: **9 fields, 178 declarations, 0
requirements**, every one carrying a `Basic` tier, `ada:analyticalMode` and `ada:reportedProperties`
among them. `build_module_bb` also ASSIGNS its required list over `to_schema()`'s rather than
merging, which silently drops the tree's ancestor requirements the moment its own list is non-empty.

All three are genuine. **An attempt to fix them was reverted** — see `docs/SILENT_SUCCESS.md` #13 —
because the change destroyed 257,052 constraints across 161 blocks while every example gate stayed
green. Redo it one defect at a time, with `constraint_census.py` read LINE BY LINE as the primary
gate and a committed baseline between steps. The saved diff is not in the repo; re-derive from the
line references above.

## componentType architecture (source of truth: spreadsheet)

`ada:componentType` is a **string** on each archive `hasPart` item, classifying the file (e.g. `ada:EPMAImageMap`). Two layers of constraint apply via `allOf`:

1. **Base BB enums.** Each file-type BB (`image`, `imageMap`, `tabularData`, `collection`, `dataCube`, `document`, `supDocImage`, `otherFile`) declares a sealed `enum` of allowed componentType strings — derived from the **Components worksheet** of `C:\GithubC\amds-ldeo\metadata\ADA-AnalyticalMethodsAndAttributes.xlsx`. This enforces that `ada:EPMAImageMap` only validates on parts whose `@type` includes `ada:imageMap`. The cached mapping lives at `tools/componentType_enum_cache.json` and is applied via `python tools/apply_componentType_enums.py`. Run with `--refresh --xlsx PATH` after editing the spreadsheet.

2. **Profile/detail layer.** A technique profile's `schema:hasPart.items` uses a schema-level `anyOf` with three kinds of branch: (a) `$ref: '../adaProduct/schema.yaml#/$defs/universalComponentTypeBranch'` for universal componentTypes (factored from per-profile boilerplate); (b) inline `properties.ada:componentType: {type: string, enum: [...]}` for technique-specific componentTypes that have no detail block; (c) `$ref: '../detail/schema.yaml'` (the technique's own detail block) for detail-bearing componentTypes. Detail schemas pin `ada:componentType` via `anyOf: [{const: "..."}]` consts AND contribute detail-specific sibling properties (e.g. `ada:spectrometersUsed`, `ada:signalUsed`) — flat on the hasPart item, NOT nested inside componentType.

### One componentType per product kind — the instrument variant rides on the TAPP, not the type

**Decided 2026-10-16, and it reverses the obvious-looking alternative, so do not re-derive it.**
Mc/Q/Sf variants of a technique share one componentType: `ada:LAICPMSMap` is the map, whichever
mass spectrometer produced it. Minting `ada:LAICPMSMap.mc` / `.q` / `.sf` was considered and
refused. A future delivery proposing variant componentTypes should be refused on this basis
rather than measured again.

**The file-shape question is SETTLED on domain grounds, not open pending data.** Map and tabular
data files from MC, Q and SF are not going to be different — Steve, who owns the domain. An
earlier draft of this paragraph said it "cannot be answered today" because no ADA or TAPP example
carries a `cdif:hasPhysicalMapping`, which wrongly framed a known answer as a gap waiting on
evidence. Do not go collecting physical mappings to settle it.

**The variant distinction is real but PROCEDURE-side only.** The three LA workbooks genuinely
differ — 128 metadata items shared, `laMcicpms` unique in **15** (Collector Configuration, Faraday
Cup Amplifier Resistor Values, the three Double-Spike items, Baseline Measurement Approach),
`laQicpms` in 1 (Signal Collection Mode), `laSficpms` in 2 (E-scan Range, Triple Scanning Mode) —
and the MC items carry BOTH Procedure-Level and Analysis-Level tiers. That difference lives
entirely in what `tapp/` and `detail/` record, which is why three TAPPs exist. It never reaches
the file, and `ada:componentType` classifies the FILE.

So the discriminator for Mc/Q/Sf is the TAPP reference — `prov:used` → a TAPP definition naming
`laMcicpmsTAPP` — which is the axis the variant actually lives on. Note that **0 of 7,447 records
carry a TAPP reference today** (`tools/check_migration_readiness.py`), so anything deriving the
variant from record content will be unable to, correctly, until that migration lands.

**Consequences for anything detecting a profile from componentType.** 21 of the 133 componentTypes
in `build_tapp.TAPP_CONFIGS` are claimed by more than one TAPP, and they are two different problems
that a priority ranking does not solve:

| group | types | handling |
|---|---|---|
| latent ICPMS families | `ada:LAICPMSImage`/`Map`/`Tabular`/`Transect`, `ada:LAICPMSGeochronTabular`, `ada:SolutionICPMSTabular` | declare an honest TIE — ranking picks a favourite and is wrong two times in three |
| live generic types | `ada:analysisLocation` (393 records), `ada:report` (210), `ada:contextPhotography` (54), `ada:quickLook` (47) | exclude from selection — they match everything and discriminate nothing |

The ICPMS six appear in **0 of 7,447 records**; the 8 LA-ICPMS records that exist carry
`ada:LAICPMSRawTabular`, `ada:logFile` and `ada:methodDescription`, none of which collide. All 657
records carrying a generic type already name their real technique in `schema:measurementTechnique`.

> **A per-profile componentType list cannot be derived from a resolved schema.** Every profile
> `$ref`s `universalComponentTypeBranch` and the base file-type blocks, so resolution inlines the
> whole sealed set: a walk over all `profile*/resolvedSchema.json` finds 238 componentTypes with
> 225 "claimed" by ~74 profiles each. That is the universal enum, not a collision. The real
> per-technique list is `build_tapp.TAPP_CONFIGS[<tapp>]["component_types"]` — 61 entries, 134
> distinct types — which is what `build_profile` emits the hasPart branches from. This follows
> from the measured fact recorded above that 0 of 61 geochemProfile detail blocks constrain
> `ada:componentType`:
> the per-profile narrowing was never built, so there is no validation narrowing to stay in step
> with.


## Conformance sidecars — how a record is matched to a profile

`<block>/conformance.json` tells CDIF's two-stage detection engine which profile URIs a record
conforms to. **71 of them, one per DISTINCT cid**, generated by
`python tools/build_conformance_sidecars.py --write` and committed. They are the gBB half of a
contract with the ADA loader: the loader DERIVES `schema:subjectOf.dcterms:conformsTo` from
record CONTENT rather than trusting what a record claims, and these files are what it derives
from. Nothing in this repository validates against them, so a wrong sidecar is invisible here
and shows up as a mis-profiled record in ADA.

Two stages, both writing into the same `conformsTo` list:

  stage 1  `detect_cdif_conformance`   CDIF modules (core, discovery, data_description,
           provenance, manifest), read from the mBB sibling repo. **Returns a plain
           `list[str]`** — not an object. A wrapper doing `r.uris or r.declared or []` silently
           yields `[]` for a list, which is how an entire acceptance run once read as zero.
  stage 2  `detect_domain_conformance` the geochem/ada profiles, read from these sidecars.

Six fields, nothing else:

| field | meaning |
|---|---|
| `conformsTo` | the URI emitted when the record matches |
| `presence` | the SPARQL ASK deciding whether it matches, built from the block's componentTypes |
| `requires` | implication — declaring this implies declaring those |
| `exclusiveGroup` | mutual exclusion — **exactly one** member of a group is declared |
| `priority` | who wins inside a group: LEGACY 3, UMBRELLA 5, MEMBER 10, TAPP 15 |
| `validityShapes` | what to validate against once declared. **`null` in all 71 — not yet populated** |

**`requires` and `exclusiveGroup` express different relations and are not interchangeable.**
Implication relates a member to its umbrella; exclusion relates members to each other. An
umbrella sharing a group with its members can never co-occur with them, whichever way the
priorities fall — measured on `adaSEM`/`adaSEMImaging`: shared group with no `requires` gives the
member alone, shared group WITH `requires` gives the umbrella alone, and only separate groups
plus `requires` gives both. The middle case looks like a fix and is a different single winner.

**An umbrella's presence is the UNION of its family**, because the implication has to be true
rather than assumed: `adaSEM`'s own six types supersetted none of its four members, and
`adaSEMFIBSEM` shared nothing with it at all, so `requires: [adaSEM]` would have declared the
umbrella for records failing its own presence test. The union EXCLUDES anything the umbrella's
legacy twin claims, so the union cannot hand it reach against a different generation of the same
technique — without that, 5 records moved off `adaSEMFull` onto `adaSEM`, which resolves 170
required names against the legacy profile's 122.

**A SUPERSEDED legacy cid is deliberately unreachable, and that is NOT the #152 bug** (Stephen,
2026-10-21). Where a TAPP `profile/` covers the same componentTypes as its legacy `profile-ada`
twin and both sit in one `exclusiveGroup`, the legacy cid at LEGACY 3 loses to the TAPP cid at
MEMBER 10 and can never be declared — for any document at all. Measured on three pairs, whose
presence ASKs are IDENTICAL for EPMA and XCT and a 5-of-12 subset for TEM. **Keep it. That is
correct supersession**: the replacement exists, covers the same files, and should win.

**The reason this needs writing down is that it is SYMPTOM-IDENTICAL to the defect fixed in
#152.** Both present as "this profile matches no record". Ask which one you have:

  the DEFECT      the presence ASK is DISJOINT from what the records carry — the profile cannot
                  match because its vocabulary is wrong (`adaSEMFull`'s ASK accepted 6 types
                  while its own schema declared 14, with no overlap at all)
  CORRECT         the ASK matches fine, and the cid loses a PRIORITY contest inside its group to
                  a superseding profile covering the same types

A fix applied to the second case would resurrect a profile that is meant to be retired. Do not
"repair" a zero-match legacy cid without checking which of the two it is.

**The accepted consequence:** the three legacy `profile-ada` examples for EPMA, TEM and XCT each
declare the cid their own block pins and detection returns the sibling TAPP cid instead, so they
can never reproduce their own declaration. A declared-vs-detected acceptance run therefore shows
3 permanent differences (88 of 111 at the time of writing). Those 3 are expected and are not a
defect to chase.

### Where componentTypes come from, and the failure mode to know

Three sources, **unioned, never falling through**: `build_tapp.TAPP_CONFIGS[<tapp>]`, the
block's own inline enum, and the sibling `detail/` block. Three separate defects in this one
function each silently narrowed a presence ASK, and **a too-narrow ASK is invisible to every
check in the repo** — it validates, it regenerates byte-identically, it lists plausible
componentTypes, and it simply fails to match records. All three were found by the metadata forms
session measuring presence against the live corpus, not by anything here:

- the inline enum was read only when the TAPP lookup came back empty, so a legacy block keyed to
  the same technique directory took the TAPP vocabulary instead of its own. `adaSEMFull`'s ASK
  was entirely DISJOINT from the 2,912 records that derived to it (measured pre-swap, when
  `adaSEM` was that legacy block's own label; they derive to `adaSEMFull` today).
- a bare `const:` was not read at all, only `enum` and `anyOf: [{const}]`. 8 detail blocks use
  the bare form.
- the TAPP lookup was keyed off `build_profile.PROFILES` (34 techniques) rather than
  `build_tapp.TECH_DIR` (61), so a technique with a TAPP and no `PROFILES` entry — XCT — could
  not reach its own componentTypes.

With all three fixed the "no discriminating componentType" skip count is **zero**. Any earlier
figure for "profiles that describe nothing distinguishing" measured this generator, not those
profiles.

**A forked cid breaks this outright.** One sidecar per distinct cid means a cid claimed by two
blocks keeps one and DISCARDS the other's vocabulary. That is why the `ada<TECH>` /
`ada<TECH>Full` split matters beyond tidiness, and why `adaTEM` cost 257 records their profile
until #157. Judge a fork by whether a componentType becomes unreachable in all 71 sidecars, not
by the fork alone.

**Check a presence ASK per RECORD, not per profile.** Measured when `adaTEM` was still the
LEGACY block's label, it had 870 records of which 613 did carry an accepted type — so it looked
healthy in aggregate while 257 records had no overlap at all. An aggregate overlap hides exactly
the records that are broken. **Read that 870 against the label of the day, not today's**: since
#149's swap those records resolve to `adaTEMFull`, and `adaTEM` is reached by none — the same
trap as the cid table above.


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
  **Two asymmetries here are deliberate and should not be "tidied".** The superseded
  `{@id, @type: [… ada:TAPPDefinition]}` REFERENCE still validates, because 7,263 of 7,447 ADA
  records link their TAPP that way and rejecting it would invalidate the corpus before the corpus
  can move; the superseded INLINE spelling (the same `@type` plus a `schema:name`) is REJECTED,
  so the replacement is enforced rather than merely emitted. Both halves are pinned by
  counterexamples — `tappdef-inline-old-spelling-is-closed-off` fails if either the inline form
  starts validating again or the reference form starts being rejected.
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

**This checkout is used by several sessions at once.** On 2026-10-10, PR #110 regenerated 620
files in it while PR #109 was being prepared, and four separate errors followed from one habit:
reporting an inference as an observation, from state that was either shared-mutable or only
partly read. `docs/SILENT_SUCCESS.md` collects the CI-side version of this family; this is its
working-tree counterpart.

**Ask the commit, not the working tree.** Any count that will drive a commit comes from a
committed ref:

```
git grep -l '<pattern>' HEAD -- '*resolvedSchema.json'
```

Grepping the tree reported 37 stale `resolvedSchema.json`; the commit held **42**, because
another process was mid-write. The tree is shared mutable state; the commit is what CI judges.
The same applies to any filtered or `head`-truncated read — a truncated grep reported "no example
carries this" while two did.

**Never `git add <directory>`. Stage explicit paths, then assert the size before pushing:**

```
git show --name-only --format= HEAD | wc -l     # must equal the number you intended
```

`git add _sources` captured **768** files against an expected 45, 711 of them another session's
uncommitted work. The same command then silently UNDER-captured: the concurrent run overwrote the
freshly resolved artifacts before staging, so `git add` saw files identical to HEAD and dropped
them, and the commit shipped a schema change without the artifacts it required —
`Regenerate and diff` went red. **A file listed in a commit with 0 changed lines is a
contradiction**, and it is the visible symptom of that under-capture.

**Probe for contention before committing anything regenerated:**

```
find _sources tools -newermt '-5 minutes' -type f | wc -l
```

Non-zero and not yours means stop and work in an isolated tree —
`git worktree add --detach <tmp> origin/main`, apply the source edits there, regenerate, commit and
push from it. That is what finally produced a trustworthy commit, and this probe alone prevents
both failure modes above.

**"Contains" is not "changes."** To judge what a branch does, diff it against its merge base:

```
git diff --name-only $(git merge-base <branch> origin/main) <branch>
```

Old text was found in 42 files of #110's head and reported as about to revert a just-merged fix;
#110 changed none of them — zero overlap — so the merge was safe. Do the cheap confirming
measurement BEFORE reporting a risk, not after. And do not attribute causation from observation:
"files changed at 15:21" is observable, "session X did it" is an inference.

### One worktree per session, and never reuse one

Worktrees are the mechanism that makes concurrent sessions safe — separate working tree, separate
index, separate branch — and the section above exists because gBB stopped using them that way.
Measured 2026-10-19:

| repo | state |
|---|---|
| `amds-ldeo/metadata` | 5 worktrees, each the home of ONE session, branch named after the worktree. Clean. |
| this repo | 2 worktrees, which between them were the working directory of **FIVE** sessions on five different branches — `brave-nightingale-f01bf6` for three, `beautiful-merkle-8446b8` for two. Both now sit on a **detached HEAD**, which is the residue. |

A worktree is not a *place* to work, it belongs to one session. Five sessions checking out five
branches inside two trees is the shared-checkout problem with extra steps, and it is where the
counts above came from.

**Populate the submodule in every new worktree, before regenerating anything:**

```
git submodule update --init --checkout tapp
```

`.gitmodules` sets `update = none` (for the reason in the TAPP-source note above), so
`git worktree add` leaves `tapp/` EMPTY. A regeneration then builds from the stale inline
`TAPPS20260813` drop instead of the pinned delivery. `tapp_source.require_delivery()` refuses
rather than falling back silently now, but the refusal is the safety net, not the workflow — do
the `--checkout`.

**At most one session in the main checkout.** It is the one tree nothing isolates. During the
2026-10-19 emitter work six `python.exe` processes were running against it and none could be
attributed; the contention probe above is the only honest answer there.

**What a worktree does NOT isolate**, so do not assume these away:

- **Shared external state.** The `ada2` database is one store however many trees read it — a
  session refreshing its cache affects every session measuring against it.
- **Hot files at merge time.** #158 and #159 both edited CLAUDE.md and conflicted; this file is
  the likeliest conflict in the repo. The fix is sequencing the merges, not isolation.
- **`main` moving underneath a branch.** #169 was built on a base four commits old, which is
  fine, but its squash stat then reported 1428 files against the 163 the commit actually carries —
  read the commit (`git show --name-only --format= <sha>`), never the merge tool's summary.

**A quiet tree is not a finished job.** On 2026-10-19 a `regenerate.py` looked complete — writes
had stopped and all four gates passed — while it was still running, and the census then found
`PSFD/profile-ada` UNREADABLE at zero bytes, complete minutes later. Those four green gates were
read off a half-written tree. Wait for the process's own exit status AND a sustained quiet window
before believing any measurement taken from the tree.
