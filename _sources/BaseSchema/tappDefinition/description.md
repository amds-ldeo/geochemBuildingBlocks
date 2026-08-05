# Technique-Aligned Protocol Profile (TAPP) Definition v3

A registered TAPP definition modeled as a `cdi:Activity` + `schema:Action`. The TAPP itself is the activity; its standard workflow is encoded in `schema:actionProcess`.

## Changes from v2 (formerly "methodDefinition")

- **Renamed**: was "methodDefinition" (`ada:MethodDefinition`); now "tappDefinition" (`ada:TAPPDefinition`). Lives under `_sources/techniqueProtocols/`.
- **Root type**: `cdi:Activity` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol` (replaces `schema:HowTo` at root)
- **Target material**: `schema:object` carries the material(s) the TAPP analyses (e.g. silicate glass, olivine)
- **TAPP author**: `schema:agent` replaces `schema:creator`
- **Workflow**: `schema:actionProcess` holds a `schema:HowTo` with ordered `cdi:Activity` + `schema:Action` steps
- **Sample preparation**: now a workflow step, not a separate property
- **Parameters distributed**: step-specific parameters live on their workflow steps; only TAPP-wide parameters remain at top level

## Structure

### TAPP identity (top level)
- `schema:name`, `schema:identifier`, `schema:version`, `schema:datePublished`
- `schema:measurementTechnique` — DefinedTerm from controlled vocabulary
- `schema:object` — target material(s) as DefinedTerm or text
- `schema:instrument` — primary instrument with manufacturer, model, sub-components
- `bios:computationalTool` — software tools (TAPP-wide)
- `bios:reagent` — reference materials used across multiple steps
- `schema:location` — laboratory/facility
- `schema:agent` — TAPP author (person or organisation)

### Standard workflow (`schema:actionProcess`)
A `schema:HowTo` containing `schema:step` — an ordered array of `cdi:Activity` + `schema:Action` items. Typical steps:

1. **Sample preparation** (`bios:LabProcess`) — mounting, polishing, coating
2. **Instrument calibration** — primary/secondary standards, spectrometer setup
3. **Data acquisition** — beam conditions, per-element parameters (linked to `ada:analyteTemplate`)
4. **Data processing** — matrix correction, TDI, blank/normalization corrections
5. **Quality control** — drift monitoring, precision/accuracy assessment

Each workflow step can carry:
- `schema:additionalProperty` — typed step parameters (MethodParameter shape: scope, fieldScope, tier)
- `bios:reagent` — step-specific standards and materials
- `bios:computationalTool` — step-specific software
- `schema:instrument` — step-specific equipment
- `prov:used` / `schema:result` / `schema:object` — input/output chaining
- `schema:actionProcess` — nested sub-workflow
- `dqv:hasQualityMeasurement` — step-specific quality metrics

### Per-analyte parameters (`ada:analyteTemplate`)
Unchanged from v1/v2. Defines columns and default rows for the element table.

### Quality metrics (`dqv:hasQualityMeasurement`)
TAPP-level quality metrics using CDIF qualityMeasure building block. Step-specific metrics can also appear on workflow steps.

## Dependencies

- [instrument](../../geochemProperties/instrument/) — instrument specification
- [laboratory](../../geochemProperties/laboratory/) — laboratory/facility
- CDIF [definedTerm](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/) — technique, target material
- CDIF [identifier](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/identifier/) — TAPP DOI
- CDIF [person](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/person/) — TAPP author
- CDIF [labeledLink](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/labeledLink/) — TAPP references
- CDIF [monetaryGrant](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/monetaryGrant/) — funding
- CDIF [qualityMeasure](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/qualityProperties/qualityMeasure/) — quality metrics
- CDIF [bioschemasProperties](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/bioschemasProperties/cdifBioschemasProperties/) — Bioschemas vocabulary
- DDI-CDI [Activity](https://docs.ddialliance.org/DDI-CDI/1.0/model/FieldLevelDocumentation/DDICDILibrary/Classes/Process/Activity.html) — activity model
