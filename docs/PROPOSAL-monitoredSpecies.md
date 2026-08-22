# Proposal: monitored species as dataset variables

**Status: DRAFT, shape agreed. Nothing here is implemented.** The five open questions in the first
draft have been settled by the reviewer and are recorded under *Decisions* below.

## What this is for

A monitored species (a "channel" in the current vocabulary) is an instrument selection position — a
mass, a Faraday cup, an energy-loss edge, an X-ray line. **Each monitored species IS a variable**,
and its configuration properties come from three different places. Today only two of those three
have a home.

The base already anticipates this. `tappDefinition.ChannelIdentifierColumn` carries
`ada:cdifPropertyPath: "#/schema:variableMeasured/schema:name"` and says the variable list "is
shared across a procedure's table parts rather than owned by any one of them". So "a channel is a
variable" is the stated intent; it is simply not built.

## The three origins

| origin | where it belongs | today |
|---|---|---|
| instrument configuration | the instrument, or one of its `schema:hasPart` components | exists |
| fixed by the procedure | `TappDefinition`, reached from `$Dataset.prov:wasGeneratedBy.prov:used` | exists — 27 read-only channel properties |
| assigned per analysis session | `$Dataset.schema:variableMeasured[]`, one object per monitored species | **does not exist** |

**No sidecar in any technique places a channel column on `$Dataset`.** That leaves 17
session-assignable channel property rows with nowhere to be reported (appendix below).

## Worked technique: Solution Q-ICP-MS v34

Its channel-keyed rows already span all three origins:

| metadata item | P / A tier | origin | placed today |
|---|---|---|---|
| Monitored Masses | Basic / Read-Only | declares the species domain | `ada:defaultChannels[]` |
| Interfering Species | Basic / Read-Only | procedure-fixed | `ada:channelColumns[]` |
| Interference Correction Method | Basic / Read-Only | procedure-fixed | `ada:channelColumns[]` |
| Isobaric Interference Corrections Applied | Basic / Read-Only | procedure-fixed | `ada:channelColumns[]` |
| Collision Gas Type | Basic / Read-Only | instrument part (CRC) | `schema:value` on the part |
| Reaction Gas Type | Advanced / Read-Only | instrument part (CRC) | `schema:value` on the part |
| **Dwell Time per Mass** | Basic / **Editable** | **session** | `ada:channelColumns[]` — procedure default only |
| **Ion Counter Dead Time** | Basic / **Editable** | **session** | **unplaced** |
| **Collision/Reaction Gas Mixture Ratio** | Advanced / **Editable** | **session** | **unplaced** |
| **Instrument Sensitivity** | N/A / **Advanced** | **session** | **unplaced** |

Note the convergence: three of the four session-level rows are exactly the rows the v34 migration
left unplaced. This model is what gives them a home.

## Shape

### TAPP side — the species definition

`ada:channelTemplate` / `ada:defaultChannels` **become the monitored-species list**. Every item in
that list has a corresponding `schema:variableMeasured` entry, and for user-friendliness the list
uses the same strings as the `schema:name` of those entries.

Each entry is a `schema:PropertyValueSpecification` carrying **its own `@id`** and the
procedure-fixed column values. The `@id` is what the dataset side points at.

```jsonc
// inside the TappDefinition
"ada:monitoredSpecies": ["66Zn", "67Zn", "68Zn"],          // matches schema:name below

"schema:variableMeasured": [
  {
    "@id": "ada:monitoredSpecies/solutionQicpmsTAPP/66Zn",
    "@type": ["schema:PropertyValueSpecification"],
    "schema:name": "66Zn",
    "schema:valueName": "monitoredSpecies66Zn",
    "ada:targetSpecies": [{ "@id": "ada:analyte/solutionQicpmsTAPP/Zn" }],
    "schema:additionalProperty": [
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": ["schema:PropertyValueSpecification"],
        "schema:readonlyValue": true,
        "schema:defaultValue": "40Ar26Mg, 32S34S"
      }
    ]
  }
]
```

The procedure-fixed column **values** live on the species object, not in the template. The template
defines a data *structure*; the per-species instances of those properties may vary.

`schema:readonlyValue` marks a procedure-fixed column — not a change of `@type`. That is the
Option A decision already applied to keyed-table columns.

### `$Dataset` side — the session record

One `schema:variableMeasured` entry per monitored species actually acquired.

```jsonc
"schema:variableMeasured": [
  {
    "@id": "_:species-66Zn",
    "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
    "schema:name": "66Zn",

    "schema:alternateName": ["Zn66_cps"],

    "cdif:isDefinedBy_RepresentedVariable": {
      "@id": "ada:monitoredSpecies/solutionQicpmsTAPP/66Zn"
    },

    "ada:reportedBy": { "@id": "_:instrument-agilent-7900" },

    "ada:targetSpecies": [{ "@id": "_:analyte-Zn" }],

    "schema:additionalProperty": [
      {
        "@id": "ada:parameter/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": ["schema:PropertyValue"],
        "schema:value": 50,
        "schema:unitText": "ms"
      },
      {
        "@id": "ada:parameter/solutionQicpmsTAPP/ionCounterDeadTime",
        "@type": ["schema:PropertyValue"],
        "schema:value": 35,
        "schema:unitText": "ns"
      }
    ]
  }
]
```

The five parts, and why each is there:

1. **`schema:alternateName`** *(proposed)* — the column key in the reported data table. Any
   `cdif:hasPhysicalMapping` tying that column to a file lives here too, never in the TAPP: the TAPP
   defines the species, the dataset says which column reports it.
2. **`cdif:isDefinedBy_RepresentedVariable`** — an object referent to the `@id` of the TAPP's
   `schema:variableMeasured` PropertyValueSpecification for this species. An **existing CDIF
   property**, not a new ADA one. `cdi:InstanceVariable` is a subclass of `cdi:RepresentedVariable`,
   so a reference pointing at an instance variable is well-formed.
3. **`ada:reportedBy`** *(proposed)* — **a union of instrument and instrument part.** For Q-ICP-MS a
   mass is measured by the single detector, so it points at the instrument; for MC-ICP-MS it points
   at the specific `Collector` part. Both must be expressible.
4. **`ada:targetSpecies`** *(proposed)* — the analyte(s) this species serves. A list, 0..\*.
5. **`schema:additionalProperty`** — session-assigned configuration, and **only** what the TAPP does
   not already fix read-only. Anything read-only is reached through the definition reference, not
   copied.

## Decisions

| question | decision |
|---|---|
| container for session configuration on a variable | `schema:additionalProperty`, as drafted |
| reference to the procedure definition | `cdif:isDefinedBy_RepresentedVariable`, an existing CDIF property, in place of a new `ada:definedBy` |
| species `@id` resolvability | a local identifier for now; a registry for cross-dataset consistency is a long-range goal |
| `ada:targetSpecies` cardinality | a list, 0..\*, revisable later |
| where procedure-fixed column values live | on the TAPP species object — the template defines only a structure, and per-species instances may vary |
| fate of `ada:channelTemplate` / `ada:defaultChannels` | they become the monitored-species list, one entry per `schema:variableMeasured`, using matching `schema:name` strings |

## Dependencies and prerequisites

1. **`cdif:isDefinedBy_RepresentedVariable` on `cdif:instanceVariable`** is being added upstream in
   `metadataBuildingBlocks`. The property already exists in CDIF (it is carried by
   `cdifDataStructureComponent`, and 38 occurrences already resolve into this repo's BaseSchema);
   what is new is its presence on the instance-variable shape. **This work waits on that
   propagating.**
2. **`@type: cdi:InstanceVariable` on every `schema:variableMeasured` value object — already
   satisfied.** Checked: all 130 variableMeasured value objects across the examples carry it, so the
   reference has a well-typed subject. This came partly from the same work that made a reported
   property on `variableMeasured` carry both `schema:PropertyValue` and `cdi:InstanceVariable`,
   since the base requires the latter. No action needed.
3. **Instruments and instrument parts have no `@id` today.** Verified across the examples: a part
   carries only `@type`, `schema:additionalType`, `schema:name`. `ada:reportedBy` cannot be built
   until they are identified. This is the single largest blocker.
4. **There is no channel-to-analyte relation.** The analyte domain is its own keyed table, and
   nothing relates a channel to the analyte it serves, so `ada:targetSpecies` has no existing basis.
   `Monitored Masses` is keyed `defines: channel per analyte`, which states the relation in prose
   only.
5. **The schema-path grammar cannot express a `$Dataset` channel placement.** All 43 channel-column
   rows resolve to `$MethodDefinition`.

## What would change

- **base** (`tappDefinition`, `geochemProduct` / `adaProduct`): a monitored-species variable shape;
  the monitored-species list replacing `ada:defaultChannels`; `@id` on instrument and instrument
  part; `ada:reportedBy` and `ada:targetSpecies`.
- **grammar** (`docs/SCHEMA_PATH_GRAMMAR.md`): a route for session-level channel properties onto
  `$Dataset.schema:variableMeasured[...]`.
- **generator** (`schema_path_emitter`): emit the species objects, and route channel-keyed rows by
  tier — read-only onto the TAPP species object, editable/session onto the dataset.
- **sidecars**: the session-assignable rows need `$Dataset` placements; four in Solution Q-ICP-MS are
  unplaced today and would be authored directly into this shape.

## Appendix — session-assignable channel properties with no `$Dataset` home

| technique | metadata item | A tier |
|---|---|---|
| EPMA v25 | Background Counting Time | Editable |
| EPMA v25 | Background Position(s) | Editable |
| EPMA v25 | Peak Counting Time | Editable |
| EPMA v25 | Dwell Time per Pixel | Editable |
| Solution Q-ICP-MS | Dwell Time per Mass | Editable |
| TEM v21 | EELS Background Subtraction Method | Editable |
| TEM v21 | EELS Sensitivity and Detection Limit | Basic |

Seven distinct items; 17 rows once counted across technique revisions. Derived from `Key by =
channel` rows whose path resolves to `ada:channelColumns[]` on `$MethodDefinition`.
