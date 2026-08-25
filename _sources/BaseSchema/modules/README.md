# Composition modules

**Everything in this directory is generated.** Do not hand-edit a module's `schema.yaml`,
`examples.yaml`, `rules.shacl` or `description.md` — regenerate them from the sources below.

A module factors out fields that many analytical techniques share, so a shared field is defined
**once** instead of once per technique. `core` holds what every procedure has (laboratory, operator,
software, funding); `laserAblation`, `mcIcpms` and `solutionIntroduction` hold what a technique
family has; `blank`, `calibrationFactor` and `targetSelection` hold small cross-cutting concerns.

## How a module is built

Two inputs, one command:

| input | what it supplies |
|---|---|
| `tapp/Claude Skills for TAPP/modules/Module_<Name>.csv` (the `tapp/` submodule) | which metadata items the module owns, and their tiers and data types |
| `docs/modules/Module_<Name>.schemapaths.csv` | where each of those items lands — the schema path |

```bash
python tools/build_module_bb.py --write              # all modules
python tools/build_module_bb.py --module Core --write
```

The schema is assembled with the **same merger the technique overlays use**
(`schema_path_emitter.insert` / `to_schema`). A module field can be a nested instrument property or
a workflow-step parameter, not just a scalar, and re-deriving that placement logic here would be a
second implementation to keep in step with the first.

Change a path or a tier in the sidecar and re-running the build is the whole update.

## What a module exposes

Up to two **root `$defs`**, split by the root of the path, because a procedure and an analysis are
separate documents:

- **`ProcedureIdentification`** — from the module's `$MethodDefinition` paths; composed into a
  technique's `tapp/`
- **`AnalysisIdentification`** — from its `$Dataset` paths; composed into `detail/`

Plus one **`Param_<Side>_<name>` `$def` per parameter** the module publishes. Parameters are
separate because a module *cannot constrain* `schema:additionalProperty` — the technique already
closes that array with an `anyOf` over its own parameters, and `allOf` would make the two
unsatisfiable together. A module can only offer a branch the technique unions into its own `anyOf`.

`reportingCore` is conditional: it emits one `$def` per block per side, so a consumer takes only the
blocks that apply to it (see `docs/REPORTINGCORE_BLOCKS.md`).

A module with no placed root fields still emits a building block when it publishes parameters —
`blank` is the only one left in that state (`calibrationFactor` was too, until its keyed
`variableMeasured` rows were added). What it must never emit is an **empty** root `$def`, which
would assert that a conforming procedure carries nothing.

### Parameter shape and identity

Parameter `$defs` are **not** written here. `build_module_bb.emit_parameter_defs()` delegates to the
two canonical emitters in `build_tapp.py`, chosen by side:

| side | emitter | `@type` |
|---|---|---|
| `Procedure` (`$MethodDefinition`) | `param_template_def` | `schema:PropertyValueSpecification` |
| `Analysis` (`$Dataset`) | `param_value_def` | `schema:PropertyValue` |

A hand-rolled variant that emitted a hybrid of the two made every module parameter differ
structurally from the technique parameter it duplicates — 181 apparent conflicts that were one
defect.

A technique mints `ada:parameter/<TAPP>/<name>`, so a shared parameter would otherwise exist once
per consuming TAPP. A module-owned parameter instead gets **one** identity:
`ada:parameter/module/<Module>/<name>`.

## Where modules are used

Membership is declared in **`tapp/composed_tapps.json`** and matched on the **source table's
filename**, so a technique stops composing modules the moment it is repointed at a table the
manifest does not list. All 16 techniques compose modules today.

`tools/module_composition.py` decides what a technique drops, and only when the module demonstrably
provides the field: the module has it, the field has a placement in the module sidecar, and the
`$def` exists.

**A covered row is dropped from the technique's own overlay** — otherwise the shared field is
defined twice and the technique's copy silently wins wherever the two differ, which is the drift
composition exists to end. That applies to the schema *and* to the generated examples: where a
module covers an item, the module owns the placement in both.

Correspondingly, a module-covered row in a technique sidecar carries **no Schema Path** — it is
marked `Source = module` with a note naming the owner. The row itself stays, because
`migrate_sidecar` diffs Metadata Items against the workbook and a deleted row returns as
"new (flagged)" at the next delivery.

## Two rules worth knowing before editing a module

**A module must not hardcode an instrument selector it cannot guarantee.** `core` once placed
`Instrument Manufacturer` under `schema:instrument[schema:additionalType='SEM']`; because `core`
composes into *every* technique, that put the instrument metadata of every ICP-MS, TEM, XCT and EPMA
procedure on an SEM node. A family module naming its own component (`laserAblation` →
`Laser Ablation System`, `mcIcpms` → `ICPMS`) is fine, because that token is true for every
consumer. A universal module naming a technique-specific one is not.

**`$ref` depth differs from a technique's.** Modules sit at `_sources/BaseSchema/modules/<name>/`,
two hops shallower than `_sources/techniqueProfile/geochemProfile/<TECH>/tapp/`, but
`build_module_bb` reuses `schema_path_emitter`'s technique-depth `REF_MAP`. A BaseSchema target
written as `../../../../BaseSchema/X` climbs past the repo root and must be `../../X`;
`build_module_bb._reref_module_depth()` does that rewrite. Only the full CI postprocess catches this
class of break — `validate_examples.py` does not.

## Checking

```bash
python tools/module_conflict_check.py               # TIGHTENS / LOOSENS / ABSENT / ADDS per consumer
python tools/module_conflict_check.py --parameters  # module vs technique parameter shapes
python tools/seed_module_sidecars.py --write        # fill a module sidecar from technique consensus
python tools/simplify_sidecars.py                   # report technique rows a module already places
```

`seed_module_sidecars` infers placements from technique **consensus**, which is how the SEM
instrument selector got into `core` — the majority vote is not always right for a universal module.
Treat a seeded row as a proposal, not a decision.
