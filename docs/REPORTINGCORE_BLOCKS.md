# `ReportingCore` and its block system

Most TAPP modules contribute all their fields to every TAPP that composes them. **`ReportingCore`
does not.** Its six fields are grouped into five *blocks*, each carrying a condition, and a
consuming TAPP takes only the blocks that apply to it.

This is the one module where "composes `ReportingCore`" does not mean "has all of `ReportingCore`",
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

## Who takes what

`composed_tapps.json` records the selection on the module entry, as `"blocks": "all"` or a
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

The general lesson is worth keeping: **a module's field list is not automatically its contract with
a consumer.** `ReportingCore` is the only conditional module today — `"conditional": true` is the
flag to test — but the code tests the flag rather than special-casing the name, so a second one will
be handled without further work.

## For the record

Absence of a block's fields from a consuming table is **correct** and needs no upstream request. An
earlier draft of `docs/upstream-requests.md` raised these 18 as a question for Ruolin; it had a
documented answer in his own README §9 and in the module's JSON, and the item was withdrawn.
