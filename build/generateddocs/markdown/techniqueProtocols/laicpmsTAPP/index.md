
# LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP) (Schema)

`ogch.techniqueProtocols.laicpmsTAPP` *v0.1*

LA-ICPMS-specific extension of the base TAPP definition. Adds laser-ablation top-level properties (spot geometry, ablation mode, laser fluence, ablation spot duration), a parameter vocabulary, and an analyte-column template covering LA-ICPMS per-element acquisition and reporting fields (detection limits, reproducibility, isobaric interference corrections). Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under the shared vocab/, parameterTemplates/, and analyteColumns/ catalogs for maintainability.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### laicpmsTAPP example Spot: LA-ICPMS spot analysis mode
laicpmsTAPP instance derived from publication LA-ICPMS spot analysis mode. Property and parameter values taken from the corresponding column of the TAPP_LAICPMS_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:laicpmsTAPP-spot",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Spot",
  "schema:description": "laicpmsTAPP example for LA-ICPMS spot analysis mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "Y",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:laicpmsTAPP-spot",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Spot",
  "schema:description": "laicpmsTAPP example for LA-ICPMS spot analysis mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "Y",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laicpmsTAPP-spot a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:description "laicpmsTAPP example for LA-ICPMS spot analysis mode." ;
    schema1:location [ a schema1:Place ;
            schema1:name "Y" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:termCode "LA-ICPMS" ] ;
    schema1:name "LA-ICPMS TAPP example Spot" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Y" ] ;
    ada:AblationSpotDuration "Y" ;
    ada:BeamDamageMinimization "Y" ;
    ada:ablationMode "Y" ;
    ada:laserFluenceDefault "Y" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> ;
    ada:spotGeometryDefault "Y" ;
    ada:spotPath "Y" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Y" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once." ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:readonlyValue true ;
    schema1:valueName "DriftMonitorFrequency" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system." ;
    schema1:name "Laser Pulse Duration" ;
    schema1:readonlyValue true ;
    schema1:valueName "LaserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix." ;
    schema1:name "Matrix Offset Correction (LIEF)" ;
    schema1:readonlyValue true ;
    schema1:valueName "MatrixOffseCorrection" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "SessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "WarmUpTime" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```


### laicpmsTAPP example Transect: LA-ICPMS transect / line-scan mode
laicpmsTAPP instance derived from publication LA-ICPMS transect / line-scan mode. Property and parameter values taken from the corresponding column of the TAPP_LAICPMS_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:laicpmsTAPP-transect",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Transect",
  "schema:description": "laicpmsTAPP example for LA-ICPMS transect / line-scan mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "N",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:laicpmsTAPP-transect",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Transect",
  "schema:description": "laicpmsTAPP example for LA-ICPMS transect / line-scan mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "N",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laicpmsTAPP-transect a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:description "laicpmsTAPP example for LA-ICPMS transect / line-scan mode." ;
    schema1:location [ a schema1:Place ;
            schema1:name "Y" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:termCode "LA-ICPMS" ] ;
    schema1:name "LA-ICPMS TAPP example Transect" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Y" ] ;
    ada:AblationSpotDuration "N" ;
    ada:BeamDamageMinimization "Y" ;
    ada:ablationMode "Y" ;
    ada:laserFluenceDefault "Y" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> ;
    ada:spotGeometryDefault "Y" ;
    ada:spotPath "Y" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Y" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once." ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:readonlyValue true ;
    schema1:valueName "DriftMonitorFrequency" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system." ;
    schema1:name "Laser Pulse Duration" ;
    schema1:readonlyValue true ;
    schema1:valueName "LaserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix." ;
    schema1:name "Matrix Offset Correction (LIEF)" ;
    schema1:readonlyValue true ;
    schema1:valueName "MatrixOffseCorrection" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "SessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "WarmUpTime" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```


### laicpmsTAPP example Mapping: LA-ICPMS 2-D mapping mode
laicpmsTAPP instance derived from publication LA-ICPMS 2-D mapping mode. Property and parameter values taken from the corresponding column of the TAPP_LAICPMS_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:laicpmsTAPP-mapping",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Mapping",
  "schema:description": "laicpmsTAPP example for LA-ICPMS 2-D mapping mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "N",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "N"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:laicpmsTAPP-mapping",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "LA-ICPMS TAPP example Mapping",
  "schema:description": "laicpmsTAPP example for LA-ICPMS 2-D mapping mode.",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "LA-ICPMS",
    "schema:name": "Laser Ablation Inductively Coupled Plasma Mass Spectrometry"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Y"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Y"
    }
  ],
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Y",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:spotGeometryDefault": "Y",
  "ada:spotPath": "Y",
  "ada:ablationMode": "Y",
  "ada:laserFluenceDefault": "Y",
  "ada:BeamDamageMinimization": "Y",
  "ada:AblationSpotDuration": "N",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/LaserPulseDuration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Laser Pulse Duration",
      "schema:valueName": "LaserPulseDuration",
      "schema:description": "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/WarmUpTime",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "WarmUpTime",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/SessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Instrument Warm-up / Session Duration Limit",
      "schema:valueName": "SessionDurationLimit",
      "schema:description": "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/DriftMonitorFrequency",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:valueName": "DriftMonitorFrequency",
      "schema:description": "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "N"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/laicpmsTAPP/MatrixOffseCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Matrix Offset Correction (LIEF)",
      "schema:valueName": "MatrixOffseCorrection",
      "schema:description": "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Y"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laicpmsTAPP-mapping a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:description "laicpmsTAPP example for LA-ICPMS 2-D mapping mode." ;
    schema1:location [ a schema1:Place ;
            schema1:name "Y" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Laser Ablation Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:termCode "LA-ICPMS" ] ;
    schema1:name "LA-ICPMS TAPP example Mapping" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Y" ] ;
    ada:AblationSpotDuration "N" ;
    ada:BeamDamageMinimization "Y" ;
    ada:ablationMode "Y" ;
    ada:laserFluenceDefault "Y" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> ;
    ada:spotGeometryDefault "Y" ;
    ada:spotPath "Y" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Y" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/DriftMonitorFrequency> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N" ;
    schema1:description "Whether the protocol uses a single acquisition pass or multiple sequential runs on the same sample location, each optimized for different analytical objectives. For multi-run designs, describe the number of runs, their purpose, key laser and instrument settings per run, and how outputs of one run feed into data reduction of another. Not applicable to raster mapping, where each spatial location is visited exactly once." ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:readonlyValue true ;
    schema1:valueName "DriftMonitorFrequency" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/LaserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Duration of each individual laser pulse, including units. Pulse duration determines the ablation regime: nanosecond (ns) pulses involve significant thermal effects and elemental fractionation; femtosecond (fs) pulses are non-thermal and substantially reduce elemental fractionation and matrix effects. This is a fixed hardware property of the laser system." ;
    schema1:name "Laser Pulse Duration" ;
    schema1:readonlyValue true ;
    schema1:valueName "LaserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/MatrixOffseCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Whether an empirical correction was applied to account for systematic differences in laser-induced elemental fractionation (LIEF) patterns between the external calibration standard and the sample matrix." ;
    schema1:name "Matrix Offset Correction (LIEF)" ;
    schema1:readonlyValue true ;
    schema1:valueName "MatrixOffseCorrection" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/SessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "SessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/laicpmsTAPP/WarmUpTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Y" ;
    schema1:description "Minimum warm-up time required after plasma ignition before analyses begin, and any maximum session duration enforced to maintain stable operating conditions. These constraints are part of the protocol and cannot be varied by the analyst." ;
    schema1:name "Instrument Warm-up / Session Duration Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "WarmUpTime" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP)
description: LA-ICPMS-specific extension of the base TAPP definition. Adds top-level
  LA-ICPMS properties, a parameter vocabulary in ada:methodParameters, and an analyte-column
  template covering LA-ICPMS per-element acquisition and reporting fields. Each ada:analyteColumns[]
  entry must match one of the catalog files in analyteColumns/ (or the inherited identifier
  column from tappDefinition); each catalog file is itself a JSON Schema whose examples[0]
  carries the canonical instance. Generated from docs/TAPP_LAICPMS_filled.xlsx by
  tools/build_TAPP_from_spreadsheet.py.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/tappDefinition/schema.yaml
- type: object
  properties:
    ada:spotGeometryDefault:
      description: "Shape and dimensions of the laser ablation spot in micrometres
        registered by the protocol. For circular spots, report diameter; for square
        or rectangular spots, report width \xD7 length. The protocol registers the
        typical geometry; analysts may adjust within protocol-allowed range."
      type: string
    ada:spotPath:
      description: Sampling mode or ablation pattern used during analysis.
      type: string
    ada:ablationMode:
      description: Sampling mode or ablation pattern used during analysis.
      type: string
    ada:laserFluenceDefault:
      description: "Laser pulse energy per unit area at the sample surface in J cm\u207B\xB2,
        as registered by the protocol. Fluence is the physically meaningful quantity
        controlling ablation rate, crater morphology, elemental fractionation, and
        particle size distribution. If the system reports only as % of maximum output,
        include that value and note the system maximum where known."
      type: string
    ada:BeamDamageMinimization:
      description: Laser pulse repetition rate in hertz registered by the protocol.
        For mapping methods, repetition rate together with scan speed and spot size
        determines pixel size and spatial resolution. Analysts may adjust within protocol-allowed
        bounds.
      type: string
    ada:AblationSpotDuration:
      description: 'Total on-sample ablation (signal acquisition) time per individual
        spot in seconds, as set in the acquisition method. This is a protocol-level
        parameter for spot analysis: it reflects the deliberate trade-off between
        signal accumulation (longer = lower LOD), sample consumption, and session
        throughput. For transect analysis, the equivalent protocol-level parameter
        is scan speed (captured in Transect Rate, Mapping Rate or Step Size). For
        mapping analysis, total acquisition time is sample-area-dependent and therefore
        analysis-level, not captured here.'
      type: string
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/IsobaricInterferenceCorrection
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/IsobaricInterferenceCorrectionMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analyticalAccuracy
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analyticalAccuracyMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/betweenSessionReproducibility
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/betweenSessionReproducibilityMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimit
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimitMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferingSpecies
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/limitOfQuantification
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spectrometerDwellTime
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotIdentifier
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotXCoordinate
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotYCoordinate
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/withinSessionReproducibility
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/withinSessionReproducibilityMethod
          allOf:
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/IsobaricInterferenceCorrection
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/IsobaricInterferenceCorrectionMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analyticalAccuracy
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analyticalAccuracyMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/betweenSessionReproducibility
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/betweenSessionReproducibilityMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimit
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimitMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferingSpecies
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/limitOfQuantification
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spectrometerDwellTime
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotIdentifier
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotXCoordinate
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spotYCoordinate
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/withinSessionReproducibility
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/withinSessionReproducibilityMethod
            minContains: 0
            maxContains: 1
    ada:methodParameters:
      type: array
      items:
        anyOf:
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/DriftMonitorFrequency
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/LaserPulseDuration
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/MatrixOffseCorrection
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/SessionDurationLimit
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/WarmUpTime
      allOf:
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/DriftMonitorFrequency
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/LaserPulseDuration
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/MatrixOffseCorrection
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/SessionDurationLimit
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/WarmUpTime
        minContains: 0
        maxContains: 1
    schema:instrument:
      type: object
      properties:
        schema:hasPart:
          type: array
          description: 'Instrument sub-components. Each item is a schema:Thing with
            at least one schema:additionalType. Spreadsheet-known types: Detector.
            Other additionalType values are accepted via the catch-all branch.'
          items:
            oneOf:
            - type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  contains:
                    const: schema:Thing
                schema:additionalType:
                  type: array
                  items:
                    type: string
                  contains:
                    const: Detector
              required:
              - '@type'
              - schema:additionalType
            - type: object
              description: Catch-all for instrument sub-component types not enumerated
                above. Authors may use any schema:additionalType outside the known
                set; schema:name is unconstrained on this branch.
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  contains:
                    const: schema:Thing
                schema:additionalType:
                  type: array
                  items:
                    type: string
                  minItems: 1
                  not:
                    anyOf:
                    - contains:
                        const: Detector
              required:
              - '@type'
              - schema:additionalType

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/schema.yaml)


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
    "nxs": "http://purl.org/nexusformat/definitions/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/laicpmsTAPP/context.jsonld)

## Sources

* [LA-ICPMS_TAPP_v8.xlsx (TAPP worksheet)](https://github.com/usgin/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/techniqueProtocols/laicpmsTAPP`

