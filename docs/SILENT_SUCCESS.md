# Silent success: when a system reports success without doing its job

A catalogue of real incidents in this repository, kept because they share one shape and that
shape keeps recurring: **something reported success while not doing the thing it existed to do.**
Not a crash, not a red check — a green one, covering an absence.

Every entry below cost real time to find, and in each case the only thing that found it was asking
*what actually happened* rather than reading the status label. Several were introduced while fixing
the one above them.

The practical rule, stated once: **a pass is evidence that nothing was detected, not evidence that
nothing happened.** Ask what the check would have to observe in order to fail, and whether it was
in a position to observe it.

---

## 1. The validator passes while content disappears

**Reported success:** `validate_examples.py`, 628/628 examples valid.

**Not doing its job:** a schema is a set of *restrictions*. Delete one and the schema becomes more
**permissive**, so every instance that validated before still validates. A bug that loses content
cannot fail a validator pointed at that content.

**Observed twice:**

- `Limit of Quantification (LOQ) Method` was deleted from nine ICP-MS schemas (2026-09-03) by
  running `simplify_sidecars` against module BBs that had not been rebuilt since their sidecars
  changed. Green throughout.
- Calling `build_pathdriven.py <tapp>` directly instead of through `regenerate.py` dropped the
  whole `schema:actionProcess` subtree — **74 JSON paths, −305/+85 lines** — and dropped it
  identically with the sidecar reverted to `HEAD`, which is what proves it was the invocation and
  not the input. `validate_examples` stayed at 614/26 the entire time.

**Rule:** audit a regenerated artifact for **lost JSON paths**, never for a passing count. A count
taken against a technique's own overlay is also not a count of what the technique has — composed
content arrives by `$ref`, so the question has to be asked of `resolvedSchema.json`.

---

## 2. The generator "works" but produces different output every run

**Reported success:** the generators ran clean and the schemas validated.

**Not doing its job:** generated output is supposed to be a function of its source. Two generators
made it a function of the run as well, which silently forecloses every check that regenerates and
compares — including the drift check built on top of them.

- **Python hash randomisation.** `schema_path_example_emitter` selected a collector label with
  `next((m for m in members if m and m in body), None)` over a **set**. Set iteration order varies
  per process, so the same source produced different files on different runs. Fixed by making the
  choice deterministic *and* meaningful — longest match, ties broken by sort order:
  `max(sorted(m for m in members if m and m in body), key=len, default=None)`.
- **Library formatting drift.** `build_tapp` dumped YAML at `width=100`; PyYAML's wrapping
  algorithm changed between versions and reflowed **2764 lines** of
  `registry/parameterTemplates` and `registry/parameterValues` with no semantic change, twice.
  Fixed with `width=4096`, so wrapping cannot vary, and backed by exact version pins in
  `requirements.txt`.

Two earlier instances of the same class, both fixed 2026-09-05: `build_module_bb` stamped
`date.today()` into every module `bblock.json`, and the shared registries recorded which techniques
had been regenerated **last**, because `remove_owned_blocks` + `append_defs` rewrote a technique's
entries at the end of the file.

**Rule:** a generator that varies by run date, process, or invocation order cannot be diffed, which
forecloses any CI check that regenerates and compares. `check-determinism.yml` now regenerates
under two different `PYTHONHASHSEED` values and compares — and it was verified against the known
defect, by checking out the pre-fix file and confirming the check goes red.

> Verifying a determinism fix is itself easy to get wrong. The first attempt stashed a file that
> had already been committed, so it tested the fix against itself. Redone with
> `git checkout <sha>^ -- <file>`.

---

## 3. The safeguard exists but is too slow to be used

**Reported success:** the drift check was present, configured, and passing.

**Not doing its job:** it took **59 minutes**, so in practice it was not waited for, and it could
not be made a required check. A safeguard nobody runs is documentation, not protection.

Two profiling passes, no cleverness:

| | before | after |
|---|---|---|
| `$defs` cycle test | pairwise `_has_ref_to`, **53,402,493** calls | one walk per body (`_refs_in` + `_cyclic_defs`) |
| source file parsing | one profile = 768 loads of 65 distinct files (11.8× redundant; `objectReference/schema.yaml` parsed **135** times) | parsed once, cached on path + `(mtime_ns, size)` |
| EPMA/profile resolve | 27448 ms | **3081 ms** |
| `resolve_schema.py --all` | ~62 min | **5 min 49 s** |
| CI drift job | 59 min 29 s | **3 min 37 s** |

The cache returns a `copy.deepcopy`, because the resolver rewrites refs in place as it inlines; a
shared dict would let one block's resolution mutate what the next one reads — a cache that changes
the answer is worse than no cache.

**Rule:** cheapness is a correctness property for a safeguard, because an expensive check gets
bypassed. Also: **measure before believing a speedup.** A process-pool parallelisation of the same
job was predicted at 3.5× and delivered **1.14×**; it was abandoned, and the cause was never
explained. The two boring fixes were everything.

---

## 4. The merge gate passes things it never checked

**Reported success:** auto-merge merged the pull request.

**Not doing its job:** auto-merge waits only on **required** checks. A red check that is not
required does not delay it at all.

- #31 merged with a failing determinism check, landing a broken workflow on main.
- #32 committed a source change, its manifest and its tool, but not the two generated artifacts —
  so main's drift check was red **for two days**, until #37 regenerated them.

There is a mirror-image trap in the fix. **A required check that never *runs* is not skipped, it is
pending forever**, and the pull request can never merge — including a pull request that would
remove the cause. `check-schema-drift.yml` carried a `paths:` filter, so it was silent on any PR
that touched nothing it matched. The filter had to be removed and *reporting on every PR* observed
first (#38), and only then could the check be required. Order mattered, and getting it backwards
would have deadlocked the repository against itself.

**Rule:** never put a `paths:` filter on a required workflow. A filter is safe only on something
that is not a gate — `deploy-viewer.yml` carries one for exactly that reason.

### The gate that was written to close #63's gap, and then was not required (2026-10-16)

`check-examples.yml` exists because of the gap recorded in §1's family: #63 merged a schema
requiring `ada:procedureAuthorDescription` that none of its three draft instances carried, green,
because no check in the repository validated an example. The workflow was added on 2026-10-08 to
close exactly that. Its own header anticipated the next step — "if this becomes a REQUIRED check"
— and the step was never taken.

Measured on 2026-10-16, `gh api repos/amds-ldeo/geochemBuildingBlocks/branches/main/protection`
returned `required_status_checks.contexts` of exactly three — `Validate and annotate (no pages)`,
`Regenerate twice and compare`, `Regenerate and diff` — and `gh api .../rulesets` returned `[]`,
so branch protection is the only gate and no ruleset adds to it. For eight days an example could
therefore break and auto-merge would merge straight past the red check, which is this section's
failure mode arriving a third time after #31 and #32.

**The ordering rule above was checked before acting, and it held.** `check-examples.yml` has no
`paths:` filter — deliberately, per its own comment — and no job-level `if:` guard at all, so the
`pull_request` event always runs it. Over its last 40 runs: 25 `pull_request` successes, 13 `push`
successes, 2 `push` cancellations on main by its own concurrency group, and **zero skipped**. It
reported on all five most recent pull requests.

It needs **no** equivalent of `validate-branch.yml`'s third guard clause for `bblocks-build`. That
clause exists to carve an exception out of a dedupe guard; with no guard to carve, nothing is
skipped. Confirmed directly rather than inferred: the check-runs on #143's head
(`365704ab2aeca8681fa7a1188bcdc6f46167e730`) list `Validate committed examples :: success`, and
#139 and #137 — both `bblocks-build` PRs — carry it too.

**The context to require is the JOB name, not the workflow name.** This is the trap in this
particular fix, and it is the same deadlock the rule above describes, reached by a different
route. The workflow is named `Check examples validate`; the check GitHub reports is its job,
`Validate committed examples`. All three existing required contexts are likewise job names
(`check-schema-drift.yml` is *named* "Check generated schemas are current" and reports
"Regenerate and diff"). Requiring the workflow name would add a context that no run can ever
report, which is pending forever — including on the pull request that would remove it.

**Rule:** before requiring a check, read its name from a real check-run
(`gh api repos/<owner>/<repo>/commits/<sha>/check-runs --jq '.check_runs[].name'`), never from the
`name:` at the top of the workflow file.

**Resolved the same day.** `Validate committed examples` was added to
`required_status_checks` on 2026-10-16 with the repository owner's explicit approval, taking the
required set from three to four. The PATCH used the `checks` form rather than the legacy
`contexts` array: each existing context is pinned to `app_id: 15368` (GitHub Actions), and a
`contexts`-only write drops that pinning, so any app could then satisfy the check — a quieter
version of this same section's failure, where the gate still reports but no longer attests what
it was built to attest.

The confirmation to insist on is not the API echo but a pull request. #144, which carries this
entry, had all four contexts green afterwards — including the newly required one. That is the
observation that distinguishes "required" from "required and unsatisfiable", and it is the one
the paths-filter incident did not have.

---

## 5. The publishing robot succeeds at everything except publishing

The longest chain, and the one most of it was self-inflicted while fixing #4.

**5a — the push.** Protecting main broke the OGC postprocess, which pushed `build/` straight to
main. It validated fine, reported `committed: true`, and failed on the last step:

```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: - 3 of 3 required status checks are expected.
```

(Quoted as observed. The number is the size of the required set, not a constant: it reads
`4 of 4` since §4 added `Validate committed examples` on 2026-10-16. Do not update the quote —
update this note.)

It cannot be exempted. The GitHub Actions app can only be a bypass actor on an **organization**
ruleset; a repository ruleset rejects it outright (`Actor GitHub Actions integration must be part
of the ruleset source or owner organization`) and accepts only deploy-key and repository-role
bypasses. `GITHUB_TOKEN` is neither. Nor can `build/` stop being committed: `deploy-viewer.yml`
reads `build/register.json` and `build/tests/report.json` out of main and publishes the tree
**without regenerating it**.

Resolved by routing the generated output through a pull request like any other change — see the
Continuous integration section of [../README.md](../README.md).

**5b — the checks that never start.** A pull request opened by `GITHUB_TOKEN` triggers **no
workflows**; GitHub blocks this to prevent robots triggering robots. Combined with #4's trap, the
build PR would have reported no checks and sat open forever. Confirmed from history rather than
docs: the `Building blocks postprocessing` commits on main have **no push-triggered run** against
them, only the chained `workflow_run` for deploy-viewer. Hence a fine-grained PAT used solely to
open the PR. It is also why a superseded build PR is **closed and reopened** rather than having its
head advanced — only `pull_request.opened` yields a fresh set of checks.

**5c — the permission that reads as read.** Arming auto-merge needs **Contents: write**, not read:
enabling auto-merge is a merge authorization. Scoped to read, every run failed on exactly that
line, having done everything else correctly.

**5d — the deploy that skipped the event it was added for.** A `push` trigger on `build/**` was
added to `deploy-viewer.yml` so Pages would stop lagging a change behind, but the job's `if` still
gated on `workflow_run.conclusion`, which is **null** on a push. On `9496e7c15`, the first build PR
merge, the run reported `skipped` on the very push it had just been given a trigger for:

```
push  skipped      Validate and process Building Blocks   <- loop-breaker, correct
push  skipped      Deploy custom bblocks-viewer           <- wrong
```

**Rule:** adding a trigger is half a change. Check the job-level condition admits the new event.

**5e — two runs, one shared branch.** The `stage` job force-resets `bblocks-build`, and the caller
had no concurrency group (the reusable workflow's own group covers only its own job). Two runs
raced; the newer won the branch and the older was rejected:

```
! [remote rejected] HEAD -> bblocks-build (refusing to allow a GitHub App to create or
  update workflow `.github/workflows/deploy-viewer.yml` without `workflows` permission)
```

The message does not state the rule, so it is recorded here: **`GITHUB_TOKEN` may push a branch
whose workflow files match the default branch, but not one that changes them.** The older run's
tree predated the deploy-viewer fix, so pushing it would have rolled a workflow file *backwards*.
That also explains why the other run's identical kind of push succeeded — its content matched main
exactly. It is not intermittent. There is no `workflows` key in the Actions `permissions:` block,
so not racing is the only fix.

**Also load-bearing:** a loop-breaker skips the run whose triggering commit message starts
`Building blocks postprocessing`. Without it the robot's own output, landing on main, restarts the
robot.

---

## 6. The upstream tool shuffles its own output

**Reported success:** the OGC postprocess completes green and its output is committed.

**Not doing its job:** it emits `properties[]` in **non-deterministic order**, so every run looks
like a large change that is not one. Between the two build commits `9496e7c15` and `88eedbaf6`:

- `_sources/` — **0 files changed**; `tapp` submodule and `bblocks-config.yaml` unchanged
- `build/` — **1310 files, +166607 −166607**
- 40 of 40 sampled JSON files: **order-insensitively identical**, 0 genuinely different
- `adaProduct/resolvedProperties.json`: 689 `properties[]` entries each side, **0 unique to
  either**

So each source change yields a ~1300-file build PR of noise, and the "nothing to propose" path
almost never fires. The loop-breaker keeps this noisy rather than dangerous. The reusable workflow
exposes only `before_postprocess`, no post hook, so the output cannot be normalised before its
commit step — this needs fixing upstream.

> **Two measurement errors made while establishing the above**, recorded because both are easy to
> repeat. First, a canonical-hash comparison that sorted **dict keys but not list elements**, which
> reported pure reordering as genuine content change. Second, comparing the wrong pair of commits
> — a pre-build-merge SHA whose `build/` was two days stale — which reported 40/40 files genuinely
> different. The claim only became trustworthy once the comparison was order-insensitive *and*
> between the two actual build commits.

**Rule:** before reporting a diff as content change, make the comparison insensitive to the thing
you are not asking about, and check you are comparing the two states you think you are.

---

## 7. The pipeline substitutes a superseded source and says nothing

**Reported success:** nothing failed. A regeneration would have run clean and `validate_examples`
would have reported 647/647.

**Not doing its job:** `tapp_source.current_delivery()` prefers the `tapp/` git submodule and
falls back to the newest inline `TAPPS<date>/` drop at the repo root. The fallback was *silent*,
and an empty submodule is the **normal state of a fresh clone or a fresh git worktree** —
`.gitmodules` sets `update = none`, which `--recursive` and `actions/checkout`'s
`submodules: true` both honour. So the default condition of a new checkout quietly redirected the
pipeline's source of truth to a superseded delivery.

**Observed 2026-10-15**, in a new `.claude/worktrees/` worktree on `main`, while fixing an
unrelated one-character typo in the SEM sidecar:

```
tapp/Current TAPPs/*.csv          0 files
tapp_source.current_delivery()    …/TAPPS20260813
```

Had the regen gone ahead, SEM would have been built from the wrong table and every check would
have been green — this is incident #1's mechanism, reached by a different route: building from the
wrong source only changes **content**, and a schema with less in it is more permissive, not
invalid. The module stages are where it bites hardest. `TAPPS20260813/` still ships
`Module_ArAr` and `Module_Group1`, both retired upstream, and `simplify_sidecars` **blanks** a
technique's own row when it decides a module covers the field — which is exactly how
`Limit of Quantification (LOQ) Method` was deleted from nine ICP-MS schemas in #1.

CLAUDE.md already said "an unrecursed clone will silently build from the old drop — check the
submodule is initialised before believing a regen". Documentation is not a guard: the condition
it warns about is invisible, so the warning only helps someone who already suspects it.

**Fixed** by making the fallback a refusal. `tapp_source.require_delivery()` raises
`StaleDeliveryError` when the submodule is unpopulated *and* an inline drop would be taken,
naming the drop and the exact fix; `current_delivery()` and `manifest_path()` each call it, since
each has its own independent scan. `regenerate.py` calls it in a **preflight before the first
stage**, because raising inside the subprocess that first touches the delivery would bury the
message in that stage's captured output. `ADA_ALLOW_STALE_TAPP_DROP=1` takes the old drop
deliberately, with a warning on stderr — the same shape as `resolve_schema.py --allow-unresolved`.

Two things it deliberately does **not** do. It stays silent when there is no inline drop to fall
into, because then the caller's own missing-file error names the exact table and is clearer. And
it does not touch `update = none`, which is itself load-bearing: that setting stops OGC's
postprocess running `git submodule update --remote` and **committing** a bumped pointer, as it did
in `c0194f7e4`, breaking `TAPP_CONFIGS` for 13 of 16 techniques on main.

CI is unaffected in both directions, which had to be checked rather than assumed.
`check-determinism.yml` populates the submodule explicitly (`--checkout`) and regenerates, so the
guard is inert there. The other three workflows never populate it — and none of them imports
`tapp_source` at all: `check-schema-drift.yml` runs `resolve_schema`, `regenerate_schema_json`,
`constraint_census` and `validate_counterexamples`, and `validate-branch.yml` /
`process-bblocks.yml` run only the OGC postprocess. An unpopulated submodule is normal there
*because nothing reads a TAPP table*, so there is no regeneration for the guard to stop.

**Rule:** a fallback that substitutes one source for another must say which one it took. Prefer
refusing: the defaults of a fresh checkout decide what most runs read, and a fallback reached by
default is not a fallback, it is the behaviour.

---

## 8. The check that cannot fail, because the loss makes the schema stricter

**Reported success:** `validate_examples.py` 647/647, all 17 counterexamples correctly rejected,
`constraint_census.py` reporting constraint counts that had gone *up*.

**Not doing its job:** nothing in the repository could observe the loss of #129's
`schema:name` -> `schema:identifier` substitute relaxation.

`tools/schema_path_emitter.py` holds `SUBSTITUTES` and `_require()`, and threads a `scope`
argument through `to_schema`'s recursive call sites so that **on `schema:object` only** an analysed
sample may satisfy `schema:name` with `schema:identifier`. It exists because ADA records identify
the sample by `schema:identifier` ("OREX-803031-101") and carry no separate laboratory name; for
XANES, XRD, QRIS and RAMAN (322 records) it was the only thing they failed on. The scoping is the
whole point: `schema:name` is required at ~48 other nodes where an identifier is **not** an
acceptable substitute.

Lose the `scope=k` threading — a plausible merge resolution, and what nearly happened resolving
PR #123, whose `_token_const` was inserted at the same anchor and edited adjacent lines — and
`_require` receives `scope=None`, `SUBSTITUTES.get(None)` misses, and the relaxation silently
disappears from every `detail/` and `profile/` block that composes
`BaseSchema/modules/core`'s `AnalysisIdentification`.

**Each of the three checks was structurally unable to see it, for a different reason:**

| check | why it could not fail |
|---|---|
| `validate_examples` | the loss makes the schema **stricter**; no example carried an identifier without a name, so every positive example still validated |
| `validate_counterexamples` | `sample-needs-name-or-identifier` sets the sample to a bare typed object carrying **neither**, so it is rejected whether or not the substitute is honoured — its own `why` field records that "no example carries a name without an identifier" |
| `constraint_census` | a removed `anyOf` becomes a firm `required`, so counts **rise**; the census reports magnitude and direction, and an increase reads as benign |

The losing direction was covered only by real ADA records, and **nothing in gBB reads ADA
records.** Its mirror image was covered: losing PR #123's `_token_const` is caught, because
`tools/check_additionaltype_policy.py` gates Rule A in CI. The two failure directions of one
function were not symmetric, and only one of them had a guard.

**Note the asymmetry this file keeps running into.** Entry 1 is the same arithmetic seen from the
other side: dropping a constraint only makes a schema more permissive, so no corpus of positive
examples can detect a loss. Here a constraint was *gained*, so no corpus of **negative** examples
can detect it either. A check suite needs an instance on each side of every line it means to hold,
and a line that moved because real records needed it has, by construction, no instance in a corpus
generated from workbooks.

**Fixed** by adding the missing positive instance:
`_sources/techniqueProfile/geochemProfile/XRD/detail/exampledetailXRD-identifierOnlySample.json`,
a sample carrying `schema:identifier` and no `schema:name`. It sits in the same block that
`sample-needs-name-or-identifier` mutates, so both halves of the line are in one directory.

**Measured 2026-10-16 on `143824ace1`** by reverting the `scope` threading on `to_schema`'s three
recursive call sites and rebuilding the modules stage, exactly as each counterexample was verified
by making it go red on purpose:

```
core AnalysisIdentification `then`:  required: [schema:name]      (anyOf gone)
exampledetailXRD-identifierOnlySample  FAIL  'schema:name' is a required property
exampledetailXRD-P0                    PASS   <- the control
```

Restoring the threading returns both to PASS. **That `-P0` passes in both states is the measurement
of the gap, not a side note** — the pre-existing corpus cannot tell the two generators apart, which
is precisely why nothing went red. Cite the commit when repeating this: the reverted lines shift
whenever the emitter is edited, and PR #123 edited it (five hunks, three inside `to_schema`) while
this entry was being written, without touching the signature, `scope`, `SUBSTITUTES` or `_require`.

A full nine-stage `python tools/regenerate.py` against a populated `tapp/` submodule leaves the new
example untouched — `git status --porcelain -- _sources` afterwards lists it and its
`.provenance.md` and nothing else — so it survives the regenerate-and-diff gate by measurement
rather than by the filename argument alone.

It is deliberately **not** generated. Neither generator in that directory emits an identifier-only
sample — the `-P0` emitter fills `schema:name` and `schema:identifier` from their sidecar rows —
and its filename sits outside both generators' namespaces
(`build_tapp_examples._prune()` globs `exampledetail-*.json`; `build_pathdriven` writes exactly
`exampledetailXRD-P0.json`). A `.provenance.md` beside it carries the rebuild recipe, because a
static derivative of a generated example will eventually go stale, and the sanctioned repair is to
rebuild it rather than to make it validate again by adding the name back — which would be this
same silent success, arriving a second time by the maintenance route.

**Rule:** before trusting a check suite to hold a constraint, ask which **direction** of change it
can observe. A relaxation and a tightening are different defects, and an instance that proves one
is silent about the other. When a constraint is loosened because real-world records required it,
the loosening needs a positive instance committed with it — the change that motivated it is
precisely the evidence that the existing corpus does not contain one.
## 9. The audit prints a failure count and exits 0

**Reported success:** `python tools/audit_building_blocks.py` printed
`Summary: 246 passed, 5 failed (of 251 building blocks)` and exited **0**. Measured on main at
`a1cb6fbdb8`, the whole run captured.

**Not doing its job:** two separate failures, and either alone was enough.

`main()` had no exit-code path at all. The only `sys.exit` calls in 875 lines were the two
import guards and a missing-`_sources` error; `main()` itself ended by falling off the bottom of
`print_report` and was invoked bare as `main()`. So every outcome was a success to any caller --
including a report naming five failing blocks.

And nothing called it. `grep -rn audit .github/workflows/` returned nothing across all six
workflows, so the exit code was moot everywhere it could have mattered. Six checks -- file
completeness, `schema.yaml` against `*Schema.json`, `resolvedSchema.json` freshness, example
validation, SHACL completeness, example coverage -- ran only when somebody thought to run them by
hand, into a shell that then ignored the result.

The second half had already been written down as though it were fixed. `check_vocab_identifier_collisions`
was added after the seven forked epmaTAPP vocabularies, and CLAUDE.md states it "now fails on a
repeat". It did not. It printed `FAIL  registry/vocab: N identifier collision(s)` and fell through
to the same return-less end of `main()`. The sentence described the intent and never the code, for
as long as both existed.

**Why it was not simply made fatal:** the five failures are the legacy `profile-ada` blocks for
QRIS, RAMAN, VNMIR, XANES and XRD, each on `No example files found`, confirmed against `HEAD`
rather than the shared working tree. No generator owns a `profile-ada` block -- `generate_profiles.py`
is deprecated and refuses to run -- so no regeneration will ever clear them: the examples must be
authored, or the blocks retired, and retirement is blocked on ADA-side record migration rather than
on schema work. A fatal audit would have been a check that cannot pass, which is section 4's
deadlock wearing different clothes.

**What was done instead:** the shape `constraint_census.py` already uses for the same problem.
`docs/audit_baseline.json` records the accepted failures verbatim; the audit exits 1 on any issue
the manifest does not record, and -- on a run no narrower than the manifest -- on a baselined issue
that is **gone**, so cleared debt has to leave the manifest in the same change instead of sitting
there absorbing the next regression at that block. Three details are deliberate:

- **Keyed by path, not by name.** `name` is the directory's last component, so 41 blocks are called
  `profile-ada` and the old report printed `[FAIL] profile-ada` five times with nothing to say
  which technique. Keying a baseline on that would let one block's accepted debt excuse another's
  failure.
- **Issue strings stored and compared verbatim**, so a block that keeps failing for a *different*
  reason is reported rather than absorbed -- the reasoning behind the mandatory `expect` field in
  `docs/counterexamples.json`.
- **A vocabulary `@id` collision is fatal and not baselineable.** It is a relationship between
  files, not a property of a block, and a forked `@id` is never accepted debt. `--write` says so
  and refuses to absorb it.

**And it is now run, by a required workflow.** As a step of `check-schema-drift.yml`
(`Regenerate and diff`), beside the census and the counterexamples, for the reason those are there:
no new required context, so nothing new can sit pending. Not `check-examples.yml` -- branch
protection lists exactly three contexts and that is not one of them, and section 4 is about a red
non-required check that auto-merge walks straight past.

**Verified by making it fail**, which is the only reason to believe any of the above:

| case | expected | measured |
|---|---|---|
| tree as committed | exit 0, 5 accepted | exit 0, `5 of the 5 are accepted ... 0 are not` |
| a 6th block loses its example | exit 1 | exit 1, `NEW ISSUES (1)` naming the block by path |
| a baselined block gains an example | exit 1 | exit 1, `1 baselined issue(s) RESOLVED` |
| same, but a narrower `--checks` run | exit 0, and say why | exit 0, `cannot tell a resolved issue from one it did not look for` |
| two vocabulary files, one `@id` | exit 1 | exit 1, and `--write will not accept it` |

The mutations were applied to copies outside the repository, not to `_sources` -- this checkout is
shared, and another session was writing to it during these runs.

**Rule:** a tool that prints `N failed` must exit non-zero, or state in its own output that it does
not gate. And before believing a check protects anything, `grep` the workflows for it -- then read
which contexts are *required*, not which are green.

---

## 10. The conformance sidecar that lists plausible values and matches nothing

**Reported success:** `build_conformance_sidecars.py` wrote 66 `conformance.json`, exit 0, no
warnings. Every one validated, every one regenerated byte-identically on a second run, every one
listed `ada:`-prefixed componentTypes that looked right for its technique. `Regenerate and diff`,
`Regenerate twice and compare`, `Validate committed examples`, the census, the counterexamples
and the audit were all green across the lot.

**Not doing its job:** four of those sidecars carried a `presence` ASK that could not match a
single record of the profile it described. `adaSEMFull`'s accepted 6 componentTypes while its own
schema declared 14, and the two sets were **entirely disjoint** -- so the ASK matched none of the
2,912 ADA records citing that profile.

Three separate defects in one function, each a source of componentTypes that should have
contributed and silently did not:

| defect | effect |
|---|---|
| the inline enum was read only when the TAPP lookup came back empty | a legacy block keyed to the same technique directory took the TAPP vocabulary instead of its own |
| a bare `const:` was never read, only `enum` and `anyOf: [{const}]` | 8 detail blocks pin componentType in the bare form; all 8 dropped |
| the TAPP lookup was keyed off `build_profile.PROFILES` (34 techniques) rather than `build_tapp.TECH_DIR` (61) | XCT has a TAPP and no PROFILES entry, so it could not reach its own componentTypes at all |

**Why nothing here could see it.** A presence ASK that is too NARROW does not fail anything. It
validates, it round-trips, it produces a plausible list. The one thing it does -- fail to match
records -- is invisible to this repository, because **no gBB check reads ADA records**. The
artifact and its consumer live in different repos, so "the generator ran and produced output" was
the only signal available locally, and that signal was true.

Worse, the defect manufactured its own corroborating evidence. Four legacy profile enums were
widened by hand in #149 to add `ARGTDocument`, `DSCHeatTabular`, `NanoIRBackground` and
`EAIRMSCollection`, reported as corpus-driven corrections. Every one of those terms was **already
declared** in the sibling detail block -- ARGT's since 2026-08-14 -- and invisible only because of
defect 2. The fix was aimed at the source of truth, which was right, instead of the reader, which
was wrong. Separately, PSFD was recorded as "a profile that describes no distinguishing content";
it carries `ada:PSFDTabular` in bare-const form. Every figure given for that category -- ~8, then
3, then 2 -- was measuring this generator. It is now zero.

**What exposed it:** the metadata forms session measuring each profile's `presence` against the
live corpus BEFORE wiring detection in, and reporting that the ASK was narrower than the block's
own enum -- 6 of 14, and 1 of 2. Neither number is derivable from anything in this repository.

**A fifth case needed a different question.** `adaTEM` showed the same 5-of-9 shape but was not
the same defect: a cid declared by two blocks yields one sidecar, and the generator kept the TAPP
block and discarded the legacy twin's vocabulary with it. 7 componentTypes became unreachable in
all 68 sidecars, and 257 records lost their technique profile. Checking all 69 against their own
block enum found zero narrower -- the right check for defects 1-3, and blind to this one.

**And the aggregate hid it.** The forms session's first overlap scan compared each profile
against all records declaring it. `adaTEM` has 870, of which 613 DO carry an accepted type, so it
looked healthy while 257 records had no overlap at all.

**Rules:**
- When sources are combined, UNION them; a fall-through is a silent drop the moment an earlier
  source is non-empty. The detail read in this same function was already a union, for this exact
  reason, and the line above it was not.
- Before "fixing" a source of truth, check that the READER can see what is already there.
- Judge a forked identifier by whether anything becomes unreachable, not by the fork.
- Measure coverage **per record**, never per profile. An aggregate overlap hides exactly the
  records that are broken.
- For an artifact whose only consumer is another repository, no local check can establish that it
  works. Say so, and get the consumer to measure before it depends on it.

---

## 11. The deploy that cancels itself, and neither run is red

**Reported success:** nothing red. `deploy-viewer.yml` produced two runs for the build-PR merge
commit, concluding `cancelled` and `skipped`. No required check failed, no notification fired,
`process-bblocks` was green, and main had moved on.

**Not doing its job:** Pages was never updated. It kept serving the previous commit while main
carried the new `build/` tree -- which is the only thing that workflow publishes.

```
01:45:03  skipped    workflow_run  65b1b8de9f   <- loop-breaker, by design
01:44:59  cancelled  push          65b1b8de9f   <- the real deploy, killed
01:30:38  success    workflow_run  3da5dce595   <- what Pages was still serving
```

Both triggers fire on a build-PR merge, seconds apart, into one `concurrency: {group: pages}`.
The `push` run passes the job's `if` and would deploy. The `workflow_run` run arrives next with
`conclusion == 'skipped'`, because `process-bblocks.yml`'s loop-breaker deliberately skips the
postprocess for a `Building blocks postprocessing` commit -- so its own job is skipped too. With
`cancel-in-progress: true` the second run **cancelled the real deploy on its way to doing
nothing**.

**It is deterministic, not flaky.** An ordinary merge deploys fine, because only a build-PR merge
fires both triggers at once. So it missed exactly the one commit per cycle that carries the
`build/` changes -- the only commit that needed publishing -- every cycle. Observed on
`4c2f5307fc` (#151) and again on `65b1b8de9f` (#155).

**The irony is recorded in the file itself.** The `push` trigger was added specifically so Pages
would not sit one change behind, and its comment says so at length. The concurrency group, added
for an unrelated and reasonable purpose, defeated it silently.

**What exposed it:** comparing the Pages-deployed SHA against `main`'s tip, instead of reading
the run list for red. Nothing was red.

**Rule:** `cancelled` and `skipped` are not `success`. When two triggers can fire for one commit,
work out which run actually performs the job and whether the other can pre-empt it -- and check a
deploy by what is deployed, never by the colour of the run.

---

## 12. The number that justified the change, measured against the wrong route

**Reported success:** #169 (`9e303a8814`) merged with every gate green. The census recorded the
delta -- 1,459,863 constraints to 1,459,734, 129 `required` entries removed across 101 blocks --
`validate_counterexamples` pinned the half of the relaxation that must still bite, verified both
ways, `validate_examples` was clean, and `Regenerate and diff` and `Regenerate twice and compare`
both passed. The PR body carried a measured record count as its justification: `schema:actionProcess`
"was being demanded of 725 ADA records that describe no procedure".

**Not doing its job:** the 725 was wrong, and nothing in the repository could have said so.
It was obtained by asking which PROFILES carried the requirement -- `SEM/profile`, `EPMA/profile`,
`XCT/profile` -- and then attributing records to them by technique. But since #149 swapped the
TAPP and legacy cids, ADA records resolve to the LEGACY blocks, and measured 2026-10-20
`adaSEMFull` and `adaEPMAFull` carry **zero** `actionProcess` requirements before the change,
after it, and at HEAD. **No record was ever failing on it.** The change fixed a latent schema
defect; the live corpus figure attached to it described nothing.

**Why no check could see it.** Every gate was checking the CHANGE, and the change was correct.
A census verifies that constraints moved as intended; counterexamples verify that what remains
still bites; `validate_examples` verifies instances. **None of them looks at whether the number
that motivated the work was measured against the right resolution route** -- and a correct change
with a wrong rationale leaves no failing artifact anywhere. This is the inverse of #8: there the
check could not observe the direction of change, here the checks observed it perfectly and the
defect was in the sentence next to it.

**What exposed it:** a sibling-repo session resolving profiles by `dcterms:conformsTo` cid instead
of by directory name, and reporting that three profiles still required the property. Chasing that
showed the surviving requirements were all Plan-side (behind the inline-TAPP guard that no record
triggers), and that the blocks records actually reach had never carried a record-side one.

**The rule: resolve by cid, never by directory -- for a RECORD COUNT as much as for a schema
path.** A technique's directory, its `profile/` block, and the cid its records resolve to are
three different things, and the answer moved twice in two days. Two corollaries from the same
week, both of which cost a wrong conclusion before being caught:

- **A required-name count is meaningless without its JSON path.** The same property name sits on
  the record side and inside the `prov:used` inline-plan branch, and the two read identically when
  quoted as a bare list. Counting without splitting them gave 30 where the answer that mattered
  was 10 -- and 30 was alarming enough to have argued against a correct migration.
- **Name presence in the document is not presence where the schema pins it.** `schema:propertyID`
  was "present on all 436 records" as a substring and satisfied nothing, because the question is
  always which CONTAINER carries it. Only running the validator settles this class.

## 13. The census reported a quarter-million lost constraints and I read it as paperwork

**Reported success:** every gate the session had been quoting was green. `validate_examples` 657
passed / 0 failed. `validate_counterexamples` 24/24 rejected. `audit_building_blocks` matching its
baseline with the 5 accepted failures. Six changes across three generators -- the emitter's
terminal-array requiredness, its copy in `build_module_bb`, two exclusion-list corrections, an
enum-sentinel fix and a required-list merge -- and after each regeneration the example-level
evidence said fine.

**Not doing its job:** `constraint_census.py` had been run, exited **1**, and printed

    The tree no longer matches docs/constraint_census.json.
    If every line above is intended, re-run with --write and commit the manifest in the
    same change, so the diff records which constraints moved and why.

That was read as the two-step bureaucracy for a deliberate constraint change -- "remember to
`--write` the manifest" -- and reported to the user as expected. It was not. Above that message
sat 1,584 decrease lines. The actual figures:

    net constraint change            -257,052
    blocks affected                       161
    AIVA/detail   type 1505 -> 36   required 581 -> 57   closed 190 -> 0   enum 176 -> 9

Roughly **18% of the repository's constraints destroyed**, including whole schemas very nearly
emptied, with no gate able to see it -- because removing a constraint only makes a schema more
PERMISSIVE, so every instance that validated still validated. This is the exact failure #8
describes, and the exact failure this file's own §"constraint_census answers the question
validate_examples structurally cannot" was written to prevent.

**What exposed it:** running the census and reading the lines, after the fourth consecutive wrong
hypothesis about an unrelated 89-path loss made it obvious that the example gates were not
measuring the thing that mattered. The tree was reverted; nothing was committed.

**The rules that follow, and the first is the one that was actually broken:**

- **An exit code of 1 is a finding, not a formality.** The census's "re-run with `--write`" line is
  advice about HOW to accept a change, printed after the evidence of WHAT changed. Read the
  evidence. A tool that says "the tree no longer matches" has already told you something; the
  instruction underneath is not the message.
- **The census is the PRIMARY gate for any generator change, ahead of the example gates.** It is
  the only tool in the repository that can see a constraint disappear. Read it line by line, not
  by exit status, and look specifically for DECREASES -- a correct additive change shows zero.
  The same session's next attempt showed `0` decreases and `+188`, all `type`, uniform `+2` per
  block: that is the shape to expect, against `AIVA/detail` going 1505 -> 36.
- **One defect per change, with a committed baseline between steps.** Six changes deep on an
  uncommitted tree, a bad step cannot be isolated and the only recovery is discarding all of it.
- **A passing example suite is not evidence about a generator.** 657 green examples coexisted with
  161 gutted blocks.

## The common thread

In all of them, the failure was invisible from the outside because the signal said "success". What
exposed each one:

| | what exposed it |
|---|---|
| 1 | counting emitted JSON paths, not passing examples |
| 2 | running the generator twice and diffing |
| 3 | a profiler, and distrusting a predicted speedup |
| 4 | reading which checks were *required*, not which were green |
| 5 | reading the job list of a "successful" run, step by step |
| 6 | an order-insensitive comparison between the correct two commits |
| 7 | asking what the tool resolved its input to, before trusting the run |
| 8 | asking which *direction* of change each check could observe, and reverting the code to see |
| 9 | running the tool and reading `$?`, then grepping CI for whether anything runs it |
| 10 | a downstream consumer measuring the artifact against real data before depending on it |
| 11 | comparing the deployed SHA against main's tip, instead of reading the run list for red |
| 12 | resolving by cid rather than by directory -- and asking what a *justifying* number measured |
| 13 | reading the census's DECREASE lines, instead of its exit code and the advice underneath |

None of these needed cleverness. They needed looking at the thing itself instead of the badge on
top of it.
