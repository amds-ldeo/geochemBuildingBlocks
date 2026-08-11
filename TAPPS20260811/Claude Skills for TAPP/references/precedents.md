# TAPP Precedent Decisions

This file documents the key non-obvious decisions made during LA-ICP-MS TAPP development, with the reasoning that led to each decision. These serve as precedents for future TAPPs — when a similar question arises, check here before opening a new discussion.

Each entry follows the format: **Decision → Reasoning → Generalization**.

---

## Group 4: Measurement Information

### Ablation Duration vs. Analysis Count Time

**Decision:** These are two distinct fields with different tier assignments. Ablation Duration per Spot is procedure-level Basic (C=Basic, D=Editable for spot mode only). Analysis Count Time was removed as a procedure-level field and replaced by Signal Integration Time at analysis level only (C=N/A, D=Basic, spot/transect only, J=N).

**Reasoning:** Ablation Duration is set in the acquisition method file before the session begins and is a deliberate procedure design choice (it reflects a trade-off between signal accumulation, sample consumption, and throughput). A reproducibility expert needs to know it. Analysis Count Time, by contrast, is the width of the integration window selected during data reduction after the ablation transient is inspected — it depends on when the signal stabilizes and may vary by sample. The Signal Integration Interval Method (the rule for choosing the window) is procedure-level; the resulting count time is analysis-level.

**Generalization:** Whenever a procedure specifies a duration and data reduction later selects a sub-interval of that duration, treat them as separate fields: the duration belongs in Group 4 (Measurement Information) at procedure level; the selected interval belongs in Group 5 (Data Processing) at analysis level. The method for selecting the interval is procedure-level (Group 5); the resulting time is analysis-level (Group 5, C=N/A).

**Mode note:** For mapping, the per-pixel cycle time is determined entirely by dwell times (a procedure-level Group 4 field) — there is no post-hoc window selection per pixel. So Signal Integration Time is J=N (not applicable to mapping). The description must explain this explicitly.

---

### Ablation Duration — mode-dependent tier

**Decision:** Ablation Duration per Spot is procedure-level Basic for spot analysis only (H=Y, I=N, J=N). The corresponding concept for transect (total transect duration) and mapping (total map acquisition time) is analysis-level, not procedure-level, and therefore is not a TAPP field at all.

**Reasoning:** For spot analysis, ablation duration is set once in the acquisition method and applied identically to every analysis — it is genuinely procedure-level. For transect, the total duration depends on the transect length, which is determined at analysis time by the size of the grain or feature being profiled. The procedure fixes the scan speed; the transect length (and therefore duration) varies by sample. For mapping, the total acquisition time depends on the map area, which is also sample-dependent. In both cases, the procedure captures what it can (scan speed for transect; scan speed + line spacing for mapping) and leaves the variable parts to the analysis record.

**Generalization:** When a duration is fully determined by the procedure (spot mode), it belongs in the TAPP. When a duration is determined by a fixed procedure parameter × a variable sample parameter (transect: speed × length), the procedure captures the fixed parameter and the analysis captures the variable one. Total duration is always analysis-level in this case.

---

### Oxide Production: two fields, not one

**Decision:** Two separate fields: "Oxide Production Method and Threshold" (C=Basic, D=Read-Only) captures the acceptance criterion and measurement proxy; "Oxide Production" (C=N/A, D=Basic) captures the actual measured ratio from the session.

**Reasoning:** These serve fundamentally different purposes. The threshold is a quality gate used during instrument tuning before analysis begins — it is part of the procedure design and should never change between analyses following the same procedure. The measured value documents actual plasma conditions in the session and varies day to day. Combining them in one field either conflates a criterion with a measurement or forces one of them to be blank in most entries.

**Generalization:** Whenever a procedure specifies an acceptance criterion (threshold, maximum allowable value, or minimum acceptable value) and the analysis records an actual measurement against that criterion, split into two fields: [Concept] Method and Threshold (procedure-level) and [Concept] (analysis-level measured). Other techniques where this pattern applies: instrumental blank threshold (solution ICP-MS), peak flatness criterion (MC-ICP-MS), detector dead time threshold (TIMS).

---

### Analyte — single merged field

**Decision:** One field: "Analyte" (C=Basic, D=Editable). The procedure registers the isotope suite the procedure is designed to measure; at analysis level the analyst records the specific isotopes actually measured in the session, which may be a subset of the procedure scope.

**Reasoning:** "Target Analyte" and "Analyte" represent the same type of information (an isotope list) at different stages, not fundamentally different data. D=Editable correctly models the relationship: the procedure-registered suite is imported into the analysis metadata form; the analyst may narrow it if certain masses were excluded due to interference issues or detector limitations in that session. This is structurally identical to other session-tunable parameters (laser fluence, flow rates), which also use D=Editable. Splitting into two fields (as done in earlier versions) created an unnecessary decoupling — the procedure value could not be auto-imported into the analysis form.

**Contrast with Oxide Production split:** The Oxide Production pair (acceptance criterion vs. measured value) is kept as two separate fields because the criterion and the measurement are *different types of information* — one is a quality gate, the other is an instrumental outcome. The Analyte case has no such distinction: procedure scope and analysis execution are the same quantity at different stages.

**Generalization:** When a procedure defines the intended scope of measurements and individual analyses may execute a subset of that scope, use a single field with C=Basic, D=Editable. Do not split. This applies to: isotope suites (isotope ratio MS), element panels (ICP-MS), spectral windows (Raman, FTIR), feature sets (XCT). The split pattern is reserved for cases where the procedure-level and analysis-level components are genuinely different types of information (criterion vs. measurement).

---

### Scan Speed — procedure or analysis level?

**Decision:** Scan speed is procedure-level (C=Advanced, D=Editable) for methods where it is fixed, but becomes analysis-level when the procedure specifies a target spatial resolution rather than a fixed speed. The TAPP field "Transect Rate, Mapping Rate or Step Size" is procedure-level.

**Reasoning:** When a procedure specifies "scan speed = 9 µm s⁻¹" as an invariant, this is a genuine procedure parameter — it constrains every analysis following this procedure. When a procedure instead specifies "target pixel size = 5 µm" (from which scan speed is calculated at analysis time based on spot size and repetition rate), the target pixel size is procedure-level and the resulting scan speed is analysis-level. In the TAPP, the field captures the procedure-level specification (either fixed speed or target resolution/rate); the description explains both interpretations.

**Generalization:** When a parameter is either directly fixed by the procedure or derivable from other fixed procedure parameters (making it a procedure-level derived value), it belongs in the TAPP. When it is derived at analysis time from a combination of procedure parameters and sample-dependent variables, it is analysis-level.

---

### Signal Smoothing — applicable to all modes with caveat

**Decision:** Signal Smoothing applies to all modes (H=Y, I=Y, J=Y) but the description explicitly flags that smoothing devices are generally incompatible with high-resolution mapping.

**Reasoning:** Excluding mapping entirely (J=N) would hide an important methodological fact: using a smoothing device for mapping degrades spatial resolution by averaging aerosol pulses from successive laser shots. Analysts choosing to run a smoothed mapping procedure should be aware of this. By keeping J=Y with a warning in the description, the TAPP ensures the field appears in mapping contexts where the user can explicitly note "None" — documenting an intentional absence rather than a missing value.

**Generalization:** Set J=N (or equivalent mode flag) only when the concept is genuinely inapplicable (e.g., "Ablation Duration per Spot" cannot apply to mapping because there is no discrete "spot analysis"). Set J=Y with a caveat when the concept applies but its implementation or appropriateness differs for mapping. This preserves the ability to document the absence of a parameter as a deliberate choice.

---

## Group 5: Data Processing

### Uncertainty Propagation Method — Advanced/Editable rather than Basic/Read-Only

> **Scope narrowed 2026-08-10.** This entry governs the PROPAGATION FRAMEWORK only. The
> uncertainty *level* was split out into its own field, `Uncertainty Level` (C=Basic,
> D=Read-Only) — see "Uncertainty Level split from Uncertainty Propagation Method" below.
> The reasoning here is unchanged and still applies to propagation.

**Decision:** C=Advanced (not Basic), D=Editable (not Read-Only).

**Reasoning (two parts):**
- Why Advanced at procedure level: Many labs use informal uncertainty estimates (e.g., "SD of replicate analyses") without a formally specified propagation framework. Requiring a formal propagation method as Basic would either exclude many legitimate procedures or generate low-quality boilerplate. Advanced encourages rigorous labs to document their approach without mandating it universally.
- Why Editable at analysis level: If D=Read-Only and the procedure-level value is void (because C=Advanced and the author chose not to specify it), Read-Only would import a blank value that the analyst cannot fill in. Editable allows the analyst to complete this field when the procedure author left it unspecified, without constituting a violation of the procedure.

**Generalization:** When a field is Advanced at procedure level (meaning it may be void in the procedure), the analysis-level tier should almost never be Read-Only. Read-Only imports the procedure value — importing void is useless. Use Editable instead, allowing the analyst to supply the value. This is the standard resolution for the "Advanced procedure / analysis needs a value" tension.

---

### Signal Integration Interval Method — procedure-level Basic

**Decision:** C=Basic (the approach is procedure-level and mandatory). The description covers spot/transect (time-window selection) and mapping (VOI selection, phase masking) as mode-specific implementations of the same concept.

**Reasoning:** Without documenting the integration approach, a data record is uninterpretable: the reader cannot know whether specific phases were excluded from integration, whether an automated or manual approach was used, or whether the data is spatially averaged or phase-specific. This is arguably one of the most important data provenance fields in Group 5. It should be Basic.

The fact that the approach means different things for different modes (time-window vs. VOI) does not disqualify it from being a single field — the description handles the mode-specific implementation. The underlying concept (how was the usable signal distinguished from the non-usable signal?) is universal.

**Generalization:** When a concept is mode-universal in purpose but mode-specific in implementation, keep it as one field and address the implementation variation in the description. Do not split into mode-specific fields unless the implementations are so different that a shared field name would be genuinely misleading.

---

### "Constants and Reference Values Used" as a mandatory Group 5 field — purpose and distinction from Reference Material Information

**Context:** Identified while building a test TAPP for LA-ICP-MS U-Th-Pb Geochronology (derived from
Horstwood et al. 2016's community reporting standard), motivated directly by a footnote in the paper's own
Table 4 ("Decay constants of Jaffey et al. (1971) used") — information the paper's own Table 3 metadata
template never captured as a structured item, despite feeding directly into every reported age.

**Decision:** Mandatory field in Group 5 of every TAPP (Rule 5), C=Basic, D=Editable, Text (free). Record
"None" when not applicable. Applied universally — including pure-imaging/morphology TAPPs — rather than
scoped only to techniques with plausible constant-dependent data reduction (decided 2026-07-28; see Rule 5
in `references/conventions.md`).

**Reasoning:** Community-recommended values for physical constants used in data reduction — decay
constants, standard isotope ratios — are periodically revised. The ²³⁸U/²³⁵U ratio is a concrete precedent:
long assumed constant at 137.88 (Steiger & Jäger 1977), then shown by Hiess et al. (2012) to vary in
nature, prompting many labs to adopt 137.818 or sample-specific values instead. A reported age computed
under the old value cannot be correctly reinterpreted against the new one unless the original value used is
documented. This is distinct from Reference Material Information (Group 6), which documents accepted
values of *specific materials* (e.g., zircon 91500's isotopic composition) rather than *universal physical
constants* that apply regardless of which material was run.

**Generalization:** Most consequential for geochronology and any isotope-dilution-dependent technique
(⁴⁰Ar/³⁹Ar, Sm-Nd, Rb-Sr all have analogous decay-constant-revision histories), but written generally since
data reduction in any technique could in principle depend on a citable, revisable constant. Mirrors the
"Analytical Mode" precedent (Rule 3, above in Group 4): a mandatory cross-TAPP field whose universal
presence is itself informative, distinguishing "deliberately none" from "not asked."

---

## Group 6: Quality Control & Uncertainty

### Detection Limit — C=Advanced, D=Basic asymmetry

**Decision:** C=Advanced (optional at procedure level), D=Basic (mandatory at analysis level). This asymmetry is intentional.

**Reasoning:** At procedure registration time, formal LOD characterization may not yet be complete — a newly designed procedure may be registered before extensive blank measurements have been accumulated. Requiring LOD as Basic at procedure level would either block registration of new procedures or result in unreliable LOD values that the community cannot trust. Advanced is appropriate: thorough labs will include it; others will add it as the procedure matures. At analysis time, however, LOD is non-negotiable for data credibility: a published dataset without LODs cannot be properly interpreted near detection limits. Basic is appropriate at analysis level.

**Generalization:** The C/D asymmetry (Advanced procedure / Basic analysis) is the correct design for any QC metric that requires accumulated session data to characterize properly but is mandatory for any complete data submission. Other fields that warrant this treatment: detection limit method, precision, accuracy, LOQ.

### Precision and Accuracy — combined value + assessment method

**Decision:** Each precision/accuracy field captures both the assessment method and the resulting values in a single combined field. These are not split into separate "Method" and "Value" fields despite the LOD/LOD-Method split precedent.

**Reasoning:** The LOD/LOD-Method split was justified because LOD Method is a formula (a procedure-level design choice) while LOD Value is session-specific (an analysis-level outcome). For precision and accuracy, both the method and the value are Advanced/Basic at the same levels — they belong together. The method (which reference material, how many replicates, which statistic) is inseparable from the value because the same number means different things depending on how it was obtained. Splitting them would create two fields that are always filled together, adding complexity without benefit.

The description for each precision/accuracy field must explicitly require both components: the assessment method (RM used, n, statistic) and the values (per element or element group). A value without a method context is nearly uninterpretable for cross-study comparison.

**Generalization:** Split method from value when they have different tier assignments (LOD pattern). Merge them when they have the same tier assignments and are always used together (precision/accuracy pattern). The test: would either component ever be filled without the other? If no, merge.

---

## Structural Decisions

### D=N/A removed as a valid analysis-level tier

**Decision:** D=N/A is no longer a valid analysis-level tier. Fields that are relevant only at procedure level (no session-specific variation, no fresh analyst input) are assigned D=Read-Only. The procedure value is inherited into the analysis metadata form and displayed as read-only.

**Reasoning:** D=N/A ("not applicable at analysis level") and D=Read-Only ("imported from procedure, cannot be changed") produced identical behavior in the analysis submission pipeline: the value comes from the procedure and the analyst cannot modify it. The distinction provided no functional difference. Removing D=N/A simplifies the tier system to four valid analysis-level values and eliminates a source of inconsistency (e.g., "Funding Source for Procedure Development" was N/A while structurally identical fields like "Procedure Author" were Read-Only). The new invariant: every field must have a meaningful analysis-level assignment.

---

### Level-neutral field naming

**Decision:** Field names must not encode which level a value belongs to. Prefixes and suffixes such as "Default", "Target", "Achieved", "Typical", and "Actual" are not used in field names. The tier columns (C and D) encode level. Column B (Description) clarifies that the procedure registers a target or typical value and that analysts may adjust within allowed bounds.

**Reasoning:** Level-embedded names ("Default Laser Fluence", "Target Analyte", "Achieved Voxel Size") required either maintaining a separate column mapping procedure names to analysis names, or accepting that the Column A names were unusable as-is when building an analysis metadata form. Level-neutral names ("Laser Fluence", "Analyte", "Voxel Size") work directly at both levels.

**Exceptions retained:** "Target Material" and "Target Feature(s)" keep "Target" because it means *the material or feature type the procedure is designed to analyze*, not a value with a later achieved counterpart. These fields have no analysis-level counterpart requiring a different name.

---

### Coupled analysis fields — four standard fields in Group 1

**Decision:** Every TAPP includes four standard fields at the end of Group 1 (after Procedure Reference(s)) documenting multi-technique workflows: Coupled Technique(s), Coupling Description, Coupled Procedure DOI, and Coupled Dataset or Publication Reference. Default tiers: Coupled Technique(s) C=Advanced/D=Editable; Coupling Description C=Advanced/D=Editable; Coupled Procedure DOI C=N/A/D=Advanced; Coupled Dataset or Publication Reference C=N/A/D=Advanced. Individual TAPPs may adjust D tiers when coupling is computationally mandatory.

**Reasoning:** Many analytical techniques are routinely applied in combination — EPMA providing internal standard concentrations for LA-ICP-MS, XCT paired with NCT for complementary contrast, ICP-MS and noble gas MS jointly required for (U-Th)/He geochronology. Without standardised fields capturing what is coupled, how the coupling works functionally, and where the companion data lives, multi-technique datasets cannot be navigated or reproduced reliably. Group 1 is the correct location because coupling is an administrative and provenance property of the procedure design, not an instrument parameter.

**Why four fields and not fewer:** Coupled Technique(s) and Coupling Description are separated because the former enables machine-readable filtering (find all procedures coupled with EPMA) while the latter carries human-readable context that cannot be reduced to a controlled list. Coupled Procedure DOI and Coupled Dataset or Publication Reference are separated because the procedure DOI is stable and citable immediately upon procedure registration, while the dataset reference may be pending, co-submitted, or shared — the two fields have different lifecycles and reliability profiles.

**Dataset reference limitations:** A DOI pointing to a combined dataset submission does not uniquely identify which instrument produced which portion. Where coupling is documented only through a shared sample IGSN, the IGSN in Group 2 (Sample Persistent Identifier) is sufficient and the Coupled Dataset or Publication Reference field may be "None". The Coupled Procedure DOI is generally more reliable than the dataset reference and is the preferred machine-actionable link.

---

### Analysis-level fields in Group 1 (Procedure Identification)

**Decision:** Several analysis-level fields (Analyst, Analysis Start/End Date, Funding Source for Analysis) reside in Group 1 alongside procedure-level fields such as Procedure Name and Procedure Author.

**Reasoning:** Group 1 serves as the administrative header for both the procedure record and the analysis record. Analysis-level identity fields (who ran the analysis, when, under what funding) are logically co-located with procedure identity fields (who designed the procedure, when, under what funding) even though they have different tier assignments. Separating them into a different group would fragment the administrative context.

The mixed-tier nature of Group 1 is a feature, not a design inconsistency. It reflects the reality that the same form serves both procedure registration and analysis documentation.

### Procedure DOI — C=N/A, D=Basic (mandatory at analysis level)

**Decision:** Procedure DOI has no procedure-level value (C=N/A, because the DOI does not exist at the time of registration) but is mandatory at analysis level (D=Basic). The description explicitly states that if a DOI has been applied for but not yet minted, "pending" is an acceptable placeholder.

**Reasoning:** This field exists primarily as a policy instrument to encourage procedure registration. Making it mandatory at analysis level creates a direct incentive: analysts who want to submit data must have a procedure DOI (or at least have applied for one). The "pending" option prevents analysts from being blocked while waiting for DOI assignment.

The C=N/A / D=Basic combination is unusual (most analysis-level Basic fields also have a procedure-level presence) but is correct here because the DOI is a product of the registration process, not an input to it.

---

### Group 1 template — superseded by `modules/Module_Group1.csv` (migrated 2026-08-08)

**Decision (2026-05):** Every new TAPP begins Group 1 from a shared template holding the field list, tier assignments and technique-neutral descriptions; technique-specific examples are added per TAPP.

**Superseded 2026-08-08.** The template was *copied* into each TAPP, and the copies drifted: 14 of 17 descriptions in LA-Q/SF-ICP-MS diverged, field order diverged in 5 TAPPs, and one tier diverged in 3. Group 1 is now **composed** from `modules/Module_Group1.csv` under Rule 6, so the content exists in one place and cannot drift. The column-ownership split the template established informally — shared descriptions and tiers, per-TAPP examples — became the formal module contract.

**Reasoning:** Group 1 is designed to be largely transferable across TAPPs. Maintaining a single template prevents drift in field names, tier assignments, and descriptions across the TAPP library. The Coupled Technique(s) and Coupling Description fields in the template use technique-neutral language; each TAPP's example column provides technique-specific coupling examples.

---

### Group 3 software fields — D=Editable

**Decision:** Acquisition software and data reduction software fields in Group 3 are D=Editable (not D=Read-Only).

**Reasoning:** A minor version update to acquisition or data reduction software (e.g., Probe for EPMA v12.9 → v12.9.5, Iolite 4.6 → 4.7) does not constitute a new procedure — instrument hardware, operating conditions, and data reduction algorithms are unchanged. Analysts running under a minor version update should document the actual version used without being forced to register a new procedure. D=Editable is correct: the procedure registers the software name and major version; the analyst confirms or updates the minor version at analysis time.

**Contrast with hardware fields:** Instrument manufacturer, model, detector configurations, and other hardware parameters are D=Read-Only because a hardware change (different instrument, different detector) fundamentally changes what is being measured and must constitute a new procedure.

---

### Reference materials (Group 6) — C=Basic, D=Editable

**Decision:** Primary Calibration Standard Name and Secondary Reference Materials are C=Basic, D=Editable.

**Reasoning:** The procedure must commit to a specific set of reference materials (C=Basic — mandatory for procedure registration, because the choice of standards directly determines the accuracy of all results). However, at analysis time, a primary standard may be exhausted, unavailable, or temporarily substituted due to logistics. D=Editable allows the analyst to document the actual material used without being forced to register a new procedure for what is effectively a material availability substitution. The analyst is expected to note any substitution explicitly. This applies to both primary calibration standards and secondary reference materials (QC standards).

---

### WDS vs. EDS dead time — intentional asymmetry between correction method and measured value

**Decision:** WDS dead time is documented as a procedure-level correction *method* (WDS Dead Time Correction, C=Basic, D=Read-Only in Group 5) with no separate measured value field. EDS dead time is documented as an analysis-level measured *percentage* (EDS Dead Time, C=N/A, D=Basic in Group 5) with no procedure-level correction method field. These are two separate fields with no "method + value" paired structure.

**Reasoning:** The physics of dead time handling differs fundamentally between the two detector types:
- **WDS:** Dead time correction is a user-selectable mathematical algorithm (constant 3 µs, high-precision, logarithmic, etc.) embedded in the data reduction software. The analyst chooses the algorithm as a procedure design decision; it is applied transparently during intensity-to-concentration conversion. No standalone "WDS dead time" value is separately reported because the correction is absorbed into the quantitative result.
- **EDS:** Dead time correction is automatic — managed entirely by the SDD detector electronics. No user-selectable algorithm exists. What is reported is the *percent dead time*: the fraction of total acquisition time the detector spent processing rather than counting, which serves as a QC metric for count rate management. Values above ~40% indicate excessive count rate and degraded data quality.

**Generalization:** When a correction is user-selectable and algorithm-dependent, document the method at procedure level (no measured value needed). When a correction is hardware-automatic and produces a reportable QC metric, document the metric at analysis level (no method needed). Do not force a method+value split onto detector-specific processes that do not share the same structure.

---

### Beam mode (geometry) — D=Read-Only

**Decision:** Beam Mode (Focused / Defocused / Raster in EPMA; equivalent geometry fields in other techniques) is D=Read-Only.

**Reasoning:** The beam geometry is a procedure design choice tied to the target material type and analysis objective. A procedure that specifies "Focused beam for anhydrous silicates; 5 µm Defocused for glass and hydrous phases" encodes a deliberate methodological decision. Analysts follow this specification — they do not deviate from the beam mode at analysis time. Changing beam mode constitutes a different analytical approach and should trigger procedure review. D=Read-Only is correct; D=Editable would imply the analyst may override the mode without a procedure change, which is not intended.

**Contrast with Beam Diameter and Beam Current**, which are D=Editable: those are tunable operating parameters that the procedure specifies as targets and the analyst confirms or fine-tunes. Beam Mode is a categorical choice, not a continuously tunable parameter.

---

### Analysis-level only fields (C=N/A) for spatially determined mapping parameters

**Decision:** Map Dimensions (pixel count in X and Y) and Map Area (physical extent in µm × µm) have C=N/A, D=Basic. Step Size / Pixel Size (spatial resolution) has C=Basic, D=Editable.

**Reasoning:** The procedure specifies *how fine* to map (Step Size = C=Basic — a deliberate resolution design choice). The *extent* of each map — how many pixels and what physical area — is determined entirely at analysis time by the sample feature or region of interest being mapped. A procedure cannot pre-specify which grain boundary or geological texture to map. Map Dimensions and Map Area are therefore analysis-level only (C=N/A, D=Basic): they must be recorded by the analyst but cannot be pre-specified.

**Generalization:** When a mapping parameter is determined by the spatial extent of an arbitrary sample feature chosen at analysis time, it is C=N/A (cannot be pre-specified in the procedure). When it controls the intrinsic spatial resolution of the technique (step size, dwell time), it is C=Basic (a procedure design choice the analyst may adjust within bounds).

---

### EDS architecture — instrument-agnostic acquisition fields vs. technique-specific quantification

**Context:** EDS is implemented across multiple instruments covered by separate TAPPs (EPMA, SEM, TEM/STEM). During Phase 4 revision of the TEM TAPP (2026-05), a cross-TAPP EDS harmonization review compared EDS fields in EPMA_TAPP_v5 and TEM_TAPP_v5.

**Decision:** EDS acquisition and detection fields are harmonized across TAPPs (identical field names, descriptions, and tier assignments where the physics is the same). EDS quantification fields diverge by instrument because the underlying physical model differs. The two quantification frameworks are treated as separate architectural domains — not harmonized — and are candidates for dedicated "EDS (bulk)" and "EDS (thin film)" TAPPs in the future.

**Harmonized fields (acquisition and detection layer):**
- EDS Detector Configuration — same field name and structure in EPMA and TEM
- EDS Live Time per Point or Pixel — harmonized name (renamed from "EDS Acquisition Time" in EPMA v5); description notes the EPMA per-point convention vs. TEM per-point/per-pixel distinction
- EDS Energy Range — instrument-agnostic
- EDS Spectral Processing Type — same field in both TAPPs (background fitting, peak deconvolution, etc.)
- EDS Dead Time — same field; C=N/A, D=Basic in both (hardware-automatic correction, QC metric only)
- Analyte (EDS) — merged from Target Analyte (EDS) + Analyte (EDS) in TEM v5, per the level-neutral naming rule (see below)
- EDS Calibration Standard(s) — same intent across instruments
- EDS Detection Limit — same intent

**Divergent fields (quantification layer):**
- EPMA uses ZAF or phi-rho-z matrix correction for bulk samples (infinite or semi-infinite geometry). The sample absorbs the full electron interaction volume. Quantification is well-established and software-implemented.
- TEM/STEM uses Cliff-Lorimer k-factor or ζ-factor methods for electron-transparent thin-film specimens (~30–100 nm). The sample is thin enough that absorption and fluorescence corrections are minimal or zero; the signal model is fundamentally different.
- These two quantification frameworks share no meaningful overlap in method vocabulary, calibration approach, or correction hierarchy. Harmonization would produce meaninglessly broad controlled vocabulary.

**Tier differences that remain intentional:**
- EDS Detector Configuration: C=Advanced in EPMA (instrument infrastructure, rarely procedure-defining); C=Basic in TEM (detector geometry — SDD position, window type — is a primary procedure factor for thin-film EDS sensitivity).
- EDS Live Time per Point or Pixel: C=Basic in EPMA (per-point time is a core procedure decision for count statistics); C=Advanced in TEM (acquisition time is secondary to probe current and sample thickness in thin-film EDS; the procedure specifies approximate targets, not binding values).
- EDS Acquisition Mode: D=Read-Only in EPMA/SEM/SEM_Composition; D=Editable in TEM (added 2026-08-11). The
  divergence follows from the two families' different mode sets, not from drift. The EPMA/SEM description
  says the field specifies beam positioning *"within the declared Analytical Mode"*, and those TAPPs carry
  `EDS Point Analysis` and `EDS Mapping` mode flag columns — once the mode is declared the acquisition
  strategy follows from it, so the value is imported and fixed. TEM's modes are TEM Imaging / STEM Imaging
  / Electron Diffraction, which encode nothing about EDS acquisition strategy, leaving it a genuine
  per-session choice. Reconciling would make one family wrong.

**Future direction:** As the TAPP family grows to include SEM-EDS and dedicated EDS procedures, consider creating "EDS Acquisition" as a shared module (fields 1–8 above) that is referenced by technique-specific TAPPs, rather than duplicating field definitions. A formal "EDS (bulk)" TAPP (covering EPMA + SEM bulk EDS) and "EDS (thin film)" TAPP (covering TEM/STEM EDS) would enable the quantification fields to be developed properly for each domain without compromising the shared acquisition vocabulary.

---

### "Analytical Mode" as a mandatory Group 4 field — purpose, placement, and distinction from related fields

**Context:** During a cross-TAPP consistency review of SEM_Composition_TAPP_v3 and EPMA_TAPP_v6 (2026-06), it was noted that the two TAPPs treated mode declaration differently. SEM v3 had an "Analytical Mode" field in Group 4; EPMA v6 had "Beam Mode" but no "Analytical Mode". This triggered a broader decision about whether "Analytical Mode" should be universal.

**Decision:** "Analytical Mode" is a mandatory first field in Group 4 (Measurement Information) in every TAPP, regardless of whether the TAPP has one analytical mode or many. It is assigned C=Basic, D=Read-Only, and flagged Y for all modes.

**Reasoning:** The mode flag columns (Y/N per field) answer the question "does this field apply to mode X?" — they serve a filtering and applicability function consumed by the sub-TAPP generation script and by the formatted xlsx view. "Analytical Mode" answers a different question: "what kind of measurement does this procedure describe?" — it is a human-readable declaration consumed by anyone reading a registered procedure record. A procedure registrant must be able to state in one field what the procedure covers. The two structures are complementary, not redundant.

**Why C=Basic, D=Read-Only:**
C=Basic because the analytical mode is the most fundamental procedure-level declaration — omitting it makes the procedure record ambiguous. D=Read-Only because if the analyst changes the mode they are running a different procedure, not adjusting within procedure-defined bounds.

**Allowed values are drawn from the mode flag column labels of that TAPP:**
The controlled vocabulary for "Analytical Mode" must match the mode flag column labels defined in Phase 0. This ensures internal consistency — a procedure that declares "Analytical Mode = WDS Point Analysis" will have all WDS Point Analysis fields marked Y in the mode flag columns, and sub-TAPP generation will include it in a WDS-filtered view. If the mode flag labels change in a future revision, "Analytical Mode" allowed values must be updated to match.

**Distinction from mode-specific sub-strategy fields that coexist with "Analytical Mode":**
Several TAPPs have additional mode-related fields in Group 4 that are NOT replacements for "Analytical Mode":

| Field | TAPP(s) | What it captures |
|---|---|---|
| Beam Mode | EPMA, SEM | Physical beam configuration (focused / defocused / rastered) — independent of analytical mode |
| EDS Acquisition Mode | EPMA, SEM, TEM | Spatial acquisition sub-strategy within EDS (point / linescan / map) |
| Analytical Sub-mode | TEM | Specific technique within a top-level TEM mode (BF-TEM, HAADF-STEM, SAED, PED, etc.) |

These fields describe *how* the measurement is conducted within a declared mode, not *what mode* the procedure targets. All four can coexist in the same TAPP without conflict.

**Retrofitting to existing TAPPs (as of 2026-06):**
The following TAPPs had "Analytical Mode" added during the 2026-06 review:
- EPMA: added in v7
- SEM: already present in v3; retained in v4
- LA-Q:SF-ICP-MS: added in v2
- Lab-XCT: added in v8
- TEM: added in v7
- LA-ICP-MS: added in v12

**Generalization:** Whenever a new TAPP is created, place "Analytical Mode" as the first field in Group 4 with C=Basic, D=Read-Only, allowed values = mode flag column labels. For single-mode techniques, the allowed values list contains one entry and the field still must be present.

---

### Modules — why composition replaced copying, and what the specificity test caught

**Context:** A review of the LA-ICP-MS Geochronology TAPP (2026-08) found it used instrument columns
(Q / SF / MC-ICP-MS) where every other TAPP uses analytical mode columns. Testing whether mode columns
should be renamed "application" columns led instead to a three-layer module architecture, formalised as
Rule 6.

**Decision:** Shared field content is held in one module file and composed into consuming TAPPs by
script, not copied into each TAPP and kept in step by hand.

**Reasoning:** Rule 4's propagation obligation had already failed on live content. `Funding Source for
Procedure Development` was C=Basic in 3 of 13 TAPPs against a template value of Advanced — a Group 1
field, squarely inside Rule 4's scope — and nobody noticed until a scripted comparison was run. 14 of 17
Group 1 descriptions in LA-Q/SF-ICP-MS had diverged from the template, and the divergence ran in both
directions: some were stranded *improvements* that never flowed back. Composition converts a rule that
depends on discipline into a property that holds by construction.

**The specificity test is the load-bearing part.** "Recurs across techniques" is necessary but not
sufficient for module membership; the field must also not already exist in the library under another
name. Applying condition 2 changed the answer four times:

| Candidate | Failure | Resolution |
|---|---|---|
| 15 fields recurring across 6 dating systems | 9 also occur outside geochronology | module shrank to 5; the 9 became `ReportingCore` |
| `Age Model and Software` | software half collided with `Data Reduction Software` (Rule 1) | narrowed to `Age Model` |
| 9 "general gaps" | 3 already covered by existing descriptions, 1 was a name-harmonization | 6 new fields, not 9 |
| `Pb*/Pbc` as a U-Pb extension | Ar-Ar's `%40Ar*` is the same quantity | promoted to Layer 2 as `Radiogenic Fraction of Measured Signal` |

The last is the most instructive: only building a *second* system module revealed that a field in the
first had over-claimed specificity. Expect the third and fourth system modules to do the same.

**Generalization:** Before adding any shared field, search the library by concept as well as by name and
read what you find. The default assumption should be that a plausible new shared field is already
present under a different name, or is an instance of something more general.

**Column ownership as the usability answer:** A Layer 2 field can carry an abstract name
(`Calibration Factor and Determination Method`) provided the consuming system module owns Column F. An
Ar-Ar geochronologist reads "the J value — give the fluence monitor, its assumed age and reference";
a U-Pb geochronologist reads "the EARTHTIME tracer, calibrated per Condon et al. (2015)". Same field,
same tiers, one place to query. The abstraction is a maintenance artifact, never user-facing. Splitting
such a field per system would destroy exactly the cross-system queryability that motivates it.

**Placement constraint discovered in build:** a module contributing to Group 5 must insert *before*
`Constants and Reference Values Used`, not append after it, or Rule 5 breaks.

---

### Known unresolved tier divergences (recorded, not decided)

Rule 4 step 4 requires that intentional or unresolved divergence be recorded here rather than
silently left in place. These two surfaced on 2026-08-08 during the Rule 1 naming harmonisation and
are deliberately left open.

**`Analysis Sequence` — three-way split across 10 TAPPs.**

| Tiers | TAPPs |
|---|---|
| C=Basic, D=Editable | 5 |
| C=Basic, D=Read-Only | 3 (the Solution ICP-MS TAPPs, formerly `Sample Sequence Design`) |
| C=Advanced, D=Editable | 2 (the geochronology TAPPs) |

The substantive question is D, not C: is the run order something the analyst may adjust within the
procedure's bracketing strategy (Editable), or does changing it constitute a different procedure
(Read-Only)? A defensible case exists either way — a bracketing interval is a procedure design
commitment, but the exact interleaving of a given session's samples is not. The C=Advanced pair is
almost certainly drift, consistent with Test 4's finding that 81% of that TAPP's tier differences
were drift rather than design.

Absent from 7 TAPPs (EPMA, SEM x4, TEM, Lab-XCT), where the sequence of standards and unknowns is
less formalised. Whether those need the field is a separate question.

**`Sample Persistent Identifier` — D split 14/3.**

C was resolved to Advanced across all 17 TAPPs on 2026-08-08, so a procedure may declare that it
expects samples to carry a persistent identifier — a meaningful standing commitment given Astromat,
EarthChem and SESAR. D remains split: D=Advanced in 14, D=Basic in the three Solution ICP-MS TAPPs.
The question is whether supplying an IGSN at analysis time should be mandatory. That is a policy
decision about how hard to push registration, not a technical one, and it was left open rather than
resolved by majority.

**Why these are recorded rather than fixed.** Both became visible only because the fields were
renamed to their canonical forms; before that they were the same field under two names, which no
check could detect. Renaming converts a hidden inconsistency into one `validate_tapp.py` reports as
`tier-divergence`. That is the intended end state for an undecided item: visible and tracked, not
resolved by whichever spelling happened to be more common.

---

#### 2026-08-11 audit — the remaining ten, and what they have in common

A full lint (`TAPP_Lint_Report_2026-08-11.csv`) after the Rule 7 retrofit reports **15**
`tier-divergence` findings across the 16-TAPP library. Five are already accounted for: the two above,
`Mass Resolution Setting` (recorded in its own entry, and the only one that should *not* converge), and
`EDS Detector Configuration` and `EDS Live Time per Point or Pixel`, both recorded as intentional under
"EDS architecture" above.

**The ten remaining divergences split along development-cohort lines, not technique-need lines.** Nine of
the ten separate either LA/geochronology from Solution ICP-MS, or EPMA/SEM from TEM — the exact groups in
which those TAPPs were developed. That is the signature of drift-by-cohort, each family having absorbed
its own tier instincts, rather than ten independent design decisions. It is the same diagnosis this
section already reaches for `Analysis Sequence`.

**A. Cohort drift — RESOLVED 2026-08-11, reconciled to the LA family tiers**

| Field | Was | Now | TAPPs changed |
|---|---|---|---|
| `Analytical Accuracy and Assessment Method` | C=Advanced (Solution) vs C=Basic (LA) | **C=Basic** everywhere | Solution MC, Q, SF |
| `Within-Session Analytical Precision and Assessment Method` | C=Advanced (Solution) vs C=Basic (LA) | **C=Basic** everywhere | Solution Q, SF |
| `Guard Electrode` | C=Advanced (Solution) vs C=Basic (LA) | **C=Basic** everywhere | Solution MC, Q, SF |
| `Dwell Time per Mass` | D=Read-Only (Solution) vs D=Editable (LA) | **D=Editable** everywhere | Solution Q, SF |

Ten tier cells across the three Solution ICP-MS TAPPs. **Reconciled toward LA rather than toward the
majority**, because the LA assignment is the one with an argument behind it: accuracy and within-session
precision are at least as central to solution ICP-MS as to laser ablation — solution work is the reference
method for concentration — so there was no basis for them being mandatory in one family and optional in
the other. The direction of travel was drift, not design.

Two fields changed in only two of the three Solution TAPPs: Solution MC-ICP-MS has no
`Dwell Time per Mass` (a multi-collector does not dwell on masses) and records within-session
reproducibility under the differently-named `In-Run Isotope Ratio Reproducibility and Assessment Method`,
which was left untouched. Whether that field should follow the same reconciliation is a separate question,
since it is a different field, not a divergent one.

Scope: Solution MC v7→v8, Solution Q v9→v10, Solution SF v9→v10 — integer bumps, tier changes being a
major structural revision. `tier-divergence` findings fell 15 → 11.

**B. Plausibly intentional — a technique argument exists, but it was never written down**

| Field | Split | The argument |
|---|---|---|
| `Sample Preparation Method` | D=Read-Only in Solution ×3 + TEM; D=Editable in the other 11 | Preparation is procedure-fixed where it is chemical and destructive (digestion, FIB foil) and adjustable where it is a mount that can be repolished or recoated |
| `Per-Analyte Calibration Strategy` | C=Advanced in Solution MC only; C=Basic in 8 | In single-element isotope work there is effectively one analyte, so a per-analyte strategy barely applies |
| `Phase Identification Method` | Lab-XCT C=Advanced/D=Editable; TEM C=Basic/D=Read-Only | In XCT it is an analysis-time segmentation choice; in TEM it is a procedure-level commitment to a diffraction or EDS approach |

**C. RESOLVED 2026-08-11**

| Field | Was | Now | Basis |
|---|---|---|---|
| `Detection Limit Method` | C=Advanced in all 12; D=Basic in 9, D=Editable in 3 | **C=Basic, D=Read-Only** in all 12 | C=Basic follows the `Uncertainty Level` precedent — a reported detection limit is not interpretable without knowing whether it is 3σ of background, Longerich et al. 1996, or 10× blank SD. D=Read-Only is what the field's own description already asserts: *"Must be consistent with the method applied to generate the Detection Limit values reported above."* Produces the Oxide Production pattern — method procedure-fixed, values a session outcome (`Detection Limit` stays C=Advanced/D=Basic) |
| `Step Size / Pixel Size` | EPMA C=Basic/D=Editable; SEM, SEM_Composition C=Advanced/D=Basic | **C=Basic, D=Editable** in all 3 | Reconciled to EPMA, which was already compliant with the existing precedent "Analysis-level only fields (C=N/A) for spatially determined mapping parameters". That entry rules step size C=Basic/D=Editable because it controls intrinsic spatial *resolution* — a procedure design choice — as opposed to map extent, which is dictated by the feature chosen at analysis time and is C=N/A |
| `EDS Acquisition Mode` | — | **unchanged** | Reclassified as intentional; recorded under "EDS architecture" above |

14 tier cells across 12 TAPPs. `tier-divergence` findings fell 11 → 9.

**Recorded, not decided — category B only.** Tier assignments are the library owner's call; the Rule 4
obligation discharged for those three is visibility. Categories A and C were both reconciled on
2026-08-11 (above), taking the library from 15 `tier-divergence` findings to 9 — of which 6 are now
recorded as intentional and 3 remain open by choice.


---

### `Technique` added to the controlled-list exemption table (2026-08-10)

**Decision.** `Technique` is exempt from the requirement that every `Controlled list` field offer
`N/A | None | Other: specify`. The exemption table in `conventions.md` — previously closed with a
single entry, `Analytical Mode` — now has two.

**Reasoning.** It is the same argument that exempted `Analytical Mode`, reached independently. The
field is the TAPP's own top-level technique identifier, drawn from the cross-TAPP technique
vocabulary under Rule 1. `N/A` and `None` are not merely unnecessary but semantically empty: every
procedure has a technique, and a procedure record declaring `Technique = None` would be malformed
rather than informative.

The three Solution ICP-MS TAPPs make the case concretely. Their Column F is a single value —
`Solution Q-ICP-MS`, `Solution SF-ICP-MS`, `Solution MC-ICP-MS` — a closed enumeration of one. There
is nothing an `N/A` option could usefully express there.

**What this does not extend to.** The exemption is for `Technique` itself, not for
`Coupled Technique(s)`, where `None` is meaningful and load-bearing: it is how a procedure records
that no coupling is intended, and the Group 1 standard depends on that value. Nor does it extend to
`Analytical Sub-mode`, `EDS Acquisition Mode` or `Beam Mode`, which the `Analytical Mode` entry
already excludes.

**Still open, and adjacent.** `Collision/Reaction Cell (CRC) Configuration` is arguably in the same
class. After its `Not applicable (SF-ICP-MS)` option was generalised to `N/A` on 2026-08-10, the
check still reports `None` as missing — but "no collision/reaction cell in use" is already
`STD (standard mode, no gas)` and "the instrument has no cell" is now `N/A`, so `None` would add a
third spelling of something already expressible. Not decided; it needs the same explicit call this
entry records for `Technique`.

**Scope of effect.** Clears 6 findings (`Technique` in LA-Q/SF v5 and its U-Pb variant, Lab-XCT v10,
and the three Solution TAPPs). No TAPP content changed — the exemption is a checker and convention
change only.

---

### Uncertainty Level split from Uncertainty Propagation Method (2026-08-10)

**Decision.** `Uncertainty Level and Propagation` is split into two fields across all 7 TAPPs that
carried it:

| Field | C | D | Data Type |
|---|---|---|---|
| `Uncertainty Level` | Basic | Read-Only | `Controlled list / Text` |
| `Uncertainty Propagation Method` | Advanced | Editable | `Text (free)` |

**This narrows the earlier precedent rather than reversing it.** The "Advanced/Editable" entry was
written when the field was named `Uncertainty Propagation Method` — propagation only — and its
argument is entirely about the propagation framework: many labs use informal uncertainty estimates
without a formally specified framework, so mandating one at Basic would exclude legitimate procedures
or generate boilerplate. That argument is sound and is preserved untouched on the propagation half,
which takes its original name back so the precedent applies to it by name again.

What the precedent never covered is the **level**. That concept was merged in by the 2026-08-08
rename to `Uncertainty Level and Propagation` and inherited C=Advanced by accident of packaging
rather than by argument. Nothing was ever written to justify treating the level as optional.

**Why the level is Basic.** `analysis/Test5_Geochronology_Module_CrossSystem.csv` row 3 records
"Uncertainty Level Convention" as REQUIRED in **6 of 6** independent community dating standards, with
recommended tiers C=Basic / D=Read-Only, and its status as "PARTIAL — folded into geochron
Uncertainty Level and Propagation". Unlike a propagation framework, there is no informal case to
exclude: every lab that reports an uncertainty quotes it at some level, and a value whose level is
unstated is not interpretable. The old description said as much itself — *"A reported uncertainty is
not interpretable without both halves"* — which is a description admitting it holds two fields.

**Why D=Read-Only does not hit the void-import trap.** The earlier entry's generalisation — that an
Advanced procedure-level field should almost never be Read-Only at analysis level, because Read-Only
imports a value that may be void — applies specifically when C=Advanced. A C=Basic field always
carries a procedure value for the analysis to inherit, and the level is a standing lab convention
rather than a session decision, so Read-Only is correct.

**Generalisation.** When a field's name contains "and", check whether the two halves warrant the same
tier. This one merged a component mandated by six community standards with a component deliberately
left optional, and the merge silently demoted the mandatory half to optional. A compound field name
is a reasonable place to look for a mis-tiered requirement.

**Scope.** 7 TAPPs, all integer-bumped because adding a field is a major structural revision:
LA-Q/SF v5→v6 (+U-Pb), LA-MC v2→v3, LA-MC U-Pb v1→v2, Solution Q v7→v8, Solution SF v7→v8,
Solution MC v5→v6. The field is in no module — at 2 fields it is below Rule 6.10's five-field
extraction threshold — so this was Rule 4 propagation.

**Literature assessment cells on the new field were left empty.** Existing extractions remain on the
propagation row where they were made. Several visibly contain level information ("2SE of individual
spot measurements reported"), so a Phase 3 re-pass could populate the new row, but copying them
wholesale would fabricate extraction never performed against this field.

---

### `Mass Resolution Setting` — D=Read-Only in LA-Q-ICP-MS, D=Editable everywhere else (2026-08-11)

**Decision:** an intentional cross-TAPP tier divergence, recorded here because `validate_tapp.py`
reports it as `tier-divergence` INFO and Rule 2/4 requires intentional divergences to be documented.

| TAPP | C | D |
|---|---|---|
| LA-Q-ICP-MS, LA-Q-ICP-MS U-Pb | Basic | **Read-Only** |
| LA-SF-ICP-MS, LA-SF-ICP-MS U-Pb, LA-MC-ICP-MS (+U-Pb) | Basic | Editable |
| Solution Q / SF / MC-ICP-MS | Basic | Read-Only |

**Reasoning.** On a quadrupole, mass resolution is fixed at unit resolution by instrument design — the
analyst cannot adjust it, so D=Editable would assert a session-tunable parameter that does not exist. On
a sector-field instrument the analyst genuinely selects low, medium or high resolution per session, which
is D=Editable by definition.

**Origin.** The divergence became visible only when the combined LA-Q/SF-ICP-MS TAPP was split on
2026-08-11. Before the split, one row had to serve both instruments and its Column F carried both answers
at once — *"Unit resolution — quadrupole (fixed) | Low resolution — SF (~300 m/Δm) …"* — with D=Editable,
which was correct for SF and wrong for Q. The field is the clearest single argument for having made the
split: a combined TAPP cannot carry two different tier assignments for one row.

**Not a candidate for reconciliation.** Unlike the divergences recorded under "Known unresolved tier
divergences", this one should not converge. The two values describe two different instruments and both
are correct.


---

### Technique-dependent key register (Rule 7.8.7) — the five entries and why

A field name normally carries the same `Keyed By` in every TAPP. These five are the ones where the
technique genuinely makes it differ. The register is a first-class list, not an escape hatch: uniformity
is the default because a field name that means one shape here and another shape there is invisible to a
curator — the same argument Rule 6.4 makes about descriptions.

**The default is justified empirically.** Of 252 field names appearing in more than one TAPP, **only 3
carry a differing key — 98.8% are already uniform.** The cross-TAPP check therefore costs almost nothing
and catches drift at the moment it is introduced, rather than at the next audit. The alternative
considered and rejected on 2026-08-11 was to make keys freely per-TAPP; that would have rebuilt, in a new
column, exactly the problem the tier-divergence audit had spent the same day untangling — 15 divergences
of which 6 were intentional and 9 were drift, and none recorded at the time it was introduced.

| Field | Keys | Why the technique makes it differ |
|---|---|---|
| `Detection Limit` | `sampling unit x reported property` in the 6 LA TAPPs; `reported property` elsewhere | Laser ablation yields a detection limit per spot, because each spot has its own background; solution work yields one per session |
| `Primary Calibration Standard Name` | `analyte` in EPMA/SEM/SEM_Composition; `(none)` in the 9 ICP-MS TAPPs | In WDS each analyte has its own calibration standard (albite for Na, Kakanui kaersutite for Si/Al/Ti); in isotope work one bracketing standard anchors the whole session |
| `Dwell Time per Pixel` | `analyte` in EPMA/SEM/SEM_Composition; `(none)` in SEM_FIBSEM/SEM_Imaging | Per element during compositional mapping; a single scan parameter in imaging-only procedures |
| `Beam Current` | `sampling unit` in EPMA/SEM/SEM_Composition; `(none)` in SEM_FIBSEM/SEM_Imaging | Added 2026-08-11 — see below |
| `Monitored Isotopes` | `defines: channel` in LA-Q, LA-SF (+U-Pb), Solution Q, Solution SF; `analyte` in LA-MC-ICP-MS (+U-Pb) | Where a collector array exists, the cup is the channel and `Collector Configuration` is the definer (7.4b), leaving `Monitored Isotopes` keyed by analyte. Single-collector instruments have no cup array, so it is itself the definer |

**`Beam Current` — the evidence, because the obvious answers were both wrong.** It was first keyed
`acquisition pass` on the reasoning that EPMA runs Na/K at low current and major elements at high. The
field's own description says *"Often varies by phase type or analyte"*, and the extracted literature
settles which dominates: three of five papers report a scalar (`5 nA`, `10 nA`), and the two that vary do
so **by phase** — Liu et al. 2016, both instruments: *"20 nA (olivine, pyroxene, Fe-Ti-Cr oxides); 10 nA
(maskelynite…)"*. No extraction reports a per-analyte current. Hence `sampling unit`, phase being a
sampling unit under 7.2, with `Sampling Unit` (Rule 9) already present in every TAPP as its definer.

The per-analyte case remains real and is documented in the field description. It was not adopted as the
key because the evidence does not support it as the dominant pattern, and `sampling unit x analyte` was
rejected as over-modelling — it would force a two-dimensional table on the majority of procedures that
need one number.

**Retiring `acquisition pass` followed.** Once `Beam Current` moved, its only remaining user was
`Multi-Run Sequential Analysis Design`, which would have had to be its own definer — a violation of 7.4c.
The key is documented in 7.2 but unused.
