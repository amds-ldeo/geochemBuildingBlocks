# Proposal: monitored species as dataset variables

**Status: DRAFT for review. Nothing here is implemented.** Property names marked *(proposed)* are
invented for this draft and are the part to argue with.

## What this is for

A monitored species (a "channel" in the current vocabulary) is an instrument selection position — a
mass, a Faraday cup, an energy-loss edge, an X-ray line. The reviewer's framing is that **each
monitored species IS a variable**, and its configuration properties come from three different
places. Today only two of those three have a home.

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

Each monitored species the procedure defines becomes an entry in
`TappDefinition.schema:variableMeasured`, typed `schema:PropertyValueSpecification`, carrying **its
own `@id`** and the procedure-fixed column values. That `@id` is what the dataset side points at.

```jsonc
// inside the TappDefinition
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

`schema:readonlyValue` is what marks a procedure-fixed column — not a change of `@type`. That is the
Option A decision already applied to keyed-table columns.

### `$Dataset` side — the session record

One `schema:variableMeasured` entry per monitored species actually acquired.

```jsonc
"schema:variableMeasured": [
  {
    "@id": "ex:session-2026-03-11/species/66Zn",
    "@type": ["schema:PropertyValue", "cdi:InstanceVariable"],
    "schema:name": "66Zn",

    "schema:alternateName": ["Zn66_cps"],

    "ada:definedBy": { "@id": "ada:monitoredSpecies/solutionQicpmsTAPP/66Zn" },

    "ada:reportedBy": { "@id": "ex:session-2026-03-11/instrument/agilent-7900" },

    "ada:targetSpecies": [{ "@id": "ex:session-2026-03-11/analyte/Zn" }],

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
2. **`ada:definedBy`** *(proposed)* — an object referent to the `@id` of the TAPP's
   `schema:variableMeasured` PropertyValueSpecification for this species.
3. **`ada:reportedBy`** *(proposed)* — **a union of instrument and instrument part.** For Q-ICP-MS a
   mass is measured by the single detector, so it points at the instrument; for MC-ICP-MS it points
   at the specific `Collector` part. Both must be expressible.
4. **`ada:targetSpecies`** *(proposed)* — the analyte(s) this species serves.
5. **`schema:additionalProperty`** — session-assigned configuration, and **only** what the TAPP does
   not already fix read-only. Anything read-only is reached through `ada:definedBy`, not copied.

## Prerequisites

1. **Instruments and instrument parts have no `@id` today.** Verified across the examples: a part
   carries only `@type`, `schema:additionalType`, `schema:name`. `ada:reportedBy` cannot be built
   until they are identified. This is the single largest blocker.
2. **There is no channel-to-analyte relation.** The analyte domain is its own keyed table, and
   nothing relates a channel to the analyte it serves, so `ada:targetSpecies` has no existing basis.
   `Monitored Masses` is keyed `defines: channel per analyte`, which states the relation in prose
   only.
3. **The schema-path grammar cannot express a `$Dataset` channel placement.** All 43 channel-column
   rows resolve to `$MethodDefinition`.

## What would change

- **base** (`tappDefinition`, `geochemProduct` / `adaProduct`): a monitored-species variable shape;
  `@id` on instrument and instrument part; the four reference properties.
- **grammar** (`docs/SCHEMA_PATH_GRAMMAR.md`): a route for session-level channel properties onto
  `$Dataset.schema:variableMeasured[...]`.
- **generator** (`schema_path_emitter`): emit the species objects, and route channel-keyed rows by
  tier — read-only to the TAPP definition, editable/session to the dataset.
- **sidecars**: the session-assignable rows need `$Dataset` placements; four in Solution Q-ICP-MS are
  unplaced today and would be authored directly into this shape.

## Open questions

1. **Is `schema:additionalProperty` the right container for session configuration on a variable**, or
   should those be direct `ada:` properties on the species object?
2. **Does the species `@id` need to be resolvable**, or is a document-scoped `ex:` identifier
   enough? This decides whether minting becomes a registry concern.
3. **Cardinality of `ada:targetSpecies`** — `Monitored Masses` is keyed "channel per analyte",
   implying many-to-one, but a mass-shift product may serve one analyte while deriving from another.
4. **Do the procedure-fixed column values belong on the TAPP species object** (as drafted), or stay
   in `ada:channelTemplate` with the species object referencing the table? The draft duplicates less
   but moves data out of the template.
5. **What becomes of `ada:channelTemplate` / `ada:defaultChannels`** — superseded by the species
   list, or retained as the column-definition table they are?

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
