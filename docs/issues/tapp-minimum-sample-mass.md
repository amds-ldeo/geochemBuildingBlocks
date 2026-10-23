# TAPP issue draft: a minimum sample mass is hiding inside Detection Limit

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Found 2026-10-23 while reconciling definitions for the variable-registry prototype.

## The problem

`Detection Limit` in `Solution_MC-ICP-MS` carries a fallback clause that reports a
different quantity:

> "Elemental detection limits, one per reported concentration variable… applicable when
> isotope dilution concentrations are also reported. **For pure isotope ratio procedures
> (no concentration output), this field is N/A or reports the minimum sample mass required
> for a measurement at target precision.**"

A minimum sample **mass** is not a detection limit. The field therefore holds a
concentration for most procedures and a mass for some, under a name that promises the
former, and nothing in the record distinguishes the two cases — a consumer reading
`Detection Limit` across the corpus would have to parse the value's units to discover
which quantity it got.

This is the same shape as the dwell-time issue filed alongside this one
(`tapp-dwell-vs-livetime.md`): a second measurand carried in a fallback clause of a field
named for the first.

## Why it is worth a row of its own

The quantity is a real and useful one. For a pure isotope-ratio procedure there is no
concentration detection limit to state, but "how much material do I need to hit the target
precision" is exactly the sensitivity question a data user wants answered — and it is
currently only sayable by overloading another field.

Scope is small: `Solution_MC-ICP-MS` is the only workbook that mentions it, 1 def today.

## Options

1. **Add a row** — `Minimum Sample Mass Required`, Purpose "Minimum sample mass required
   for a measurement at target precision", and drop the fallback clause from
   `Detection Limit` so that field means one thing. Recommended.
2. **Add the row and keep `Detection Limit` as `N/A`** for pure ratio procedures, which is
   already the first half of the existing fallback. Same as option 1 with the `N/A`
   behaviour stated explicitly.
3. **Leave it in the fallback** and accept that `Detection Limit` is two quantities for
   this technique. Cheapest, and it keeps the field unreadable without unit inspection.
4. **Drop the clause** entirely, if the mass is not in fact reported by any submitter —
   worth checking before adding a row nobody fills.

Option 1 unless option 4 turns out to be the case; the `N/A` half of the clause already
covers what `Detection Limit` should say for these procedures.

## Status in geochemBuildingBlocks

Recorded in `docs/variable_registry_decisions.json` under the `Detection Limit` decision:
the prototype promotes the clause to `ada:variable/minimumSampleMassRequired`, marked
`blocked_on` this issue, because the registry is GENERATED from the workbooks and no row
declares the label. Nothing is generated from the prototype, so the entry costs nothing to
revise or withdraw.
