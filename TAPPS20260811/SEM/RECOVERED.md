# Two CSVs in this folder are recovered, not authored

`SEM_TAPP_v10.csv` and `SEM_Composition_TAPP_v10.csv` were **generated from their xlsx** by
`Claude Skills for TAPP/scripts/xlsx_to_tapp_csv.py` on 2026-08-11. Every other TAPP CSV in this
delivery came from upstream; these two did not exist there in CSV form.

The rest of the library treats the CSV as the source of truth and the xlsx as a generated
artifact. **For these two that relationship is inverted** — the xlsx is what was delivered, and the
CSV is derived from it.

## Why this is safe to read

Recovery is lossless for content. Colour in the xlsx re-encodes the tier already present in
Columns C/D, and the Legends sheet is documentation, so nothing schema-relevant lives only in the
spreadsheet. Two checks back this up:

- **Round-trip.** Running the tool against `EPMA_TAPP_v13.xlsx`, which *does* have an authored CSV,
  reproduces it with 0 cell differences across 97 rows x 29 columns.
- **Their validator.** `validate_tapp.py --root .` reports 16 files, 0 ERROR, 0 WARN, 9 INFO —
  identical to the 14-file baseline. Adding these two introduced no new findings, and the
  cross-TAPP checks compare fields between files, so malformed content would have shown up.

Encoding matches the library: UTF-8 with BOM, CRLF, superscripts and Greek preserved.

## Why it still matters

A recovered file is not authoritative. If Ruolin edits the upstream source, these will not follow,
and nothing here will make that visible. Two consequences:

- **Do not edit these CSVs.** Under Rule 6.6 a composed TAPP is a build output anyway; edit the
  module or the source and recompose.
- **Replace, do not merge.** If the real CSVs appear upstream, overwrite these outright and delete
  this note.

`SEM_TAPP_v10` is the combined SEM TAPP (11 modes, 118 content rows) — the superset of
`SEM_Imaging_TAPP_v9`, `SEM_Composition_TAPP_v10` and `SEM_FIBSEM_TAPP_v9`, all four of which the
library maintains in parallel.
