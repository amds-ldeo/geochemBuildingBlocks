# Module consolidation — where this got to, and what's next

> **RESOLVED UPSTREAM, 2026-09-02** (delivery `af3f7bc`). Ruolin adopted the ICP-MS
> proposal. `Module_ICPMS` (39 fields, 9 consumers), `Module_CollisionCell` (8, 6) and
> `Module_CompositionQC` (6, 12) now exist in the library, and `Module_TargetSelection`
> became `Module_SamplingUnitSelection`. **Composition coverage went 25% → 73%**
> (651 composed against 231 still minted per technique, measured the same way as below).
> 456 sidecar rows that each technique used to place itself now come from a module.
>
> | | composed | own | |
> |---|--:|--:|--:|
> | Solution-MC-ICPMS | 65 | 0 | 100% |
> | LA-MC-ICPMS-UPb | 97 | 7 | 93% |
> | LA-Q-ICPMS / LA-MC-ICPMS / Solution-Q / LA-Q-UPb | | | 90% |
> | LA-SF ×2 / Solution-SF | | | 78–79% |
> | EMPA | 5 | 12 | 29% |
> | SEM family | | | 13–22% |
> | TEM | 5 | 40 | 11% |
> | XCT | 3 | 36 | 7% |
>
> The ICP-MS family is essentially done. The electron-beam and tomography families are
> untouched — our eight electron-beam drafts remain in `draft/`, and the floors measured
> for Lab-XCT and TEM below still stand. The six ICP-MS drafts have been deleted; eight of
> their fields were NOT adopted and are recorded in `docs/upstream-requests.md` §1.
>
> Two of the open questions below are now closed by the delivery rather than by us:
> `Secondary Reference Materials` moved into `Module_CompositionQC` after upstream
> harmonised the electron-beam three from `defines: standard per analyte` to
> `defines: standard` — the split we refused to average was removed at source; and the
> three cross-family fields went to `Module_CompositionQC` rather than the `Module_Blank`
> we proposed, which is the same call with a better home.
>
> Everything below is the state as of 2026-08-28 and is kept as the record of what was
> measured and asked for.

Working note, 2026-08-26. Records the measurements behind the module
drafts so they don't have to be re-derived, and says what is decided,
what is open, and what to do next.

Architecture is in `agents.md` §"Module composition". This is state, not
design.

## The finding, in one line

Module composition **works** — 242 parameters across the 16 technique
`tapp/` schemas are composed from a module. It is just **unevenly
applied**: 694 are still minted per technique, and the gap falls almost
entirely on the families that have no module.

## What was measured, and how

Run these to reproduce; nothing below is an estimate.

```bash
# composed vs minted, per technique  (the number that matters)
python - <<'EOF'
import re,glob,collections
T=collections.Counter()
for d in sorted(glob.glob('_sources/techniqueProfile/geochemProfile/*/tapp/schema.yaml')):
    s=open(d,encoding='utf-8').read()
    refs=len(re.findall(r'modules/[a-zA-Z]+/schema\.yaml#/\$defs/Param_', s))
    own=len(re.findall(r'ada:parameter/[a-zA-Z]+TAPP/', s))
    print(f"{d.split('/')[3]:22} {refs:3} composed  {own:3} own")
    T['r']+=refs; T['o']+=own
print(f"TOTAL {T['r']} composed / {T['o']} own = {T['r']*100//(T['r']+T['o'])}%")
EOF

# which modules each TAPP composes, and how many rows that covers
cd tools && python module_composition.py
```

**Result: 25% composed overall**, ranging from 39% (LA-MC-ICPMS-UPb) to
7% (Lab-XCT). Full table in `agents.md`.

### What this percentage is, and is not

It is **not** "the share of a technique's properties that come from a module". It counts
one specific thing: **parameter slots** — entries under `schema:additionalProperty`, each
either a `$ref` to a module's `Param_*` `$def` or a technique-minted
`ada:parameter/<TAPP>/<name>` identity. Read it as *"of the parameters the sixteen TAPP
schemas declare, what share is composed rather than minted per technique"*.

Three things it deliberately leaves out, and the direction each biases:

- **Top-level `ada:` properties** — a Basic-tier field is promoted to a direct property, not
  a parameter, so none of them is counted either way. EPMA declares nine; the metric sees none.
- **Module ROOT `$defs`** (`ProcedureIdentification` / `AnalysisIdentification`) — a module
  contributing a whole block of fields counts for nothing. EPMA composes one. **This makes the
  number an UNDER-statement of how much a module actually supplies.**
- **Keyed-table columns, instrument-tree placements, workflow steps, dqv measurements** —
  placed by path, not as parameters.

It also counts **occurrences, not distinct parameters** (a parameter's identity appears more
than once per definition): 651 occurrences over 331 distinct on the module side, 231 over 132
own. On distinct parameters the same state reads **71%** rather than 73% — close enough that
the headline is not distorted, but the two are not the same number.

**100% is not the target and is not reachable.** Of the 79 distinct fields no module covers,
**50 are technique-of-one** — a module needs two consumers, and TEM's EELS/diffraction fields
and XCT's reconstruction fields have no second carrier. Only **29** are carried by two or more
tables at identical structure. Nothing in the remainder is blocked by the composability rule
(`schema:additionalProperty`, keyed-table column arrays); every one is simply a field the
library has not modularised. The realistic ceiling is around 85%, and closing the gap is
upstream's call, not a pipeline change.

### A measurement trap, recorded so it isn't repeated

The first pass measured `_sources/registry/*`. Those catalogues are
`isTypeLibrary: true` and per-technique **by construction** — all 1,325
defs carry a TAPP identity, including fields whose technique *does*
compose the module. That yields "87% of defs are duplicated", which is
literally true and answers nothing. **Measure `tapp/`, not `registry/`.**

## Decided

- **`group1` is archived** (`archive/modules/`, 2026-08-26). Nothing
  composed it — zero `$ref`s. Removing its sidecar also settled a real
  ambiguity: `coupledProcedureDoi` and
  `coupledDatasetOrPublicationReference` were claimed by both `Core` and
  `Group1`, so no single module owned them. Both now resolve to `Core`.
- **Six items remain double-owned**, every one pairing a specific module
  with `ReportingCore`. That is the conditional-composition design
  (`module_composition.py`: "ReportingCore is conditional… a consumer
  composes only the blocks its manifest entry names"), **not** ambiguity.
  Left alone deliberately.
- **`calibrationFactorAndDeterminationMethod`'s 14 copies are correct.**
  The `variableMeasured` guard fires. Not a bug, do not "fix" it.

## Drafted, awaiting review

`docs/modules/draft/` now holds **14** `Draft_Module_*.csv`:

| family | modules | items |
|---|---|--:|
| ICP-MS (pre-existing) | ICPMSCore, CollisionReactionCell, SignalAcquisition, InterferenceHandling, CalibrationUncertainty, SampleSpecimen | 71 |
| Electron-beam (added 2026-08-26) | ElectronColumn, XraySpectrometry, XrayQuantification, SpectralInterference, ElectronImaging, EBSD, Cathodoluminescence, FIBTomography | 72 |

See `draft/README_ElectronBeam.md` for the electron-beam rationale and
method. **14 of the 72 carry a `NEEDS RECONCILING` flag** in `Comments`
— structure agrees, prose differs between tables, variants preserved
verbatim for Ruolin to choose.

## Decided 2026-08-26 (second pass)

**1. The four cross-family fields — resolved.** Three belong in an EXISTING
module, `Module_Blank`, whose 12 consumers are exactly their carrier set:
`Detection Limit`, `Detection Limit Method` and `Normalization /
Standards-Based Correction`. Measured across all 16 tables rather than
either family, each is carried by **12 of 16** with identical Procedure
tier, Analysis tier, Data Type and Keyed By. Removed from
`CalibrationUncertainty` (21 → 18) and `XrayQuantification` (17 → 14). A
`QuantificationQuality` draft was written first and withdrawn: measuring the
carrier set against the existing modules showed `Blank` already serves exactly
those 12 techniques, so a new module would have duplicated one in the library.
Placement is upstream's call under Rule 6.15 prong 2 — the measurement is ours,
the decision is not.

`Secondary Reference Materials` did **not** move. Its structure splits
exactly on the family boundary — `defines: standard per analyte` in the
three electron-beam tables, `defines: standard` in the nine ICP-MS ones —
and a field whose structure differs is refused, not averaged. It stays in
both family drafts with the difference recorded. It is also the field the
open `defines: standard per analyte` question turns on, so folding it into
a shared module would have buried a decision rather than made one.

**2. Lab-XCT cannot be modularised.** Of its 55 fields that no module
already owns, **2** appear in any other table and only **1** with identical
structure. A module needs at least two consumers to remove duplication, so
there is nothing to draft — tomography is simply a technique of one here.
The earlier note that it "needs its own module" assumed a tomography family
that does not exist. No draft was written.

**3. TEM needs no further module.** Re-measured against all 16 tables, not
just the electron-beam ones. TEM shares exactly **4** non-header fields at
identical structure, and all four are already drafted:

| field | draft | also in |
|---|---|---|
| Accelerating Voltage | `ElectronColumn` | EPMA, Lab-XCT, SEM ×4 |
| Electron Source | `ElectronColumn` | EPMA, SEM ×4 |
| EDS Dead Time | `XraySpectrometry` | EPMA, SEM, SEM_Composition |
| EDS Spectral Processing Type | `XraySpectrometry` | EPMA, SEM, SEM_Composition |

The open question was whether TEM duplicated anything *outside* SEM/EPMA.
It does not. Its remaining ~50 fields are TEM-only, so its 11% is a floor,
not a gap.

> **Measurement trap, second instance.** Comparing raw table rows makes the
> six section headers (`1. Procedure Identification`, `2. Samples`, …) look
> like fields shared by all 16 tables with identical structure — their tier
> and type cells are empty, so every table "agrees". Skip rows matching
> `^\d+\.\s`, as `load_rows` and `validate_application_grid` already do.

## The geochronology family — closed 2026-08-28

`Geochronology` (20 sidecar rows, 11 keyed) and `UPb` are complete and build.
`ArAr` does **not**, and that is correct, not a gap:

- nothing in `composed_tapps.json` composes it, so `build_module_bb` skips it
  and emits no building block
- there is **no Ar-Ar table** in `tapp/Current TAPPs/` for it to serve
- upstream `Module_ArAr.json` (v4, "40Ar/39Ar Geochronology") describes itself
  as built to test whether the J value maps onto a Calibration Factor field —
  a design probe, not a module with consumers

Our `docs/modules/Module_ArAr.schemapaths.csv` carries 4 hand-authored paths,
all placing cleanly. They are **inert until an Ar-Ar TAPP exists**, and that is
the finished state: the placements are ready, and nothing regenerates or
validates them because nothing composes the module. Do not re-open this as a
flagged-rows problem — the rows are placed; the module simply has no consumer.

Two things to know if an Ar-Ar table ever lands: the module builds with no
further work once `composed_tapps.json` names it, and its upstream notes still
reference `Module_ReportingCore`, which was dissolved on 2026-08-14 — so those
notes need re-reading against the five successor modules before they are trusted.

## Next step

Both remaining low-coverage techniques are now measured and neither is
actionable: Lab-XCT and TEM are at their floor. The consolidation question
is no longer "what else can be drafted" but **whether the 15 existing drafts
get adopted** — which is Ruolin's call, not ours (see below).

## Not to be confused

These drafts are **ours and provisional**. The library's modules are
Ruolin's to author (`docs/upstream-requests.md` §1). If he adopts a
draft, the real module arrives in a delivery and the draft is deleted.
