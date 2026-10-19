# `ReportingCore` and its block system

> ## STATE, 2026-10-18: `ReportingCore` IS RETIRED UPSTREAM AND THE BLOCK SYSTEM IS DORMANT
>
> Read this before using anything below as current fact. Measured against the `tapp/` submodule as
> pinned, whose `composed_tapps.json` is generated 2026-10-01:
>
> | | |
> |---|---|
> | `Module_ReportingCore.json` upstream | **gone** — 15 `Module_*.json` remain and it is not among them |
> | TAPPs composing `ReportingCore` | **0** of 16 |
> | manifest entries using a `blocks` selection | **0** |
> | upstream modules with `conditional: true` | **0** of 15 |
> | `build_module_bb.module_blocks("reportingCore")` | returns **`None`** |
> | `docs/modules/Module_ReportingCore.schemapaths.csv` | already removed |
> | `_sources/BaseSchema/modules/reportingCore/` | **still present** |
>
> So the block-selection path in `build_module_bb` and `module_composition` is working code that
> nothing currently exercises, and the per-TAPP selection table below describes a manifest that no
> longer exists. The surviving gBB block still carries the frozen per-block `$defs` from when it
> was live — `TargetSelection_Procedure`, `AggregationQc_Analysis`, `AllBlocks_Procedure`,
> `AllBlocks_Analysis`.
>
> **`reportingCore` is now in exactly the state `group1` was in before it was archived** to
> `archive/modules/` (`a1ba43b19`): no upstream declaration, no sidecar, no consumer. Archiving it
> the same way is the obvious next step and has not been done. CLAUDE.md already records it as
> "the current manifest composes into nothing".
>
> **Every module still declares a `blocks` array** — Core 6, ICPMS 4, LaserAblation 4, and so on —
> because blocks also drive table composition and placement. What made `ReportingCore` special was
> `conditional: true`, which is the flag the schema side tests, and no module sets it today. So do
> not read "has blocks" as "is conditional"; the code is right to test the flag.
>
> The rest of this file is kept because the reasoning is still the reason the mechanism exists, and
> because it is the live precedent for any future conditional module — including the request in
> `docs/upstream-requests.md` §4a to make `Sampling Unit Name` a selectable block of Core. Treat
> what follows as **how it worked**, not as what is composed now.

Most TAPP modules contribute all their fields to every TAPP that composes them. **`ReportingCore`
did not.** Its six fields are grouped into five *blocks*, each carrying a condition, and a
consuming TAPP took only the blocks that applied to it.

This was the one module where "composes `ReportingCore`" did not mean "has all of `ReportingCore`",
and missing that produces a confident wrong answer. It produced one here: a check comparing the
whole module against every consumer reported **18 fields as missing**, which read like a defect in
the library and was in fact the block conditions working exactly as designed.

---

## The five blocks

Declared in `Claude Skills for TAPP/modules/Module_ReportingCore.json`, which carries
`"conditional": true` and a `blocks` array. This mapping is **data, not convention** — read it,
never infer it.

| block | field(s) | applies when |
|---|---|---|
| `target_selection` | `Target Selection Criteria`, `Pre-Analysis Imaging and Screening` | the procedure analyses a *selected part* of a sample rather than the bulk |
| `calibration_factor` | `Calibration Factor and Determination Method` | the reported quantity depends on a factor calibrated against an independently known reference — zeta, J value, isotopic tracer, RSF, Cliff-Lorimer *k*, dose rate, CT-number calibration |
| `blank` | `Procedural Blank Level` | the procedure has an analytical blank |
| `aggregation` | `Analysis Inclusion and Rejection Criteria` | reported values aggregate several measurements |
| `aggregation_qc` | `Goodness-of-Fit or Dispersion Statistic` | that aggregation carries a dispersion statistic |

Each block also declares `target_group`, `placement` and sometimes `anchor_field` — where the fields
land in the composed table. That matters for composition, not for schema generation.

## Who took what — HISTORICAL

The table below is the selection as it stood when this file was written. **No entry in the current
manifest names `ReportingCore` at all**, so none of these rows is live; they are kept as the record
of which analytical differences the blocks encoded, which is the part worth preserving.

`composed_tapps.json` recorded the selection on the module entry, as `"blocks": "all"` or a
comma-separated list:

| TAPP | blocks | consequence |
|---|---|---|
| EPMA, SEM, SEM-Composition, all six LA | `all` | all six fields |
| Lab-XCT | `target_selection, calibration_factor` | no blank, no aggregation fields |
| TEM | `target_selection, calibration_factor, aggregation, aggregation_qc` | **no blank** — no analytical blank in TEM |
| SEM-FIBSEM, SEM-Imaging | `target_selection` | imaging techniques: nothing to calibrate, aggregate or blank |
| Solution Q, SF, MC | `calibration_factor, blank, aggregation, aggregation_qc` | **no target selection** — bulk techniques have no target to select |

Read the pattern rather than the list: **imaging techniques select a target but do not aggregate;
bulk techniques aggregate but have no target.** The blocks encode real analytical differences, which
is why they are conditions and not just a checklist.

## What follows for schema generation

**A technique schema cannot `$ref` the whole module.** Composing all six fields into Lab-XCT would
add `Procedural Blank Level` to a technique that has no blank — and because five of the six fields
are `Basic` on at least one tier, most of those additions become *requirements the table never
stated*. Of the 18 (field × table) pairs excluded by blocks, **15 would become required** if
composed blindly. Only `Pre-Analysis Imaging and Screening` (Advanced/Editable) is optional.

`allOf` intersects constraints and cannot relax them, so there is no repairing this downstream: a
technique that composes a required field cannot opt out of it. The selection has to happen at
composition time.

So the module building block exposes **one `$def` per block per side**, and a consumer composes the
blocks its manifest entry names:

```yaml
allOf:
- $ref: ../../../BaseSchema/tappDefinition/schema.yaml
- $ref: ../../../BaseSchema/modules/reportingCore/schema.yaml#/$defs/TargetSelection_Procedure
- $ref: ../../../BaseSchema/modules/reportingCore/schema.yaml#/$defs/CalibrationFactor_Procedure
- type: object
  properties: {}   # only what this technique owns
```

rather than a single `ProcedureIdentification` covering all six. A `$ref` naming a `$def` resolves
to that `$def` alone, so a consumer carries only the blocks it selected.

`AllBlocks_Procedure` / `AllBlocks_Analysis` are also emitted, as the convenience for the ten TAPPs
whose entry reads `"blocks": "all"`.

## Checking it

`tools/module_conflict_check.py` reads the block declarations and compares only the fields a
consumer actually takes. Before it did, it reported `ADDS 18`; it now reports `ADDS 0` and states
that 18 pairs were not compared and why.

The general lesson is worth keeping, and is why this file survives its subject: **a module's field
list is not automatically its contract with a consumer.** `ReportingCore` was the only conditional
module; **none is today**, and `"conditional": true` remains the flag to test. The code tests the
flag rather than special-casing the name, so a future conditional module is handled without further
work — which is exactly what `docs/upstream-requests.md` §4a asks Ruolin to use for `Sampling Unit
Name`.

## For the record

Absence of a block's fields from a consuming table is **correct** and needs no upstream request. An
earlier draft of `docs/upstream-requests.md` raised these 18 as a question for Ruolin; it had a
documented answer in his own README §9 and in the module's JSON, and the item was withdrawn.
