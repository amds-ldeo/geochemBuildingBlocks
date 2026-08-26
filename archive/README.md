# archive/

Superseded material, kept rather than deleted so a decision can be read
back later. Nothing here is built, validated, or referenced by anything
in `_sources/` or `docs/` — if something still `$ref`s it, it does not
belong here yet.

| what | retired | why |
|---|---|---|
| `modules/group1/` | 2026-08-26 | The hand-written pilot module, superseded by the generated ones. Nothing composed it: zero `$ref`s from any `_sources/**/schema.yaml`. |
| `modules/Module_Group1.schemapaths.csv` | 2026-08-26 | Source sidecar for the above. Also the cause of a double-membership ambiguity — `coupledProcedureDoi` and `coupledDatasetOrPublicationReference` resolved to both `Core` and `Group1`, so no single module owned them. |
| `SEM_TAPP_v4.xlsx`, `SEM_TAPP_v4.schemapaths.csv` | earlier | Superseded SEM delivery. |
| `new_tapps202606/` | earlier | Superseded delivery intake. |
| `techniqueProfile/` | earlier | Superseded profile drafts. |

## On group1 specifically

`Group1` predates the module generator — `build_module_bb.py` calls it
"hand-written as the pilot, before this generator existed". Several
tool comments still cite it as the worked example of a thin module, and
`build_module_bb.DIRNAME` still carries its `"Group1": "group1"` entry.
Those are inert once the sidecar is gone (no CSV, no module built) and
are left alone rather than chased, since the comments still describe
real history accurately.
