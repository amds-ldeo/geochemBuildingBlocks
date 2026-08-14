# Requests to the TAPP library

Things the schema-generation work has found that can only be fixed upstream, in the tables and
modules Ruolin authors. We import those read-only ([.github/CODEOWNERS](../.github/CODEOWNERS)), so
nothing here is something we can change on our side.

Ordered by how much work each one saves. Every number is measured against the 2026-08-13 delivery
and reproducible with the tool named beside it.

---

## 1. The LA family needs more modules — 83 shared fields have none

**The finding.** The six LA tables (Q/SF/MC, each with a UPb variant) hold 153 distinct fields.
**115 of them appear in all six.** The existing modules cover 42. The remaining **73 are duplicated
six times over**, and 10 more are shared by four or more tables with no module either.

| shared by | fields | in a module | in none |
|---|---|---|---|
| all 6 tables | 115 | 42 | **73** |
| 4–5 tables | 10 | 0 | **10** |

**Why it matters to us.** Without modules for these, generating schemas for the six LA tables means
authoring six near-identical sets of schema paths — about 230 placements, most of them the same
decision repeated. That is the drift the module system exists to prevent, and it is why the LA
configs are on hold: we would rather wait than manufacture six copies of an ICP-MS core that should
be one module.

**Proposal.** The 83 fields cluster cleanly. Suggested groupings, for you to name and scope:

- **ICP-MS instrument core** — ICP-MS Manufacturer & Model, ICP-MS Type, RF Power, coolant /
  auxiliary / carrier gas flow rates, Torch Type, Torch Depth, Interface Cone Configuration,
  Sampler and Skimmer Cone Material, Guard Electrode, Plasma Thermal Mode, Detector Configuration,
  Ion Counter Dead Time, Sample Introduction, Instrument Serial Number or Lab Identifier, ICP
  Tuning, Instrument Warm-up / Session Duration Limit
- **Collision / reaction cell** — CRC Configuration, Collision Gas Type and Flow Rate, Reaction Gas
  Type and Flow Rate, Cell Exit Discrimination Voltage
- **Signal acquisition** — Dwell Time per Mass, Signal Integration Time, Signal Integration Interval
  Method, Total Integration Time per Output Data Point, Background Count Time, Number of Replicates,
  Signal Smoothing, Monitored Isotopes, Mass Resolution Setting, Mass Resolution Assignment
- **Interference handling** — Interfering Species, Isobaric Interference Corrections Applied,
  Interference Correction Method, Oxide Production, Oxide Production Method and Threshold,
  Doubly-Charged Species Production, Doubly-Charged Species Monitor
- **Calibration and uncertainty** — Detection Limit, Detection Limit Method, Limit of Quantification
  (LOQ) Method, Within-Session and Between-Session Analytical Precision and Assessment Method,
  Analytical Accuracy and Assessment Method, Uncertainty Level, Uncertainty Propagation Method,
  Primary Calibration Standard Name, Secondary Reference Materials, Per-Analyte Calibration
  Strategy, Internal Standard Approach, Internal Standard Element, Normalization / Standards-Based
  Correction, Blank / Background Correction Method
- **Sample / specimen** — Sample Name, Sample Persistent Identifier, Sample Form / Analytical
  Substrate, Sample Preparation Method, Target Material, Sampling Unit

The last group is the widest: those six are shared by **every** technique, not only LA, yet none is
in Group1 or ReportingCore. They may belong in one of those rather than a new module.

*Reproduce:* the per-field counts come from the six `Current TAPPs/LA-*.csv` tables against
`Claude Skills for TAPP/modules/Module_*.csv`.

---

## 2. `Module_UPb` — 12 of its 15 rows carry no tiers

Only `Chemical Abrasion Conditions`, `Intermediate Daughter Disequilibrium Correction` and
`Discordance Definition and Values` have a Procedure or Analysis tier and a Description. The other
twelve carry only an `Example / Allowed Content` value, against fields `Module_Geochronology` and
`Module_ReportingCore` own.

We read those as **example overlays, not owned fields**, and generate nothing for them — a module
row with no tier has no requiredness to express and no placement to author. Confirming that reading
would be useful; if they are meant to be owned, they need tiers.

`Module_Geochronology` has no such rows, so the pattern looks deliberate rather than accidental.

*Reproduce:* `python tools/build_module_bb.py`

---

## 3. `Module_ReportingCore` carries six fields that seven tables do not

The manifest says all sixteen tables compose ReportingCore, but seven lack fields the module
declares — 18 (field × table) pairs:

- **Lab-XCT, SEM-FIBSEM, SEM-Imaging, TEM** lack Procedural Blank Level, Goodness-of-Fit or
  Dispersion Statistic, Analysis Inclusion and Rejection Criteria
- **Solution Q, SF, MC** lack Target Selection Criteria, Pre-Analysis Imaging and Screening

Composing gives those tables the fields, which is reasonable if the module is the newer statement of
intent — but `Analysis Inclusion and Rejection Criteria` and `Target Selection Criteria` are
Procedure-Level Basic, so they become **requirements those tables never stated**. Is the module
ahead of the tables, or are those tables genuinely exempt?

Everything else agrees exactly: across 578 (module field × consuming table) pairs where the table
carries the field, tiers match in **all 578**. No TIGHTENS, LOOSENS or ABSENT anywhere.

*Reproduce:* `python tools/module_conflict_check.py`

---

## 4. `Error Correlation Between Reported Quantities` belongs to no module

It appears in the UPb tables and in none of the eight modules — the only UPb-specific field with no
module home. Should it join `Module_UPb` or `Module_Geochronology`?

---

## 5. Delivery mechanics

**`composed_tapps.json` did not ship with the 2026-08-13 drop.** Stephen copied it across from
Drive. Since it declares what composes what, a delivery without it leaves the composition
undescribed; our tooling now falls back to the newest manifest in any delivery and says which one it
used, but the fallback is a workaround.

**Its `tapp` paths do not match the delivery layout.** The manifest records per-technique paths such
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
