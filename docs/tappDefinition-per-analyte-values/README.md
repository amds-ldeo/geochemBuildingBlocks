# Per-analyte values lifted out of the tappDefinition examples

Three tables of per-analyte column values that used to sit inside
`ada:analyteTemplate.ada:defaultAnalytes` in the `tappDefinition` examples. They were invalid
there, and a TAPP document has no valid home for them, so they are kept here rather than deleted.

## Why they moved

The schema is explicit:

> `ada:defaultAnalytes` — The analytes (analyzed constituents) this method targets by default —
> the ROWS of the per-analyte table. Each is **a bare string or a `schema:DefinedTerm` identifying
> the analyte**; per-analyte column **VALUES live in the analysis record, not here**.

The examples instead put a whole row object in each member:

```json
{"analyte": "SiO2", "beamCurrent": 6, "spectrometer": "WDS 1", "xrayLine": "Ka", ...}
```

Every such row was one validation error — 2, 9 and 21 of them, matching the row counts exactly.
That single mistake accounted for all three `tappDefinition` failures.

The examples now carry analyte identifiers only, which is what the schema allows, and validate.

## What is here

| file | from | rows | columns |
|---|---|---|---|
| `concord-glass-v1-0-6.json` | EPMA WDS tephra glass, Concord University | 2 | 17 |
| `nmnh-spinel-oxybar-v1.json` | EPMA WDS spinel oxybarometry, Smithsonian NMNH | 9 | 11 |
| `uoc-laicpms-glass-v1.json` | LA-ICP-MS volcanic glass trace elements, U. Cologne | 21 | 6 |

Each carries the original rows verbatim, the `analyteColumns` they correspond to, and a pointer
back to the example they came from.

The content is real and publication-derived — spectrometer assignments, peak and background
counting times, diffracting crystals, calibration standards, detection limits. It is worth keeping.

## What should happen to it

Per the schema, these values belong in an **analysis record** — a dataset instance conforming to a
technique profile, not a procedure definition. No analysis-record example exists for these three
procedures yet. When one does, this content is what should populate it.

Until then this directory is a holding pen, not a modelled artifact: nothing reads it, and it
conforms to no schema.

Worth noting as an open modelling question: a TAPP can state per-COLUMN defaults through
`analyteColumns` (each column is a `schema:PropertyValueSpecification` with a `schema:defaultValue`),
but it has no way to state a per-ANALYTE default — a different beam current for SiO2 than for TiO2,
say. These tables are exactly that shape, which is presumably why the examples put them where they
did.
