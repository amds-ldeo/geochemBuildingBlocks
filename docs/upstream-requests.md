# Requests to the TAPP library

(from claude with SMR edits)

Things the schema-generation work has found that can only be fixed upstream, in the tables and modules Ruolin authors. SMR imports those read-only ([.github/CODEOWNERS](../.github/CODEOWNERS)), so I don't want to change in my github unless you give me the go ahead....

Ordered by how much work each one saves. Every number is measured against the 2026-08-13 delivery and reproducible with the tool named beside it.  I copies teh 8-13 drop from the google drive. 

---

## 1. The LA family needs more modules — 83 shared fields have none

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
above. Two are ICP-MS-specific and could join a group — `Mapping Area` and `Pulse / Analog Detector
Nonlinearity Correction`. The other **seven are universal**, and this is a finding in its own right:

> `Acquisition Software` · `Data Reduction Software` · `Analytical Mode` · `Analyte` ·
> `Reported Variables and Units` · `Constants and Reference Values Used` · `Additional Notes`

Your README §10 lists most of these among the fields "present in all 16" — yet none is in `Group1`
or `ReportingCore`, so every TAPP carries its own copy. If the sample/specimen six belong in an
existing module, these seven probably do too, and that is a change to `Group1`/`ReportingCore`
rather than a new module.

*Reproduce:* `python tools/draft_module.py --measure` — it reads the six `Current TAPPs/LA-*.csv`
tables and your `Claude Skills for TAPP/modules/Module_*.csv`, and refuses any field whose
definition differs between tables rather than averaging it.

---


---

##  `Error Correlation Between Reported Quantities` belongs to no module

It appears in the UPb tables and in none of the eight modules — the only UPb-specific field with no
module home. Should it join `Module_UPb` or `Module_Geochronology`?

---

##  Delivery mechanics


**composed_tapps.json `tapp` paths do not match the delivery layout.** The manifest records per-technique paths such
as `EPMA/EPMA_TAPP_v20.csv`, while 2026-08-13 puts every table in a flat `Current TAPPs/` folder —
so **0 of 16 entries resolve** as written. We now resolve by filename instead. Either the manifest
or the layout should move, since a consumer following the manifest literally finds nothing.

**Modules ship in three places.** `Claude Skills for TAPP/modules/` (confirmed authoritative),
`Claude Skills for TAPP/references/modules/`, and a `.json` beside each `.csv`. Knowing which the
`.json` is for — generated view, or a second source — would help; we currently read only the CSVs.

---

## Settled, recorded here so it is not re-litigated

- **Protocol → Procedure** renamed 61 items across the 2026-08 tables. Carried automatically.
- **`Sample IGSN` → `Sample Persistent Identifier`**, **`Sample Sequence Design` → `Analysis
  Sequence`**, **`Target Foil Thickness` → `Foil Thickness`**, **`Mass Resolution per Analyte` →
  `Mass Resolution Assignment`** — renames beyond the mechanical rules, each confirmed against the
  new table's Description before its authored paths were moved.
- **`Spatial Resolution` + `Minimum Resolvable Feature Size` → `Effective Spatial Resolution
  (PSF/MTF)`** — a 2→1 merge in Lab-XCT, confirmed by Stephen 2026-08-13.
