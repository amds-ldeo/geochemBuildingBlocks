---
description: Propagate a schema/URI/naming change across the CDIF + ADA building-block ecosystem with parallel per-repo subagents, validation, and draft PRs.
argument-hint: "[--dry-run] <change description, e.g. 'rename xasOptional to xasDiscovery and update conformsTo URIs'>"
---

# /propagate-schema

User-supplied change description: **$ARGUMENTS**

You are the orchestrator. Follow the phases below in order. **Never skip the gate in Phase 4.**

---

## Repo registry

| key | path | git | regenerate | validate | source dirs | generated dirs |
|---|---|---|---|---|---|---|
| `mbb` | `C:\GithubC\CDIF\metadataBuildingBlocks` | yes | `python tools/regenerate_schema_json.py && python tools/resolve_schema.py --all && python tools/augment_register.py` | `python tools/validate_examples.py` | `_sources/` | `build/` |
| `geochem` | `C:\GithubC\USGIN\geochemBuildingBlocks` | yes | `python tools/regenerate_schema_json.py && python tools/resolve_schema.py --all && python tools/augment_register.py` | `python tools/validate_examples.py` | `_sources/` | `build/` |
| `dde` | `C:\GithubC\USGIN\ddeBuildingBlocks` | yes | `python tools/regenerate_schema_json.py && python tools/resolve_schema.py --all && python tools/augment_register.py` | `python tools/validate_examples.py` | `_sources/` (DDEproperties, profiles) | `build/` |
| `profile-core` | `C:\GithubC\CDIF\profile-core` | yes (reviewRevision202606) | (none — release repo; schema/SHACL synced from `mbb`) | `python FrameAndValidate.py` | `examples/`, `cdifCoreStructuredSchema.json`, `coreRules.shacl` | n/a |
| `profile-discovery` | `C:\GithubC\CDIF\profile-discovery` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifDiscoveryStructuredSchema.json`, `discoveryRules.shacl` | n/a |
| `profile-datadescription` | `C:\GithubC\CDIF\profile-datadescription` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifDataDescriptionStructuredSchema.json`, `dataDescriptionRules.shacl` | n/a |
| `profile-manifest` | `C:\GithubC\CDIF\profile-manifest` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifManifestStructuredSchema.json`, `manifestRules.shacl` | n/a |
| `profile-provenance` | `C:\GithubC\CDIF\profile-provenance` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifProvenanceStructuredSchema.json`, `provenanceRules.shacl` | n/a |
| `profile-codelist` | `C:\GithubC\CDIF\profile-codelist` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `Examples/`, `CDIFCodelistProfileStructuredSchema.json`, `rules.shacl` | n/a |
| `profile-conceptscheme` | `C:\GithubC\CDIF\profile-conceptscheme` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifConceptSchemeStructuredSchema.json`, `conceptSchemeRules.shacl` | n/a |
| `profile-datastructure` | `C:\GithubC\CDIF\profile-datastructure` | yes (reviewRevision202606) | (none — release repo) | `python FrameAndValidate.py` | `examples/`, `cdifDataStructureStructuredSchema.json`, `dataStructureRules.shacl` | n/a |
| `w3id` | `C:\GithubC\smrgeoinfo\w3id.org` | yes (master) | (none — text edit) | grep round-trip on touched URIs | `cdif/.htaccess` | n/a |

**Out of scope:** `ada_metadata_forms` (no git, monolithic schema not yet derived from BBs).

**`mbb` gh-pages publish.** Downstream repos resolve CDIF `$ref`s against the **published gh-pages**
copy of `mbb`'s `_sources/`, not any local checkout. Pages is published by the `deploy-viewer.yml`
workflow (it uploads the whole tree via `upload-pages-artifact`, `path: '.'`), and `process-bblocks.yml`
sets `skip-pages: true` so `deploy-viewer` is the sole publisher. `deploy-viewer` auto-runs only when
`process-bblocks` concludes **success** on `main`; if that CI is red the auto-run is **skipped** and
gh-pages freezes at the last good deploy. Publish lever (bypasses the success gate):
`gh workflow run deploy-viewer.yml -R Cross-Domain-Interoperability-Framework/metadataBuildingBlocks --ref main`.
See Phase 0c and Phase 6.5.

---

## Phase 0a — parse flags

Inspect `$ARGUMENTS` for the literal token `--dry-run` (anywhere in the string). If present:
- Set `DRY_RUN=true`.
- **Strip** `--dry-run` from `$ARGUMENTS` before doing anything else, so it isn't re-included in the change description handed to subagents, commit messages, or PR bodies. Use the cleaned string for all downstream substitutions.

If absent, `DRY_RUN=false`.

State the mode explicitly to the user in your first response: `Mode: DRY-RUN (no commits/pushes/PRs)` or `Mode: LIVE`.

---

## Phase 0b — autodetect affected repos

Parse the cleaned `$ARGUMENTS` using the matching primitives below. Apply all rules; union the resulting repo set.

**Matching primitives** (do NOT use bare substring search — that over-matches on compound names like `DDEDiscovery`):

- **Word match** for token T: T appears in the description with a non-letter/non-digit on each side (or at string start/end). Case-insensitive. Example: `discovery` word-matches "fix discovery typo" but does NOT match "fix DDEDiscovery typo" (no boundary between `DDE` and `Discovery`).
- **CamelCase-prefix match** for prefix P: a contiguous run of letters/digits in the description starts with P (case-insensitive on P), AND the character immediately after P is either an uppercase letter, a non-letter, or end-of-run. Example: prefix `DDE` matches "DDEDiscovery", "DDE", "dde-typo", but does NOT match "addends" or "address".

**Rules** (apply all that fire):

- CamelCase-prefix `DDE` → `dde`. Also word-match: `dde`, `DDEproperties`, `dde.bbr.metadata`. Phrase match: "Deep-time Digital Earth".
- CamelCase-prefix `ada` → `geochem`. Also word-match: `geochem`, `EMPA`, `ICPOES`, `LAF`, `NanoIR`, `QRIS`, `SLS`, `VNMIR`, `ECL`.
- CamelCase-prefix `xas` → `mbb` (xasProperties live in mbb; no separate xas release repo in current scope).
- CamelCase-prefix `CDIF` → `mbb` (the CDIF base; downstream release repos add only when a more specific rule below also fires).
- Word `core`, `cdifCore`, `cdif-core` → `mbb`, `profile-core`.
- Word `discovery`, `cdifDiscovery`, `xasDiscovery`, `xasOptional` → `mbb`, `profile-discovery`.
- Word `codelist`, `CDIFCodelist` → `mbb`, `profile-codelist`.
- Word `data_description`, `dataDescription`, `CDIFDataDescriptionProfile` → `mbb`, `profile-datadescription`.
- Word `data_structure`, `dataStructure`, `CDIFDataStructure` → `mbb`, `profile-datastructure`.
- Word `conceptscheme`, `conceptScheme` → `mbb`, `profile-conceptscheme`.
- Word `manifest` → `mbb`, `profile-manifest`.
- Word `provenance` → `mbb`, `profile-provenance`.
- Word `xasCore` → `mbb`.
- Word `conformsTo`, `w3id`, `redirect`, `.htaccess`, or any literal w3id.org URI substring → `w3id`.
- Any explicit mention of editing `_sources/` in `mbb` (e.g. "change CDIF base schema X") is a downstream-affecting change → add **all** repos that consume CDIF refs: `geochem`, `dde`, `profile-core`, `profile-discovery`, `profile-datadescription`, `profile-manifest`, `profile-provenance`, `profile-codelist`, `profile-conceptscheme`, `profile-datastructure`.

**Worked examples** — verify your matching by running these in your head before applying to the user's input:

- "fix typo in DDEDiscovery description" → CamelCase-prefix `DDE` matches "DDEDiscovery"; word `discovery` does NOT (no boundary before `D`); word `description` is not a trigger. Scope: `dde` only.
- "rename xasOptional to xasDiscovery and update conformsTo URIs" → word `xasOptional` and `xasDiscovery` both fire the discovery rule; word `conformsTo` fires w3id. Scope: `mbb`, `profile-discovery`, `w3id`.
- "regenerate cdifCore schemas" → word `cdifCore` fires the core rule. Scope: `mbb`, `profile-core`.
- "fix EMPA example" → word `EMPA` fires geochem. Scope: `geochem`.
- "update CDIF base manifest building block" → CamelCase-prefix `CDIF` → `mbb`; word `manifest` → `mbb`, `profile-manifest`; explicit "CDIF base" mention triggers downstream-affecting union. Scope: `mbb`, `geochem`, `dde`, `profile-core`, `profile-discovery`, `profile-datadescription`, `profile-manifest`, `profile-provenance`, `profile-codelist`, `profile-conceptscheme`, `profile-datastructure`.

If autodetection produces zero repos, ask the user via `AskUserQuestion` to specify the scope manually rather than guessing. If it produces a scope you suspect is over-broad (e.g. a CamelCase compound triggered multiple rules), call that out explicitly to the user when confirming.

Show the user the autodetected list with `AskUserQuestion`, offering:
- "Confirm scope" (recommended)
- "Edit scope" (then ask which to add/remove)
- "Abort"

Do not proceed without explicit confirmation.

---

## Phase 0c — classify gh-pages dependency (two-wave detection)

Downstream repos (`geochem`, `dde`, `ecrr`, the `profile-*` repos) resolve CDIF `$ref`s against the
**published gh-pages** URL
(`https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/...`),
not the local `mbb` checkout. Because `deploy-viewer.yml` is gated on `process-bblocks` success (see the
registry note above), an `mbb` `_sources/` edit is **invisible to downstream validation until Pages is
republished**. A downstream subagent that regenerates/validates against stale gh-pages will report a
false **red** even though the change is correct.

> Worked case (the motivating instance): `mbb` `_sources/schemaorgProperties/instrument/schema.yaml`
> changed `additionalType.items` to `anyOf: [string, {@id}]` and the commit was on `main`, but gh-pages
> still served `items: {type: string}`. Every `geochem` example that emitted `additionalType: [{"@id": …}]`
> failed JSON-Schema validation against the resolved (gh-pages-sourced) schema — not a geochem bug, a
> publish lag.

Set **`GHPAGES_DEPENDENT=true`** when the run edits any `mbb` `_sources/**/schema.yaml` that a
downstream repo `$ref`s by gh-pages URL — in practice, whenever the Phase 0b line-72 rule unioned the
downstream repos into scope because of an `mbb` `_sources/` change. Otherwise `GHPAGES_DEPENDENT=false`.

When `GHPAGES_DEPENDENT=true`, the propagation is **two-wave** and the waves span **two invocations**
(draft PRs never auto-merge, so the `mbb` merge happens out-of-band between waves):

- **Wave 1 — this run — `mbb` (+ `w3id` if in scope) only.** Apply, validate, PR. Then, once the
  operator merges the `mbb` PR, run Phase 6.5 to **publish + round-trip-verify** gh-pages. Do **not**
  spawn downstream subagents this run — they cannot pass their gate against stale gh-pages.
- **Wave 2 — a follow-up `/propagate-schema` invocation — the downstream repos.** Runs only after
  Phase 6.5 confirms the changed files round-trip current on gh-pages. Phase 7 prints the exact
  follow-up command.

State the wave plan explicitly and get confirmation before Phase 1. For `GHPAGES_DEPENDENT=false`
runs, ignore waves and proceed normally.

---

## Phase 1 — create worktrees

If `GHPAGES_DEPENDENT=true`, the **affected repo set for this run is Wave 1 only** (`mbb`, plus
`w3id` if in scope). The downstream repos are handled in the Wave-2 follow-up invocation (Phase 0c),
so do not create worktrees or subagents for them now.

Pick a timestamp slug: `TS=$(date -u +%Y%m%dT%H%M%SZ)`.
For each affected repo (of the current wave), in parallel:

```bash
WT="/c/Users/smrTu/.claude-worktrees/propagate-${TS}/<key>"
cd "<repo path>"
BRANCH="propagate/${TS}-<short-slug-of-change>"
git fetch origin
git worktree add -b "$BRANCH" "$WT" origin/main   # base branch: origin/master for w3id; origin/reviewRevision202606 for the profile-* release repos
```

If the working tree at the repo path has uncommitted changes, **stop** and surface them to the user with `AskUserQuestion` (continue / stash / abort) — do not silently include or exclude them.

Record the resulting `{key → worktree path → branch}` map for later phases.

---

## Phase 2 — spawn parallel subagents

Spawn **one Task subagent per affected repo in a single message** (parallel). Use `subagent_type: general-purpose`. Each prompt is self-contained — copy the template below, substituting the bracketed values:

> **You are the propagation worker for repo `<key>`.**
>
> Worktree: `<worktree path>` (already created on branch `<branch>`). Operate **only inside this worktree** — do not touch the user's main checkout.
>
> Change to apply: **$ARGUMENTS**
>
> Steps, in order:
> 1. **Apply the change.** Edit only files in the source dirs (`<source dirs>`). Never patch generated artifacts directly — fix the source and regenerate. (See feedback memory `feedback_generated_files.md`.)
> 2. **Regenerate** by running: `<regenerate command, or "skip"`.
> 3. **Validate** by running: `<validate command>`. Capture full output.
> 4. **Run consistency audit** (see "Consistency checks" section of `propagate-schema.md`). Fix any hits at the source and re-run steps 2–3 until clean.
> 5. **Pre-stage hygiene check:** run `git status --porcelain`. List every modified/untracked file. **Reject** any of: `*.docx`, `*.xlsx` (unless `docs/` Excel is the explicit target), `Copy of *`, `~$*`, `.DS_Store`, `Thumbs.db`, anything outside the source/generated dirs for this repo. If any such file appears, do **not** stage it — list it in your report under `unrelated_files` and continue.
> 6. **Stage explicitly** by listing each path (`git add path1 path2 ...`). Never `git add -A` or `git add .`.
> 7. **Do not commit, do not push, do not open PRs** — that is the orchestrator's job.
>
> Report back as JSON:
> ```json
> {
>   "key": "<key>",
>   "branch": "<branch>",
>   "worktree": "<path>",
>   "status": "green" | "red",
>   "validation_summary": "<one-line>",
>   "files_staged": ["..."],
>   "unrelated_files": ["..."],
>   "consistency_hits_fixed": ["trailing-slash:...", "const-concat:..."],
>   "remaining_issues": ["..."],
>   "diff_stat": "<output of git diff --cached --stat>"
> }
> ```
> `status: "green"` requires: validation passes, no `remaining_issues`, no `unrelated_files` staged.

---

## Phase 3 — collect reports

Wait for all subagents. Render a table: key | status | files_staged count | hits | remaining_issues.

---

## Phase 4 — gate (DO NOT SKIP)

If **any** subagent reports `status: "red"` or any `remaining_issues` or any `unrelated_files`:
- **Abort.** No commits, no pushes, no PRs in any repo.
- Surface the failures to the user. Offer (via `AskUserQuestion`): re-spawn just the failing subagents with corrective guidance, abandon the run (worktrees stay for inspection), or drop into manual mode.

Only when **every** subagent is green do you proceed to Phase 4.5.

**Wave note (`GHPAGES_DEPENDENT=true`).** This gate applies to the current wave's repos only. In
Wave 1 that is `mbb` (+ `w3id`); downstream repos are not in this run at all (Phase 1), so their
absence is expected, not a failure. Never let a Wave-1 run proceed to downstream work — downstream
validation is only meaningful after Phase 6.5 republishes gh-pages.

---

## Phase 4.5 — dry-run exit

If `DRY_RUN=true`, **stop here**. Do not run Phase 5, 6, or any commit/push/PR action.

Print a dry-run summary:
- Mode banner: `DRY-RUN COMPLETE — no commits, pushes, or PRs created.`
- The same final table format as Phase 7 (repo | branch | worktree path | files staged count | validation summary), but with PR URL replaced by `(skipped: dry-run)`.
- A reminder of the worktree paths and the exact commands the user can run to inspect each one (`git -C <wt> diff --cached`, `git -C <wt> log --oneline -1`).
- A reminder that worktrees were left in place at `~/.claude-worktrees/propagate-<TS>/` and how to clean them up (`git -C <repo path> worktree remove <wt>` per repo, then `git -C <repo path> branch -D <branch>` if they don't want the local branch either).

Then exit. Do not proceed to Phase 5.

If `DRY_RUN=false`, proceed to Phase 5.

---

## Phase 5 — commit + push (orchestrator only, LIVE mode only)

For each green subagent's worktree, in sequence (not parallel — easier to back out if something surprises you):

1. `cd "<worktree>"`
2. `git status` — re-verify the staged set matches `files_staged` from the report. If it differs, abort that repo and surface diff.
3. Commit:
   ```bash
   git commit -m "$(cat <<'EOF'
   propagate: <one-line summary derived from $ARGUMENTS>

   <2–4 line body explaining what changed in this repo and why.
   Cross-reference sibling repos updated in the same propagation run.>

   Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
   EOF
   )"
   ```
   Never use `--no-verify`. Never `--amend`. If a hook fails, fix and create a **new** commit.
4. Push: `git push -u origin "<branch>"`.

---

## Phase 6 — open draft PRs

For each pushed branch:

```bash
gh pr create --draft --base main --head "<branch>" \
  --title "propagate: <short title>" \
  --body "$(cat <<'EOF'
## Summary
- Part of a coordinated propagation across the CDIF/ADA ecosystem.
- Change: $ARGUMENTS
- Sibling PRs (this run): <list of {repo: PR URL} once known>

## Validation
- <validation_summary from subagent report>
- Consistency audit hits fixed: <list>

## Test plan
- [ ] Maintainer reviews diff
- [ ] Confirms sibling PRs land together (do not merge in isolation)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

`--base` is `master` for `w3id`, `reviewRevision202606` for the `profile-*` release repos, `main` for everything else. Always `--draft`. **Never** `gh pr merge`.

After all PRs are open, edit each PR body to replace `<list of {repo: PR URL}>` with the actual sibling URLs so reviewers can navigate the set.

---

## Phase 6.5 — publish + verify `mbb` gh-pages (LIVE, `GHPAGES_DEPENDENT=true` only)

Skip this phase entirely when `GHPAGES_DEPENDENT=false`.

Downstream `$ref` resolution reads gh-pages, so Wave 2 cannot validate until the merged `mbb` change
is republished there. Draft PRs never auto-merge (guardrail), so this phase runs **after the operator
confirms the `mbb` PR is merged to `main`** — pause and ask via `AskUserQuestion` ("mbb PR merged?
publish Pages now" / "not yet — stop here"). Do not dispatch against an unmerged branch: `deploy-viewer`
uploads `main`, so publishing before merge would ship the old tree.

1. **Trigger the publisher** (manual dispatch bypasses the `process-bblocks`-success gate that skips
   the auto-run):
   ```bash
   gh workflow run deploy-viewer.yml \
     -R Cross-Domain-Interoperability-Framework/metadataBuildingBlocks --ref main
   ```
   If `process-bblocks` is currently red, the normal `workflow_run` auto-deploy is **skipped**
   (its `if` requires `workflow_run.conclusion == 'success'`); the manual dispatch above runs anyway.
   Flag the red CI to the operator — Pages will publish, but the underlying failure still needs fixing.

2. **Wait for it to finish:**
   ```bash
   RID=$(gh run list --workflow=deploy-viewer.yml -L1 \
     -R Cross-Domain-Interoperability-Framework/metadataBuildingBlocks --json databaseId --jq '.[0].databaseId')
   gh run watch "$RID" -R Cross-Domain-Interoperability-Framework/metadataBuildingBlocks
   ```

3. **Round-trip verify every changed source file on gh-pages** (Pages/CDN can lag a minute or two —
   poll, don't assume). For each `mbb` `_sources/**/schema.yaml` touched this run, fetch the gh-pages
   URL and grep for the new content. Worked example (instrument `additionalType` `@id`-form):
   ```bash
   curl -s "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/instrument/schema.yaml" \
     | grep -A6 "'schema:additionalType'" | grep -q '@id' && echo "PAGES OK" || echo "PAGES STALE — wait + re-check"
   ```
   Do not declare Wave 1 done until every touched file round-trips its new content.

Only after all touched files verify current is the ecosystem ready for **Wave 2** (the downstream
follow-up invocation).

---

## Phase 7 — report to user

Print a final table: repo | branch | PR URL | status. Tell the user the worktrees remain at `~/.claude-worktrees/propagate-<TS>/` for inspection until they ask to clean up. **Do not delete worktrees automatically.**

**If `GHPAGES_DEPENDENT=true`,** also print the Wave-1 → Wave-2 handoff:
- Whether Phase 6.5 ran and the round-trip result per touched file (`PAGES OK` / `PAGES STALE`), or
  `pending` if the `mbb` PR isn't merged yet.
- The exact **Wave-2 follow-up command** to run once the `mbb` PR is merged and Pages verifies:
  `/propagate-schema <same change description>` — note that on the re-run, Phase 0c will re-classify,
  but with `mbb` already landed the downstream repos now resolve the updated gh-pages and pass. If the
  downstream change also has a generator flag staged behind the publish (e.g. geochem's instrument
  `additionalType` `@id`-form emitter), name it so the operator flips it in Wave 2.

---

## Consistency checks (every subagent runs these)

Run grep over the worktree's source dirs *and* any regenerated artifacts. Treat any hit as a hit-to-fix at the source.

1. **Trailing slash in conformsTo / $id / w3id URIs**
   Pattern: `https://w3id\.org/cdif/[^"\s]+/"` (slash before closing quote).
   Past incident: commit `fcb291eb9` removed trailing slashes from all CDIF conformance URIs.

2. **camelCase / underscore drift in conformance class names**
   Watch for both forms appearing for the same component: `dataDescription` vs `data_description`, `xasOptional` vs `xasDiscovery`, etc. The canonical form (per `fcb291eb9`) is underscore-segmented for multi-word URIs (`data_description/1.0`).

3. **Const concatenation in YAML → JSON conversion**
   Past incident: commit `f1e2218a` — a regex for `@type` const conversion concatenated the const value with the next property on the same line (e.g. `const: "Foo"nextProp:`). Grep regenerated schemas for `["'][a-zA-Z_]+:` (a quote immediately followed by an identifier and colon) and for `Schema"[a-z]` patterns. Re-run `regenerate_schema_json.py` after fixing the source `schema.yaml`.

4. **Self-referential `$defs` causing RecursionError**
   Past incident: commit `2f402f6e0` — `resolve_schema.py` blew up on local `$defs` that referenced themselves (CDIFCodelist). If `resolve_schema.py` raises `RecursionError`, suspect a self-ref in a newly added `$defs` block; the tool already has a guard but new patterns may slip past it.

5. **Stale register entries**
   After regenerate, compare `build/register.json` entries to `_sources/` directory listing. Any orphans or missing entries are a fix-at-source problem (add/remove the source dir).

If a check fires, fix the source, regenerate, and re-run validation. Report each fix in `consistency_hits_fixed`.

---

## Guardrails (always)

- **Never** stage with `git add -A`, `git add .`, or `git add --all`. Always list paths explicitly.
- **Never** stage `*.docx`, `Copy of *`, `~$*`, `.DS_Store`, `Thumbs.db`. `*.xlsx` only if explicitly part of the change target (e.g. `docs/TAPP_EPMA_filled.xlsx` when EPMA template is the subject).
- **Never** `--no-verify`, `--no-gpg-sign`, `--amend`, `git reset --hard`, `git push --force`. If a hook fails, fix and re-commit.
- **Never** patch generated artifacts directly — always trace to source generator/template/schema and regenerate (see `feedback_generated_files.md`).
- **Never** auto-merge. PRs are always `--draft`.
- **Never** delete worktrees without asking.
- If the user has uncommitted changes in any repo's main checkout when Phase 1 starts, stop and ask — do not assume those changes should or should not flow into the propagation branch.
