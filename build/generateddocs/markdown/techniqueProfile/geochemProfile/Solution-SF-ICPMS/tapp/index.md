
# Solution SF-ICP-MS Technique-Aligned Protocol Profile (solutionSficpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.tapp` *v0.1*

Solution sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from docs/Solution_SF-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### solutionSficpmsTAPP example P0
solutionSficpmsTAPP instance derived from Desem+etal2022 | Nu Attom SC-SF-ICP-MS | Univ Melbourne.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — P0",
  "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3) Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero (10 s wash blank before each measurement; stated section 2.3).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Pb isotopes (204Pb, 206Pb, 207Pb, 208Pb) with mass fractionation monitors 202Hg",
      "203Tl",
      "205Tl (stated section 2.3)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Soil samples (sequential acid leach fractions; stated abstract)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Sequential acid leaching of bulk soil (TD and AR fractions; stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Aqua regia (AR fraction); HF-HNO3 for residue (stated section 2.2)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)",
        "schema:description": "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:finalSolutionMatrix": "2% HNO3 + 1 ppb Tl (stated section 2.3)",
  "ada:chromatographicSeparationApplied": "None (Pb separation performed for MC-ICP-MS only; SF-ICP-MS uses unseparated leachate with Tl addition; stated section 2.3)",
  "ada:isotopeDilutionSpike": "None (Tl added for mass fractionation correction only, not ID)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM; deflector peak jump mode for Pb isotopes (stated section 2.3)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Glass Expansion glass nebulizer (stated section 2.3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Glass Expansion cyclonic spray chamber (stated section 2.3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.33,
              "schema:description": "0.33 ml/min (stated section 2.3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/ICP-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Interface-Cone"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Nu Instruments -- \"a Nu Instruments Attom SC-SF-ICP-MS\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Melbourne, Australia (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "2000 sweeps per set x 30 sets (stated section 2.3)",
  "ada:numberOfReplicatesPerSample": "1 (30 sets of 2000 sweeps = single 4.5 min continuous analysis; stated section 2.3)",
  "ada:washTimeBetweenSamples": "10 s in two 2% HNO3 reservoirs (stated section 2.3)",
  "ada:internalStandardElement": "Tl (203Tl and 205Tl for mass fractionation correction; stated section 2.3)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/internalStandardConcentration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "internalStandardConcentration",
      "schema:name": "Internal Standard Concentration",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:value": 1,
      "schema:description": "1 ppb Tl in sample matrix (stated section 2.3)"
    }
  ],
  "ada:primaryStandardNameDefault": "NIST SRM981 Common Lead Standard (stated section 2.3)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "N/A",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "On-peak zero",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb -- dimensionless isotope ratios"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 P0",
  "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3) Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero (10 s wash blank before each measurement; stated section 2.3).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Pb isotopes (204Pb, 206Pb, 207Pb, 208Pb) with mass fractionation monitors 202Hg",
      "203Tl",
      "205Tl (stated section 2.3)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Soil samples (sequential acid leach fractions; stated abstract)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Sequential acid leaching of bulk soil (TD and AR fractions; stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Aqua regia (AR fraction); HF-HNO3 for residue (stated section 2.2)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)",
        "schema:description": "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:finalSolutionMatrix": "2% HNO3 + 1 ppb Tl (stated section 2.3)",
  "ada:chromatographicSeparationApplied": "None (Pb separation performed for MC-ICP-MS only; SF-ICP-MS uses unseparated leachate with Tl addition; stated section 2.3)",
  "ada:isotopeDilutionSpike": "None (Tl added for mass fractionation correction only, not ID)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM; deflector peak jump mode for Pb isotopes (stated section 2.3)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Glass Expansion glass nebulizer (stated section 2.3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Glass Expansion cyclonic spray chamber (stated section 2.3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.33,
              "schema:description": "0.33 ml/min (stated section 2.3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/ICP-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Interface-Cone"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Nu Instruments -- \"a Nu Instruments Attom SC-SF-ICP-MS\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Melbourne, Australia (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "2000 sweeps per set x 30 sets (stated section 2.3)",
  "ada:numberOfReplicatesPerSample": "1 (30 sets of 2000 sweeps = single 4.5 min continuous analysis; stated section 2.3)",
  "ada:washTimeBetweenSamples": "10 s in two 2% HNO3 reservoirs (stated section 2.3)",
  "ada:internalStandardElement": "Tl (203Tl and 205Tl for mass fractionation correction; stated section 2.3)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/internalStandardConcentration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "internalStandardConcentration",
      "schema:name": "Internal Standard Concentration",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:value": 1,
      "schema:description": "1 ppb Tl in sample matrix (stated section 2.3)"
    }
  ],
  "ada:primaryStandardNameDefault": "NIST SRM981 Common Lead Standard (stated section 2.3)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "N/A",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "On-peak zero",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb -- dimensionless isotope ratios"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-P0 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Aqua regia (AR fraction); HF-HNO3 for residue (stated section 2.2)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Sequential acid leaching of bulk soil (TD and AR fractions; stated section 2.2)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3) Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero (10 s wash blank before each measurement; stated section 2.3)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Melbourne, Australia (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P0" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Soil samples (sequential acid leach fractions; stated abstract)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)" ;
                    schema1:name "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "203Tl",
                "205Tl (stated section 2.3)",
                "Pb isotopes (204Pb, 206Pb, 207Pb, 208Pb) with mass fractionation monitors 202Hg" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler" ;
    ada:blankBackgroundCorrectionMethod "On-peak zero" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None (Pb separation performed for MC-ICP-MS only; SF-ICP-MS uses unseparated leachate with Tl addition; stated section 2.3)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "2% HNO3 + 1 ppb Tl (stated section 2.3)" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Tl (203Tl and 205Tl for mass fractionation correction; stated section 2.3)" ;
    ada:isotopeDilutionSpike "None (Tl added for mass fractionation correction only, not ID)" ;
    ada:numberOfReplicatesPerSample "1 (30 sets of 2000 sweeps = single 4.5 min continuous analysis; stated section 2.3)" ;
    ada:numberOfScansPerReplicate "2000 sweeps per set x 30 sets (stated section 2.3)" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "NIST SRM981 Common Lead Standard (stated section 2.3)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb -- dimensionless isotope ratios" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"" ;
    ada:secondaryReferenceMaterialDefault "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "10 s in two 2% HNO3 reservoirs (stated section 2.3)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:description "1 ppb Tl in sample matrix (stated section 2.3)" ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value 1 ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Glass Expansion glass nebulizer (stated section 2.3)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3.3e-01 ;
    schema1:description "0.33 ml/min (stated section 2.3)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Glass Expansion cyclonic spray chamber (stated section 2.3)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nu Instruments -- \"a Nu Instruments Attom SC-SF-ICP-MS\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM; deflector peak jump mode for Pb isotopes (stated section 2.3)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .


```


### solutionSficpmsTAPP example P1
solutionSficpmsTAPP instance derived from Li+etal2016 | Thermo Element I | IGGCAS Beijing.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — P1",
  "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = IS normalization (103Rh; stated Table 1); ada:perAnalyteCalibrationStrategy = External calibration with IS normalization (stated Table 1); ada:blankBackgroundCorrectionMethod = Solution blank (stated section 2.3).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Trace elements: REEs",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Li",
      "Rb",
      "Sr",
      "Cs",
      "Ba (stated section 2.3.2)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.96,
              "schema:description": "0.96 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14.6,
              "schema:description": "14.6 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (sampling gas; Table 1)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 200,
              "schema:description": "200 uL/min (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Element I HR-ICP-MS (stated Table 1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, pulse counting only (stated Table 1: counting mode)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (Table 1)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"An Inductively Coupled Sector Plasma Mass Spectrometer (Element I, ThermoFisher, USA)\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Magnetite and pyrite (mineral separates from skarn deposits; stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 100,
          "schema:description": "~100 mg mineral powder (stated section 2.3)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Step 1: 6M HCl (1.5 ml) + 8M HNO3 (0.5 ml); Step 2: 10M HCl (1.5 ml) for re-dissolution; stated section 2.3.1",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "15 mL Teflon capsule (stated section 2.3)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 2,
            "schema:description": "2 (step 1: 6M HCl + 8M HNO3 at 130 deg C / 48 h; step 2: evaporate + re-dissolve in 10M HCl; both steps explicitly described; stated section 2.3.1)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "48 h (stated section 2.3)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 deg C (stated section 2.3)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "2% HNO3 + 5 ng/ml Rh (stated section 2.3)",
  "ada:chromatographicSeparationApplied": "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)",
  "ada:isotopeDilutionSpike": "None (external calibration used; stated section 2.3)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
  },
  "ada:washTimeBetweenSamples": "60 s (Table 1)",
  "ada:internalStandardElement": "Rh (103Rh; Table 1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/internalStandardConcentration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "internalStandardConcentration",
      "schema:name": "Internal Standard Concentration",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:value": 5,
      "schema:description": "5 ng/ml Rh (stated section 2.3)"
    }
  ],
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Solution blank",
  "ada:secondaryReferenceMaterialDefault": [
    "FER-2 and geological RMs in Table 5 (BHVO-2, BCR-2, etc.; stated section 2.3.2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Mass fractions of Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Rb, Sr, Ge, Cs, Ba, Y and the REE; detection limits in ng mL-1 [Table 2]. Concentration unit is not stated in the Table 4 header"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 P1",
  "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = IS normalization (103Rh; stated Table 1); ada:perAnalyteCalibrationStrategy = External calibration with IS normalization (stated Table 1); ada:blankBackgroundCorrectionMethod = Solution blank (stated section 2.3).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Trace elements: REEs",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Li",
      "Rb",
      "Sr",
      "Cs",
      "Ba (stated section 2.3.2)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.96,
              "schema:description": "0.96 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14.6,
              "schema:description": "14.6 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (sampling gas; Table 1)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 200,
              "schema:description": "200 uL/min (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Element I HR-ICP-MS (stated Table 1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, pulse counting only (stated Table 1: counting mode)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (Table 1)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"An Inductively Coupled Sector Plasma Mass Spectrometer (Element I, ThermoFisher, USA)\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Magnetite and pyrite (mineral separates from skarn deposits; stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 100,
          "schema:description": "~100 mg mineral powder (stated section 2.3)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Step 1: 6M HCl (1.5 ml) + 8M HNO3 (0.5 ml); Step 2: 10M HCl (1.5 ml) for re-dissolution; stated section 2.3.1",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "15 mL Teflon capsule (stated section 2.3)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 2,
            "schema:description": "2 (step 1: 6M HCl + 8M HNO3 at 130 deg C / 48 h; step 2: evaporate + re-dissolve in 10M HCl; both steps explicitly described; stated section 2.3.1)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "48 h (stated section 2.3)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 deg C (stated section 2.3)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "2% HNO3 + 5 ng/ml Rh (stated section 2.3)",
  "ada:chromatographicSeparationApplied": "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)",
  "ada:isotopeDilutionSpike": "None (external calibration used; stated section 2.3)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
  },
  "ada:washTimeBetweenSamples": "60 s (Table 1)",
  "ada:internalStandardElement": "Rh (103Rh; Table 1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/internalStandardConcentration",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "internalStandardConcentration",
      "schema:name": "Internal Standard Concentration",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:value": 5,
      "schema:description": "5 ng/ml Rh (stated section 2.3)"
    }
  ],
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Solution blank",
  "ada:secondaryReferenceMaterialDefault": [
    "FER-2 and geological RMs in Table 5 (BHVO-2, BCR-2, etc.; stated section 2.3.2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Mass fractions of Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Rb, Sr, Ge, Cs, Ba, Y and the REE; detection limits in ng mL-1 [Table 2]. Concentration unit is not stated in the Table 4 header"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-P1 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Mineral separates (~100 mg powder; stated section 2.3)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Step 1: 6M HCl (1.5 ml) + 8M HNO3 (0.5 ml); Step 2: 10M HCl (1.5 ml) for re-dissolution; stated section 2.3.1" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = IS normalization (103Rh; stated Table 1); ada:perAnalyteCalibrationStrategy = External calibration with IS normalization (stated Table 1); ada:blankBackgroundCorrectionMethod = Solution blank (stated section 2.3)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Magnetite and pyrite (mineral separates from skarn deposits; stated abstract)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Ba (stated section 2.3.2)",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Li",
                "Ni",
                "Rb",
                "Sr",
                "Trace elements: REEs",
                "Zn" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\"" ;
    ada:blankBackgroundCorrectionMethod "Solution blank" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)" ;
    ada:driftCorrectionMethod "IS normalization" ;
    ada:finalSolutionMatrix "2% HNO3 + 5 ng/ml Rh (stated section 2.3)" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Rh (103Rh; Table 1)" ;
    ada:isotopeDilutionSpike "None (external calibration used; stated section 2.3)" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Mass fractions of Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Rb, Sr, Ge, Cs, Ba, Y and the REE; detection limits in ng mL-1 [Table 2]. Concentration unit is not stated in the Table 4 header" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"" ;
    ada:secondaryReferenceMaterialDefault "FER-2 and geological RMs in Table 5 (BHVO-2, BCR-2, etc.; stated section 2.3.2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "60 s (Table 1)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "48 h (stated section 2.3)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 130 ;
    schema1:description "130 deg C (stated section 2.3)" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "15 mL Teflon capsule (stated section 2.3)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:description "5 ng/ml Rh (stated section 2.3)" ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value 5 ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.90 L/min (sampling gas; Table 1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:description "2 (step 1: 6M HCl + 8M HNO3 at 130 deg C / 48 h; step 2: evaporate + re-dissolve in 10M HCl; both steps explicitly described; stated section 2.3.1)" ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value 2 ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 mg mineral powder (stated section 2.3)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 200 ;
    schema1:description "200 uL/min (Table 1)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9.6e-01 ;
    schema1:description "0.96 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.46e+01 ;
    schema1:description "14.6 L/min (Table 1)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "60 s wash between samples (Table 1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1300 ;
    schema1:description "1300 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Element I HR-ICP-MS (stated Table 1)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific -- \"An Inductively Coupled Sector Plasma Mass Spectrometer (Element I, ThermoFisher, USA)\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM, pulse counting only (stated Table 1: counting mode)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1300 W; Table 1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni sampler and Ni skimmer (Table 1)" .


```


### solutionSficpmsTAPP example P2
solutionSficpmsTAPP instance derived from Lu+etal2007 | Finnigan ELEMENT | PML Okayama.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — P2",
  "schema:description": "Continuous nebulization (not pFI) for SF-ICP-MS; background measured before each sample after HF wash; sapphire injector used (HF-resistant); 60 s uptake stabilization; stated section 2.1.2 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.2); ada:perAnalyteCalibrationStrategy = Isotope dilution with Nb as ID internal standard for Ti (stated section 2.1.2).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Ti (47Ti, 49Ti) with Nb (93Nb) as ID-IS",
      "stated section 2.1.2"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1.1 kW; stated section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.1,
              "schema:description": "1.1 kW (stated Table in section 2.1.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz glass torch with sapphire injector (stated Table in section 2.1.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (stated Table in section 2.1.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Scott double-pass, uncooled, Teflon (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 60,
              "schema:description": "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        }
      ],
      "schema:model": {
        "schema:name": "Finnigan ELEMENT sector-field ICP-MS (stated section 2.1.2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, pulse counting (stated section 2.1.2)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "MR (M/Delta-m = 3000; stated section 2.1.2)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "200 s wash with 0.5 mol/l HF before each sample (stated section 2.1.2)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"(b) ICP-SFMS, Finnigan ELEMENT\"; stated as \"Finnigan ELEMENT\", the pre-Thermo brand name",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Geological reference materials and carbonaceous chondrites (basalt, andesite, peridotite, chondrites; stated section 2.5)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations with Nb as ID internal standard for Ti (stated section 2.1.2)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- the ID equation is built on spike and natural isotope ratios, and the mixed standard solution is referenced to the B isotope ratio standard of Makishima et al. (1997). No constant values or their sources are tabulated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "0.5 mol/l HF (same as Q-ICP-MS portion; stated section 2.1.1)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFM bomb (TFM-981; stated section 2.1.1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "SF-ICP-MS (ELEMENT) measured Ti (47Ti, 49Ti) by ID; Q-ICP-MS (7500cs) measured all other elements; both on same digested solutions; stated section 2.1"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
  },
  "ada:numberOfScansPerReplicate": "30 scans in 50 s (stated section 2.1.2)",
  "ada:sampleSequenceDesign": "Standard solution measured every two samples; background measured before each sample (stated section 2.1.2)",
  "ada:washTimeBetweenSamples": "~200 s (background measured after 200 s wash before each sample; stated section 2.1.2)",
  "ada:internalStandardElement": "Nb (93Nb as ID internal standard for Ti; stated section 2.1.2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.2)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:secondaryReferenceMaterialDefault": [
    "USGS and GSJ geological RMs and carbonaceous chondrites (stated section 2.5)"
  ],
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.2)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Ti and Nb mass fractions by ICP-SFMS (ug g-1); TiO2 also reported; detection limits in solution (ng g-1) and in rock (ug g-1) [Table 2b]"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:finalSolutionMatrix": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:primaryStandardNameDefault": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 P2",
  "schema:description": "Continuous nebulization (not pFI) for SF-ICP-MS; background measured before each sample after HF wash; sapphire injector used (HF-resistant); 60 s uptake stabilization; stated section 2.1.2 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.2); ada:perAnalyteCalibrationStrategy = Isotope dilution with Nb as ID internal standard for Ti (stated section 2.1.2).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Ti (47Ti, 49Ti) with Nb (93Nb) as ID-IS",
      "stated section 2.1.2"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1.1 kW; stated section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.1,
              "schema:description": "1.1 kW (stated Table in section 2.1.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz glass torch with sapphire injector (stated Table in section 2.1.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (stated Table in section 2.1.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Scott double-pass, uncooled, Teflon (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 60,
              "schema:description": "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        }
      ],
      "schema:model": {
        "schema:name": "Finnigan ELEMENT sector-field ICP-MS (stated section 2.1.2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, pulse counting (stated section 2.1.2)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "MR (M/Delta-m = 3000; stated section 2.1.2)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "200 s wash with 0.5 mol/l HF before each sample (stated section 2.1.2)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"(b) ICP-SFMS, Finnigan ELEMENT\"; stated as \"Finnigan ELEMENT\", the pre-Thermo brand name",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Geological reference materials and carbonaceous chondrites (basalt, andesite, peridotite, chondrites; stated section 2.5)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations with Nb as ID internal standard for Ti (stated section 2.1.2)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- the ID equation is built on spike and natural isotope ratios, and the mixed standard solution is referenced to the B isotope ratio standard of Makishima et al. (1997). No constant values or their sources are tabulated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "0.5 mol/l HF (same as Q-ICP-MS portion; stated section 2.1.1)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFM bomb (TFM-981; stated section 2.1.1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "SF-ICP-MS (ELEMENT) measured Ti (47Ti, 49Ti) by ID; Q-ICP-MS (7500cs) measured all other elements; both on same digested solutions; stated section 2.1"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
  },
  "ada:numberOfScansPerReplicate": "30 scans in 50 s (stated section 2.1.2)",
  "ada:sampleSequenceDesign": "Standard solution measured every two samples; background measured before each sample (stated section 2.1.2)",
  "ada:washTimeBetweenSamples": "~200 s (background measured after 200 s wash before each sample; stated section 2.1.2)",
  "ada:internalStandardElement": "Nb (93Nb as ID internal standard for Ti; stated section 2.1.2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.2)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:secondaryReferenceMaterialDefault": [
    "USGS and GSJ geological RMs and carbonaceous chondrites (stated section 2.5)"
  ],
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.2)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Ti and Nb mass fractions by ICP-SFMS (ug g-1); TiO2 also reported; detection limits in solution (ng g-1) and in rock (ug g-1) [Table 2b]"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:finalSolutionMatrix": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:primaryStandardNameDefault": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-P2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "0.5 mol/l HF (same as Q-ICP-MS portion; stated section 2.1.1)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Continuous nebulization (not pFI) for SF-ICP-MS; background measured before each sample after HF wash; sapphire injector used (HF-resistant); 60 s uptake stabilization; stated section 2.1.2 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.2); ada:perAnalyteCalibrationStrategy = Isotope dilution with Nb as ID internal standard for Ti (stated section 2.1.2)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Geological reference materials and carbonaceous chondrites (basalt, andesite, peridotite, chondrites; stated section 2.5)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "SF-ICP-MS (ELEMENT) measured Ti (47Ti, 49Ti) by ID; Q-ICP-MS (7500cs) measured all other elements; both on same digested solutions; stated section 2.1" ;
                    schema1:name "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Ti (47Ti, 49Ti) with Nb (93Nb) as ID-IS",
                "stated section 2.1.2" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\"" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "Every two samples (stated section 2.1.2)" ;
    ada:chromatographicSeparationApplied "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)" ;
    ada:driftCorrectionMethod "Standard bracketing" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Nb (93Nb as ID internal standard for Ti; stated section 2.1.2)" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate "30 scans in 50 s (stated section 2.1.2)" ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 1% (stated section 2.1.2)" ;
    ada:perAnalyteCalibrationStrategy "Isotope dilution (all analytes)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Ti and Nb mass fractions by ICP-SFMS (ug g-1); TiO2 also reported; detection limits in solution (ng g-1) and in rock (ug g-1) [Table 2b]" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "Standard solution measured every two samples; background measured before each sample (stated section 2.1.2)" ;
    ada:samplingUnit "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites" ;
    ada:secondaryReferenceMaterialDefault "USGS and GSJ geological RMs and carbonaceous chondrites (stated section 2.5)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "~200 s (background measured after 200 s wash before each sample; stated section 2.1.2)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- the ID equation is built on spike and natural isotope ratios, and the mixed standard solution is referenced to the B isotope ratio standard of Makishima et al. (1997). No constant values or their sources are tabulated" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "TFM bomb (TFM-981; stated section 2.1.1)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.90 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.2)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 60 ;
    schema1:description "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Scott double-pass, uncooled, Teflon (stated Table in section 2.1.2)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 14 ;
    schema1:description "14 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "MR (M/Delta-m = 3000; stated section 2.1.2)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "200 s wash with 0.5 mol/l HF before each sample (stated section 2.1.2)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.1e+00 ;
    schema1:description "1.1 kW (stated Table in section 2.1.2)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Finnigan ELEMENT sector-field ICP-MS (stated section 2.1.2)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "Quartz glass torch with sapphire injector (stated Table in section 2.1.2)" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific -- \"(b) ICP-SFMS, Finnigan ELEMENT\"; stated as \"Finnigan ELEMENT\", the pre-Thermo brand name" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM, pulse counting (stated section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "IUPAC isotope dilution equations with Nb as ID internal standard for Ti (stated section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1.1 kW; stated section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni sampler and Ni skimmer (stated Table in section 2.1.2)" .


```


### solutionSficpmsTAPP example P3
solutionSficpmsTAPP instance derived from Milne+etal2010 | Thermo Finnigan Element I | FSU NHMFL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — P3",
  "schema:description": "Off-line pre-concentration by chelating resin essential for open-ocean seawater; enriched isotope spikes added before chelation (pre-equilibration); standard addition for Mn and Co (no suitable spike isotope); stated section 2.2 Reported detail: ada:blankBackgroundCorrectionMethod = Procedural blank (stated section 2.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mn (55Mn)",
      "Fe (57Fe)",
      "Co (59Co)",
      "Ni (62Ni)",
      "Cu (65Cu)",
      "Zn (68Zn)",
      "Cd (111Cd)",
      "Pb (207Pb) in seawater (stated Table 1)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.05,
              "schema:description": "1.05 L/min (varied and optimized daily; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 13,
              "schema:description": "13 L/min (Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni/Cu sampler and Ni skimmer (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "PFA microflow PFA-100 (Elemental Scientific; Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "PFA Teflon Savillex 100 mL with internal baffle (Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (varied and optimized daily; Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 150,
              "schema:description": "150 uL/min (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Finnigan Element I (E1) HR-ICP-MS (stated section 2.4)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, dual mode (stated section 2.4)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a Thermo-Finnigan Element I (E1) HR-ICP-MS\"; \"Instrument ThermoFinnigan Element1\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Open-ocean seawater (stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 12,
          "schema:description": "12 mL seawater (stated section 2.2)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations (stated section 2.1)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample digestion",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "1.0 M HNO3 (trace elements eluted from chelating resin in 1 mL; stated section 2.2)",
  "ada:chromatographicSeparationApplied": "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)",
  "ada:isotopeDilutionSpike": "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
  },
  "ada:internalStandardElement": "None (ID method used; no external IS; stated section 2.1)",
  "ada:oxideProductionMethodAndThreshold": "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)",
  "ada:primaryStandardNameDefault": "Commercial standard of natural isotopic abundance (not formally named; stated section 2.4)",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "Procedural blank",
  "ada:secondaryReferenceMaterialDefault": [
    "NASS-5 (certified seawater); SAFe inter-comparison samples S1 and D2 (stated section 2.4)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Dissolved Mn, Fe, Co, Ni, Cu, Zn, Cd and Pb concentrations in nM"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:washTimeBetweenSamples": -9999,
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 P3",
  "schema:description": "Off-line pre-concentration by chelating resin essential for open-ocean seawater; enriched isotope spikes added before chelation (pre-equilibration); standard addition for Mn and Co (no suitable spike isotope); stated section 2.2 Reported detail: ada:blankBackgroundCorrectionMethod = Procedural blank (stated section 2.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mn (55Mn)",
      "Fe (57Fe)",
      "Co (59Co)",
      "Ni (62Ni)",
      "Cu (65Cu)",
      "Zn (68Zn)",
      "Cd (111Cd)",
      "Pb (207Pb) in seawater (stated Table 1)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.05,
              "schema:description": "1.05 L/min (varied and optimized daily; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 13,
              "schema:description": "13 L/min (Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni/Cu sampler and Ni skimmer (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "PFA microflow PFA-100 (Elemental Scientific; Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "PFA Teflon Savillex 100 mL with internal baffle (Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (varied and optimized daily; Table 2)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 150,
              "schema:description": "150 uL/min (Table 2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Finnigan Element I (E1) HR-ICP-MS (stated section 2.4)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, dual mode (stated section 2.4)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a Thermo-Finnigan Element I (E1) HR-ICP-MS\"; \"Instrument ThermoFinnigan Element1\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Open-ocean seawater (stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 12,
          "schema:description": "12 mL seawater (stated section 2.2)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations (stated section 2.1)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample digestion",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "1.0 M HNO3 (trace elements eluted from chelating resin in 1 mL; stated section 2.2)",
  "ada:chromatographicSeparationApplied": "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)",
  "ada:isotopeDilutionSpike": "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
  },
  "ada:internalStandardElement": "None (ID method used; no external IS; stated section 2.1)",
  "ada:oxideProductionMethodAndThreshold": "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)",
  "ada:primaryStandardNameDefault": "Commercial standard of natural isotopic abundance (not formally named; stated section 2.4)",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "Procedural blank",
  "ada:secondaryReferenceMaterialDefault": [
    "NASS-5 (certified seawater); SAFe inter-comparison samples S1 and D2 (stated section 2.4)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Dissolved Mn, Fe, Co, Ni, Cu, Zn, Cd and Pb concentrations in nM"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:washTimeBetweenSamples": -9999,
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-P3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Off-line pre-concentration by chelating resin essential for open-ocean seawater; enriched isotope spikes added before chelation (pre-equilibration); standard addition for Mn and Co (no suitable spike isotope); stated section 2.2 Reported detail: ada:blankBackgroundCorrectionMethod = Procedural blank (stated section 2.1)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Open-ocean seawater (stated abstract)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Cd (111Cd)",
                "Co (59Co)",
                "Cu (65Cu)",
                "Fe (57Fe)",
                "Mn (55Mn)",
                "Ni (62Ni)",
                "Pb (207Pb) in seawater (stated Table 1)",
                "Zn (68Zn)" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\"" ;
    ada:blankBackgroundCorrectionMethod "Procedural blank" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "1.0 M HNO3 (trace elements eluted from chelating resin in 1 mL; stated section 2.2)" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "None (ID method used; no external IS; stated section 2.1)" ;
    ada:isotopeDilutionSpike "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate -9999 ;
    ada:oxideProductionMethodAndThreshold "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "Commercial standard of natural isotopic abundance (not formally named; stated section 2.4)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Dissolved Mn, Fe, Co, Ni, Cu, Zn, Cd and Pb concentrations in nM" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"" ;
    ada:secondaryReferenceMaterialDefault "NASS-5 (certified seawater); SAFe inter-comparison samples S1 and D2 (stated section 2.4)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (varied and optimized daily; Table 2)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "PFA microflow PFA-100 (Elemental Scientific; Table 2)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "12 mL seawater (stated section 2.2)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 uL/min (Table 2)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "PFA Teflon Savillex 100 mL with internal baffle (Table 2)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.05e+00 ;
    schema1:description "1.05 L/min (varied and optimized daily; Table 2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 13 ;
    schema1:description "13 L/min (Table 2)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR (R ~300) and MR (R ~4000; stated section 2.4)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1300 ;
    schema1:description "1300 W (Table 2)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Finnigan Element I (E1) HR-ICP-MS (stated section 2.4)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific -- \"a Thermo-Finnigan Element I (E1) HR-ICP-MS\"; \"Instrument ThermoFinnigan Element1\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM, dual mode (stated section 2.4)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "IUPAC isotope dilution equations (stated section 2.1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1300 W; Table 2)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni/Cu sampler and Ni skimmer (Table 2)" .


```


### solutionSficpmsTAPP example P4
solutionSficpmsTAPP instance derived from Misra+etal2014 | Thermo Element XR | Univ Cambridge.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-P4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — P4",
  "schema:description": "Thermo Element XR with Jet pump; extraction voltage 2000 V (Table 1); ESI Pt injector 1.8 mm ID; Pt cones; dual mode detector fixed per analyte; daily detector cross-calibration required (stated section 2.3.1) Reported detail: ada:driftCorrectionMethod = Standard bracketing (blocks of 7 samples bracketed by calibration standards; stated section 2.3.1); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 10 ppm Ca (all analytes; stated section 2.3.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Li",
      "B",
      "Na",
      "Mg",
      "Al",
      "Mn",
      "Fe",
      "Zn",
      "Sr",
      "Cd",
      "Ba",
      "U as Me/Ca ratios in foraminifera (stated section 2.3)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Foraminifera calcite (benthic and planktonic species; stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 1,
          "schema:description": "1-2 mg foraminifera shells (stated section 2.4)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Foraminifera shells cleaned and dissolved in minimum 1 M HNO3 then diluted (stated section 2.4)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: SEM-to-analog cross-calibration performed daily (stated section 2.3.1)"
          },
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "1 M HNO3 (minimum volume for dissolution; stated section 2.4)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 1,
            "schema:description": "1 (stated section 2.4)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "0.1 M HNO3 + 0.3 M HF (Table 1)",
  "ada:chromatographicSeparationApplied": "None (direct dissolution analysis; stated section 2.4)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Element XR single-collector SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Pt-normal sampler + Pt-H skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Pt sampler and Pt skimmer (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI 50 uL microconcentric nebulizer; self-aspirating (Table 1)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Teflon Scott-type single-pass (Savillex PFA; Table 1 footnote)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 50,
              "schema:description": "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1250 W; Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1250,
              "schema:description": "1250 W (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, dual mode (pulse counting + analog; fixed per analyte; Table 1)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR and MR (stated Table 1 and section 2.3)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "120 s washout (Table 1)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a Thermo Element XR, a single collector sector field high resolution inductively coupled plasma mass spectrometer\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "LR: 15 passes x 3 runs = 45 total; MR: 3 passes x 3 runs = 9 total (Table 3)",
  "ada:numberOfReplicatesPerSample": "3 runs (LR and MR; Table 3)",
  "ada:sampleSequenceDesign": "Blocks of 7 samples bracketed by pair of acid blanks and consistency standards (stated section 2.3.1)",
  "ada:washTimeBetweenSamples": "120 s (Table 1)",
  "ada:internalStandardElement": "None (matrix-matched external calibration; stated section 2.3.1)",
  "ada:oxideProductionMethodAndThreshold": "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)",
  "ada:primaryStandardNameDefault": "Series of matrix-matched standards at 10 ppm Ca (not formally named; stated section 2.3.1)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Four in-house foraminifera consistency standards (C. wuellerstorfi, Uvigerina spp., synthetic mix; stated section 2.2)"
  ],
  "ada:calibrationMeasurementFrequency": "Bracketing blocks of 7 samples (stated section 2.3.1)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "B/Ca and Me/Ca (Li, Mg, Al, Sr, Cd, Ba, U in low resolution; Na, Mn, Fe, Zn in medium resolution) in umol/mol and mmol/mol"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-P4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 P4",
  "schema:description": "Thermo Element XR with Jet pump; extraction voltage 2000 V (Table 1); ESI Pt injector 1.8 mm ID; Pt cones; dual mode detector fixed per analyte; daily detector cross-calibration required (stated section 2.3.1) Reported detail: ada:driftCorrectionMethod = Standard bracketing (blocks of 7 samples bracketed by calibration standards; stated section 2.3.1); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 10 ppm Ca (all analytes; stated section 2.3.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Li",
      "B",
      "Na",
      "Mg",
      "Al",
      "Mn",
      "Fe",
      "Zn",
      "Sr",
      "Cd",
      "Ba",
      "U as Me/Ca ratios in foraminifera (stated section 2.3)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Foraminifera calcite (benthic and planktonic species; stated abstract)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 1,
          "schema:description": "1-2 mg foraminifera shells (stated section 2.4)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Foraminifera shells cleaned and dissolved in minimum 1 M HNO3 then diluted (stated section 2.4)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: SEM-to-analog cross-calibration performed daily (stated section 2.3.1)"
          },
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "1 M HNO3 (minimum volume for dissolution; stated section 2.4)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 1,
            "schema:description": "1 (stated section 2.4)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "0.1 M HNO3 + 0.3 M HF (Table 1)",
  "ada:chromatographicSeparationApplied": "None (direct dissolution analysis; stated section 2.4)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Element XR single-collector SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Pt-normal sampler + Pt-H skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Pt sampler and Pt skimmer (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI 50 uL microconcentric nebulizer; self-aspirating (Table 1)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Teflon Scott-type single-pass (Savillex PFA; Table 1 footnote)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 50,
              "schema:description": "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1250 W; Table 1)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1250,
              "schema:description": "1250 W (Table 1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM, dual mode (pulse counting + analog; fixed per analyte; Table 1)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR and MR (stated Table 1 and section 2.3)"
        },
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "120 s washout (Table 1)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a Thermo Element XR, a single collector sector field high resolution inductively coupled plasma mass spectrometer\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "LR: 15 passes x 3 runs = 45 total; MR: 3 passes x 3 runs = 9 total (Table 3)",
  "ada:numberOfReplicatesPerSample": "3 runs (LR and MR; Table 3)",
  "ada:sampleSequenceDesign": "Blocks of 7 samples bracketed by pair of acid blanks and consistency standards (stated section 2.3.1)",
  "ada:washTimeBetweenSamples": "120 s (Table 1)",
  "ada:internalStandardElement": "None (matrix-matched external calibration; stated section 2.3.1)",
  "ada:oxideProductionMethodAndThreshold": "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)",
  "ada:primaryStandardNameDefault": "Series of matrix-matched standards at 10 ppm Ca (not formally named; stated section 2.3.1)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Four in-house foraminifera consistency standards (C. wuellerstorfi, Uvigerina spp., synthetic mix; stated section 2.2)"
  ],
  "ada:calibrationMeasurementFrequency": "Bracketing blocks of 7 samples (stated section 2.3.1)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "B/Ca and Me/Ca (Li, Mg, Al, Sr, Cd, Ba, U in low resolution; Na, Mn, Fe, Zn in medium resolution) in umol/mol and mmol/mol"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-P4 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "1 M HNO3 (minimum volume for dissolution; stated section 2.4)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Foraminifera shells cleaned and dissolved in minimum 1 M HNO3 then diluted (stated section 2.4)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Thermo Element XR with Jet pump; extraction voltage 2000 V (Table 1); ESI Pt injector 1.8 mm ID; Pt cones; dual mode detector fixed per analyte; daily detector cross-calibration required (stated section 2.3.1) Reported detail: ada:driftCorrectionMethod = Standard bracketing (blocks of 7 samples bracketed by calibration standards; stated section 2.3.1); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 10 ppm Ca (all analytes; stated section 2.3.1)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Foraminifera calcite (benthic and planktonic species; stated abstract)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Al",
                "B",
                "Ba",
                "Cd",
                "Fe",
                "Li",
                "Mg",
                "Mn",
                "Na",
                "Sr",
                "U as Me/Ca ratios in foraminifera (stated section 2.3)",
                "Zn" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Bracketing blocks of 7 samples (stated section 2.3.1)" ;
    ada:chromatographicSeparationApplied "None (direct dissolution analysis; stated section 2.4)" ;
    ada:driftCorrectionMethod "Standard bracketing" ;
    ada:finalSolutionMatrix "0.1 M HNO3 + 0.3 M HF (Table 1)" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "None (matrix-matched external calibration; stated section 2.3.1)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:numberOfReplicatesPerSample "3 runs (LR and MR; Table 3)" ;
    ada:numberOfScansPerReplicate "LR: 15 passes x 3 runs = 45 total; MR: 3 passes x 3 runs = 9 total (Table 3)" ;
    ada:oxideProductionMethodAndThreshold "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "Series of matrix-matched standards at 10 ppm Ca (not formally named; stated section 2.3.1)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "B/Ca and Me/Ca (Li, Mg, Al, Sr, Cd, Ba, U in low resolution; Na, Mn, Fe, Zn in medium resolution) in umol/mol and mmol/mol" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "Blocks of 7 samples bracketed by pair of acid blanks and consistency standards (stated section 2.3.1)" ;
    ada:samplingUnit "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"" ;
    ada:secondaryReferenceMaterialDefault "Four in-house foraminifera consistency standards (C. wuellerstorfi, Uvigerina spp., synthetic mix; stated section 2.2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "120 s (Table 1)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "ESI 50 uL microconcentric nebulizer; self-aspirating (Table 1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:description "1 (stated section 2.4)" ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value 1 ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1-2 mg foraminifera shells (stated section 2.4)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Teflon Scott-type single-pass (Savillex PFA; Table 1 footnote)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR and MR (stated Table 1 and section 2.3)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "120 s washout (Table 1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: SEM-to-analog cross-calibration performed daily (stated section 2.3.1)" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1250 ;
    schema1:description "1250 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Element XR single-collector SF-ICP-MS (stated section 2.3)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific -- \"a Thermo Element XR, a single collector sector field high resolution inductively coupled plasma mass spectrometer\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM, dual mode (pulse counting + analog; fixed per analyte; Table 1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Pt-normal sampler + Pt-H skimmer (Table 1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1250 W; Table 1)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Pt sampler and Pt skimmer (Table 1)" .


```


### solutionSficpmsTAPP example Willbold2005
solutionSficpmsTAPP instance derived from Willbold2005 | ThermoFinnigan ELEMENT2 | MPI Mainz.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:solutionSficpmsTAPP-Willbold2005",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol — Willbold2005",
  "schema:description": "Magnetic jump + electric scan mode: each peak monitored by E-scan for 100 ms dwell; 15 samples per peak; in-run Ru-Re for mass fractionation correction; DF ~21000 (LR) or ~1000 (HR) in 0.4 mol/l HNO3; stated section on instrumentation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "26 trace elements: Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Cs",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "Pb",
      "Th",
      "U (stated Table 2)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1235 W; Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1235,
              "schema:description": "1235 W (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI microconcentric Teflon nebulizer (stated section on instrumentation)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI Teflon spray chamber (stated section on instrumentation)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.0,
              "schema:description": "1.0 L/min (sample gas; Table 3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 100,
              "schema:description": "~100 uL/min (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "ThermoFinnigan ELEMENT2 (stated section on instrumentation)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a ThermoFinnigan ELEMENT2 mass spectrometer\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Geological reference materials (basalt, andesite, granite, shale, peridotite, NIST glass; stated Table 2)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 100,
          "schema:description": "~100 mg (stated sample prep section)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (~100 mg; stated section on sample preparation)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations for 12 elements; RSF ratio calibration for 14 elements (stated section on instrumentation)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\""
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "HF (1-2 ml) + HNO3 (0.2 ml; stated sample prep section)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "15 ml Savillex PFA beakers (non-refractory, hotplate); Parr bombs (refractory minerals; stated sample prep section)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "12 h (non-refractory, hotplate); 7 days (refractory, Parr bomb; stated sample prep section)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 deg C (hotplate, non-refractory); 180 deg C (Parr bomb, refractory; stated sample prep section)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "0.4 mol/l HNO3 (dilution factor ~21000 for LR, ~1000 for HR; stated sample prep section)",
  "ada:chromatographicSeparationApplied": "None (direct analysis; stated section on instrumentation)",
  "ada:isotopeDilutionSpike": "Multi-element spike (MES; enriched isotopes of Rb, Sr, Y, Zr, Nb, Cs, Ba, REE, Hf, Pb, Th, U; stated section on instrumentation)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "70-120 scans per analysis (stated section on instrumentation)",
  "ada:internalStandardElement": "Ru and Re (in-run mass fractionation correction; ~6 uL Ru-Re solution per dilution; stated section on instrumentation)",
  "ada:internalStandardApproach": "N/A",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Trace element mass fractions in ug g-1 -- Eqs (1) and (2) both return \"ug g-1\"; limits of detection as rock equivalents in ng g-1"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:washTimeBetweenSamples": -9999,
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-Willbold2005",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionSficpms protocol \u2014 Willbold2005",
  "schema:description": "Magnetic jump + electric scan mode: each peak monitored by E-scan for 100 ms dwell; 15 samples per peak; in-run Ru-Re for mass fractionation correction; DF ~21000 (LR) or ~1000 (HR) in 0.4 mol/l HNO3; stated section on instrumentation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "26 trace elements: Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Cs",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "Pb",
      "Th",
      "U (stated Table 2)"
    ],
    "ada:analyteColumns": [
      {
        "schema:valueName": "analyte",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1235 W; Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1235,
              "schema:description": "1235 W (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)"
            },
            {
              "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni sampler and Ni skimmer (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Interface-Cone",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerType",
              "schema:name": "Nebulizer Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI microconcentric Teflon nebulizer (stated section on instrumentation)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "ESI Teflon spray chamber (stated section on instrumentation)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "nebulizerGasFlowRateDefault",
              "schema:name": "Nebulizer Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.0,
              "schema:description": "1.0 L/min (sample gas; Table 3)"
            },
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 100,
              "schema:description": "~100 uL/min (Table 3)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
      "schema:model": {
        "schema:name": "ThermoFinnigan ELEMENT2 (stated section on instrumentation)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific -- \"a ThermoFinnigan ELEMENT2 mass spectrometer\"",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Geological reference materials (basalt, andesite, granite, shale, peridotite, NIST glass; stated Table 2)"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 100,
          "schema:description": "~100 mg (stated sample prep section)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (~100 mg; stated section on sample preparation)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations for 12 elements; RSF ratio calibration for 14 elements (stated section on instrumentation)"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated"
          },
          {
            "@id": "ada:parameter/module/Core/constantsReferenceValuesDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "constantsReferenceValuesDefault",
            "schema:name": "Constants Reference Values",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\""
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "HF (1-2 ml) + HNO3 (0.2 ml; stated sample prep section)",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "15 ml Savillex PFA beakers (non-refractory, hotplate); Parr bombs (refractory minerals; stated sample prep section)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "12 h (non-refractory, hotplate); 7 days (refractory, Parr bomb; stated sample prep section)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 deg C (hotplate, non-refractory); 180 deg C (Parr bomb, refractory; stated sample prep section)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:finalSolutionMatrix": "0.4 mol/l HNO3 (dilution factor ~21000 for LR, ~1000 for HR; stated sample prep section)",
  "ada:chromatographicSeparationApplied": "None (direct analysis; stated section on instrumentation)",
  "ada:isotopeDilutionSpike": "Multi-element spike (MES; enriched isotopes of Rb, Sr, Y, Zr, Nb, Cs, Ba, REE, Hf, Pb, Th, U; stated section on instrumentation)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
  },
  "ada:numberOfScansPerReplicate": "70-120 scans per analysis (stated section on instrumentation)",
  "ada:internalStandardElement": "Ru and Re (in-run mass fractionation correction; ~6 uL Ru-Re solution per dilution; stated section on instrumentation)",
  "ada:internalStandardApproach": "N/A",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Trace element mass fractions in ug g-1 -- Eqs (1) and (2) both return \"ug g-1\"; limits of detection as rock equivalents in ng g-1"
    ],
    "ada:reportedPropertyColumns": [
      {
        "schema:valueName": "reportedProperty",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnit": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:washTimeBetweenSamples": -9999,
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-Willbold2005 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder (~100 mg; stated section on sample preparation)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "HF (1-2 ml) + HNO3 (0.2 ml; stated sample prep section)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Magnetic jump + electric scan mode: each peak monitored by E-scan for 100 ms dwell; 15 samples per peak; in-run Ru-Re for mass fractionation correction; DF ~21000 (LR) or ~1000 (HR) in 0.4 mol/l HNO3; stated section on instrumentation" ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — Willbold2005" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Geological reference materials (basalt, andesite, granite, shale, peridotite, NIST glass; stated Table 2)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "26 trace elements: Rb",
                "Ba",
                "Ce",
                "Cs",
                "Dy",
                "Er",
                "Eu",
                "Gd",
                "Hf",
                "Ho",
                "La",
                "Lu",
                "Nb",
                "Nd",
                "Pb",
                "Pr",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Tm",
                "U (stated Table 2)",
                "Y",
                "Yb",
                "Zr" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None (direct analysis; stated section on instrumentation)" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "0.4 mol/l HNO3 (dilution factor ~21000 for LR, ~1000 for HR; stated sample prep section)" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Ru and Re (in-run mass fractionation correction; ~6 uL Ru-Re solution per dilution; stated section on instrumentation)" ;
    ada:isotopeDilutionSpike "Multi-element spike (MES; enriched isotopes of Rb, Sr, Y, Zr, Nb, Cs, Ba, REE, Hf, Pb, Th, U; stated section on instrumentation)" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate "70-120 scans per analysis (stated section on instrumentation)" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Trace element mass fractions in ug g-1 -- Eqs (1) and (2) both return \"ug g-1\"; limits of detection as rock equivalents in ng g-1" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"" ;
    ada:secondaryReferenceMaterialDefault "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\"" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "12 h (non-refractory, hotplate); 7 days (refractory, Parr bomb; stated sample prep section)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 130 ;
    schema1:description "130 deg C (hotplate, non-refractory); 180 deg C (Parr bomb, refractory; stated sample prep section)" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "15 ml Savillex PFA beakers (non-refractory, hotplate); Parr bombs (refractory minerals; stated sample prep section)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1e+00 ;
    schema1:description "1.0 L/min (sample gas; Table 3)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "ESI microconcentric Teflon nebulizer (stated section on instrumentation)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 mg (stated sample prep section)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 uL/min (Table 3)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "ESI Teflon spray chamber (stated section on instrumentation)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.9 L/min (Table 3)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (Table 3)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1235 ;
    schema1:description "1235 W (Table 3)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ThermoFinnigan ELEMENT2 (stated section on instrumentation)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific -- \"a ThermoFinnigan ELEMENT2 mass spectrometer\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "IUPAC isotope dilution equations for 12 elements; RSF ratio calibration for 14 elements (stated section on instrumentation)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1235 W; Table 3)" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni sampler and Ni skimmer (Table 3)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution SF-ICP-MS Technique-Aligned Protocol Profile (solutionSficpmsTAPP)
description: Solution sector-field (high-resolution) ICP-MS extension of the base
  TAPP definition, generated from tapp/Current TAPPs/Solution_SF-ICP-MS_TAPP_v32.csv
  via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: ICPMS
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: ICP Source
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: auxiliaryGasFlowRateDefault
                                schema:name:
                                  const: Auxiliary Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: L/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            - title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: coolantGasFlowRateDefault
                                schema:name:
                                  const: Coolant (Plasma) Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: L/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            - title: Plasma Thermal Mode
                              description: "Whether the ICP plasma is operated under
                                cool plasma or normal (hot) plasma conditions. Normal
                                plasma (>1000 W RF) is standard for most solution
                                SF-ICP-MS analyses. Cool plasma (\u2264900 W RF) reduces
                                argide-based interferences (e.g., 40Ar12C+ on 52Cr)
                                at the cost of reduced sensitivity and ionization
                                efficiency for most elements."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/plasmaThermalMode
                                schema:name:
                                  const: Plasma Thermal Mode
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            - title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/rfPowerDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: rfPowerDefault
                                schema:name:
                                  const: RF Power
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: W
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                          allOf:
                          - contains:
                              title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: auxiliaryGasFlowRateDefault
                                schema:name:
                                  const: Auxiliary Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: L/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/coolantGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: coolantGasFlowRateDefault
                                schema:name:
                                  const: Coolant (Plasma) Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: L/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Plasma Thermal Mode
                              description: "Whether the ICP plasma is operated under
                                cool plasma or normal (hot) plasma conditions. Normal
                                plasma (>1000 W RF) is standard for most solution
                                SF-ICP-MS analyses. Cool plasma (\u2264900 W RF) reduces
                                argide-based interferences (e.g., 40Ar12C+ on 52Cr)
                                at the cost of reduced sensitivity and ionization
                                efficiency for most elements."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/plasmaThermalMode
                                schema:name:
                                  const: Plasma Thermal Mode
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/rfPowerDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: rfPowerDefault
                                schema:name:
                                  const: RF Power
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: W
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            minContains: 0
                            maxContains: 1
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Torch
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Type of plasma torch used (e.g., standard quartz,
                            high-matrix, low-flow).
                          anyOf:
                          - type: string
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              readOnly: true
                        schema:additionalProperty:
                          type: array
                          items:
                            title: Torch Depth
                            description: Distance between the load coil and the sampling
                              cone tip (mm), also called injector depth or torch position
                              depending on the instrument manufacturer. Affects ion
                              transmission efficiency, oxide formation, and doubly-charged
                              species production. The procedure specifies a target
                              value optimised during initial setup; the analyst confirms
                              or fine-adjusts during session tuning.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/solutionSficpmsTAPP/torchDepthDefault
                              '@type':
                                const:
                                - schema:PropertyValueSpecification
                              schema:valueName:
                                const: torchDepthDefault
                              schema:name:
                                const: Torch Depth
                              ada:dataType:
                                const: string
                              ada:fieldScope:
                                const: session
                              schema:readonlyValue:
                                const: false
                              ada:tier:
                                const: R
                            required:
                            - '@id'
                            - '@type'
                            - schema:valueName
                            - schema:name
                            - ada:dataType
                            - ada:fieldScope
                          allOf:
                          - contains:
                              title: Torch Depth
                              description: Distance between the load coil and the
                                sampling cone tip (mm), also called injector depth
                                or torch position depending on the instrument manufacturer.
                                Affects ion transmission efficiency, oxide formation,
                                and doubly-charged species production. The procedure
                                specifies a target value optimised during initial
                                setup; the analyst confirms or fine-adjusts during
                                session tuning.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/torchDepthDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: torchDepthDefault
                                schema:name:
                                  const: Torch Depth
                                ada:dataType:
                                  const: string
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            minContains: 0
                            maxContains: 1
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Interface Cone
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Interface Cone Configuration
                              description: Geometry and designation of the sampler
                                and skimmer cones installed during analysis. Some
                                SF-ICP-MS instruments offer multiple cone geometries
                                that differ in aperture size and affect ion transmission
                                efficiency and matrix tolerance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration
                                schema:name:
                                  const: Interface Cone Configuration
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            - title: Sampler and Skimmer Cone Material
                              description: Material composition of the sampler and
                                skimmer cones. Nickel (Ni) is standard for most aqueous
                                matrices. Aluminium (Al) cones are used in some SF-ICP-MS
                                labs for enhanced sensitivity at high resolution.
                                Platinum (Pt) is used for HCl-rich matrices.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial
                                schema:name:
                                  const: Sampler and Skimmer Cone Material
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                          allOf:
                          - contains:
                              title: Interface Cone Configuration
                              description: Geometry and designation of the sampler
                                and skimmer cones installed during analysis. Some
                                SF-ICP-MS instruments offer multiple cone geometries
                                that differ in aperture size and affect ion transmission
                                efficiency and matrix tolerance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/interfaceConeConfiguration
                                schema:name:
                                  const: Interface Cone Configuration
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Sampler and Skimmer Cone Material
                              description: Material composition of the sampler and
                                skimmer cones. Nickel (Ni) is standard for most aqueous
                                matrices. Aluminium (Al) cones are used in some SF-ICP-MS
                                labs for enhanced sensitivity at high resolution.
                                Platinum (Pt) is used for HCl-rich matrices.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/samplerAndSkimmerConeMaterial
                                schema:name:
                                  const: Sampler and Skimmer Cone Material
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            minContains: 0
                            maxContains: 1
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Sample Introduction System
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerType
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sprayChamberTypeAndCoolingTemperature
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleUptakeRate
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerType
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sprayChamberTypeAndCoolingTemperature
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleUptakeRate
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: ICP Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Interface Cone
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Sample Introduction System
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Doubly-Charged Species Monitor
                    description: Mass ratio monitored to estimate doubly-charged ion
                      (M2+) formation during instrument tuning. Doubly-charged ions
                      appear at half the nominal mass of the parent ion and can interfere
                      with lighter analyte masses. In SF-ICP-MS, doubly-charged species
                      are not suppressed by collision cells and require monitoring
                      through plasma tuning. Ba2+/Ba+ (m/z 69/138) is the most common
                      proxy.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitorDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: doublyChargedSpeciesMonitorDefault
                      schema:name:
                        const: Doubly-Charged Species Monitor
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Detector Configuration
                    description: 'Type(s) of detector(s) installed in the mass spectrometer
                      and the detection mode(s) used. SF-ICP-MS instruments typically
                      use a single SEM. Some instruments (e.g., Thermo Element XR)
                      support triple mode: pulse counting for low signals, analog
                      for mid-range signals, and Faraday cup for high signals. The
                      cross-calibration correction between detector modes is documented
                      in Group 5.'
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionSficpmsTAPP/detectorConfiguration
                      schema:name:
                        const: Detector Configuration
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                    readOnly: true
                  - title: Doubly-Charged Species Production
                    description: Measured percentage of doubly-charged ion production
                      for the monitored species at the time of instrument tuning.
                      Record both the acceptance threshold and the measured value.
                      Elevated doubly-charged production indicates incomplete ionization
                      and potential interference on elements at approximately half
                      the mass of abundant matrix components.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProductionDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: doublyChargedSpeciesProductionDefault
                      schema:name:
                        const: Doubly-Charged Species Production
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: instrumentSerialNumberOrLabIdentifierDefault
                      schema:name:
                        const: Instrument Serial Number or Lab Identifier
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Make-up Gas and Flow Rate
                    description: "Supplementary gas added to the sample-carrying stream
                      between the sample introduction system and the plasma, with
                      its identity and the procedure-registered target flow rate.
                      Argon make-up is standard and maintains total gas delivery where
                      the carrier flow alone is insufficient \u2014 downstream of
                      an ablation cell, or of a desolvation system that has removed
                      solvent load. Small nitrogen or hydrogen additions are also
                      made here to enhance sensitivity for some elements; record them
                      with their own flow, whose unit commonly differs from the make-up
                      flow. Record 'None' explicitly where no supplementary gas is
                      added, to distinguish it from not reported."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRateDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: makeUpGasAndFlowRateDefault
                      schema:name:
                        const: Make-up Gas and Flow Rate
                      ada:dataType:
                        const: number
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                      schema:unitText:
                        const: L/min
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Mass Resolution Setting
                    description: "Mass resolution mode(s) used in this procedure.
                      Sector-field instruments allow selection of low resolution (LR;
                      m/\u0394m \u2248 300\u2013400), medium resolution (MR; m/\u0394m
                      \u2248 2500\u20135000), or high resolution (HR; m/\u0394m \u2248
                      10,000). Multi-resolution procedures assign individual analytes
                      to specific modes (documented in Group 4 under Mass Resolution
                      Assignment). Procedure registers the mode(s) in use; analyst
                      confirms at session start."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSettingDefault
                      schema:name:
                        const: Mass Resolution Setting
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Memory Effect Mitigation
                    description: Procedure applied to identify and minimize carry-over
                      of high-concentration elements between successive sample introductions.
                      For solution ICP-MS, mitigation is implemented primarily at
                      measurement time through extended rinse periods (see Wash Time
                      Between Samples, Group 4). At data processing level, documents
                      any flagging or exclusion of measurements preceded by high-concentration
                      samples or standards where the required washout time may not
                      have been achieved.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: memoryEffectMitigationDefault
                      schema:name:
                        const: Memory Effect Mitigation
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                allOf:
                - contains:
                    title: Doubly-Charged Species Monitor
                    description: Mass ratio monitored to estimate doubly-charged ion
                      (M2+) formation during instrument tuning. Doubly-charged ions
                      appear at half the nominal mass of the parent ion and can interfere
                      with lighter analyte masses. In SF-ICP-MS, doubly-charged species
                      are not suppressed by collision cells and require monitoring
                      through plasma tuning. Ba2+/Ba+ (m/z 69/138) is the most common
                      proxy.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitorDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: doublyChargedSpeciesMonitorDefault
                      schema:name:
                        const: Doubly-Charged Species Monitor
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Detector Configuration
                    description: 'Type(s) of detector(s) installed in the mass spectrometer
                      and the detection mode(s) used. SF-ICP-MS instruments typically
                      use a single SEM. Some instruments (e.g., Thermo Element XR)
                      support triple mode: pulse counting for low signals, analog
                      for mid-range signals, and Faraday cup for high signals. The
                      cross-calibration correction between detector modes is documented
                      in Group 5.'
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionSficpmsTAPP/detectorConfiguration
                      schema:name:
                        const: Detector Configuration
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                    readOnly: true
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Doubly-Charged Species Production
                    description: Measured percentage of doubly-charged ion production
                      for the monitored species at the time of instrument tuning.
                      Record both the acceptance threshold and the measured value.
                      Elevated doubly-charged production indicates incomplete ionization
                      and potential interference on elements at approximately half
                      the mass of abundant matrix components.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProductionDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: doublyChargedSpeciesProductionDefault
                      schema:name:
                        const: Doubly-Charged Species Production
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: instrumentSerialNumberOrLabIdentifierDefault
                      schema:name:
                        const: Instrument Serial Number or Lab Identifier
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Make-up Gas and Flow Rate
                    description: "Supplementary gas added to the sample-carrying stream
                      between the sample introduction system and the plasma, with
                      its identity and the procedure-registered target flow rate.
                      Argon make-up is standard and maintains total gas delivery where
                      the carrier flow alone is insufficient \u2014 downstream of
                      an ablation cell, or of a desolvation system that has removed
                      solvent load. Small nitrogen or hydrogen additions are also
                      made here to enhance sensitivity for some elements; record them
                      with their own flow, whose unit commonly differs from the make-up
                      flow. Record 'None' explicitly where no supplementary gas is
                      added, to distinguish it from not reported."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRateDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: makeUpGasAndFlowRateDefault
                      schema:name:
                        const: Make-up Gas and Flow Rate
                      ada:dataType:
                        const: number
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                      schema:unitText:
                        const: L/min
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Mass Resolution Setting
                    description: "Mass resolution mode(s) used in this procedure.
                      Sector-field instruments allow selection of low resolution (LR;
                      m/\u0394m \u2248 300\u2013400), medium resolution (MR; m/\u0394m
                      \u2248 2500\u20135000), or high resolution (HR; m/\u0394m \u2248
                      10,000). Multi-resolution procedures assign individual analytes
                      to specific modes (documented in Group 4 under Mass Resolution
                      Assignment). Procedure registers the mode(s) in use; analyst
                      confirms at session start."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/massResolutionSettingDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSettingDefault
                      schema:name:
                        const: Mass Resolution Setting
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Memory Effect Mitigation
                    description: Procedure applied to identify and minimize carry-over
                      of high-concentration elements between successive sample introductions.
                      For solution ICP-MS, mitigation is implemented primarily at
                      measurement time through extended rinse periods (see Wash Time
                      Between Samples, Group 4). At data processing level, documents
                      any flagging or exclusion of measurements preceded by high-concentration
                      samples or standards where the required washout time may not
                      have been achieved.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: memoryEffectMitigationDefault
                      schema:name:
                        const: Memory Effect Mitigation
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: ICPMS
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    schema:object:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              '@type':
                contains:
                  const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
            required:
            - '@type'
          then:
            properties:
              schema:additionalProperty:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:name:
                          const: Target Material
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:value:
                          type: array
                          items:
                            description: General description of the material type(s)
                              this procedure is designed to analyse. Used for discoverability
                              and procedure matching, and because the material type
                              constrains sample preparation, calibration and matrix-matching
                              requirements.
                            anyOf:
                            - type: string
                              enum:
                              - Basalt
                              - Chondrite
                              - Peridotite
                              - Synthetic solution
                              - N/A
                              - None
                              - missing
                            - type: string
                            readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Target Material
                    required:
                    - schema:name
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleAliquotMassOrVolume
                  minContains: 0
                  maxContains: 1
      allOf:
      - contains:
          properties:
            '@type':
              contains:
                const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
          required:
          - '@type'
    schema:actionProcess:
      type: object
      properties:
        schema:step:
          type: array
          items:
            type: object
            allOf:
            - if:
                properties:
                  schema:name:
                    const: Sample preparation
                required:
                - schema:name
              then:
                properties:
                  schema:description:
                    description: General approach to mechanical sample preparation
                      prior to dissolution (e.g., whole-rock crushing and powdering,
                      mineral separation). Documents how the solid material was conditioned
                      before acid digestion.
                    anyOf:
                    - type: string
                      readOnly: true
                    - type: array
                      items:
                        type: string
                        readOnly: true
            - if:
                properties:
                  schema:name:
                    const: Sample digestion
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionVesselType
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_numberOfDigestionSteps
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionVesselType
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_numberOfDigestionSteps
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                      minContains: 0
                      maxContains: 1
            - if:
                properties:
                  schema:name:
                    const: Data acquisition
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      title: Guard Electrode
                      description: Whether a guard electrode (grounded shield electrode)
                        is installed and active on the torch assembly. Capacitively
                        decouples the plasma from the load coil, reducing secondary
                        discharge and improving ion extraction efficiency. Actively
                        used as a design feature on Thermo Element 2 and Element XR
                        instruments.
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/solutionSficpmsTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/solutionSficpmsTAPP/guardElectrode
                        schema:name:
                          const: Guard Electrode
                        schema:value:
                          type: string
                      required:
                      - '@id'
                      - '@type'
                      - schema:propertyID
                      - schema:name
                      - schema:value
                      readOnly: true
                    allOf:
                    - contains:
                        title: Guard Electrode
                        description: Whether a guard electrode (grounded shield electrode)
                          is installed and active on the torch assembly. Capacitively
                          decouples the plasma from the load coil, reducing secondary
                          discharge and improving ion extraction efficiency. Actively
                          used as a design feature on Thermo Element 2 and Element
                          XR instruments.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionSficpmsTAPP/guardElectrode
                          schema:name:
                            const: Guard Electrode
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      minContains: 0
                      maxContains: 1
            - if:
                properties:
                  schema:name:
                    const: Data reduction
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied to output
                          concentrations relative to a reference value (e.g., correction
                          to a BHVO-2 working value).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: normalizationStandardsBasedCorrectionDefault
                          schema:name:
                            const: Normalization / Standards-Based Correction
                          ada:dataType:
                            const: string
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                        required:
                        - '@id'
                        - '@type'
                        - schema:valueName
                        - schema:name
                        - ada:dataType
                        - ada:fieldScope
                      - title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog (and Faraday, for triple-mode instruments) detection
                          modes. For SF-ICP-MS instruments, the signal transitions
                          between pulse counting (low concentrations) and analog detection
                          (high concentrations). For triple-mode instruments (e.g.,
                          Thermo Element XR), an additional transition to Faraday
                          cup detection occurs at the highest signal intensities.
                          Cross-calibration factors between detector modes must be
                          confirmed, typically measured each session.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: pulseAnalogDetectorNonlinearityCorrectionDefault
                          schema:name:
                            const: Pulse/Analog Detector Nonlinearity Correction
                          ada:dataType:
                            const: string
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                        required:
                        - '@id'
                        - '@type'
                        - schema:valueName
                        - schema:name
                        - ada:dataType
                        - ada:fieldScope
                      - title: Isotope Dilution Data Reduction Method
                        description: "Mass balance approach used to calculate sample
                          mass fractions from spike\u2013sample isotope ratio measurements.
                          Spike must have been added before digestion for accurate
                          equilibration. Record 'None' if isotope dilution is not
                          used."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod
                          schema:name:
                            const: Isotope Dilution Data Reduction Method
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied to output
                          concentrations relative to a reference value (e.g., correction
                          to a BHVO-2 working value).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: normalizationStandardsBasedCorrectionDefault
                          schema:name:
                            const: Normalization / Standards-Based Correction
                          ada:dataType:
                            const: string
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                        required:
                        - '@id'
                        - '@type'
                        - schema:valueName
                        - schema:name
                        - ada:dataType
                        - ada:fieldScope
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog (and Faraday, for triple-mode instruments) detection
                          modes. For SF-ICP-MS instruments, the signal transitions
                          between pulse counting (low concentrations) and analog detection
                          (high concentrations). For triple-mode instruments (e.g.,
                          Thermo Element XR), an additional transition to Faraday
                          cup detection occurs at the highest signal intensities.
                          Cross-calibration factors between detector modes must be
                          confirmed, typically measured each session.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: pulseAnalogDetectorNonlinearityCorrectionDefault
                          schema:name:
                            const: Pulse/Analog Detector Nonlinearity Correction
                          ada:dataType:
                            const: string
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                        required:
                        - '@id'
                        - '@type'
                        - schema:valueName
                        - schema:name
                        - ada:dataType
                        - ada:fieldScope
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Isotope Dilution Data Reduction Method
                        description: "Mass balance approach used to calculate sample
                          mass fractions from spike\u2013sample isotope ratio measurements.
                          Spike must have been added before digestion for accurate
                          equilibration. Record 'None' if isotope dilution is not
                          used."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionSficpmsTAPP/isotopeDilutionDataReductionMethod
                          schema:name:
                            const: Isotope Dilution Data Reduction Method
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      minContains: 0
                      maxContains: 1
          allOf:
          - contains:
              properties:
                schema:name:
                  const: Sample preparation
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Sample digestion
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Data acquisition
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        - title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Varies the accelerating voltage to
            cover masses in the vicinity of the set magnetic mass without re-scanning
            the magnet. Record 'N/A' if E-scan acquisition mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionSficpmsTAPP/eScanRange
            schema:name:
              const: E-scan Range
            schema:value:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          - schema:unitText
          readOnly: true
        - title: Triple Scanning Mode
          description: Whether each mass peak is scanned three times per cycle and
            the results averaged (Y/N). Used to reduce noise from short-term magnetic
            field instabilities on sector-field instruments. Triple scanning affects
            the effective integration time per cycle and should be reported. Record
            'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionSficpmsTAPP/tripleScanningMode
            schema:name:
              const: Triple Scanning Mode
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_internalStandardConcentration
        - title: Spike / Outlier Filtering Approach
          description: Criteria used to identify and exclude anomalous replicate measurements
            or data points from the calculated mean.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproachDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: spikeOutlierFilteringApproachDefault
            schema:name:
              const: Spike / Outlier Filtering Approach
            ada:dataType:
              const: string
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Uncertainty Propagation Method
          description: 'The approach used to propagate analytical uncertainty through
            the data reduction chain to the final reported value. State which sources
            are included in the propagation: counting statistics, calibration standard
            uncertainty, internal standard uncertainty, drift correction, and any
            systematic contributions. Distinct from Uncertainty Level, which states
            the convention at which the resulting uncertainty is quoted.'
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: uncertaintyPropagationMethodDefault
            schema:name:
              const: Uncertainty Propagation Method
            ada:dataType:
              const: string
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
      allOf:
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        minContains: 0
        maxContains: 1
      - contains:
          title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Varies the accelerating voltage to
            cover masses in the vicinity of the set magnetic mass without re-scanning
            the magnet. Record 'N/A' if E-scan acquisition mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionSficpmsTAPP/eScanRange
            schema:name:
              const: E-scan Range
            schema:value:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          - schema:unitText
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          title: Triple Scanning Mode
          description: Whether each mass peak is scanned three times per cycle and
            the results averaged (Y/N). Used to reduce noise from short-term magnetic
            field instabilities on sector-field instruments. Triple scanning affects
            the effective integration time per cycle and should be reported. Record
            'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionSficpmsTAPP/tripleScanningMode
            schema:name:
              const: Triple Scanning Mode
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_internalStandardConcentration
        minContains: 0
        maxContains: 1
      - contains:
          title: Spike / Outlier Filtering Approach
          description: Criteria used to identify and exclude anomalous replicate measurements
            or data points from the calculated mean.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproachDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: spikeOutlierFilteringApproachDefault
            schema:name:
              const: Spike / Outlier Filtering Approach
            ada:dataType:
              const: string
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
      - contains:
          title: Uncertainty Propagation Method
          description: 'The approach used to propagate analytical uncertainty through
            the data reduction chain to the final reported value. State which sources
            are included in the propagation: counting statistics, calibration standard
            uncertainty, internal standard uncertainty, drift correction, and any
            systematic contributions. Distinct from Uncertainty Level, which states
            the convention at which the resulting uncertainty is quoted.'
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: uncertaintyPropagationMethodDefault
            schema:name:
              const: Uncertainty Propagation Method
            ada:dataType:
              const: string
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the analyte element they serve where they serve one. Covers atomic
                isotopes and, where a reaction cell shifts an analyte onto a different
                mass, the product mass actually measured. Includes interference-monitor
                and internal-standard masses, which serve no analyte and so have no
                parent element. The analyte list is given by the Analyte field and
                is never inferred from the element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: monitoredMasses
                schema:name:
                  const: Monitored Masses
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Mass Resolution Assignment
              description: Mass resolution mode assigned to each acquired mass. The
                selected resolution determines which polyatomic interferences are
                physically resolved by the magnetic sector. One analyte may be acquired
                at more than one resolution, so the assignment is per acquired mass
                rather than per element. The overall mode(s) used in the procedure
                are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: massResolutionAssignment
                schema:name:
                  const: Mass Resolution Assignment
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Dwell Time per Mass
              description: Integration time spent on each mass peak per sweep (ms).
                May differ between masses where per-mass dwell times are programmed.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Isobaric Interference Corrections Applied
              description: Whether mathematical corrections for residual isobaric
                or polyatomic interferences are applied in data reduction (supplementary
                to any interference suppression achieved through mass resolution selection).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interfering Species
              description: List of isobaric or polyatomic species mathematically corrected
                in data reduction. In SF-ICP-MS, mass resolution is the primary interference
                mitigation strategy; mathematical corrections address residual interferences
                not resolved at the operating resolution.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingSpecies
                schema:name:
                  const: Interfering Species
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interference Correction Method
              description: Mathematical approach used to calculate and remove residual
                interference contributions from measured signals. In SF-ICP-MS, interference
                solutions isolating specific polyatomic species are measured alongside
                samples and used to calibrate correction factors.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionMethod
                schema:name:
                  const: Interference Correction Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set). Specify units
                (\xB5g/g or \xB5g/L) and whether values are procedure-typical estimates
                or session-specific measured values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/detectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimit
                schema:name:
                  const: Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Detection Limit Method
              description: Method used to calculate detection limits for each reported
                concentration variable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Limit of Quantification (LOQ) Method
              description: Method used to determine the limit of quantification.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: limitOfQuantificationMethod
                schema:name:
                  const: Limit of Quantification (LOQ) Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Within-Session Analytical Precision and Assessment Method
              description: Precision of repeated measurements within a single analytical
                session and the method used to assess it. Report both the assessment
                method and the precision values. The assessment method must specify
                the reference material or standard measured, the number of replicates
                n, and the statistic reported (1s RSD, 2s RSD, 2SD, 2SE, 95% CI).
                Distinct from the internal precision of a single measurement, which
                derives from counting statistics over the cycles of that measurement
                rather than from repeated analyses.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: withinSessionAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Within-Session Analytical Precision and Assessment Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Between-Session (Long-Term) Analytical Precision and Assessment
                Method
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported. Long-term precision is normally poorer than within-session
                precision and is the figure a data user should carry when comparing
                results from different sessions."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: betweenSessionAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Between-Session (Long-Term) Analytical Precision and Assessment
                    Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Analytical Accuracy and Assessment Method
              description: Accuracy of final concentration measurements relative to
                certified or consensus values and the method used to assess it.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracyAndAssessmentMethod
                schema:name:
                  const: Analytical Accuracy and Assessment Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
          allOf:
          - contains:
              title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the analyte element they serve where they serve one. Covers atomic
                isotopes and, where a reaction cell shifts an analyte onto a different
                mass, the product mass actually measured. Includes interference-monitor
                and internal-standard masses, which serve no analyte and so have no
                parent element. The analyte list is given by the Analyte field and
                is never inferred from the element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/monitoredMasses
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: monitoredMasses
                schema:name:
                  const: Monitored Masses
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Mass Resolution Assignment
              description: Mass resolution mode assigned to each acquired mass. The
                selected resolution determines which polyatomic interferences are
                physically resolved by the magnetic sector. One analyte may be acquired
                at more than one resolution, so the assignment is per acquired mass
                rather than per element. The overall mode(s) used in the procedure
                are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/massResolutionAssignment
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: massResolutionAssignment
                schema:name:
                  const: Mass Resolution Assignment
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Dwell Time per Mass
              description: Integration time spent on each mass peak per sweep (ms).
                May differ between masses where per-mass dwell times are programmed.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Isobaric Interference Corrections Applied
              description: Whether mathematical corrections for residual isobaric
                or polyatomic interferences are applied in data reduction (supplementary
                to any interference suppression achieved through mass resolution selection).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Interfering Species
              description: List of isobaric or polyatomic species mathematically corrected
                in data reduction. In SF-ICP-MS, mass resolution is the primary interference
                mitigation strategy; mathematical corrections address residual interferences
                not resolved at the operating resolution.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/interferingSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingSpecies
                schema:name:
                  const: Interfering Species
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Interference Correction Method
              description: Mathematical approach used to calculate and remove residual
                interference contributions from measured signals. In SF-ICP-MS, interference
                solutions isolating specific polyatomic species are measured alongside
                samples and used to calibrate correction factors.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/interferenceCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionMethod
                schema:name:
                  const: Interference Correction Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set). Specify units
                (\xB5g/g or \xB5g/L) and whether values are procedure-typical estimates
                or session-specific measured values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/detectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimit
                schema:name:
                  const: Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Detection Limit Method
              description: Method used to calculate detection limits for each reported
                concentration variable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Limit of Quantification (LOQ) Method
              description: Method used to determine the limit of quantification.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/limitOfQuantificationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: limitOfQuantificationMethod
                schema:name:
                  const: Limit of Quantification (LOQ) Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Within-Session Analytical Precision and Assessment Method
              description: Precision of repeated measurements within a single analytical
                session and the method used to assess it. Report both the assessment
                method and the precision values. The assessment method must specify
                the reference material or standard measured, the number of replicates
                n, and the statistic reported (1s RSD, 2s RSD, 2SD, 2SE, 95% CI).
                Distinct from the internal precision of a single measurement, which
                derives from counting statistics over the cycles of that measurement
                rather than from repeated analyses.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: withinSessionAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Within-Session Analytical Precision and Assessment Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Between-Session (Long-Term) Analytical Precision and Assessment
                Method
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported. Long-term precision is normally poorer than within-session
                precision and is the figure a data user should carry when comparing
                results from different sessions."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: betweenSessionAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Between-Session (Long-Term) Analytical Precision and Assessment
                    Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Analytical Accuracy and Assessment Method
              description: Accuracy of final concentration measurements relative to
                certified or consensus values and the method used to assess it.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracyAndAssessmentMethod
                schema:name:
                  const: Analytical Accuracy and Assessment Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
    ada:numberOfScansPerReplicate:
      description: "Number of complete mass scans accumulated per analytical replicate.
        A scan \u2014 also called a sweep or a pass \u2014 is one complete traversal
        of the monitored masses by a sequentially scanning analyser, so the scan count
        multiplied by the per-mass dwell time gives the total integration time per
        replicate. Distinct from a cycle in simultaneous multi-collection, which is
        one readout of all detectors at once rather than a traversal of masses."
      anyOf:
      - type: integer
      - type: string
      readOnly: true
    ada:numberOfReplicatesPerSample:
      description: Number of replicate measurements performed on the same sample,
        or on the same nominal location where the technique is spatially resolved.
        For spot analysis this is the number of individual spots per grain or location;
        for transects, the number of replicate lines; for mapping, the number of map
        acquisitions of the same area; for solution work, the number of discrete replicate
        measurements acquired per sample solution. The procedure registers an intended
        count where it has one; the analysis records the count actually acquired.
      anyOf:
      - type: integer
      - type: string
    ada:sampleSequenceDesign:
      description: 'Description of the measurement order within a session: how samples,
        blanks, calibration standards, and reference materials are interleaved.'
      type: string
      readOnly: true
    ada:internalStandardElement:
      description: Element(s) added at a known concentration to all solutions (samples,
        blanks, calibration standards) and used as internal standards for drift correction
        and matrix normalization. Specify element and monitored isotope.
      type: string
      readOnly: true
    ada:oxideProductionMethodAndThreshold:
      description: Method used to quantify plasma oxide production and the acceptance
        threshold applied before commencing analysis. Record both the monitored mass
        ratio(s) and the maximum allowed threshold(s). Measured values are recorded
        in Oxide Production. CeO+/Ce+ (m/z 156/140) is the standard monitor proxy;
        stricter thresholds than Q-ICP-MS are commonly required. BaO+/Ba+ may also
        be monitored.
      type: string
      readOnly: true
    ada:primaryStandardNameDefault:
      description: Name and reference material identifier of the external calibration
        standard used to convert signal intensities to elemental concentrations. Include
        the material name, its source or supplier, and a citation for the accepted
        values used, since results calibrated against different published values for
        the same material are not directly comparable.
      type: string
    ada:internalStandardApproach:
      description: 'Role(s) assigned to the internal standard(s) in data reduction:
        drift correction only, matrix normalization, or a combination.'
      type: string
      enum:
      - Drift correction only
      - Matrix normalization
      - Drift + matrix normalization
      - N/A
      - None
      - missing
      readOnly: true
    ada:driftCorrectionMethod:
      description: Method used to correct for instrumental signal drift across a session.
      type: string
      enum:
      - IS normalization
      - Standard bracketing
      - IS normalization + bracketing
      - None
      - N/A
      - missing
      readOnly: true
    ada:perAnalyteCalibrationStrategy:
      type: array
      items:
        description: Approach used to convert measured ion signals to elemental concentrations.
          Documents cases where different analytes or analyte groups are calibrated
          using different strategies within the same procedure. If a single strategy
          is applied uniformly to all analytes, record that strategy.
        type: string
        enum:
        - External calibration (all analytes)
        - Isotope dilution (all analytes)
        - Matrix-matched bracketing with BHVO-2
        - ID for REE; external calibration for transition metals
        - N/A
        - None
        - missing
        readOnly: true
    ada:signalIntegrationIntervalMethod:
      description: Method used to define the integration window for each replicate
        measurement (e.g., full acquisition time, stable-interval selection, automated
        criteria).
      type: string
      enum:
      - Full replicate
      - Stable interval selection
      - Automated peak detection
      - N/A
      - None
      - missing
      readOnly: true
    ada:blankBackgroundCorrectionMethod:
      description: Method used to subtract instrument background and/or procedural
        blank from sample signals.
      type: string
      enum:
      - On-peak zero
      - Solution blank
      - Procedural blank
      - N/A
      - None
      - missing
      readOnly: true
    ada:secondaryReferenceMaterialDefault:
      type: array
      items:
        description: Reference material(s) measured as unknowns to independently assess
          analytical accuracy. Specify material name and expected-value source.
        type: string
    ada:calibrationMeasurementFrequency:
      description: How often the primary calibration standard is measured relative
        to unknown samples within a session.
      type: string
      readOnly: true
  required:
  - ada:numberOfScansPerReplicate
  - ada:numberOfReplicatesPerSample
  - ada:sampleSequenceDesign
  - ada:internalStandardElement
  - ada:oxideProductionMethodAndThreshold
  - ada:primaryStandardNameDefault
  - ada:internalStandardApproach
  - ada:driftCorrectionMethod
  - ada:signalIntegrationIntervalMethod
  - ada:blankBackgroundCorrectionMethod
  - ada:calibrationMeasurementFrequency

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/context.jsonld)

## Sources

* [Solution_SF-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp`

