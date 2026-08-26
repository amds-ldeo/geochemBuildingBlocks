# Module consolidation — where this got to, and what's next

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

## Open — needs a decision, not more analysis

1. **Four fields are cross-family and have two candidate homes.**
   Detection Limit, Detection Limit Method, Secondary Reference
   Materials, Normalization / Standards-Based Correction appear in the
   ICP-MS `CalibrationUncertainty` draft *and* in three electron-beam
   tables. Either `CalibrationUncertainty` becomes the shared home and
   `XrayQuantification` drops them, or they move to a neutral module both
   compose. They are currently in both drafts so the overlap is visible.

2. **Lab-XCT is still at 7%** and no draft addresses it. It shares
   exactly one field (`Accelerating Voltage`) with the electron-beam
   tables, so tomography needs its own module rather than a seat in
   these. **This is the obvious next drafting pass.**

3. **Solution and LA families have drafts but no adoption path.** The
   drafts measure what modularising would save; they do not modularise
   anything. Nothing changes until the library modules exist.

## Next step

Draft the missing modules for **Lab-XCT** (and re-check TEM, which sits
at 11% with 39 minted parameters — the electron-beam drafts cover only
what it shares with SEM/EPMA, and its own duplication with nothing else
was not examined).

Method is fixed and in `agents.md`; the electron-beam pass is the worked
example. Source tables are in the `tapp` submodule under
`tapp/Current TAPPs/`.

## Not to be confused

These drafts are **ours and provisional**. The library's modules are
Ruolin's to author (`docs/upstream-requests.md` §1). If he adopts a
draft, the real module arrives in a delivery and the draft is deleted.
