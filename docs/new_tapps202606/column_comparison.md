# New TAPP worksheets — column comparison (2026-06)

Source: Google Drive `TAPPs/` shared folder (synced locally via the `TAPPs.lnk` shortcut →
`G:\.shortcut-targets-by-id\1GIX3tb3VB2cRtroSIlNBXPHVI-OVhGXw\TAPPs`). 9 workbooks, each a single
`TAPP` sheet (+ `Legends`). Header is **row 1**. Per instruction, only columns from A through the
**`Literature Assessment`** separator are schema-relevant; everything to its right is
publication/literature-specific and ignored.

These workbooks do **not** carry the `[schema path, matchComment, implementation notes]` guidance
columns that the two already-implemented references (`LA-ICPMS_TAPP_v8`, `TAPP_EPMA_filled-noInterp`)
have.

## A. Schema-defining (structural) columns — present in ALL 9

| worksheet | Metadata Item | Description / Purpose | Protocol-Level Tier | Analysis-Level Tier | Data Type | Example / Allowed Content | Comments | Last Update | Literature Assessment |
|---|---|---|---|---|---|---|---|---|---|
| EPMA_TAPP_v6 | X | X | X | X | X | X | X | X | X |
| EPMA_TAPP_v7 | X | X | X | X | X | X | X | X | X |
| LA-Q_SF-ICPMS_TAPP_v2 | X | X | X | X | X | X | X | X | X |
| SEM_Composition_TAPP_v4 | X | X | X | X | X | X | X | X | X |
| SEM_FIBSEM_TAPP_v4 | X | X | X | X | X | X | X | X | X |
| SEM_Imaging_TAPP_v4 | X | X | X | X | X | X | X | X | X |
| SEM_TAPP_v4 | X | X | X | X | X | X | X | X | X |
| TEM_TAPP_v7 | X | X | X | X | X | X | X | X | X |
| Lab-XCT_TAPP_v8 | X | X | X | X | X | X | X | X | X |

**The 8 schema-defining columns are identical across all 9 worksheets** (Literature Assessment is the
right-edge separator). This is the same A–F + Comments/Last-Update block the existing parser
(`tools/_tapp_lib.py`, `COL` map) consumes — minus the guidance columns G–J.

### Label variants (cosmetic only — normalized above)
- `Description` (LA-Q_SF-ICPMS, Lab-XCT) vs `Description / Purpose` (other 7) — same column.
- `Example/Allowed Content` (LA-Q_SF-ICPMS) vs `Example / Allowed Content` (other 8) — spacing.

These should be normalized in the parser (or the sheets) before generation.

## B. Technique-mode columns (between `Last Update` and `Literature Assessment`)

These are per-acquisition-mode applicability flags (Y/N per variable row) — **technique-specific, not
schema-defining**. They vary by instrument family and define which modes each protocol supports.

| worksheet | EDS Point Analysis | EDS Mapping | WDS Point Analysis | WDS Mapping | Spot | Transect | Mapping | TEM Sample Preparation | 3D Tomography | SE Imaging | BSE Imaging | CL Point Analysis | CL Mapping | EBSD | TEM Imaging | STEM Imaging | Electron Diffraction | Single-volume | Multi-volume stitching |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EPMA_TAPP_v6 | X | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPMA_TAPP_v7 | X | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LA-Q_SF-ICPMS_TAPP_v2 |  |  |  |  | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |
| SEM_Composition_TAPP_v4 | X | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SEM_FIBSEM_TAPP_v4 |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |  |
| SEM_Imaging_TAPP_v4 |  |  |  |  |  |  |  |  |  | X | X | X | X | X |  |  |  |  |  |
| SEM_TAPP_v4 | X | X | X | X |  |  |  | X | X | X | X | X | X | X |  |  |  |  |  |
| TEM_TAPP_v7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X | X |  |  |
| Lab-XCT_TAPP_v8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |

Note: `SEM_TAPP_v4` is the superset; `SEM_Composition` / `SEM_FIBSEM` / `SEM_Imaging` are mode-subset
splits of it. `EPMA_TAPP_v6` and `v7` are identical in column structure (content may differ).

## Workbook → method inventory

| method | workbook(s) |
|---|---|
| EPMA | EPMA_TAPP_v6, EPMA_TAPP_v7 (v7 newest) |
| SEM  | SEM_TAPP_v4 (full) + splits: SEM_Composition_v4, SEM_FIBSEM_v4, SEM_Imaging_v4 |
| TEM  | TEM_TAPP_v7 |
| LA-(Q/SF)-ICP-MS | LA-Q_SF-ICPMS_TAPP_v2 |
| Lab-XCT | Lab-XCT_TAPP_v8 |
