# Technique-Aligned Protocol Profile (TAPP) Definition v3

A registered TAPP definition modeled as a plan: `prov:Plan` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol` + `schema:HowTo`. Its standard workflow is encoded in `schema:actionProcess`. An analysis event links the TAPP it followed with `schema:actionProcess {"@id": <tapp>}`, or with `schema:isBasedOn` on its own inline workflow; `schema:HowTo` is what makes the TAPP a valid value there.

## Changes 2026-11-11 (the CDIF activity-used-resources change)

- **Root type**: `schema:HowTo` added, `cdi:Activity` dropped (no TAPP carries a DDI-CDI process property, and in DDI-CDI the class names a run, not a plan).
- **Resources**: the instruments, computational tools and reagents a plan prescribes are all items of `schema:instrument` — always an array — told apart by the Wikidata kind term in `schema:additionalType` (`https://www.wikidata.org/entity/Q3099911` instrument, `…/Q7397` software, `…/Q2356542` reagent), which selects the shape (`$defs/PlanResource`). The direct `bios:computationalTool` / `bios:reagent` properties are closed off.
- **Steps**: typed `schema:Action` + `schema:HowToStep`; their tools and reagents are `schema:instrument` items too, and their inputs are `schema:object` (was `prov:used`).

## Changes from v2 (formerly "methodDefinition")

- **Renamed**: was "methodDefinition" (`ada:MethodDefinition`); now "tappDefinition" (`ada:TAPPDefinition`). Lives under `_sources/techniqueProtocols/`.
- **Root type**: `cdi:Activity` + `schema:Action` + `ada:TAPPDefinition` + `bios:LabProtocol` (replaced `schema:HowTo` at root; `schema:HowTo` came back, and `cdi:Activity` went, on 2026-11-11)
- **Target material**: `schema:object` carries the material(s) the TAPP analyses (e.g. silicate glass, olivine)
- **TAPP author**: `schema:agent` replaces `schema:creator`
- **Workflow**: `schema:actionProcess` holds a `schema:HowTo` with ordered steps
- **Sample preparation**: now a workflow step, not a separate property
- **Parameters distributed**: step-specific parameters live on their workflow steps; only TAPP-wide parameters remain at top level

## Structure

### TAPP identity (top level)
- `schema:name`, `schema:identifier`, `schema:version`, `schema:datePublished`
- `schema:measurementTechnique` — DefinedTerm from controlled vocabulary
- `schema:object` — target material(s) as DefinedTerm or text
- `schema:instrument` — the instruments (with manufacturer, model, sub-components), the software tools and the reference materials used across the TAPP, one array told apart by kind
- `schema:location` — laboratory/facility
- `schema:agent` — TAPP author (person or organisation)

### Standard workflow (`schema:actionProcess`)
A `schema:HowTo` containing `schema:step` — an ordered array of `schema:Action` + `schema:HowToStep` items. Typical steps:

1. **Sample preparation** (`bios:LabProcess`) — mounting, polishing, coating
2. **Instrument calibration** — primary/secondary standards, spectrometer setup
3. **Data acquisition** — beam conditions, per-element parameters (linked to `ada:targetSpeciesTemplate`)
4. **Data processing** — matrix correction, TDI, blank/normalization corrections
5. **Quality control** — drift monitoring, precision/accuracy assessment

Each workflow step can carry:
- `schema:additionalProperty` — typed step parameters (MethodParameter shape: scope, fieldScope, tier)
- `schema:instrument` — step-specific equipment, software, standards and materials (kind items, or `{@id}` references)
- `schema:object` / `schema:result` — input/output chaining
- `schema:actionProcess` — nested sub-workflow
- `dqv:hasQualityMeasurement` — step-specific quality metrics

### Per-analyte parameters (`ada:targetSpeciesTemplate`)
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
