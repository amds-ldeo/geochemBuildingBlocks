# Target-Material-Column Specification Registry

One `$def` per column of a technique's per-target-material table. A column exists because some
TAPP field's `Keyed By` cell names `target material`, meaning its value repeats over the material
types the procedure is designed to analyse rather than being a single value for the procedure.

The target-material domain has the same three parts as the other keyed domains
(`ada:targetMaterialTemplate` holding `ada:targetMaterialColumns[]` and
`ada:defaultTargetMaterials[]`, with a mandatory `targetMaterial` identifier column), so a field
keyed by the domain is a COLUMN and the `defines: target material` field is the ROW axis.

Generated: `python tools/build_pathdriven.py <TAPP>` publishes each technique's columns here by
upsert on `@id`. Do not hand-edit.
