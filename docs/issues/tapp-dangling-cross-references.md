# TAPP issue draft: Purpose texts citing `Analyte`, a field that no longer exists

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Found 2026-10-23 while reconciling definitions for the variable-registry prototype.

## The finding

Purpose texts cite other fields by name. Checked against every Metadata Item in the
workbooks — 415 rows across the 61 workbooks plus 166 in the module sidecars, 420 distinct
— one cited name does not exist, and it is a direct consequence of the
`analyte` → `target species` migration:

| cited as | occurrences | status |
|---|---|---|
| **`Analyte`** | **16** | no such row. The field is now `Target Species` (13 defs). |
| `Transect Rate` | 6 | abbreviated — the row is `Transect Rate, Mapping Rate or Step Size` |

`Analyte` is the substantive one. `Monitored Isotopes` leans on it for a rule that matters:

> "The analyte list is given by the **Analyte** field and is never inferred from the
> element symbols appearing here."

That sentence exists to stop a consumer deriving the analyte list from the isotope symbols,
and it points at a field that was renamed out from under it. A reader who follows the
citation finds nothing, so the rule reads as advice about a field that does not exist.

`Transect Rate` is milder: a human finds the row, an exact match does not.

## Why it will not surface on its own

Nothing validates prose. A citation in a Purpose cell is read by people, not by a
generator, so a renamed target leaves it pointing at nothing and no build step notices.
geochemBuildingBlocks has the same failure mode recorded in CLAUDE.md: `adaProfile/QRIS`
named a detail block in its description and referenced it nowhere for as long as the file
existed.

The renaming is what makes this a recurring risk rather than a one-off: every future
vocabulary change can strand citations the same way, and `analyte` → `target species` is
only partly done — 73 defs still use the retired term, 45 of them in one un-migrated row.

## Options

1. **Repoint the citations** — `Analyte` → `Target Species`, `Transect Rate` → the full row
   name. Recommended, and it should ride along with the rest of the `analyte` migration
   rather than being tracked separately.
2. **Repoint and shorten** — give `Transect Rate, Mapping Rate or Step Size` a short form
   that citations may use, if abbreviating is wanted.
3. **Drop the citation** and state the rule without naming a field. Loses the pointer,
   which in `Monitored Isotopes` is the useful part.

## Suggested follow-up

Worth running over each delivery rather than once: extract every field name cited in a
Purpose text and assert it resolves against the workbooks' Metadata Items. Two notes on
getting that check right, both learned by getting it wrong here:

- **Validate against the WORKBOOK ROWS, not against generated defs.** A first pass checked
  citations against the 6 technique registries and reported `Internal Standard Approach`
  and `Acquisition Software` as dangling. Both exist — as workbook rows and as module
  sidecar rows. Module-owned fields are absent from the technique registries *by design*,
  so that label set was structurally blind to 166 rows.
- **The phrasings vary.** "captured in X", "see 'X'", "the X field", "given by the X field",
  "recorded in X", "documented in X". A scan matching only the first two found 5 citations;
  broadening it found 11.
