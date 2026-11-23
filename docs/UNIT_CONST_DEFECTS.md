# Non-unit values that reached `schema:unitText`

`schema:unitText` names the unit a dimensioned value is expressed in. `build_tapp.unit()` reads it
out of the Data Type cell's first parenthesis, and both parameter emitters turn it into a
**`const`** on the procedure side (`param_template_def`) and a required `{type: string}` on the
analysis side (`param_value_def`).

Taking the parenthesis verbatim put two kinds of non-unit into that const. Measured 2026-11-23
over the 16 pinned deliveries: **5 distinct values across 8 committed files.**

## Alternation — fixed, by encoding it as "dimensioned, unit not fixed here"

| Data Type cell | rows | techniques |
|---|---|---|
| `Numeric (mg or mL)` | 3 | solutionMcicpms, solutionQicpms, solutionSficpms — *Sample Aliquot Mass or Volume* |
| `Numeric (pA or nA)` | 1 | temTAPP — *STEM Probe Current* |
| `Numeric (µL/min or mL/min)` | 3 | solutionMcicpms, solutionQicpms, solutionSficpms — *Sample Uptake Rate* |

The cell asserts a dimension and declines to fix the unit. A `const` can pin only ONE string, so
`{"const": "pA or nA"}` demanded that an instance state that literal phrase and **rejected the
`pA` or the `nA` the cell was offering a choice between.** That is a constraint the workbook never
stated, and one no correct instance satisfies.

`UNIT_UNNAMED` is the encoding that already existed for exactly this case — the SEM and Solution
tables write `Numeric + unit` where EPMA and the LA family write `Numeric (um)`, and both assert
that a unit exists while only the second says which. So these three now resolve to `UNIT_UNNAMED`:
the template's `schema:unitText` becomes `{type: string}` instead of an unsatisfiable `const`, and
the analysis side still **requires** it, so the instance states which unit it actually used.

Nothing authored upstream is relaxed. gBB stops asserting what the workbook did not.

`Sample Aliquot Mass or Volume` is the one where the two alternatives are different *quantities*
(a mass or a volume, not one quantity at two scales). `UNIT_UNNAMED` is still right — and the
field would be better split in two upstream, which is a question for amds-ldeo/tapp, not something
to restructure here.

## Arity — half fixed: the unit is now correct, the arity is not yet sayable

| Data Type cell | rows | techniques |
|---|---|---|
| `Numeric pair (µm × µm)` | 3 | epmaTAPP, semCompositionTAPP, semTAPP — *Beam Raster Dimensions* |
| `Numeric pair (pixels x pixels)` | 4 | epmaTAPP — *Map Dimensions*; temTAPP — *STEM Scan Dimensions*; semCompositionTAPP, semTAPP — *EDS Map Dimensions* |

Here the workbook says **both** things correctly and in the right places: the arity in the type
phrase (`Numeric pair`) and the unit in the parenthesis, repeated once per dimension. Taking the
whole parenthesis lost the real unit **and** put the arity in the unit slot, where no consumer
looks for it.

`unit()` now matches the repeat — `A × A` is an arity, `A × B` is a compound unit and is left
alone — and returns the single factor. So `schema:unitText` is `µm` and `pixels`, which is true.

**The arity is still dropped, in two places, and both wait on the same thing:**

- `jtype()` collapses `Numeric pair` to `number`. A pair of numbers is not a number.
- nothing records that the value has two components.

Both belong in the multiplicity slot being added for **amds-ldeo/tapp#23** (a column's declared
data type names the ITEM type, with multiplicity carried separately). Neither `schema:unitText`
nor `ada:dataType` is the place: `ada:dataType` admits only `string|number|integer|boolean|date|uri`,
and putting arity in `unitText` is the defect this file documents.

Until that lands the fact is **not lost, only unstated** — the workbook still carries it, and the
seven rows are listed above so the multiplicity work can find them without re-deriving the set.

## Still wrong, and deliberately not fixed here

`Integer (QuantitativeValue)` on stemTAPP's *Image Width* and *Image Height* makes `unit()` return
`QuantitativeValue`, a schema.org type name. It reaches **no committed const today**, because
neither row is placed where a parameter emitter sees it. Guarding it would change no byte and so
no gate could confirm the guard works — it is recorded here instead, to be fixed when a placement
makes it live, or upstream in the workbook cell, which is the better fix.
