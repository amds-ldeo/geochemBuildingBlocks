# Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP)

Laboratory X-ray computed tomography (polychromatic cone-beam) extension of the base
[tappDefinition](../tappDefinition/) building block. Adds XCT protocol-level acquisition and
processing defaults as top-level `ada:` properties and a parameter vocabulary used in
`ada:methodParameters`.

## Structure

labxctTAPP composes via `allOf`:
- `$ref: ../tappDefinition/schema.yaml` — base TAPP shape (identity, workflow, instrument, location, …)
- ADA XCT overlay — adds XCT-specific top-level properties (`ada:voxelSizeDefault`,
  `ada:acceleratingVoltageDefault`, `ada:analyticalMode`, …) and the `ada:methodParameters` array
  whose entries reference the labxctTAPP parameter templates.

XCT produces 3D volumes rather than per-element analyte measurements, so **no `ada:analyteTemplate`
is defined** (unlike empaTAPP).

## Row → schema routing (from the Lab-XCT TAPP worksheet)

- **Protocol-Level Tier = Basic** → top-level `ada:` property (a `…Default` suffix marks values the
  analyst may override per dataset).
- **Protocol-Level Tier = Advanced** → `ada:methodParameters[]` template (`schema:PropertyValueSpecification`,
  `readonlyValue: true`) in the [parameterTemplates](../parameterTemplates/) registry.
- Identity rows (Protocol Name, Technique, Author, Laboratory, Start Date, Funding, Target Material,
  CT System Model, References, DOI) populate the **inherited** base-TAPP fields rather than new
  `ada:` properties.

## Supporting files

- `vocab/labxct_<name>.json` — `schema:DefinedTermSet` reference vocabularies (one per controlled list).
- `../parameterTemplates/schema.yaml#/$defs/labxct_<name>` — parameter templates referenced from
  `ada:methodParameters`.

## Dependencies

- [tappDefinition](../tappDefinition/) — base TAPP definition
- [parameterTemplates](../parameterTemplates/) — method-parameter template registry

## Source spec

Property/parameter definitions are generated from the **TAPP worksheet** of
`docs/Lab-XCT_TAPP_v8.xlsx` by `tools/build_labxct_from_spreadsheet.py`.
