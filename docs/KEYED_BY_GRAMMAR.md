# `Keyed By` → schema-path grammar

Written 2026-08-11 against the delivery in `TAPPS20260811/` (16 TAPPs, 1691 content rows). The
field names, tiers, counts and examples below are taken from those CSVs.

**Re-checked 2026-10-05 against `tapp @ 6a6eed2`** (EPMA v88, SEM v85, SEM_Composition v83), the
delivery that re-keys the counting times per target material. The previous re-check was against
`94fa379`, which enforced the keyed-value notation on all sixteen TAPPs (`KEYED_NOTATION_EXEMPT` is
now empty). **Two renames have happened since this document was written and it has not been
reworded throughout: `analyte` is now `target species`, and `channel` is now `monitored
property`.** Read the older sections with that substitution; the paths in them
(`ada:targetSpeciesColumns[]`, `ada:monitoredPropertyColumns[]`) are current, and
`keyed_path()` aliases both new spellings onto the old route keys.

Counted from the sixteen `Current TAPPs/*.csv`: **1936 content rows, 674 keyed row-instances,
25 distinct forms** — not the eight described here.

```
monitored property 109   reported property 99   acquisition pass 83   sample 48
target species 40   standard x reported property 33   combined result x reported property 26
sample > sampling unit 25   sample > sampling unit x reported property 21
defines: target material 16   defines: sample 16   defines: sample > sampling unit 16
target material 16   defines: reported property 16   defines: target species 13
defines: monitored property per target species 13   combined result 13
defines: combined result 13   target material x target species 12   defines: standard 12
defines: acquisition pass 9   preparation step 9   pair: reported property 7
target material x monitored property 6   defines: preparation step 3
```

**What `6a6eed2` changed, and it is the whole delta:** `monitored property` drops 115 → 109 and a
twenty-fifth form appears, `target material x monitored property` 6. Those are the same six rows —
`Peak Counting Time` and `Background Counting Time` in each of EPMA v88, SEM v85 and
SEM_Composition v83. A counting time is set per spectrometer AND per material, so the single key
understated it.

**Fourteen forms are routed** by `bootstrap_schemapaths.keyed_path()`, covering 453 of the 674
instances: `monitored property`, `reported property`, `sample`, `target species`,
`target material`, `combined result`, `combined result x reported property`,
`target material x target species`, `sample persistent identifier`, and the `defines:` forms for
`sample`, `sample > sampling unit`, `reported property`, `target species`, `target material` and
`combined result`.

**Eleven are left unrouted rather than guessed at**, 221 instances: `acquisition pass` (83),
`standard x reported property` (33), `sample > sampling unit` (25),
`sample > sampling unit x reported property` (21), `defines: monitored property per target
species` (13), `defines: standard` (12), `defines: acquisition pass` (9), `preparation step` (9),
`pair: reported property` (7), `target material x monitored property` (6),
`defines: preparation step` (3). That is the point — an inferred placement for a domain nobody has
modelled is worse than an empty cell, because it looks decided.

> Earlier revisions of this file listed `target material x target species` among the unrouted. It
> has been routed since the target-material template landed, to
> `ada:targetMaterialTemplate.ada:targetMaterialColumns[]` — the X half names the table and the Y
> half rides the column. `target material x monitored property` is the same construction and is
> the obvious candidate to route next.

### Which keys actually have a table to be a column of

Four, and `tools/schema_path_emitter.KEYED_TABLES` registers exactly those: `ada:targetSpecies-`,
`ada:monitoredProperty-`, `ada:reportedProperty-` and `ada:targetMaterialColumns`. A key outside
that set has no table, so a row keyed by it lands wherever inference puts it — typically a
`schema:additionalProperty` name/value pair, which records the value and loses which row it
belongs to.

`DEFAULT_ROW_ARRAYS` registers only **three** of the four row axes —
`ada:defaultTargetSpecies`, `ada:defaultMonitoredProperties`, `ada:defaultTargetMaterials`.
`ada:defaultReportedProperties` is defined in `tappDefinition` but is absent from both that set
and `normalize_path`'s trailing-`[]` collapse. No sidecar row ends at it today (16, 13 and 5 rows
end at the other three), so this is latent rather than live — but it is the same gap that made a
path ending `ada:defaultTargetMaterials[]` emit the raw items schema instead of the members, and
cost 136 examples.

### Three keys whose modelling is settled, and settled AGAINST a table

Do not read these as gaps waiting for a template:

- **`acquisition pass` (83 instances, 9 tables).** Retired by rule — tapp conventions.md 7.4b/c,
  2026-08-11, taking the in-use vocabulary from ten keys to six — and reinstatement has been
  declined twice in writing, for Collector Configuration and then Desolvation System. The reason
  is Rule 7's own test: the key is the finest axis attested in REPORTED data, and reported data is
  indexed by analyte and reported property, never by which pass produced it. Multi-pass structure
  is procedural, not a data axis. **The tables nevertheless still declare it** — 7 rows in
  `Solution_Q-ICP-MS_TAPP_v94` at `6a6eed2`, plus a `defines:` row — because `8632ef2` was
  documentation only and never touched the `Keyed By` column. Our sidecars mirror the tables, as
  `Key by` must; the contradiction is upstream's to resolve.
- **`sample > sampling unit` (25) and `defines: sample > sampling unit` (16).** A data-table axis,
  not a procedure one. `geochemProduct/schema.yaml` states it: the procedure and the analysis can
  state only the KIND of unit (`ada:samplingUnitType`), a particular unit's identifier is a
  `schema:variableMeasured` naming a COLUMN in a distribution, and the unit-to-material binding
  exists only in the instance data table. An array of sampling-unit objects was added 2026-09-25
  and REMOVED 2026-10-01 once that was settled; `ada:samplingUnits` appears nowhere in the sources
  today.
- **`combined result` (13) and `defines: combined result` (13).** Analysis-side only. The
  procedure can say HOW results will be combined (Combination Method, keyed by reported property)
  but not WHICH were, so there is deliberately no `ada:combinedResults` counterpart in
  `tappDefinition`.

**The authoritative statement of the notation is now the delivery's own `Legends` worksheet**, not
this file. It defines the four constructions in one place:

| notation | meaning |
|---|---|
| `(none)` | scalar — one value per procedure or analysis |
| `X` | one value per member of X — **a column in X's table** |
| `defines: X` | **the header of X's child table, not a column in it** — enumerates the domain |
| `X x Y` | cross-product, "for each X, one value per Y" |
| `a > b` | containment — b exists only within a |

This document says where each construction lands in the schema, and §1.2 says how the member list
inside a `defines:` cell is read.

**Status: partly implemented (updated 2026-10-01).** The three original keyed-table domains —
target species, monitored property, reported property — generate as keyed tables (a `…Columns[]`
template plus a `…defaults[]` array, with registry catalogs under `_sources/registry/`). Three more
row axes exist without that triple: `sample > sampling unit`, `target material` and
`combined result` (§1.3). Thirteen of the 24 forms route, eleven are flagged — the header lists
both. The member grammar inside a `defines:` cell is implemented (§1.2), which is the part this
document previously deferred. §12 logs what is decided and what is open.

Column I (`Keyed By`) states what a field's value repeats over, and it decides schema *shape*.
Companion reading: the delivery's own **`Legends` worksheet**, which is now the authoritative
statement of the notation; `README_TAPP_for_Schema_Generation_v2.md` §4; and
`SCHEMA_PATH_GRAMMAR.md` for the path families.

---

## 1. The model

1. **A key names a domain.** Nine are in use as of 2026-10-01: `target species` (was `analyte`),
   `monitored property` (was `channel`), `reported property`, `sample`, `sampling unit` (always
   nested, `sample > sampling unit`), `standard`, `preparation step`, `acquisition pass`, and the
   two the 2026-10-01 delivery added — **`target material`** and **`combined result`**.
2. **Exactly one field declares each domain**, marked `defines: X`. Its *value* supplies the
   members — and that value is authored when a TAPP instance is created, not fixed here.
3. **Each instance of the domain carries every property whose `Keyed By` names that domain.** So a
   keyed field is a **column of a table**, and the `defines:` field is the table's **row axis**.

We already have exactly this structure for one domain:

```
$MethodDefinition.ada:targetSpeciesTemplate.ada:targetSpeciesColumns[]     column definitions
$MethodDefinition.ada:targetSpeciesTemplate.ada:defaultTargetSpecies[]    row axis (the member list)
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

### 1.2 The `defines: X` list grammar — IMPLEMENTED 2026-09-29

**This section used to say the parse belonged to the authoring app and the pipeline should not
attempt it. That is no longer true.** `tools/schema_path_example_emitter.py` parses these cells
(`_parse_grouped_members`, and the guard `_looks_like_members`), and the grammar below is what it
implements. The authoring app should still confirm a split with the author — a bad split is best
caught as "you declared 8 target species, here they are" — but it is no longer the only thing
standing between a cell and a table.

**A `defines: X` cell has TWO levels, not one.**

```
84Sr, 86Sr, 87Sr, 88Sr (Sr); 85Rb (Rb); 83Kr, 167Er2+, 173Yb2+ (monitors, no target species)
└──────── group 1 ────────┘  └─ group 2 ─┘ └──────────── group 3 ─────────────┘
```

- **`;` separates groups. `,` separates members within a group.** Splitting on both alike gives
  nine members here instead of eight, and attaches each parenthetical to whichever member happened
  to precede it.
- Both splits are at **parenthesis depth zero**, so a separator inside `(...)` or `[...]` is
  ordinary text. `BHVO-2 (Fe isotopes; Dauphas & Rouxel 2006 compilation)` is one member.

**A parenthetical qualifies the group or the member, and which is DECIDED, not assumed:**

| form | reading |
|---|---|
| only the **last** member of a group carries one | it qualifies the **whole group** — `84Sr, 86Sr, 88Sr (Sr)` is three members of parent `Sr` |
| **several** members carry one | each qualifies **its own** member — `32S (L3), 33S (C), 34S (H3)` is three members with three collectors |

Both forms occur in the corpus and they mean different things.

**A qualifier is recognised, not parsed** (`_classify`). It is the parent species if it matches a
member of the `defines: target species` cell, a collector if it matches a collector label, and
otherwise an annotation — in which case the member is an orphan with no parent. That recognition
is why no syntax for "this one has no parent" is needed: `(monitors, no target species)` matches
nothing and the member simply has none.

**Four normalisations, each put in for a cell it was silently corrupting:**

1. **`and` is a separator** when what follows looks like a member — a digit, a superscript, or a
   capitalised element symbol. `Fe, Cr and Mg` is three species. Without this a member three words
   wide failed the guard and took its whole list down. Note the superscripts ¹ ² ³ live in
   **Latin-1**, not the U+2070 superscript block, so a character class of `⁰-₟` alone misses every
   mass starting 1xx, 2xx or 3xx — that dropped a nine-member Os/Re/W cell whose every mass is 18x.
2. **A leading label is stripped**, not taken as the first member: `48 trace elements: Li, Be, …`,
   `Session 1: Al, …`, `masses 90, 91, 92`. It sits before the first comma, so it became member one,
   and being several words wide then failed the guard.
3. **A comma inside a member is not a separator** where the previous member ends in a sub-level
   host — letters then digits, the shape of an energy-loss edge. `Fe L2,3 (707 eV)` is ONE member.
   Deliberately narrow: a bare mass does not match, which is what stops `90, 91, 92` being glued
   into one.
4. **A `+` joins two species into one member and does not spend the word budget.** `⁸⁷Rb + ⁸⁷Sr` is
   a single Faraday cup carrying two unresolved isobars — one collector, one measured quantity.

**The guard, and why it rejects the whole cell.** A member is at most two words
(`MEMBER_MAX_WORDS`), measured against the corpus: of the 141 "members" the flat splitter produced,
98 were one or two words and the rest were prose shredded out of a paragraph — one read literally
`"N - spectrometer-to-element assignments not stated"`. If **any** member fails, the whole cell
yields **no members**, not the ones that parsed. A half-parsed list is worse than none: "here are
four of the eight" reads as complete and is not.

**Rejection must not lose the data.** An unparseable cell keeps its text verbatim in the
declaration field beside the table — `ada:collectorConfiguration` for monitored properties,
`ada:targetSpeciesDeclaration` for target species, which was added for exactly this reason. A
partly-parsed cell yields the members that were recognised **plus** the statement they were
recognised from, so nothing is discarded. Where a declaration cannot be parsed, that text IS the
answer.

### 1.2.1 How values in fields keyed to X are processed

A field keyed `X` is a column of X's table, so its cell holds **one value per member of X, in the
member order the `defines: X` cell established**. Since the 2026-10-01 delivery that cell is
**value-only**: the key is no longer repeated inside it.

```
Keyed By: monitored property
  before   'Si=Sp1; Ti=Sp2; Cr=Sp2+Sp3 (aggregate intensity counting); Fe=Sp3'
  after    'Sp1' | 'Sp2+Sp3 (aggregate intensity counting)' | 'Sp4'
```

That change is why Column F parsing improved rather than broke: the old form made
`enum_terms()` emit `'Si=Sp1; Ti=Sp2; …'` as a **single** vocabulary concept. Only two fields
feeding vocabularies were affected (`Plasma Thermal Mode`, `Sample Preparation Method`), but for
those the published concepts were malformed.

Three rules for reading a keyed cell:

1. **Positional against the definer.** Value *i* belongs to member *i*. A cell with fewer values
   than members leaves the rest unstated; it does not shift.
2. **A cross-product `X x Y` is still one column.** `combined result x reported property` rides on
   the combined-result row as a per-reported-property value — the Y half is carried by the column's
   `schema:valueName`, not by a second container. A consequence worth knowing: **a cross-product is
   not recoverable from a path**, because `combined result` and `combined result x reported
   property` route to the same row array, so `backfill_keyby` returns the simple key. Same
   limitation already applies to the channel and standard keys.
3. **The N=1 fallback applies here too** (§1.1, Decision 6): a keyed cell that does not parse into
   per-member values becomes one value against a one-row table whose key is the text as written.

The examples below are why rule 1 needs stating at all — the library's cells do not agree with one
another:

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
| target species (was analyte) | `ada:targetSpeciesTemplate` | `ada:targetSpeciesColumns[]` | `ada:defaultTargetSpecies[]` |
| monitored property (was channel) | `ada:monitoredPropertyTemplate` | `ada:monitoredPropertyColumns[]` | `ada:defaultMonitoredProperties[]` |
| reported property | `ada:reportedPropertyTemplate` | `ada:reportedPropertyColumns[]` | `ada:defaultReportedProperties[]` |
| preparation step | — (ordinal, §6) | — | `schema:numberOfItems` |
| standard | — (never standalone, §7) | — | `ada:secondaryReferenceMaterials[]` |

The three domains added since, which do **not** use the template/columns/defaults triple — their
rows carry their keyed values directly, so there is no separate column-definition array:

| domain | row axis | side | added |
|---|---|---|---|
| sample > sampling unit | `$Dataset.schema:variableMeasured[schema:name=…]` — a DATA COLUMN | analysis | 2026-09-25, corrected 2026-10-01 |
| target material | `$MethodDefinition.ada:targetMaterials[].schema:name` | **procedure** | 2026-10-01 |
| combined result | `$Dataset.prov:wasGeneratedBy.ada:combinedResults[].schema:name` | analysis | 2026-10-01 |

**One of these is not metadata, and that is the most important distinction in this section.**

- **A sampling unit is DATA.** The procedure and the analysis can state only the KIND of unit —
  `ada:samplingUnitType`, a controlled type that defines nothing, because a type cannot enumerate
  its own instances. A *particular* unit (a microprobe analysis point) is a **column in one of the
  dataset's distributions**, and the record holds only the `schema:variableMeasured` that names
  that column. The binding from a unit to its target material is in that same instance data table,
  beside the analytical results for that unit — `Target Material of Sampling Unit` therefore
  declares a column too, not a property of anything in the record.

  This was got wrong first: on 2026-09-25 an `ada:samplingUnits[]` array of unit OBJECTS was added
  to `geochemProduct`, nested in the sample, with a `schema:name` and an `ada:targetMaterial` FK.
  It was removed on 2026-10-01. The lesson is the one worth keeping: **before giving a domain a
  container in the record, ask whether its members are metadata at all.** A domain whose members
  are only ever observed per data row belongs in the data, and its `defines:` row declares the
  column rather than the members.
- **`target material` is procedure-side**, because it is what the procedure declares it expects to
  find, and the materials are assumed present in any sample it analyses. There is deliberately
  **no** per-sample list of contained materials — nothing maps a `schema:object` to the materials
  inside it. The only place a sample meets a material is the data column above.
- **`combined result` sits on the ACTIVITY and IS metadata**, because a combined result is a
  statement the record makes about its own contents, and it names its own sample rather than
  belonging to exactly one — an isochron over 36 runs is the case in hand.

---

## 2. `analyte` — 77 rows, 24 fields, 13 TAPPs

Declared by `Analyte` (`C=Basic, D=Editable`). Consumers include `Background Counting Time`,
`Diffracting Crystal`, `EPMA Technique per Analyte`, `Blank Correction`.

```
$MethodDefinition.ada:targetSpeciesTemplate.ada:targetSpeciesColumns[]
$MethodDefinition.ada:targetSpeciesTemplate.ada:defaultTargetSpecies[]
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
$MethodDefinition.ada:monitoredPropertyTemplate.ada:monitoredPropertyColumns[]
$MethodDefinition.ada:monitoredPropertyTemplate.ada:defaultMonitoredProperties[]
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
strip the `e.g.,` prefix. **Do not split further for this purpose.** That is a different job from
reading a `defines:` cell into members (§1.2), and the two must not be confused: `examples` is a
non-validating annotation showing the author what a cell may look like, so an alternative is one
example string and splitting inside it would offer fragments as guidance. §1.2's grammar runs only
where a cell is being turned into table ROWS.

`tools/build_tapp.enum_terms()` is the `|` splitter, and it strips the `e.g.` prefix. It is also
what the 2026-10-01 value-only notation improved: see §1.2.1.

---

## 11. What the grammar needs

| # | family | rows served |
|---|---|---|
| 1 | `reportedPropertyColumns[]` + shared `$Dataset.schema:variableMeasured[]` | 81 + 16 |
| 2 | `monitoredPropertyColumns[]` / `defaultMonitoredProperties[]` | 47 + 10 |
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

Settled since:

8. **The `defines: X` member grammar is implemented, not deferred to the forms app.** Two levels
   (`;` groups, `,` members), depth-zero splitting, group-or-member qualifiers decided by how many
   carry one, and a two-word guard that rejects the WHOLE cell rather than half a list. §1.2,
   2026-09-29.
9. **A rejected cell keeps its text** in the declaration field beside the table
   (`ada:collectorConfiguration`, `ada:targetSpeciesDeclaration`). Rejecting without that field
   discarded the data, which is why the target-species counterpart was added. §1.2
10. **A keyed cell is positional against its definer**, and since 2026-10-01 is value-only — the
    key is no longer repeated inside it. §1.2.1
11. **`target material` is procedure-side; `combined result` is activity-side.** Neither uses the
    template/columns/defaults triple. The deciding question is whether a member can belong to more
    than one sample: a sampling unit cannot, so it nests in the sample; a combined result can, so
    it sits on the activity. §1.3, 2026-10-01.
12. **No per-sample list of contained target materials.** The procedure's list is what is expected
    in any sample it analyses; a sample meets a material only through
    `ada:samplingUnits[].ada:targetMaterial`, at the granularity the assignment is observed. §1.3

Open:

1. **The monitored-property / target-species binding**, and the shifting definition of the latter
   across techniques. §3.1 — for Ruolin. (Written as channel/analyte; both were renamed.)
2. **Eleven of the 24 forms are still flagged rather than routed** — see the header for the list.
   The two that now have consumers and no home are `target material x target species` (12 rows,
   `Primary Calibration Standard Name`, module-owned by CompositionQC) and `acquisition pass`
   (83 rows, the largest unrouted domain in the column).
3. **The 55 legacy cross-product rows do not follow this grammar.** `standard x reported property`
   (33) and `sample > sampling unit x reported property` (22) are all parked on
   `ada:targetSpeciesColumns[]` — the wrong domain — as a keyed-value-column fallback that predates
   the Legends sheet. The 2026-10-01 domains follow the Legend instead, so the two conventions now
   coexist until those 55 migrate.
2. **Per-domain templates, or one generic keyed table?** This document instantiates the
   `analyteTemplate` precedent per domain. A generic
   `ada:keyedTable[ada:key='analyte'].ada:columns[]` would be more uniform and would make
   cross-products fall out as two keys, but breaks from what ships today.
3. **Where the parse-and-confirm step lives** in the forms app. §1.2
