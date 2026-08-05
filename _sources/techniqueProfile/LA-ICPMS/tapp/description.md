# LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP)

LA-ICPMS-specific extension of the base [tappDefinition](../tappDefinition/) building block. Adds top-level laser-ablation properties, a parameter vocabulary used in `ada:methodParameters`, and an analyte-column template used in `ada:analyteTemplate.ada:analyteColumns`.

## Structure

laicpmsTAPP composes via `allOf`:
- `$ref: ../tappDefinition/schema.yaml` — base TAPP shape
- ADA LA-ICPMS overlay — adds laser-ablation top-level properties (`ada:spotGeometryDefault`, `ada:ablationMode`, `ada:laserFluenceDefault`, `ada:AblationSpotDuration`, ...) and the analyte-column template

## Analysis modes

The TAPP captures three LA-ICPMS analysis modes, each with its own worked example:
- **Spot** — discrete single-spot ablation
- **Transect** — line-scan / continuous-traverse ablation
- **Mapping** — 2-D raster mapping

## Supporting files

The building block references shared catalog JSON files that humans and tools use when authoring laicpmsTAPP instances:

- `../vocab/<name>.json` — `schema:DefinedTermSet` objects with `schema:hasDefinedTerm` arrays; the canonical vocabulary for each enum.
- `../parameterTemplates/<ParameterName>.json` — `schema:PropertyValueSpecification` template per parameter. Instances use these as `ada:methodParameters[]` entries.
- `../analyteColumns/<columnName>.json` — `schema:PropertyValueSpecification` template per per-element analyte column. Instances use these as `ada:analyteTemplate.ada:analyteColumns[]` entries.

## Dependencies

- [tappDefinition](../tappDefinition/) — base TAPP definition

## Source spec

Property/parameter/analyte-column definitions are derived from the **TAPP worksheet** of `docs/TAPP_LAICPMS_filled.xlsx` (reshaped from `LA-ICPMS_TAPP_v8.xlsx`). The "implementation notes" column tags each row with one of `property`, `parameter`, `analyteColumn`, or a combination, plus `dataType` and `readOnly` flags. The Spot / Transect / Mapping columns supply the per-mode example values.
