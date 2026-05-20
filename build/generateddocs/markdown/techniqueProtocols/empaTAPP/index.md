
# EMPA Technique-Aligned Protocol Profile (empaTAPP) (Schema)

`ogch.techniqueProtocols.empaTAPP` *v0.1*

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### empaTAPP example P0: Richard & Deng 2026 (synthetic comprehensive WDS example)
empaTAPP instance derived from publication Richard & Deng 2026 (synthetic comprehensive WDS example). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p0",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element silicate and oxide| all properties",
  "schema:description": "empaTAPP example derived from Richard & Deng 2026 (synthetic comprehensive WDS example).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Richard| S.M. ORCID:0000-0001-6041-5302; Deng| Ruolin ORCID:0000-0001-5383-3039"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "IEDA| Columbia University"
  },
  "schema:datePublished": "2026-04-28",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-1234567"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://example.org/EMPA/WDS",
      "schema:name": "Method reference"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Feldspar"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Pyroxene"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Olivine"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SXFiveFE",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SXFiveFE"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP1",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Inclined"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LiF, PET, TAP, PC2"
          }
        ],
        "schema:description": "Less sensitive to specimen height; good for rough surfaces; low pressure"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP2",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LLiF,LPET"
          }
        ],
        "schema:description": "High pressure for greater sensitivity; large crystals for trace/light elements"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP3",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "TAP, PC0"
          }
        ],
        "schema:description": "Low pressure; light element coverage"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP4",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LPET, TAP"
          }
        ],
        "schema:description": "Low pressure"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA v12.9.5",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Cameca PeakSight",
      "ada:toolRole": "reduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "CalcZAF",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "5",
  "ada:beamCurrentDefault": "10",
  "ada:matrixCorrectionMethod": "Armstrong/Love-Scott",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "None required (anhydrous minerals)"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/DriftCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Drift Correction",
      "schema:valueName": "DriftCorrection",
      "schema:description": "Describe method used to monitor and correct for instrument drift",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Primary major element reference materials are run at beginning and end of every analytical session and the calibration is interpolated"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/massAbsorptionCoefficients",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Mass Absorption Coefficients (MACs)",
      "schema:valueName": "massAbsorptionCoefficients",
      "schema:description": "Database of mass absorption coefficients used in the matrix correction.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "MCMASTER"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "N/A"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/wdsDeadTimeCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "WDS Dead Time Correction",
      "schema:valueName": "wdsDeadTimeCorrection",
      "schema:description": "Method used to correct WDS proportional counter dead time at high count rates.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Super-precision"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/spectrometerNumber",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS Spectrometer Channel",
        "schema:valueName": "spectrometerNumber",
        "schema:description": "WDS spectrometer number used for this element.",
        "ada:dataType": "integer",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/analysisOrder",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "analysisOrder",
        "schema:description": "Order of analysis on spectormeter. To give an example, if there are 5 detectors, 5 analytes (elements) will be measured simultaneously on the first pass (i.e., Sequence = 1 for all of them), then 5 other analytes will be measured simultaneously on the second pass (i.e., Sequence = 2 for these 5 analytes), etc. The numbering depends on the order of these analytes being measured during an analysis. Also, if there are 20 analytes, there will be at least 4 passes in this case.",
        "ada:dataType": "integer",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/monochromatorCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "monochromatorCrystal",
        "schema:description": "Analysing crystal (monochromator) used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/monochromatorCrystal"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/wdsDetectorType",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Proportional Counter / Detector",
        "schema:valueName": "wdsDetectorType",
        "schema:description": "Type of detector used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/wdsDetectorType"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/pulseHeightAnalyzeSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "pulseHeightAnalyzeSetting",
        "schema:description": "Pulse height analyzer setting used for the WDS detector.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Background Position(s)",
        "schema:valueName": "backgroundCountingPosition",
        "schema:description": "Positions of background measurements relative to the peak, in mm and/or sinθ, and whether on the high or low energy side.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Blank Correction",
        "schema:valueName": "blankCorrection",
        "schema:description": "Method and reference materials used to determine and apply blank corrections.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/normalization-standardsCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization / Standards-Based Correction",
        "schema:valueName": "normalization-standardsCorrection",
        "schema:description": "Post-acquisition normalization applied using secondary reference materials.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/edsDeadTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EDS Dead Time",
        "schema:valueName": "edsDeadTime",
        "schema:description": "Percent dead time reported by the EDS spectrometer",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Correction Method",
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:description": "Method used to estimate and subtract background X-ray intensity beneath the peak.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/backgroundCorrectionMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Time-Dependent Intensity Correction",
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:description": "Type of time-dependent intensity correction applied for volatile or beam-sensitive elements.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/timeDependentIntensityCorrection"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/elementEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Element Estimation Method",
        "schema:valueName": "elementEstimationMethod",
        "schema:description": "How elemental concentrations were calculated — directly from measured X-ray intensities or via cation stoichiometry.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/elementEstimationMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferenceCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interference Corrections Applied",
        "schema:valueName": "interferenceCorrection",
        "schema:description": "Flag indicating whether a spectral interference correction was applied for this element.",
        "ada:dataType": "boolean",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interfering Elements",
        "schema:valueName": "interferingElements",
        "schema:description": "List of elements whose X-ray lines overlap with the measured line for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interference Correction Standard",
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:description": "Reference material used to quantify and calibrate the interference correction.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "schema:description": "Method used to compute detection limits.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalAnalyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Analytical Precision",
        "schema:valueName": "typicalAnalyticalPrecision",
        "schema:description": "Reproducibility of repeated measurements on the same or equivalent standard, expressed as 1σ relative standard deviation (%).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalAnalyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Analytical Accuracy",
        "schema:valueName": "typicalAnalyticalAccuracy",
        "schema:description": "Offset between measured and accepted reference values for secondary standards, expressed as % relative bias.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalCountingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Counting Statistics Error",
        "schema:valueName": "typicalCountingStatisticsError",
        "schema:description": "1σ uncertainty propagated from counting statistics on peak and background intensities.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 1,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalAnalyticalPrecision": "0.5% (1σ, n=20 for SiO2)",
        "typicalAnalyticalAccuracy": "1.2% relative to GeoReM preferred value for VG-2 SiO2",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 3,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "K",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 2,
        "monochromatorCrystal": "LLIF",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 4,
        "monochromatorCrystal": "LLIF",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 5,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 30,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 4,
        "analysisOrder": 1,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 3,
        "analysisOrder": 1,
        "monochromatorCrystal": "TAP",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 2,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 3,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 1,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1σ error per measurement"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p0",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element silicate and oxide| all properties",
  "schema:description": "empaTAPP example derived from Richard & Deng 2026 (synthetic comprehensive WDS example).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Richard| S.M. ORCID:0000-0001-6041-5302; Deng| Ruolin ORCID:0000-0001-5383-3039"
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "IEDA| Columbia University"
  },
  "schema:datePublished": "2026-04-28",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-1234567"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://example.org/EMPA/WDS",
      "schema:name": "Method reference"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Feldspar"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Pyroxene"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Olivine"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SXFiveFE",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SXFiveFE"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP1",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Inclined"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LiF, PET, TAP, PC2"
          }
        ],
        "schema:description": "Less sensitive to specimen height; good for rough surfaces; low pressure"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP2",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LLiF,LPET"
          }
        ],
        "schema:description": "High pressure for greater sensitivity; large crystals for trace/light elements"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP3",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "TAP, PC0"
          }
        ],
        "schema:description": "Low pressure; light element coverage"
      },
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "wdsSpectrometer"
        ],
        "schema:name": "SP4",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Orientation",
            "schema:value": "Vertical"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:name": "Crystals",
            "schema:value": "LPET, TAP"
          }
        ],
        "schema:description": "Low pressure"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Probe for EPMA v12.9.5",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Cameca PeakSight",
      "ada:toolRole": "reduction"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "CalcZAF",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "5",
  "ada:beamCurrentDefault": "10",
  "ada:matrixCorrectionMethod": "Armstrong/Love-Scott",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "None required (anhydrous minerals)"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/DriftCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Drift Correction",
      "schema:valueName": "DriftCorrection",
      "schema:description": "Describe method used to monitor and correct for instrument drift",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Primary major element reference materials are run at beginning and end of every analytical session and the calibration is interpolated"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/massAbsorptionCoefficients",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Mass Absorption Coefficients (MACs)",
      "schema:valueName": "massAbsorptionCoefficients",
      "schema:description": "Database of mass absorption coefficients used in the matrix correction.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "MCMASTER"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "N/A"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/wdsDeadTimeCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "WDS Dead Time Correction",
      "schema:valueName": "wdsDeadTimeCorrection",
      "schema:description": "Method used to correct WDS proportional counter dead time at high count rates.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Super-precision"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/spectrometerNumber",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS Spectrometer Channel",
        "schema:valueName": "spectrometerNumber",
        "schema:description": "WDS spectrometer number used for this element.",
        "ada:dataType": "integer",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/analysisOrder",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Sequence",
        "schema:valueName": "analysisOrder",
        "schema:description": "Order of analysis on spectormeter. To give an example, if there are 5 detectors, 5 analytes (elements) will be measured simultaneously on the first pass (i.e., Sequence = 1 for all of them), then 5 other analytes will be measured simultaneously on the second pass (i.e., Sequence = 2 for these 5 analytes), etc. The numbering depends on the order of these analytes being measured during an analysis. Also, if there are 20 analytes, there will be at least 4 passes in this case.",
        "ada:dataType": "integer",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/monochromatorCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "monochromatorCrystal",
        "schema:description": "Analysing crystal (monochromator) used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/monochromatorCrystal"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/wdsDetectorType",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Proportional Counter / Detector",
        "schema:valueName": "wdsDetectorType",
        "schema:description": "Type of detector used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/wdsDetectorType"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/pulseHeightAnalyzeSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "WDS PHA Setting",
        "schema:valueName": "pulseHeightAnalyzeSetting",
        "schema:description": "Pulse height analyzer setting used for the WDS detector.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Background Position(s)",
        "schema:valueName": "backgroundCountingPosition",
        "schema:description": "Positions of background measurements relative to the peak, in mm and/or sin\u03b8, and whether on the high or low energy side.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Blank Correction",
        "schema:valueName": "blankCorrection",
        "schema:description": "Method and reference materials used to determine and apply blank corrections.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/normalization-standardsCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Normalization / Standards-Based Correction",
        "schema:valueName": "normalization-standardsCorrection",
        "schema:description": "Post-acquisition normalization applied using secondary reference materials.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/edsDeadTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EDS Dead Time",
        "schema:valueName": "edsDeadTime",
        "schema:description": "Percent dead time reported by the EDS spectrometer",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Correction Method",
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:description": "Method used to estimate and subtract background X-ray intensity beneath the peak.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/backgroundCorrectionMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Time-Dependent Intensity Correction",
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:description": "Type of time-dependent intensity correction applied for volatile or beam-sensitive elements.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/timeDependentIntensityCorrection"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/elementEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Element Estimation Method",
        "schema:valueName": "elementEstimationMethod",
        "schema:description": "How elemental concentrations were calculated \u2014 directly from measured X-ray intensities or via cation stoichiometry.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/elementEstimationMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferenceCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interference Corrections Applied",
        "schema:valueName": "interferenceCorrection",
        "schema:description": "Flag indicating whether a spectral interference correction was applied for this element.",
        "ada:dataType": "boolean",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interfering Elements",
        "schema:valueName": "interferingElements",
        "schema:description": "List of elements whose X-ray lines overlap with the measured line for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Interference Correction Standard",
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:description": "Reference material used to quantify and calibrate the interference correction.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Detection Limit Method",
        "schema:valueName": "detectionLimitMethod",
        "schema:description": "Method used to compute detection limits.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalAnalyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Analytical Precision",
        "schema:valueName": "typicalAnalyticalPrecision",
        "schema:description": "Reproducibility of repeated measurements on the same or equivalent standard, expressed as 1\u03c3 relative standard deviation (%).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalAnalyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Analytical Accuracy",
        "schema:valueName": "typicalAnalyticalAccuracy",
        "schema:description": "Offset between measured and accepted reference values for secondary standards, expressed as % relative bias.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalCountingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Counting Statistics Error",
        "schema:valueName": "typicalCountingStatisticsError",
        "schema:description": "1\u03c3 uncertainty propagated from counting statistics on peak and background intensities.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 1,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalAnalyticalPrecision": "0.5% (1\u03c3, n=20 for SiO2)",
        "typicalAnalyticalAccuracy": "1.2% relative to GeoReM preferred value for VG-2 SiO2",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 3,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "K",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 2,
        "monochromatorCrystal": "LLIF",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 4,
        "monochromatorCrystal": "LLIF",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 2,
        "analysisOrder": 5,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "High Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 30,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Linear",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 4,
        "analysisOrder": 1,
        "monochromatorCrystal": "LPET",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 3,
        "analysisOrder": 1,
        "monochromatorCrystal": "TAP",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 2,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 3,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Double exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "WDS",
        "spectrometerNumber": 1,
        "analysisOrder": 1,
        "monochromatorCrystal": "LiF",
        "wdsDetectorType": "Low Pressure P10 Flow",
        "pulseHeightAnalyzeSetting": "Integral",
        "peakCountingTime": 60,
        "backgroundCountingTime": 10,
        "backgroundCountingPosition": "+5 mm (High)",
        "blankCorrection": "single-sample mean; quartz",
        "normalization-standardsCorrection": "Single-sample normalization to JdF-D2 basalt glass",
        "edsDeadTime": "10-12 %",
        "backgroundCorrectionMethod": "1-point low with slope factor",
        "timeDependentIntensityCorrection": "Exponential",
        "elementEstimationMethod": "Direct (measured)",
        "secondaryReferenceMaterial": "USNM 111240/52 VG-2",
        "interferenceCorrection": "Yes",
        "interferingElements": "None",
        "interferenceCorrectionStandard": "N/A",
        "detectionLimitMethod": "A.B.(1997)",
        "typicalCountingStatisticsError": "Propagated 1\u03c3 error per measurement"
      }
    ]
  }
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

ex:empaTAPP-p0 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Richard| S.M. ORCID:0000-0001-6041-5302; Deng| Ruolin ORCID:0000-0001-5383-3039" ] ;
    schema1:datePublished "2026-04-28" ;
    schema1:description "empaTAPP example derived from Richard & Deng 2026 (synthetic comprehensive WDS example)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-1234567" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Orientation" ;
                            schema1:value "Vertical" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystals" ;
                            schema1:value "LLiF,LPET" ] ;
                    schema1:additionalType "wdsSpectrometer" ;
                    schema1:description "High pressure for greater sensitivity; large crystals for trace/light elements" ;
                    schema1:name "SP2" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ElectronSource" ;
                    schema1:name "Field Emission (FEG)" ],
                [ a schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Orientation" ;
                            schema1:value "Vertical" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystals" ;
                            schema1:value "LPET, TAP" ] ;
                    schema1:additionalType "wdsSpectrometer" ;
                    schema1:description "Low pressure" ;
                    schema1:name "SP4" ],
                [ a schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Orientation" ;
                            schema1:value "Vertical" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystals" ;
                            schema1:value "TAP, PC0" ] ;
                    schema1:additionalType "wdsSpectrometer" ;
                    schema1:description "Low pressure; light element coverage" ;
                    schema1:name "SP3" ],
                [ a schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Orientation" ;
                            schema1:value "Inclined" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Crystals" ;
                            schema1:value "LiF, PET, TAP, PC2" ] ;
                    schema1:additionalType "wdsSpectrometer" ;
                    schema1:description "Less sensitive to specimen height; good for rough surfaces; low pressure" ;
                    schema1:name "SP1" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SXFiveFE" ] ;
            schema1:name "Cameca SXFiveFE" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "IEDA| Columbia University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element silicate and oxide| all properties" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Olivine" ],
        [ a schema1:DefinedTerm ;
            schema1:name "Pyroxene" ],
        [ a schema1:DefinedTerm ;
            schema1:name "Feldspar" ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:name "Method reference" ;
            schema1:url "https://example.org/EMPA/WDS" ] ;
    ada:acceleratingVoltageDefault "20" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/analysisOrder>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingPosition>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/edsDeadTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/elementEstimationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferenceCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/monochromatorCrystal>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/normalization-standardsCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/pulseHeightAnalyzeSetting>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/spectrometerNumber>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalAnalyticalAccuracy>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalAnalyticalPrecision>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalCountingStatisticsError>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/wdsDetectorType> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "10" ;
    ada:beamDiameterDefault "5" ;
    ada:beamMode "Focused" ;
    ada:matrixCorrectionMethod "Armstrong/Love-Scott" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/DriftCorrection>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/massAbsorptionCoefficients>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/wdsDeadTimeCorrection> ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "CalcZAF" ;
            ada:toolRole "reduction" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Cameca PeakSight" ;
            ada:toolRole "reduction" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA v12.9.5" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/analysisOrder> a schema1:PropertyValueSpecification ;
    schema1:description "Order of analysis on spectormeter. To give an example, if there are 5 detectors, 5 analytes (elements) will be measured simultaneously on the first pass (i.e., Sequence = 1 for all of them), then 5 other analytes will be measured simultaneously on the second pass (i.e., Sequence = 2 for these 5 analytes), etc. The numbering depends on the order of these analytes being measured during an analysis. Also, if there are 20 analytes, there will be at least 4 passes in this case." ;
    schema1:name "Sequence" ;
    schema1:readonlyValue true ;
    schema1:valueName "analysisOrder" ;
    ada:dataType "integer" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:description "Method used to estimate and subtract background X-ray intensity beneath the peak." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/backgroundCorrectionMethod> ;
    schema1:name "Background Correction Method" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingPosition> a schema1:PropertyValueSpecification ;
    schema1:description "Positions of background measurements relative to the peak, in mm and/or sinθ, and whether on the high or low energy side." ;
    schema1:name "Typical Background Position(s)" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCountingPosition" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Total time spent counting at background position(s) in seconds." ;
    schema1:name "Default Background Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:description "Method and reference materials used to determine and apply blank corrections." ;
    schema1:name "Blank Correction" ;
    schema1:readonlyValue true ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:description "Method used to compute detection limits." ;
    schema1:name "Detection Limit Method" ;
    schema1:readonlyValue true ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/edsDeadTime> a schema1:PropertyValueSpecification ;
    schema1:description "Percent dead time reported by the EDS spectrometer" ;
    schema1:name "EDS Dead Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "edsDeadTime" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/elementEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:description "How elemental concentrations were calculated — directly from measured X-ray intensities or via cation stoichiometry." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/elementEstimationMethod> ;
    schema1:name "Element Estimation Method" ;
    schema1:readonlyValue true ;
    schema1:valueName "elementEstimationMethod" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferenceCorrection> a schema1:PropertyValueSpecification ;
    schema1:description "Flag indicating whether a spectral interference correction was applied for this element." ;
    schema1:name "Interference Corrections Applied" ;
    schema1:readonlyValue true ;
    schema1:valueName "interferenceCorrection" ;
    ada:dataType "boolean" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Reference material used to quantify and calibrate the interference correction." ;
    schema1:name "Interference Correction Standard" ;
    schema1:readonlyValue true ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:description "List of elements whose X-ray lines overlap with the measured line for this element." ;
    schema1:name "Interfering Elements" ;
    schema1:readonlyValue true ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/monochromatorCrystal> a schema1:PropertyValueSpecification ;
    schema1:description "Analysing crystal (monochromator) used in the WDS spectrometer for this element." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/monochromatorCrystal> ;
    schema1:name "Diffracting Crystal" ;
    schema1:readonlyValue true ;
    schema1:valueName "monochromatorCrystal" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/normalization-standardsCorrection> a schema1:PropertyValueSpecification ;
    schema1:description "Post-acquisition normalization applied using secondary reference materials." ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:readonlyValue true ;
    schema1:valueName "normalization-standardsCorrection" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Time spent counting X-ray intensity at the peak position in seconds." ;
    schema1:name "Default Peak Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/pulseHeightAnalyzeSetting> a schema1:PropertyValueSpecification ;
    schema1:description "Pulse height analyzer setting used for the WDS detector." ;
    schema1:name "WDS PHA Setting" ;
    schema1:readonlyValue true ;
    schema1:valueName "pulseHeightAnalyzeSetting" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial> a schema1:PropertyValueSpecification ;
    schema1:description "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns." ;
    schema1:name "Secondary Reference Materials" ;
    schema1:readonlyValue true ;
    schema1:valueName "secondaryReferenceMaterial" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/spectrometerNumber> a schema1:PropertyValueSpecification ;
    schema1:description "WDS spectrometer number used for this element." ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:readonlyValue true ;
    schema1:valueName "spectrometerNumber" ;
    ada:dataType "integer" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:description "Type of time-dependent intensity correction applied for volatile or beam-sensitive elements." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/timeDependentIntensityCorrection> ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:readonlyValue true ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalAnalyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:description "Offset between measured and accepted reference values for secondary standards, expressed as % relative bias." ;
    schema1:name "Typical Analytical Accuracy" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalAnalyticalAccuracy" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalAnalyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:description "Reproducibility of repeated measurements on the same or equivalent standard, expressed as 1σ relative standard deviation (%)." ;
    schema1:name "Typical Analytical Precision" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalAnalyticalPrecision" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalCountingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:description "1σ uncertainty propagated from counting statistics on peak and background intensities." ;
    schema1:name "Typical Counting Statistics Error" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalCountingStatisticsError" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/wdsDetectorType> a schema1:PropertyValueSpecification ;
    schema1:description "Type of detector used in the WDS spectrometer for this element." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/wdsDetectorType> ;
    schema1:name "Proportional Counter / Detector" ;
    schema1:readonlyValue true ;
    schema1:valueName "wdsDetectorType" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None required (anhydrous minerals)" ;
    schema1:description "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals." ;
    schema1:name "Beam Damage Minimization" ;
    schema1:readonlyValue true ;
    schema1:valueName "BeamDamageMinimization" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/DriftCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Primary major element reference materials are run at beginning and end of every analytical session and the calibration is interpolated" ;
    schema1:description "Describe method used to monitor and correct for instrument drift" ;
    schema1:name "Drift Correction" ;
    schema1:readonlyValue true ;
    schema1:valueName "DriftCorrection" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A" ;
    schema1:description "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases." ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:readonlyValue true ;
    schema1:valueName "halogenOxygenCorrection" ;
    ada:dataType "boolean" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/massAbsorptionCoefficients> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "MCMASTER" ;
    schema1:description "Database of mass absorption coefficients used in the matrix correction." ;
    schema1:name "Mass Absorption Coefficients (MACs)" ;
    schema1:readonlyValue true ;
    schema1:valueName "massAbsorptionCoefficients" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/wdsDeadTimeCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Super-precision" ;
    schema1:description "Method used to correct WDS proportional counter dead time at high count rates." ;
    schema1:name "WDS Dead Time Correction" ;
    schema1:readonlyValue true ;
    schema1:valueName "wdsDeadTimeCorrection" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```


### empaTAPP example P1: Chi et al. 2015 (Tissintite, EPSL)
empaTAPP instance derived from publication Chi et al. 2015 (Tissintite, EPSL). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    }
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF correction procedure (Armstrong, 1995)",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/xrayEmissionLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayEmissionLine",
        "schema:description": "The X-ray emission line measured for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Albite"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Fayalite"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Forsterite"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Mn2SiO4"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "TiO2"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Cr2O3"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Microcline"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    }
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF correction procedure (Armstrong, 1995)",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/xrayEmissionLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayEmissionLine",
        "schema:description": "The X-ray emission line measured for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Anorthite"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Albite"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Fayalite"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Forsterite"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Mn2SiO4"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "TiO2"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Cr2O3"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Microcline"
      }
    ]
  }
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

ex:empaTAPP-p1 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma et al." ] ;
    schema1:description "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/xrayEmissionLine> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "5" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "CITZAF correction procedure (Armstrong, 1995)" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Total time spent counting at background position(s) in seconds." ;
    schema1:name "Default Background Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Time spent counting X-ray intensity at the peak position in seconds." ;
    schema1:name "Default Peak Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/xrayEmissionLine> a schema1:PropertyValueSpecification ;
    schema1:description "The X-ray emission line measured for this element." ;
    schema1:name "X-ray Line" ;
    schema1:readonlyValue true ;
    schema1:valueName "xrayEmissionLine" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P2: Hu et al. 2020 (Coesite NWA8657, GCA)
empaTAPP instance derived from publication Hu et al. 2020 (Coesite NWA8657, GCA). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p2",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Sen Hu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Maskelynite, \nmelt inclusion glasses, \nsilica glass, \ncoesite aggregates, \nmesostasis"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8100",
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
      "schema:name": "JXA-8100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamCurrentDefault": "10",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3σ) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "SiO2: 0.02 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "MgO: 0.02 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "FeO: 0.05 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Jadeite",
        "typicalDetectionLimit": "Na2O: 0.02 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Jadeite",
        "typicalDetectionLimit": "Al2O3: 0.02 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Bustamite",
        "typicalDetectionLimit": "CaO: 0.02 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Bustamite",
        "typicalDetectionLimit": "MnO: 0.06 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "K-feldspar",
        "typicalDetectionLimit": "K2O: 0.01 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Synthetic rutile",
        "typicalDetectionLimit": "TiO2: 0.03 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Cr2O3",
        "typicalDetectionLimit": "Cr2O3: 0.03 wt%"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p2",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Sen Hu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Maskelynite, \nmelt inclusion glasses, \nsilica glass, \ncoesite aggregates, \nmesostasis"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8100",
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
      "schema:name": "JXA-8100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamCurrentDefault": "10",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3\u03c3) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "SiO2: 0.02 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "MgO: 0.02 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Natural kaersutite",
        "typicalDetectionLimit": "FeO: 0.05 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Jadeite",
        "typicalDetectionLimit": "Na2O: 0.02 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Jadeite",
        "typicalDetectionLimit": "Al2O3: 0.02 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Bustamite",
        "typicalDetectionLimit": "CaO: 0.02 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Bustamite",
        "typicalDetectionLimit": "MnO: 0.06 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "K-feldspar",
        "typicalDetectionLimit": "K2O: 0.01 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Synthetic rutile",
        "typicalDetectionLimit": "TiO2: 0.03 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Cr2O3",
        "typicalDetectionLimit": "Cr2O3: 0.03 wt%"
      }
    ]
  }
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

ex:empaTAPP-p2 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Sen Hu et al." ] ;
    schema1:description "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8100" ] ;
            schema1:name "JEOL JXA-8100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals and glass" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name """Maskelynite, 
melt inclusion glasses, 
silica glass, 
coesite aggregates, 
mesostasis""" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "10" ;
    ada:beamMode "Focused" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> a schema1:PropertyValueSpecification ;
    schema1:description "Method detection limit at 99% confidence (3σ) for each measured element." ;
    schema1:name "Typical Detection Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalDetectionLimit" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P3sil: Liu et al. 2016 (Tissint silicate mineral chem., MAPS)
empaTAPP instance derived from publication Liu et al. 2016 (Tissint silicate mineral chem., MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p3sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS silicates/oxides",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint silicate mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Olivine, pyroxene, Fe-Ti-Cr oxides"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1–2 µm focused",
  "ada:beamCurrentDefault": "20 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3σ) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for SiO2"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for TiO2"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for Al2O3"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for MgO"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for CaO"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for FeO"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for MnO"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for Cr2O3"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for NiO"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for Na2O"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for K2O"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for P2O5"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p3sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS silicates/oxides",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint silicate mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Olivine, pyroxene, Fe-Ti-Cr oxides"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1\u20132 \u00b5m focused",
  "ada:beamCurrentDefault": "20 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3\u03c3) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for SiO2"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for TiO2"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for Al2O3"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for MgO"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for CaO"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for FeO"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for MnO"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for Cr2O3"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for NiO"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for Na2O"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for K2O"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for P2O5"
      }
    ]
  }
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

ex:empaTAPP-p3sil a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Yang Liu et al." ] ;
    schema1:description "empaTAPP example derived from Liu et al. 2016 (Tissint silicate mineral chem., MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
            schema1:name "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS silicates/oxides" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Olivine, pyroxene, Fe-Ti-Cr oxides" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "1–2 µm focused" ;
    ada:beamMode "Focused" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> a schema1:PropertyValueSpecification ;
    schema1:description "Method detection limit at 99% confidence (3σ) for each measured element." ;
    schema1:name "Typical Detection Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalDetectionLimit" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P3phos: Liu et al. 2016 (Tissint phosphate mineral chem., MAPS)
empaTAPP instance derived from publication Liu et al. 2016 (Tissint phosphate mineral chem., MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p3phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS maskelynite, phosphate, sulfide, glass",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint phosphate mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "maskelynite, phosphate, sulfide, glass"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:beamMode": "Defocused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "5–10 µm defocused",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3σ) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for SiO2"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for TiO2"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for Al2O3"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for MgO"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.03 wt% for CaO"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for FeO"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for MnO"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for Cr2O3"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for NiO"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for Na2O"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for K2O"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "typicalDetectionLimit": "<0.05–0.1 wt% for P2O5"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p3phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS maskelynite, phosphate, sulfide, glass",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint phosphate mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "maskelynite, phosphate, sulfide, glass"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:beamMode": "Defocused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "5\u201310 \u00b5m defocused",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3\u03c3) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for SiO2"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for TiO2"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for Al2O3"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for MgO"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.03 wt% for CaO"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for FeO"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for MnO"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for Cr2O3"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for NiO"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for Na2O"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for K2O"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "typicalDetectionLimit": "<0.05\u20130.1 wt% for P2O5"
      }
    ]
  }
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

ex:empaTAPP-p3phos a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Yang Liu et al." ] ;
    schema1:description "empaTAPP example derived from Liu et al. 2016 (Tissint phosphate mineral chem., MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
            schema1:name "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS maskelynite, phosphate, sulfide, glass" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "maskelynite, phosphate, sulfide, glass" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "10 nA" ;
    ada:beamDiameterDefault "5–10 µm defocused" ;
    ada:beamMode "Defocused" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> a schema1:PropertyValueSpecification ;
    schema1:description "Method detection limit at 99% confidence (3σ) for each measured element." ;
    schema1:name "Typical Detection Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalDetectionLimit" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P4: Ma et al. 2017 (Liebermannite, MAPS)
empaTAPP instance derived from publication Ma et al. 2017 (Liebermannite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p4",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    }
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF correction procedure (Armstrong, 1995)",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/xrayEmissionLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayEmissionLine",
        "schema:description": "The X-ray emission line measured for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3σ) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "Si: 0.05 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "Al: 0.06 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "K: 0.02 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic anorthite",
        "typicalDetectionLimit": "Ca: 0.02 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Amelia albite",
        "typicalDetectionLimit": "Na: 0.03 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic fayalite",
        "typicalDetectionLimit": "Fe: 0.06 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic forsterite",
        "typicalDetectionLimit": "Mg: 0.02 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic TiO2",
        "typicalDetectionLimit": "Ti: 0.04 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic Cr2O3",
        "typicalDetectionLimit": "Cr: 0.05 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "xrayEmissionLine": "Kα",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic Mn-olivine",
        "typicalDetectionLimit": "Mn: 0.06 wt%"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p4",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    }
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF correction procedure (Armstrong, 1995)",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/xrayEmissionLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "X-ray Line",
        "schema:valueName": "xrayEmissionLine",
        "schema:description": "The X-ray emission line measured for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3\u03c3) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "Si: 0.05 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "Al: 0.06 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Asbestos microcline",
        "typicalDetectionLimit": "K: 0.02 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic anorthite",
        "typicalDetectionLimit": "Ca: 0.02 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Amelia albite",
        "typicalDetectionLimit": "Na: 0.03 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic fayalite",
        "typicalDetectionLimit": "Fe: 0.06 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic forsterite",
        "typicalDetectionLimit": "Mg: 0.02 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic TiO2",
        "typicalDetectionLimit": "Ti: 0.04 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic Cr2O3",
        "typicalDetectionLimit": "Cr: 0.05 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "xrayEmissionLine": "K\u03b1",
        "peakCountingTime": 20,
        "backgroundCountingTime": 10,
        "primaryCalibrationStandard": "Synthetic Mn-olivine",
        "typicalDetectionLimit": "Mn: 0.06 wt%"
      }
    ]
  }
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

ex:empaTAPP-p4 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma et al." ] ;
    schema1:description "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/xrayEmissionLine> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "5" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "CITZAF correction procedure (Armstrong, 1995)" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Total time spent counting at background position(s) in seconds." ;
    schema1:name "Default Background Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Time spent counting X-ray intensity at the peak position in seconds." ;
    schema1:name "Default Peak Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> a schema1:PropertyValueSpecification ;
    schema1:description "Method detection limit at 99% confidence (3σ) for each measured element." ;
    schema1:name "Typical Detection Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalDetectionLimit" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/xrayEmissionLine> a schema1:PropertyValueSpecification ;
    schema1:description "The X-ray emission line measured for this element." ;
    schema1:name "X-ray Line" ;
    schema1:readonlyValue true ;
    schema1:valueName "xrayEmissionLine" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P5: Frank et al. 2023 (Ivuna CAI, MAPS)
empaTAPP instance derived from publication Frank et al. 2023 (Ivuna CAI, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p5",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "David Frank et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SX100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "1 µm (focused)",
  "ada:beamCurrentDefault": "20",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3σ) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "SiO2: 0.05 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "Al2O3: 0.03–0.04 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "TiO2: 0.06–0.09 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "K2O: 0.03–0.04 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "Na2O: 0.05 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "FeO: 0.05 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "MgO: 0.05 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "CaO: 0.03–0.04 wt%"
      },
      {
        "analyte": "S",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Canyon Diablo troilite",
        "typicalDetectionLimit": "SO2: 0.06–0.09 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Rhodonite",
        "typicalDetectionLimit": "MnO: 0.05 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Chromium metal",
        "typicalDetectionLimit": "Cr2O3: 0.06–0.09 wt%"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Nickel metal",
        "typicalDetectionLimit": "NiO: 0.06–0.09 wt%"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Apatite",
        "typicalDetectionLimit": "P2O5: 0.06–0.09 wt%"
      },
      {
        "analyte": "V",
        "epmaTechnique": "√",
        "peakCountingTime": "10–50",
        "primaryCalibrationStandard": "Vanadium metal",
        "typicalDetectionLimit": "V2O3: 0.06–0.09 wt%"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p5",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "David Frank et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SX100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "1 \u00b5m (focused)",
  "ada:beamCurrentDefault": "20",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/typicalDetectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Typical Detection Limit",
        "schema:valueName": "typicalDetectionLimit",
        "schema:description": "Method detection limit at 99% confidence (3\u03c3) for each measured element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "SiO2: 0.05 wt%"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "Al2O3: 0.03\u20130.04 wt%"
      },
      {
        "analyte": "Ti",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "TiO2: 0.06\u20130.09 wt%"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "K2O: 0.03\u20130.04 wt%"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "Na2O: 0.05 wt%"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "FeO: 0.05 wt%"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "MgO: 0.05 wt%"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Kakanui kaersutite",
        "typicalDetectionLimit": "CaO: 0.03\u20130.04 wt%"
      },
      {
        "analyte": "S",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Canyon Diablo troilite",
        "typicalDetectionLimit": "SO2: 0.06\u20130.09 wt%"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Rhodonite",
        "typicalDetectionLimit": "MnO: 0.05 wt%"
      },
      {
        "analyte": "Cr",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Chromium metal",
        "typicalDetectionLimit": "Cr2O3: 0.06\u20130.09 wt%"
      },
      {
        "analyte": "Ni",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Nickel metal",
        "typicalDetectionLimit": "NiO: 0.06\u20130.09 wt%"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Apatite",
        "typicalDetectionLimit": "P2O5: 0.06\u20130.09 wt%"
      },
      {
        "analyte": "V",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "10\u201350",
        "primaryCalibrationStandard": "Vanadium metal",
        "typicalDetectionLimit": "V2O3: 0.06\u20130.09 wt%"
      }
    ]
  }
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

ex:empaTAPP-p5 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "David Frank et al." ] ;
    schema1:description "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SX100" ] ;
            schema1:name "Cameca SX100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene" ] ;
    ada:acceleratingVoltageDefault "20" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "20" ;
    ada:beamDiameterDefault "1 µm (focused)" ;
    ada:beamMode "Focused" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Time spent counting X-ray intensity at the peak position in seconds." ;
    schema1:name "Default Peak Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/typicalDetectionLimit> a schema1:PropertyValueSpecification ;
    schema1:description "Method detection limit at 99% confidence (3σ) for each measured element." ;
    schema1:name "Typical Detection Limit" ;
    schema1:readonlyValue true ;
    schema1:valueName "typicalDetectionLimit" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P6: Broussard et al. 2026 (OC002 CI chondrite, MAPS)
empaTAPP instance derived from publication Broussard et al. 2026 (OC002 CI chondrite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Broussard et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "edsDetector"
        ],
        "schema:name": "JEOL (e2v/Gresham) silicon-drift EDS spectrometer",
        "schema:description": "JEOL (e2v/Gresham) silicon-drift EDS spectrometer"
      }
    ]
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF (Armstrong, 1995); CalcImage; Quantitative Microanalysis Explorer",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "25 nA",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "F measurement with polynomial background fit (LDE1 crystal)"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/monochromatorCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "monochromatorCrystal",
        "schema:description": "Analysing crystal (monochromator) used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/monochromatorCrystal"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Correction Method",
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:description": "Method used to estimate and subtract background X-ray intensity beneath the peak.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/backgroundCorrectionMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "√",
        "monochromatorCrystal": "LDE1 (for F)",
        "backgroundCorrectionMethod": "MAN (mean atomic number) background calibration",
        "secondaryReferenceMaterial": "Smithsonian Microbeam standards (for analytical accuracy confirmation)"
      },
      {
        "analyte": "CO2",
        "epmaTechnique": "√",
        "monochromatorCrystal": "LDE1 (for F)",
        "backgroundCorrectionMethod": "MAN (mean atomic number) background calibration",
        "secondaryReferenceMaterial": "Smithsonian Microbeam standards (for analytical accuracy confirmation)"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Broussard et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
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
      "schema:name": "JXA-8200"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing"
        ],
        "schema:additionalType": [
          "edsDetector"
        ],
        "schema:name": "JEOL (e2v/Gresham) silicon-drift EDS spectrometer",
        "schema:description": "JEOL (e2v/Gresham) silicon-drift EDS spectrometer"
      }
    ]
  },
  "bios:computationalTool": [
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
      "schema:name": "CITZAF (Armstrong, 1995); CalcImage; Quantitative Microanalysis Explorer",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "25 nA",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "F measurement with polynomial background fit (LDE1 crystal)"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/monochromatorCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Diffracting Crystal",
        "schema:valueName": "monochromatorCrystal",
        "schema:description": "Analysing crystal (monochromator) used in the WDS spectrometer for this element.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/monochromatorCrystal"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Background Correction Method",
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:description": "Method used to estimate and subtract background X-ray intensity beneath the peak.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/backgroundCorrectionMethod"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "\u221a",
        "monochromatorCrystal": "LDE1 (for F)",
        "backgroundCorrectionMethod": "MAN (mean atomic number) background calibration",
        "secondaryReferenceMaterial": "Smithsonian Microbeam standards (for analytical accuracy confirmation)"
      },
      {
        "analyte": "CO2",
        "epmaTechnique": "\u221a",
        "monochromatorCrystal": "LDE1 (for F)",
        "backgroundCorrectionMethod": "MAN (mean atomic number) background calibration",
        "secondaryReferenceMaterial": "Smithsonian Microbeam standards (for analytical accuracy confirmation)"
      }
    ]
  }
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

ex:empaTAPP-p6 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Broussard et al." ] ;
    schema1:description "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Thing ;
                    schema1:additionalType "edsDetector" ;
                    schema1:description "JEOL (e2v/Gresham) silicon-drift EDS spectrometer" ;
                    schema1:name "JEOL (e2v/Gresham) silicon-drift EDS spectrometer" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/monochromatorCrystal>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial> ;
            ada:defaultAnalytes [ ],
                [ ] ] ;
    ada:beamCurrentDefault "25 nA" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection> ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "Probe for EPMA" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "CITZAF (Armstrong, 1995); CalcImage; Quantitative Microanalysis Explorer" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:description "Method used to estimate and subtract background X-ray intensity beneath the peak." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/backgroundCorrectionMethod> ;
    schema1:name "Background Correction Method" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/monochromatorCrystal> a schema1:PropertyValueSpecification ;
    schema1:description "Analysing crystal (monochromator) used in the WDS spectrometer for this element." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/monochromatorCrystal> ;
    schema1:name "Diffracting Crystal" ;
    schema1:readonlyValue true ;
    schema1:valueName "monochromatorCrystal" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial> a schema1:PropertyValueSpecification ;
    schema1:description "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns." ;
    schema1:name "Secondary Reference Materials" ;
    schema1:readonlyValue true ;
    schema1:valueName "secondaryReferenceMaterial" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "F measurement with polynomial background fit (LDE1 crystal)" ;
    schema1:description "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals." ;
    schema1:name "Beam Damage Minimization" ;
    schema1:readonlyValue true ;
    schema1:valueName "BeamDamageMinimization" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)" ;
    schema1:description "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases." ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:readonlyValue true ;
    schema1:valueName "halogenOxygenCorrection" ;
    ada:dataType "boolean" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```


### empaTAPP example P7: Seifert et al. 2026 (Bennu apatite, MAPS)
empaTAPP instance derived from publication Seifert et al. 2026 (Bennu apatite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p7",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element apatite (phosphate)",
  "schema:description": "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Seifert et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Apatite [Ca5(PO4)3(F,Cl,OH)]"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
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
      "schema:name": "JEOL 8530 EMPA (Field Emission)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 µm",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 µm and 10 µm spot conditions"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F measured; Cl measured; OH by difference)"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "SrF2",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "albite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "SW olivine",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "quartz",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "Wilburforce apatite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "Wilburforce apatite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "S",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "barite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Cl",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "tugtupite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "rhodonite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "ilmenite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "OH",
        "epmaTechnique": "√",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p7",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element apatite (phosphate)",
  "schema:description": "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Seifert et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Apatite [Ca5(PO4)3(F,Cl,OH)]"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
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
      "schema:name": "JEOL 8530 EMPA (Field Emission)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 \u00b5m",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/BeamDamageMinimization",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 \u00b5m and 10 \u00b5m spot conditions"
    },
    {
      "@context": {
        "schema": "http://schema.org/",
        "ada": "https://ada.astromat.org/metadata/"
      },
      "@id": "ada:parameter/empaTAPP/halogenOxygenCorrection",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F measured; Cl measured; OH by difference)"
    }
  ],
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Peak Counting Time",
        "schema:valueName": "peakCountingTime",
        "schema:description": "Time spent counting X-ray intensity at the peak position in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Default Background Counting Time",
        "schema:valueName": "backgroundCountingTime",
        "schema:description": "Total time spent counting at background position(s) in seconds.",
        "ada:dataType": "number",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/secondaryReferenceMaterial",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Secondary Reference Materials",
        "schema:valueName": "secondaryReferenceMaterial",
        "schema:description": "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "SrF2",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "albite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "SW olivine",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "quartz",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "Wilburforce apatite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "Wilburforce apatite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "S",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "barite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Cl",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "tugtupite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "rhodonite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "primaryCalibrationStandard": "ilmenite",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      },
      {
        "analyte": "OH",
        "epmaTechnique": "\u221a",
        "peakCountingTime": "20 s peak time",
        "backgroundCountingTime": "10 s background",
        "secondaryReferenceMaterial": "Durango apatite (halogen volatilization test; F and Cl values compared to Wudarska et al. 2021)"
      }
    ]
  }
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

ex:empaTAPP-p7 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Seifert et al." ] ;
    schema1:description "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ElectronSource" ;
                    schema1:name "Field Emission (FEG)" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8530 EMPA (Field Emission)" ] ;
            schema1:name "JEOL JEOL 8530 EMPA (Field Emission)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA major element apatite (phosphate)" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Apatite [Ca5(PO4)3(F,Cl,OH)]" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "2 µm" ;
    ada:methodParameters <https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection> .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Total time spent counting at background position(s) in seconds." ;
    schema1:name "Default Background Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:description "Time spent counting X-ray intensity at the peak position in seconds." ;
    schema1:name "Default Peak Counting Time" ;
    schema1:readonlyValue true ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/secondaryReferenceMaterial> a schema1:PropertyValueSpecification ;
    schema1:description "List of quality-control reference materials (secondary standards) routinely analyzed alongside unknowns." ;
    schema1:name "Secondary Reference Materials" ;
    schema1:readonlyValue true ;
    schema1:valueName "secondaryReferenceMaterial" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/BeamDamageMinimization> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 µm and 10 µm spot conditions" ;
    schema1:description "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals." ;
    schema1:name "Beam Damage Minimization" ;
    schema1:readonlyValue true ;
    schema1:valueName "BeamDamageMinimization" ;
    ada:dataType "string" ;
    ada:fieldScope "session" ;
    ada:tier "R" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/halogenOxygenCorrection> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Yes (F measured; Cl measured; OH by difference)" ;
    schema1:description "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases." ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:readonlyValue true ;
    schema1:valueName "halogenOxygenCorrection" ;
    ada:dataType "boolean" ;
    ada:fieldScope "session" ;
    ada:tier "R" .


```


### empaTAPP example P8sil: Zega et al. 2025 (Bennu silicates, Nat. Geosci.)
empaTAPP instance derived from publication Zega et al. 2025 (Bennu silicates, Nat. Geosci.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p8sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu silicates, sulfides, oxides",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu silicates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite,"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "~1 µm focused",
  "ada:beamCurrentDefault": "20 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p8sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu silicates, sulfides, oxides",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu silicates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite,"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "~1 \u00b5m focused",
  "ada:beamCurrentDefault": "20 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p8sil a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zega et al." ] ;
    schema1:description "empaTAPP example derived from Zega et al. 2025 (Bennu silicates, Nat. Geosci.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
            schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu silicates, sulfides, oxides" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite," ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "~1 µm focused" ;
    ada:beamMode "Focused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools; ZAF correction" ;
            ada:toolRole "reduction" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools (for phase maps)" ;
            ada:toolRole "acquisition" ] .


```


### empaTAPP example P8carb: Zega et al. 2025 (Bennu carbonates, Nat. Geosci.)
empaTAPP instance derived from publication Zega et al. 2025 (Bennu carbonates, Nat. Geosci.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p8carb",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu carbonates",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu carbonates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "carbonates (calcite, dolomite, magnesite)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "variable",
  "ada:beamCurrentDefault": "4 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p8carb",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu carbonates",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu carbonates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "carbonates (calcite, dolomite, magnesite)"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "variable",
  "ada:beamCurrentDefault": "4 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p8carb a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zega et al." ] ;
    schema1:description "empaTAPP example derived from Zega et al. 2025 (Bennu carbonates, Nat. Geosci.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
            schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu carbonates" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "carbonates (calcite, dolomite, magnesite)" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "4 nA" ;
    ada:beamDiameterDefault "variable" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools (for phase maps)" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools; ZAF correction" ;
            ada:toolRole "reduction" ] .


```


### empaTAPP example P8phos: Zega et al. 2025 (Bennu phosphates, Nat. Geosci.)
empaTAPP instance derived from publication Zega et al. 2025 (Bennu phosphates, Nat. Geosci.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p8phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu  phosphates",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu phosphates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "phosphates"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "variable",
  "ada:beamCurrentDefault": "8 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p8phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu  phosphates",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu phosphates, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "phosphates"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools (for phase maps)",
      "ada:toolRole": "acquisition"
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "XMapTools; ZAF correction",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "variable",
  "ada:beamCurrentDefault": "8 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p8phos a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zega et al." ] ;
    schema1:description "empaTAPP example derived from Zega et al. 2025 (Bennu phosphates, Nat. Geosci.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
            schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu  phosphates" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "phosphates" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "8 nA" ;
    ada:beamDiameterDefault "variable" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools (for phase maps)" ;
            ada:toolRole "acquisition" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "XMapTools; ZAF correction" ;
            ada:toolRole "reduction" ] .


```


### empaTAPP example P9sil: McCoy et al. 2025 (Bennu silicates, Nature)
empaTAPP instance derived from publication McCoy et al. 2025 (Bennu silicates, Nature). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p9sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap  silicates, oxides",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu silicates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sheet silicates, pyrrhotite, pentlandite, magnetite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 F+ Hyperprobe FEG (Smithsonian)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1 µm",
  "ada:beamCurrentDefault": "10 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p9sil",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap  silicates, oxides",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu silicates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Sheet silicates, pyrrhotite, pentlandite, magnetite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 F+ Hyperprobe FEG (Smithsonian)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1 \u00b5m",
  "ada:beamCurrentDefault": "10 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p9sil a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "McCoy et al." ] ;
    schema1:description "empaTAPP example derived from McCoy et al. 2025 (Bennu silicates, Nature)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ElectronSource" ;
                    schema1:name "Field Emission (FEG)" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL; Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8530 F+ Hyperprobe FEG (Smithsonian)" ] ;
            schema1:name "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu evap  silicates, oxides" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Sheet silicates, pyrrhotite, pentlandite, magnetite" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "10 nA" ;
    ada:beamDiameterDefault "1 µm" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "ZAF correction procedure" ;
            ada:toolRole "reduction" ] .


```


### empaTAPP example P9carb: McCoy et al. 2025 (Bennu carbonates, Nature)
empaTAPP instance derived from publication McCoy et al. 2025 (Bennu carbonates, Nature). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p9carb",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap carbonates",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu carbonates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "calcite, dolomite, magnesite, Na carbonate"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 (U of Arizona)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "5 µm",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Na",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "albite"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "dolomite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "calcite"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Mn carbonate"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "apatite"
      },
      {
        "analyte": "S",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "baryte"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "fayalite"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p9carb",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap carbonates",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu carbonates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "calcite, dolomite, magnesite, Na carbonate"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 (U of Arizona)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "5 \u00b5m",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "Na",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "albite"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "dolomite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "calcite"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Mn carbonate"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "apatite"
      },
      {
        "analyte": "S",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "baryte"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "fayalite"
      }
    ]
  }
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

ex:empaTAPP-p9carb a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "McCoy et al." ] ;
    schema1:description "empaTAPP example derived from McCoy et al. 2025 (Bennu carbonates, Nature)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ElectronSource" ;
                    schema1:name "Field Emission (FEG)" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL; Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 (U of Arizona)" ] ;
            schema1:name "JEOL; Cameca Cameca SX-100 (U of Arizona)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu evap carbonates" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "calcite, dolomite, magnesite, Na carbonate" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "10 nA" ;
    ada:beamDiameterDefault "5 µm" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "ZAF correction procedure" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P9phos: McCoy et al. 2025 (Bennu phosphates, Nature)
empaTAPP instance derived from publication McCoy et al. 2025 (Bennu phosphates, Nature). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p9phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap phosphates",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu phosphates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Mg Phosphate, Na phosphate"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 (U of Arizona)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Defocused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 µm",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "P",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "rhodonite"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "fayalite"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "anorthite"
      },
      {
        "analyte": "S",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "baryte"
      },
      {
        "analyte": "K",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "K-feldspar"
      },
      {
        "analyte": "Cl",
        "epmaTechnique": "√",
        "primaryCalibrationStandard": "scapolite"
      }
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
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p9phos",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA Bennu evap phosphates",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu phosphates, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Mg Phosphate, Na phosphate"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 (U of Arizona)"
    },
    "schema:hasPart": [
      {
        "@type": [
          "schema:Thing",
          "schema:Product"
        ],
        "schema:additionalType": [
          "ElectronSource"
        ],
        "schema:name": "Field Emission (FEG)"
      }
    ]
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Defocused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 \u00b5m",
  "ada:beamCurrentDefault": "10 nA",
  "ada:analyteTemplate": {
    "ada:analyteColumns": [
      {
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Analyzed constituent",
        "schema:valueName": "analyte",
        "schema:description": "Analyzed constituent identified by the analyte row.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name"
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/epmaTechnique",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "EPMA Technique per Element",
        "schema:valueName": "epmaTechnique",
        "schema:description": "Whether this element was measured by WDS or EDS.",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M",
        "schema:inDefinedTermSet": {
          "@id": "ada:vocab/empaTAPP/epmaTechnique"
        }
      },
      {
        "@id": "ada:analyteColumn/empaTAPP/primaryCalibrationStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "Primary Calibration Standard Name",
        "schema:valueName": "primaryCalibrationStandard",
        "schema:description": "Primary reference material used for element standardization (calibration).",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "ada:tier": "M"
      }
    ],
    "ada:defaultAnalytes": [
      {
        "analyte": "F",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "P",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "Ca",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "fluorapatite"
      },
      {
        "analyte": "Si",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mg",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "Fo92 olivine"
      },
      {
        "analyte": "Mn",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "rhodonite"
      },
      {
        "analyte": "Fe",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "fayalite"
      },
      {
        "analyte": "Al",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "anorthite"
      },
      {
        "analyte": "S",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "baryte"
      },
      {
        "analyte": "K",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "K-feldspar"
      },
      {
        "analyte": "Cl",
        "epmaTechnique": "\u221a",
        "primaryCalibrationStandard": "scapolite"
      }
    ]
  }
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

ex:empaTAPP-p9phos a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "McCoy et al." ] ;
    schema1:description "empaTAPP example derived from McCoy et al. 2025 (Bennu phosphates, Nature)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ElectronSource" ;
                    schema1:name "Field Emission (FEG)" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL; Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 (U of Arizona)" ] ;
            schema1:name "JEOL; Cameca Cameca SX-100 (U of Arizona)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA Bennu evap phosphates" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "Mg Phosphate, Na phosphate" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:description "Analyzed constituent identified by the analyte row." ;
                    schema1:name "Analyzed constituent" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique>,
                <https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> ;
            ada:defaultAnalytes [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ] ;
    ada:beamCurrentDefault "10 nA" ;
    ada:beamDiameterDefault "2 µm" ;
    ada:beamMode "Defocused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "ZAF correction procedure" ;
            ada:toolRole "reduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/epmaTechnique> a schema1:PropertyValueSpecification ;
    schema1:description "Whether this element was measured by WDS or EDS." ;
    schema1:inDefinedTermSet <https://ada.astromat.org/metadata/vocab/empaTAPP/epmaTechnique> ;
    schema1:name "EPMA Technique per Element" ;
    schema1:readonlyValue true ;
    schema1:valueName "epmaTechnique" ;
    ada:dataType "string" ;
    ada:tier "M" .

<https://ada.astromat.org/metadata/analyteColumn/empaTAPP/primaryCalibrationStandard> a schema1:PropertyValueSpecification ;
    schema1:description "Primary reference material used for element standardization (calibration)." ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:readonlyValue true ;
    schema1:valueName "primaryCalibrationStandard" ;
    ada:dataType "string" ;
    ada:tier "M" .


```


### empaTAPP example P10: Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)
empaTAPP instance derived from publication Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p10",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS eucrite major/minor element minerals",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
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
      "schema:name": "JEOL 8100"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 focused",
  "ada:beamCurrentDefault": "20 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p10",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS eucrite major/minor element minerals",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
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
      "schema:name": "JEOL 8100"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 focused",
  "ada:beamCurrentDefault": "20 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p10 a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Pang et al." ] ;
    schema1:description "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8100" ] ;
            schema1:name "JEOL JEOL 8100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanjing University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS eucrite major/minor element minerals" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "0 focused" ;
    ada:beamMode "Focused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "ZAF correction procedure" ;
            ada:toolRole "reduction" ] .


```


### empaTAPP example P10plag: Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.)
empaTAPP instance derived from publication Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p10plag",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS eucrite  plagioclase and polymorphs",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "plagioclase,  tissintite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
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
      "schema:name": "JEOL 8100"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2–5 µm defocused",
  "ada:beamCurrentDefault": "20 nA"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p10plag",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS eucrite  plagioclase and polymorphs",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:creator": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:object": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "plagioclase,  tissintite"
    }
  ],
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
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
      "schema:name": "JEOL 8100"
    }
  },
  "bios:computationalTool": [
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "ZAF correction procedure",
      "ada:toolRole": "reduction"
    }
  ],
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2\u20135 \u00b5m defocused",
  "ada:beamCurrentDefault": "20 nA"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:empaTAPP-p10plag a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Pang et al." ] ;
    schema1:description "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8100" ] ;
            schema1:name "JEOL JEOL 8100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanjing University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS eucrite  plagioclase and polymorphs" ;
    schema1:object [ a schema1:DefinedTerm ;
            schema1:name "plagioclase,  tissintite" ] ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "2–5 µm defocused" ;
    bios:computationalTool [ a schema1:SoftwareApplication ;
            schema1:name "ZAF correction procedure" ;
            ada:toolRole "reduction" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMPA Technique-Aligned Protocol Profile (empaTAPP)
description: EMPA-specific extension of the base TAPP definition. Adds top-level EPMA
  properties (beam mode, accelerating voltage default, matrix correction method, etc.),
  a parameter vocabulary in ada:methodParameters, and an analyte-column template covering
  EPMA per-element acquisition and reporting fields. Each ada:analyteColumns[] entry
  must match one of the catalog files in analyteColumns/ (or the inherited identifier
  column from tappDefinition); each catalog file is itself a JSON Schema whose examples[0]
  carries the canonical instance. Generated from docs/TAPP_EPMA_filled.xlsx by tools/build_empaTAPP_from_spreadsheet.py.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/tappDefinition/schema.yaml
- type: object
  properties:
    ada:beamMode:
      description: Whether the beam was focused, defocused, or rastered over an area.
      type: string
      enum:
      - Focused
      - Defocused
      - Raster
    ada:acceleratingVoltageDefault:
      description: Electron beam accelerating voltage in kilovolts (kV).
      type: string
    ada:beamDiameterDefault:
      description: Diameter of the focused or defocused electron beam in micrometers.
      type: string
    ada:beamCurrentDefault:
      description: Probe current in nanoamperes (nA).
      type: string
    ada:matrixCorrectionMethod:
      description: X-ray matrix correction algorithm applied during data reduction.
      type: string
      enum:
      - PAP (Pouchou & Pichoir Full)
      - XPP (Simplified PAP)
      - PhiRhoZ Bastin (EPQ-91)
      - Love-Scott I
      - Love-Scott II
      - Armstrong/Love-Scott
      - Heinrich/Duncumb-Reed
      - Conventional Philibert/Duncumb-Reed
      - Other
      - Unknown
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analysisOrder
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCorrectionMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCountingPosition
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCountingTime
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/blankCorrection
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimitMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/edsDeadTime
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/elementEstimationMethod
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/epmaTechnique
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferenceCorrection
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferenceCorrectionStandard
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferingElements
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/monochromatorCrystal
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/normalization-standardsCorrection
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/peakCountingTime
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/primaryCalibrationStandard
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/pulseHeightAnalyzeSetting
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/secondaryReferenceMaterial
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spectrometerNumber
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/timeDependentIntensityCorrection
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalAnalyticalAccuracy
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalAnalyticalPrecision
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalCountingStatisticsError
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalDetectionLimit
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/wdsDetectorType
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/xrayEmissionLine
          allOf:
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/analysisOrder
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCorrectionMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCountingPosition
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/backgroundCountingTime
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/blankCorrection
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/detectionLimitMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/edsDeadTime
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/elementEstimationMethod
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/epmaTechnique
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferenceCorrection
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferenceCorrectionStandard
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/interferingElements
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/monochromatorCrystal
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/normalization-standardsCorrection
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/peakCountingTime
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/primaryCalibrationStandard
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/pulseHeightAnalyzeSetting
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/secondaryReferenceMaterial
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/spectrometerNumber
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/timeDependentIntensityCorrection
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalAnalyticalAccuracy
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalAnalyticalPrecision
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalCountingStatisticsError
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/typicalDetectionLimit
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/wdsDetectorType
            minContains: 0
            maxContains: 1
          - contains:
              $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/analyteColumns/schema.yaml#/$defs/xrayEmissionLine
            minContains: 0
            maxContains: 1
    ada:methodParameters:
      type: array
      items:
        anyOf:
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/BeamDamageMinimization
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/DriftCorrection
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/edsSpectralProcessingType
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/halogenOxygenCorrection
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/massAbsorptionCoefficients
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/wdsDeadTimeCorrection
      allOf:
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/BeamDamageMinimization
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/DriftCorrection
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/edsSpectralProcessingType
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/halogenOxygenCorrection
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/massAbsorptionCoefficients
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterTemplates/schema.yaml#/$defs/wdsDeadTimeCorrection
        minContains: 0
        maxContains: 1
    schema:instrument:
      type: object
      properties:
        schema:hasPart:
          type: array
          description: 'Instrument sub-components. Each item is a schema:Thing with
            at least one schema:additionalType. Spreadsheet-known types: ElectronSource,
            edsDetector, wdsSpectrometer. Other additionalType values are accepted
            via the catch-all branch.'
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
                    const: ElectronSource
                schema:name:
                  type: string
                  enum:
                  - Field Emission (FEG)
                  - LaB6/CeB6
                  - Tungsten (W)
                  - Other
                  - Unknown
              required:
              - '@type'
              - schema:additionalType
              - schema:name
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
                    const: wdsSpectrometer
              required:
              - '@type'
              - schema:additionalType
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
                    const: edsDetector
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
                        const: ElectronSource
                    - contains:
                        const: wdsSpectrometer
                    - contains:
                        const: edsDetector
              required:
              - '@type'
              - schema:additionalType

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/context.jsonld)

## Sources

* [TAPP_EPMA_filled.xlsx (Components / TAPP worksheet)](https://github.com/usgin/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/techniqueProtocols/empaTAPP`

