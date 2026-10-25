# Committing in a shared checkout

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

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

`.gitmodules` sets `update = none` (for the reason in `CLAUDE.md`'s TAPP-source note), so
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
- **Hot files at merge time.** #158 and #159 both edited CLAUDE.md and conflicted; that file is
  the likeliest conflict in the repo. The fix is sequencing the merges, not isolation.
- **`main` moving underneath a branch.** #169 was built on a base four commits old, which is
  fine, but its squash stat then reported 1428 files against the 163 the commit actually carries —
  read the commit (`git show --name-only --format= <sha>`), never the merge tool's summary.

**A quiet tree is not a finished job.** On 2026-10-19 a `regenerate.py` looked complete — writes
had stopped and all four gates passed — while it was still running, and the census then found
`PSFD/profile-ada` UNREADABLE at zero bytes, complete minutes later. Those four green gates were
read off a half-written tree. Wait for the process's own exit status AND a sustained quiet window
before believing any measurement taken from the tree.
