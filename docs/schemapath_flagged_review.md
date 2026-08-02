# Schema-path flagged review (Phase 0)

40 paths the normalizer could not confidently canonicalize. Fill the **canonical** column
(per docs/SCHEMA_PATH_GRAMMAR.md) OR fix the `schema path` cell in the workbook and re-run
`python tools/normalize_schema_paths.py`.


## INSTRUMENT

| workbook | Metadata Item | original schema path | canonical (fill in) |
|---|---|---|---|
| laicpmsTAPP | Ablation Cell Type | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS].schema:hasPart[].additionalType[ 'Ablation Cell']. Schema:name` |  |
| laicpmsTAPP | Collision/Reaction Cell (CRC) Configuration | `$MethodDefinition.schema:instrument.schema:additionalProperty['Collision-ReactionCellConfiguration']. Schema:value` |  |
| laicpmsTAPP | Detector Configuration | `$MethodDefinition.schema:instrument.schema:additionalProperty['Detector Configuration']. Schema:value` |  |
| laicpmsTAPP | ICP-MS Manufacturer & Model | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS].schema:manufacturer.schema:Organization.schema:name | .schema:instrument.schema:model.schema:name` |  |
| laicpmsTAPP | ICP-MS Type | `$MethodDefinition.schema:instrument.schema:additionalType[ICP-MS].schema:name` |  |
| laicpmsTAPP | Interface Cone Configuration | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS]schema:hasPart[].additionalType [ 'Interface Cone']. Schema:name` |  |
| laicpmsTAPP | Laser Manufacturer & Model | `$MethodDefinition.schema:instrument[additionalType = 'Laser ablation system'].schema:manufacturer.schema:Organization.schema:name | .schema:instrument.schema:model.schema:name` |  |
| laicpmsTAPP | Laser Wavelength and Type | `$MethodDefinition.schema:instrument.additionalType['Laser'].additionalProperty[ 'Laser Wavelength and Type'].schema:value` |  |
| laicpmsTAPP | Mass Resolution Setting | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS]schema:additionalProperty['Mass Resolution Setting']. Schema:value` |  |
| laicpmsTAPP | Sampler and Skimmer Cone Material | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS]schema:hasPart[].additionalType [ 'Interface Cone']. schema:additiionalProperty['Sampler and Skimmer Cone Material'].schema:value` |  |
| laicpmsTAPP | Torch Depth | `$MethodDefinition.schema:instrument.:additionalType[ICP-MS]schema:additionalProperty['Torch Depth']. Schema:value` |  |
| semFibsemTAPP | BSE Detector Type | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'BSE_Detector'].schema.name` |  |
| semFibsemTAPP | Electron Source | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'ElectronSource'].schema:name` |  |
| semFibsemTAPP | Instrument Manufacturer | `$MethodDefinition.schema:instrument.schema:manufacturer.schema:Organization.schema:name` |  |
| semFibsemTAPP | Instrument Model | `$MethodDefinition.schema:instrument.schema:model.schema:name` |  |
| semFibsemTAPP | Instrument Variant | `$MethodDefinition.schema:instrument.schema:additionalType[]` |  |
| semFibsemTAPP | Ion Beam Source | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'IonBeamSource'].schema.name` |  |
| semFibsemTAPP | SE Detector Type | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'SE_Detector'].schema.name` |  |
| semImagingTAPP | Electron Source | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType = 'ElectronSource'` |  |
| semImagingTAPP | Instrument Manufacturer | `$MethodDefinition.schema:instrument.schema:manufacturer.schema:Organization.schema:name` |  |
| semImagingTAPP | Instrument Model | `$MethodDefinition.schema:instrument.schema:model.schema:name` |  |
| semImagingTAPP | Instrument Variant | `$MethodDefinition.schema:instrument.schema:additionalType` |  |
| temTAPP | 4D-STEM Detector | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'STEM4Ddetector']` |  |
| temTAPP | Aberration Corrector | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'AberrationCorrector'].schema:name` |  |
| temTAPP | EDS Detector Configuration | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'edsDetector']` |  |
| temTAPP | EELS Spectrometer | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'eelsSpectrometer']` |  |
| temTAPP | Electron Source | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'ElectronSource'].schema:name` |  |
| temTAPP | Imaging and Diffraction Detectors | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'ImagingAndDiffractionDetector']` |  |
| temTAPP | Instrument Manufacturer | `$MethodDefinition.schema:instrument.schema:manufacturer.schema:Organization.schema:name` |  |
| temTAPP | Instrument Model | `$MethodDefinition.schema:instrument.schema:model.schema:name` |  |
| temTAPP | Monochromator | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'Monochromator'].schema:name` |  |
| temTAPP | Sample Holder | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'SampleHolder'].schema:name` |  |
| temTAPP | Spectroscopic Detector(s) | `$MethodDefinition.schema:instrument.schema:hasPart[].additionalType[ 'SpectroscopicDetector'].schema:name` |  |

## MALFORMED

| workbook | Metadata Item | original schema path | canonical (fill in) |
|---|---|---|---|
| laicpmsTAPP | Analysis Location/Spot Coordinates | `$Dataset.schema.object[$type = schema:Thing].schema.name = 'mapped area description'.schema.description` |  |
| laicpmsTAPP | Uncertainty Propagation Method | `$MethodDefinition.schema:Uncertainty Propagation Method'].schema:defaultValue` |  |

## PROTOCOL-REF

| workbook | Metadata Item | original schema path | canonical (fill in) |
|---|---|---|---|
| labxctTAPP | Protocol Reference(s) | `$MethodDefinition.schema:relatedLink[].schema:linkRelationship[name = 'techniquePublication'].` |  |
| laicpmsTAPP | Protocol Reference(s) | `$MethodDefinition.schema:relatedLink[].schema:linkRelationship[name = 'techniquePublication'].` |  |
| semFibsemTAPP | Protocol Reference(s) | `$MethodDefinition.schema:relatedLink[].schema:linkRelationship[name = 'techniquePublication'].` |  |
| semImagingTAPP | Protocol Reference(s) | `$MethodDefinition.schema:relatedLink[].schema:linkRelationship[name = 'techniquePublication'].` |  |
| temTAPP | Protocol Reference(s) | `$MethodDefinition.schema:relatedLink[].schema:linkRelationship[name = 'techniquePublication'].` |  |
