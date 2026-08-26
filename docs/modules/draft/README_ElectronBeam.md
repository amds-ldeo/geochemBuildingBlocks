# Draft modules for the electron-beam techniques

Eight proposed modules covering 72 fields that the electron-beam TAPP
tables currently define once per technique. For review by Ruolin — these
are drafts on our side, not library modules; the real ones are his to
author (see `docs/upstream-requests.md` §1).

Companion to the six ICP-MS drafts already in this directory. Same
format, same method, different family.

## Why these, and why now

Module composition already works. Measured across the 16 technique
`tapp/` schemas, 242 parameters are composed from modules and 694 are
minted per technique — but the coverage is uneven, and it tracks exactly
which modules exist:

| technique | composed | own | shared |
|---|--:|--:|--:|
| LA-MC-ICPMS-UPb | 44 | 67 | 39% |
| Solution-MC-ICPMS | 25 | 44 | 36% |
| LA-MC-ICPMS | 30 | 67 | 30% |
| EPMA | 5 | 14 | 26% |
| SEM | 4 | 27 | 12% |
| TEM | 5 | 39 | 11% |
| Lab-XCT | 3 | 36 | **7%** |

`LaserAblation`, `MCICPMS` and `SolutionIntroduction` exist; nothing
equivalent covers electron-beam or tomography. The six existing drafts
are also ICP-MS-shaped, so adopting them alone would widen the gap.

## Method

The same rule the LA drafts followed (`tools/draft_module.py`):
**definitions come from the tables, not from us.** A field is a candidate
only if it

1. appears in more than one electron-beam table,
2. carries **identical structure** across them — Procedure tier, Analysis
   tier, Data Type and Keyed By — and
3. is not already owned by an existing `Module_*.schemapaths.csv`.

Of 120 fields shared by more than one table, 109 are structurally
consistent, and 72 of those are not already module-owned. **Eleven were
refused** because their structure genuinely differs between tables;
those stay per-technique.

Where the prose differs but the structure does not, the **majority
wording** is used and every variant is preserved verbatim in the
`Comments` column, marked `NEEDS RECONCILING`. 14 of the 72 are in that
state. Nothing was averaged or invented.

That flag matters: `Accelerating Voltage` is shared by all seven tables,
but Lab-XCT describes it as *"X-ray tube accelerating voltage"* where the
electron-beam tables say *"Electron beam accelerating voltage"*. Same
quantity, different instrument vernacular — a reconciliation, not a
reason to split the field.

## The eight modules

| module | items | reconcile | covers |
|---|--:|--:|---|
| `ElectronColumn` | 9 | 4 | beam and column conditions every EB technique sets — accelerating voltage, electron source, working distance, chamber pressure |
| `XraySpectrometry` | 14 | 2 | WDS and EDS acquisition — crystals, spectrometer channels, counting times, dead time, PHA |
| `XrayQuantification` | 17 | 6 | turning X-ray intensity into composition — matrix correction, MACs, drift, detection limits, precision and accuracy |
| `SpectralInterference` | 3 | 2 | X-ray line overlap and its correction |
| `ElectronImaging` | 3 | 0 | SE/BSE detector type and image pixel size |
| `EBSD` | 9 | 0 | electron backscatter diffraction acquisition and indexing |
| `Cathodoluminescence` | 6 | 0 | CL detector, grating, wavelength range and calibration |
| `FIBTomography` | 11 | 0 | FIB-SEM serial sectioning — milling, lift-out, slice thickness, voxel size, registration |

## Two things worth deciding before adoption

**`XrayQuantification` overlaps `CalibrationUncertainty`.** Four fields
— Detection Limit, Detection Limit Method, Secondary Reference
Materials, Normalization / Standards-Based Correction — are in the
existing ICP-MS draft *and* in three electron-beam tables. They are
cross-family, not ICP-MS-specific. Either `CalibrationUncertainty`
becomes the shared home and `XrayQuantification` drops them, or they move
to a neutral module both compose. We have not chosen; they appear here so
the overlap is visible rather than silently duplicated a second time.

**Interference is not one concept across families.** The existing
`InterferenceHandling` draft covers isobaric and molecular overlap in
mass spectrometry. `SpectralInterference` here covers X-ray line overlap.
The names rhyme and the physics does not, so they are kept separate
deliberately.

## Not addressed

Lab-XCT contributes one field (`Accelerating Voltage`) and stays at 7%
composed. Tomography shares almost nothing with the electron-beam
tables, so it needs its own module rather than a place in these — worth a
separate pass.
