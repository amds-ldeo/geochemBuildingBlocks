# EMPA Technique-Aligned Protocol Profile (empaTAPP)

EMPA-specific extension of the base [tappDefinition](../tappDefinition/) building block. Adds top-level EPMA properties, a parameter vocabulary used in `ada:methodParameters`, and an analyte-column template used in `ada:analyteTemplate.ada:analyteColumns`.

## Structure

empaTAPP composes via `allOf`:
- `$ref: ../tappDefinition/schema.yaml` — base TAPP shape
- ADA EPMA overlay — adds EPMA-specific top-level properties (`ada:beamMode`, ...) and constrains where applicable

## Supporting files

The building block ships three sets of supporting JSON files that humans and tools reference when authoring empaTAPP instances. The schema does not currently `$ref` them as constraints; they are canonical reference data:

- `vocab/<name>.json` — `schema:DefinedTermSet` objects with `schema:hasDefinedTerm` arrays. Each is the canonical vocabulary for one EPMA enum.
- `parameters/<ParameterName>.json` — `schema:PropertyValueSpecification` template per parameter. Instances use these as `ada:methodParameters[]` entries.
- `analyteColumns/<columnName>.json` — `schema:PropertyValueSpecification` template per per-element analyte column. Instances use these as `ada:analyteTemplate.ada:analyteColumns[]` entries.

## POC scope (this version)

Three-row proof-of-concept covering one of each pattern:
- **Property** — `ada:beamMode` (top-level enum: Focused | Defocused | Raster)
- **Parameter** — `BeamRasterDimensions` (PropertyValueSpecification)
- **AnalyteColumn** — `monochromatorCrystal` (PropertyValueSpecification, references the monochromatorCrystal vocab)

The remaining ~60 rows from `docs/TAPP_EPMA_filled.xlsx` (TAPP worksheet) will be added once this POC pattern is approved.

## Dependencies

- [tappDefinition](../tappDefinition/) — base TAPP definition

## Source spec

Property/parameter/analyte-column definitions are derived from the **TAPP worksheet** of `docs/TAPP_EPMA_filled.xlsx`. The "implementation notes" column tags each row with one of `property`, `parameter`, `analyteColumn`, or a combination, plus `dataType` and `readOnly` flags.
