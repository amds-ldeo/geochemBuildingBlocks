# TAPP structure — a guide for generating JSON Schemas (v2)

**v2, 2026-08-13.** Merges Ruolin's `README_TAPP_for_Schema_Generation.md` (2026-08-11) — which
describes what is in the TAPP files and what will mislead you — with how the generator in this
repository actually consumes them. Where v1 suggested an approach and the implementation went a
different way, both are stated and the reason given: v1's advice is sound for a reader starting
fresh, and the divergences are where reality pushed back.

Sections 1–8 are the source format (largely v1, updated for the 2026-08-13 delivery). Sections
9–14 are the generation side. `Claude Skills for TAPP/references/conventions.md` remains
authoritative for the format itself.

---

## 1. The one thing to get right first

**A TAPP is not one schema. It describes two related objects.**

| Object | What it is | Registered/created when |
|---|---|---|
| **Procedure** | The standing set of guidelines specifying how a technique is applied at a lab. Registerable, citable, gets a DOI. | Once, then reused |
| **Analysis** | One execution of that procedure — one **session**, which may cover many samples. | Every time the procedure is run |

Every field row carries **two independent tier assignments**: Column C says what the field means at
procedure level, Column D what it means at analysis level. A row is not "required" or "optional" —
it is required-or-not *at each of two levels, differently*.

Producing a single flat object with one `required` array loses the distinction the whole framework
exists to express.

**This repository emits exactly two schemas per technique**, which is v1's recommendation realised:

| v1 calls it | here | root | file |
|---|---|---|---|
| procedure schema | `$MethodDefinition` | `prov:Plan` + `ada:TAPPDefinition` | `_sources/techniqueProfile/geochemProfile/<T>/tapp/schema.yaml` |
| analysis schema | `$Dataset` | `schema:Dataset` | `_sources/techniqueProfile/geochemProfile/<T>/detail/schema.yaml` |

Those two names are the roots of every schema path (§10), so a row states which object it lands on
before it says anything else.

**The analysis object is a session, not a sample — Rule 13, 2026-08-12.** One analysis record covers
every sample measured in one execution. Three fields are mandatory in every TAPP as a result:
`Session Identifier` (`(none)`), `Sample Name` (`defines: sample`) and `Sample Persistent
Identifier` (`sample`). Column I separates the levels: `(none)` at analysis level means *per
session*, `sample` means *per sample*, `sample > sampling unit` *per spot within a sample*.

---

## 2. Files and layout

16 TAPPs, one per technique or technique variant. **The CSV is the source of truth**; the xlsx is a
generated artifact and should not be parsed for content.

**The 2026-08-13 delivery changed the layout.** Tables now sit flat in `Current TAPPs/` — a
generated mirror holding the latest version of each, refreshed on every version bump under Rule 12.
Earlier versions stay in the per-technique folders (`EPMA/`, `SEM/`, …).

> **This broke a consumer.** `composed_tapps.json` still records per-technique paths
> (`EPMA/EPMA_TAPP_v20.csv`), so **0 of its 16 entries resolve** against the delivery as laid out.
> Our tooling now resolves manifest entries by filename. Either the manifest or the layout should
> move — see `docs/upstream-requests.md` §5.

| TAPP (current) | Modules composed | ReportingCore blocks |
|---|---|---|
| `EPMA_TAPP_v20.csv` | Group1, ReportingCore | `all` |
| `LA-MC-ICPMS_TAPP_v13.csv` | Group1, LaserAblation, MCICPMS, ReportingCore | `all` |
| `LA-MC-ICPMS_UPb_TAPP_v13.csv` | + Geochronology, UPb | `all` |
| `LA-Q-ICP-MS_TAPP_v15.csv` | Group1, LaserAblation, ReportingCore | `all` |
| `LA-Q-ICP-MS_UPb_TAPP_v16.csv` | + Geochronology, UPb | `all` |
| `LA-SF-ICP-MS_TAPP_v16.csv` | Group1, LaserAblation, ReportingCore | `all` |
| `LA-SF-ICP-MS_UPb_TAPP_v17.csv` | + Geochronology, UPb | `all` |
| `Lab-XCT_TAPP_v17.csv` | Group1, ReportingCore | `target_selection,calibration_factor` |
| `SEM_TAPP_v17.csv` | Group1, ReportingCore | `all` |
| `SEM_Composition_TAPP_v17.csv` | Group1, ReportingCore | `all` |
| `SEM_FIBSEM_TAPP_v11.csv` | Group1, ReportingCore | `target_selection` |
| `SEM_Imaging_TAPP_v11.csv` | Group1, ReportingCore | `target_selection` |
| `Solution_MC-ICP-MS_TAPP_v16.csv` | Group1, MCICPMS, ReportingCore, SolutionIntroduction | `calibration_factor,blank,aggregation,aggregation_qc` |
| `Solution_Q-ICP-MS_TAPP_v17.csv` | Group1, ReportingCore, SolutionIntroduction | `calibration_factor,blank,aggregation,aggregation_qc` |
| `Solution_SF-ICP-MS_TAPP_v18.csv` | Group1, ReportingCore, SolutionIntroduction | `calibration_factor,blank,aggregation,aggregation_qc` |
| `TEM_TAPP_v17.csv` | Group1, ReportingCore | `target_selection,calibration_factor,aggregation,aggregation_qc` |

**Version numbers move.** Resolve the current file by listing, or from `composed_tapps.json`. Never
hard-code filenames — and, as of this delivery, do not hard-code the *directory* either.

Encoding is UTF-8 with BOM (`utf-8-sig`). Content carries superscripts and Greek (`²⁰⁶Pb/²³⁸U`,
`δ⁵⁶Fe`, `J cm⁻²`) — preserve it. Write the BOM back: Excel needs it to read the file as UTF-8, and
omitting it turns that content into cp1252 mojibake on the next hand edit.

---

## 3. Column structure

Columns A–I are fixed. Everything after them is variable-width and must be located by header.

| Col | Header | Use in schema generation |
|---|---|---|
| A | `Metadata Item` | The field name. Here it is a **lookup key**, not a property name — see §10. |
| B | `Description` *or* `Description / Purpose` | → `description`. Often carries conditional rules — §7. |
| C | `Procedure-Level Tier` | Requiredness at procedure level. §5. |
| D | `Analysis-Level Tier` | Requiredness/mutability at analysis level. §5. |
| E | `Data Type` | → JSON type + format. §6. |
| F | `Example / Allowed Content` | Enumeration **or** examples — depends on Column E. §6. |
| G | `Comments` | Provenance labels only. Excluded. |
| H | `Last Update` | Provenance only. |
| I | `Keyed By` | **Cardinality.** §4. |
| J … | Mode flag columns | 0–11 of them. §8. |
| (after modes) | `Literature Assessment` | **Sentinel** marking the end of the mode block. |
| (after sentinel) | Literature columns | Evidence. **Not schema content.** |

**Parse A–I by position.** Columns B and F have two header spellings each; A–I are positionally
stable. Locate the mode block between `Keyed By` and the `Literature Assessment` sentinel — three
TAPPs (Solution Q, SF, MC) have **zero** mode columns.

> **A header rename cost us weeks, silently.** Column C changed from `Protocol-Level Tier` to
> `Procedure-Level Tier`. Our loader matched on `protocol` only, so the column read as empty: every
> row looked neither Basic nor Advanced, and the schemas quietly lost their required-branch
> constraints instead of failing. Accept both spellings, and treat a tier column that matches
> nothing as an error rather than a blank.

### Row types

1. **Group header** — Column A matches `^\d+\.\s`. Six per TAPP, always the same six in order:
   `1. Procedure Identification` · `2. Samples` · `3. Instrument & Software` ·
   `4. Measurement Information` · `5. Data Processing` · `6. Quality Control & Uncertainty`.
2. **Blank separator** — all of A–H empty. Skip.
3. **Content row** — everything else. One field.

---

## 4. `Keyed By` — the cardinality system (Column I)

**This determines schema shape and has no equivalent in an ordinary spreadsheet-to-schema
conversion.** It states what a field's value repeats over. Ignoring it produces a flat object where
roughly 20% of fields should be arrays of objects. Column I is never blank on a content row.

| Value | Meaning | Schema consequence |
|---|---|---|
| `(none)` | Scalar — per procedure, or **per session** at analysis level. 76% of fields. | Ordinary property |
| `sample` | Per sample covered by the session | Member of the `samples` array |
| `analyte` | Per chemical species determined — **the element or species, never the isotope** | Member of `analytes` |
| `channel` | Per instrument selection position (mass, cup, X-ray line, energy-loss edge) | Member of `channels` |
| `reported property` | Per reported quantity, ratios and dates alike, plus uncertainties | Member of `reportedProperties` |
| `sampling unit` | Per subdivision carrying its own row — grain, spot, aliquot, phase | Member of `samplingUnits` |
| `standard` | Per reference material or database entry | Member of `standards` |
| `preparation step` | Per sample-preparation stage | Member of `preparationSteps` |
| `defines: X` | **This field enumerates domain X** — the header of the child table, not a column in it | Populates the key set for `X` |
| `A x B` | Cross-product, **ordered**: "for each A, one value per B" | Array of objects nested one level |
| `A > B` | Containment — B exists only within A | Nested array |
| `A > B x C` | Containment then cross-product | One row: `sample > sampling unit x reported property` |
| `defines: A per B` | Enumerates A and carries a parent key into B — the channel↔analyte binding | Child array for A with a **nullable** FK to B |
| `pair: A` | Keyed by an unordered pair of A | `{"between": [...], "value": …}` |

**Separator is a literal ASCII `x`, not `×`.** Split on `\s+x\s+` (or `\s*[x>]\s*` for nesting).
Eighteen distinct strings library-wide; recount before relying on it.

### Invariants

- Every key used has **exactly one** field declaring `defines:` it.
- `Reported Variables and Units` and `Sampling Unit` are mandatory everywhere for their declarative
  purpose and may have no consumers.
- A field name normally carries the same key everywhere. **Five are technique-dependent by design**:
  `Detection Limit`, `Primary Calibration Standard Name`, `Dwell Time per Pixel`, `Beam Current`,
  `Monitored Isotopes`. Do not build one global field→key map.
- Where a TAPP declares both analyte and channel domains, the channel definer carries
  `defines: channel per analyte`. **The parent key is optional per row — model it nullable.**
  Interference monitors, internal standards and carriers are channels with no analyte.
- **Never infer domain membership from a child table.** Parsing `202Hg` into "Hg" records a
  determinand the procedure never determined.

### Implementation status

Three of the eight domains are built here — `analyte`, `channel`, `reported property` — each as a
keyed table: a column-definition template (`ada:analyteTemplate.ada:analyteColumns[]`) plus a
defaults array (`ada:defaultAnalytes[]`). The remaining five (`sample`, `sampling unit`, `standard`,
`preparation step`) and all the compound forms (`A x B`, `A > B`, `pair:`) are **not yet
implemented**; rows carrying them are flagged rather than guessed at.

**The schema can express the relationship; it cannot enumerate the members.** Which analytes exist
is content supplied when a procedure is registered.

---

## 5. Tiers — Columns C and D

**Column C — Procedure-Level:** `Basic` (mandatory to register) · `Advanced` (optional, recommended)
· `N/A` (analysis-level only).

**Column D — Analysis-Level:** `Read-Only` (inherited, immutable) · `Editable` (inherited,
adjustable within bounds) · `Basic` (**mandatory at analysis time**) · `Advanced` (optional at
analysis time). **`N/A` is not valid in Column D.**

### v1's requiredness table, and what the generator does with it

| C | D | Procedure schema | Analysis schema |
|---|---|---|---|
| `Basic` | `Read-Only` | required | required, immutable, inherited |
| `Basic` | `Editable` | required | required, inherited, may be overridden |
| `Basic` | `Basic` | required | required, supplied fresh |
| `Advanced` | any | optional | per D |
| `N/A` | `Basic` | **absent** | required, supplied fresh |
| `N/A` | `Advanced` | **absent** | optional, supplied fresh |

The generator adds one thing v1 leaves implicit — **where the value physically lives**:

| C | shape on the procedure |
|---|---|
| `Basic` | a direct `ada:` property, required |
| `Advanced` | a `schema:additionalProperty[]` entry, a `PropertyValueSpecification` |
| `N/A` | absent |

and **dual-homing**: four tier pairs put the field in *both* schemas — a default on the procedure
and a value on the analysis.

```
Advanced/Editable   Advanced/Advanced   Advanced/Basic   Basic/Editable
```

A dual-homed row therefore needs **two schema paths**, one per root. The procedure side takes the
`…Default` name or `schema:defaultValue`; the analysis side takes the bare name or `schema:value`.
**A `$Dataset` path never carries a `Default`** — the analysis records what was used, not what was
recommended.

Two structural guarantees hold: `Read-Only`/`Editable` always pair with `Basic`/`Advanced` at
procedure level, and `C=N/A` always pairs with `D=Basic`/`D=Advanced`.

---

## 6. Data types — Columns E and F

Column F's meaning **depends on Column E**.

| Column E | Column F contains | JSON |
|---|---|---|
| `Text (free)` | *Examples*, usually `e.g.,`-prefixed | `"type": "string"` — **never** an `enum` |
| `Controlled list` | *The enumeration*, pipe-separated | `"enum": [...]` |
| `Controlled list / Text` | Enumeration, unlisted values permitted | `anyOf: [enum, string]` |
| `Numeric (<unit>)` | Examples | `"type": "number"`, unit from the parentheses |
| `Numeric + unit` | Examples | Number **and** unit supplied by the user |
| `Integer` / `Boolean` / `Date` | — | `integer` / `boolean` / `string` + `format: date` |
| `URI / DOI`, `URI / IGSN` | Examples | string with format/pattern |
| `X / Text` | Structured with free-text fallback | `anyOf` |

- **Units are embedded in Column E**: extract with `^Numeric \((.+)\)$`. `Numeric + unit` means the
  unit is *not* fixed.
- **`N/A`, `None`, `Other: specify` are legitimate members**, not nulls. Open-world enum.
- Treating `Text (free)` pipes as an enumeration is the most common way to over-constrain. This
  generator puts them in `examples` instead, which keeps them visible without binding them.

---

## 7. Conditional applicability lives in Column B

No machine-readable conditional column. The condition is a sentence at the end of Column B, with
`N/A` offered in Column F:

> *"Record 'N/A' where EDS is not listed in Spectroscopic Detector(s)."*

Pattern: `Record 'N/A' where <Field Name> <condition>.`, referencing the governing field by its
exact Column A name. ~40 rows library-wide. Extractable into `if`/`then`, but the canonical
representation is simply that `N/A` is permitted.

---

## 8. Mode flags

Columns between `Keyed By` and the sentinel. Values **`Y` or `N` only**. `Y` means the field applies
to that mode. Mode sets are per-TAPP, 0–11 wide; Solution Q/SF/MC have none. Every TAPP carries
`Analytical Mode` declaring which modes a procedure executes. Modes are **not mutually exclusive**.

---

## 9. Modules → shared definitions

The TAPPs are **composed, not copied**. A field in several TAPPs is one definition, identical in
Columns A–E and I.

| Module | Fields | Consumers | Layer |
|---|---|---|---|
| `Group1` (Procedure Identification) | 18 | 16 | 2 |
| `ReportingCore` | 6 | 16 | 2 |
| `LaserAblation` | 18 | 6 | 2 |
| `SolutionIntroduction` | 16 | 3 | 2 |
| `MCICPMS` | 15 | 3 | 2 |
| `Geochronology` | 6 | 3 | 2 |
| `UPb` | 15 | 3 | 3 |
| `ArAr` | 16 | 0 (built, unconsumed) | 3 |

Module CSVs live in `Claude Skills for TAPP/modules/` — **authoritative**, over the copies under
`references/modules/`. Only columns A–F and I are meaningful: the module owns name, description,
tiers, data type and `Keyed By`; the consuming TAPP owns examples, comments, dates and mode flags.

**A module row with neither tier is an overlay, not an owned field.** `Module_UPb` has 15 rows but
only 3 with tiers; the other 12 supply U-Pb *examples* for fields `Geochronology` and
`ReportingCore` own. Treating them as owned invents 12 rival definitions.

**`ReportingCore` is conditional** — each of its five blocks carries an `applies_when`, and each
TAPP selects the blocks that apply. `Procedural Blank Level` is absent from TEM and Lab-XCT,
`Target Selection Criteria` from the three Solution TAPPs.

### Status here

Seven modules are built as OGC building blocks under `_sources/BaseSchema/modules/`, each with two
`$defs` split by root — `ProcedureIdentification` and `AnalysisIdentification` — because the
procedure and the analysis are separate documents. **They are not yet composed into the technique
schemas**; that wiring is the next step. `Group1` is hand-authored, the rest generated from their
own schema-path sidecars.

**Composition was checked before committing to it**: across 578 (module field × consuming table)
pairs where the table carries the field, tiers agree in **all 578** — no case where `allOf` would
tighten or loosen a technique's own requirement. `allOf` cannot relax a constraint, so this had to
be verified rather than assumed.

---

## 10. How this repository actually generates schemas

**This is the main divergence from v1.** v1 suggests slugifying `Metadata Item` into a property key.
That is a reasonable default and it is *not* what happens here.

A slugified key invents a new vocabulary term per field, and these schemas must interoperate with
schema.org, PROV, DDI-CDI and Bioschemas. `Laboratory` is not a new property — it is
`schema:location` on a `schema:Place`. `Analysis Start Date` is `prov:wasGeneratedBy.schema:startDate`.

So every field is mapped, by hand, to a **canonical schema path** in an existing vocabulary, and
those mappings live in a **sidecar CSV**, one row per (item → path):

```
TAPPS20260813/Current TAPPs/EPMA_TAPP_v20.csv    ← Ruolin's table, read-only to us
docs/EPMA_TAPP_v20.schemapaths.csv               ← our placement
docs/modules/Module_Group1.schemapaths.csv       ← module placements, shared by every consumer
```

Sidecars sit in `docs/`, not beside their tables. They were briefly co-located, which reads well
until you notice it puts our hand-authored mapping inside somebody else's tree — the boundary
`.github/CODEOWNERS` draws. `schemapath_io.csv_path()` resolves on the source's **basename**, so a
table can move (2026-08-13 flattened them all into `Current TAPPs/`) without moving its sidecar.

Columns: `Metadata Item | Protocol Tier | Analysis Tier | Data Type | Schema Path | Source | Scope | Notes`.
`Metadata Item` is the join key back to the table, which is why it must match the table exactly.
`Source` records provenance — `authored` (human-set), `inferred` (bootstrap guess), `flagged` (needs
a path).

A path names its root, then navigates:

```
$MethodDefinition.ada:acceleratingVoltageDefault
$MethodDefinition.schema:instrument[schema:additionalType='EPMA'].schema:model.schema:name
$Dataset.prov:wasGeneratedBy.schema:additionalProperty[schema:name='Drift Correction'].schema:value
$Dataset.dqv:hasQualityMeasurement[dqv:isMeasurementOf='Goodness-of-Fit'].dqv:value
```

**45 grammar families** are recognised (`tools/normalize_schema_paths.py`). Anything unrecognised is
reported, never guessed. Current state: **1406 technique paths + 105 module paths, 0 unrecognised,
102 rows still flagged**, 12 TAPPs generating and validating GREEN.

Two distinctions that are easy to miss and cost real debugging here:

- **An UpperCamel segment asserts `@type`; it does not navigate a property.** `ada:ReportedDateType`
  parsed as a type and emitted *nothing*, while passing every check. Property segments are
  lowerCamel; the grammar now rejects the other spelling rather than silently dropping it.
- **`$Dataset.schema:additionalProperty[…]` and
  `$Dataset.prov:wasGeneratedBy.schema:additionalProperty[…]` mean different things.** The first is
  a property of the *delivered data* (map area, volume dimensions); the second is a parameter of the
  *session* (how the instrument was set). One session can yield products of differing extent, so
  both spellings are legal and neither auto-corrects to the other.

---

## 11. Round-tripping a new delivery

The two sides never edit the same file — Ruolin owns the tables and modules, we own the sidecars and
everything generated (`.github/CODEOWNERS`). So the risk is not merge conflicts but **drift**: a
rename upstream invalidates sidecar rows keyed on `Metadata Item`, and it fails *quietly*.

```bash
python tools/intake_delivery.py TAPPS<date>      # read-only report
```

1. **Land the drop untouched** — new dated folder, one commit, nothing of ours in it.
2. **Report before changing anything** — what would carry, rename, be **dropped**, or arrive flagged;
   what composing a module would change; which paths no longer resolve.
3. **Read `DROPPED` closely.** An item that looks deleted is usually renamed beyond the mechanical
   rules, and its authored paths go with it. Confirm against the new table's own Description, then
   record it in `migrate_sidecar.ALIASES`. Six such renames have been confirmed so far, including a
   2→1 merge.
4. **Apply**: `migrate_sidecar --write` per technique, carry `overrides.json` forward by hand,
   re-seed the module sidecars, then re-point `TAPP_CONFIGS` (two strings per technique).
5. **Rebuild, validate, commit in three** — import, sidecars, regeneration.

The 2026-08-13 intake carried **524 items with 0 dropped** across eight techniques this way.

---

## 12. Gotchas

Ruolin's ten, still true:

1. **Don't parse the xlsx.** Generated from the CSV.
2. **Column G is provenance only** — 27 rows in the U-Pb variants, blank everywhere else.
3. **Don't hard-code column indices past I.** Find `Literature Assessment`.
4. **Three TAPPs have no mode columns.**
5. **Match A–I by position** — B and F have two spellings each.
6. **Literature columns are evidence, not schema.**
7. **`N/A` and `None` are values.** Do not coerce to `null`.
8. **No global field-name → type map.** Five fields are technique-dependent.
9. **Superscripts and Greek matter.** Do not normalise `²⁰⁶Pb/²³⁸U`.
10. **Filenames carry versions that move.** Resolve via `composed_tapps.json` — and now the
    directory moves too.

And five learned generating from them:

11. **Accept both `Procedure-Level` and `Protocol-Level`.** A missed tier column is silent.
12. **Write the BOM back.** Excel needs it; without it the Greek returns as mojibake.
13. **A clean "0 unrecognised" is necessary, not sufficient.** A path can satisfy the grammar and
    still emit nothing — confirm newly authored paths actually produce a property.
14. **Never let a re-run replace an existing path with a flag**, or overwrite a hand-placed path
    with a derived one. Compare content, not the `Source` label: labels go stale the moment a path
    is edited and the metadata is not.
15. **Skipping is not passing.** A resolver that finds no file, or a check that skips an unmatched
    field, reports a clean zero for work it never did. Both have happened here; both now report.

---

## 13. Open questions with the library

Tracked in `docs/upstream-requests.md`, summarised:

1. **83 shared LA fields have no module.** The six LA tables hold 115 fields common to all six; the
   modules cover 42. Generating those six TAPPs before the gap closes means authoring six
   near-identical sets of ~230 placements. Six candidate modules are proposed.
2. **`Module_UPb`'s 12 tier-less rows** — read as example overlays; confirmation wanted.
3. **`ReportingCore` declares six fields that seven tables lack** — 18 pairs. Composing adds them,
   and two are Basic, so they become requirements those tables never stated.
4. **`Error Correlation Between Reported Quantities`** belongs to no module.
5. **Delivery mechanics** — the manifest's paths do not match the layout; modules ship in three
   places.

---

## 14. Validating your understanding

In the library:

- `Claude Skills for TAPP/scripts/validate_tapp.py` — every structural invariant as executable
  checks; the best single reference for a well-formed TAPP. Baseline 0 ERROR, 0 WARN.
- `compose_tapp.py` — how modules are built in, including column ownership.
- `references/conventions.md` — the specification, Rules 1–13.
- `references/precedents.md` — why specific decisions were made.
- `Decision_Record_2026-08-12_Session_Sample_and_Analyte.md` — the session/sample split and the
  `analyte` definition.

On this side:

- `tools/intake_delivery.py` — what a new delivery would change. Read-only.
- `tools/module_conflict_check.py` — what composing a module would do to its consumers.
- `tools/normalize_schema_paths.py` — the 45 path families, each with the reason it exists.
- `docs/SCHEMA_PATH_GRAMMAR.md`, `docs/KEYED_BY_GRAMMAR.md` — the path and cardinality grammars.

A good first sanity check remains v1's: parse one TAPP, count content rows, confirm the number
matches `validate_tapp.py`. If your parser counts group headers or separators as fields, that
surfaces immediately.
