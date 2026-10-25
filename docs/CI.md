# CI: required-check history and the build-PR mechanism

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

**`Validate committed examples` became required on 2026-10-16**, and for eight days before that
it was not. It is the check written to close #63's gap — a schema requiring a property no example
carried, merged green because nothing validated an example — and an unrequired gate is one
auto-merge merges straight past when red, which is how #31 and #32 landed broken. Requiring it was
gated on the ordering rule in `CLAUDE.md` (no `paths:` filter on a required workflow), verified first rather than assumed: no `paths:` filter, no
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

The STEM/EBSD caveat (`CLAUDE.md`, three categories of example) still stands and is NOT contradicted by that zero: the content loss
belongs to the per-technique `regenerate.py --tapp <ONE>` path, which this job does not use.


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
GITHUB_TOKEN would get no checks, per the rule in `CLAUDE.md` (a GITHUB_TOKEN push triggers no workflow), and would sit open forever. It grants no
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
