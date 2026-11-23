# The standards-table migration

**A calibration standard is not a reagent.** The two carry different metadata because different
things go wrong with them: a reagent is described by purity, lot number, expiration and the
contamination it contributes, tracked through method blanks; a standard is described by its
certified values, the uncertainties on them, its traceability chain, its source and its
preparation. Flattening a standard into a reagent loses exactly the metrological traceability an
analytical provenance record exists to carry. That is the authority for this whole migration
(Stephen, 2026-11-01, in `tappDefinition/schema.yaml`'s `ada:standardTemplate` description).

Today, in the authored static examples, standards are still `schema:instrument` members with the
reagent kind term `Q2356542` and an `ada:reagentRole` of `primaryStandard` or `secondaryStandard`.
Retiring those four enum terms is the **consequence** of this migration, not a precursor: 27
entries in 5 authored examples that NO generator rewrites would fail against their own schema the
moment the terms went, so the destination has to exist first.

## The destination, settled on amds-ldeo/tapp#22

Two tables, because one table cannot both identify the standards and record what each calibrates:

1. **The standards** — one row per standard. Its identifier (registered where one exists), its own
   material (its matrix, *not* a target material of the procedure), the citation for its reference
   values, and the accepted value itself.
2. **The calibration assignment** — keyed `target material x target species`, naming a standard and
   the role it plays there.

The split is what dissolves the hard cases without a multi-valued role property: one kaersutite
calibrating Si, Fe and Mg is three rows of table 2 and one of table 1, and a material that is
primary for one phase and secondary for another is two rows of table 2 differing only in role.
**So the role belongs to the ASSIGNMENT, not to the standard** — which is also why it must never
reuse `ada:reagentRole`: that property is a single string used as a path SELECTOR
(`schema:instrument[ada:reagentRole='referenceMaterial']`) and cannot carry several roles.

Matrix matching then falls out instead of being asserted twice: compare the standard's own material
in table 1 with the target material in table 2's key.

Agreed by both sides as of 2026-11-20: table 1, the rename of `Primary Calibration Standard Name`,
the certified value, one role vocabulary restricted per technique by SHACL rather than by narrowed
per-table enums, and the dropping of the multi-valued `Reference Material Role`.

## Where each field lands in gBB

gBB has ONE keyed-table container per key, and the key is implicit in *which container*
(`schema_path_emitter.KEYED_TABLES`, 5 entries). A new key therefore means a new container.

| tapp#22 field | keyed by | gBB container | state |
|---|---|---|---|
| 1 `Reference Materials` | defines: standard | `ada:defaultStandards` (the ROWS) | **ready** |
| 3 `Reference Material Type` | standard | `ada:standardColumns[]` column | **ready** |
| 4 `Reference Material Identifier` | standard | `ada:standardColumns[]` column | **ready** |
| 5 `Reference Value Source` | standard | `ada:standardColumns[]` column | **ready** |
| 5a `Reference Value` | standard x reported property | `ada:standardColumns[]` column, pair rows | awaiting Q3 |
| 6 `Calibration Standard` | target material x target species | **no container exists** | awaiting Q1 |
| 6a `Quality-Control Standards` | target material x target species | **no container exists** | awaiting Q1 |
| 7 `Interference Correction Standard` | target species | `ada:targetSpeciesColumns[]` column | awaiting Q1 |
| 8 `delta/epsilon Reference Standard` | target species | `ada:targetSpeciesColumns[]` column | awaiting Q1 |
| 9-13 precision and accuracy | standard x reported property | as now | no change |

Note what this says about table 1: because `Reference Value` is keyed `standard x reported
property`, table 1 is **not** one row per standard after all — its rows stay standard-by-target
PAIRS and the per-standard columns (3, 4, 5) repeat across a standard's rows. That is exactly the
shape `ada:standardTemplate` already has, and it is why `StandardIdentifierColumn` is deliberately
not unique per row. Table 1 needs no restructuring; **table 2 is the new build.**

## What the generator does, which is the answer to tapp#22's question 1

The question was: *one field per role in the TAPP, pivoted into your table 2 with role as a column
— does that work for your generator?* Measured in `tools/schema_path_emitter.py`:

- **One workbook field becomes one COLUMN, never one row.** `_is_analyte_column()` (line 1037)
  returns true for any sidecar path ending at a `KEYED_TABLES` array, and `build()` then emits
  **one generated column def per row** and narrows the array's `items` to those columns. So four
  role fields arrive as four columns of one table, not as four rows carrying a `role` column.
- **A selector on a keyed-table column array falls OUT of that branch entirely**, because
  `_is_analyte_column` requires `selector is None`. A path such as
  `ada:standardColumns[ada:standardRole='primaryCalibration']` would drop through to generic leaf
  handling and emit `items: {type: string}` against the technique's `items: {anyOf: [...column
  objects...]}` — an `allOf` no instance can satisfy. That is not hypothetical: it is how
  `Module_ICPMS` broke 96 examples.

So the pivot cannot happen in a path selector, and it does not need to happen at all. Four columns
is the generator-native form, and it is **strictly more checkable** than one `standard` column plus
a free-text `role`: each role gets its own sealed column shape with its own `schema:propertyID`
into the role vocabulary, instead of a string that any value satisfies. The role is then carried by
column identity.

The cost is that `role` stops being a value you can group by inside one table, which matters only
if a consumer wants "every assignment, whatever its role" in one pass.

Two consequences to carry into the answer:

- **Fields 7 and 8 cannot share table 2.** They are keyed by bare `target species`, not by
  `target material x target species`, and in gBB a different key is a different container. They
  belong as columns of the existing per-species table (`ada:targetSpeciesColumns`), which is the
  right home anyway — interference overlaps and delta scales do not depend on the phase.
- **Module placement reconciles without anyone moving anything.** `build_module_bb.is_composable()`
  refuses any path containing `ada:standardColumns`, so these rows cannot be constrained by a gBB
  module BB. Upstream a module is an authoring device that writes its rows into every table that
  uses it, so the 16 delivered tables already carry them per technique — which is precisely the
  form gBB needs.

## Step 1, landed 2026-11-22

Three defects in the existing infrastructure, all independent of the three open questions:

1. **`ada:defaultStandards` could not hold a row object, and that was unsatisfiable rather than
   merely unstated.** `schema_path_emitter.DEFAULT_ROW_ARRAYS` lists all five default-row arrays and
   emits `string|DefinedTerm|object` for each; this base stopped at `string|DefinedTerm`; `allOf`
   intersects. The first sidecar row to path a standards default would have failed with
   `{'standard': ...} is not valid under any of the given schemas` while the base read as though it
   allowed exactly that. Three of the five arrays carried the branch, two did not — this one and
   `ada:defaultReportedProperties`, fixed together. The description also asserted that per-standard
   column values "live in the analysis record, not here", which is false for table 1, whose entire
   content is per-standard.
2. **`ada:standardizationType` was never declared.** The description named it as the property saying
   which domain a row's target was in. One occurrence in the repo, in that description. Removed
   rather than declared, because the agreed split removes the question it answered: the target is
   the assignment table's key, not a free choice of domain.
3. **The whole template was unexercised.** Measured before this commit: `ada:standardTemplate`,
   `ada:standardColumns` and `ada:defaultStandards` were referenced by 0 sidecar rows, carried by 0
   examples and pinned by 0 counterexamples — so no gate in this repo could see a change to any of
   them, in either direction. `exampletappDefinition-all-properties.json` carried 3 of the 5
   templates, and this was one of the two missing. It now carries a 4-column table 1 with 5 row
   objects, for the five standards that example already names as instrument members, and three
   counterexamples pin the identifier requirement, the `contains` and the `maxContains: 1`.

The five standards' ROLES stay in `ada:reagentRole` for now. There is nowhere else to put a role
until table 2 exists, and moving them earlier would lose the information.

## Blocked, and on what

Ruolin will not change a table until the three questions are confirmed ("we won't change any tables
until you confirm", tapp#22, 2026-11-20). Table 2's rows come from workbook fields, so the gBB half
cannot start until they are delivered. The questions:

1. One field per role, pivoted into table 2 with role as a column — does that work for the
   generator? *Measured above: yes, as four columns rather than a role column.*
2. The four-value role vocabulary (primary calibration, interference correction, delta or epsilon
   reference, secondary QC), with bracketing folded into primary calibration, drift monitor treated
   as a use rather than an assignment, and matrix correction deferred.
3. `Reference Value` keyed `standard x reported property`.

On question 3 there is one thing worth saying rather than silently emitting: the field's Data Type
is `Text (free)`, so "0.52 +/- 0.03 wt%" closes the gap nominally but not numerically — it still
does not let anyone recompute an accuracy figure, which was the stated reason the gap mattered. A
structured value / uncertainty / unit triple would. The workbook is the source of truth for the
field, so this is a question to put upstream, not something to restructure here.

Also still open, and listed here so it is not rediscovered: `ada:standardizationType` is gone, but
nothing yet declares the role vocabulary itself, and `ada:defaultStandards` row objects are accepted
without their column values being checked against the declared columns — the same latitude every
other keyed table's rows have.

## When resuming

- Read this file, then `tappDefinition/schema.yaml`'s `ada:standardTemplate` description.
- Measure before quoting any count here; re-run the greps rather than trusting the numbers.
- The authored static examples are the ones that matter for the enum removal
  (`tappDefinition/example*.json`, `geochemBaseProfile/examplegeochemBaseProfile.json`): 14
  `primaryStandard` and 13 `secondaryStandard` entries across 5 files. The generated examples carry
  only `referenceMaterial` (61) and `reagent` (27), and the `referenceMaterial` occurrences all come
  from ONE sidecar row, so they move when that row's path moves.
