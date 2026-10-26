# Validation gates: the audit baseline, vendored remotes, the census and the counterexamples

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

**The audit is baselined, and it gates.** Until 2026-10-16 it printed
`Summary: 246 passed, 5 failed` and exited **0**, and no workflow ran it — a failure report nothing
could act on (`docs/SILENT_SUCCESS.md` #9). It now exits 1 on any issue not recorded in
`docs/audit_baseline.json`, and runs as a step of `check-schema-drift.yml`.

The baseline is EMPTY as of 2026-10-26. It held 5 accepted failures — the legacy
`geochemProfile/<TECH>/profile-ada` blocks for QRIS, RAMAN, VNMIR, XANES and XRD, each on
`No example files found` — and those blocks were retired rather than given examples: no record
derived to their `ada<TECH>Full` cids (measured over all 7,447) and each lost every detection
contest to its TAPP twin. Accepting them while they existed is what let the audit gate at all;
making it fatal outright would have built a check that can never pass.

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
targets, closed objects, branch counts — 1,467,862 of them across 257 blocks in the committed manifest on 2026-10-25) and compares the
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
constrains nothing, a `$ref` that now resolves somewhere more permissive. 27 cases (2026-10-25) in
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
