# TAPP Composition Module: Group1 (Procedure Identification)

The seventeen identification fields every TAPP carries — who wrote the procedure, which technique
it implements, which laboratory runs it, when it was published, and on the analysis side, who ran
it and when.

This module is a **profile, not a vocabulary**. Every one of its fields maps to a property that
already exists on [`tappDefinition`](../../tappDefinition/) or [`adaProduct`](../../adaProduct/) —
`schema:name`, `schema:creator`, `schema:location`, `prov:wasGeneratedBy` and so on. It introduces
no `ada:` terms. What it contributes is the assertion that a conforming procedure carries these
properties, and that a defined subset of them is required.

## Why it exists

The 2026-08-11 library ships sixteen TAPP tables, and these seventeen fields appear in all of them.
Placing them independently in each technique means making the same modelling decision sixteen times
and letting sixteen copies drift apart. Composing this block instead makes the decision once.

The evidence that the block really is shared, rather than sixteen coincidentally similar sets of
fields, is that all nine curated schema-path sidecars agree unanimously on where every one of the
seventeen lives.

## The two `$defs`

A procedure and an analysis are separate documents in this repository, so the module exposes two
composable shapes:

| `$def` | composed into | carries |
|---|---|---|
| `ProcedureIdentification` | a TAPP schema (`prov:Plan`) | what the procedure asserts once |
| `AnalysisIdentification` | a technique detail schema (`schema:Dataset`) | what each run supplies fresh |

They live in one file because they are one upstream module with one version, and because both are
derived from the same seventeen rows — change a tier and both move together. A `$ref` naming a
`$def` resolves to that `$def` alone, so a detail schema composing `AnalysisIdentification` does not
carry the procedure half.

## Requiredness

Derived from the module's own two tier columns, per the TAPP tier matrix:

| tier | effect |
|---|---|
| Procedure-Level Basic | required in `ProcedureIdentification` |
| Procedure-Level Advanced | permitted, not required |
| Procedure-Level N/A | absent from the procedure; analysis-level only |
| Analysis-Level Basic | required in `AnalysisIdentification` — cannot be known until the run |
| Analysis-Level Advanced | permitted, not required |
| Analysis-Level Read-Only / Editable | inherited from the procedure, so not required again |

## Composing it

```yaml
allOf:
- $ref: ../../../BaseSchema/tappDefinition/schema.yaml
- $ref: ../../../BaseSchema/modules/group1/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties: {}   # only what this technique itself owns
```

Note that `allOf` composes constraints and cannot relax them: a technique that composes this module
accepts its required set in full. Column F (Example / Allowed Content) is consumer-owned per the
module manifest, so no enum is pinned here — a consuming TAPP may narrow a value space, never widen
it.
