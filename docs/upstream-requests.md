# Requests to the TAPP library

(from claude with SMR edits)

Things the schema-generation work has found that can only be fixed upstream, in the tables and modules Ruolin authors. SMR imports those read-only ([.github/CODEOWNERS](../.github/CODEOWNERS)), so I don't want to change in my github unless you give me the go ahead....

Ordered by how much work each one saves, and each number is reproducible with the tool named beside it.

**Which delivery each section was measured against**, because they differ and the older numbers
were never re-run: §1, §2 and §3 were measured against the **2026-08-13** drop (copied from Google
Drive at the time) and §1 and §2 are both marked DELIVERED since. §4 was measured on
**2026-10-18** against the `tapp/` submodule as pinned, whose `composed_tapps.json` is generated
**2026-10-01** and lists 16 composed TAPPs. Where a §1–§3 count is restated below it is labelled as
historical rather than silently refreshed.

---

## 1. The LA family needs more modules — 83 shared fields have none

> **DELIVERED 2026-09-02** (`af3f7bc`). Ruolin created `Module_ICPMS` (39 fields, 9 consumers),
> `Module_CollisionCell` (8, 6) and `Module_CompositionQC` (6, 12), which together cover the
> groupings proposed below. Our six ICP-MS drafts have been deleted; **456 rows** that each
> technique used to mint now come from a module. Eight of the drafted fields were NOT taken up —
> `Detector Configuration`, `Dwell Time per Mass`, `Total Integration Time per Output Data Point`,
> `Number of Replicates`, `Mass Resolution Assignment`, `Doubly-Charged Species Production`,
> `Doubly-Charged Species Monitor` and `Mass Bias Correction Strategy` — and remain per-table. The
> original request is kept below unchanged, as the record of what was asked and measured.

**The finding.** The six LA tables (Q/SF/MC, each with a UPb variant) hold 153 distinct fields. **115 of them appear in all six.** The existing modules cover 42. The remaining **73 are duplicated six times over**, and 10 more are shared by four or more tables with no module either.

| shared by | fields | in a module | in none |
|---|---|---|---|
| all 6 tables | 115 | 42 | **73** |
| 4–5 tables | 10 | 0 | **10** |

**Why it matters.** Without modules, generating schemas for the six LA tables means authoring six near-identical sets of schema paths (mapping from TAPP property to JSON-LD path), most of them the same decision repeated. That is the drift the module system exists to prevent; I'm holding up on the configs until we decide about adding these modules.

**What it would save — measured, not estimated.** I built the six groupings below as local drafts
(`docs/modules/draft/`) and counted:

| | placements |
|---|---|
| field instances across the six LA tables | 796 |
| already covered by your existing modules | 309 |
| **left to place per-table today** | **487** |
| covered if these six were modules | 717 |
| **left to place per-table then** | **79** |

487 becomes 71 authored once plus 79 remaining — a **net reduction of 337, about 69%**. And 67 of
the 71 (94%) already have a placement in a technique sidecar we curated earlier, so the module-side
work would largely seed itself; only 4 fields need placing from scratch.

**The precondition holds.** A field can only be a module field if its definition is the same
everywhere. Of the 83 candidates, **80 carry identical tiers, data type and `Keyed By` across all
six tables**. The 3 that differ are `Mass Resolution Setting`, `Monitored Isotopes` and
`Primary Calibration Standard Name` — all documented as technique-dependent by design (README §4),
so they stay per-table. That is the right answer rather than a gap, and it is why they are absent
from the groupings below.

One thing for you to settle if you adopt this: six of the collision/reaction-cell fields are
structurally identical but **worded differently** between the Q and MC families. The drafts use the
more common wording; a real module needs one description.

**Proposal.** The 83 fields cluster cleanly. Suggested groupings — field counts are what the drafts
actually built, for you to name and scope:

- **ICP-MS instrument core** (20) — ICP-MS Manufacturer & Model, ICP-MS Type, RF Power, coolant /
  auxiliary / carrier gas flow rates, Torch Type, Torch Depth, Interface Cone Configuration,
  Sampler and Skimmer Cone Material, Guard Electrode, Plasma Thermal Mode, Detector Configuration,
  Ion Counter Dead Time, Sample Introduction, Instrument Serial Number or Lab Identifier, ICP
  Tuning, Instrument Warm-up / Session Duration Limit, Plasma / Make-up Gas Addition,
  Sensitivity as Useful Yield
- **Collision / reaction cell** (6) — CRC Configuration, Collision Gas Type and Flow Rate, Reaction Gas
  Type and Flow Rate, Cell Exit Discrimination Voltage
- **Signal acquisition** (9) — Dwell Time per Mass, Signal Integration Time, Signal Integration
  Interval Method, Total Integration Time per Output Data Point, Background Count Time, Number of
  Replicates, Signal Smoothing, Mass Resolution Assignment, Multi-Run Sequential Analysis Design
- **Interference handling** (7) — Interfering Species, Isobaric Interference Corrections Applied,
  Interference Correction Method, Oxide Production, Oxide Production Method and Threshold,
  Doubly-Charged Species Production, Doubly-Charged Species Monitor
- **Calibration and uncertainty** (21) — Detection Limit, Detection Limit Method, Limit of Quantification
  (LOQ) Method, Within-Session and Between-Session Analytical Precision and Assessment Method,
  Analytical Accuracy and Assessment Method, Uncertainty Level, Uncertainty Propagation Method,
  Secondary Reference Materials, Per-Analyte Calibration
  Strategy, Internal Standard Approach, Internal Standard Element, Normalization / Standards-Based
  Correction, Blank / Background Correction Method, Calibration Standard Measurement Frequency,
  Spike / Outlier Filtering Approach, Elemental Fractionation Correction, Mass Bias Correction
  Strategy, Matrix Offset Correction (LIEF), Isotope Dilution Data Reduction Method, Memory
  Effect Mitigation
- **Sample / specimen** (8) — Sample Name, Sample Persistent Identifier, Sample Form / Analytical
  Substrate, Sample Preparation Method, Target Material, Sampling Unit, Analysis Sequence,
  Fusion Flux and Dilution Ratio

The last group is the widest: those six are shared by **every** technique, not only LA, yet none is in Group1 or ReportingCore. They may belong in one of those rather than a new module.

**That accounts for 71 of the 83.** Of the remaining 12, three are the technique-dependent fields
above and two are ICP-MS-specific and could join a group — `Mapping Area` and `Pulse / Analog
Detector Nonlinearity Correction`. The other seven turned out to be a separate and wider finding,
which is §2.

*Reproduce:* `python tools/draft_module.py --measure` — it reads the six `Current TAPPs/LA-*.csv`
tables and your `Claude Skills for TAPP/modules/Module_*.csv`, and refuses any field whose
definition differs between tables rather than averaging it.

---

## 2. Seven near-universal fields are in no module — 101 repeated instances

> **DELIVERED 2026-09-02** (`af3f7bc`). All seven now sit in a module: six in `Module_Core`
> (`Acquisition Software`, `Analytical Mode`, `Reported Variables and Units`, `Constants and
> Reference Values Used`, `Additional Notes`, `Data Processing Software(s)` — the renamed `Data
> Reduction Software`) and `Analyte` in `Module_Analyte`. Neither `Group1` nor `ReportingCore` was
> used; both are now composed by nothing.

Found while reconciling §1's arithmetic, and it applies to the whole library rather than just LA.
These seven appear in nearly every TAPP and belong to **no module at all**, so each of the sixteen
carries its own copy:

| field | in N of 16 | in a module |
|---|---|---|
| `Acquisition Software` | 16 | — |
| `Analytical Mode` | 16 | — |
| `Reported Variables and Units` | 16 | — |
| `Constants and Reference Values Used` | 16 | — |
| `Additional Notes` | 16 | — |
| `Data Reduction Software` | 15 | — |
| `Analyte` | 13 | — |
| **108 field instances** | | **7 if modularised — 101 stop being repeated** |

**All seven are structurally identical wherever they appear** — same tiers, data type and
`Keyed By`, with no exceptions across all sixteen tables. That is a stronger result than §1's
(80 of 83), and it means there is nothing to reconcile before they could move.

Your README §10 already singles out three of them as fields "worth special handling", present in all
16 — `Reported Variables and Units`, `Constants and Reference Values Used` and `Additional Notes`,
the last described as always the final field of the whole TAPP. Fields that important, that
consistent and that widespread look like module material.

**Suggestion.** These are not a new subject area, so a new module seems wrong. `Acquisition
Software` and `Data Reduction Software` are procedure identification, so `Group1`. `Reported
Variables and Units`, `Constants and Reference Values Used` and `Additional Notes` are reporting, so
`ReportingCore` — though note `ReportingCore` is block-conditional and these would need to be
unconditional, or a block every TAPP selects. `Analytical Mode` and `Analyte` are the two I am least
sure about: both are declarative (`Analyte` carries `defines: analyte`), and a definer moving into a
shared module may interact with Rule 7 in ways you will see and I will not.

*Reproduce:* counts and the identity test run over `Current TAPPs/*.csv` against
`Claude Skills for TAPP/modules/Module_*.csv`.

---

## 3. `Error Correlation Between Reported Quantities` belongs to no module

Still open, re-measured 2026-10-18. It appears in **four** technique tables —
`LA-MC-ICPMS_UPb`, `LA-Q-ICP-MS_UPb`, `LA-SF-ICP-MS_UPb` and **`Solution_MC-ICP-MS`** — and in
none of the module sidecars. So it is no longer UPb-specific, which the original wording assumed,
and the module count has moved: the manifest now composes **15** modules (16 exist; `ReportingCore`
is composed by nothing), not the eight this section was written against.

Should it join `Module_UPb` or `Module_Geochronology` — or, given the Solution MC-ICP-MS
appearance, somewhere less geochronology-specific?

---

## 4. `Sampling Unit Name` is required of records that have no data table

**The ask: should this item be conditional on the record having a tabular data structure?** It is
your item, at Analysis Tier **Basic**, and the question is about where the requirement sits rather
than whether it is right. Nothing changes until you say so.

**The row**, from `docs/modules/Module_Core.schemapaths.csv`:

| | |
|---|---|
| Metadata Item | `Sampling Unit Name` |
| Protocol Tier | N/A |
| Analysis Tier | **Basic** |
| Data Type | Text (free) |
| Schema Path | `$Dataset.schema:variableMeasured[schema:name='Sampling Unit Name']` |
| Scope | module (Core) |
| Notes | "declares the COLUMN that identifies a sampling unit in the instance data table…" |

Because the path carries a selector, the emitter turns it into a `contains` with a literal const,
in `_sources/BaseSchema/modules/core/schema.yaml`:

```yaml
schema:variableMeasured:
  allOf:
  - contains:
      properties: {schema:name: {const: Sampling Unit Name}}
      required: [schema:name]
```

It is in Core, so it reaches **every** technique — 162 `resolvedSchema.json` carry it.

**The argument is about layers, not counts — and gBB has already settled it once, in the block
that composes this very item.** `_sources/BaseSchema/geochemProduct/schema.yaml`, lines 362–368,
in prose written for a neighbouring question:

> "An individual sampling unit is not [metadata]: the procedure and the analysis can state only
> the KIND of unit (`ada:samplingUnitType`), while a particular unit's identifier is a
> `schema:variableMeasured` naming a **COLUMN in one of the distributions**, and the binding from
> that unit to its target material **exists only in the instance data table** beside the results.
> There is therefore no array of sampling-unit objects here; one was added on 2026-09-25 and
> removed on 2026-10-01 once that was settled."

So `geochemProduct` already asserts that the declaration names a column in a distribution and that
the binding exists only in the instance data table. **A record with no instance data table has
nothing for the declaration to name** — stated by the schema, not inferred from the corpus. The
same paragraph ties the 2026-09-25/10-01 array experiment to this reasoning, so the layer
question has been answered once in this file already; what is left is applying the answer to the
`contains`.

The type hierarchy says it too, independently: `schema:variableMeasured` is declared in
`geochemProduct` as extending `cdifInstanceVariable` — an **instance** variable. A method
definition or detail block can only *define* which fields might appear; only an actual data
instance can assert which columns exist. And the row's own Notes agree — "the units themselves
exist only in the data".

**What the corpus shows**, measured by the ADA metadata forms session over all 7,447 records
(1,682 of which would gain a technique profile once content-based detection is switched on):

| | records | share |
|---|---|---|
| have any `schema:variableMeasured` | 125 | 7.4% |
| have a tabular part or column structure | 129 | 7.7% |
| have **neither** | **1,553** | **92.3%** |
| carry a variable named `Sampling Unit Name` | **0 of 7,447** | — |

`adaLabXCT` 701, `adaSTHMAFM` 483 and `adaSXRF` 324 are 1,508 of those on their own — XCT image
stacks, AFM scans, synchrotron XRF maps. They have no columns, so there is no column for the
declaration to name.

**And the one example that does satisfy it is a placeholder, with the wrong semantics.** Our
generated `XCT/profile/exampleadaLabXCT.json` validates clean only because the generator's fill
pass invented the variable:

```json
{ "schema:name": "Sampling Unit Name",
  "schema:description": "Sampling Unit Name reported for this dataset. Example value.",
  "schema:unitText": "counts",
  "cdi:role": "MeasureComponent" }
```

A sampling-unit name is a **label**; this emits it as a measure component in **counts**. So the
constraint is met nowhere by genuine content, and where it appears to be met the content
misdescribes the field.

**The options, in what we think is preference order:**

1. **Make the item conditional on a tabular data structure existing.** gBB already has that exact
   predicate — `geochemProduct` guards `cdifDataDescription` on *non-empty
   `schema:variableMeasured` OR a distribution/part typed `cdi:TabularTextDataSet`*, added
   2026-10-16, and 6,575 records stopped declaring `data_description` as a result. Applying the
   same guard here needs either a sidecar-grammar way to say "only when the data is tabular" or an
   emitter rule; both are our side, and small.
2. **Keep it unconditional and treat the 1,553 as incomplete.** Defensible only if an image-stack
   product is genuinely expected to declare a sampling-unit column, which we do not think it is.
3. **Narrow the Scope from `module` (Core) to the techniques whose products are tabular.** Avoids a
   grammar change at the cost of per-technique duplication, and Core is where it belongs
   conceptually.

**What we are NOT asking.** The literal name is the identity of the declaration and we are not
proposing to change it, nor to replace it with an array of unit objects — the Notes record that
being tried on 2026-09-25 and removed on 2026-10-01.

### 4a. The condition we think is right, and why it has to be yours

Stephen's rule: **the variable is mandatory only if the TAPP keys data by sampling unit.** That is
exactly the right axis, and the mechanism to express it already exists — but it is declared in
your files, not ours, which is why this is a request rather than a change.

`Module_Core.json` carries `"conditional": false` and puts `Sampling Unit Name` in the **`samples`**
block, whose `applies_when` reads:

> "Universal — every TAPP carries every field in this module. Unconditional: all blocks are always
> composed together."

So the field is declared universal upstream. The alternative is already **supported**, though not currently
exercised: a module marks itself `conditional` and declares blocks, and a TAPP's entry in
`composed_tapps.json` names the blocks it takes. `build_module_bb.module_blocks()` and
`module_composition._blocks()` both read that, so **nothing in our generators needs changing** —
only the declaration.

Stated carefully, because an earlier draft of this section overstated it: `Module_ReportingCore`
is the module that declares blocks, and in the current manifest (`composed_tapps.json`, generated
2026-10-01) **`ReportingCore` is composed by no TAPP at all**, and **no entry uses a `blocks`
selection**. So the mechanism is implemented and documented
(`docs/REPORTINGCORE_BLOCKS.md` — whose per-TAPP selection table describes an earlier manifest and
is itself stale) rather than in live use. That makes this an ask to use a supported feature, not
to copy a working neighbour.

**The ask:** separate `Sampling Unit Name` from the universal `samples` block and let a TAPP select
it — the shape `Module_ReportingCore` already declares for its own five blocks.

**Measured, so the selection does not have to be guessed.** Distinguishing the two uses of the key
in our sidecars:

| | sidecars | meaning |
|---|---|---|
| `defines: sample > sampling unit` | **60 of 60** | every TAPP declares the key — Core gives it to them, so this cannot discriminate |
| `keyed by: … sample > sampling unit` | **17 technique TAPPs** + 3 modules | the TAPP actually reports values per sampling unit |

The 17 that key data by it: EPMA (7 rows), the six LA tables (3 each), Lab-XCT (6), SEM (7),
SEM-Composition (7), SEM-Imaging (3), SEM-FIBSEM (2), Solution Q/SF/MC (2 each), TEM (1),
VNMIR (6). **44 of 61 technique sidecars have no such row** — which is the selection we would
expect, if you agree with the axis.

### 4b. Lab-XCT keys six rows by sampling unit — is that right?

This is the part the measurement does **not** settle, and it matters most, because `adaLabXCT` is
**701 records** — the single largest group of the ~1,633.

`Lab-XCT_TAPP_v47` keys six rows by `sample > sampling unit` — **three distinct items, each
appearing twice**:

- *Segmentation Threshold Values or Criteria*
- *Phase Identification Method*
- *Partial Volume Effect Criteria*

So that table asserts XCT results **are** reported per sampling unit, and under the rule above XCT
would keep the requirement. (The doubling may be worth a glance in its own right — we have not
looked into whether the pairs differ in tier or are a duplicate row.)

But those 701 records have **no instance data table at all** — no `schema:variableMeasured` and no
tabular part. An XCT product is a reconstructed volume, and if its results are not in fact tabulated
per sampling unit, the six keyed rows may be the thing to revisit rather than the Core item.

**The question:** for a laboratory XCT volume, are segmentation thresholds and the other five keyed
items genuinely per-sampling-unit values belonging in a table — or are they procedure-level
settings that were keyed by analogy with the point-analysis techniques? If the latter, un-keying
them is a smaller and more accurate change than exempting XCT from a Core field.

We are not proposing an answer. The reason for asking is that the two possibilities lead to
opposite fixes, and only you can say which describes an XCT session.

**Not the same question as `schema:actionProcess`.** That one also blocks those records, and it is
**ours, not yours**: no row declares it, and our emitter was requiring it because 69 authored rows
place leaves beneath `$Dataset.prov:wasGeneratedBy.schema:actionProcess.schema:step[…]` and it
required every ancestor a Basic leaf navigates through. Stephen has decided we fix that in the
emitter. Mentioned only so the two are not merged — an earlier draft of ours did merge them, on the
false reasoning that an image stack is not an instrument session.

---

## 5. Delivery mechanics


**composed_tapps.json `tapp` paths do not match the delivery layout.** The manifest records per-technique paths such
as `EPMA/EPMA_TAPP_v88.csv`, while the delivery puts every table in a flat `Current TAPPs/` folder —
so **0 of 16 entries resolve** as written, while **16 of 16 resolve by basename**. We resolve by
filename instead. (Re-measured 2026-10-18: still 0 of 16; only the version in the example has
moved, v60 → v88.) Either the manifest
or the layout should move, since a consumer following the manifest literally finds nothing.

> **Half of this is now fixed.** The *version* drift — six entries naming superseded files, filed as
> [amds-ldeo/tapp#5](https://github.com/amds-ldeo/tapp/issues/5) — was root-caused in `4d684d3`:
> `bump_for_module_20260827.py` set `generated` but never updated `e["tapp"]`, so a recomposition
> pass edited the superseded copy and reported MATCH. Fixed in the script, not just the data, with
> a `register-stale-tapp-path` guard. All 16 basenames are current as of `af3f7bc`. The *directory
> prefix* still does not resolve, which is what this entry is now about.

**Modules ship in three places.** `Claude Skills for TAPP/modules/` (confirmed authoritative),
`Claude Skills for TAPP/references/modules/`, and a `.json` beside each `.csv`. Knowing which the
`.json` is for — generated view, or a second source — would help; we currently read only the CSVs.

---

## 6. NOT FOR RUOLIN — ADA records no acquisition mode, so the mode flags cannot be honoured

**Audience: ADA and its data submitters, not the TAPP author.** Recorded here because it is the
upstream blocker for a TAPP feature, and because the natural reading of the symptom is "gBB has
not implemented the mode flags yet", which is wrong and would send the work to the wrong place.

The workbooks' design is complete and correct. Mode-flag columns state per-field applicability,
`Analytical Mode` declares the modes a procedure executes, and the Purpose cell spells out the
split. **284 field rows across 14 techniques** carry mixed `Y`/`N` applicability — and only those
14 of 61 have mode-flag columns at all; for the other 47 the mode is informational and gates
nothing. Nothing is wrong with
the tables.

What is missing is the data. Measured on the live corpus 2026-10-21:

| | |
|---|---|
| `ada:analyticalMode` in the 7,447 records | **0** |
| any key containing "mode" in 111,963 `record_subjects` | **0** |
| `componentType` naming EDS | 502, all SEM/STEM/TEM |
| `componentType` naming WDS | **0** |
| EPMA records with an EDS signal in `componentType` | **0 of 436** |

So a mode cannot be read, and for EPMA it cannot be derived either. The consequence is concrete:
`EDS Dead Time` is marked `N` for both WDS modes in `EPMA_TAPP_v88`, yet it is required of all 436
EPMA records, 436 of which fail it — and no conditional can excuse the WDS ones, because nothing
in ADA says which were WDS.

**The ask, for whoever owns ADA intake:** record the acquisition mode, or the detector used, per
analysis. One controlled value per dataset — or per `hasPart` item, since **264 records** already
mix EDS and non-EDS parts in a single distribution — would make 284 workbook rows enforceable as
their author intended.

Until then the interim answer is the nil token (`http://www.opengis.net/def/nil/OGC/0/unknown`),
which is literally true on these numbers: ADA holds no record of a dead time that does not exist,
only of one nobody sent. See `docs/ANALYTICAL_MODE.md`.

Three anchors were measured and rejected, so they need not be retried: instrument components
(0 of 7,447 records carry any `schema:hasPart` on an instrument), instrument `schema:additionalType`
(present on all 7,447, one distinct value, `nxs:base_classes/NXinstrument.html`), and the
`prov:used` TAPP reference (7,263 records carry one, but the `@id` is an opaque per-lab URI that
JSON Schema cannot dereference).

---

## Settled, recorded here so it is not re-litigated

- **Protocol → Procedure** renamed 61 items across the 2026-08 tables. Carried automatically.
- **`Sample IGSN` → `Sample Persistent Identifier`**, **`Sample Sequence Design` → `Analysis
  Sequence`**, **`Target Foil Thickness` → `Foil Thickness`**, **`Mass Resolution per Analyte` →
  `Mass Resolution Assignment`** — renames beyond the mechanical rules, each confirmed against the
  new table's Description before its authored paths were moved.
- **`Spatial Resolution` + `Minimum Resolvable Feature Size` → `Effective Spatial Resolution
  (PSF/MTF)`** — a 2→1 merge in Lab-XCT, confirmed by Stephen 2026-08-13.
