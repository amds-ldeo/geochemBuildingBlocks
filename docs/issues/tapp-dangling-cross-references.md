# TAPP issue draft: one Purpose text cites a field that does not exist

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Found 2026-10-23 while reconciling definitions for the variable-registry prototype.

## The problem

One Purpose text directs the reader to another field by name, and that name exists as no
label anywhere in the workbooks:

| cited as | cited from | nearest existing label |
|---|---|---|
| `Internal Standard Approach` | `Normalization / Standards-Based Correction`, the LA-ICPMS variant — "Distinct from the primary internal standard approach captured in *Internal Standard Approach*." | `Internal Standard Concentration` (3 defs) |

The sentence exists to draw a boundary — this field is *not* the internal standard
approach — and a reader who follows it finds nothing, so the boundary is unverifiable.

> **A second candidate was withdrawn.** `Sample Persistent Identifier (Group 2)` was
> initially reported here as a dangling reference too. It is not: `(Group N)` is a pointer
> to the workbook's own numbered SECTION, so this reads "the Sample Persistent Identifier
> field in section 2, Samples" — and that field exists with 61 defs, in exactly that
> section. The citation is correct and resolves. 252 Purpose texts use the same `Group N`
> convention and all 252 resolve against the section headers; the registry prototype now
> substitutes the section name when it emits a definition, since a bare number means
> nothing outside the workbook.

## Why it will not surface on its own

Nothing validates prose. A cross-reference in a Purpose cell is read by people, not by a
generator, so a renamed or never-created target leaves the citation pointing at nothing
and no build step notices. geochemBuildingBlocks has the same failure mode on its own
side, recorded in CLAUDE.md: `adaProfile/QRIS` named a detail block in its description and
referenced it nowhere for as long as the file existed, because no regeneration would ever
have looked.

This was found by extracting every `captured in X` / `see 'X'` phrase from the 1893
registry defs and testing each target against the set of real labels — 5 references found,
4 resolve, 1 does not.

## Options

1. **Point the citation at the existing field** — `Internal Standard Approach` →
   `Internal Standard Concentration`. Assumes the intended target is the nearest match,
   which is worth confirming: "approach" and "concentration" are not obviously the same
   field.
2. **Add the missing field**, if `Internal Standard Approach` was meant to exist as its own
   row distinct from the concentration.
3. **Drop the citation** from the Purpose text and state the boundary without naming a
   field.

The choice between 1 and 2 is Ruolin's — it depends on whether the approach and the
concentration were meant to be one field or two.

## Suggested follow-up

The check is three lines and worth running over each delivery rather than once: extract
every field name cited in a Purpose text and assert it resolves. Nothing else will catch
the next one.
