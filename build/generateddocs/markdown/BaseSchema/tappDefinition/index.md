
# Technique-Aligned Protocol Profile (TAPP) Definition (Schema)

`ogch.BaseSchema.tappDefinition` *v0.3*

A registered Technique-Aligned Protocol Profile (TAPP) definition modeled as cdi:Activity + schema:Action + ada:TAPPDefinition + bios:LabProtocol. TAPP identity (name, technique, instrument, location, target material) at top level. Standard workflow encoded in schema:actionProcess as a schema:HowTo with ordered cdi:Activity + schema:Action steps. Each workflow step carries its own parameters, reagents, instruments. Uses bios:computationalTool for software, bios:reagent for reference materials, dqv:hasQualityMeasurement for quality metrics, ada:fieldScope (method/session/element) for parameter lifecycle.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### EPMA TAPP Definition Example (Concord glass)
Electron Microprobe Analysis TAPP definition for CU tephra glass,
modeled as cdi:Activity + schema:Action. Workflow in schema:actionProcess
with 5 ordered steps: sample preparation, calibration, WDS acquisition,
data processing, and quality control. Each step carries its own
parameters, reagents, and quality measurements.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ARL SEMQ",
    "schema:additionalType": [
      "ada:EPMAInstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "ARL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SEMQ"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "WDS Spectrometer",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "@id": "ex:instrument/ada-EPMAInstrument/part/WDS-Spectrometer"
      }
    ],
    "@id": "ex:instrument/ada-EPMAInstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Concord University, Athens, West Virginia, USA"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Concord University"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Additional Notes",
      "schema:valueName": "additionalNotes",
      "ada:fieldScope": "method",
      "ada:category": "General",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "ada:tier": "O"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS tephra glass analytical workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Tephra glass grains mounted, polished, and carbon coated for EPMA.",
        "bios:reagent": [
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Carbon",
            "ada:reagentRole": "coatingMaterial"
          }
        ],
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Albite",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Kaersutite amphibole",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "Lipari obsidian ID3506",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "USGS BHVO-2g",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "USGS NKT-1g",
            "ada:reagentRole": "secondaryStandard"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction.",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 6,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "ada:fieldScope": "session",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 10,
            "schema:minValue": 0,
            "schema:maxValue": 50,
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "schema:version": "9.6.4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": [
              "https://vocab.onegeochemistry.org/epma/matrix-correction"
            ],
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary reference materials at start/end of session; calibration interpolated",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical precision (1-sigma)",
            "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analyte",
        "schema:description": "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "xenon"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "P-10"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "SDD"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Si(Li)"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Other"
            }
          ]
        }
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "phaSettings",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Integral"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Differential"
            }
          ]
        }
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Method",
        "schema:valueName": "normalizationMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Standards",
        "schema:valueName": "normalizationStandards",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "number",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      "TiO2"
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ARL SEMQ",
    "schema:additionalType": [
      "ada:EPMAInstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "ARL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SEMQ"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "WDS Spectrometer",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "@id": "ex:instrument/ada-EPMAInstrument/part/WDS-Spectrometer"
      }
    ],
    "@id": "ex:instrument/ada-EPMAInstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Concord University, Athens, West Virginia, USA"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Concord University"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Additional Notes",
      "schema:valueName": "additionalNotes",
      "ada:fieldScope": "method",
      "ada:category": "General",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "ada:tier": "O"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS tephra glass analytical workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Tephra glass grains mounted, polished, and carbon coated for EPMA.",
        "bios:reagent": [
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Carbon",
            "ada:reagentRole": "coatingMaterial"
          }
        ],
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Albite",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Kaersutite amphibole",
            "ada:reagentRole": "primaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "Lipari obsidian ID3506",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "USGS BHVO-2g",
            "ada:reagentRole": "secondaryStandard"
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "USGS NKT-1g",
            "ada:reagentRole": "secondaryStandard"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction.",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 6,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "ada:fieldScope": "session",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 10,
            "schema:minValue": 0,
            "schema:maxValue": 50,
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "schema:version": "9.6.4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": [
              "https://vocab.onegeochemistry.org/epma/matrix-correction"
            ],
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary reference materials at start/end of session; calibration interpolated",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical precision (1-sigma)",
            "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analyte",
        "schema:description": "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "xenon"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "P-10"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "SDD"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Si(Li)"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Other"
            }
          ]
        }
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "phaSettings",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Integral"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Differential"
            }
          ]
        }
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Method",
        "schema:valueName": "normalizationMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization Standards",
        "schema:valueName": "normalizationStandards",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "O"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "number",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      "TiO2"
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA WDS tephra glass analytical workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Primary reference materials at start/end of session; calibration interpolated" ;
                            schema1:name "Drift Correction" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "driftCorrection" ;
                            schema1:valueRequired false ;
                            ada:category "Quality Control" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "R" ] ;
                    schema1:description "Secondary standards analysed at start and end of every session. Drift correction by interpolation of primary standard calibrations." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedResults> ;
                    schema1:position 5 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "analytical precision (1-sigma)" ;
                            dqv:value "Reported per element on secondary standards; see relatedLink publications" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/matrix-correction-models> ;
                            schema1:name "Matrix Correction Model" ;
                            schema1:propertyID "https://vocab.onegeochemistry.org/epma/matrix-correction" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "matrixCorrectionModel" ;
                            schema1:valueRequired true ;
                            ada:category "Data Processing" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ;
                    schema1:description "Matrix correction, blank correction, and standards-based normalization using Probe for EPMA." ;
                    schema1:name "Data processing" ;
                    schema1:object <file:///github/workspace/#rawAnalyses> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#quantifiedResults> ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA" ;
                            schema1:version "9.6.4" ;
                            ada:toolRole "dataReduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate WDS spectrometers on primary standards. Verify on secondary standards at start and end of session." ;
                    schema1:name "Instrument calibration" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 2 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "USGS NKT-1g" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:ChemicalSubstance ;
                            schema1:name "Kaersutite amphibole" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "Lipari obsidian ID3506" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:name "USGS BHVO-2g" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:ChemicalSubstance ;
                            schema1:name "Albite" ;
                            ada:reagentRole "primaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 15 ;
                            schema1:name "Accelerating Voltage" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "kV" ;
                            schema1:valueName "acceleratingVoltage" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Si, Al, Na acquired first; 6-7 time intervals for TDI correction" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-damage-methods> ;
                            schema1:name "Beam Damage Minimization" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDamageMinimization" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 6 ;
                            schema1:maxValue 200 ;
                            schema1:minValue 1 ;
                            schema1:name "Beam Current" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "nA" ;
                            schema1:valueName "beamCurrent" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 10 ;
                            schema1:maxValue 50 ;
                            schema1:minValue 0 ;
                            schema1:name "Beam Diameter" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "um" ;
                            schema1:valueName "beamDiameter" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ;
                    schema1:description "Quantitative WDS analysis at 15 kV / 6 nA. Si, Al, Na acquired first to minimize beam damage with TDI correction." ;
                    schema1:name "WDS data acquisition" ;
                    schema1:position 3 ;
                    schema1:result <file:///github/workspace/#rawAnalyses> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Tephra glass grains mounted, polished, and carbon coated for EPMA." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ;
                    bios:reagent [ a schema1:ChemicalSubstance ;
                            schema1:name "Carbon" ;
                            ada:reagentRole "coatingMaterial" ] ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "Concord University" ] ;
    schema1:datePublished "2011-10-20" ;
    schema1:instrument <https://example.org/instrument/ada-EPMAInstrument> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Concord University, Athens, West Virginia, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ] ;
    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "silicate glass" ] ;
    schema1:version "1.0.6" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard Name" ;
                    schema1:valueName "calibrationStandardName" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit Method" ;
                    schema1:valueName "detectionLimitMethod" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Sequence" ;
                    schema1:valueName "sequence" ;
                    schema1:valueRequired false ;
                    ada:dataType "integer" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Normalization Method" ;
                    schema1:valueName "normalizationMethod" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "O" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/background-methods> ;
                    schema1:name "Background Method" ;
                    schema1:valueName "backgroundMethod" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Spectrometer" ;
                    schema1:valueName "spectrometer" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/diffracting-crystals> ;
                    schema1:name "Diffracting Crystal" ;
                    schema1:valueName "diffractingCrystal" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit" ;
                    schema1:valueName "detectionLimit" ;
                    schema1:valueRequired false ;
                    ada:dataType "number" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Peak Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "peakCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Normalization Standards" ;
                    schema1:valueName "normalizationStandards" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "O" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                            schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                                    schema1:termCode "Differential" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "Integral" ] ] ;
                    schema1:name "WDS PHA Setting" ;
                    schema1:valueName "phaSettings" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                            schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                                    schema1:termCode "Other" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "SDD" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "P-10" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "Si(Li)" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "xenon" ] ] ;
                    schema1:name "Detector Type" ;
                    schema1:valueName "detectorType" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "Beam Current (nA)" ;
                    schema1:unitText "nA" ;
                    schema1:valueName "beamCurrent" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/xray-lines> ;
                    schema1:name "X-ray Line" ;
                    schema1:valueName "xrayLine" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Background Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings." ;
                    schema1:name "Analysed Oxide/Element" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Detection Limit Unit" ;
                    schema1:valueName "detectionLimitUnit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ] ;
            ada:defaultAnalytes "SiO2",
                "TiO2" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
            schema1:name "Additional Notes" ;
            schema1:readonlyValue true ;
            schema1:valueName "additionalNotes" ;
            schema1:valueRequired false ;
            ada:category "General" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "O" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            schema1:version "9.6.4" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/ada-EPMAInstrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ada:EPMAInstrument" ;
    schema1:hasPart <https://example.org/instrument/ada-EPMAInstrument/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ARL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SEMQ" ] ;
    schema1:name "ARL SEMQ" .

<https://example.org/instrument/ada-EPMAInstrument/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
    schema1:name "WDS Spectrometer Array" .


```


### NMNH Spinel Oxybarometry TAPP Definition (NMNH Smithsonian)
Spinel oxybarometry TAPP definition at NMNH Smithsonian, modeled as
cdi:Activity + schema:Action. Workflow with 5 steps including
calibration with Smithsonian reference standards carrying
catalog identifiers and citations. Multiple target materials
(spinel, olivine, orthopyroxene) via schema:object.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Spinel oxybarometry version 1",
  "schema:version": "1.0",
  "schema:datePublished": "2013-11-08",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "olivine",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "orthopyroxene",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8900"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "WDS Spectrometer",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH.",
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/WDS-Spectrometer"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National Museum of Natural History, Smithsonian Institution"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Smithsonian Institution, Department of Mineral Sciences"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "WDS Utilization",
      "schema:valueName": "wdsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Yes",
      "ada:tier": "M",
      "schema:inDefinedTermSet": {
        "@type": "schema:DefinedTermSet",
        "schema:hasDefinedTerm": [
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "Yes"
          },
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "No"
          }
        ]
      }
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "EDS Utilization",
      "schema:valueName": "edsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "No",
      "ada:tier": "M",
      "schema:inDefinedTermSet": {
        "@type": "schema:DefinedTermSet",
        "schema:hasDefinedTerm": [
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "Yes"
          },
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "No"
          }
        ]
      }
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS spinel oxybarometry workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated.",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992).",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "San Carlos olivine",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 111312/444"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Tiebaghi Mine chromite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 117075"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Kakanui Hornblende",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 143965"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Spinel",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 136041"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Manganite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 114887"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Wollastonite (synthetic, F.R. Boyd)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320",
            "schema:description": "Secondary spinel standards for Fe3+/Î£Fe calibration",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously.",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 40,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-modes"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Focused beam",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Raster",
            "schema:valueName": "beamRaster",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "none",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "not applicable",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction using CITZAF. Fe3+/Î£Fe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known MÃ¶ssbauer Fe3+/Î£Fe ratios.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": [
              "https://vocab.onegeochemistry.org/epma/matrix-correction"
            ],
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "CITZAF",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Primary and secondary standards run at start and end of session; subset run regularly during session.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary and secondary standards at start/end; subset run regularly during session.",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical reproducibility",
            "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analyte",
        "schema:description": "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard ID",
        "schema:valueName": "calibrationStandardID",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Citation for Standard",
        "schema:valueName": "citationForStandard",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      "TiO2",
      "Al2O3",
      "Cr2O3",
      "FeOT",
      "MnO",
      "MgO",
      "CaO",
      "NiO"
    ]
  },
  "schema:relatedLink": []
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Spinel oxybarometry version 1",
  "schema:version": "1.0",
  "schema:datePublished": "2013-11-08",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "olivine",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "orthopyroxene",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8900"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "WDS Spectrometer",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "WDS Spectrometer Array",
        "schema:description": "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH.",
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/WDS-Spectrometer"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National Museum of Natural History, Smithsonian Institution"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Smithsonian Institution, Department of Mineral Sciences"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "WDS Utilization",
      "schema:valueName": "wdsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Yes",
      "ada:tier": "M",
      "schema:inDefinedTermSet": {
        "@type": "schema:DefinedTermSet",
        "schema:hasDefinedTerm": [
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "Yes"
          },
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "No"
          }
        ]
      }
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "EDS Utilization",
      "schema:valueName": "edsUtilization",
      "ada:fieldScope": "method",
      "ada:category": "Instrument & Software",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "No",
      "ada:tier": "M",
      "schema:inDefinedTermSet": {
        "@type": "schema:DefinedTermSet",
        "schema:hasDefinedTerm": [
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "Yes"
          },
          {
            "@type": "schema:DefinedTerm",
            "schema:termCode": "No"
          }
        ]
      }
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPMA WDS spinel oxybarometry workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated.",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Instrument calibration",
        "schema:position": 2,
        "schema:description": "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992).",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "bios:reagent": [
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "San Carlos olivine",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 111312/444"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u00e2\u20ac\u201c47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Tiebaghi Mine chromite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 117075"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u00e2\u20ac\u201c47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Kakanui Hornblende",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 143965"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43\u00e2\u20ac\u201c47."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Spinel",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 136041"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "Manganite",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "Smithsonian catalog",
              "schema:value": "NMNH 114887"
            },
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:ChemicalSubstance"
            ],
            "schema:name": "Wollastonite (synthetic, F.R. Boyd)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Davis et al. (2017), American Mineralogist."
          },
          {
            "@type": [
              "schema:Product"
            ],
            "schema:name": "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320",
            "schema:description": "Secondary spinel standards for Fe3+/\u00ce\u00a3Fe calibration",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "WDS data acquisition",
        "schema:position": 3,
        "schema:description": "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously.",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Accelerating Voltage",
            "schema:valueName": "acceleratingVoltage",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 15,
            "schema:unitText": "kV",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Current",
            "schema:valueName": "beamCurrent",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": 40,
            "schema:minValue": 1,
            "schema:maxValue": 200,
            "schema:unitText": "nA",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Diameter",
            "schema:valueName": "beamDiameter",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/beam-modes"
            },
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "Focused beam",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Raster",
            "schema:valueName": "beamRaster",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "none",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Beam Damage Minimization",
            "schema:valueName": "beamDamageMinimization",
            "ada:fieldScope": "method",
            "ada:category": "Beam Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "not applicable",
            "ada:tier": "R"
          }
        ],
        "schema:result": {
          "@id": "#rawAnalyses"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data processing",
        "schema:position": 4,
        "schema:description": "Matrix correction using CITZAF. Fe3+/\u00ce\u00a3Fe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known M\u00c3\u00b6ssbauer Fe3+/\u00ce\u00a3Fe ratios.",
        "schema:object": {
          "@id": "#rawAnalyses"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Probe for EPMA",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Matrix Correction Model",
            "schema:valueName": "matrixCorrectionModel",
            "schema:propertyID": [
              "https://vocab.onegeochemistry.org/epma/matrix-correction"
            ],
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
            },
            "ada:fieldScope": "method",
            "ada:category": "Data Processing",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "CITZAF",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedResults"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 5,
        "schema:description": "Primary and secondary standards run at start and end of session; subset run regularly during session.",
        "schema:object": {
          "@id": "#quantifiedResults"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Drift Correction",
            "schema:valueName": "driftCorrection",
            "ada:fieldScope": "session",
            "ada:category": "Quality Control",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": false,
            "schema:defaultValue": "Primary and secondary standards at start/end; subset run regularly during session.",
            "ada:tier": "R"
          }
        ],
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "analytical reproducibility",
            "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysed Oxide/Element",
        "schema:valueName": "analyte",
        "schema:description": "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayLine",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/xray-lines"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Peak Counting Time (s)",
        "schema:valueName": "peakCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Method",
        "schema:valueName": "backgroundMethod",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/background-methods"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Counting Time (s)",
        "schema:valueName": "backgroundCountingTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard Name",
        "schema:valueName": "calibrationStandardName",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Calibration Standard ID",
        "schema:valueName": "calibrationStandardID",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Citation for Standard",
        "schema:valueName": "citationForStandard",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      "TiO2",
      "Al2O3",
      "Cr2O3",
      "FeOT",
      "MnO",
      "MgO",
      "CaO",
      "NiO"
    ]
  },
  "schema:relatedLink": []
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/nmnh-spinel-oxybar-v1> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "EPMA WDS spinel oxybarometry workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate WDS spectrometers on primary Smithsonian standards. Verify with secondary spinel standards from Wood & Virgo (1989), Bryndzia & Wood (1990), and Ionov & Wood (1992)." ;
                    schema1:name "Instrument calibration" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 2 ;
                    bios:reagent [ a schema1:Product ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 136041" ] ;
                            schema1:name "Spinel" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Product ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 114887" ] ;
                            schema1:name "Manganite" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Product ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 143965" ] ;
                            schema1:name "Kakanui Hornblende" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Product ;
                            schema1:citation "Wood & Virgo (1989); Bryndzia & Wood (1990); Ionov & Wood (1992)." ;
                            schema1:description "Secondary spinel standards for Fe3+/Î£Fe calibration" ;
                            schema1:name "IO-5657, PS-216, Vi314-5, IM8703, DB8803-3, BAR8601-10, MO4334-14, KLB8320" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:ChemicalSubstance ;
                            schema1:citation "Davis et al. (2017), American Mineralogist." ;
                            schema1:name "Wollastonite (synthetic, F.R. Boyd)" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Product ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 111312/444" ] ;
                            schema1:name "San Carlos olivine" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:Product ;
                            schema1:citation "Jarosewich et al. (1980), Geostandards Newsletter, 4(1): 43â€“47." ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:propertyID "Smithsonian catalog" ;
                                    schema1:value "NMNH 117075" ] ;
                            schema1:name "Tiebaghi Mine chromite" ;
                            ada:reagentRole "primaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Spinel-bearing peridotite samples mounted in epoxy, polished, and carbon coated." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "not applicable" ;
                            schema1:name "Beam Damage Minimization" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDamageMinimization" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 15 ;
                            schema1:name "Accelerating Voltage" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "kV" ;
                            schema1:valueName "acceleratingVoltage" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "none" ;
                            schema1:name "Beam Raster" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamRaster" ;
                            schema1:valueRequired false ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Focused beam" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-modes> ;
                            schema1:name "Beam Diameter" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "beamDiameter" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 40 ;
                            schema1:maxValue 200 ;
                            schema1:minValue 1 ;
                            schema1:name "Beam Current" ;
                            schema1:readonlyValue true ;
                            schema1:unitText "nA" ;
                            schema1:valueName "beamCurrent" ;
                            schema1:valueRequired true ;
                            ada:category "Beam Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ;
                    schema1:description "Quantitative WDS analysis at 15 kV / 40 nA, focused beam. 5 spectrometers measuring SiO2, TiO2, Al2O3, Cr2O3, FeOT, MnO, MgO, CaO, NiO simultaneously." ;
                    schema1:name "WDS data acquisition" ;
                    schema1:position 3 ;
                    schema1:result <file:///github/workspace/#rawAnalyses> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "CITZAF" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/matrix-correction-models> ;
                            schema1:name "Matrix Correction Model" ;
                            schema1:propertyID "https://vocab.onegeochemistry.org/epma/matrix-correction" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "matrixCorrectionModel" ;
                            schema1:valueRequired true ;
                            ada:category "Data Processing" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ] ;
                    schema1:description "Matrix correction using CITZAF. Fe3+/Î£Fe calculated from spinel stoichiometry using flank method calibrated against secondary spinel standards with known MÃ¶ssbauer Fe3+/Î£Fe ratios." ;
                    schema1:name "Data processing" ;
                    schema1:object <file:///github/workspace/#rawAnalyses> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#quantifiedResults> ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA" ;
                            ada:toolRole "dataReduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Primary and secondary standards at start/end; subset run regularly during session." ;
                            schema1:name "Drift Correction" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "driftCorrection" ;
                            schema1:valueRequired false ;
                            ada:category "Quality Control" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "R" ] ;
                    schema1:description "Primary and secondary standards run at start and end of session; subset run regularly during session." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedResults> ;
                    schema1:position 5 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "analytical reproducibility" ;
                            dqv:value "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304" ] ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "Smithsonian Institution, Department of Mineral Sciences" ] ;
    schema1:datePublished "2013-11-08" ;
    schema1:instrument <https://example.org/instrument/nxs-BaseClass-NXinstrument> ;
    schema1:location [ a schema1:Place ;
            schema1:name "National Museum of Natural History, Smithsonian Institution" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ] ;
    schema1:name "Spinel oxybarometry version 1" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "orthopyroxene" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "spinel" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "olivine" ] ;
    schema1:version "1.0" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard Name" ;
                    schema1:valueName "calibrationStandardName" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Peak Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "peakCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Spectrometer" ;
                    schema1:valueName "spectrometer" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/diffracting-crystals> ;
                    schema1:name "Diffracting Crystal" ;
                    schema1:valueName "diffractingCrystal" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Each row in the analyte table identifies the analyzed constituent for that row (e.g. an oxide, element, or isotope). In the long run, values should come from a DefinedTermSet; for now they are strings." ;
                    schema1:name "Analysed Oxide/Element" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "Beam Current (nA)" ;
                    schema1:unitText "nA" ;
                    schema1:valueName "beamCurrent" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Calibration Standard ID" ;
                    schema1:valueName "calibrationStandardID" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Citation for Standard" ;
                    schema1:valueName "citationForStandard" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:minValue 1 ;
                    schema1:name "Background Counting Time (s)" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountingTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/background-methods> ;
                    schema1:name "Background Method" ;
                    schema1:valueName "backgroundMethod" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/xray-lines> ;
                    schema1:name "X-ray Line" ;
                    schema1:valueName "xrayLine" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ;
            ada:defaultAnalytes "Al2O3",
                "CaO",
                "Cr2O3",
                "FeOT",
                "MgO",
                "MnO",
                "NiO",
                "SiO2",
                "TiO2" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Yes" ;
            schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                    schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                            schema1:termCode "No" ],
                        [ a schema1:DefinedTerm ;
                            schema1:termCode "Yes" ] ] ;
            schema1:name "WDS Utilization" ;
            schema1:readonlyValue true ;
            schema1:valueName "wdsUtilization" ;
            schema1:valueRequired true ;
            ada:category "Instrument & Software" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "No" ;
            schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                    schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                            schema1:termCode "No" ],
                        [ a schema1:DefinedTerm ;
                            schema1:termCode "Yes" ] ] ;
            schema1:name "EDS Utilization" ;
            schema1:readonlyValue true ;
            schema1:valueName "edsUtilization" ;
            schema1:valueRequired true ;
            ada:category "Instrument & Software" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/nxs-BaseClass-NXinstrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "nxs:BaseClass/NXinstrument" ;
    schema1:hasPart <https://example.org/instrument/nxs-BaseClass-NXinstrument/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8900" ] ;
    schema1:name "JEOL JXA-8900 Superprobe; JEOL JXA-8530F Hyperprobe" .

<https://example.org/instrument/nxs-BaseClass-NXinstrument/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:description "5 WDS spectrometers with TAPx2, LiFx2, PETJ, LiFH." ;
    schema1:name "WDS Spectrometer Array" .


```


### LA-ICP-MS Volcanic Glass Trace Elements TAPP (UoC v1)
Laser ablation ICP-MS TAPP definition for trace elements in volcanic
glass from the University of Cologne. Demonstrates a non-EPMA technique
with a different workflow: sample prep, ICP-MS tuning, laser
calibration with NIST612/610/ATHO-G/StHs6/80-G standards, laser
ablation acquisition (193 nm excimer, point mode, 15-20 um spots),
Iolite 4 data reduction, and QC. Shows compound instrument
(laser + mass spec as schema:hasPart), isotope-based analyte
template, and TAPP-level funding/references.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "UoC volcanic glass trace elements v.1",
  "schema:identifier": "http://doi.org/10.60520/IEDA/114187",
  "schema:version": "1.0",
  "schema:datePublished": "2022-04-22",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "LA-ICP-MS",
      "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "volcanic glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "Laser Ablation System",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System"
      },
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "ICPMS",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Thermo Fisher Scientific"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/ICPMS"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Cologne, Institute of Geology and Mineralogy"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "dataReduction"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Internal Standard",
      "schema:valueName": "internalStandard",
      "ada:fieldScope": "method",
      "ada:category": "Calibration",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Si analyzed by EPMA or EDS",
      "schema:description": "Internal standard element and how its concentration is derived for each unknown.",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Element Fractionation Correction",
      "schema:valueName": "elementFractionationCorrection",
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "No correction other than measurement relative to NIST612 and use of Si as internal standard",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Calibration/QC/Unknown Sequence",
      "schema:valueName": "analysisSequenceRatio",
      "schema:description": "Ratio of calibration standard / QC standard / unknown analyses in a repeating block.",
      "ada:fieldScope": "session",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": false,
      "schema:valueRequired": false,
      "schema:defaultValue": "2/4/15",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Detection Limit Method",
      "schema:valueName": "detectionLimitMethod",
      "ada:fieldScope": "method",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Sample individual LOD calculation according to Pettke et al. (2012)",
      "ada:tier": "R"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "DFG INST 216/1019-1 FUGG no. 665508"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:relatedLink": [],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15â€“20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {
          "@id": "#rawSignals"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {
          "@id": "#quantifiedConcentrations"
        },
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Measured Isotope",
        "schema:valueName": "analyte",
        "schema:description": "Element symbol with mass number (e.g. Si29, Ba138, U238).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer Dwell Time",
        "schema:valueName": "spectrometerDwellTime",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Dwell time per isotope per sweep in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysis Count Time",
        "schema:valueName": "analysisCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Total signal integration time during ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Count Time",
        "schema:valueName": "backgroundCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Gas blank measurement time before ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "schema:description": "Typical detection limit at 99% confidence (3-sigma).",
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "ppm"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "ppb"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "weight percent (%m/m)"
            }
          ]
        }
      }
    ],
    "ada:defaultAnalytes": [
      "Si29",
      "Ca43",
      "Rb85",
      "Sr88",
      "Y89",
      "Zr90",
      "Nb93",
      "Ba138",
      "La139",
      "Ce140",
      "Nd146",
      "Sm147",
      "Eu153",
      "Gd157",
      "Dy163",
      "Er166",
      "Yb172",
      "Lu175",
      "Hf178",
      "Th232",
      "U238"
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "UoC volcanic glass trace elements v.1",
  "schema:identifier": "http://doi.org/10.60520/IEDA/114187",
  "schema:version": "1.0",
  "schema:datePublished": "2022-04-22",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "LA-ICP-MS",
      "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "volcanic glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "Laser Ablation System",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System"
      },
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "ICPMS",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Thermo Fisher Scientific"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/ICPMS"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany"
  },
  "schema:agent": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Cologne, Institute of Geology and Mineralogy"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "dataReduction"
    }
  ],
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Internal Standard",
      "schema:valueName": "internalStandard",
      "ada:fieldScope": "method",
      "ada:category": "Calibration",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Si analyzed by EPMA or EDS",
      "schema:description": "Internal standard element and how its concentration is derived for each unknown.",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Element Fractionation Correction",
      "schema:valueName": "elementFractionationCorrection",
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "No correction other than measurement relative to NIST612 and use of Si as internal standard",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Calibration/QC/Unknown Sequence",
      "schema:valueName": "analysisSequenceRatio",
      "schema:description": "Ratio of calibration standard / QC standard / unknown analyses in a repeating block.",
      "ada:fieldScope": "session",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": false,
      "schema:valueRequired": false,
      "schema:defaultValue": "2/4/15",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Detection Limit Method",
      "schema:valueName": "detectionLimitMethod",
      "ada:fieldScope": "method",
      "ada:category": "Quality Control",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Sample individual LOD calculation according to Pettke et al. (2012)",
      "ada:tier": "R"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "DFG INST 216/1019-1 FUGG no. 665508"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:relatedLink": [],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u00e2\u20ac\u201c429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u00e2\u20ac\u201c429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15\u00e2\u20ac\u201c20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {
          "@id": "#rawSignals"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {
          "@id": "#quantifiedConcentrations"
        },
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Measured Isotope",
        "schema:valueName": "analyte",
        "schema:description": "Element symbol with mass number (e.g. Si29, Ba138, U238).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer Dwell Time",
        "schema:valueName": "spectrometerDwellTime",
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "schema:description": "Dwell time per isotope per sweep in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analysis Count Time",
        "schema:valueName": "analysisCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Total signal integration time during ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Count Time",
        "schema:valueName": "backgroundCountTime",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:description": "Gas blank measurement time before ablation in seconds.",
        "schema:unitText": "seconds",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit",
        "schema:valueName": "detectionLimit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "schema:description": "Typical detection limit at 99% confidence (3-sigma).",
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Unit",
        "schema:valueName": "detectionLimitUnit",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "ppm"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "ppb"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "weight percent (%m/m)"
            }
          ]
        }
      }
    ],
    "ada:defaultAnalytes": [
      "Si29",
      "Ca43",
      "Rb85",
      "Sr88",
      "Y89",
      "Zr90",
      "Nb93",
      "Ba138",
      "La139",
      "Ce140",
      "Nd146",
      "Sm147",
      "Eu153",
      "Gd157",
      "Dy163",
      "Er166",
      "Yb172",
      "Lu175",
      "Hf178",
      "Th232",
      "U238"
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://registry.onegeochemistry.org/methods/uoc-laicpms-glass-v1> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "LA-ICP-MS volcanic glass trace element workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G." ;
                    schema1:name "Laser ablation calibration" ;
                    schema1:position 3 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING Icelandic rhyolite glass" ;
                            schema1:name "ATHO-G" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING St. Helens dacite glass" ;
                            schema1:name "StHs6/80-G" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429." ;
                            schema1:description "Trace Elements in Glass (nominal 500 ppm)" ;
                            schema1:name "NIST SRM 610" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429." ;
                            schema1:description "Trace Elements in Glass (nominal 50 ppm)" ;
                            schema1:name "NIST SRM 612" ;
                            ada:reagentRole "primaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "15; 20" ;
                            schema1:description "Spot width in um; multiple values if varied during session." ;
                            schema1:name "Laser Spot Width" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "um" ;
                            schema1:valueName "laserSpotWidth" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "7 ns" ;
                            schema1:name "Laser Pulse Time" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserPulseTime" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 5 ;
                            schema1:name "Repetition Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "Hz" ;
                            schema1:valueName "repetitionRate" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "point" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/laicpms/spot-geometries> ;
                            schema1:name "Laser Spot Path Geometry" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "laserSpotPathGeometry" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "193 nm (ArF excimer)" ;
                            schema1:name "Laser Wavelength" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserWavelength" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1e-03 ;
                            schema1:name "Laser Energy" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "mJ" ;
                            schema1:valueName "laserEnergy" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ;
                    schema1:description "Ablate sample in point mode with 15â€“20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device." ;
                    schema1:name "Laser ablation data acquisition" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#rawSignals> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard)." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012)." ;
                    schema1:name "Data reduction" ;
                    schema1:object <file:///github/workspace/#rawSignals> ;
                    schema1:position 5 ;
                    schema1:result <file:///github/workspace/#quantifiedConcentrations> ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Iolite" ;
                            schema1:version "4" ;
                            ada:toolRole "dataReduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedConcentrations> ;
                    schema1:position 6 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "detection limit method" ;
                            dqv:value "Sample-individual LOD per Pettke et al. (2012)" ],
                        [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "oxide production" ;
                            dqv:value "ThO/Th ca. 0.7%" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "ca. 0.7%" ;
                            schema1:name "Oxide Production (ThO/Th)" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "oxideProduction" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 9e-01 ;
                            schema1:name "Carrier Gas (He) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasHeFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 8e-01 ;
                            schema1:name "Carrier Gas (Ar) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasArFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Glass smoothing device" ;
                            schema1:name "Signal Smoothing" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "signalSmoothing" ;
                            schema1:valueRequired false ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1200 ;
                            schema1:name "RF Power" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "W" ;
                            schema1:valueName "rfPower" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ;
                    schema1:description "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%)." ;
                    schema1:name "ICP-MS tuning and optimization" ;
                    schema1:position 2 ] ] ;
    schema1:agent [ a schema1:Organization ;
            schema1:name "University of Cologne, Institute of Geology and Mineralogy" ] ;
    schema1:datePublished "2022-04-22" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:name "Deutsche Forschungsgemeinschaft (DFG)" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "DFG INST 216/1019-1 FUGG no. 665508" ] ] ;
    schema1:identifier "http://doi.org/10.60520/IEDA/114187" ;
    schema1:instrument <https://example.org/instrument/nxs-BaseClass-NXinstrument> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Geo-/Cosmochemistry lab, Institute of Geology and Mineralogy, University of Cologne, Germany" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:description "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "LA-ICP-MS" ] ;
    schema1:name "UoC volcanic glass trace elements v.1" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "volcanic glass" ] ;
    schema1:version "1.0" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Gas blank measurement time before ablation in seconds." ;
                    schema1:minValue 1 ;
                    schema1:name "Background Count Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "backgroundCountTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Element symbol with mass number (e.g. Si29, Ba138, U238)." ;
                    schema1:name "Measured Isotope" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                            schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                                    schema1:termCode "ppm" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "ppb" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "weight percent (%m/m)" ] ] ;
                    schema1:name "Detection Limit Unit" ;
                    schema1:valueName "detectionLimitUnit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Dwell time per isotope per sweep in seconds." ;
                    schema1:name "Spectrometer Dwell Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "spectrometerDwellTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Total signal integration time during ablation in seconds." ;
                    schema1:minValue 1 ;
                    schema1:name "Analysis Count Time" ;
                    schema1:unitText "seconds" ;
                    schema1:valueName "analysisCountTime" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:description "Typical detection limit at 99% confidence (3-sigma)." ;
                    schema1:name "Detection Limit" ;
                    schema1:valueName "detectionLimit" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ] ;
            ada:defaultAnalytes "Ba138",
                "Ca43",
                "Ce140",
                "Dy163",
                "Er166",
                "Eu153",
                "Gd157",
                "Hf178",
                "La139",
                "Lu175",
                "Nb93",
                "Nd146",
                "Rb85",
                "Si29",
                "Sm147",
                "Sr88",
                "Th232",
                "U238",
                "Y89",
                "Yb172",
                "Zr90" ] ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Si analyzed by EPMA or EDS" ;
            schema1:description "Internal standard element and how its concentration is derived for each unknown." ;
            schema1:name "Internal Standard" ;
            schema1:readonlyValue true ;
            schema1:valueName "internalStandard" ;
            schema1:valueRequired true ;
            ada:category "Calibration" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "2/4/15" ;
            schema1:description "Ratio of calibration standard / QC standard / unknown analyses in a repeating block." ;
            schema1:name "Calibration/QC/Unknown Sequence" ;
            schema1:readonlyValue false ;
            schema1:valueName "analysisSequenceRatio" ;
            schema1:valueRequired false ;
            ada:category "Quality Control" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Sample individual LOD calculation according to Pettke et al. (2012)" ;
            schema1:name "Detection Limit Method" ;
            schema1:readonlyValue true ;
            schema1:valueName "detectionLimitMethod" ;
            schema1:valueRequired false ;
            ada:category "Quality Control" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "No correction other than measurement relative to NIST612 and use of Si as internal standard" ;
            schema1:name "Element Fractionation Correction" ;
            schema1:readonlyValue true ;
            schema1:valueName "elementFractionationCorrection" ;
            schema1:valueRequired false ;
            ada:category "Data Processing" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "R" ] ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Iolite" ;
            schema1:url "https://iolite-software.com/" ;
            schema1:version "4" ;
            ada:toolRole "dataReduction" ] .

<https://example.org/instrument/nxs-BaseClass-NXinstrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "nxs:BaseClass/NXinstrument" ;
    schema1:hasPart <https://example.org/instrument/nxs-BaseClass-NXinstrument/part/ICPMS>,
        <https://example.org/instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System> ;
    schema1:name "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS" .

<https://example.org/instrument/nxs-BaseClass-NXinstrument/part/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:description "Single-quadrupole ICP-MS" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:name "Thermo Fischer iCAP Q" .

<https://example.org/instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:description "193 nm ArF excimer laser ablation system" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Elemental Scientific Lasers (ESI)" ] ;
    schema1:name "ESI imageGEO193" .


```


### All-properties reference instance (synthetic)
Every property tappDefinition allows, populated - the file to read when asking
"what may a TAPP contain?". Generated from resolvedSchema.json and populated
with values mined from the publication-derived examples, so the shapes are the
schema's and the content is real: six analyte columns, the six-step workflow,
real instruments and calibration standards.

Note ada:defaultAnalytes here: the schema allows a bare string OR a
schema:DefinedTerm identifying the analyte. Per-analyte column VALUES are not
members of that array.

Synthetic, so it describes no real laboratory procedure and must not be cited
as one.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
    },
    "schema:value": "NMNH 111312/444",
    "schema:url": "https://iolite-software.com/"
  },
  "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:dateModified": "synthetic schema:dateModified",
  "schema:additionalType": [
    "ada:EPMAInstrument"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "LA-ICP-MS",
      "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@id": "#preparedMount"
    },
    {
      "@id": "#rawAnalyses"
    },
    {
      "@id": "#quantifiedResults"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "Laser Ablation System",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System"
      },
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "ICPMS",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Thermo Fisher Scientific"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/ICPMS"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:version": "1.0.6",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "dataReduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "dataReduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "dataReduction"
    }
  ],
  "bios:reagent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:identifier": {
        "@type": [
          "prov:Plan"
        ],
        "schema:propertyID": "Smithsonian catalog",
        "schema:value": "NMNH 111312/444"
      },
      "schema:termCode": "xenon",
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods",
        "schema:name": "CU routine tephra glass version 1.0 with 6nA"
      },
      "ada:reagentRole": "primaryStandard",
      "schema:citation": {
        "@type": [
          "prov:Plan"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:url": "https://iolite-software.com/"
      }
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Carbon",
      "ada:reagentRole": "coatingMaterial"
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Albite",
      "ada:reagentRole": "primaryStandard"
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Kaersutite amphibole",
      "ada:reagentRole": "primaryStandard"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Lipari obsidian ID3506",
      "ada:reagentRole": "secondaryStandard"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "USGS BHVO-2g",
      "ada:reagentRole": "secondaryStandard"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXsource"
    ],
    "schema:name": {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      },
      "schema:value": "NMNH 111312/444",
      "schema:url": "https://iolite-software.com/"
    },
    "schema:alternateName": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Concord University, Athens, West Virginia, USA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ],
    "schema:geo": {
      "@type": [
        "schema:GeoCoordinates"
      ],
      "schema:latitude": 15.0,
      "schema:longitude": 15.0
    },
    "geosparql:hasGeometry": {
      "@type": [
        "schema:Place"
      ],
      "geosparql:asWKT": {
        "@type": [
          "geosparql:wktLiteral"
        ],
        "@value": "synthetic @value"
      },
      "geosparql:crs": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      }
    }
  },
  "schema:creator": {
    "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
    "@type": [
      "schema:Person"
    ],
    "schema:name": "CU routine tephra glass version 1.0 with 6nA",
    "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      },
      "schema:value": "NMNH 111312/444",
      "schema:url": "https://iolite-software.com/"
    },
    "schema:alternateName": "synthetic schema:alternateName",
    "schema:affiliation": {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "@type": [
        "schema:Organization"
      ],
      "schema:additionalType": [
        "ada:EPMAInstrument",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:alternateName": "synthetic schema:alternateName",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:sameAs": [
        {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        }
      ]
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "synthetic schema:email"
    },
    "schema:sameAs": [
      {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      }
    ]
  },
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15â€“20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {
          "@id": "#rawSignals"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {
          "@id": "#quantifiedConcentrations"
        },
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:valueName": "additionalNotes",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:value": "NMNH 111312/444",
            "schema:url": "https://iolite-software.com/"
          },
          "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
          "schema:termCode": "xenon"
        }
      ],
      "schema:inDefinedTermSet": {
        "@type": [
          "schema:CreativeWork"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:minValue": 1,
      "schema:maxValue": 200,
      "schema:stepValue": 15.0,
      "schema:valuePattern": "synthetic schema:valuePattern",
      "schema:multipleValues": true,
      "ada:fieldScope": "method",
      "ada:category": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "ada:dataType": "string",
      "schema:unitText": "kV",
      "schema:unitCode": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": 15,
      "schema:unitText": "kV",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Current",
      "schema:valueName": "beamCurrent",
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": 6,
      "schema:minValue": 1,
      "schema:maxValue": 200,
      "schema:unitText": "nA",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Diameter",
      "schema:valueName": "beamDiameter",
      "ada:fieldScope": "session",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": false,
      "schema:valueRequired": true,
      "schema:defaultValue": 10,
      "schema:minValue": 0,
      "schema:maxValue": 50,
      "schema:unitText": "um",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "beamDamageMinimization",
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
      },
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Correction Model",
      "schema:valueName": "matrixCorrectionModel",
      "schema:propertyID": [
        "https://vocab.onegeochemistry.org/epma/matrix-correction"
      ],
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
      },
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
      "ada:tier": "M"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "analyte",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "xenon"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "P-10"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "SDD"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Si(Li)"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Other"
            }
          ]
        }
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "TiO2",
        "schema:termCode": "TiO2",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      },
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Al2O3",
        "schema:termCode": "Al2O3",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      },
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Cr2O3",
        "schema:termCode": "Cr2O3",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      }
    ]
  },
  "ada:channelTemplate": {
    "ada:channelColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "channel",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      }
    ],
    "ada:defaultChannels": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ]
  },
  "ada:reportedPropertyTemplate": {
    "ada:reportedPropertyColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "reportedProperty",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      }
    ],
    "ada:defaultReportedProperties": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ]
  },
  "dqv:hasQualityMeasurement": [
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "dqv:value": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "analytical precision (1-sigma)",
      "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "analytical reproducibility",
      "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "oxide production",
      "dqv:value": "ThO/Th ca. 0.7%"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "detection limit method",
      "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:url": "https://iolite-software.com/"
    }
  ],
  "schema:funding": [
    {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:funder": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:alternateName": "synthetic schema:alternateName",
        "schema:affiliation": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
          "@type": [
            "schema:Organization"
          ],
          "schema:additionalType": [
            "ada:EPMAInstrument",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:alternateName": "synthetic schema:alternateName",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "synthetic schema:propertyID",
            "schema:value": "NMNH 111312/444",
            "schema:url": "https://iolite-software.com/"
          },
          "schema:sameAs": [
            {
              "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
            }
          ]
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "synthetic schema:email"
        },
        "schema:sameAs": [
          {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          }
        ]
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "DFG INST 216/1019-1 FUGG no. 665508"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "prov:Plan"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "ada:dataType": "string",
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "schema:value": "NMNH 111312/444"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "dqv": "http://www.w3.org/ns/dqv#",
      "prov": "http://www.w3.org/ns/prov#",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "CU routine tephra glass version 1.0 with 6nA",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
    },
    "schema:value": "NMNH 111312/444",
    "schema:url": "https://iolite-software.com/"
  },
  "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
  "schema:version": "1.0.6",
  "schema:datePublished": "2011-10-20",
  "schema:dateModified": "synthetic schema:dateModified",
  "schema:additionalType": [
    "ada:EPMAInstrument"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "EPMA-WDS",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "LA-ICP-MS",
      "schema:description": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "silicate glass",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    },
    {
      "@id": "#preparedMount"
    },
    {
      "@id": "#rawAnalyses"
    },
    {
      "@id": "#quantifiedResults"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "spinel",
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/materials"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Product",
      "schema:Thing"
    ],
    "schema:name": "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS",
    "schema:hasPart": [
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "Laser Ablation System",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "ESI imageGEO193",
        "schema:description": "193 nm ArF excimer laser ablation system",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Elemental Scientific Lasers (ESI)"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System"
      },
      {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "ICPMS",
          {
            "@id": "https://www.wikidata.org/wiki/Q3099911"
          }
        ],
        "schema:name": "Thermo Fischer iCAP Q",
        "schema:description": "Single-quadrupole ICP-MS",
        "schema:manufacturer": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Thermo Fisher Scientific"
        },
        "@id": "ex:instrument/nxs-BaseClass-NXinstrument/part/ICPMS"
      }
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      {
        "@id": "https://www.wikidata.org/wiki/Q3099911"
      }
    ],
    "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:version": "1.0.6",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "schema:version": "9.6.4",
      "ada:toolRole": "dataReduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA",
      "ada:toolRole": "dataReduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Iolite",
      "schema:version": "4",
      "schema:url": "https://iolite-software.com/",
      "ada:toolRole": "dataReduction"
    }
  ],
  "bios:reagent": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:identifier": {
        "@type": [
          "prov:Plan"
        ],
        "schema:propertyID": "Smithsonian catalog",
        "schema:value": "NMNH 111312/444"
      },
      "schema:termCode": "xenon",
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods",
        "schema:name": "CU routine tephra glass version 1.0 with 6nA"
      },
      "ada:reagentRole": "primaryStandard",
      "schema:citation": {
        "@type": [
          "prov:Plan"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:url": "https://iolite-software.com/"
      }
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Carbon",
      "ada:reagentRole": "coatingMaterial"
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Albite",
      "ada:reagentRole": "primaryStandard"
    },
    {
      "@type": [
        "schema:ChemicalSubstance"
      ],
      "schema:name": "Kaersutite amphibole",
      "ada:reagentRole": "primaryStandard"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Lipari obsidian ID3506",
      "ada:reagentRole": "secondaryStandard"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "USGS BHVO-2g",
      "ada:reagentRole": "secondaryStandard"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXsource"
    ],
    "schema:name": {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
      "schema:termCode": "xenon"
    },
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      },
      "schema:value": "NMNH 111312/444",
      "schema:url": "https://iolite-software.com/"
    },
    "schema:alternateName": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Concord University, Athens, West Virginia, USA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ],
    "schema:geo": {
      "@type": [
        "schema:GeoCoordinates"
      ],
      "schema:latitude": 15.0,
      "schema:longitude": 15.0
    },
    "geosparql:hasGeometry": {
      "@type": [
        "schema:Place"
      ],
      "geosparql:asWKT": {
        "@type": [
          "geosparql:wktLiteral"
        ],
        "@value": "synthetic @value"
      },
      "geosparql:crs": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      }
    }
  },
  "schema:creator": {
    "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
    "@type": [
      "schema:Person"
    ],
    "schema:name": "CU routine tephra glass version 1.0 with 6nA",
    "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      },
      "schema:value": "NMNH 111312/444",
      "schema:url": "https://iolite-software.com/"
    },
    "schema:alternateName": "synthetic schema:alternateName",
    "schema:affiliation": {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "@type": [
        "schema:Organization"
      ],
      "schema:additionalType": [
        "ada:EPMAInstrument",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:alternateName": "synthetic schema:alternateName",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:sameAs": [
        {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        }
      ]
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "synthetic schema:email"
    },
    "schema:sameAs": [
      {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
      }
    ]
  },
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "LA-ICP-MS volcanic glass trace element workflow",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:position": 1,
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:description": "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard).",
        "schema:result": {
          "@id": "#preparedMount"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "ICP-MS tuning and optimization",
        "schema:position": 2,
        "schema:description": "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%).",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "RF Power",
            "schema:valueName": "rfPower",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 1200,
            "schema:unitText": "W",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (He) Flow Rate",
            "schema:valueName": "carrierGasHeFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.9,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Carrier Gas (Ar) Flow Rate",
            "schema:valueName": "carrierGasArFlowRate",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.8,
            "schema:unitText": "L/min",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Signal Smoothing",
            "schema:valueName": "signalSmoothing",
            "ada:fieldScope": "method",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": false,
            "schema:defaultValue": "Glass smoothing device",
            "ada:tier": "R"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Oxide Production (ThO/Th)",
            "schema:valueName": "oxideProduction",
            "ada:fieldScope": "session",
            "ada:category": "ICP-MS Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "ca. 0.7%",
            "ada:tier": "M"
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation calibration",
        "schema:position": 3,
        "schema:description": "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G.",
        "bios:reagent": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 612",
            "schema:description": "Trace Elements in Glass (nominal 50 ppm)",
            "ada:reagentRole": "primaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u00e2\u20ac\u201c429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "NIST SRM 610",
            "schema:description": "Trace Elements in Glass (nominal 500 ppm)",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397\u00e2\u20ac\u201c429."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "ATHO-G",
            "schema:description": "MPI-DING Icelandic rhyolite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          },
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "StHs6/80-G",
            "schema:description": "MPI-DING St. Helens dacite glass",
            "ada:reagentRole": "secondaryStandard",
            "schema:citation": "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)."
          }
        ]
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Laser ablation data acquisition",
        "schema:position": 4,
        "schema:description": "Ablate sample in point mode with 15\u00e2\u20ac\u201c20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device.",
        "schema:object": {
          "@id": "#preparedMount"
        },
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Wavelength",
            "schema:valueName": "laserWavelength",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "193 nm (ArF excimer)",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Width",
            "schema:valueName": "laserSpotWidth",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "15; 20",
            "schema:description": "Spot width in um; multiple values if varied during session.",
            "schema:unitText": "um",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Spot Path Geometry",
            "schema:valueName": "laserSpotPathGeometry",
            "schema:inDefinedTermSet": {
              "@id": "https://vocab.onegeochemistry.org/laicpms/spot-geometries"
            },
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": "point",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Energy",
            "schema:valueName": "laserEnergy",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 0.001,
            "schema:unitText": "mJ",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Laser Pulse Time",
            "schema:valueName": "laserPulseTime",
            "ada:fieldScope": "method",
            "ada:category": "Laser Conditions",
            "ada:dataType": "string",
            "schema:readonlyValue": true,
            "schema:valueRequired": true,
            "schema:defaultValue": "7 ns",
            "ada:tier": "M"
          },
          {
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:name": "Repetition Rate",
            "schema:valueName": "repetitionRate",
            "ada:fieldScope": "session",
            "ada:category": "Laser Conditions",
            "ada:dataType": "number",
            "schema:readonlyValue": false,
            "schema:valueRequired": true,
            "schema:defaultValue": 5,
            "schema:unitText": "Hz",
            "ada:tier": "M"
          }
        ],
        "schema:result": {
          "@id": "#rawSignals"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:position": 5,
        "schema:description": "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012).",
        "schema:object": {
          "@id": "#rawSignals"
        },
        "bios:computationalTool": [
          {
            "@type": [
              "schema:SoftwareApplication"
            ],
            "schema:name": "Iolite",
            "schema:version": "4",
            "ada:toolRole": "dataReduction"
          }
        ],
        "schema:result": {
          "@id": "#quantifiedConcentrations"
        }
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Quality control",
        "schema:position": 6,
        "schema:description": "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session.",
        "schema:object": {
          "@id": "#quantifiedConcentrations"
        },
        "dqv:hasQualityMeasurement": [
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "oxide production",
            "dqv:value": "ThO/Th ca. 0.7%"
          },
          {
            "@type": [
              "dqv:QualityMeasurement"
            ],
            "dqv:isMeasurementOf": "detection limit method",
            "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
          }
        ]
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:valueName": "additionalNotes",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:propertyID": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:value": "NMNH 111312/444",
            "schema:url": "https://iolite-software.com/"
          },
          "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
          "schema:termCode": "xenon"
        }
      ],
      "schema:inDefinedTermSet": {
        "@type": [
          "schema:CreativeWork"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:minValue": 1,
      "schema:maxValue": 200,
      "schema:stepValue": 15.0,
      "schema:valuePattern": "synthetic schema:valuePattern",
      "schema:multipleValues": true,
      "ada:fieldScope": "method",
      "ada:category": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "ada:dataType": "string",
      "schema:unitText": "kV",
      "schema:unitCode": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": 15,
      "schema:unitText": "kV",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Current",
      "schema:valueName": "beamCurrent",
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": 6,
      "schema:minValue": 1,
      "schema:maxValue": 200,
      "schema:unitText": "nA",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Diameter",
      "schema:valueName": "beamDiameter",
      "ada:fieldScope": "session",
      "ada:category": "Beam Conditions",
      "ada:dataType": "number",
      "schema:readonlyValue": false,
      "schema:valueRequired": true,
      "schema:defaultValue": 10,
      "schema:minValue": 0,
      "schema:maxValue": 50,
      "schema:unitText": "um",
      "ada:tier": "M"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "beamDamageMinimization",
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/beam-damage-methods"
      },
      "ada:fieldScope": "method",
      "ada:category": "Beam Conditions",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": false,
      "schema:defaultValue": "Si, Al, Na acquired first; 6-7 time intervals for TDI correction",
      "ada:tier": "R"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Correction Model",
      "schema:valueName": "matrixCorrectionModel",
      "schema:propertyID": [
        "https://vocab.onegeochemistry.org/epma/matrix-correction"
      ],
      "schema:inDefinedTermSet": {
        "@id": "https://vocab.onegeochemistry.org/epma/matrix-correction-models"
      },
      "ada:fieldScope": "method",
      "ada:category": "Data Processing",
      "ada:dataType": "string",
      "schema:readonlyValue": true,
      "schema:valueRequired": true,
      "schema:defaultValue": "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs",
      "ada:tier": "M"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "analyte",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Beam Current (nA)",
        "schema:valueName": "beamCurrent",
        "ada:dataType": "number",
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:unitText": "nA",
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Spectrometer",
        "schema:valueName": "spectrometer",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "sequence",
        "ada:dataType": "integer",
        "schema:valueRequired": false,
        "ada:tier": "R"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "diffractingCrystal",
        "schema:inDefinedTermSet": {
          "@id": "https://vocab.onegeochemistry.org/epma/diffracting-crystals"
        },
        "ada:dataType": "string",
        "schema:valueRequired": true,
        "ada:tier": "M"
      },
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detector Type",
        "schema:valueName": "detectorType",
        "ada:dataType": "string",
        "schema:valueRequired": false,
        "ada:tier": "R",
        "schema:inDefinedTermSet": {
          "@type": "schema:DefinedTermSet",
          "schema:hasDefinedTerm": [
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "xenon"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "P-10"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "SDD"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Si(Li)"
            },
            {
              "@type": "schema:DefinedTerm",
              "schema:termCode": "Other"
            }
          ]
        }
      }
    ],
    "ada:defaultAnalytes": [
      "SiO2",
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "TiO2",
        "schema:termCode": "TiO2",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      },
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Al2O3",
        "schema:termCode": "Al2O3",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      },
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Cr2O3",
        "schema:termCode": "Cr2O3",
        "schema:inDefinedTermSet": "https://w3id.org/ada/vocab/analyte"
      }
    ]
  },
  "ada:channelTemplate": {
    "ada:channelColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "channel",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      }
    ],
    "ada:defaultChannels": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ]
  },
  "ada:reportedPropertyTemplate": {
    "ada:reportedPropertyColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:valueName": "reportedProperty",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:propertyID": [
          {
            "@type": [
              "schema:DefinedTerm"
            ],
            "schema:name": "CU routine tephra glass version 1.0 with 6nA",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:value": "NMNH 111312/444",
              "schema:url": "https://iolite-software.com/"
            },
            "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
            "schema:termCode": "xenon"
          }
        ],
        "schema:inDefinedTermSet": {
          "@type": [
            "schema:CreativeWork"
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "schema:minValue": 1,
        "schema:maxValue": 200,
        "schema:valuePattern": "synthetic schema:valuePattern",
        "ada:dataType": "string",
        "schema:unitText": "kV",
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      }
    ],
    "ada:defaultReportedProperties": [
      {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    ]
  },
  "dqv:hasQualityMeasurement": [
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      },
      "dqv:value": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "CU routine tephra glass version 1.0 with 6nA",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:inDefinedTermSet": "https://vocab.onegeochemistry.org/techniques",
        "schema:termCode": "xenon"
      }
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "analytical precision (1-sigma)",
      "dqv:value": "Reported per element on secondary standards; see relatedLink publications"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "analytical reproducibility",
      "dqv:value": "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "oxide production",
      "dqv:value": "ThO/Th ca. 0.7%"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "detection limit method",
      "dqv:value": "Sample-individual LOD per Pettke et al. (2012)"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:url": "https://iolite-software.com/"
    }
  ],
  "schema:funding": [
    {
      "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
        },
        "schema:value": "NMNH 111312/444",
        "schema:url": "https://iolite-software.com/"
      },
      "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "schema:funder": {
        "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)",
        "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          },
          "schema:value": "NMNH 111312/444",
          "schema:url": "https://iolite-software.com/"
        },
        "schema:alternateName": "synthetic schema:alternateName",
        "schema:affiliation": {
          "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6",
          "@type": [
            "schema:Organization"
          ],
          "schema:additionalType": [
            "ada:EPMAInstrument",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "CU routine tephra glass version 1.0 with 6nA",
          "schema:alternateName": "synthetic schema:alternateName",
          "schema:description": "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "synthetic schema:propertyID",
            "schema:value": "NMNH 111312/444",
            "schema:url": "https://iolite-software.com/"
          },
          "schema:sameAs": [
            {
              "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
            }
          ]
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "synthetic schema:email"
        },
        "schema:sameAs": [
          {
            "@id": "https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6"
          }
        ]
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:value": "DFG INST 216/1019-1 FUGG no. 665508"
      },
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Deutsche Forschungsgemeinschaft (DFG)"
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "prov:Plan"
      ],
      "schema:name": "CU routine tephra glass version 1.0 with 6nA",
      "ada:dataType": "string",
      "schema:defaultValue": "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization",
      "schema:value": "NMNH 111312/444"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ns1: <geosparql:> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/instrument/nxs-BaseClass-NXinstrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "nxs:BaseClass/NXinstrument" ;
    schema1:hasPart <https://example.org/instrument/nxs-BaseClass-NXinstrument/part/ICPMS>,
        <https://example.org/instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System> ;
    schema1:name "ESI imageGEO193 laser + Thermo Fischer iCAP Q ICP-MS" .

<https://example.org/instrument/nxs-BaseClass-NXinstrument/part/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:description "Single-quadrupole ICP-MS" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:name "Thermo Fischer iCAP Q" .

<https://example.org/instrument/nxs-BaseClass-NXinstrument/part/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:description "193 nm ArF excimer laser ablation system" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Elemental Scientific Lasers (ESI)" ] ;
    schema1:name "ESI imageGEO193" .

<https://vocab.onegeochemistry.org/epma/beam-damage-methods> schema1:name "CU routine tephra glass version 1.0 with 6nA" .

<https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> a cdi:Activity,
        schema1:Action,
        schema1:DefinedTerm,
        schema1:MonetaryGrant,
        schema1:Organization,
        schema1:Person,
        schema1:SoftwareApplication,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "LA-ICP-MS volcanic glass trace element workflow" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Calibrate using NIST612 as primary reference material. Verify with secondary standards NIST610, ATHO-G, and StHs6/80-G." ;
                    schema1:name "Laser ablation calibration" ;
                    schema1:position 3 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429." ;
                            schema1:description "Trace Elements in Glass (nominal 500 ppm)" ;
                            schema1:name "NIST SRM 610" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2011), Geostandards and Geoanalytical Research, 35(4): 397â€“429." ;
                            schema1:description "Trace Elements in Glass (nominal 50 ppm)" ;
                            schema1:name "NIST SRM 612" ;
                            ada:reagentRole "primaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING St. Helens dacite glass" ;
                            schema1:name "StHs6/80-G" ;
                            ada:reagentRole "secondaryStandard" ],
                        [ a schema1:DefinedTerm ;
                            schema1:citation "Jochum et al. (2006), Geochemistry Geophysics Geosystems, 7(2)." ;
                            schema1:description "MPI-DING Icelandic rhyolite glass" ;
                            schema1:name "ATHO-G" ;
                            ada:reagentRole "secondaryStandard" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Volcanic glass shards or tephra grains mounted in epoxy, polished to expose flat surfaces, and carbon coated for prior EPMA analysis of major elements (Si used as internal standard)." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    schema1:result <file:///github/workspace/#preparedMount> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Process raw time-resolved signals in Iolite 4. Background subtraction using 30 s pre-ablation gas blank. Normalize to NIST612 with Si as internal standard. Calculate concentrations and sample-individual detection limits per Pettke et al. (2012)." ;
                    schema1:name "Data reduction" ;
                    schema1:object <file:///github/workspace/#rawSignals> ;
                    schema1:position 5 ;
                    schema1:result <file:///github/workspace/#quantifiedConcentrations> ;
                    bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Iolite" ;
                            schema1:version "4" ;
                            ada:toolRole "dataReduction" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "ca. 0.7%" ;
                            schema1:name "Oxide Production (ThO/Th)" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "oxideProduction" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 8e-01 ;
                            schema1:name "Carrier Gas (Ar) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasArFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "Glass smoothing device" ;
                            schema1:name "Signal Smoothing" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "signalSmoothing" ;
                            schema1:valueRequired false ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "R" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1200 ;
                            schema1:name "RF Power" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "W" ;
                            schema1:valueName "rfPower" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 9e-01 ;
                            schema1:name "Carrier Gas (He) Flow Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "L/min" ;
                            schema1:valueName "carrierGasHeFlowRate" ;
                            schema1:valueRequired true ;
                            ada:category "ICP-MS Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ;
                    schema1:description "Tune ICP-MS using auto-tune function on line scan of NIST612. Optimize for maximum sensitivity while minimizing oxide production (ThO/Th ~0.7%)." ;
                    schema1:name "ICP-MS tuning and optimization" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "point" ;
                            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/laicpms/spot-geometries> ;
                            schema1:name "Laser Spot Path Geometry" ;
                            schema1:readonlyValue false ;
                            schema1:valueName "laserSpotPathGeometry" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 1e-03 ;
                            schema1:name "Laser Energy" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "mJ" ;
                            schema1:valueName "laserEnergy" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "193 nm (ArF excimer)" ;
                            schema1:name "Laser Wavelength" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserWavelength" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "15; 20" ;
                            schema1:description "Spot width in um; multiple values if varied during session." ;
                            schema1:name "Laser Spot Width" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "um" ;
                            schema1:valueName "laserSpotWidth" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue "7 ns" ;
                            schema1:name "Laser Pulse Time" ;
                            schema1:readonlyValue true ;
                            schema1:valueName "laserPulseTime" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "string" ;
                            ada:fieldScope "method" ;
                            ada:tier "M" ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:defaultValue 5 ;
                            schema1:name "Repetition Rate" ;
                            schema1:readonlyValue false ;
                            schema1:unitText "Hz" ;
                            schema1:valueName "repetitionRate" ;
                            schema1:valueRequired true ;
                            ada:category "Laser Conditions" ;
                            ada:dataType "number" ;
                            ada:fieldScope "session" ;
                            ada:tier "M" ] ;
                    schema1:description "Ablate sample in point mode with 15â€“20 um spot. 30 s gas blank followed by 40 s ablation. Helium carrier gas transports aerosol to ICP-MS via signal smoothing device." ;
                    schema1:name "Laser ablation data acquisition" ;
                    schema1:object <file:///github/workspace/#preparedMount> ;
                    schema1:position 4 ;
                    schema1:result <file:///github/workspace/#rawSignals> ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:description "Secondary standards (NIST610, ATHO-G, StHs6/80-G) analysed interspersed with unknowns in ratio 2 calibration / 4 QC / 15 unknowns. Drift monitored via repeated NIST612 analyses throughout session." ;
                    schema1:name "Quality control" ;
                    schema1:object <file:///github/workspace/#quantifiedConcentrations> ;
                    schema1:position 6 ;
                    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "detection limit method" ;
                            dqv:value "Sample-individual LOD per Pettke et al. (2012)" ],
                        [ a dqv:QualityMeasurement ;
                            dqv:isMeasurementOf "oxide production" ;
                            dqv:value "ThO/Th ca. 0.7%" ] ] ] ;
    schema1:additionalProperty [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
            schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
            schema1:inDefinedTermSet [ a schema1:CreativeWork ;
                    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:url "https://iolite-software.com/" ] ;
            schema1:maxValue 200 ;
            schema1:minValue 1 ;
            schema1:multipleValues true ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:propertyID [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ;
            schema1:readonlyValue true ;
            schema1:stepValue 1.5e+01 ;
            schema1:unitCode [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ;
            schema1:unitText "kV" ;
            schema1:valueName "additionalNotes" ;
            schema1:valuePattern "synthetic schema:valuePattern" ;
            schema1:valueRequired false ;
            ada:category [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ;
            ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue 10 ;
            schema1:maxValue 50 ;
            schema1:minValue 0 ;
            schema1:name "Beam Diameter" ;
            schema1:readonlyValue false ;
            schema1:unitText "um" ;
            schema1:valueName "beamDiameter" ;
            schema1:valueRequired true ;
            ada:category "Beam Conditions" ;
            ada:dataType "number" ;
            ada:fieldScope "session" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Si, Al, Na acquired first; 6-7 time intervals for TDI correction" ;
            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-damage-methods> ;
            schema1:name "Beam Damage Minimization" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDamageMinimization" ;
            schema1:valueRequired false ;
            ada:category "Beam Conditions" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue 15 ;
            schema1:name "Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:unitText "kV" ;
            schema1:valueName "acceleratingVoltage" ;
            schema1:valueRequired true ;
            ada:category "Beam Conditions" ;
            ada:dataType "number" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue 6 ;
            schema1:maxValue 200 ;
            schema1:minValue 1 ;
            schema1:name "Beam Current" ;
            schema1:readonlyValue true ;
            schema1:unitText "nA" ;
            schema1:valueName "beamCurrent" ;
            schema1:valueRequired true ;
            ada:category "Beam Conditions" ;
            ada:dataType "number" ;
            ada:fieldScope "method" ;
            ada:tier "M" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Armstrong/Packwood-Brown 1981 MAS Phi(pz) with CITZMU MACs" ;
            schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/matrix-correction-models> ;
            schema1:name "Matrix Correction Model" ;
            schema1:propertyID "https://vocab.onegeochemistry.org/epma/matrix-correction" ;
            schema1:readonlyValue true ;
            schema1:valueName "matrixCorrectionModel" ;
            schema1:valueRequired true ;
            ada:category "Data Processing" ;
            ada:dataType "string" ;
            ada:fieldScope "method" ;
            ada:tier "M" ] ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ada:EPMAInstrument" ;
    schema1:affiliation <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    schema1:alternateName "synthetic schema:alternateName" ;
    schema1:citation [ a prov:Plan ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:url "https://iolite-software.com/" ] ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "synthetic schema:email" ],
        [ a schema1:ContactPoint ;
            schema1:email "synthetic schema:email" ] ;
    schema1:creator <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    schema1:dateModified "synthetic schema:dateModified" ;
    schema1:datePublished "2011-10-20" ;
    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
    schema1:funder <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:name "Deutsche Forschungsgemeinschaft (DFG)" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:value "DFG INST 216/1019-1 FUGG no. 665508" ] ],
        <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    schema1:identifier [ a prov:Plan ;
            schema1:propertyID "Smithsonian catalog" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID "synthetic schema:propertyID" ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
            schema1:url "https://iolite-software.com/" ;
            schema1:value "NMNH 111312/444" ] ;
    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/beam-damage-methods> ;
    schema1:instrument <https://example.org/instrument/nxs-BaseClass-NXinstrument> ;
    schema1:location [ a schema1:Place ;
            ns1:hasGeometry [ a schema1:Place ;
                    ns1:asWKT "synthetic @value"^^<['geosparql:wktLiteral']> ;
                    ns1:crs <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ] ;
            schema1:additionalType "nxs:BaseClass/NXsource" ;
            schema1:alternateName [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "Concord University, Athens, West Virginia, USA" ;
                    schema1:termCode "xenon" ] ;
            schema1:geo [ a schema1:GeoCoordinates ;
                    schema1:latitude 1.5e+01 ;
                    schema1:longitude 1.5e+01 ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                    schema1:url "https://iolite-software.com/" ;
                    schema1:value "NMNH 111312/444" ] ;
            schema1:name [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:termCode "xenon" ] ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                    schema1:url "https://iolite-software.com/" ;
                    schema1:value "NMNH 111312/444" ] ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:termCode "xenon" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "EPMA-WDS" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "LA-ICP-MS" ] ;
    schema1:name "CU routine tephra glass version 1.0 with 6nA",
        "Deutsche Forschungsgemeinschaft (DFG)" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                    schema1:url "https://iolite-software.com/" ;
                    schema1:value "NMNH 111312/444" ] ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:termCode "xenon" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "silicate glass" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/materials" ;
            schema1:name "spinel" ],
        <file:///github/workspace/#preparedMount>,
        <file:///github/workspace/#quantifiedResults>,
        <file:///github/workspace/#rawAnalyses> ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:url "https://iolite-software.com/" ] ;
    schema1:sameAs <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    schema1:termCode "xenon" ;
    schema1:url "https://iolite-software.com/" ;
    schema1:variableMeasured [ a prov:Plan ;
            schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
            schema1:value "NMNH 111312/444" ;
            ada:dataType "string" ] ;
    schema1:version "1.0.6" ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ;
            dqv:value [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "oxide production" ;
            dqv:value "ThO/Th ca. 0.7%" ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "analytical precision (1-sigma)" ;
            dqv:value "Reported per element on secondary standards; see relatedLink publications" ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "analytical reproducibility" ;
            dqv:value "Davis et al. (2017) report reproducibility on spinels PS211, PS212, OC231350, KLB8304" ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "detection limit method" ;
            dqv:value "Sample-individual LOD per Pettke et al. (2012)" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "Beam Current (nA)" ;
                    schema1:unitText "nA" ;
                    schema1:valueName "beamCurrent" ;
                    schema1:valueRequired true ;
                    ada:dataType "number" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet <https://vocab.onegeochemistry.org/epma/diffracting-crystals> ;
                    schema1:name "Diffracting Crystal" ;
                    schema1:valueName "diffractingCrystal" ;
                    schema1:valueRequired true ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Spectrometer" ;
                    schema1:valueName "spectrometer" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:inDefinedTermSet [ a schema1:DefinedTermSet ;
                            schema1:hasDefinedTerm [ a schema1:DefinedTerm ;
                                    schema1:termCode "Si(Li)" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "SDD" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "Other" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "xenon" ],
                                [ a schema1:DefinedTerm ;
                                    schema1:termCode "P-10" ] ] ;
                    schema1:name "Detector Type" ;
                    schema1:valueName "detectorType" ;
                    schema1:valueRequired false ;
                    ada:dataType "string" ;
                    ada:tier "R" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
                    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                    schema1:inDefinedTermSet [ a schema1:CreativeWork ;
                            schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:url "https://iolite-software.com/" ] ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:propertyID [ a schema1:DefinedTerm ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:url "https://iolite-software.com/" ;
                                    schema1:value "NMNH 111312/444" ] ;
                            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:termCode "xenon" ] ;
                    schema1:readonlyValue true ;
                    schema1:unitText "kV" ;
                    schema1:valueName "analyte" ;
                    schema1:valuePattern "synthetic schema:valuePattern" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                [ a schema1:PropertyValueSpecification ;
                    schema1:name "Sequence" ;
                    schema1:valueName "sequence" ;
                    schema1:valueRequired false ;
                    ada:dataType "integer" ;
                    ada:tier "R" ] ;
            ada:defaultAnalytes [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://w3id.org/ada/vocab/analyte" ;
                    schema1:name "TiO2" ;
                    schema1:termCode "TiO2" ],
                [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://w3id.org/ada/vocab/analyte" ;
                    schema1:name "Al2O3" ;
                    schema1:termCode "Al2O3" ],
                [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://w3id.org/ada/vocab/analyte" ;
                    schema1:name "Cr2O3" ;
                    schema1:termCode "Cr2O3" ],
                "SiO2" ] ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
                    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                    schema1:inDefinedTermSet [ a schema1:CreativeWork ;
                            schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:url "https://iolite-software.com/" ] ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:propertyID [ a schema1:DefinedTerm ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:url "https://iolite-software.com/" ;
                                    schema1:value "NMNH 111312/444" ] ;
                            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:termCode "xenon" ] ;
                    schema1:readonlyValue true ;
                    schema1:unitText "kV" ;
                    schema1:valueName "channel" ;
                    schema1:valuePattern "synthetic schema:valuePattern" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ;
            ada:defaultChannels [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ] ;
    ada:reagentRole "primaryStandard" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
                            schema1:url "https://iolite-software.com/" ;
                            schema1:value "NMNH 111312/444" ] ;
                    schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:termCode "xenon" ] ;
            ada:reportedPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:defaultValue "Water by difference included in x-ray matrix corrections for improved accuracy on hydrated glasses; offline multi-standard blank correction; offline standards-based normalization" ;
                    schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                    schema1:inDefinedTermSet [ a schema1:CreativeWork ;
                            schema1:description "4 WDS spectrometers: #1 PET/xenon, #2 RAP/P-10, #3 LIF/xenon, #4 TAP/P-10; flow detectors with polypropylene windows" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:url "https://iolite-software.com/" ] ;
                    schema1:maxValue 200 ;
                    schema1:minValue 1 ;
                    schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                    schema1:propertyID [ a schema1:DefinedTerm ;
                            schema1:identifier [ a schema1:PropertyValue ;
                                    schema1:url "https://iolite-software.com/" ;
                                    schema1:value "NMNH 111312/444" ] ;
                            schema1:inDefinedTermSet "https://vocab.onegeochemistry.org/techniques" ;
                            schema1:name "CU routine tephra glass version 1.0 with 6nA" ;
                            schema1:termCode "xenon" ] ;
                    schema1:readonlyValue true ;
                    schema1:unitText "kV" ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valuePattern "synthetic schema:valuePattern" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:toolRole "acquisition" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "dataReduction" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            schema1:version "9.6.4" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            schema1:version "9.6.4" ;
            ada:toolRole "dataReduction" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Iolite" ;
            schema1:url "https://iolite-software.com/" ;
            schema1:version "4" ;
            ada:toolRole "dataReduction" ],
        <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> ;
    bios:reagent [ a schema1:ChemicalSubstance ;
            schema1:name "Carbon" ;
            ada:reagentRole "coatingMaterial" ],
        [ a schema1:ChemicalSubstance ;
            schema1:name "Albite" ;
            ada:reagentRole "primaryStandard" ],
        [ a schema1:ChemicalSubstance ;
            schema1:name "Kaersutite amphibole" ;
            ada:reagentRole "primaryStandard" ],
        [ a schema1:DefinedTerm ;
            schema1:name "Lipari obsidian ID3506" ;
            ada:reagentRole "secondaryStandard" ],
        [ a schema1:DefinedTerm ;
            schema1:name "USGS BHVO-2g" ;
            ada:reagentRole "secondaryStandard" ],
        <https://registry.onegeochemistry.org/methods/concord-glass-v1-0-6> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Technique-Aligned Protocol Profile (TAPP) Definition v3
description: "A registered Technique-Aligned Protocol Profile (TAPP) definition modeled
  as a PLAN \u2014 prov:Plan / bios:LabProtocol (also cdi:Activity + schema:Action
  for the DDI-CDI process/action description). It is a reusable procedure that prescribes
  an analysis; the analysis OCCURRENCE is the prov:Activity in adaProduct.prov:wasGeneratedBy,
  which references this plan via prov:used. Because the TAPP is a plan, its instrument
  / bios:computationalTool / bios:reagent are directly-specified resources (not prov:used
  entities). The TAPP identity (name, technique, instrument, location) lives at the
  top level. The standard workflow is encoded in schema:actionProcess as a schema:HowTo
  containing an ordered sequence of cdi:Activity + schema:Action steps (sample preparation,
  calibration, acquisition, data processing, quality control). Each workflow step
  carries its own parameters, reagents, and instruments. TAPP-level parameters that
  apply across all steps remain at the top level in schema:additionalProperty. Integrates
  Bioschemas vocabulary for computational tools and reagents, DDI-CDI for activity
  sequence, and dqv:hasQualityMeasurement for quality metrics."
type: object
properties:
  '@context':
    type: object
    description: JSON-LD context declaring the namespace prefixes used in a method
      definition. Required for the document to be a valid JSON-LD instance. Bound
      prefixes must include schema (always), cdi (DDI-CDI), and ada (ADA vocabulary).
      Additional prefixes (bios, dqv, prov, skos) are recommended when those vocabularies
      are used in the body of the definition.
    properties:
      schema:
        const: http://schema.org/
      ada:
        const: https://ada.astromat.org/metadata/
      cdi:
        const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
      bios:
        const: https://bioschemas.org/
      dqv:
        const: http://www.w3.org/ns/dqv#
      prov:
        const: http://www.w3.org/ns/prov#
      skos:
        const: http://www.w3.org/2004/02/skos/core#
    required:
    - schema
    - ada
    - cdi
  '@id':
    type: string
    description: Persistent URI for this TAPP definition in the registry.
  '@type':
    type: array
    items:
      type: string
    minItems: 5
    allOf:
    - contains:
        const: prov:Plan
    - contains:
        const: cdi:Activity
    - contains:
        const: schema:Action
    - contains:
        const: ada:TAPPDefinition
    - contains:
        const: bios:LabProtocol
    description: "Must include prov:Plan, cdi:Activity, schema:Action, ada:TAPPDefinition,
      and bios:LabProtocol. The TAPP is a PLAN (prov:Plan / bios:LabProtocol) \u2014
      a reusable procedure description that prescribes the analysis, NOT the analysis
      occurrence (that is the prov:Activity in adaProduct.prov:wasGeneratedBy, which
      references this plan via prov:used). As a plan, its instrument / bios:computationalTool
      / bios:reagent are directly-specified resources (bios:LabProtocol convention),
      not prov:used entities."
  schema:name:
    type: string
    title: Method Name
    description: Short descriptive name with version (e.g. "JEOL-8530F WDS Major Element
      Glass v2.1").
    x-jsonld-id: http://schema.org/name
  schema:identifier:
    description: DOI or other persistent ID for this method definition.
    anyOf:
    - type: string
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
    x-jsonld-id: http://schema.org/identifier
  schema:description:
    type: string
    description: Human-readable summary of the method, may be auto-generated from
      constant parameters at registration time.
    x-jsonld-id: http://schema.org/description
  schema:version:
    type: string
    description: Semantic version string (e.g. "2.1.0").
    x-jsonld-id: http://schema.org/version
  schema:datePublished:
    title: Method Start Date
    type: string
    description: ISO 8601 date when this method configuration was first used.
    x-jsonld-id: http://schema.org/datePublished
  schema:dateModified:
    type: string
    description: ISO 8601 date of last update to this definition.
    x-jsonld-id: http://schema.org/dateModified
  schema:additionalType:
    description: Further classification of the activity type (e.g. schema:CreateAction
      for a production method).
    type: array
    items:
      type: string
    x-jsonld-id: http://schema.org/additionalType
  schema:measurementTechnique:
    title: Technique
    description: The analytical technique this method implements. Must be a DefinedTerm
      from a controlled vocabulary of techniques.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
    x-jsonld-id: http://schema.org/measurementTechnique
  schema:object:
    description: Target material(s) this method is designed to analyse (e.g. silicate
      glass, olivine, spinel), modeled as DefinedTerm(s) or free text; and/or the
      sample(s) analysed, modeled as iSamples material-sample objects (the "Samples
      analyzed" shape carried over from geochemProduct).
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DefinedTerm'
      - type: string
      - type: object
        description: Samples analyzed
        properties:
          '@type':
            type: array
            items:
              type: string
            allOf:
            - contains:
                const: schema:Thing
            - contains:
                const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
            minItems: 2
          schema:additionalType:
            type: array
            items:
              type: string
            x-jsonld-id: http://schema.org/additionalType
          schema:identifier:
            type: array
            items:
              type: string
            x-jsonld-id: http://schema.org/identifier
          schema:name:
            description: Sample name/identifier as used in the lab.
            type: string
            x-jsonld-id: http://schema.org/name
          schema:additionalProperty:
            description: Per-sample PropertyValue entries (e.g. analysis location);
              technique profiles constrain these.
            type: array
            items:
              type: object
            x-jsonld-id: http://schema.org/additionalProperty
    x-jsonld-id: http://schema.org/object
  schema:instrument:
    description: 'Instrument specification(s) for this method: a single instrument
      object, or an array of instruments when the method uses more than one (e.g.
      LA-ICP-MS = a laser ablation system plus the ICP-MS). Use schema:hasPart for
      instrument sub-components (spectrometers, detectors, ICP source, sample introduction
      system). Path-driven technique overlays select a specific instrument by schema:additionalType
      and constrain its sub-component tree.'
    anyOf:
    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
    - type: array
      items:
        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
    x-jsonld-id: http://schema.org/instrument
  bios:computationalTool:
    description: Software tools used for data acquisition, reduction, and processing.
      Each tool carries name, version, and optional URL.
    type: array
    items:
      $ref: '#/$defs/ComputationalTool'
    x-jsonld-id: https://bioschemas.org/computationalTool
  bios:reagent:
    description: Reference materials, calibration standards, and chemical reagents
      used across this method. Reagents specific to a single workflow step should
      be placed on that step instead.
    type: array
    items:
      $ref: '#/$defs/Reagent'
    x-jsonld-id: https://bioschemas.org/reagent
  schema:location:
    title: Laboratory
    description: Laboratory where this method was developed. Optional; omit for methods
      that are instrument-generic.
    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/schema.yaml
    x-jsonld-id: http://schema.org/location
  schema:creator:
    title: Method Author
    description: Person or organisation who defined or is responsible for this method.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
    - type: object
      required:
      - '@id'
      additionalProperties: false
      properties:
        '@id':
          type: string
    x-jsonld-id: http://schema.org/creator
  schema:actionProcess:
    description: The standard workflow for this method, expressed as a schema:HowTo
      containing an ordered sequence of workflow steps. Each step is a cdi:Activity
      + schema:Action describing a distinct phase (sample preparation, calibration,
      acquisition, data processing, quality control). Steps carry their own parameters,
      reagents, instruments, and sub-steps.
    $ref: '#/$defs/WorkflowHowTo'
    x-jsonld-id: http://schema.org/actionProcess
  schema:additionalProperty:
    type: array
    description: Method-level Advanced-protocol parameters that apply across all workflow
      steps. Editable parameters are schema:PropertyValueSpecification entries (a
      default the analyst may override); read-only parameters are schema:PropertyValue
      entries carrying the fixed protocol value. Replaces the former ada:methodParameters.
      Technique TAPP profiles constrain the allowed entries via $refs to the parameterTemplates
      (specifications) and parameterValues (values) registries. Step-specific parameters
      should be placed on the appropriate workflow step instead.
    items:
      anyOf:
      - $ref: '#/$defs/MethodParameter'
      - $ref: '#/$defs/MethodParameterValue'
    x-jsonld-id: http://schema.org/additionalProperty
  ada:analyteTemplate:
    description: Template for per-analyte (element-specific) parameters. Defines the
      columns that appear in the element table, each with scope, datatype, and constraints.
      Analyte rows become schema:variableMeasured entries in metadata records. Typically
      associated with the acquisition workflow step.
    type: object
    properties:
      ada:analyteColumns:
        type: array
        description: Columns of the per-analyte parameter table. Must include exactly
          one column with schema:valueName "analyte" that identifies the analyzed
          constituent named in each row.
        minItems: 1
        items:
          $ref: '#/$defs/AnalyteColumn'
        contains:
          $ref: '#/$defs/AnalyteIdentifierColumn'
        maxContains: 1
        x-jsonld-id: https://ada.astromat.org/metadata/analyteColumns
      ada:defaultAnalytes:
        type: array
        description: "The analytes (analyzed constituents) this method targets by
          default \u2014 the ROWS of the per-analyte table. Each is a bare string
          or a schema:DefinedTerm identifying the analyte; per-analyte column VALUES
          live in the analysis record, not here."
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/DefinedTerm'
        x-jsonld-id: https://ada.astromat.org/metadata/defaultAnalytes
    required:
    - ada:analyteColumns
    x-jsonld-id: https://ada.astromat.org/metadata/analyteTemplate
  ada:channelTemplate:
    description: Template for per-channel parameters, a channel being an instrument
      selection position (a mass, a Faraday cup, an energy-loss edge, an X-ray line).
      Declares the channel domain and the columns that repeat over it. The domain
      is declared by different fields per technique -- Monitored Isotopes for ICP-MS,
      Collector Configuration for MC-ICP-MS, EELS Edges for TEM.
    type: object
    properties:
      ada:channelColumns:
        type: array
        description: Columns of the per-channel parameter table. Must include exactly
          one column with schema:valueName "channel" identifying the selection position
          named in each row.
        minItems: 1
        items:
          $ref: '#/$defs/ChannelColumn'
        contains:
          $ref: '#/$defs/ChannelIdentifierColumn'
        maxContains: 1
        x-jsonld-id: https://ada.astromat.org/metadata/channelColumns
      ada:defaultChannels:
        type: array
        description: "The channels this procedure defines by default \u2014 the ROWS
          of the channel table. Each is a bare string or a schema:DefinedTerm identifying
          the channel; per-channel column VALUES live in the analysis record's collectorConfiguration
          array, not here."
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/DefinedTerm'
        x-jsonld-id: https://ada.astromat.org/metadata/defaultChannels
    required:
    - ada:channelColumns
    x-jsonld-id: https://ada.astromat.org/metadata/channelTemplate
  ada:reportedPropertyTemplate:
    description: 'Template for the variables this procedure REPORTS and their units,
      as distinct from ada:analyteTemplate which records what was acquired. Declares
      the reported-property domain and the columns that repeat over it. It also states
      the procedure''s scope boundary: a derived quantity inside this list is in scope,
      anything beyond it belongs to a separate, coupled procedure.'
    type: object
    properties:
      ada:reportedPropertyColumns:
        type: array
        description: Columns of the reported-property table. Must include exactly
          one column with schema:valueName "reportedProperty" identifying the reported
          variable named in each row.
        minItems: 1
        items:
          $ref: '#/$defs/ReportedPropertyColumn'
        contains:
          $ref: '#/$defs/ReportedPropertyIdentifierColumn'
        maxContains: 1
        x-jsonld-id: https://ada.astromat.org/metadata/reportedPropertyColumns
      ada:defaultReportedProperties:
        type: array
        description: "The reported properties this procedure defines by default \u2014
          the ROWS of the reported- property table. Each is a bare string or a schema:DefinedTerm
          identifying the property; per-property column VALUES live in the analysis
          record, not here."
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/DefinedTerm'
        x-jsonld-id: https://ada.astromat.org/metadata/defaultReportedProperties
    required:
    - ada:reportedPropertyColumns
    x-jsonld-id: https://ada.astromat.org/metadata/reportedPropertyTemplate
  dqv:hasQualityMeasurement:
    description: Quality measurements that characterize the method's expected performance
      (e.g. analytical precision, accuracy, counting statistics error). Uses the CDIF
      qualityMeasure building block.
    type: array
    items:
      $ref: '#/$defs/QualityMeasure'
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMeasurement
  schema:relatedLink:
    title: Method References
    type: array
    description: Publications, Zenodo records, or other references reports describing
      or evaluating this method.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
    x-jsonld-id: http://schema.org/relatedLink
  schema:funding:
    title: Funding Source
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.yaml
    x-jsonld-id: http://schema.org/funding
  schema:variableMeasured:
    title: Reported Variables
    description: "Variables / properties this procedure reports (e.g. detection limit,
      limit of quantification, calibration factor, uncertainty propagation method),
      each modeled as a schema:PropertyValueSpecification (a procedure-level default,
      carrying schema:defaultValue) or a schema:PropertyValue (a measured value, carrying
      schema:value), keyed by schema:name. A technique profile enumerates the reported
      properties it defines; a dataset instance overrides each schema:defaultValue
      with a schema:value. Left open here \u2014 the technique overlay narrows it."
    type: array
    items:
      type: object
      properties:
        '@type':
          type: array
          items:
            type: string
        schema:name:
          type: string
          x-jsonld-id: http://schema.org/name
        ada:dataType:
          type: string
          x-jsonld-id: https://ada.astromat.org/metadata/dataType
        schema:defaultValue:
          x-jsonld-id: http://schema.org/defaultValue
        schema:value:
          x-jsonld-id: http://schema.org/value
    x-jsonld-id: http://schema.org/variableMeasured
required:
- '@context'
- '@type'
- schema:name
- schema:measurementTechnique
$defs:
  WorkflowHowTo:
    type: object
    description: The method's standard workflow expressed as a schema:HowTo. Contains
      an ordered array of workflow steps in schema:step, where each step is a cdi:Activity
      + schema:Action.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:HowTo
        minItems: 1
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the workflow (e.g. "EPMA WDS analytical workflow").
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        description: Overview of the workflow.
        x-jsonld-id: http://schema.org/description
      schema:url:
        type: string
        format: uri
        description: URL to a published protocol document.
        x-jsonld-id: http://schema.org/url
      schema:step:
        type: array
        description: Ordered sequence of workflow steps. Each step is a cdi:Activity
          + schema:Action describing a distinct phase of the analytical procedure.
          Must include exactly one sample-preparation step (schema:name "Sample preparation"
          with schema:additionalType containing "bios:LabProcess"); its schema:position
          is left to the protocol author.
        items:
          $ref: '#/$defs/WorkflowStep'
        contains:
          type: object
          description: a sample preparation step is required.
          properties:
            schema:name:
              const: Sample preparation
              x-jsonld-id: http://schema.org/name
            schema:additionalType:
              type: array
              contains:
                const: bios:LabProcess
              x-jsonld-id: http://schema.org/additionalType
          required:
          - schema:name
          - schema:additionalType
        maxContains: 1
        x-jsonld-id: http://schema.org/step
    required:
    - '@type'
    - schema:step
  WorkflowStep:
    type: object
    description: A single step in the analytical workflow, modeled as a cdi:Activity
      + schema:Action. Each step describes a distinct phase such as sample preparation,
      instrument calibration, data acquisition, data processing, or quality control.
      Steps carry their own parameters, instruments, reagents, and may contain sub-steps
      via schema:actionProcess.
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 2
        allOf:
        - contains:
            const: cdi:Activity
        - contains:
            const: schema:Action
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of this workflow step (e.g. "Sample preparation").
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        description: Detailed description of what this step involves.
        x-jsonld-id: http://schema.org/description
      schema:position:
        type: integer
        description: Ordinal position in the workflow sequence (1-based).
        x-jsonld-id: http://schema.org/position
      schema:additionalType:
        description: Further classification of this step (e.g. bios:LabProcess for
          wet-lab steps, schema:CreateAction for production steps).
        type: array
        items:
          type: string
        x-jsonld-id: http://schema.org/additionalType
      schema:instrument:
        description: Instrument or equipment used in this step.
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
        - type: object
          additionalProperties: false
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://schema.org/instrument
      bios:computationalTool:
        description: Software tools used in this step.
        type: array
        items:
          $ref: '#/$defs/ComputationalTool'
        x-jsonld-id: https://bioschemas.org/computationalTool
      bios:reagent:
        description: Reference materials, standards, or reagents used in this step.
        type: array
        items:
          $ref: '#/$defs/Reagent'
        x-jsonld-id: https://bioschemas.org/reagent
      prov:used:
        description: Input entities consumed or referenced by this step (e.g. prepared
          sample from a prior step).
        type: array
        items:
          anyOf:
          - type: string
          - type: object
            required:
            - '@id'
            additionalProperties: false
            properties:
              '@id':
                type: string
        x-jsonld-id: http://www.w3.org/ns/prov#used
      schema:result:
        description: Output entity produced by this step (can be referenced as input
          by a subsequent step).
        anyOf:
        - type: string
        - type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
        x-jsonld-id: http://schema.org/result
      schema:object:
        description: Reference to a prior step whose result is the input for this
          step (action chaining).
        anyOf:
        - type: string
        - type: object
          required:
          - '@id'
          additionalProperties: false
          properties:
            '@id':
              type: string
        x-jsonld-id: http://schema.org/object
      schema:additionalProperty:
        description: Step-specific parameters (e.g. beam conditions for the acquisition
          step, matrix correction settings for the data processing step). Editable
          parameters are schema:PropertyValueSpecification entries (a default the
          analyst may override); read-only parameters are schema:PropertyValue entries
          carrying the fixed protocol value.
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/MethodParameter'
          - $ref: '#/$defs/MethodParameterValue'
        x-jsonld-id: http://schema.org/additionalProperty
      schema:actionProcess:
        description: Sub-workflow for this step, expressed as a nested schema:HowTo
          with its own ordered steps. Use for steps that have a multi-phase internal
          procedure (e.g. sample preparation with mount, grind, polish, coat).
        $ref: '#/$defs/WorkflowHowTo'
        x-jsonld-id: http://schema.org/actionProcess
      dqv:hasQualityMeasurement:
        description: Quality measurements specific to this workflow step.
        type: array
        items:
          $ref: '#/$defs/QualityMeasure'
        x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMeasurement
    required:
    - '@type'
    - schema:name
    - schema:position
  MethodParameter:
    type: object
    description: 'A parameter specification for the method, typed as schema:PropertyValueSpecification.
      Uses schema.org properties for value constraints (defaultValue, minValue, maxValue,
      readonlyValue, valueRequired) and ada: extensions for analytical method semantics
      (fieldScope, category, tier). Link to a controlled vocabulary via schema:inDefinedTermSet.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValueSpecification
        minItems: 1
      schema:name:
        type: string
        description: Human-readable display label (e.g. "Accelerating Voltage").
        x-jsonld-id: http://schema.org/name
      schema:valueName:
        type: string
        description: Machine-readable parameter name for serialization (e.g. "acceleratingVoltage").
        x-jsonld-id: http://schema.org/valueName
      schema:description:
        type: string
        description: Guidance text shown to the user in the form.
        x-jsonld-id: http://schema.org/description
      schema:propertyID:
        description: URI identifying this parameter type in a formal vocabulary. Links
          to a skos:Concept or similar term definition. URI-shape values MUST be serialized
          as JSON-LD IRI references ({"@id":"..."}).
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/PropertyIDValue'
        x-jsonld-id: http://schema.org/propertyID
      schema:inDefinedTermSet:
        description: "Controlled vocabulary providing allowed values for this parameter.
          When present, form renders a dropdown/select populated from the vocabulary.
          Four shapes are accepted: (1) a plain URI string identifying an external
          SKOS ConceptScheme; (2) an object reference ({\"@id\": \"<uri>\"}) to a
          vocabulary defined elsewhere; (3) a LabeledLink (LinkRole with name and
          URL); (4) an inline schema:DefinedTermSet enumerating the allowed values\n
          \   as schema:DefinedTerm objects (replaces the prior ada:enumeration)."
        anyOf:
        - type: string
          format: uri
        - type: object
          additionalProperties: false
          description: Object reference to a vocabulary defined elsewhere.
          properties:
            '@id':
              type: string
              format: uri
          required:
          - '@id'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
        - type: object
          additionalProperties: false
          description: Inline schema:DefinedTermSet listing the allowed values as
            schema:DefinedTerm objects. Use when no external vocabulary URI is available;
            replaces the deprecated ada:enumeration property.
          properties:
            '@type':
              const: schema:DefinedTermSet
            schema:hasDefinedTerm:
              type: array
              minItems: 1
              items:
                type: object
                properties:
                  '@type':
                    const: schema:DefinedTerm
                  schema:termCode:
                    type: string
                    x-jsonld-id: http://schema.org/termCode
                required:
                - '@type'
                - schema:termCode
              x-jsonld-id: http://schema.org/hasDefinedTerm
          required:
          - '@type'
          - schema:hasDefinedTerm
        x-jsonld-id: http://schema.org/inDefinedTermSet
      schema:defaultValue:
        description: The default value for this parameter. For constant parameters
          (readonlyValue=true), this is the fixed value. For editable parameters,
          this is the pre-filled default.
        anyOf:
        - type: string
        - type: number
        - type: boolean
        x-jsonld-id: http://schema.org/defaultValue
      schema:readonlyValue:
        type: boolean
        description: true = constant, fixed for every session (read-only in form).
          false = editable (default or optional depending on valueRequired).
        x-jsonld-id: http://schema.org/readonlyValue
      schema:valueRequired:
        type: boolean
        description: 'true = must be provided (mandatory). false = optional. Combined
          with readonlyValue: readonly+required = constant mandatory; !readonly+required
          = editable mandatory; !readonly+!required = optional.'
        x-jsonld-id: http://schema.org/valueRequired
      schema:minValue:
        type: number
        description: Minimum allowed numeric value. Defines the lower bound of a valid
          range at the method level; specific values within this range may be set
          per element in the analyteTemplate.
        x-jsonld-id: http://schema.org/minValue
      schema:maxValue:
        type: number
        description: Maximum allowed numeric value. Upper bound of valid range.
        x-jsonld-id: http://schema.org/maxValue
      schema:stepValue:
        type: number
        description: Granularity expected of the value (e.g. 0.1 for nA).
        x-jsonld-id: http://schema.org/stepValue
      schema:valuePattern:
        type: string
        description: Regex pattern for validating string values.
        x-jsonld-id: http://schema.org/valuePattern
      schema:multipleValues:
        type: boolean
        description: Whether multiple values are allowed (default false).
        x-jsonld-id: http://schema.org/multipleValues
      ada:fieldScope:
        type: string
        enum:
        - method
        - session
        - element
        description: Whether this parameter is fixed at the method level, varies per
          analytical session, or is element-specific.
        x-jsonld-id: https://ada.astromat.org/metadata/fieldScope
      ada:category:
        description: Grouping label for form layout (e.g. "Beam Conditions", "Data
          Processing", "Quality Control"). String for simple cases; DefinedTerm to
          link to a controlled vocabulary of parameter categories.
        anyOf:
        - type: string
        - $ref: '#/$defs/DefinedTerm'
        x-jsonld-id: https://ada.astromat.org/metadata/category
      ada:dataType:
        type: string
        enum:
        - string
        - number
        - integer
        - boolean
        - date
        - uri
        description: Expected data type for the parameter value.
        x-jsonld-id: https://ada.astromat.org/metadata/dataType
      schema:unitText:
        type: string
        description: Unit of measure label (e.g. "kV", "nA", "um").
        x-jsonld-id: http://schema.org/unitText
      schema:unitCode:
        description: URI for unit of measure (QUDT preferred).
        anyOf:
        - type: string
        - $ref: '#/$defs/DefinedTerm'
        x-jsonld-id: http://schema.org/unitCode
      ada:cdifPropertyPath:
        type: string
        description: The CDIF building block property path this parameter maps to.
          Used for JSON-LD serialisation.
        x-jsonld-id: https://ada.astromat.org/metadata/cdifPropertyPath
      ada:tier:
        type: string
        enum:
        - M
        - R
        - O
        description: Mandatory / Recommended / Optional tier from the metadata profile.
          Informs validation strictness.
        x-jsonld-id: https://ada.astromat.org/metadata/tier
    required:
    - schema:name
    - ada:fieldScope
    - ada:dataType
  MethodParameterValue:
    type: object
    description: A read-only method parameter carrying the fixed protocol value, typed
      as schema:PropertyValue. Used for Advanced-protocol parameters that the analyst
      cannot change (the value is set by the protocol). The value is in schema:value;
      the human-readable label is in schema:name. Contrast with MethodParameter (schema:PropertyValueSpecification),
      used for editable parameters.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValue
        minItems: 1
      schema:name:
        type: string
        description: Human-readable display label (e.g. "Ablation Cell Type").
        x-jsonld-id: http://schema.org/name
      schema:propertyID:
        description: URI identifying this parameter type in a formal vocabulary. URI-shape
          values MUST be serialized as JSON-LD IRI references ({"@id":"..."}).
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/PropertyIDValue'
        x-jsonld-id: http://schema.org/propertyID
      schema:value:
        description: The fixed protocol value for this read-only parameter.
        x-jsonld-id: http://schema.org/value
      schema:unitText:
        type: string
        description: Unit of measure label (e.g. "kV", "nA", "um").
        x-jsonld-id: http://schema.org/unitText
    required:
    - schema:name
    - schema:value
  KeyedTableColumn:
    type: object
    description: Definition of one column of a KEYED TABLE, typed as schema:PropertyValueSpecification.
      A keyed table has one row per member of some domain -- an analyte, a reported
      property, a channel -- and one column per field whose value repeats over that
      domain (the TAPP workbook's `Keyed By` column). Rows become schema:variableMeasured
      entries; columns become schema:additionalProperty within each. AnalyteColumn
      and ReportedPropertyColumn are the two domains modelled so far; both are this
      shape.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValueSpecification
        minItems: 1
      schema:name:
        type: string
        description: Human-readable column label (e.g. "Diffracting Crystal").
        x-jsonld-id: http://schema.org/name
      schema:valueName:
        type: string
        description: Machine-readable column identifier (e.g. "diffractingCrystal").
        x-jsonld-id: http://schema.org/valueName
      schema:description:
        type: string
        description: Guidance text for this column.
        x-jsonld-id: http://schema.org/description
      schema:propertyID:
        description: URI identifying this column's parameter type in a formal vocabulary.
          URI-shape values MUST be serialized as JSON-LD IRI references ({"@id":"..."}).
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/PropertyIDValue'
        x-jsonld-id: http://schema.org/propertyID
      schema:inDefinedTermSet:
        description: "Controlled vocabulary providing allowed values for this column.
          Four shapes are accepted: (1) a plain URI string identifying an external
          SKOS ConceptScheme; (2) an object reference ({\"@id\": \"<uri>\"}) to a
          vocabulary defined elsewhere; (3) a LabeledLink (LinkRole with name and
          URL); (4) an inline schema:DefinedTermSet enumerating the allowed values\n
          \   as schema:DefinedTerm objects (replaces the prior ada:enumeration)."
        anyOf:
        - type: string
          format: uri
        - type: object
          additionalProperties: false
          description: Object reference to a vocabulary defined elsewhere.
          properties:
            '@id':
              type: string
              format: uri
          required:
          - '@id'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
        - type: object
          additionalProperties: false
          description: Inline schema:DefinedTermSet listing the allowed values as
            schema:DefinedTerm objects. Use when no external vocabulary URI is available;
            replaces the deprecated ada:enumeration property.
          properties:
            '@type':
              const: schema:DefinedTermSet
            schema:hasDefinedTerm:
              type: array
              minItems: 1
              items:
                type: object
                properties:
                  '@type':
                    const: schema:DefinedTerm
                  schema:termCode:
                    type: string
                    x-jsonld-id: http://schema.org/termCode
                required:
                - '@type'
                - schema:termCode
              x-jsonld-id: http://schema.org/hasDefinedTerm
          required:
          - '@type'
          - schema:hasDefinedTerm
        x-jsonld-id: http://schema.org/inDefinedTermSet
      schema:defaultValue:
        description: Default value for this column (pre-filled per row).
        anyOf:
        - type: string
        - type: number
        - type: boolean
        x-jsonld-id: http://schema.org/defaultValue
      schema:readonlyValue:
        type: boolean
        description: true = constant across all analytes (read-only column).
        x-jsonld-id: http://schema.org/readonlyValue
      schema:valueRequired:
        type: boolean
        description: true = must be provided for every analyte row.
        x-jsonld-id: http://schema.org/valueRequired
      schema:minValue:
        type: number
        x-jsonld-id: http://schema.org/minValue
      schema:maxValue:
        type: number
        x-jsonld-id: http://schema.org/maxValue
      schema:valuePattern:
        type: string
        x-jsonld-id: http://schema.org/valuePattern
      ada:dataType:
        type: string
        enum:
        - string
        - number
        - integer
        - boolean
        - date
        - uri
        x-jsonld-id: https://ada.astromat.org/metadata/dataType
      schema:unitText:
        type: string
        x-jsonld-id: http://schema.org/unitText
      ada:tier:
        type: string
        enum:
        - M
        - R
        - O
        x-jsonld-id: https://ada.astromat.org/metadata/tier
      ada:cdifPropertyPath:
        type: string
        description: How this column maps into the variableMeasured JSON-LD structure.
        x-jsonld-id: https://ada.astromat.org/metadata/cdifPropertyPath
    required:
    - schema:name
    - ada:dataType
  AnalyteColumn:
    description: One column of the per-analyte parameter table. Structurally a KeyedTableColumn;
      kept as its own name because generated schemas and the shared analyteColumns
      registry $ref it.
    allOf:
    - $ref: '#/$defs/KeyedTableColumn'
  ReportedPropertyColumn:
    description: One column of the reported-property table. The reported properties
      are what the procedure REPORTS -- '206Pb/238U date (Ma)', 'd56Fe (permil vs
      IRMM-014)' -- as distinct from the analytes and channels it ACQUIRES. Structurally
      a KeyedTableColumn.
    allOf:
    - $ref: '#/$defs/KeyedTableColumn'
  ChannelColumn:
    description: 'One column of the channel table. A channel is an instrument SELECTION
      POSITION -- a mass, a Faraday cup, an energy-loss edge, an X-ray line. It is
      not a flavour of analyte: the analyte is what is measured, the channel is the
      position it is measured on, and the two are independent. One analyte may occupy
      several channels, and MC-ICP-MS cups routinely monitor interferences that are
      not analytes at all. Structurally a KeyedTableColumn.'
    allOf:
    - $ref: '#/$defs/KeyedTableColumn'
  ChannelIdentifierColumn:
    description: The mandatory channel-identifier column, naming the selection position
      in each row. Mirrors AnalyteIdentifierColumn and ReportedPropertyIdentifierColumn;
      like both it maps into schema:variableMeasured/schema:name, because the variable
      list is shared across a procedure's table parts rather than owned by any one
      of them.
    allOf:
    - $ref: '#/$defs/KeyedTableColumn'
    - type: object
      properties:
        schema:valueName:
          const: channel
          x-jsonld-id: http://schema.org/valueName
        ada:dataType:
          const: string
          x-jsonld-id: https://ada.astromat.org/metadata/dataType
        schema:readonlyValue:
          const: true
          x-jsonld-id: http://schema.org/readonlyValue
        schema:valueRequired:
          const: true
          x-jsonld-id: http://schema.org/valueRequired
        ada:tier:
          const: M
          x-jsonld-id: https://ada.astromat.org/metadata/tier
        ada:cdifPropertyPath:
          const: '#/schema:variableMeasured/schema:name'
          x-jsonld-id: https://ada.astromat.org/metadata/cdifPropertyPath
      required:
      - schema:valueName
      - ada:dataType
      - schema:readonlyValue
      - schema:valueRequired
      - ada:tier
      - ada:cdifPropertyPath
  ReportedPropertyIdentifierColumn:
    description: 'The mandatory reported-property identifier column, naming the reported
      variable in each row. Mirrors AnalyteIdentifierColumn: pinned constants fix
      the column''s role as a row identifier rather than an editable parameter. Both
      identifier columns map into schema:variableMeasured/schema:name because the
      variable list is SHARED -- a procedure yields several tables (analyte, channel,
      reported property) over one logical variable registry, not one table per document.'
    allOf:
    - $ref: '#/$defs/KeyedTableColumn'
    - type: object
      properties:
        schema:valueName:
          const: reportedProperty
          x-jsonld-id: http://schema.org/valueName
        ada:dataType:
          const: string
          x-jsonld-id: https://ada.astromat.org/metadata/dataType
        schema:readonlyValue:
          const: true
          x-jsonld-id: http://schema.org/readonlyValue
        schema:valueRequired:
          const: true
          x-jsonld-id: http://schema.org/valueRequired
        ada:tier:
          const: M
          x-jsonld-id: https://ada.astromat.org/metadata/tier
        ada:cdifPropertyPath:
          const: '#/schema:variableMeasured/schema:name'
          x-jsonld-id: https://ada.astromat.org/metadata/cdifPropertyPath
      required:
      - schema:valueName
      - ada:dataType
      - schema:readonlyValue
      - schema:valueRequired
      - ada:tier
      - ada:cdifPropertyPath
  AnalyteIdentifierColumn:
    description: 'The mandatory analyte-identifier column. Each row in the analyte
      table must carry a value for this column naming the analyzed constituent (e.g.
      "SiO2", "Fe"). Pinned constants enforce the column''s role: readonly (the identifier
      of a row, not an editable parameter), required, mandatory tier, and a fixed
      mapping into schema:variableMeasured/schema:name. Long-term the value space
      should be a DefinedTermSet; for now a string.'
    allOf:
    - $ref: '#/$defs/AnalyteColumn'
    - type: object
      properties:
        schema:valueName:
          const: analyte
          x-jsonld-id: http://schema.org/valueName
        ada:dataType:
          const: string
          x-jsonld-id: https://ada.astromat.org/metadata/dataType
        schema:readonlyValue:
          const: true
          x-jsonld-id: http://schema.org/readonlyValue
        schema:valueRequired:
          const: true
          x-jsonld-id: http://schema.org/valueRequired
        ada:tier:
          const: M
          x-jsonld-id: https://ada.astromat.org/metadata/tier
        ada:cdifPropertyPath:
          const: '#/schema:variableMeasured/schema:name'
          x-jsonld-id: https://ada.astromat.org/metadata/cdifPropertyPath
      required:
      - schema:valueName
      - ada:dataType
      - schema:readonlyValue
      - schema:valueRequired
      - ada:tier
      - ada:cdifPropertyPath
  ComputationalTool:
    type: object
    description: Software application used for data acquisition, reduction, or processing.
      Follows Bioschemas ComputationalTool pattern.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:SoftwareApplication
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the software (e.g. "Probe for EPMA").
        x-jsonld-id: http://schema.org/name
      schema:version:
        type: string
        description: Software version string (e.g. "12.9.5").
        x-jsonld-id: http://schema.org/version
      schema:description:
        type: string
        description: Role or purpose of this tool in the method.
        x-jsonld-id: http://schema.org/description
      schema:url:
        type: string
        format: uri
        description: URL to the software product or documentation.
        x-jsonld-id: http://schema.org/url
      ada:toolRole:
        type: string
        enum:
        - acquisition
        - dataReduction
        - processing
        - visualization
        description: Role this software plays in the analytical workflow.
        x-jsonld-id: https://ada.astromat.org/metadata/toolRole
    required:
    - schema:name
  Reagent:
    type: object
    description: A reference material, calibration standard, or chemical reagent.
      Follows Bioschemas reagent pattern with extensions for geochemistry reference
      materials.
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
        description: 'What the material IS, independent of the role it plays here
          (that is ada:reagentRole). One of the three kinds must be present: schema:DefinedTerm
          for a material identified by a registry entry (GeoReM, NIST SRM, USGS);
          schema:Product for a specific catalogued specimen or purchased lot (Smithsonian
          NMNH number, IGSN, in-house standard); schema:ChemicalSubstance for a bulk
          chemical or coating stock.'
        contains:
          enum:
          - schema:DefinedTerm
          - schema:Product
          - schema:ChemicalSubstance
      '@id':
        type: string
        description: Persistent identifier (e.g. IGSN, GeoReM URL).
      schema:name:
        type: string
        description: Name of the material (e.g. "San Carlos olivine").
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        x-jsonld-id: http://schema.org/description
      schema:identifier:
        description: Formal identifier (IGSN, catalog number, GeoReM ID).
        anyOf:
        - type: string
        - type: object
          additionalProperties: false
          properties:
            '@type':
              type: array
              items:
                type: string
              minItems: 1
            schema:propertyID:
              type: string
              x-jsonld-id: http://schema.org/propertyID
            schema:value:
              type: string
              x-jsonld-id: http://schema.org/value
        x-jsonld-id: http://schema.org/identifier
      schema:termCode:
        type: string
        description: Registry code for the material on the schema:DefinedTerm path
          (e.g. "SRM 610", "ATHO-G").
        x-jsonld-id: http://schema.org/termCode
      schema:inDefinedTermSet:
        description: The registry the schema:termCode belongs to (GeoReM, NIST SRM
          catalogue, USGS RM list).
        anyOf:
        - type: string
          format: uri
        - type: object
          additionalProperties: false
          properties:
            '@id':
              type: string
              format: uri
            schema:name:
              type: string
              x-jsonld-id: http://schema.org/name
        x-jsonld-id: http://schema.org/inDefinedTermSet
      ada:reagentRole:
        type: string
        enum:
        - primaryStandard
        - secondaryStandard
        - interferenceStandard
        - blankMaterial
        - coatingMaterial
        - referenceMaterial
        - reagent
        description: Role of this material in the method.
        x-jsonld-id: https://ada.astromat.org/metadata/reagentRole
      schema:citation:
        description: Publication reference for the standard's accepted values.
        anyOf:
        - type: string
        - type: object
          additionalProperties: false
          properties:
            '@type':
              type: array
              items:
                type: string
            schema:name:
              type: string
              x-jsonld-id: http://schema.org/name
            schema:url:
              type: string
              format: uri
              x-jsonld-id: http://schema.org/url
        x-jsonld-id: http://schema.org/citation
    required:
    - '@type'
    - schema:name
  PropertyIDValue:
    description: "One value of schema:propertyID: a vocabulary URI, a JSON-LD IRI
      reference, or a DefinedTerm.\nWhether the property holding these is an ARRAY
      depends on which job schema:PropertyValue is doing, because schema.org overloads
      that one class for several things that ought to be distinct (see the CDIF Core
      Implementation Guide, \"Polymorphism of PropertyValue\"):\n\n  * schema:additionalProperty
      and schema:variableMeasured -- a measured or declared parameter.\n    propertyID
      is 0..* there, so it is ALWAYS an array and a consumer iterates without first\n
      \   testing the value's type.\n  * schema:identifier -- an identifier for the
      identifier scheme (DOI, ARK, IGSN). Upstream\n    types that one as a bare string
      or {\"@id\": ...}, never an array, so do NOT wrap it."
    anyOf:
    - type: string
      format: uri
    - type: object
      additionalProperties: false
      required:
      - '@id'
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/DefinedTerm'
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  prov: http://www.w3.org/ns/prov#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  bios: https://bioschemas.org/
  dqv: http://www.w3.org/ns/dqv#
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)
* [OneGeochemistry EPMA Metadata Profile v1.0](https://github.com/amds-ldeo/geochemBuildingBlocks)
* [Bioschemas LabProtocol Profile](https://bioschemas.org/profiles/LabProtocol)
* [DDI-CDI 1.0 Process Model](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [W3C Data Quality Vocabulary (DQV)](https://www.w3.org/TR/vocab-dqv/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/tappDefinition`

