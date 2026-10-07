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

---

## 5. The publishing robot succeeds at everything except publishing

The longest chain, and the one most of it was self-inflicted while fixing #4.

**5a — the push.** Protecting main broke the OGC postprocess, which pushed `build/` straight to
main. It validated fine, reported `committed: true`, and failed on the last step:

```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: - 3 of 3 required status checks are expected.
```

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

## The common thread

In all six, the failure was invisible from the outside because the signal said "success". What
exposed each one:

| | what exposed it |
|---|---|
| 1 | counting emitted JSON paths, not passing examples |
| 2 | running the generator twice and diffing |
| 3 | a profiler, and distrusting a predicted speedup |
| 4 | reading which checks were *required*, not which were green |
| 5 | reading the job list of a "successful" run, step by step |
| 6 | an order-insensitive comparison between the correct two commits |

None of these needed cleverness. They needed looking at the thing itself instead of the badge on
top of it.
