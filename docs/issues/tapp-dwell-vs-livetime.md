# TAPP issue draft: three labels, two quantities — dwell time vs detector live time

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.

## The problem

Three workbook labels overlap, and one of them carries two different quantities:

| label | defs | what the Purpose text says |
|---|---|---|
| `Dwell Time per Pixel` | 9 | SEM/TEM: how long the **beam dwells** on a pixel. EPMA: "time spent **acquiring X-ray signal**… for EDS, **total live-time per spectrum per pixel**" |
| `EDS Live Time per Point or Pixel` | 5 | the detector's live time, as its own field |
| `4D-STEM Dwell Time per Probe Position` | 2 | per-probe-position dwell, referenced by name from `Dwell Time per Pixel`'s TEM text |

Beam dwell time and detector live time are not the same measurement — live time is
dead-time corrected, real time is not. So EPMA's reading of `Dwell Time per Pixel`
describes the quantity that `EDS Live Time per Point or Pixel` already owns, under a
different name.

Consequence: a consumer reading `Dwell Time per Pixel` across techniques gets beam
residence time from SEM and TEM and detector integration time from EPMA, with nothing
in the field to tell them apart.

## Options

1. **`Dwell Time per Pixel` means beam residence only.** Move EPMA's EDS live-time
   clause to `EDS Live Time per Point or Pixel`, which already exists. Smallest change;
   EPMA's WDS clause ("one value per spectrometer assignment per pixel") stays, since
   that *is* a dwell.
2. **Rename to disambiguate** — `Beam Dwell Time per Pixel` and `Detector Live Time per
   Pixel` — and retire the unqualified label. Clearest to a reader, but renames a field
   13 techniques already populate.
3. **Keep one label, add a qualifier column** saying which quantity a given technique
   reports. Avoids a rename, but puts the distinction somewhere a consumer must join to.
4. **Leave as is**, and document that the label is technique-dependent. Cheapest, and
   the option that keeps the ambiguity.

Option 1 is the recommendation: it uses a field that exists, touches one technique's
text, and needs no rename.

## Interim handling in geochemBuildingBlocks

The variable-registry prototype splits the label two ways pending this decision —
`ada:variable/beamDwellTimePerPixel` (SEM, semComposition, semFibsem, semImaging, TEM)
and `ada:variable/detectorLiveTimePerPixel` (EPMA) — recorded in
`docs/variable_registry_decisions.json`. Nothing is generated from it, so the interim
split costs nothing to revise.
