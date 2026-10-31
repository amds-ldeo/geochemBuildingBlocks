# Proposal: five keyed-value templates

**Status: DRAFT for discussion with Ruolin. Nothing here is implemented.**
Design by Stephen Richard, 2026-10-30/31. Measurements and JSON shapes drafted with Claude.
Companion to [amds-ldeo/tapp#22](https://github.com/amds-ldeo/tapp/issues/22).

The TAPP workbooks' `Key by` column declares that a field is an attribute of some *keyed value* —
a target species, a monitored property, a standard. Today 1,085 rows across the 61 live sidecars
are keyed, and the structures they need mostly do not exist. This proposes five, and says what
each looks like on the procedure side and in a dataset record.

---

## 1. What a keyed value is, and the one rule that makes it implementable

A keyed-value field defines a **template**: a list of identified things, plus the properties that
may be assigned to each. It is realised either as a JSON object in the metadata or as a **table in
a dataset distribution** — and which one follows from how the property varies:

| the property… | goes to |
|---|---|
| varies per analysis — per sample, per sampling unit, per standard | `schema:variableMeasured` / InstanceVariable, **plus** a DataStructure with `cdif:hasPhysicalMapping` locating it in the distribution's files |
| is fixed for the session but editable in the procedure | `schema:additionalProperty` with `schema:propertyID` into the parameter registry |
| is read-only | the procedure definition, **copied** into the record that uses it |

Variability picks the destination, not the tier column. The tier matrix already encodes
read-only vs editable, so rows 2–3 explain what it does; row 1 is the new requirement.

**The copy in row 3 is deliberate denormalisation,** so a record reads without dereferencing its
TAPP. The procedure stays the source of truth and the copy is one-way. This is *not* a
counterexample to the one-home rule that retired `ada:procedureAuthorDescription` — say so when
implementing, because it looks like one.

### Tier routing, within a template

| Protocol Tier | Analysis Tier | where the attribute goes |
|---|---|---|
| Basic | — | required, as a named `ada:<name>` field on the item |
| Advanced | — | `schema:additionalProperty` on the item |
| N/A | Basic | record side only, and **required to have a value** there |

### The rule that keeps it buildable: list-order matching, and the flatten fallback

An item's attributes are matched to the defining list **by list order** — the *n*th entry in a
keyed field belongs to the *n*th declared item. The workbooks carry no syntax guaranteeing those
lists align, and inspection of Ruolin's example values shows cases where they cannot be matched.

**When the lists cannot be matched, flatten rather than guess.** Emit a one-element list whose
single object carries the raw strings:

```json
"ada:monitoredPropertyTemplate": {
  "ada:defaultMonitoredProperties": [
    {
      "schema:name": "monitoredPropertyList",
      "ada:monitoredPropertyPerTargetSpecies": "<the raw defining cell>",
      "ada:backgroundPosition": "<the raw keyed cell, unparsed>"
    }
  ]
}
```

This is the difference between a prototype that ships and one that doesn't. A parser that must
succeed will either fail loudly on real workbooks or, worse, mis-associate attributes silently.

### `applies to all` is structural, not a string

Measured over the EPMA / LA-Q-ICPMS / SEM-composition literature assessments: most keyed-value
cells are unassigned, and where values exist they are usually **constant across the domain** — of
86 example cells on the `target material x target species` key, 33 are populated and **32 key on
"all"**. The one that genuinely varies is McCoy+2025_UA.

So: **a one-element list IS "applies to all"**, with the phrase carried as a label, never as the
value. A literal `"applies to all"` in a value slot would be a fourth magic string beside
`missing`, the OGC nil token, and the `None` / `Other` / `N/A` trio — and CLAUDE.md forbids adding
a second sentinel. Cardinality carries the meaning; a consumer that ignores labels still reads it
correctly.

**Do not resolve "mostly empty" by relaxing the workbook constraints.** The ADA corpus predates
TAPP generation. Design the representation so "absent" and "constant over the domain" are
*expressible* — which is what the one-element list is for.

---

## 2. Where things stand, measured

61 live sidecars, 4,102 rows, of which 1,085 are keyed. For the five topics:

| topic | sidecar rows | **distinct metadata items** | workbooks | in its own container | in a `targetSpecies` container | elsewhere / flat | module-owned |
|---|---|---|---|---|---|---|---|
| TargetSpecies | 53 | 10 | 13 | 40 | 0 | 13 | 0 |
| TargetMaterials | 41 | 6 | 16 | 16 | 4 | 21 | 0 |
| MonitoredProperty | 145 | 28 | 13 | 35 | 27 | 63 | 20 |
| Standards | 45 | 6 | 12 | **0** | **33** | 3 | 9 |
| ReportedProperties | 258 | 20 | 59 | **0** | **21** | 19 | 218 |

**Read the row count as multiplicity, not surface.** The same metadata item recurs across
workbooks, and twice within one workbook when it is dual-homed (`$MethodDefinition` *and*
`$Dataset` — EPMA carries `Beam Diameter` both ways). The design surface is **70 distinct
items**, not 542 rows.

**The two zeros are the finding.** There is no `standardTemplate` and no
`reportedPropertyTemplate`, so 54 rows are filed under target species *because there is no box for
them*. That is a missing structure, not a mis-filing — the generator put them in the only keyed
container that existed.

Containers that exist today:

| container | uses |
|---|---|
| `ada:targetSpeciesTemplate` / `…Columns` | 135 / 122 |
| `ada:monitoredPropertyTemplate` / `…Columns` | 80 / 70 |
| `ada:targetMaterialTemplate` / `…Columns` | 34 / 18 |
| `ada:monitoredElements` | 6 — retire, see §4 |

"Flat" lumps two different things: fields that legitimately live elsewhere (`Collector
Configuration` belongs on `schema:instrument[…].schema:hasPart[…]`, not in a keyed table) and
fields with genuinely nowhere to go. Only the second kind needs a destination.

### Two cross-products remain, and one axis is nearly unexercised

| key | rows | workbooks |
|---|---|---|
| `standard x reported property` | 33 | 12 |
| `target material x target species` | 12 | 12 |
| `target material x monitored property` | 6 | 3 |

Two that existed at v88 are gone (`combined result x reported property`,
`sample > sampling unit x reported property`).

---

## 3. Cardinality differs by technique family, and the design must hold both ways

| family | target species | target materials | monitored properties |
|---|---|---|---|
| electron probe (EPMA, SEM, TEM) | mean 7.4, max 14 | mean 1.8, max 7 | **absent — 0 of 32 examples** |
| mass spectrometry | mean 13.6, max 54 | mean 1.7, max 14 | mean 7.5, max 18 (n=21) |

- **Electron probe**: target species and monitored property are the same thing, and the fold is
  *total* — no EPMA/SEM example carries a monitored-property list at all. The experiment may
  however report several **target materials** from one sample (different mineral grains in a thin
  section).
- **Mass spectrometry**: typically a single target material (zircon, K-spar, solution), but one
  target species maps to **many** monitored properties — U to `235U` and `238U`.

So the species↔monitored relationship is many-to-many, and neither axis may be assumed 1:1. The
two families fan out on *different* axes, which is why the cross-product keys exist.

**A warning about reading the corpus.** The material fan-out this design exists for is barely
exercised: 58 of 99 electron-probe examples carry exactly one target material, and 38 of 57
mass-spec examples carry zero or one. The same shape recurs across this repo — 32 of 33 keyed
cells key on `all`; 7,442 of 7,446 ADA records carry `hasPart` and 4 are monolithic. The corpus
will consistently argue for dropping the axis the design needs. **Rare is not optional.**

### Open design question for §3

Does electron probe get an explicit monitored-property list that duplicates its target species, or
stay folded with a **declared 1:1 identity**? The declaration avoids double-entering 7–14 elements
per definition and matches the measurement. Recommended: declare the identity, do not duplicate.

---

## 4. One monitored-property container, with the kind as a property

The concept is spelled three ways, and the split is **by technique family, carrying real
information** — not drift:

| item name | occurrences | workbooks | family |
|---|---|---|---|
| `Monitored Masses` | 30 | 18 | mass spectrometry |
| `Monitored Elements` | 6 | 6 | electron probe |
| `X-ray Detection Method per Monitored Element` | 6 | — | electron probe |

**The generic container name is already settled, and for this exact reason.**
[`PROPOSAL-monitoredSpecies.md`](PROPOSAL-monitoredSpecies.md) landed `monitoredSpecies` →
`monitoredProperty` precisely because "the word 'species' was dropped — the thing selected is not
always a chemical species", and it already names the kinds in play: *a mass, a Faraday cup, an
energy-loss edge, an X-ray line*. It also settled the record-side mapping this proposal depends on:
**each monitored property IS a variable**. So §4 and §6 are not new arguments — they extend a
decision already taken, which is why the recommendation below is to finish it rather than revisit
it.

A flat rename of the ITEM names to `Monitored Property` would, however, **destroy** the
element/mass distinction across 36 item names. Instead:

- **one container**, `ada:monitoredPropertyTemplate`, retiring `ada:monitoredElements[]` (6 rows);
- **the kind carried as a property** on each monitored property — `element`, `mass`,
  `absorptionCoefficient`, `intensity`, …

That also answers the granularity question for x-ray absorption and spectroscopy: those become
*values* of the kind property, not new field names — which keeps spectroscopy, XCT and AFM
expressible without settling them now.

**All five topics stay optional.** For a technique family whose shape is unexplored, a conditional
that cannot be evaluated must degrade to optional, never to required.

---

## 5. The five templates

Procedure side, under `$MethodDefinition`. Each `*Template` is an object holding a `default*[]`
list (the declared items) and a `*Columns[]` array (the per-item column definitions). Every item
carries an identifier, because associations are by reference.

### 5.1 TargetSpecies — `ada:targetSpeciesTemplate` (exists)

The elements or molecules of interest. The definition declares the complete list; an instance may
report a subset.

```json
"ada:targetSpeciesTemplate": {
  "ada:defaultTargetSpecies": [
    {"@id": "ex:species/Si", "schema:name": "Si", "ada:targetSpeciesIdentifier": "Si"}
  ],
  "ada:targetSpeciesColumns": [
    {"schema:valueName": "targetSpeciesIdentifier", "ada:dataType": "string",
     "ada:fieldScope": "identifier", "schema:readonlyValue": true}
  ]
}
```

### 5.2 TargetMaterials — `ada:targetMaterialTemplate` (exists)

The kinds of material analysed — minerals, rock types, or `powdered sample` / `aqueous liquid`.
Each material may carry its own target-species subset and its own procedure or instrument
parameters.

```json
"ada:targetMaterialTemplate": {
  "ada:defaultTargetMaterials": [
    {"@id": "ex:material/olivine", "schema:name": "olivine",
     "ada:targetSpeciesAnalysed": [{"@id": "ex:species/Si"}, {"@id": "ex:species/Mg"}],
     "ada:beamCurrent": {"schema:value": 10, "schema:unitText": "nA"}}
  ],
  "ada:targetMaterialColumns": [ ]
}
```

### 5.3 MonitoredProperty — `ada:monitoredPropertyTemplate` (exists; §4 applies)

What is actually measured — the raw data. Each monitored property associates with 0..* target
species. **With none, the field carries prose explaining the usage** — "monitored to correct the
Kβ overlap on Mn".

```json
"ada:monitoredPropertyTemplate": {
  "ada:defaultMonitoredProperties": [
    {"@id": "ex:monitored/238U", "schema:name": "238U",
     "ada:monitoredPropertyKind": "mass",
     "ada:targetSpecies": [{"@id": "ex:species/U"}]},
    {"@id": "ex:monitored/Kb-overlap", "schema:name": "Mn Kβ overlap monitor",
     "ada:monitoredPropertyKind": "element",
     "ada:targetSpecies": [],
     "schema:description": "monitored to correct the Kβ overlap on Mn"}
  ],
  "ada:monitoredPropertyColumns": [ ]
}
```

### 5.4 Standards — `ada:standardTemplate` (**NEW**)

Materials used to calibrate measures, applied during data processing. A standard has a
**standardization target**: one of a target species, a target material, or a monitored property.

```json
"ada:standardTemplate": {
  "ada:defaultStandards": [
    {"@id": "ex:standard/91500", "schema:name": "91500 zircon",
     "ada:standardRole": "primary",
     "ada:standardizationTarget": {"@id": "ex:species/U"},
     "schema:citation": {"schema:name": "Wiedenbeck et al. 1995",
                         "schema:url": "https://doi.org/10.1111/j.1751-908X.1995.tb00147.x"}}
  ],
  "ada:standardColumns": [
    {"schema:valueName": "standardIdentifier", "ada:dataType": "string",
     "ada:fieldScope": "identifier", "schema:readonlyValue": true}
  ]
}
```

Where the definition names no specific standards, **no default or read-only value can be assigned
to a reported property on a standard** — the columns are declared and left unvalued.

This **deprecates `standard x reported property`** (33 rows, 12 workbooks). Its information
becomes `ada:standardColumns` referencing entries in the reported-property list.

> **The asymmetry that makes this urgent.** `defines: standard` declares exactly one row,
> *Secondary Reference Materials*, in 12 workbooks. So the standard axis currently names
> **secondary** standards only, while **primary calibration standards exist nowhere as declared
> entities** — they are free text inside a cross-product cell. That is why
> `standard x reported property` has nothing to point at, and it is the concrete argument for
> tapp#22.

### 5.5 ReportedProperties — `ada:reportedPropertyTemplate` (**NEW**)

Final result values after processing. Each is linked to 1..* monitored properties, a target
species, and the standards used — **plus a description of the processing** that connects them.

```json
"ada:reportedPropertyTemplate": {
  "ada:defaultReportedProperties": [
    {"@id": "ex:reported/206Pb-238U-age", "schema:name": "206Pb/238U age",
     "schema:description": "Concordia age from corrected ratios",
     "ada:monitoredProperty": [{"@id": "ex:monitored/238U"}, {"@id": "ex:monitored/206Pb"}],
     "ada:targetSpecies": [{"@id": "ex:species/U"}],
     "ada:standardUsed": [{"@id": "ex:standard/91500"}],
     "ada:processingDescription": "..."}
  ],
  "ada:reportedPropertyColumns": [ ]
}
```

Every entry must carry a label and a definition. **218 of the 258 ReportedProperties rows are
module-owned**, so this template must be built in coordination with the composition modules, not
from the technique sidecars alone — the module `$def` decides, and `docs/modules/emitted.json`
records what it actually carries.

---

## 6. The record side

In a profile document describing a dataset:

| topic | becomes |
|---|---|
| ReportedProperties | `schema:variableMeasured[]` InstanceVariable objects, carrying only the **editable** attributes (Basic editable, or N/A Basic — the latter **required** to have a value) |
| MonitoredProperty | `schema:variableMeasured[]` InstanceVariables; attributes as `ada:` properties when Basic, `schema:additionalProperty` when analysis-only |
| Standards | a list of standards with values for the editable reported properties of each, plus a **variable identifying each standard** |
| sample | `prov:wasGeneratedBy / schema:object[]` — a list of samples, each with the editable properties, plus any detail-specific ones |
| sampling unit | variables in the data tables identifying the source sampling unit |

### sample

In the TAPP definition expect **one** `schema:object`, whose properties are read-only or defaults
— it defines the *kind* of sample the procedure targets. In a record, `schema:object` is a list of
actual samples. A form shows the read-only procedure properties as **non-editable heading text**
and copies them into each sample description.

*Wanted: a check that the analysed sample is consistent with the sample type the method definition
specifies.* Nothing does this today.

### sampling unit

The definition can only state the **types** of sampling unit and the name of the identifying
variable. In a record, any table reporting monitored or reported values must carry a field
identifying the source sampling unit — correlated to samples either by carrying both
`samplingUnitID` and `sampleID`, or via a separate mapping table that may also carry other
sampling-unit properties. A sampling unit may be identified by x–y coordinates.

**If samples or sampling units are referenced in the data, variables identifying those instances
must be declared.**

### `cdif:hasPhysicalMapping` is on the critical path — and is not greenfield

Measured on main: present in **18 of 657** examples, with `cdi:InstanceVariable` in 146,
`cdi:isStructuredBy` in 37 and `cdi:DimensionalDataStructure` in 36. There is a working pattern to
extend. The repo's existing note that physical mapping is absent-by-design holds only for
publication-derived examples with no data files; for per-analysis keyed properties it is required.

---

## 7. Plans: acquisition pass and preparation step

### acquisition pass (102 rows, 9 workbooks)

Parse `defines: acquisition pass` into a series of

```
$MethodDefinition.schema:actionProcess.schema:step[schema:name='Data acquisition']
```

steps, each taking its attributes from the fields keyed to `acquisition pass`:
Procedure-Level **Basic** becomes a required `ada:<name>` field on the step; **Advanced** becomes
a `schema:additionalProperty`; **N/A** appears only on the record side.

**If the defining list cannot be mapped**, all of it goes into **one** step named
`Acquisition multiple pass information`, with the raw defining cell as that step's description.

Correlating result values to the right acquisition pass requires each pass to have an identifier,
but **those relations live in the `cdif:hasPhysicalMapping` of an individual DataDownload** — the
shape of the delivered tables is determined by neither the TAPP nor the profile schema.

> **Two cautions, both load-bearing.** A `schema:step` selector literal is **sentence-case**, and
> the literal IS the node's identity — Title Case silently builds a second, separate step. And the
> step constraints are `if`/`then`, so a name that matches no `if` is not a failure: the
> constraints are **silently absent** and the record validates clean.

### preparation step (15 rows)

A plan of steps describing how samples are prepared — actions that may use software, reagents or
instruments, each with a name and description. In a record the steps may be repeated with values
for any editable property.

**It does not map to one literal.** Measured over the live sidecars, the preparation family is
three technique-specific step names:

| literal | uses |
|---|---|
| `Sample preparation` | 37 |
| `Sample digestion` | 18 — the solution ICP-MS route |
| `Ion milling` | 11 — the TEM route |

Route per technique, by the literal that technique's plan actually uses. Pinning
`Sample preparation` universally would match neither of the others — and by the `if`/`then` rule
above, would silently drop their constraints.

---

## 8. Forms view

A JSON object that is a list of items with per-item properties should render as a **table**: one
row per list item, one column per property. The analytes table in the current form already follows
this pattern, and every template in §5 has that shape by construction.

---

## 9. What this needs from upstream (for Ruolin)

1. **`defines: standard` should declare primary standards too**, not only *Secondary Reference
   Materials*. Without declared primary standards, `standard x reported property` has nothing to
   reference. (tapp#22)
2. **Confirm the monitored-property kind vocabulary** — `element`, `mass`, and what spectroscopy /
   XCT / AFM need. The field *names* `Monitored Masses` and `Monitored Elements` can then stay, or
   collapse to `Monitored Property` with the kind carried as data.
3. **Confirm the list-order convention**, or confirm the flatten fallback is acceptable where
   lists cannot be aligned. This is the single largest risk to a parser.
4. **`standard x reported property`: deprecate?** Its information moves to the standards template.
5. Three families — spectroscopy, XCT, AFM — need their target material / monitored property
   semantics worked out. Not blocking: all five topics are optional.

## 10. Open on our side

- Define `ada:standardTemplate` and `ada:reportedPropertyTemplate`, and re-point the 54 rows
  currently filed under target species.
- Retire `ada:monitoredElements[]` (6 rows) into `ada:monitoredPropertyTemplate`.
- Coordinate the reported-property template with the composition modules (218 of 258 rows).
- `populate_template_columns` is fed the resolved schema and nothing else, so a workbook cell is
  never offered to the column path. It needs a parser for the nested
  `outer [inner: value; inner: value]` notation and a per-row slot — 1,289 of 1,446 keyed-table
  rows are written as bare name lists today. **Blocked on tapp#22**: a parser written into
  `ada:targetMaterialColumns` before #22 decides where standards live is work thrown away.

---

### Re-deriving the numbers

The sidecar tables above come from the `Key by` and `Schema Path` columns of the 61 **live**
sidecars. Filter by the basenames of `build_tapp.TAPP_CONFIGS[*]["xlsx"]` — `docs/` also holds
module sidecars and an archive, and counting those measures history rather than the live set.
