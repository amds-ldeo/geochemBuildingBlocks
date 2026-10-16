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

---

## The common thread

In all eight, the failure was invisible from the outside because the signal said "success". What
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

None of these needed cleverness. They needed looking at the thing itself instead of the badge on
top of it.
