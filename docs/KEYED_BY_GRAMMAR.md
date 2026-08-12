# `Keyed By` → schema-path grammar

Written 2026-08-11 against the TAPP delivery in `TAPPS20260811/` — 16 TAPPs, 1691 content rows.
Every field name, tier, count and example is taken from those CSVs.

**Status: design proposal.** One part is already implemented — the tier rules on analyte columns
(§2.1). Everything else is unbuilt. §12 logs what has been decided and what is still open.

Column I (`Keyed By`) states what a field's value repeats over. It decides schema *shape*, and we
currently model one of its six domains. Companion reading:
`TAPPS20260811/README_TAPP_for_Schema_Generation.md` §4, and `SCHEMA_PATH_GRAMMAR.md` for the
families we already have.

---

## 1. The model

1. **A key names a domain**: `analyte`, `channel`, `reported property`, `sampling unit`,
   `standard`, `preparation step`.
2. **Exactly one field declares each domain**, marked `defines: X`. Its *value* supplies the
   members — and that value is authored when a TAPP instance is created, not fixed here.
3. **Each instance of the domain carries every property whose `Keyed By` names that domain.** So a
   keyed field is a **column of a table**, and the `defines:` field is the table's **row axis**.

We already have exactly this structure for one domain:

```
$MethodDefinition.ada:analyteTemplate.ada:analyteColumns[]     column definitions
$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes[]    row axis (the member list)
```

The proposal is to recognise that as the general case and instantiate it per domain.

### 1.1 The declaration may not be a list — and the schema cannot know

The member list is supplied by whoever authors a TAPP instance. **Column F is guidance, not an
enumeration** — for a `Text (free)` field it shows example syntax, and the author may or may not
follow it. So enumerability is a property of the *instance*, decided at authoring time, and the
generated schema cannot branch on it.

Rather than admit two shapes, **always emit the table**: a declaration that does not parse into
members yields a **one-row table whose row key is the text as written**. The fallback is then not a
separate branch but N=1. One family, one path, graceful degradation, and the referential-integrity
rule ("a keyed entry references a member of the defining field") holds either way.

Data types of the eight declaring fields:

| Data Type | declaring fields | members come from |
|---|---|---|
| `Text (free)` | Analyte · Monitored Isotopes · Collector Configuration · EELS Edges · Reported Variables and Units · Secondary Reference Materials | authored list, parsed |
| `Controlled list / Text` | Sampling Unit | **a type, not members** — see §5 |
| `Integer` | Number of Digestion Steps | ordinals 1..N — see §6 |

### 1.2 The parse belongs to the authoring app

Splitting the declaration into members is a pipeline responsibility, and the right place is the
forms app at TAPP-instance authoring — split it, show the author the rows just created, let them
correct it. A bad split then shows up as "you declared 8 analytes, here they are" instead of
surfacing as a malformed table later.

That matters, because the examples in the library do not agree with one another:

```
Analyte                'Fe, O, Si, Mg, Ca, Al' | 'Fe, O, Si, Mg, Ca, Al, Ti (EDS); Fe, O (EELS)'
Reported Variables     'Element concentration (ppm); oxide (wt%)'
Secondary Ref Mat.     'BHVO-2 (Fe isotopes; Dauphas & Rouxel 2006 compilation) | BCR-2 | …'
EELS Edges             'Fe L2,3 (707 eV), O K (532 eV)'
```

Three distinct hazards:

1. **The outer `|` separates alternative example strings, not members.** `Analyte`'s three chunks
   are three illustrations; members within each are comma-separated.
2. **The member separator differs by field** — comma for `Analyte` and `EELS Edges`, semicolon for
   `Reported Variables and Units`.
3. **Separators occur inside members.** `Fe L2,3 (707 eV)` has a comma in the edge name;
   `BHVO-2 (Fe isotopes; Dauphas & Rouxel 2006 compilation)` has a semicolon inside parentheses.
   Naive splitting corrupts both, and silently — the result still looks like a list.

Parenthesis-aware splitting handles (3). Nothing handles (1) without the author.

### 1.3 Naming

| domain | template | columns | row axis |
|---|---|---|---|
| analyte | `ada:analyteTemplate` | `ada:analyteColumns[]` | `ada:defaultAnalytes[]` |
| channel | `ada:channelTemplate` | `ada:channelColumns[]` | `ada:defaultChannels[]` |
| reported property | `ada:reportedPropertyTemplate` | `ada:reportedPropertyColumns[]` | `ada:defaultReportedProperties[]` |
| sampling unit | `ada:samplingUnitTemplate` | `ada:samplingUnitColumns[]` | `ada:samplingUnitType` (scalar) |
| preparation step | — (ordinal, §6) | — | `schema:numberOfItems` |
| standard | — (never standalone, §7) | — | `ada:secondaryReferenceMaterials[]` |

---

## 2. `analyte` — 77 rows, 24 fields, 13 TAPPs

Declared by `Analyte` (`C=Basic, D=Editable`). Consumers include `Background Counting Time`,
`Diffracting Crystal`, `EPMA Technique per Analyte`, `Blank Correction`.

```
$MethodDefinition.ada:analyteTemplate.ada:analyteColumns[]
$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes[]
```

`ada:cdifPropertyPath: "#/schema:variableMeasured/schema:name"` **stays on the analyte identifier
column** — see §4 for why the conflict it appeared to create is not one.

### 2.1 Column tiers — IMPLEMENTED 2026-08-11

A column's requiredness follows its tiers, exactly as parameter templates do:

- **C=Basic** → the procedure must state it: `ada:tier: M`, `schema:defaultValue` declared and
  **required**
- **C=Advanced** → `ada:tier: R`, `schema:defaultValue` declared, optional
- **C=N/A** → `ada:tier: O`, no default (the procedure does not specify the column)

`analyte_column_def()` previously hardcoded `ada:tier: "M"` for every column and declared no
default at all, so a column default had nowhere to live and no type. Only the base's
analyte-identifier column is unconditionally `M`, and that lives in `tappDefinition`.

After the fix, of 116 registry defs: 43 `R` with default, 34 `M` with required default, 10 `O`,
and 29 still hardcoded `M` — the last being legacy `_tapp_lib` output (27) and the archived
`semTAPP` (2), which the path-driven route does not regenerate.

---

## 3. `channel` — 47 rows, 9 fields, 10 TAPPs

Declared by **three different fields** depending on technique: `Monitored Isotopes` (ICP-MS),
`Collector Configuration` (MC-ICP-MS), `EELS Edges` (TEM). A channel is an **instrument selection
position** — a mass, a Faraday cup, an energy-loss edge, an X-ray line.

It does not belong under `schema:hasPart`: that selector keys on component *type* (one EDS
detector, one ICP source), whereas channels are *instances* of one type.

```
$MethodDefinition.ada:channelTemplate.ada:channelColumns[]
$MethodDefinition.ada:channelTemplate.ada:defaultChannels[]
```

Hardware-per-position consumers (`Faraday Cup Amplifier Resistor Values`, `Ion Counter Dead Time`,
`Faraday Cup Gain Calibration Method`) are columns like any other — the cup *is* the row.

### 3.1 OPEN: channel and analyte are not bound, and they overlap

`Monitored Isotopes` describes itself as *"Specific isotope(s) monitored **per analyte element** in
this procedure, including any interference-monitor masses"* — so the relationship exists in prose
and nowhere machine-readable.

Underneath that, **`analyte` means different things per technique**:

```
EPMA         Analyte = "The element(s) measured by this procedure"
LA-Q-ICP-MS  Analyte = "Isotopes (mass/charge) this procedure is designed to measure"
```

In ICP-MS the two domains largely coincide, channel additionally covering interference monitors:

```
both analyte + channel:  10 TAPPs (all ICP-MS + TEM)
analyte only:             3 TAPPs (EPMA, SEM_Composition, SEM)
channel only:             0
```

Two candidate resolutions — either channels gain an `analyte` column, making the binding a column
of the channel table and needing no new machinery; or `analyte` gets a consistent cross-technique
definition. **To raise with Ruolin rather than model around.**

---

## 4. `reported property` — 81 rows, 14 fields; declared in all 16, consumed in 13

Declared by `Reported Variables and Units`:

> "The final variable(s) this procedure reports and their units — **distinct from Analyte and
> Monitored Isotopes, which record what was acquired.**"

Consumers: `Detection Limit Method`, `Age Calculation Method`, `Age Model`,
`Goodness-of-Fit or Dispersion Statistic`.

### 4.1 `variableMeasured` is shared, not owned

An earlier draft proposed moving `schema:variableMeasured` from analyte to reported property. That
was wrong. Analytes, channels and reported properties are *all* measured variables; the correct
reading is that a TAPP instance produces **several tables**, not one:

- an analyte result table
- a channel result table
- a reported-variable table

So the dataset has **parts** for these tables, each with its own physical mapping, all referencing
**one shared `schema:variableMeasured` list** (`schema:PropertyValue` / `cdi:InstanceVariable`).
That is the CDIF DataDescription shape — `cdi:PhysicalDataSet` per part over a shared logical
variable registry — so it is native rather than invented, and it dissolves the conflict instead of
relocating it.

Consequence: the number of parts is data-dependent. An EPMA procedure has an analyte table; an
LA-ICP-MS procedure has an analyte table *and* a channel table.

```
$MethodDefinition.ada:reportedPropertyTemplate.ada:reportedPropertyColumns[]
$MethodDefinition.ada:reportedPropertyTemplate.ada:defaultReportedProperties[]
$Dataset.schema:variableMeasured[]           <- shared registry, referenced by every table part
```

`Reported Variables and Units` also **declares the procedure's scope boundary** (README §10): a
derived quantity inside the list is in scope, anything beyond it belongs to a coupled procedure.

---

## 5. `sampling unit` — 14 rows, 6 fields; declared in all 16, consumed in 11

Declared by `Sampling Unit`, Data Type `Controlled list / Text`:

> `Whole sample | Aliquot | Grain | Spot | Analysis point | Phase | Sub-volume | Region of interest`

Being a controlled list, **Column F here IS an enumeration** and should generate
`anyOf: [enum, string]` for the field's own value (§10). What it enumerates is *subdivision types*,
not domain members: the author picks `Spot`; how many spots exist is analysis-time content. So the
row axis is scalar on the procedure side and populated on the dataset side.

Consumers split across the two roots, which is good evidence the model is right:

| field | C | D | |
|---|---|---|---|
| `Beam Current` | Basic | Editable | procedure default, per-spot override |
| `Phase Identification Method` | Basic | Read-Only | procedure only |
| `Analysis Location/Spot Coordinates` | **N/A** | Basic | analysis only |
| `Minimum Resolvable Feature Size` | **N/A** | Advanced | analysis only |

```
$MethodDefinition.ada:samplingUnitType                              'Spot'
$MethodDefinition.ada:samplingUnitTemplate.ada:samplingUnitColumns[]
$Dataset.prov:wasGeneratedBy.schema:object[@type='…materialsample']
        .schema:hasPart[].schema:additionalProperty[schema:name='…'].schema:value
```

`.schema:hasPart[]` rather than properties hung straight off the sample: a sampling unit is a
*subdivision*, and there are many per sample. Attaching directly works only for `Whole sample`.

---

## 6. `preparation step` — 9 rows, 3 fields, 3 TAPPs (ordinal)

Declared by `Number of Digestion Steps`, Data Type **Integer** — the giveaway that steps are
**ordinal, not named**. Consumers: `Digestion Acid(s)`, `Digestion Temperature`,
`Digestion Duration`.

`schema:actionProcess` is multi-typed `["schema:HowTo", "schema:ItemList"]` so that
`schema:numberOfItems` is in range — `numberOfItems` has `domainIncludes: ItemList`, and `HowTo` is
a `CreativeWork`, so `HowTo` alone would be a range violation.

```jsonc
"schema:actionProcess": {
  "@type": ["schema:HowTo", "schema:ItemList"],
  "schema:name": "Sample preparation",
  "schema:numberOfItems": 2,
  "schema:step": [
    { "@type": "schema:HowToStep", "schema:position": 1, "schema:name": "digestion 1",
      "ada:digestionAcid": "HF–HNO3", "ada:digestionTemperature": 120,
      "ada:digestionDuration": "48 h" },
    { "@type": "schema:HowToStep", "schema:position": 2, "schema:name": "digestion 2",
      "ada:digestionAcid": "HNO3 only", "ada:digestionTemperature": 90,
      "ada:digestionDuration": "12 h" } ] }
```

**`schema:position` is authoritative; the name is only a disambiguator.** Appending the position to
the step name lets the existing selector-keyed grammar
(`schema:step[schema:name='digestion 1']`) address individual steps, so **no ordinal family is
needed** — an earlier draft wrongly claimed the grammar had to change here. The cost is that the
name becomes data-dependent and will not field-match across procedures with different step counts;
acceptable while `schema:position` carries the ordering.

---

## 7. `standard` — declared by 12 TAPPs, **0 direct consumers**

Declared by `Secondary Reference Materials`. No field is keyed by `standard` alone; it exists only
as the outer axis of `standard x reported property`. So no standalone per-standard table — just the
member list:

```
$MethodDefinition.ada:secondaryReferenceMaterials[]
```

---

## 8. Cross-products

`A x B` is **ordered**: "for each A, one value per B".

### `standard x reported property` — 33 rows, 7 fields, 12 TAPPs

The QA/QC table: `Analytical Accuracy`, `Analytical Precision`, `Between-Session (Long-Term)
Analytical Precision and Assessment Method`, `In-Run Isotope Ratio Reproducibility and Assessment
Method`. Nearly all `C=Advanced, D=Basic` — measured at analysis time.

It reuses the existing `dqv:hasQualityMeasurement` family. The composite label is kept for display,
with the two axes carried as siblings so they remain queryable:

```jsonc
"dqv:hasQualityMeasurement": [
  { "dqv:isMeasurementOf": "GOR132-G REE concentrations",
    "ada:standard": "GOR132-G",
    "ada:reportedProperty": "REE concentrations",
    "dqv:value": "within ±5% of GeoReM preferred values (n=15)" },
  { "dqv:isMeasurementOf": "GOR132-G Nb concentration",
    "ada:standard": "GOR132-G",
    "ada:reportedProperty": "Nb concentration",
    "dqv:value": "+8% (known matrix sensitivity)" } ]
```

Composite alone would have made "everything measured on GOR132-G" unanswerable without string
surgery; the siblings avoid that at the cost of two extra properties per node.

### `sampling unit x reported property` (6 rows) · `sampling unit x analyte` (3 rows)

`Detection Limit` and `Counting Statistics Error`. These are **columns of the per-spot result
table** — one row per sampling unit, carrying a detection limit and a counting-statistics error for
that spot — not QA/QC entries. Per-spot granularity at this level is expected to be unusual.

---

## 9. `pair: reported property` — 7 rows, 2 fields, 4 TAPPs

Unordered pair. The three U-Pb variants carry both fields; `Solution_MC-ICP-MS` carries
`Error Correlation` alone.

```jsonc
"ada:errorCorrelation": [
  { "ada:between": ["206Pb/238U", "207Pb/235U"], "schema:value": 0.83 } ]
```

The two do **not** land in the same place — their analysis tiers differ:

| field | C | D | home |
|---|---|---|---|
| `Error Correlation Between Reported Quantities` | Advanced | **Basic** | dataset `additionalProperty` |
| `Discordance Definition and Values` | Advanced | **Read-Only** | procedure side, inherited |

---

## 10. Column E → Column F handling

Column F's meaning depends on Column E, and getting this wrong over-constrains the schema. Across
the delivery's 1691 content rows:

| Column E | rows | emit |
|---|---|---|
| `Controlled list` | 217 | `enum: [...]` from splitting F on `\|` |
| `Controlled list / Text` | 74 | `anyOf: [enum, string]` |
| `Text (free)` | 951 | `type: string` plus **`examples: [...]`** |

`examples` is a JSON Schema 2020-12 annotation with no validation effect, so the guidance stays
visible to a form builder or a human reader without constraining anything. Piping a `Text (free)`
Column F into an `enum` is, per README §6, the most common way to over-constrain a generated
schema.

When building `examples`, split on the outer `|` — those *are* alternative example strings — and
strip the `e.g.,` prefix. Do not split further; see §1.2.

---

## 11. What the grammar needs

| # | family | rows served |
|---|---|---|
| 1 | `reportedPropertyColumns[]` + shared `$Dataset.schema:variableMeasured[]` | 81 + 16 |
| 2 | `channelColumns[]` / `defaultChannels[]` | 47 + 10 |
| 3 | `dqv:hasQualityMeasurement` with `ada:standard` / `ada:reportedProperty` siblings | 42 |
| 4 | `samplingUnitColumns[]` + `schema:object…hasPart[]` | 14 + 16 |
| 5 | `pair:` shape | 7 |

All additive. `preparation step` needs no new family — §6.

---

## 12. Decisions

Settled 2026-08-11:

1. **`variableMeasured` stays shared**, referenced by every table part; it is not owned by analyte
   or by reported property. §4.1
2. **Each keyed domain yields its own table**, and the dataset carries parts for them. §4.1
3. **`actionProcess` is multi-typed** `["schema:HowTo","schema:ItemList"]`; `schema:position` is
   authoritative and the step name is a disambiguator. §6
4. **QA/QC keeps the composite `dqv:isMeasurementOf` label** for display, with `ada:standard` and
   `ada:reportedProperty` as siblings. §8
5. **`Text (free)` Column F becomes `examples`**, never `enum`. §10
6. **An unparseable declaration yields a one-row table**, not a second schema shape. §1.1
7. **Column tiers follow the procedure-level tier** — implemented. §2.1

Open:

1. **The channel/analyte binding**, and the shifting definition of `analyte` across techniques.
   §3.1 — for Ruolin.
2. **Per-domain templates, or one generic keyed table?** This document instantiates the
   `analyteTemplate` precedent per domain. A generic
   `ada:keyedTable[ada:key='analyte'].ada:columns[]` would be more uniform and would make
   cross-products fall out as two keys, but breaks from what ships today.
3. **Where the parse-and-confirm step lives** in the forms app. §1.2
