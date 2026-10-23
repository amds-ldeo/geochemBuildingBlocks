# TAPP issue draft: two Purpose texts cite a field that does not exist

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Found 2026-10-23 while reconciling definitions for the variable-registry prototype.

## The problem

Two Purpose texts direct the reader to another field by name. Neither name exists as a
label anywhere in the workbooks:

| cited as | cited from | nearest existing label |
|---|---|---|
| `Internal Standard Approach` | `Normalization / Standards-Based Correction`, the LA-ICPMS variant — "Distinct from the primary internal standard approach captured in *Internal Standard Approach*." | `Internal Standard Concentration` (3 defs) |
| `Sample Persistent Identifier (Group 2)` | — | `Sample Persistent Identifier` (61 defs) |

The `(Group 2)` suffix looks like a stale echo of the earlier Group-1 / Group-2
coupling-field naming, so that one is probably a rename that left a reference behind.

`Internal Standard Approach` is the more consequential of the two: the sentence exists to
draw a boundary — this field is *not* the internal standard approach — and a reader who
follows it finds nothing, so the boundary is unverifiable.

## Why it will not surface on its own

Nothing validates prose. A cross-reference in a Purpose cell is read by people, not by a
generator, so a renamed or never-created target leaves the citation pointing at nothing
and no build step notices. geochemBuildingBlocks has the same failure mode on its own
side, recorded in CLAUDE.md: `adaProfile/QRIS` named a detail block in its description and
referenced it nowhere for as long as the file existed, because no regeneration would ever
have looked.

Both of these were found by extracting every `captured in X` / `see 'X'` phrase from the
1893 registry defs and testing each target against the set of real labels — 5 references
found, 3 resolve, 2 do not.

## Options

1. **Point each citation at the existing field.** `Internal Standard Approach` →
   `Internal Standard Concentration`; `Sample Persistent Identifier (Group 2)` →
   `Sample Persistent Identifier`. Assumes the intended target is the nearest match, which
   is worth confirming for the first one — "approach" and "concentration" are not obviously
   the same field.
2. **Add the missing field**, if `Internal Standard Approach` was meant to exist as its own
   row distinct from the concentration.
3. **Drop the citation** from the Purpose text and state the boundary without naming a
   field.

Option 1 for `Sample Persistent Identifier (Group 2)`, which is clearly a stale suffix.
For `Internal Standard Approach`, the choice between 1 and 2 is Ruolin's — it depends on
whether the approach and the concentration were meant to be one field or two.

## Suggested follow-up

The check is three lines and worth running over each delivery rather than once: extract
every field name cited in a Purpose text and assert it resolves. Nothing else will catch
the next one.
