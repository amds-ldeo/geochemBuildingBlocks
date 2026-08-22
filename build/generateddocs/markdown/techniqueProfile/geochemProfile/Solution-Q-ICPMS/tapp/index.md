
# Solution Q-ICP-MS Technique-Aligned Protocol Profile (solutionQicpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.tapp` *v0.1*

Solution quadrupole ICP-MS extension of the base TAPP definition, generated from docs/Solution_Q-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### solutionQicpmsTAPP example Gao2008
solutionQicpmsTAPP instance derived from Hu+Gao2008 | PerkinElmer ELAN 6100 DRC | NWU Xi'an.
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
  "@id": "ex:solutionQicpmsTAPP-Gao2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — Gao2008",
  "schema:description": "Autolens used (not guard electrode; stated section 3.1); 3 sweeps/reading x 3 readings = 9 sweeps/replicate; 48 trace elements analyzed Reported detail: ada:driftCorrectionMethod = IS normalization + standard bracketing (Rh IS + repeated calibration solution; stated section 3.1); ada:perAnalyteCalibrationStrategy = External calibration (all analytes; stated section 3.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)"
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
            "Geological reference materials (basalt, andesite, granite, shale); upper continental crust samples (stated abstract)"
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
          "schema:defaultValue": 50,
          "schema:description": "50 mg (stated section 3.3)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (50 mg; stated section 3.3)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
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
            "schema:defaultValue": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated"
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
            "schema:name": "Step 1: conc. HNO3 (1 ml) + conc. HF (1 ml); Steps 2-3: conc. HNO3 fuming to dryness (twice); Step 4: HNO3 (1.5 ml) + ultra-pure water (2.5 ml); stated section 3.3",
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
            "schema:value": "PTFE-lined stainless steel bomb (home-made; stated section 3.3)"
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
            "schema:description": "2 (step 1: bomb at 190 deg C / 48 h in HNO3+HF; step 4: bomb at 150 deg C overnight in HNO3+water; five steps explicitly numbered; stated section 3.3)"
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
            "schema:defaultValue": 190,
            "schema:description": "190 deg C (stated section 3.3)"
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
            "schema:defaultValue": "48 h (stated section 3.3)"
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
  "ada:finalSolutionMatrix": "Dilute HNO3 (~3%; 1.5 ml conc. HNO3 in ~50 ml; stated section 3.3)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of digested solution)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesMonitorDefault",
          "schema:name": "Doubly-Charged Species Monitor",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ (m/z 70/140; stated section 3.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesProductionDefault",
          "schema:name": "Doubly-Charged Species Production",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ < 2.5% threshold (stated section 3.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Glass microconcentric nebulizer (MCN; stated section 3.1)"
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
              "schema:value": "Cyclonic spray chamber (stated section 3.1)"
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
              "schema:defaultValue": 0.2,
              "schema:description": "0.20 ml/min (stated section 3.1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1350,
              "schema:description": "1350 W (stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1350 W; stated section 3.1)"
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
        "schema:name": "PerkinElmer -- \"a PerkinElmer SCIEX ELAN 6100 DRC ICP-MS\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "48 trace elements: Li",
      "Be",
      "B",
      "Sc",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Ge",
      "As",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Mo",
      "Cd",
      "In",
      "Sn",
      "Sb",
      "Te",
      "Cs",
      "Ba",
      "La-Lu",
      "Hf",
      "Ta",
      "W",
      "Tl",
      "Pb",
      "Bi",
      "Th",
      "U (stated section 3.1)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:massCyclesPerReplicate": "3 sweeps/reading x 3 readings/replicate (= 9 sweeps/replicate; stated section 3.1)",
  "ada:internalStandardElement": "Rh (stated section 3.1)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 2.5% and Ce2+/Ce+ < 2.5% (stated section 3.1)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element calibration solution (not formally named; stated section 3.1)",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, BHVO-1, G-2, SCO-1, GSR-5 (stated Table 2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Forty-eight trace element concentrations (ppm); blanks (ppb)"
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
  "ada:samplingUnit": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-Gao2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Gao2008",
  "schema:description": "Autolens used (not guard electrode; stated section 3.1); 3 sweeps/reading x 3 readings = 9 sweeps/replicate; 48 trace elements analyzed Reported detail: ada:driftCorrectionMethod = IS normalization + standard bracketing (Rh IS + repeated calibration solution; stated section 3.1); ada:perAnalyteCalibrationStrategy = External calibration (all analytes; stated section 3.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)"
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
            "Geological reference materials (basalt, andesite, granite, shale); upper continental crust samples (stated abstract)"
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
          "schema:defaultValue": 50,
          "schema:description": "50 mg (stated section 3.3)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (50 mg; stated section 3.3)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
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
            "schema:defaultValue": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated"
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
            "schema:name": "Step 1: conc. HNO3 (1 ml) + conc. HF (1 ml); Steps 2-3: conc. HNO3 fuming to dryness (twice); Step 4: HNO3 (1.5 ml) + ultra-pure water (2.5 ml); stated section 3.3",
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
            "schema:value": "PTFE-lined stainless steel bomb (home-made; stated section 3.3)"
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
            "schema:description": "2 (step 1: bomb at 190 deg C / 48 h in HNO3+HF; step 4: bomb at 150 deg C overnight in HNO3+water; five steps explicitly numbered; stated section 3.3)"
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
            "schema:defaultValue": 190,
            "schema:description": "190 deg C (stated section 3.3)"
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
            "schema:defaultValue": "48 h (stated section 3.3)"
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
  "ada:finalSolutionMatrix": "Dilute HNO3 (~3%; 1.5 ml conc. HNO3 in ~50 ml; stated section 3.3)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of digested solution)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesMonitorDefault",
          "schema:name": "Doubly-Charged Species Monitor",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ (m/z 70/140; stated section 3.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesProductionDefault",
          "schema:name": "Doubly-Charged Species Production",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ < 2.5% threshold (stated section 3.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Glass microconcentric nebulizer (MCN; stated section 3.1)"
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
              "schema:value": "Cyclonic spray chamber (stated section 3.1)"
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
              "schema:defaultValue": 0.2,
              "schema:description": "0.20 ml/min (stated section 3.1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1350,
              "schema:description": "1350 W (stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1350 W; stated section 3.1)"
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
        "schema:name": "PerkinElmer -- \"a PerkinElmer SCIEX ELAN 6100 DRC ICP-MS\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "48 trace elements: Li",
      "Be",
      "B",
      "Sc",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Ge",
      "As",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Mo",
      "Cd",
      "In",
      "Sn",
      "Sb",
      "Te",
      "Cs",
      "Ba",
      "La-Lu",
      "Hf",
      "Ta",
      "W",
      "Tl",
      "Pb",
      "Bi",
      "Th",
      "U (stated section 3.1)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:massCyclesPerReplicate": "3 sweeps/reading x 3 readings/replicate (= 9 sweeps/replicate; stated section 3.1)",
  "ada:internalStandardElement": "Rh (stated section 3.1)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 2.5% and Ce2+/Ce+ < 2.5% (stated section 3.1)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element calibration solution (not formally named; stated section 3.1)",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, BHVO-1, G-2, SCO-1, GSR-5 (stated Table 2)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Forty-eight trace element concentrations (ppm); blanks (ppb)"
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
  "ada:samplingUnit": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-Gao2008 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder (50 mg; stated section 3.3)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
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
                            schema1:name "Step 1: conc. HNO3 (1 ml) + conc. HF (1 ml); Steps 2-3: conc. HNO3 fuming to dryness (twice); Step 4: HNO3 (1.5 ml) + ultra-pure water (2.5 ml); stated section 3.3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Autolens used (not guard electrode; stated section 3.1); 3 sweeps/reading x 3 readings = 9 sweeps/replicate; 48 trace elements analyzed Reported detail: ada:driftCorrectionMethod = IS normalization + standard bracketing (Rh IS + repeated calibration solution; stated section 3.1); ada:perAnalyteCalibrationStrategy = External calibration (all analytes; stated section 3.1)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Gao2008" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Geological reference materials (basalt, andesite, granite, shale); upper continental crust samples (stated abstract)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "48 trace elements: Li",
                "As",
                "B",
                "Ba",
                "Be",
                "Bi",
                "Cd",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Ga",
                "Ge",
                "Hf",
                "In",
                "La-Lu",
                "Mo",
                "Nb",
                "Ni",
                "Pb",
                "Rb",
                "Sb",
                "Sc",
                "Sn",
                "Sr",
                "Ta",
                "Te",
                "Th",
                "Tl",
                "U (stated section 3.1)",
                "V",
                "W",
                "Y",
                "Zn",
                "Zr" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None (direct analysis of digested solution)" ;
    ada:driftCorrectionMethod "Standard bracketing" ;
    ada:finalSolutionMatrix "Dilute HNO3 (~3%; 1.5 ml conc. HNO3 in ~50 ml; stated section 3.3)" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Rh (stated section 3.1)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate "3 sweeps/reading x 3 readings/replicate (= 9 sweeps/replicate; stated section 3.1)" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 2.5% and Ce2+/Ce+ < 2.5% (stated section 3.1)" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "Multi-element calibration solution (not formally named; stated section 3.1)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Forty-eight trace element concentrations (ppm); blanks (ppb)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml" ;
    ada:secondaryReferenceMaterialDefault "AGV-1, BHVO-1, G-2, SCO-1, GSR-5 (stated Table 2)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
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

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "48 h (stated section 3.3)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 190 ;
    schema1:description "190 deg C (stated section 3.3)" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "PTFE-lined stainless steel bomb (home-made; stated section 3.3)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Glass microconcentric nebulizer (MCN; stated section 3.1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:description "2 (step 1: bomb at 190 deg C / 48 h in HNO3+HF; step 4: bomb at 150 deg C overnight in HNO3+water; five steps explicitly numbered; stated section 3.3)" ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value 2 ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "50 mg (stated section 3.3)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2e-01 ;
    schema1:description "0.20 ml/min (stated section 3.1)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Cyclonic spray chamber (stated section 3.1)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (intermediate gas; stated section 3.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 14 ;
    schema1:description "14 L/min (outer ICP gas; stated section 3.1)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ce2+/Ce+ (m/z 70/140; stated section 3.1)" ;
    schema1:name "Doubly-Charged Species Monitor" ;
    schema1:valueName "doublyChargedSpeciesMonitorDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ce2+/Ce+ < 2.5% threshold (stated section 3.1)" ;
    schema1:name "Doubly-Charged Species Production" ;
    schema1:valueName "doublyChargedSpeciesProductionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1350 ;
    schema1:description "1350 W (stated section 3.1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "STD (standard mode, no gas)" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> ;
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
            schema1:name "PerkinElmer -- \"a PerkinElmer SCIEX ELAN 6100 DRC ICP-MS\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:value "Unit resolution (quadrupole, fixed; m/Delta-m ~300)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1350 W; stated section 3.1)" .


```


### solutionQicpmsTAPP example P1
solutionQicpmsTAPP instance derived from Yu+etal2005 | PerkinElmer ELAN DRC II | Univ Cambridge.
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
  "@id": "ex:solutionQicpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — P1",
  "schema:description": "Peak hopping scan mode explicitly stated in Table 1 [NOTE: no dedicated Signal Collection Mode field in TAPP v2; Phase 4 flag]; pulse counting detection; autolens on (Table 1); 0.03 mm ID pump tubing for ~60 uL/min uptake Reported detail: ada:signalCollectionMode = Peak hopping (stated Table 1); ada:driftCorrectionMethod = Standard bracketing (matrix-matched standards at fixed intervals; stated section 2); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 100 ppm Ca (stated section 2); ada:blankBackgroundCorrectionMethod = On-peak zero (stated implicitly; calibration standards include procedural blank equivalent).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Cambridge (affiliation)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-AES (for initial [Ca] determination; stated section 2)",
        "schema:description": "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Foraminifera calcite (benthic and planktonic species; stated abstract)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Foraminifera shells cleaned mechanically and chemically then dissolved; no grinding (stated section 2)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
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
            "schema:defaultValue": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated"
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
            "schema:defaultValue": "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%"
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
            "schema:description": "1 (simple dissolution; stated section 2)"
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
  "ada:finalSolutionMatrix": "0.075 M HNO3 at 100 ppm Ca (stated section 2)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of dissolved foraminifera)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "PerkinElmer Elan DRC II (stated section 2 and Table 1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (stated Table 1)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Glass Expansion Micromist FM005 (stated section 2 and Table 1)"
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
              "schema:value": "Cyclonic quartz spray chamber (stated Table 1)"
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
              "schema:description": "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)"
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
              "schema:defaultValue": 0.99,
              "schema:description": "0.99-1.02 L/min (Table 1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 1)"
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
        "schema:name": "PerkinElmer -- \"a Perkin-Elmer Elan DRC II instrument\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "9 Me/Ca ratios: Li",
      "B",
      "Mg",
      "Al",
      "Mn",
      "Zn",
      "Sr",
      "Cd",
      "U relative to Ca (stated Table 1)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "7Li",
      "11B",
      "25Mg",
      "46Ca",
      "27Al",
      "55Mn",
      "66Zn",
      "87Sr",
      "111Cd",
      "238U (Table 1)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:massCyclesPerReplicate": "250 sweeps per replicate (Table 1)",
  "ada:numberOfReplicatesPerSample": "6 replicates (Table 1)",
  "ada:washTimeBetweenSamples": "60 s (Table 1)",
  "ada:signalCollectionMode": "Peak hopping",
  "ada:internalStandardElement": "None (matrix-matched external calibration; stated section 2)",
  "ada:oxideProductionMethodAndThreshold": "CeO/Ce < 3% (stated section 2)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Procedural blank",
  "ada:primaryStandardNameDefault": "Series of matrix-matched standards at 100 ppm Ca (not formally named; stated section 2)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Element/Ca ratios: Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (umol/mol); U/Ca (nmol/mol)"
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
  "ada:samplingUnit": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 P1",
  "schema:description": "Peak hopping scan mode explicitly stated in Table 1 [NOTE: no dedicated Signal Collection Mode field in TAPP v2; Phase 4 flag]; pulse counting detection; autolens on (Table 1); 0.03 mm ID pump tubing for ~60 uL/min uptake Reported detail: ada:signalCollectionMode = Peak hopping (stated Table 1); ada:driftCorrectionMethod = Standard bracketing (matrix-matched standards at fixed intervals; stated section 2); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 100 ppm Ca (stated section 2); ada:blankBackgroundCorrectionMethod = On-peak zero (stated implicitly; calibration standards include procedural blank equivalent).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Cambridge (affiliation)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-AES (for initial [Ca] determination; stated section 2)",
        "schema:description": "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Foraminifera calcite (benthic and planktonic species; stated abstract)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Foraminifera shells cleaned mechanically and chemically then dissolved; no grinding (stated section 2)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
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
            "schema:defaultValue": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated"
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
            "schema:defaultValue": "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%"
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
            "schema:description": "1 (simple dissolution; stated section 2)"
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
  "ada:finalSolutionMatrix": "0.075 M HNO3 at 100 ppm Ca (stated section 2)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of dissolved foraminifera)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "PerkinElmer Elan DRC II (stated section 2 and Table 1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (stated Table 1)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Glass Expansion Micromist FM005 (stated section 2 and Table 1)"
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
              "schema:value": "Cyclonic quartz spray chamber (stated Table 1)"
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
              "schema:description": "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)"
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
              "schema:defaultValue": 0.99,
              "schema:description": "0.99-1.02 L/min (Table 1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1300,
              "schema:description": "1300 W (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.2,
              "schema:description": "1.2 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1300 W; Table 1)"
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
        "schema:name": "PerkinElmer -- \"a Perkin-Elmer Elan DRC II instrument\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "9 Me/Ca ratios: Li",
      "B",
      "Mg",
      "Al",
      "Mn",
      "Zn",
      "Sr",
      "Cd",
      "U relative to Ca (stated Table 1)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "7Li",
      "11B",
      "25Mg",
      "46Ca",
      "27Al",
      "55Mn",
      "66Zn",
      "87Sr",
      "111Cd",
      "238U (Table 1)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:massCyclesPerReplicate": "250 sweeps per replicate (Table 1)",
  "ada:numberOfReplicatesPerSample": "6 replicates (Table 1)",
  "ada:washTimeBetweenSamples": "60 s (Table 1)",
  "ada:signalCollectionMode": "Peak hopping",
  "ada:internalStandardElement": "None (matrix-matched external calibration; stated section 2)",
  "ada:oxideProductionMethodAndThreshold": "CeO/Ce < 3% (stated section 2)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Procedural blank",
  "ada:primaryStandardNameDefault": "Series of matrix-matched standards at 100 ppm Ca (not formally named; stated section 2)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Element/Ca ratios: Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (umol/mol); U/Ca (nmol/mol)"
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
  "ada:samplingUnit": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
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

ex:solutionQicpmsTAPP-P1 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Foraminifera shells cleaned mechanically and chemically then dissolved; no grinding (stated section 2)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Peak hopping scan mode explicitly stated in Table 1 [NOTE: no dedicated Signal Collection Mode field in TAPP v2; Phase 4 flag]; pulse counting detection; autolens on (Table 1); 0.03 mm ID pump tubing for ~60 uL/min uptake Reported detail: ada:signalCollectionMode = Peak hopping (stated Table 1); ada:driftCorrectionMethod = Standard bracketing (matrix-matched standards at fixed intervals; stated section 2); ada:perAnalyteCalibrationStrategy = External calibration with matrix-matched standards at 100 ppm Ca (stated section 2); ada:blankBackgroundCorrectionMethod = On-peak zero (stated implicitly; calibration standards include procedural blank equivalent)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Cambridge (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — P1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Foraminifera calcite (benthic and planktonic species; stated abstract)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)" ;
                    schema1:name "ICP-AES (for initial [Ca] determination; stated section 2)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "9 Me/Ca ratios: Li",
                "Al",
                "B",
                "Cd",
                "Mg",
                "Mn",
                "Sr",
                "U relative to Ca (stated Table 1)",
                "Zn" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler" ;
    ada:blankBackgroundCorrectionMethod "Procedural blank" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "111Cd",
                "11B",
                "238U (Table 1)",
                "25Mg",
                "27Al",
                "46Ca",
                "55Mn",
                "66Zn",
                "7Li",
                "87Sr" ] ;
    ada:chromatographicSeparationApplied "None (direct analysis of dissolved foraminifera)" ;
    ada:driftCorrectionMethod "Standard bracketing" ;
    ada:finalSolutionMatrix "0.075 M HNO3 at 100 ppm Ca (stated section 2)" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "None (matrix-matched external calibration; stated section 2)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate "250 sweeps per replicate (Table 1)" ;
    ada:numberOfReplicatesPerSample "6 replicates (Table 1)" ;
    ada:oxideProductionMethodAndThreshold "CeO/Ce < 3% (stated section 2)" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "Series of matrix-matched standards at 100 ppm Ca (not formally named; stated section 2)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Element/Ca ratios: Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (umol/mol); U/Ca (nmol/mol)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)" ;
    ada:signalCollectionMode "Peak hopping" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "60 s (Table 1)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%" ;
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
    schema1:defaultValue 9.9e-01 ;
    schema1:description "0.99-1.02 L/min (Table 1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Glass Expansion Micromist FM005 (stated section 2 and Table 1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:description "1 (simple dissolution; stated section 2)" ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value 1 ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 60 ;
    schema1:description "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Cyclonic quartz spray chamber (stated Table 1)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (Table 1)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "60 s wash between samples (stated Table 1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1300 ;
    schema1:description "1300 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "PerkinElmer Elan DRC II (stated section 2 and Table 1)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "STD (standard mode, no gas)" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> ;
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
            schema1:name "PerkinElmer -- \"a Perkin-Elmer Elan DRC II instrument\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:value "Unit resolution (quadrupole, fixed; m/Delta-m ~300)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1300 W; Table 1)" .


```


### solutionQicpmsTAPP example Agilent7500
solutionQicpmsTAPP instance derived from Makishima+etal2011 | Agilent 7500cs | PML Okayama.
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
  "@id": "ex:solutionQicpmsTAPP-Agilent7500",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — Agilent7500",
  "schema:description": "Dwell times in Table 1 expressed as ms per 1 s cycle time; octopole CRC present but no gas used (PML practice); 149Sm used as both ID spike and internal standard Reported detail: ada:driftCorrectionMethod = IS normalization (149Sm spike ratio; stated section 2); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (ID-IS; all analytes; stated section 2).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)"
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
            "Silicate reference materials (basalt, andesite, peridotite), NIST SRM glasses, carbonaceous chondrites (stated section 2)"
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
          "schema:defaultValue": 15,
          "schema:description": "15-63 mg (silicates); 8-22 mg (NIST glass); 9-28 mg (chondrites; stated section 2)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder or glass chips (stated section 2)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations with ID-IS internal standard normalization (stated section 2)"
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
            "schema:defaultValue": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision"
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
            "schema:defaultValue": "\"113In/115In = 0.0448 (Rosman and Taylor 1998)\" used in the In correction; \"For a 94Mo/95Mo value of 0.58\" and MoOH+/MoO+ \"a value of ~0.15 was obtained\", both used in the Mo-oxide correction"
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
            "schema:name": "HF + HClO4 (basalt/glass, ultrasonic); HF alone in TFE bomb (peridotite/chondrite; stated section 2)",
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
            "schema:value": "Ultrasonic bath (basalt/glass); TFE bomb at 245 deg C (peridotite/chondrite; stated section 2)"
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
            "schema:defaultValue": 245,
            "schema:description": "Ambient for ultrasonic; 245 deg C for TFE bomb (stated section 2)"
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
  "ada:finalSolutionMatrix": "0.5 mol/l HNO3 (stated section 2)",
  "ada:chromatographicSeparationApplied": "None (direct analysis)",
  "ada:isotopeDilutionSpike": "149Sm-enriched spike (used as ID internal standard for Cd, In, Tl, Bi; stated section 2)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500cs (stated section 2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)"
        }
      ],
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Agilent -- \"Agilent 7500cs; Yokogawa Analytical Systems, Mitaka, Japan\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Cd",
      "In",
      "Tl",
      "Bi (with 149Sm as ID-IS reference; stated section 2)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "95Mo",
      "111Cd",
      "113Cd",
      "115In",
      "118Sn",
      "149Sm",
      "205Tl",
      "209Bi (Table 1)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:washTimeBetweenSamples": ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)",
  "ada:internalStandardElement": "149Sm (as ID-IS reference; stated section 2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 0.01 (= <1%; stated section 2)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element calibrator solution (Cd, In, Tl, Bi, Sm; not formally named; stated section 2)",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610/612/614/616, carbonaceous chondrites (stated in text)"
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Cd, In, Tl and Bi mass fractions (ng g-1)"
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
  "ada:samplingUnit": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-Agilent7500",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Agilent7500",
  "schema:description": "Dwell times in Table 1 expressed as ms per 1 s cycle time; octopole CRC present but no gas used (PML practice); 149Sm used as both ID spike and internal standard Reported detail: ada:driftCorrectionMethod = IS normalization (149Sm spike ratio; stated section 2); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (ID-IS; all analytes; stated section 2).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)"
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
            "Silicate reference materials (basalt, andesite, peridotite), NIST SRM glasses, carbonaceous chondrites (stated section 2)"
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
          "schema:defaultValue": 15,
          "schema:description": "15-63 mg (silicates); 8-22 mg (NIST glass); 9-28 mg (chondrites; stated section 2)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder or glass chips (stated section 2)",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations with ID-IS internal standard normalization (stated section 2)"
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
            "schema:defaultValue": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision"
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
            "schema:defaultValue": "\"113In/115In = 0.0448 (Rosman and Taylor 1998)\" used in the In correction; \"For a 94Mo/95Mo value of 0.58\" and MoOH+/MoO+ \"a value of ~0.15 was obtained\", both used in the Mo-oxide correction"
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
            "schema:name": "HF + HClO4 (basalt/glass, ultrasonic); HF alone in TFE bomb (peridotite/chondrite; stated section 2)",
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
            "schema:value": "Ultrasonic bath (basalt/glass); TFE bomb at 245 deg C (peridotite/chondrite; stated section 2)"
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
            "schema:defaultValue": 245,
            "schema:description": "Ambient for ultrasonic; 245 deg C for TFE bomb (stated section 2)"
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
  "ada:finalSolutionMatrix": "0.5 mol/l HNO3 (stated section 2)",
  "ada:chromatographicSeparationApplied": "None (direct analysis)",
  "ada:isotopeDilutionSpike": "149Sm-enriched spike (used as ID internal standard for Cd, In, Tl, Bi; stated section 2)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500cs (stated section 2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)"
        }
      ],
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Agilent -- \"Agilent 7500cs; Yokogawa Analytical Systems, Mitaka, Japan\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Cd",
      "In",
      "Tl",
      "Bi (with 149Sm as ID-IS reference; stated section 2)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "95Mo",
      "111Cd",
      "113Cd",
      "115In",
      "118Sn",
      "149Sm",
      "205Tl",
      "209Bi (Table 1)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:washTimeBetweenSamples": ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)",
  "ada:internalStandardElement": "149Sm (as ID-IS reference; stated section 2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 0.01 (= <1%; stated section 2)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element calibrator solution (Cd, In, Tl, Bi, Sm; not formally named; stated section 2)",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610/612/614/616, carbonaceous chondrites (stated in text)"
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Cd, In, Tl and Bi mass fractions (ng g-1)"
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
  "ada:samplingUnit": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-Agilent7500 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder or glass chips (stated section 2)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "HF + HClO4 (basalt/glass, ultrasonic); HF alone in TFE bomb (peridotite/chondrite; stated section 2)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Dwell times in Table 1 expressed as ms per 1 s cycle time; octopole CRC present but no gas used (PML practice); 149Sm used as both ID spike and internal standard Reported detail: ada:driftCorrectionMethod = IS normalization (149Sm spike ratio; stated section 2); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (ID-IS; all analytes; stated section 2)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7500" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate reference materials (basalt, andesite, peridotite), NIST SRM glasses, carbonaceous chondrites (stated section 2)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Bi (with 149Sm as ID-IS reference; stated section 2)",
                "Cd",
                "In",
                "Tl" ] ;
    ada:analyticalMode "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "111Cd",
                "113Cd",
                "115In",
                "118Sn",
                "149Sm",
                "205Tl",
                "209Bi (Table 1)",
                "95Mo" ] ;
    ada:chromatographicSeparationApplied "None (direct analysis)" ;
    ada:driftCorrectionMethod "IS normalization" ;
    ada:finalSolutionMatrix "0.5 mol/l HNO3 (stated section 2)" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "149Sm (as ID-IS reference; stated section 2)" ;
    ada:isotopeDilutionSpike "149Sm-enriched spike (used as ID internal standard for Cd, In, Tl, Bi; stated section 2)" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 0.01 (= <1%; stated section 2)" ;
    ada:perAnalyteCalibrationStrategy "Isotope dilution (all analytes)" ;
    ada:primaryStandardNameDefault "Multi-element calibrator solution (Cd, In, Tl, Bi, Sm; not formally named; stated section 2)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Cd, In, Tl and Bi mass fractions (ng g-1)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"" ;
    ada:secondaryReferenceMaterialDefault "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610/612/614/616, carbonaceous chondrites (stated in text)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"113In/115In = 0.0448 (Rosman and Taylor 1998)\" used in the In correction; \"For a 94Mo/95Mo value of 0.58\" and MoOH+/MoO+ \"a value of ~0.15 was obtained\", both used in the Mo-oxide correction" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 245 ;
    schema1:description "Ambient for ultrasonic; 245 deg C for TFE bomb (stated section 2)" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Ultrasonic bath (basalt/glass); TFE bomb at 245 deg C (peridotite/chondrite; stated section 2)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15-63 mg (silicates); 8-22 mg (NIST glass); 9-28 mg (chondrites; stated section 2)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue ">=200 s in 0.5 mol/l HNO3; 200 s HF wash after Mo standard (stated section 2)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500cs (stated section 2)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

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
            schema1:name "Agilent -- \"Agilent 7500cs; Yokogawa Analytical Systems, Mitaka, Japan\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "IUPAC isotope dilution equations with ID-IS internal standard normalization (stated section 2)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:value "Unit resolution (quadrupole, fixed; m/Delta-m ~300)" .


```


### solutionQicpmsTAPP example Agilent7900
solutionQicpmsTAPP instance derived from Long+etal2025 | Agilent 7900 | IPGP France.
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
  "@id": "ex:solutionQicpmsTAPP-Agilent7900",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — Agilent7900",
  "schema:description": "He KED applied only for masses 23-75; above mass 75 no KED (stated Methods); coupled to MC-ICP-MS Neptune Plus for Zn isotopes on same dissolved aliquots Reported detail: ada:driftCorrectionMethod = IS normalization (Sc, In, Re; stated Methods); ada:perAnalyteCalibrationStrategy = External calibration (stated Methods).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut de Physique du Globe de Paris (IPGP), France (affiliation)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "MC-ICP-MS (Neptune Plus at IPGP; for Zn isotope measurements; stated Methods)",
        "schema:description": "Same dissolved aliquots analyzed by Q-ICP-MS (major/trace elements, masses 23-75) and MC-ICP-MS (Zn isotopes); stated Methods"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Carbonaceous chondrites (CI, CM, CV, CO, CR, CK, CH, CY, CB types; stated abstract)"
          ]
        }
      ]
    }
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis; stated Methods)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (stated Methods)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "KED (kinetic energy discrimination, He gas)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He (stated Methods)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasFlowRateDefault",
              "schema:name": "Collision Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "5 mL/min (stated Methods)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "MicroMist nebulizer (stated Methods)"
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
              "schema:value": "Scott spray chamber (stated Methods)"
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
              "schema:defaultValue": 0.2,
              "schema:description": "0.2 mL/min (stated Methods)"
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
        "schema:name": "Agilent -- \"an Agilent 7900 Quadrupole Inductively Coupled Plasma Mass Spectrometry instrument\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Major and trace elements (masses 23-75, Na to As; stated Methods)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:internalStandardElement": "Sc, In, Re (stated Methods)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
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
  "ada:primaryStandardNameDefault": "Mixture of certified standards (not formally named; stated Methods)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Partially -- \"The elemental content of samples was analyzed\"; concentration unit ug/g attested (\"[Zn] = 309 ug/g\", \"144 ug/g\"); the reported variable list is in Tables S1-S2, not in the paper"
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
  "ada:samplingUnit": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-Agilent7900",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Agilent7900",
  "schema:description": "He KED applied only for masses 23-75; above mass 75 no KED (stated Methods); coupled to MC-ICP-MS Neptune Plus for Zn isotopes on same dissolved aliquots Reported detail: ada:driftCorrectionMethod = IS normalization (Sc, In, Re; stated Methods); ada:perAnalyteCalibrationStrategy = External calibration (stated Methods).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut de Physique du Globe de Paris (IPGP), France (affiliation)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "MC-ICP-MS (Neptune Plus at IPGP; for Zn isotope measurements; stated Methods)",
        "schema:description": "Same dissolved aliquots analyzed by Q-ICP-MS (major/trace elements, masses 23-75) and MC-ICP-MS (Zn isotopes); stated Methods"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Carbonaceous chondrites (CI, CM, CV, CO, CR, CK, CH, CY, CB types; stated abstract)"
          ]
        }
      ]
    }
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis; stated Methods)",
  "ada:isotopeDilutionSpike": "None",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (stated Methods)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "KED (kinetic energy discrimination, He gas)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He (stated Methods)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasFlowRateDefault",
              "schema:name": "Collision Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "5 mL/min (stated Methods)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "MicroMist nebulizer (stated Methods)"
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
              "schema:value": "Scott spray chamber (stated Methods)"
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
              "schema:defaultValue": 0.2,
              "schema:description": "0.2 mL/min (stated Methods)"
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
        "schema:name": "Agilent -- \"an Agilent 7900 Quadrupole Inductively Coupled Plasma Mass Spectrometry instrument\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Major and trace elements (masses 23-75, Na to As; stated Methods)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:internalStandardElement": "Sc, In, Re (stated Methods)",
  "ada:internalStandardApproach": "N/A",
  "ada:driftCorrectionMethod": "IS normalization",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "None"
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
  "ada:primaryStandardNameDefault": "Mixture of certified standards (not formally named; stated Methods)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Partially -- \"The elemental content of samples was analyzed\"; concentration unit ug/g attested (\"[Zn] = 309 ug/g\", \"144 ug/g\"); the reported variable list is in Tables S1-S2, not in the paper"
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
  "ada:samplingUnit": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-Agilent7900 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "He KED applied only for masses 23-75; above mass 75 no KED (stated Methods); coupled to MC-ICP-MS Neptune Plus for Zn isotopes on same dissolved aliquots Reported detail: ada:driftCorrectionMethod = IS normalization (Sc, In, Re; stated Methods); ada:perAnalyteCalibrationStrategy = External calibration (stated Methods)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institut de Physique du Globe de Paris (IPGP), France (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7900" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Carbonaceous chondrites (CI, CM, CV, CO, CR, CK, CH, CY, CB types; stated abstract)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Same dissolved aliquots analyzed by Q-ICP-MS (major/trace elements, masses 23-75) and MC-ICP-MS (Zn isotopes); stated Methods" ;
                    schema1:name "MC-ICP-MS (Neptune Plus at IPGP; for Zn isotope measurements; stated Methods)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Major and trace elements (masses 23-75, Na to As; stated Methods)" ] ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None (direct analysis; stated Methods)" ;
    ada:driftCorrectionMethod "IS normalization" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalStandardApproach "N/A" ;
    ada:internalStandardElement "Sc, In, Re (stated Methods)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "Mixture of certified standards (not formally named; stated Methods)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Partially -- \"The elemental content of samples was analyzed\"; concentration unit ug/g attested (\"[Zn] = 309 ug/g\", \"144 ug/g\"); the reported variable list is in Tables S1-S2, not in the paper" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "MicroMist nebulizer (stated Methods)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2e-01 ;
    schema1:description "0.2 mL/min (stated Methods)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Scott spray chamber (stated Methods)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "5 mL/min (stated Methods)" ;
    schema1:name "Collision Gas Flow Rate" ;
    schema1:valueName "collisionGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (stated Methods)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "KED (kinetic energy discrimination, He gas)" .

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
            schema1:name "Agilent -- \"an Agilent 7900 Quadrupole Inductively Coupled Plasma Mass Spectrometry instrument\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> a schema1:PropertyValue ;
    schema1:name "Collision Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:value "He (stated Methods)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "None" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:value "Unit resolution (quadrupole, fixed; m/Delta-m ~300)" .


```


### solutionQicpmsTAPP example Agilent7500-2
solutionQicpmsTAPP instance derived from Lu+etal2007 | Agilent 7500cs | PML Okayama.
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
  "@id": "ex:solutionQicpmsTAPP-Agilent7500-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — Agilent7500-2",
  "schema:description": "Pseudo-flow injection (pFI) acquisition: 30 s / 48 scans / 1 pt per mass; 0.5 mol/l HF as carrier and wash; shield torch on; Pt cones; self-aspiration PFA-20 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.1); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (all analytes; stated section 2.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SF-ICP-MS (Finnigan ELEMENT at PML; for Ti measurements; stated section 2.1.2)",
        "schema:description": "Q-ICP-MS (7500cs) measured B, Zr, Nb, Mo, Sn, Sb, Hf, Ta; SF-ICP-MS (ELEMENT) measured Ti and Nb; both techniques on same digested solutions; stated section 2.1"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Geological reference materials (basalt, andesite, peridotite) and carbonaceous chondrites (stated section 2.5)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb with HF; stated section 2.1.1)",
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
        "schema:name": "Data acquisition",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionQicpmsTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (shield torch system used; stated section 2.1.1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations (ID-IS method; stated section 2.1)"
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
            "schema:defaultValue": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated"
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
            "schema:name": "0.5 mol/l HF (stated section 2.1.1)",
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
  "ada:finalSolutionMatrix": "0.5 mol/l HF (stated section 2.1.1)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.1)",
  "ada:isotopeDilutionSpike": "Multi-element enriched isotope spikes (Mo, Sn, Sb, Zr, Hf, Ta, B spikes; stated section 2.1)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500cs (stated section 2.1.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz glass torch with Pt injector (stated Table in section 2.1.1)",
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
              "@id": "ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Pt sampler and Pt skimmer (stated Table in section 2.1.1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.1)"
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
              "schema:value": "Scott double-pass, cooled at 2 deg C, Teflon (stated Table in section 2.1.1)"
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
              "schema:defaultValue": 2.1,
              "schema:description": "Self-aspiration; volumetric flow rate N (stated Table in section 2.1.1)"
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
              "schema:defaultValue": 0.92,
              "schema:description": "0.92 L/min (stated Table in section 2.1.1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.6,
              "schema:description": "1.6 kW (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1.6 kW; stated section 2.1.1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode: pulse counting + analog (crossover ~10^6 cps; stated section 2.1.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.25,
          "schema:description": "0.25 L/min supplementary Ar for PFA micronebulizer (stated Table in section 2.1.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~3 min washout; ~3 min uptake stabilization (stated section 2.1.1)"
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
        "schema:name": "Agilent -- \"A Q-pole type ICP mass spectrometer, Agilent 7500 cs (Yokogawa Analytical Systems, Japan)\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "B",
      "Zr",
      "Nb",
      "Mo",
      "Sn",
      "Sb",
      "Hf",
      "Ta (stated Table 2a)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "10B",
      "11B",
      "90Zr",
      "91Zr",
      "93Nb",
      "95Mo",
      "97Mo",
      "118Sn",
      "119Sn",
      "121Sb",
      "123Sb",
      "178Hf",
      "179Hf",
      "181Ta (Table 2a)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:massCyclesPerReplicate": "48 scans per 30 s acquisition (stated section 2.1.1)",
  "ada:sampleSequenceDesign": "Standard solution measured every two samples (stated section 2.1.1)",
  "ada:washTimeBetweenSamples": "~180 s (~3 min; stated: each measurement ~6 min including ~3 min wash; section 2.1.1)",
  "ada:internalStandardElement": "None (ID-IS method: spike isotope ratios used; stated section 2.1)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.1)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element standard solution (not formally named; stated section 2.1.1)",
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.1)",
  "ada:secondaryReferenceMaterialDefault": [
    "USGS and GSJ geological reference materials and carbonaceous chondrites (stated Table 5)"
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "B, Ti, Zr, Nb, Mo, Sn, Sb, Hf and Ta mass fractions (ug g-1); detection limits in solution (pg g-1) and in rock (ng g-1) [Table 2a]"
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
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-Agilent7500-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Agilent7500-2",
  "schema:description": "Pseudo-flow injection (pFI) acquisition: 30 s / 48 scans / 1 pt per mass; 0.5 mol/l HF as carrier and wash; shield torch on; Pt cones; self-aspiration PFA-20 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.1); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (all analytes; stated section 2.1).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SF-ICP-MS (Finnigan ELEMENT at PML; for Ti measurements; stated section 2.1.2)",
        "schema:description": "Q-ICP-MS (7500cs) measured B, Zr, Nb, Mo, Sn, Sb, Hf, Ta; SF-ICP-MS (ELEMENT) measured Ti and Nb; both techniques on same digested solutions; stated section 2.1"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
            "Geological reference materials (basalt, andesite, peridotite) and carbonaceous chondrites (stated section 2.5)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb with HF; stated section 2.1.1)",
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
        "schema:name": "Data acquisition",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionQicpmsTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (shield torch system used; stated section 2.1.1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "IUPAC isotope dilution equations (ID-IS method; stated section 2.1)"
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
            "schema:defaultValue": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated"
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
            "schema:name": "0.5 mol/l HF (stated section 2.1.1)",
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
  "ada:finalSolutionMatrix": "0.5 mol/l HF (stated section 2.1.1)",
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.1)",
  "ada:isotopeDilutionSpike": "Multi-element enriched isotope spikes (Mo, Sn, Sb, Zr, Hf, Ta, B spikes; stated section 2.1)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500cs (stated section 2.1.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz glass torch with Pt injector (stated Table in section 2.1.1)",
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
              "@id": "ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Pt sampler and Pt skimmer (stated Table in section 2.1.1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "STD (standard mode, no gas)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.1)"
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
              "schema:value": "Scott double-pass, cooled at 2 deg C, Teflon (stated Table in section 2.1.1)"
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
              "schema:defaultValue": 2.1,
              "schema:description": "Self-aspiration; volumetric flow rate N (stated Table in section 2.1.1)"
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
              "schema:defaultValue": 0.92,
              "schema:description": "0.92 L/min (stated Table in section 2.1.1)"
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
              "@id": "ada:parameter/solutionQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.6,
              "schema:description": "1.6 kW (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.9,
              "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1.6 kW; stated section 2.1.1)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/ICP-Source",
          "schema:name": "missing"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Unit resolution (quadrupole, fixed; m/Delta-m ~300)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode: pulse counting + analog (crossover ~10^6 cps; stated section 2.1.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.25,
          "schema:description": "0.25 L/min supplementary Ar for PFA micronebulizer (stated Table in section 2.1.1)"
        },
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~3 min washout; ~3 min uptake stabilization (stated section 2.1.1)"
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
        "schema:name": "Agilent -- \"A Q-pole type ICP mass spectrometer, Agilent 7500 cs (Yokogawa Analytical Systems, Japan)\"",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "B",
      "Zr",
      "Nb",
      "Mo",
      "Sn",
      "Sb",
      "Hf",
      "Ta (stated Table 2a)"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "10B",
      "11B",
      "90Zr",
      "91Zr",
      "93Nb",
      "95Mo",
      "97Mo",
      "118Sn",
      "119Sn",
      "121Sb",
      "123Sb",
      "178Hf",
      "179Hf",
      "181Ta (Table 2a)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:massCyclesPerReplicate": "48 scans per 30 s acquisition (stated section 2.1.1)",
  "ada:sampleSequenceDesign": "Standard solution measured every two samples (stated section 2.1.1)",
  "ada:washTimeBetweenSamples": "~180 s (~3 min; stated: each measurement ~6 min including ~3 min wash; section 2.1.1)",
  "ada:internalStandardElement": "None (ID-IS method: spike isotope ratios used; stated section 2.1)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.1)",
  "ada:driftCorrectionMethod": "Standard bracketing",
  "ada:perAnalyteCalibrationStrategy": [
    "Isotope dilution (all analytes)"
  ],
  "ada:primaryStandardNameDefault": "Multi-element standard solution (not formally named; stated section 2.1.1)",
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.1)",
  "ada:secondaryReferenceMaterialDefault": [
    "USGS and GSJ geological reference materials and carbonaceous chondrites (stated Table 5)"
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "B, Ti, Zr, Nb, Mo, Sn, Sb, Hf and Ta mass fractions (ug g-1); detection limits in solution (pg g-1) and in rock (ng g-1) [Table 2a]"
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
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-Agilent7500-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/guardElectrode> ;
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
                            schema1:name "0.5 mol/l HF (stated section 2.1.1)" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder (decomposed in TFM bomb with HF; stated section 2.1.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> ;
    schema1:datePublished "missing" ;
    schema1:description "Pseudo-flow injection (pFI) acquisition: 30 s / 48 scans / 1 pt per mass; 0.5 mol/l HF as carrier and wash; shield torch on; Pt cones; self-aspiration PFA-20 Reported detail: ada:driftCorrectionMethod = Standard bracketing (standard every two samples; stated section 2.1.1); ada:perAnalyteCalibrationStrategy = Isotope dilution with ID-IS normalization (all analytes; stated section 2.1)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7500-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Geological reference materials (basalt, andesite, peridotite) and carbonaceous chondrites (stated section 2.5)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Q-ICP-MS (7500cs) measured B, Zr, Nb, Mo, Sn, Sb, Hf, Ta; SF-ICP-MS (ELEMENT) measured Ti and Nb; both techniques on same digested solutions; stated section 2.1" ;
                    schema1:name "SF-ICP-MS (Finnigan ELEMENT at PML; for Ti measurements; stated section 2.1.2)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "B",
                "Hf",
                "Mo",
                "Nb",
                "Sb",
                "Sn",
                "Ta (stated Table 2a)",
                "Zr" ] ;
    ada:analyticalMode "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every two samples (stated section 2.1.1)" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "10B",
                "118Sn",
                "119Sn",
                "11B",
                "121Sb",
                "123Sb",
                "178Hf",
                "179Hf",
                "181Ta (Table 2a)",
                "90Zr",
                "91Zr",
                "93Nb",
                "95Mo",
                "97Mo" ] ;
    ada:chromatographicSeparationApplied "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.1)" ;
    ada:driftCorrectionMethod "Standard bracketing" ;
    ada:finalSolutionMatrix "0.5 mol/l HF (stated section 2.1.1)" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "None (ID-IS method: spike isotope ratios used; stated section 2.1)" ;
    ada:isotopeDilutionSpike "Multi-element enriched isotope spikes (Mo, Sn, Sb, Zr, Hf, Ta, B spikes; stated section 2.1)" ;
    ada:massCyclesPerReplicate "48 scans per 30 s acquisition (stated section 2.1.1)" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 1% (stated section 2.1.1)" ;
    ada:perAnalyteCalibrationStrategy "Isotope dilution (all analytes)" ;
    ada:primaryStandardNameDefault "Multi-element standard solution (not formally named; stated section 2.1.1)" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "B, Ti, Zr, Nb, Mo, Sn, Sb, Hf and Ta mass fractions (ug g-1); detection limits in solution (pg g-1) and in rock (ng g-1) [Table 2a]" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "Standard solution measured every two samples (stated section 2.1.1)" ;
    ada:samplingUnit "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites" ;
    ada:secondaryReferenceMaterialDefault "USGS and GSJ geological reference materials and carbonaceous chondrites (stated Table 5)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "~180 s (~3 min; stated: each measurement ~6 min including ~3 min wash; section 2.1.1)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
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
    schema1:defaultValue 9.2e-01 ;
    schema1:description "0.92 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Micro-flow PFA nebulizer PFA-20 (ESI, USA); self-aspiration (stated Table in section 2.1.1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2.1e+00 ;
    schema1:description "Self-aspiration; volumetric flow rate N (stated Table in section 2.1.1)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Scott double-pass, cooled at 2 deg C, Teflon (stated Table in section 2.1.1)" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.90 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2.5e-01 ;
    schema1:description "0.25 L/min supplementary Ar for PFA micronebulizer (stated Table in section 2.1.1)" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~3 min washout; ~3 min uptake stabilization (stated section 2.1.1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.6e+00 ;
    schema1:description "1.6 kW (stated Table in section 2.1.1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500cs (stated section 2.1.1)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "STD (standard mode, no gas)" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial> ;
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
    schema1:name "Quartz glass torch with Pt injector (stated Table in section 2.1.1)" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Agilent -- \"A Q-pole type ICP mass spectrometer, Agilent 7500 cs (Yokogawa Analytical Systems, Japan)\"" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/detectorConfiguration> ;
    schema1:value "Dual mode: pulse counting + analog (crossover ~10^6 cps; stated section 2.1.1)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/guardElectrode> a schema1:PropertyValue ;
    schema1:name "Guard Electrode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/guardElectrode> ;
    schema1:value "On (shield torch system used; stated section 2.1.1)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "IUPAC isotope dilution equations (ID-IS method; stated section 2.1)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/massResolutionSetting> ;
    schema1:value "Unit resolution (quadrupole, fixed; m/Delta-m ~300)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1.6 kW; stated section 2.1.1)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Pt sampler and Pt skimmer (stated Table in section 2.1.1)" .


```


### solutionQicpmsTAPP example Agilent8800
solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel.
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
  "@id": "ex:solutionQicpmsTAPP-Agilent8800",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — Agilent8800",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v34.csv). Reported detail: ada:perAnalyteCalibrationStrategy = External calibration for both Te and Se.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "N — 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW"
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
            "Estuarine suspended particulate matter and sediment (Gironde Estuary sorption experiments)"
          ]
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 8800 (QQQ-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "ICP-MS/MS (triple-quadrupole mode)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "O2 (used as the collision/reaction gas for the mass shift)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "O2"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Agilent",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Te and Se"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "125Te",
      "77Se"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh, to correct for matrix effects",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Te and Se concentrations (ug L-1; mg kg-1)"
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
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-Agilent8800",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Agilent8800",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v34.csv). Reported detail: ada:perAnalyteCalibrationStrategy = External calibration for both Te and Se.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "N \u2014 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW"
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
            "Estuarine suspended particulate matter and sediment (Gironde Estuary sorption experiments)"
          ]
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 8800 (QQQ-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "ICP-MS/MS (triple-quadrupole mode)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "O2 (used as the collision/reaction gas for the mass shift)"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "O2"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Agilent",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Te and Se"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "125Te",
      "77Se"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh, to correct for matrix effects",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Te and Se concentrations (ug L-1; mg kg-1)"
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
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-Agilent8800 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v34.csv). Reported detail: ada:perAnalyteCalibrationStrategy = External calibration for both Te and Se." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "N — 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — Agilent8800" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Estuarine suspended particulate matter and sediment (Gironde Estuary sorption experiments)" ] ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Te and Se" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "125Te",
                "77Se" ] ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "103Rh, to correct for matrix effects" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Te and Se concentrations (ug L-1; mg kg-1)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "missing" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 8800 (QQQ-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "ICP-MS/MS (triple-quadrupole mode)" .

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
            schema1:name "Agilent" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> a schema1:PropertyValue ;
    schema1:name "Collision Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:value "O2 (used as the collision/reaction gas for the mass shift)" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> a schema1:PropertyValue ;
    schema1:name "Reaction Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:value "O2" .


```


### solutionQicpmsTAPP example P6
solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated.
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
  "@id": "ex:solutionQicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — P6",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "N — instrument given as 'iCAP-TQ, Thermo' with no laboratory stated"
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
            "Estuarine sediment — total digestions and selective extraction fractions"
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (tri-acid) and 40-50 mg (microwave)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Dried at 50 C and homogenised in an agate mortar before microwave digestion",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Tri-acid HNO3+HCl+HF: 750 uL HNO3 (14M), 1.5 mL HCl (10M), 2.5 mL HF (29M); re-dissolved in 250 uL HNO3. Microwave route for Se: 3 mL HNO3, 0.5 mL H2O2, 0.25 mL HF, 0.5 mL Milli-Q",
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) on a heating block; PTFE vessels for evaporation; microwave START1500 (MLS GmbH)"
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
            "schema:defaultValue": 110,
            "schema:description": "110 C on the heating block; evaporation at 120 C; microwave ramp to 210 C held 10 min; evaporation at 70 C"
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
            "schema:defaultValue": "2 h at 110 C; microwave 10 min at 210 C then cooling overnight"
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
  "ada:finalSolutionMatrix": "Made up to 10 mL with Milli-Q water (18.2 MOhm); Se route made up to 6 mL",
  "ada:chromatographicSeparationApplied": "No — sequential selective extractions (acetate, ascorbate, H2O2, HCl/HNO3) rather than chromatography",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCAP-TQ",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He for KED; O2 for the mass-shift mode"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "O2 (for the 125Te mass-shift mode)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Te"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "125Te and 126Te (and their O-shifted products)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "NCS 73307 stream sediment"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Particulate Te concentration (mg kg-1)"
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
  "ada:samplingUnit": "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 P6",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "N \u2014 instrument given as 'iCAP-TQ, Thermo' with no laboratory stated"
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
            "Estuarine sediment \u2014 total digestions and selective extraction fractions"
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (tri-acid) and 40-50 mg (microwave)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Dried at 50 C and homogenised in an agate mortar before microwave digestion",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Tri-acid HNO3+HCl+HF: 750 uL HNO3 (14M), 1.5 mL HCl (10M), 2.5 mL HF (29M); re-dissolved in 250 uL HNO3. Microwave route for Se: 3 mL HNO3, 0.5 mL H2O2, 0.25 mL HF, 0.5 mL Milli-Q",
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) on a heating block; PTFE vessels for evaporation; microwave START1500 (MLS GmbH)"
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
            "schema:defaultValue": 110,
            "schema:description": "110 C on the heating block; evaporation at 120 C; microwave ramp to 210 C held 10 min; evaporation at 70 C"
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
            "schema:defaultValue": "2 h at 110 C; microwave 10 min at 210 C then cooling overnight"
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
  "ada:finalSolutionMatrix": "Made up to 10 mL with Milli-Q water (18.2 MOhm); Se route made up to 6 mL",
  "ada:chromatographicSeparationApplied": "No \u2014 sequential selective extractions (acetate, ascorbate, H2O2, HCl/HNO3) rather than chromatography",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCAP-TQ",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He for KED; O2 for the mass-shift mode"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "O2 (for the 125Te mass-shift mode)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Te"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "125Te and 126Te (and their O-shifted products)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "NCS 73307 stream sediment"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Particulate Te concentration (mg kg-1)"
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
  "ada:samplingUnit": "Weighed sediment aliquot \u2014 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-P6 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Dried at 50 C and homogenised in an agate mortar before microwave digestion" ;
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
                            schema1:name "Tri-acid HNO3+HCl+HF: 750 uL HNO3 (14M), 1.5 mL HCl (10M), 2.5 mL HF (29M); re-dissolved in 250 uL HNO3. Microwave route for Se: 3 mL HNO3, 0.5 mL H2O2, 0.25 mL HF, 0.5 mL Milli-Q" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v34.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "N — instrument given as 'iCAP-TQ, Thermo' with no laboratory stated" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — P6" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Estuarine sediment — total digestions and selective extraction fractions" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Te" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "125Te and 126Te (and their O-shifted products)" ] ;
    ada:chromatographicSeparationApplied "No — sequential selective extractions (acetate, ascorbate, H2O2, HCl/HNO3) rather than chromatography" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "Made up to 10 mL with Milli-Q water (18.2 MOhm); Se route made up to 6 mL" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "missing" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Particulate Te concentration (mg kg-1)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction" ;
    ada:secondaryReferenceMaterialDefault "NCS 73307 stream sediment" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2 h at 110 C; microwave 10 min at 210 C then cooling overnight" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 110 ;
    schema1:description "110 C on the heating block; evaporation at 120 C; microwave ramp to 210 C held 10 min; evaporation at 70 C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Closed PP tubes (DigiTUBEs, SCP Science) on a heating block; PTFE vessels for evaporation; microwave START1500 (MLS GmbH)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 30 ;
    schema1:description "30 mg (tri-acid) and 40-50 mg (microwave)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCAP-TQ" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "N/A" .

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
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> a schema1:PropertyValue ;
    schema1:name "Collision Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:value "He for KED; O2 for the mass-shift mode" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> a schema1:PropertyValue ;
    schema1:name "Reaction Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:value "O2 (for the 125Te mass-shift mode)" .


```


### solutionQicpmsTAPP example P7
solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe.
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
  "@id": "ex:solutionQicpmsTAPP-P7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — P7",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Karlsruhe Institute of Technology (KIT), Germany"
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
            "Estuarine water — dissolved Se from sorption kinetics and isotherms"
          ]
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "XSeries 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He+H2 mixture at 92% : 8%, to minimise 40Ar37Cl interferences"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "N/A — collision mode only"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Se"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N — Se isotopes not individually stated"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh and 115In",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "CRM-TMDW drinking water and NIST 1643f freshwater"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Dissolved Se concentration (ug L-1)"
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
  "ada:samplingUnit": "N — sub-sampled water aliquots",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-P7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 P7",
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Karlsruhe Institute of Technology (KIT), Germany"
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
            "Estuarine water \u2014 dissolved Se from sorption kinetics and isotherms"
          ]
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "XSeries 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He+H2 mixture at 92% : 8%, to minimise 40Ar37Cl interferences"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "N/A \u2014 collision mode only"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Se"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N \u2014 Se isotopes not individually stated"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh and 115In",
  "ada:perAnalyteCalibrationStrategy": [
    "External calibration (all analytes)"
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "CRM-TMDW drinking water and NIST 1643f freshwater"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Dissolved Se concentration (ug L-1)"
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
  "ada:samplingUnit": "N \u2014 sub-sampled water aliquots",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-P7 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v34.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Karlsruhe Institute of Technology (KIT), Germany" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — P7" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Estuarine water — dissolved Se from sorption kinetics and isotherms" ] ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Se" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "N — Se isotopes not individually stated" ] ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "103Rh and 115In" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "External calibration (all analytes)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Dissolved Se concentration (ug L-1)" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "N — sub-sampled water aliquots" ;
    ada:secondaryReferenceMaterialDefault "CRM-TMDW drinking water and NIST 1643f freshwater" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "XSeries 2" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "N/A" .

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
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> a schema1:PropertyValue ;
    schema1:name "Collision Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:value "He+H2 mixture at 92% : 8%, to minimise 40Ar37Cl interferences" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> a schema1:PropertyValue ;
    schema1:name "Reaction Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:value "N/A — collision mode only" .


```


### solutionQicpmsTAPP example P8
solutionQicpmsTAPP instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo.
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
  "@id": "ex:solutionQicpmsTAPP-P8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol — P8",
  "schema:description": "solutionQicpmsTAPP instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Science Tokyo"
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
            "Carbonaceous asteroid particles (Ryugu, Hayabusa2 TD1) and the Allende chondrite"
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
          "schema:defaultValue": 1.478,
          "schema:description": "1.478-4.325 mg per particle; 4-10% aliquot taken for Group-1"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 ug readability) and transferred to PFA vials without powdering",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "ID-IS method of Kagami and Yokoyama (2021); isotope dilution for Ti, Zr, Mo, Hf and W"
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
            "schema:defaultValue": "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'"
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
            "schema:name": "0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water; then 0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O2; final 0.2 mL HNO3 + 0.2 mL H2O2",
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
            "schema:value": "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches to maintain high-pressure conditions"
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
            "schema:value": "Four heating stages are described"
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
            "schema:defaultValue": 120,
            "schema:description": "120 C, then 220 C, then 100 C; second stage 150 C; final 80 C"
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
            "schema:defaultValue": "3 h ultrasonic agitation, 12 h at 120 C, 5 days at 220 C, 1 day at 150 C, 1 day at 80 C"
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
  "ada:finalSolutionMatrix": "5 mL 0.5 M HNO3, dilution factors 1200 (A0066) to 3400 (A0259); Group-1 aliquots diluted to DF 20,000; Group-3 in 0.5 M HNO3 + ~0.05 M HF",
  "ada:isotopeDilutionSpike": "97Mo (94.19%, Mo = 28 ng/g) and 182W (94.07%, W = 12 ng/g), dissolved in ~1 M HF",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCAP TQ",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "KED (kinetic energy discrimination, He gas)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "N/A — KED only"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "54 elements: Li",
      "Be",
      "Sc",
      "Ga",
      "As",
      "Se",
      "Rb",
      "Sr",
      "Y",
      "Ag",
      "Cd",
      "In",
      "Cs",
      "Ba",
      "La-Lu",
      "Tl",
      "Pb",
      "Bi",
      "Th",
      "U",
      "Na",
      "Mg",
      "Al",
      "P",
      "K",
      "Ca",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ti",
      "Zr",
      "Nb",
      "Hf",
      "Ta",
      "Mo",
      "W"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "54 elements measured in three groups: Group-1 trace elements",
      "Group-2 major and minor elements",
      "Group-3 HFSE plus Mo and W"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh for the calibration-curve elements; 113In-203Tl for the ID-IS method; 91Zr and 179Hf for Nb and Ta",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "XSTC-13 and a custom solution for the calibration-curve elements; MISA05-1 (AccuStandard Inc.) for Group-3",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Allende powder (20 mg), dissolved and measured n = 5 under the same procedure"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Elemental abundances, CI-normalised ratios"
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
  "ada:samplingUnit": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-P8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 P8",
  "schema:description": "solutionQicpmsTAPP instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo (publication column of Solution_Q-ICP-MS_TAPP_v34.csv).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution Q-ICP-MS (triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Science Tokyo"
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
            "Carbonaceous asteroid particles (Ryugu, Hayabusa2 TD1) and the Allende chondrite"
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
          "schema:defaultValue": 1.478,
          "schema:description": "1.478-4.325 mg per particle; 4-10% aliquot taken for Group-1"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 ug readability) and transferred to PFA vials without powdering",
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
            "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "ID-IS method of Kagami and Yokoyama (2021); isotope dilution for Ti, Zr, Mo, Hf and W"
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
            "schema:defaultValue": "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'"
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
            "schema:name": "0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water; then 0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O2; final 0.2 mL HNO3 + 0.2 mL H2O2",
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
            "schema:value": "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches to maintain high-pressure conditions"
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
            "schema:value": "Four heating stages are described"
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
            "schema:defaultValue": 120,
            "schema:description": "120 C, then 220 C, then 100 C; second stage 150 C; final 80 C"
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
            "schema:defaultValue": "3 h ultrasonic agitation, 12 h at 120 C, 5 days at 220 C, 1 day at 150 C, 1 day at 80 C"
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
  "ada:finalSolutionMatrix": "5 mL 0.5 M HNO3, dilution factors 1200 (A0066) to 3400 (A0259); Group-1 aliquots diluted to DF 20,000; Group-3 in 0.5 M HNO3 + ~0.05 M HF",
  "ada:isotopeDilutionSpike": "97Mo (94.19%, Mo = 28 ng/g) and 182W (94.07%, W = 12 ng/g), dissolved in ~1 M HF",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCAP TQ",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "KED (kinetic energy discrimination, He gas)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/collisionGasType"
                }
              ],
              "schema:name": "Collision Gas Type",
              "schema:value": "He"
            },
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "N/A \u2014 KED only"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
            "Sample Introduction System",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Sample-Introduction-System"
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
        "schema:name": "Thermo Fisher Scientific",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "54 elements: Li",
      "Be",
      "Sc",
      "Ga",
      "As",
      "Se",
      "Rb",
      "Sr",
      "Y",
      "Ag",
      "Cd",
      "In",
      "Cs",
      "Ba",
      "La-Lu",
      "Tl",
      "Pb",
      "Bi",
      "Th",
      "U",
      "Na",
      "Mg",
      "Al",
      "P",
      "K",
      "Ca",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ti",
      "Zr",
      "Nb",
      "Hf",
      "Ta",
      "Mo",
      "W"
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
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "54 elements measured in three groups: Group-1 trace elements",
      "Group-2 major and minor elements",
      "Group-3 HFSE plus Mo and W"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalStandardElement": "103Rh for the calibration-curve elements; 113In-203Tl for the ID-IS method; 91Zr and 179Hf for Nb and Ta",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "XSTC-13 and a custom solution for the calibration-curve elements; MISA05-1 (AccuStandard Inc.) for Group-3",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Allende powder (20 mg), dissolved and measured n = 5 under the same procedure"
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedPropertyTemplate": {
    "ada:defaultReportedProperties": [
      "Elemental abundances, CI-normalised ratios"
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
  "ada:samplingUnit": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:solutionQicpmsTAPP-P8 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water; then 0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O2; final 0.2 mL HNO3 + 0.2 mL H2O2" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 ug readability) and transferred to PFA vials without powdering" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo (publication column of Solution_Q-ICP-MS_TAPP_v34.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Science Tokyo" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — P8" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Carbonaceous asteroid particles (Ryugu, Hayabusa2 TD1) and the Allende chondrite" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "54 elements: Li",
                "Ag",
                "Al",
                "As",
                "Ba",
                "Be",
                "Bi",
                "Ca",
                "Cd",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Fe",
                "Ga",
                "Hf",
                "In",
                "K",
                "La-Lu",
                "Mg",
                "Mn",
                "Mo",
                "Na",
                "Nb",
                "Ni",
                "P",
                "Pb",
                "Rb",
                "Sc",
                "Se",
                "Sr",
                "Ta",
                "Th",
                "Ti",
                "Tl",
                "U",
                "V",
                "W",
                "Y",
                "Zn",
                "Zr" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> ;
            ada:defaultChannels "54 elements measured in three groups: Group-1 trace elements",
                "Group-2 major and minor elements",
                "Group-3 HFSE plus Mo and W" ] ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "5 mL 0.5 M HNO3, dilution factors 1200 (A0066) to 3400 (A0259); Group-1 aliquots diluted to DF 20,000; Group-3 in 0.5 M HNO3 + ~0.05 M HF" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "103Rh for the calibration-curve elements; 113In-203Tl for the ID-IS method; 91Zr and 179Hf for Nb and Ta" ;
    ada:isotopeDilutionSpike "97Mo (94.19%, Mo = 28 ng/g) and 182W (94.07%, W = 12 ng/g), dissolved in ~1 M HF" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "XSTC-13 and a custom solution for the calibration-curve elements; MISA05-1 (AccuStandard Inc.) for Group-3" ;
    ada:reportedPropertyTemplate [ ada:defaultReportedProperties "Elemental abundances, CI-normalised ratios" ;
            ada:reportedPropertyColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "reportedProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende" ;
    ada:secondaryReferenceMaterialDefault "Smithsonian Allende powder (20 mg), dissolved and measured n = 5 under the same procedure" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3 h ultrasonic agitation, 12 h at 120 C, 5 days at 220 C, 1 day at 150 C, 1 day at 80 C" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 120 ;
    schema1:description "120 C, then 220 C, then 100 C; second stage 150 C; final 80 C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches to maintain high-pressure conditions" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value "Four heating stages are described" ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.478e+00 ;
    schema1:description "1.478-4.325 mg per particle; 4-10% aliquot taken for Group-1" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCAP TQ" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "KED (kinetic energy discrimination, He gas)" .

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
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> a schema1:PropertyValue ;
    schema1:name "Collision Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionGasType> ;
    schema1:value "He" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "ID-IS method of Kagami and Yokoyama (2021); isotope dilution for Ti, Zr, Mo, Hf and W" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> a schema1:PropertyValue ;
    schema1:name "Reaction Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionGasType> ;
    schema1:value "N/A — KED only" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution Q-ICP-MS Technique-Aligned Protocol Profile (solutionQicpmsTAPP)
description: Solution quadrupole ICP-MS extension of the base TAPP definition, generated
  from tapp/Current TAPPs/Solution_Q-ICP-MS_TAPP_v34.csv via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
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
                        discharge and improving ion extraction efficiency.
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/solutionQicpmsTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/solutionQicpmsTAPP/guardElectrode
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
                          discharge and improving ion extraction efficiency.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionQicpmsTAPP/guardElectrode
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
                      - title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog detection modes. For Q-ICP-MS instruments with
                          dual-mode SEM detectors, a cross-calibration factor is measured
                          and applied at the pulse-to-analog crossover threshold.
                          Accurate cross-calibration is critical for analytes spanning
                          a wide concentration range in the same session.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                          Record 'None' if isotope dilution is not used."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod
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
                      - title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied to output
                          concentrations relative to a reference value (e.g., correction
                          to a monitor element's certified value in the calibration
                          standard).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog detection modes. For Q-ICP-MS instruments with
                          dual-mode SEM detectors, a cross-calibration factor is measured
                          and applied at the pulse-to-analog crossover threshold.
                          Accurate cross-calibration is critical for analytes spanning
                          a wide concentration range in the same session.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                          Record 'None' if isotope dilution is not used."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionQicpmsTAPP/isotopeDilutionDataReductionMethod
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
                        title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied to output
                          concentrations relative to a reference value (e.g., correction
                          to a monitor element's certified value in the calibration
                          standard).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                  - title: Mass Resolution Setting
                    description: "Mass resolution of the quadrupole analyser. For
                      quadrupole instruments, mass resolution is fixed at unit resolution
                      by instrument design (m/\u0394m \u2248 300); no operator selection
                      is possible. This field documents the instrument class constraint
                      at procedure level."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionQicpmsTAPP/massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                    readOnly: true
                  - title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer
                      and whether dual pulse-counting/analog mode is used. Most Q-ICP-MS
                      instruments use a single SEM in dual mode (pulse counting at
                      low signals, analog at high signals), with an instrument-specific
                      crossover threshold. The pulse-to-analog cross-calibration correction
                      is documented in Group 5.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionQicpmsTAPP/detectorConfiguration
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
                        const: ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault
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
                  - title: Doubly-Charged Species Monitor
                    description: Mass ratio monitored to estimate doubly-charged ion
                      (M2+) formation during instrument tuning. Doubly-charged ions
                      appear at half the nominal mass of the parent ion and can interfere
                      with lighter analyte masses. Ba2+/Ba+ (m/z 69/138) and Ce2+/Ce+
                      (m/z 70/140) are the most common proxies for solution ICP-MS.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault
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
                    title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    title: Mass Resolution Setting
                    description: "Mass resolution of the quadrupole analyser. For
                      quadrupole instruments, mass resolution is fixed at unit resolution
                      by instrument design (m/\u0394m \u2248 300); no operator selection
                      is possible. This field documents the instrument class constraint
                      at procedure level."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionQicpmsTAPP/massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
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
                    title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer
                      and whether dual pulse-counting/analog mode is used. Most Q-ICP-MS
                      instruments use a single SEM in dual mode (pulse counting at
                      low signals, analog at high signals), with an instrument-specific
                      crossover threshold. The pulse-to-analog cross-calibration correction
                      is documented in Group 5.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionQicpmsTAPP/detectorConfiguration
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
                        const: ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault
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
                    title: Doubly-Charged Species Monitor
                    description: Mass ratio monitored to estimate doubly-charged ion
                      (M2+) formation during instrument tuning. Doubly-charged ions
                      appear at half the nominal mass of the parent ion and can interfere
                      with lighter analyte masses. Ba2+/Ba+ (m/z 69/138) and Ce2+/Ce+
                      (m/z 70/140) are the most common proxies for solution ICP-MS.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault
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
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
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
                                const: ada:parameter/solutionQicpmsTAPP/torchDepthDefault
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
                                  const: ada:parameter/solutionQicpmsTAPP/torchDepthDefault
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
                                instruments offer multiple skimmer cone geometries
                                (standard, high-sensitivity) that differ in aperture
                                size and affect ion transmission efficiency and matrix
                                tolerance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration
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
                                matrices. Platinum (Pt) is used for samples in HCl-rich
                                or organic matrices due to greater corrosion resistance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial
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
                                instruments offer multiple skimmer cone geometries
                                (standard, high-sensitivity) that differ in aperture
                                size and affect ion transmission efficiency and matrix
                                tolerance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/interfaceConeConfiguration
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
                                matrices. Platinum (Pt) is used for samples in HCl-rich
                                or organic matrices due to greater corrosion resistance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/samplerAndSkimmerConeMaterial
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
                            const: Collision Reaction Cell
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Whether a collision or reaction cell is installed
                            and its operating mode for this procedure. STD = standard
                            mode with no cell gas; KED = kinetic energy discrimination
                            with He or H2 collision gas to suppress polyatomic interferences;
                            DRC = dynamic reaction cell with reactive gas (e.g., NH3).
                            Specific gas types, flow rates, and voltages are documented
                            in Group 4.
                          anyOf:
                          - type: string
                            enum:
                            - Not installed
                            - STD (standard mode, no gas)
                            - KED (kinetic energy discrimination, He gas)
                            - DRC (dynamic reaction cell, reactive gas)
                            - KED+DRC
                            - ICP-MS/MS (triple-quadrupole mode)
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Not installed
                              - STD (standard mode, no gas)
                              - KED (kinetic energy discrimination, He gas)
                              - DRC (dynamic reaction cell, reactive gas)
                              - KED+DRC
                              - ICP-MS/MS (triple-quadrupole mode)
                              - N/A
                              - None
                              - missing
                              readOnly: true
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Collision Gas Type
                              description: Type of collision gas used in KED mode
                                for polyatomic interference suppression. Record 'N/A'
                                if KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/collisionGasType
                                schema:name:
                                  const: Collision Gas Type
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            - title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas in KED mode
                                (mL/min). Higher flow rates provide greater interference
                                suppression at the cost of analyte sensitivity. Record
                                'N/A' if KED mode is not used. Record 'N/A' where
                                Collision/Reaction Cell (CRC) Configuration does not
                                include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: collisionGasFlowRateDefault
                                schema:name:
                                  const: Collision Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: mL/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            - title: Cell Exit Discrimination Voltage
                              description: Kinetic energy discrimination offset voltage
                                applied at the exit of the collision cell (V). Controls
                                the degree of polyatomic ion suppression. Record 'N/A'
                                if KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltageDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: cellExitDiscriminationVoltageDefault
                                schema:name:
                                  const: Cell Exit Discrimination Voltage
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: V
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                            - title: Reaction Gas Type
                              description: Type of reactive gas introduced into the
                                dynamic reaction cell (e.g., NH3, O2, CH4). Record
                                'N/A' if DRC mode is not used. Record 'N/A' where
                                Collision/Reaction Cell (CRC) Configuration does not
                                include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/reactionGasType
                                schema:name:
                                  const: Reaction Gas Type
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            - title: Reaction Gas Flow Rate
                              description: Flow rate of the reaction gas in DRC mode
                                (mL/min). Record 'N/A' if DRC mode is not used. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/reactionGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: reactionGasFlowRateDefault
                                schema:name:
                                  const: Reaction Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: mL/min
                              required:
                              - '@id'
                              - '@type'
                              - schema:valueName
                              - schema:name
                              - ada:dataType
                              - ada:fieldScope
                          allOf:
                          - contains:
                              title: Collision Gas Type
                              description: Type of collision gas used in KED mode
                                for polyatomic interference suppression. Record 'N/A'
                                if KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/collisionGasType
                                schema:name:
                                  const: Collision Gas Type
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
                              title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas in KED mode
                                (mL/min). Higher flow rates provide greater interference
                                suppression at the cost of analyte sensitivity. Record
                                'N/A' if KED mode is not used. Record 'N/A' where
                                Collision/Reaction Cell (CRC) Configuration does not
                                include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/collisionGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: collisionGasFlowRateDefault
                                schema:name:
                                  const: Collision Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: mL/min
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
                              title: Cell Exit Discrimination Voltage
                              description: Kinetic energy discrimination offset voltage
                                applied at the exit of the collision cell (V). Controls
                                the degree of polyatomic ion suppression. Record 'N/A'
                                if KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltageDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: cellExitDiscriminationVoltageDefault
                                schema:name:
                                  const: Cell Exit Discrimination Voltage
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: V
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
                              title: Reaction Gas Type
                              description: Type of reactive gas introduced into the
                                dynamic reaction cell (e.g., NH3, O2, CH4). Record
                                'N/A' if DRC mode is not used. Record 'N/A' where
                                Collision/Reaction Cell (CRC) Configuration does not
                                include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/reactionGasType
                                schema:name:
                                  const: Reaction Gas Type
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
                              title: Reaction Gas Flow Rate
                              description: Flow rate of the reaction gas in DRC mode
                                (mL/min). Record 'N/A' if DRC mode is not used. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/reactionGasFlowRateDefault
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: reactionGasFlowRateDefault
                                schema:name:
                                  const: Reaction Gas Flow Rate
                                ada:dataType:
                                  const: number
                                ada:fieldScope:
                                  const: session
                                schema:readonlyValue:
                                  const: false
                                ada:tier:
                                  const: R
                                schema:unitText:
                                  const: mL/min
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleUptakeRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerGasFlowRate
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleUptakeRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_nebulizerGasFlowRate
                            minContains: 0
                            maxContains: 1
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
                            - title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/rfPowerDefault
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
                            - title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault
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
                            - title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault
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
                            - title: Plasma Thermal Mode
                              description: "Whether the ICP plasma is operated under
                                cool plasma or normal (hot) plasma conditions. Normal
                                plasma (>1000 W RF) is standard for most solution
                                ICP-MS analyses. Cool plasma (\u2264900 W RF) reduces
                                argide-based interferences (e.g., 40Ar12C+ on 52Cr)
                                at the cost of reduced sensitivity and ionization
                                efficiency for most elements."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/plasmaThermalMode
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
                          allOf:
                          - contains:
                              title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/rfPowerDefault
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
                          - contains:
                              title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/coolantGasFlowRateDefault
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
                              title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRateDefault
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
                              title: Plasma Thermal Mode
                              description: "Whether the ICP plasma is operated under
                                cool plasma or normal (hot) plasma conditions. Normal
                                plasma (>1000 W RF) is standard for most solution
                                ICP-MS analyses. Cool plasma (\u2264900 W RF) reduces
                                argide-based interferences (e.g., 40Ar12C+ on 52Cr)
                                at the cost of reduced sensitivity and ionization
                                efficiency for most elements."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/plasmaThermalMode
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
                allOf:
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
                          const: Collision Reaction Cell
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
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: ICP Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: ICPMS
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_internalStandardConcentration
        - title: Spike / Outlier Filtering Approach
          description: Criteria used to identify and exclude anomalous replicate measurements
            or data points from the calculated mean.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproachDefault
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
              const: ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethodDefault
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
              const: ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproachDefault
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
              const: ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethodDefault
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
    ada:channelTemplate:
      type: object
      properties:
        ada:defaultChannels:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: Dwell Time per Mass
              description: Integration time spent on each mass peak per sweep (ms).
                May differ between masses where per-mass dwell times are programmed.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass
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
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
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
              description: Whether mathematical corrections for isobaric or polyatomic
                interferences are applied during data reduction (in addition to any
                KED or DRC mitigation in the instrument).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
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
                in data reduction. For Q-ICP-MS, common interferences include ArCl+
                on 75As, MoO+ species on Cd isotopes, and BaO+ on Eu. Additional interference
                mitigation via KED or DRC is documented in Group 3 and Group 4.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/interferingSpecies
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interference Correction Method
              description: Mathematical approach used to calculate and remove interference
                contributions from measured signals (e.g., interference standard solutions
                isolating specific polyatomics, mass-balance equations using empirical
                correction factors).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
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
              title: Dwell Time per Mass
              description: Integration time spent on each mass peak per sweep (ms).
                May differ between masses where per-mass dwell times are programmed.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/dwellTimePerMass
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
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
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
              description: Whether mathematical corrections for isobaric or polyatomic
                interferences are applied during data reduction (in addition to any
                KED or DRC mitigation in the instrument).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/isobaricInterferenceCorrectionsApplied
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
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
                in data reduction. For Q-ICP-MS, common interferences include ArCl+
                on 75As, MoO+ species on Cd isotopes, and BaO+ on Eu. Additional interference
                mitigation via KED or DRC is documented in Group 3 and Group 4.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/interferingSpecies
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
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
              description: Mathematical approach used to calculate and remove interference
                contributions from measured signals (e.g., interference standard solutions
                isolating specific polyatomics, mass-balance equations using empirical
                correction factors).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionQicpmsTAPP/interferenceCorrectionMethod
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
                  anyOf:
                  - type: string
                  - type: array
                    items:
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
    ada:massCyclesPerReplicate:
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
    ada:signalCollectionMode:
      description: Mode used to collect ion signal across the monitored masses. In
        peak hopping mode, the quadrupole jumps sequentially between pre-set mass
        positions and dwells at each peak; in scanning mode, the quadrupole sweeps
        continuously across a defined mass range. Peak hopping is standard for multi-element
        trace analysis as it maximises integration time at each mass.
      type: string
      enum:
      - Peak hopping
      - Scanning
      - N/A
      - None
      - missing
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
        in Oxide Production. CeO+/Ce+ (m/z 156/140) is the standard monitor proxy.
      type: string
      readOnly: true
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
        - ID for Zn (67Zn spike); external calibration for all other elements
        - External calibration + standard addition
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
    ada:primaryStandardNameDefault:
      description: Name and reference material identifier of the external calibration
        standard used to convert signal intensities to elemental concentrations. Include
        the material name, its source or supplier, and a citation for the accepted
        values used, since results calibrated against different published values for
        the same material are not directly comparable.
      type: string
    ada:calibrationMeasurementFrequency:
      description: How often the primary calibration standard is measured relative
        to unknown samples within a session.
      type: string
      readOnly: true
    ada:secondaryReferenceMaterialDefault:
      type: array
      items:
        description: Reference material(s) measured as unknowns to independently assess
          analytical accuracy. Specify material name and expected-value source.
        type: string
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set). Specify units
                (\xB5g/g or \xB5g/L) and whether values are procedure-typical estimates
                or session-specific measured values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionQicpmsTAPP/detectionLimit
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
              title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set). Specify units
                (\xB5g/g or \xB5g/L) and whether values are procedure-typical estimates
                or session-specific measured values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionQicpmsTAPP/detectionLimit
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/detectionLimitMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
  required:
  - ada:massCyclesPerReplicate
  - ada:numberOfReplicatesPerSample
  - ada:sampleSequenceDesign
  - ada:signalCollectionMode
  - ada:internalStandardElement
  - ada:oxideProductionMethodAndThreshold
  - ada:internalStandardApproach
  - ada:driftCorrectionMethod
  - ada:signalIntegrationIntervalMethod
  - ada:blankBackgroundCorrectionMethod
  - ada:primaryStandardNameDefault
  - ada:calibrationMeasurementFrequency

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld)

## Sources

* [Solution_Q-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp`

