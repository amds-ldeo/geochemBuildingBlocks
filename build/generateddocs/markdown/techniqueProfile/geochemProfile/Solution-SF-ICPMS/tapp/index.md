
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
  "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Pb"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Soil samples"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
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
      "schema:model": {
        "schema:name": "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "N — the Attom's 'deflector peak jump' mode is stated (§2.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "N — Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3"
        },
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\""
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
      "schema:manufacturer": {
        "schema:name": "Nu Instruments",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/eScanRange",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/eScanRange"
        }
      ],
      "schema:name": "E-scan Range",
      "schema:value": "N/A — Nu Attom uses deflector peak jump, not E-scan",
      "schema:unitText": "example value"
    },
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/tripleScanningMode",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/tripleScanningMode"
        }
      ],
      "schema:name": "Triple Scanning Mode",
      "schema:value": "N/A — Nu Attom instrument; not applicable"
    },
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
  "ada:numberOfScansPerReplicate": "all: 30 sets of 2000 sweeps — total analysis time 4.5 min (§2.4)",
  "ada:numberOfReplicatesPerSample": "1 — one acquisition of 30 sets of 2000 sweeps (§2.4)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Soils oven-dried (50 °C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' — §2.1, §2.2, §2.4; the rock chips were analysed by MC-ICP-MS only",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing"
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      },
      {
        "schema:name": "Sample digestion",
        "schema:description": "TD HNO3 leach (3 ml conc. HNO3, 80 °C, 48 h, leachate discarded); TD HF (4 ml conc. HF, 100 °C, 48 h, evaporated); TD HNO3 (2 × 1 ml conc. HNO3, 100 °C); TD HCl (5 ml 6 M HCl, 80 °C, 15 h, then centrifuged); AR leach (3 ml aqua regia, 3:1 HCl:HNO3, 20 °C, 15 h, then centrifuged) — §2.2",
        "bios:reagent": [
          {
            "schema:name": "TD HNO3 leach: conc. HNO3; TD HF: conc. HF; TD HNO3: conc. HNO3; TD HCl: 6 M HCl; AR leach: aqua regia (3:1 HCl:HNO3) — §2.2",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Melbourne, Australia (affiliation)"
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
  "ada:samplingUnitType": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:reportedProperties": [
    "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb — dimensionless Pb isotope ratios (§2.4)"
  ],
  "ada:chromatographicSeparationApplied": "None — the SC-SF-ICP-MS splits were analysed unseparated; the anion-exchange separation (§2.3) was for MC-ICP-MS",
  "ada:isotopeDilutionSpike": "None (Tl added for mass fractionation correction only, not ID)",
  "ada:finalSolutionMatrix": "all: 2% HNO3 doped with 1 ppb Tl — §2.4",
  "ada:washTimeBetweenSamples": "10 s in each of two 2% HNO3 reservoirs, then a third reservoir for the blank — the blank solution 'was replaced every 20 samples' (§2.4)",
  "ada:uncertaintyLevel": "2 standard errors for within-run precision; 2sd for the averages of standards — 'Typical within-run precision (2 standards errors)' (§2.4); '(2sd, n = 22)'",
  "ada:blankBackgroundCorrectionMethod": "Blank determination before each sample acquisition (average 900 cps on 208Pb, equivalent to 1.8 ppt Pb); on-line baseline correction — §2.4",
  "ada:internalStandardElement": "all: Tl (203Tl, 205Tl), for mass-bias correction — §2.4",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Pb"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Soil samples"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
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
      "schema:model": {
        "schema:name": "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "N \u2014 the Attom's 'deflector peak jump' mode is stated (\u00a72.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "N \u2014 Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3"
        },
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\""
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
      "schema:manufacturer": {
        "schema:name": "Nu Instruments",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/eScanRange",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/eScanRange"
        }
      ],
      "schema:name": "E-scan Range",
      "schema:value": "N/A \u2014 Nu Attom uses deflector peak jump, not E-scan",
      "schema:unitText": "example value"
    },
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/tripleScanningMode",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/tripleScanningMode"
        }
      ],
      "schema:name": "Triple Scanning Mode",
      "schema:value": "N/A \u2014 Nu Attom instrument; not applicable"
    },
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
  "ada:numberOfScansPerReplicate": "all: 30 sets of 2000 sweeps \u2014 total analysis time 4.5 min (\u00a72.4)",
  "ada:numberOfReplicatesPerSample": "1 \u2014 one acquisition of 30 sets of 2000 sweeps (\u00a72.4)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Soils oven-dried (50 \u00b0C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' \u2014 \u00a72.1, \u00a72.2, \u00a72.4; the rock chips were analysed by MC-ICP-MS only",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing"
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      },
      {
        "schema:name": "Sample digestion",
        "schema:description": "TD HNO3 leach (3 ml conc. HNO3, 80 \u00b0C, 48 h, leachate discarded); TD HF (4 ml conc. HF, 100 \u00b0C, 48 h, evaporated); TD HNO3 (2 \u00d7 1 ml conc. HNO3, 100 \u00b0C); TD HCl (5 ml 6 M HCl, 80 \u00b0C, 15 h, then centrifuged); AR leach (3 ml aqua regia, 3:1 HCl:HNO3, 20 \u00b0C, 15 h, then centrifuged) \u2014 \u00a72.2",
        "bios:reagent": [
          {
            "schema:name": "TD HNO3 leach: conc. HNO3; TD HF: conc. HF; TD HNO3: conc. HNO3; TD HCl: 6 M HCl; AR leach: aqua regia (3:1 HCl:HNO3) \u2014 \u00a72.2",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Melbourne, Australia (affiliation)"
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
  "ada:samplingUnitType": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:reportedProperties": [
    "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb \u2014 dimensionless Pb isotope ratios (\u00a72.4)"
  ],
  "ada:chromatographicSeparationApplied": "None \u2014 the SC-SF-ICP-MS splits were analysed unseparated; the anion-exchange separation (\u00a72.3) was for MC-ICP-MS",
  "ada:isotopeDilutionSpike": "None (Tl added for mass fractionation correction only, not ID)",
  "ada:finalSolutionMatrix": "all: 2% HNO3 doped with 1 ppb Tl \u2014 \u00a72.4",
  "ada:washTimeBetweenSamples": "10 s in each of two 2% HNO3 reservoirs, then a third reservoir for the blank \u2014 the blank solution 'was replaced every 20 samples' (\u00a72.4)",
  "ada:uncertaintyLevel": "2 standard errors for within-run precision; 2sd for the averages of standards \u2014 'Typical within-run precision (2 standards errors)' (\u00a72.4); '(2sd, n = 22)'",
  "ada:blankBackgroundCorrectionMethod": "Blank determination before each sample acquisition (average 900 cps on 208Pb, equivalent to 1.8 ppt Pb); on-line baseline correction \u2014 \u00a72.4",
  "ada:internalStandardElement": "all: Tl (203Tl, 205Tl), for mass-bias correction \u2014 \u00a72.4",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-P0> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Soils oven-dried (50 °C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' — §2.1, §2.2, §2.4; the rock chips were analysed by MC-ICP-MS only" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "TD HNO3 leach (3 ml conc. HNO3, 80 °C, 48 h, leachate discarded); TD HF (4 ml conc. HF, 100 °C, 48 h, evaporated); TD HNO3 (2 × 1 ml conc. HNO3, 100 °C); TD HCl (5 ml 6 M HCl, 80 °C, 15 h, then centrifuged); AR leach (3 ml aqua regia, 3:1 HCl:HNO3, 20 °C, 15 h, then centrifuged) — §2.2" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "TD HNO3 leach: conc. HNO3; TD HF: conc. HF; TD HNO3: conc. HNO3; TD HCl: 6 M HCl; AR leach: aqua regia (3:1 HCl:HNO3) — §2.2" ] ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/eScanRange>,
        <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/tripleScanningMode> ;
    schema1:datePublished "missing" ;
    schema1:description "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)" ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Melbourne, Australia (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P0" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)" ;
                    schema1:name "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler" ;
    ada:blankBackgroundCorrectionMethod "Blank determination before each sample acquisition (average 900 cps on 208Pb, equivalent to 1.8 ppt Pb); on-line baseline correction — §2.4" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None — the SC-SF-ICP-MS splits were analysed unseparated; the anion-exchange separation (§2.3) was for MC-ICP-MS" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "all: 2% HNO3 doped with 1 ppb Tl — §2.4" ;
    ada:internalStandardElement "all: Tl (203Tl, 205Tl), for mass-bias correction — §2.4" ;
    ada:isotopeDilutionSpike "None (Tl added for mass fractionation correction only, not ID)" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample "1 — one acquisition of 30 sets of 2000 sweeps (§2.4)" ;
    ada:numberOfScansPerReplicate "all: 30 sets of 2000 sweeps — total analysis time 4.5 min (§2.4)" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "206Pb/204Pb, 207Pb/204Pb, 208Pb/204Pb, 207Pb/206Pb, 208Pb/206Pb — dimensionless Pb isotope ratios (§2.4)" ;
    ada:samplingUnitType "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"" ;
    ada:secondaryReferenceMaterialDefault "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Soil samples" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Pb" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "2 standard errors for within-run precision; 2sd for the averages of standards — 'Typical within-run precision (2 standards errors)' (§2.4); '(2sd, n = 22)'" ;
    ada:washTimeBetweenSamples "10 s in each of two 2% HNO3 reservoirs, then a third reservoir for the blank — the blank solution 'was replaced every 20 samples' (§2.4)" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nu Instruments" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nu Instruments Attom SC-SF-ICP-MS (stated section 2.3)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "N — the Attom's 'deflector peak jump' mode is stated (§2.4)" ;
    schema1:valueName "detectorConfiguration" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/eScanRange> a schema1:PropertyValue ;
    schema1:name "E-scan Range" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/eScanRange> ;
    schema1:unitText "example value" ;
    schema1:value "N/A — Nu Attom uses deflector peak jump, not E-scan" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/tripleScanningMode> a schema1:PropertyValue ;
    schema1:name "Triple Scanning Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/tripleScanningMode> ;
    schema1:value "N/A — Nu Attom instrument; not applicable" .


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
  "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = Rh internal standard — 'In order to correct the instrumental drift, the internal standard concentration of Rh was kept constant at 5 ng mL−1 in the sample, calibration, and blank solutions' (§2.2).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "Be",
      "Sc",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ge",
      "Rb",
      "Sr",
      "Y",
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
      "Lu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14.6,
              "schema:description": "14.6 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — RF power 1300 W (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Counting — Table 1 'Detection mode'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (Table 1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\""
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "magnetite",
      "pyrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
          }
        ],
        "ada:detectionLimitMethod": "all: 3 × SD of six procedural blanks (MDL) — Table 2 note; the IDL is 3 × SD of six replicate measurements of 2% HNO3",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "HCl-HNO3 attack: 48 h; re-dissolution: N — §2.3.1"
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
            "schema:defaultValue": 3,
            "schema:description": "HCl-HNO3 attack: 130 °C; re-dissolution: 130 °C (evaporation) — §2.3.1"
          }
        ],
        "schema:description": "HCl-HNO3 attack (1.5 ml 6 M HCl + 0.5 ml 8 M HNO3, 130 °C, 48 h); re-dissolution (evaporated at 130 °C close to dryness, then 1.5 ml 10 M HCl) — §2.3.1, for magnetite and pyrite; FER-2 took 1 ml 28 M HF + 1 ml 8 M HNO3 at 130 °C for at least 48 h, then 1.5 ml 10 M HCl for 24 h",
        "bios:reagent": [
          {
            "schema:name": "HCl-HNO3 attack: 6 M HCl + 8 M HNO3; re-dissolution: 10 M HCl — §2.3.1",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
  },
  "ada:samplingUnitType": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:reportedProperties": [
    "Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Ge, Rb, Sr, Y, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (µg/g) — Table 3 (FER-2) in µg g⁻¹; the unit of Table 4 (samples) is not stated in its header"
  ],
  "ada:chromatographicSeparationApplied": "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)",
  "ada:isotopeDilutionSpike": "None (external calibration used; stated section 2.3)",
  "ada:finalSolutionMatrix": "all: 2% HNO3 containing 5 ng/mL Rh — §2.3.2",
  "ada:washTimeBetweenSamples": "60 s — Table 1; '1 min with 3% v/v HNO3' (§2.1)",
  "ada:uncertaintyLevel": "1 standard deviation -- \"The mean values and respective standard deviations (s) for three analyses\"; \"Mean +/- s (n = 3)\"; \"RSD = standard deviation/mean x 100%\"",
  "ada:blankBackgroundCorrectionMethod": "N — a blank solution in 2% HNO3 is part of the calibration set (§2.2); the blank correction is not described",
  "ada:internalStandardElement": "all: Rh (103Rh) — Table 1",
  "ada:secondaryReferenceMaterialDefault": [
    "FER-2 — iron-formation reference material (CCRMP), 'used to validate of the proposed method' (§2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = Rh internal standard \u2014 'In order to correct the instrumental drift, the internal standard concentration of Rh was kept constant at 5 ng mL\u22121 in the sample, calibration, and blank solutions' (\u00a72.2).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "Be",
      "Sc",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ge",
      "Rb",
      "Sr",
      "Y",
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
      "Lu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14.6,
              "schema:description": "14.6 L/min (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 RF power 1300 W (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Counting \u2014 Table 1 'Detection mode'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash between samples (Table 1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\""
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "magnetite",
      "pyrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
          }
        ],
        "ada:detectionLimitMethod": "all: 3 \u00d7 SD of six procedural blanks (MDL) \u2014 Table 2 note; the IDL is 3 \u00d7 SD of six replicate measurements of 2% HNO3",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionDurationDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionDurationDefault",
            "schema:name": "Digestion Duration",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "HCl-HNO3 attack: 48 h; re-dissolution: N \u2014 \u00a72.3.1"
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
            "schema:defaultValue": 3,
            "schema:description": "HCl-HNO3 attack: 130 \u00b0C; re-dissolution: 130 \u00b0C (evaporation) \u2014 \u00a72.3.1"
          }
        ],
        "schema:description": "HCl-HNO3 attack (1.5 ml 6 M HCl + 0.5 ml 8 M HNO3, 130 \u00b0C, 48 h); re-dissolution (evaporated at 130 \u00b0C close to dryness, then 1.5 ml 10 M HCl) \u2014 \u00a72.3.1, for magnetite and pyrite; FER-2 took 1 ml 28 M HF + 1 ml 8 M HNO3 at 130 \u00b0C for at least 48 h, then 1.5 ml 10 M HCl for 24 h",
        "bios:reagent": [
          {
            "schema:name": "HCl-HNO3 attack: 6 M HCl + 8 M HNO3; re-dissolution: 10 M HCl \u2014 \u00a72.3.1",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
  },
  "ada:samplingUnitType": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:reportedProperties": [
    "Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Ge, Rb, Sr, Y, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (\u00b5g/g) \u2014 Table 3 (FER-2) in \u00b5g g\u207b\u00b9; the unit of Table 4 (samples) is not stated in its header"
  ],
  "ada:chromatographicSeparationApplied": "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)",
  "ada:isotopeDilutionSpike": "None (external calibration used; stated section 2.3)",
  "ada:finalSolutionMatrix": "all: 2% HNO3 containing 5 ng/mL Rh \u2014 \u00a72.3.2",
  "ada:washTimeBetweenSamples": "60 s \u2014 Table 1; '1 min with 3% v/v HNO3' (\u00a72.1)",
  "ada:uncertaintyLevel": "1 standard deviation -- \"The mean values and respective standard deviations (s) for three analyses\"; \"Mean +/- s (n = 3)\"; \"RSD = standard deviation/mean x 100%\"",
  "ada:blankBackgroundCorrectionMethod": "N \u2014 a blank solution in 2% HNO3 is part of the calibration set (\u00a72.2); the blank correction is not described",
  "ada:internalStandardElement": "all: Rh (103Rh) \u2014 Table 1",
  "ada:secondaryReferenceMaterialDefault": [
    "FER-2 \u2014 iron-formation reference material (CCRMP), 'used to validate of the proposed method' (\u00a72.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-P1> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Mineral separates (~100 mg powder; stated section 2.3)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "HCl-HNO3 attack (1.5 ml 6 M HCl + 0.5 ml 8 M HNO3, 130 °C, 48 h); re-dissolution (evaporated at 130 °C close to dryness, then 1.5 ml 10 M HCl) — §2.3.1, for magnetite and pyrite; FER-2 took 1 ml 28 M HF + 1 ml 8 M HNO3 at 130 °C for at least 48 h, then 1.5 ml 10 M HCl for 24 h" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "HCl-HNO3 attack: 6 M HCl + 8 M HNO3; re-dissolution: 10 M HCl — §2.3.1" ] ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3 × SD of six procedural blanks (MDL) — Table 2 note; the IDL is 3 × SD of six replicate measurements of 2% HNO3" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only Reported detail: ada:driftCorrectionMethod = Rh internal standard — 'In order to correct the instrumental drift, the internal standard concentration of Rh was kept constant at 5 ng mL−1 in the sample, calibration, and blank solutions' (§2.2)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\"" ;
    ada:blankBackgroundCorrectionMethod "N — a blank solution in 2% HNO3 is part of the calibration set (§2.2); the blank correction is not described" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "AG1-X8 anion exchange resin + TRUspec resin (stated section 2.3.2)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 2% HNO3 containing 5 ng/mL Rh — §2.3.2" ;
    ada:internalStandardElement "all: Rh (103Rh) — Table 1" ;
    ada:isotopeDilutionSpike "None (external calibration used; stated section 2.3)" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Li, Be, Sc, Cr, Co, Ni, Cu, Zn, Ge, Rb, Sr, Y, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (µg/g) — Table 3 (FER-2) in µg g⁻¹; the unit of Table 4 (samples) is not stated in its header" ;
    ada:samplingUnitType "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"" ;
    ada:secondaryReferenceMaterialDefault "FER-2 — iron-formation reference material (CCRMP), 'used to validate of the proposed method' (§2.2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "magnetite",
                "pyrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ba",
                "Be",
                "Ce",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Gd",
                "Ge",
                "Ho",
                "La",
                "Li",
                "Lu",
                "Nd",
                "Ni",
                "Pr",
                "Rb",
                "Sc",
                "Sm",
                "Sr",
                "Tb",
                "Tm",
                "Y",
                "Yb",
                "Zn" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "1 standard deviation -- \"The mean values and respective standard deviations (s) for three analyses\"; \"Mean +/- s (n = 3)\"; \"RSD = standard deviation/mean x 100%\"" ;
    ada:washTimeBetweenSamples "60 s — Table 1; '1 min with 3% v/v HNO3' (§2.1)" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Element I HR-ICP-MS (stated Table 1)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9.6e-01 ;
    schema1:description "0.96 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "1.1 mm Ni sampler + 0.8 mm Ni skimmer (Table 1)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.46e+01 ;
    schema1:description "14.6 L/min (Table 1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "60 s wash between samples (Table 1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1300 W (Table 1)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1300 ;
    schema1:description "1300 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni sampler and Ni skimmer (Table 1)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Counting — Table 1 'Detection mode'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "HCl-HNO3 attack: 48 h; re-dissolution: N — §2.3.1" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "HCl-HNO3 attack: 130 °C; re-dissolution: 130 °C (evaporation) — §2.3.1" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b) Reported detail: ada:driftCorrectionMethod = Standard solution every two samples — 'No time drift of fTi was observed during measurements over 2 h, thus all fTi were averaged and used' (§2.7).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Ti"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — plasma power 1.1 kW (Table 1b)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Pulse counting mode — §2.1.2"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample — §2.1.2"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "peridotite",
      "carbonaceous chondrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N — Ti is determined by internal standardisation, not isotope dilution"
          }
        ],
        "ada:detectionLimitMethod": "all: 3σ — Table 2b",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFM bomb (TFM-981; stated section 2.1.1)"
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
            "schema:defaultValue": 70,
            "schema:description": "ultrasonic HF decomposition: <70 °C; bomb HF decomposition: 245 °C; re-dissolution: N — abstract"
          }
        ],
        "schema:description": "ultrasonic HF decomposition (basalts and andesites, <70 °C); bomb HF decomposition (peridotites and meteorites, 30 mol/l HF, 245 °C, mannitol added); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) — abstract; §2.5",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF decomposition: HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF — §2.5",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:numberOfScansPerReplicate": "all: 30 scans in 50 s — Table 1b 'Middle resolution 50 s with 30 scans (continuous nebulization)'",
  "ada:analysisSequenceDefault": "Standard solution every two samples; each sample measurement ~6 min, including ~3 min washing — §2.1.2",
  "ada:driftCorrectionMethod": "N/A",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti — abstract; §2.7"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
  ],
  "ada:reportedProperties": [
    "Ti (µg/g); TiO2 — Ti by ICP-SFMS; Nb is from the ICP-QMS. Detection limits in solution (ng/g) and in rock (µg/g) in Table 2b"
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)",
  "ada:isotopeDilutionSpike": "N — Ti is not spiked; the Zr–Hf and Mo–Sn–Sb spikes serve the ICP-QMS elements",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HF with mannitol, diluted — 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (§2.5)",
  "ada:washTimeBetweenSamples": "~3 min with 0.5 mol/l HF — §2.1.2; Table 1b: background measured before each sample 'after 200 s wash'",
  "ada:uncertaintyLevel": "RSD% with observed ranges in parentheses",
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.2)",
  "ada:blankBackgroundCorrectionMethod": "Background measured before each sample after a 200 s wash — Table 1b",
  "ada:internalStandardElement": "all: Nb (93Nb) — §2.1.2",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — GSJ and USGS silicate reference materials (§2.3); the chondrites are samples"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
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
  "schema:description": "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b) Reported detail: ada:driftCorrectionMethod = Standard solution every two samples \u2014 'No time drift of fTi was observed during measurements over 2 h, thus all fTi were averaged and used' (\u00a72.7).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Ti"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 plasma power 1.1 kW (Table 1b)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
            "Interface Cone",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Pulse counting mode \u2014 \u00a72.1.2"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample \u2014 \u00a72.1.2"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "peridotite",
      "carbonaceous chondrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N \u2014 Ti is determined by internal standardisation, not isotope dilution"
          }
        ],
        "ada:detectionLimitMethod": "all: 3\u03c3 \u2014 Table 2b",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFM bomb (TFM-981; stated section 2.1.1)"
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
            "schema:defaultValue": 70,
            "schema:description": "ultrasonic HF decomposition: <70 \u00b0C; bomb HF decomposition: 245 \u00b0C; re-dissolution: N \u2014 abstract"
          }
        ],
        "schema:description": "ultrasonic HF decomposition (basalts and andesites, <70 \u00b0C); bomb HF decomposition (peridotites and meteorites, 30 mol/l HF, 245 \u00b0C, mannitol added); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) \u2014 abstract; \u00a72.5",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF decomposition: HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF \u2014 \u00a72.5",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:numberOfScansPerReplicate": "all: 30 scans in 50 s \u2014 Table 1b 'Middle resolution 50 s with 30 scans (continuous nebulization)'",
  "ada:analysisSequenceDefault": "Standard solution every two samples; each sample measurement ~6 min, including ~3 min washing \u2014 \u00a72.1.2",
  "ada:driftCorrectionMethod": "N/A",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti \u2014 abstract; \u00a72.7"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
  ],
  "ada:reportedProperties": [
    "Ti (\u00b5g/g); TiO2 \u2014 Ti by ICP-SFMS; Nb is from the ICP-QMS. Detection limits in solution (ng/g) and in rock (\u00b5g/g) in Table 2b"
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)",
  "ada:isotopeDilutionSpike": "N \u2014 Ti is not spiked; the Zr\u2013Hf and Mo\u2013Sn\u2013Sb spikes serve the ICP-QMS elements",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HF with mannitol, diluted \u2014 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (\u00a72.5)",
  "ada:washTimeBetweenSamples": "~3 min with 0.5 mol/l HF \u2014 \u00a72.1.2; Table 1b: background measured before each sample 'after 200 s wash'",
  "ada:uncertaintyLevel": "RSD% with observed ranges in parentheses",
  "ada:calibrationMeasurementFrequency": "Every two samples (stated section 2.1.2)",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% (stated section 2.1.2)",
  "ada:blankBackgroundCorrectionMethod": "Background measured before each sample after a 200 s wash \u2014 Table 1b",
  "ada:internalStandardElement": "all: Nb (93Nb) \u2014 \u00a72.1.2",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 \u2014 GSJ and USGS silicate reference materials (\u00a72.3); the chondrites are samples"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-P2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "ultrasonic HF decomposition (basalts and andesites, <70 °C); bomb HF decomposition (peridotites and meteorites, 30 mol/l HF, 245 °C, mannitol added); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) — abstract; §2.5" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "ultrasonic HF decomposition: HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF — §2.5" ] ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3σ — Table 2b" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b) Reported detail: ada:driftCorrectionMethod = Standard solution every two samples — 'No time drift of fTi was observed during measurements over 2 h, thus all fTi were averaged and used' (§2.7)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti — abstract; §2.7" ;
                    schema1:name "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard solution every two samples; each sample measurement ~6 min, including ~3 min washing — §2.1.2" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\"" ;
    ada:blankBackgroundCorrectionMethod "Background measured before each sample after a 200 s wash — Table 1b" ;
    ada:calibrationMeasurementFrequency "Every two samples (stated section 2.1.2)" ;
    ada:chromatographicSeparationApplied "None (direct analysis of 0.5 mol/l HF solution; stated section 2.1.2)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 0.5 mol/l HF with mannitol, diluted — 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (§2.5)" ;
    ada:internalStandardElement "all: Nb (93Nb) — §2.1.2" ;
    ada:isotopeDilutionSpike "N — Ti is not spiked; the Zr–Hf and Mo–Sn–Sb spikes serve the ICP-QMS elements" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate "all: 30 scans in 50 s — Table 1b 'Middle resolution 50 s with 30 scans (continuous nebulization)'" ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 1% (stated section 2.1.2)" ;
    ada:reportedProperties "Ti (µg/g); TiO2 — Ti by ICP-SFMS; Nb is from the ICP-QMS. Detection limits in solution (ng/g) and in rock (µg/g) in Table 2b" ;
    ada:samplingUnitType "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites" ;
    ada:secondaryReferenceMaterialDefault "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — GSJ and USGS silicate reference materials (§2.3); the chondrites are samples" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "andesite",
                "basalt",
                "carbonaceous chondrite",
                "peridotite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD% with observed ranges in parentheses" ;
    ada:washTimeBetweenSamples "~3 min with 0.5 mol/l HF — §2.1.2; Table 1b: background measured before each sample 'after 200 s wash'" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Finnigan ELEMENT sector-field ICP-MS (stated section 2.1.2)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "Quartz glass torch with sapphire injector (stated Table in section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "1 mm Ni sampler + 0.8 mm Ni skimmer (stated Table in section 2.1.2)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 14 ;
    schema1:description "14 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N — Ti is determined by internal standardisation, not isotope dilution" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "MR (M/Delta-m = 3000; stated section 2.1.2)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample — §2.1.2" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — plasma power 1.1 kW (Table 1b)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.1e+00 ;
    schema1:description "1.1 kW (stated Table in section 2.1.2)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni sampler and Ni skimmer (stated Table in section 2.1.2)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Pulse counting mode — §2.1.2" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 70 ;
    schema1:description "ultrasonic HF decomposition: <70 °C; bomb HF decomposition: 245 °C; re-dissolution: N — abstract" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (§2.2–2.3) Reported detail: ada:driftCorrectionMethod = Elution acid, an enriched-isotope standard and a natural-abundance commercial standard measured every 10–12 samples — 'to assess instrument drift and mass bias' (§2.4).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Cd",
      "Pb"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 13,
              "schema:description": "13 L/min (Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — incident RF power 1300 W (Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Open-ocean seawater"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Standard isotope dilution equation (de Jong et al.), with a per-element mass-bias factor applied to the sample isotope ratios — §2.5"
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
        "ada:detectionLimitMethod": "all: 3 SD of the reagent blank — Table 5, for a 12 mL sample",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no digestion vessel; seawater pre-concentration"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "N/A — seawater; pre-concentration by chelation; no acid digestion",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4,
        "schema:description": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
  },
  "ada:samplingUnitType": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:reportedProperties": [
    "Mn, Fe, Co, Ni, Cu, Zn, Cd, Pb (nM, dissolved) — dissolved concentrations in seawater"
  ],
  "ada:chromatographicSeparationApplied": "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)",
  "ada:isotopeDilutionSpike": "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)",
  "ada:finalSolutionMatrix": "all: 1.0 M HNO3 — 'extracted trace elements were eluted with 1 mL of 1.0 M Q-HNO3' (§2.2)",
  "ada:uncertaintyLevel": "Mixed and each stated: \"Mean blank +/- 1 S.D. (pmoles)\"; \"The precision is calculated as the percent relative standard deviation (%RSD) (n = 3)\" [Table 4 footnote]; \"95% confidence limit\"",
  "ada:oxideProductionMethodAndThreshold": "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)",
  "ada:blankBackgroundCorrectionMethod": "All sample concentrations corrected for the ammonium acetate buffer and the extraction procedure (flow manifold, chelating resin, elution acid), which includes the ICP-MS background — §2.5",
  "ada:internalStandardElement": "all: none — isotope dilution for Fe, Ni, Cu, Zn, Cd and Pb, standard additions for Co and Mn (§2.5)",
  "ada:secondaryReferenceMaterialDefault": [
    "NASS-5; SAFe S1; SAFe D2 — NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (§2.6)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
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
  "schema:description": "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (\u00a72.2\u20132.3) Reported detail: ada:driftCorrectionMethod = Elution acid, an enriched-isotope standard and a natural-abundance commercial standard measured every 10\u201312 samples \u2014 'to assess instrument drift and mass bias' (\u00a72.4).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Cd",
      "Pb"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 13,
              "schema:description": "13 L/min (Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 incident RF power 1300 W (Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Open-ocean seawater"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:description": "missing",
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Standard isotope dilution equation (de Jong et al.), with a per-element mass-bias factor applied to the sample isotope ratios \u2014 \u00a72.5"
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
        "ada:detectionLimitMethod": "all: 3 SD of the reagent blank \u2014 Table 5, for a 12 mL sample",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no digestion vessel; seawater pre-concentration"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "N/A \u2014 seawater; pre-concentration by chelation; no acid digestion",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4,
        "schema:description": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
  },
  "ada:samplingUnitType": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:reportedProperties": [
    "Mn, Fe, Co, Ni, Cu, Zn, Cd, Pb (nM, dissolved) \u2014 dissolved concentrations in seawater"
  ],
  "ada:chromatographicSeparationApplied": "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)",
  "ada:isotopeDilutionSpike": "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)",
  "ada:finalSolutionMatrix": "all: 1.0 M HNO3 \u2014 'extracted trace elements were eluted with 1 mL of 1.0 M Q-HNO3' (\u00a72.2)",
  "ada:uncertaintyLevel": "Mixed and each stated: \"Mean blank +/- 1 S.D. (pmoles)\"; \"The precision is calculated as the percent relative standard deviation (%RSD) (n = 3)\" [Table 4 footnote]; \"95% confidence limit\"",
  "ada:oxideProductionMethodAndThreshold": "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)",
  "ada:blankBackgroundCorrectionMethod": "All sample concentrations corrected for the ammonium acetate buffer and the extraction procedure (flow manifold, chelating resin, elution acid), which includes the ICP-MS background \u2014 \u00a72.5",
  "ada:internalStandardElement": "all: none \u2014 isotope dilution for Fe, Ni, Cu, Zn, Cd and Pb, standard additions for Co and Mn (\u00a72.5)",
  "ada:secondaryReferenceMaterialDefault": [
    "NASS-5; SAFe S1; SAFe D2 \u2014 NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (\u00a72.6)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:numberOfScansPerReplicate": -9999,
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-P3> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3 SD of the reagent blank — Table 5, for a 12 mL sample" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N/A — seawater; pre-concentration by chelation; no acid digestion" ] ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (§2.2–2.3) Reported detail: ada:driftCorrectionMethod = Elution acid, an enriched-isotope standard and a natural-abundance commercial standard measured every 10–12 samples — 'to assess instrument drift and mass bias' (§2.4)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\"" ;
    ada:blankBackgroundCorrectionMethod "All sample concentrations corrected for the ammonium acetate buffer and the extraction procedure (flow manifold, chelating resin, elution acid), which includes the ICP-MS background — §2.5" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Toyopearl AF-Chelate-650M chelating resin (pre-concentration from seawater; stated section 2.2)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 1.0 M HNO3 — 'extracted trace elements were eluted with 1 mL of 1.0 M Q-HNO3' (§2.2)" ;
    ada:internalStandardElement "all: none — isotope dilution for Fe, Ni, Cu, Zn, Cd and Pb, standard additions for Co and Mn (§2.5)" ;
    ada:isotopeDilutionSpike "57Fe, 62Ni, 65Cu, 68Zn, 111Cd, 207Pb enriched isotope spikes (stated Table 1)" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:numberOfScansPerReplicate -9999 ;
    ada:oxideProductionMethodAndThreshold "In (5 ppb) used for LR tuning; oxide rate typically <5% (stated section 2.4)" ;
    ada:reportedProperties "Mn, Fe, Co, Ni, Cu, Zn, Cd, Pb (nM, dissolved) — dissolved concentrations in seawater" ;
    ada:samplingUnitType "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"" ;
    ada:secondaryReferenceMaterialDefault "NASS-5; SAFe S1; SAFe D2 — NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (§2.6)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Open-ocean seawater" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Cd",
                "Co",
                "Cu",
                "Fe",
                "Mn",
                "Ni",
                "Pb",
                "Zn" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "Mixed and each stated: \"Mean blank +/- 1 S.D. (pmoles)\"; \"The precision is calculated as the percent relative standard deviation (%RSD) (n = 3)\" [Table 4 footnote]; \"95% confidence limit\"" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Finnigan Element I (E1) HR-ICP-MS (stated section 2.4)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.05e+00 ;
    schema1:description "1.05 L/min (varied and optimized daily; Table 2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Ni/Cu sampler (Spectron Inc.) + Ni skimmer (Spectron Inc.; Table 2)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 13 ;
    schema1:description "13 L/min (Table 2)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "Standard isotope dilution equation (de Jong et al.), with a per-element mass-bias factor applied to the sample isotope ratios — §2.5" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR (R ~300) and MR (R ~4000; stated section 2.4)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — incident RF power 1300 W (Table 2)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1300 ;
    schema1:description "1300 W (Table 2)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni/Cu sampler and Ni skimmer (Table 2)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "N/A — no digestion vessel; seawater pre-concentration" ;
    schema1:valueName "digestionVesselType" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (§2.3) Reported detail: ada:driftCorrectionMethod = N — the blocks of seven are bracketed by acid blanks and a consistency standard; at low calcium concentrations there was 'minimal instrumental sensitivity drift' (§2.3.1).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
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
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Foraminifera calcite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Handpicked 1–2 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 µL of supernatant diluted with 200 µL 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF — §2.4; the HF-bearing matrix 'was used only in the final dilution step'",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "LR; MR — low resolution (Δm/m = 300) and medium resolution (Δm/m = 4000) methods, 'Calcium was measured in both low and medium resolution to maintain accuracy of Me/Ca ratios obtained from the two mass resolution modes' (Table 3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "all: detector cross-calibration between pulse and analog modes performed daily — §2.3.1"
          },
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      },
      {
        "schema:name": "Sample digestion",
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
            "schema:value": "N/A — simple dissolution; stated section 2.4"
          }
        ],
        "schema:description": "dissolution (minimum volume of 1 M HNO3, 40–60 µL, then centrifuged 2 min at 10,000 rpm) — §2.4",
        "bios:reagent": [
          {
            "schema:name": "dissolution: 1 M HNO3 — §2.4",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Pt-normal sampler + Pt-H skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — RF power 1250 W (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Dual mode, fixed for each isotope: counting for 7Li, 11B, 111Cd, 137Ba, 238U, 55Mn, 56Fe, 66Zn and analog for 25Mg, 27Al, 43Ca, 87Sr, 23Na — Tables 1 and 3; 'measured at a fixed detection mode to avoid detection mode switch (pulse to analog) during analysis' (§2.3.1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "120 s washout (Table 1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\""
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfScansPerReplicate": "LR: 15 passes × 3 runs; MR: 5 passes × 3 runs — Table 3; Table 1 prints 3 passes for MR",
  "ada:numberOfReplicatesPerSample": "3 runs (LR and MR; Table 3)",
  "ada:analysisSequenceDefault": "Blocks of seven samples, each bracketed by a pair of acid blanks and internal consistency standards (Standard 3 of the calibration) — §2.3.1",
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "instrumentWarmUpSessionDurationLimit",
      "schema:name": "Instrument Warm up Session Duration Limit",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Partially -- \"The instrument was conditioned with a 10 [ppb solution]\" before analysis, and detector mode was \"kept fixed through the entire run to avoid detection mode switch induced changes in sensitivity\". No warm-up time or session duration limit stated"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2 — low and medium resolution (Tables 1 and 3)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
  },
  "ada:samplingUnitType": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:reportedProperties": [
    "B/Ca (µmol/mol); Li/Ca, Mg/Ca, Al/Ca, Sr/Ca, Cd/Ca, Ba/Ca, U/Ca, Na/Ca, Mn/Ca, Fe/Ca, Zn/Ca (µmol/mol or mmol/mol) — Me/Ca ratios; Li, Mg, Al, Sr, Cd, Ba and U in low resolution, Na, Mn, Fe and Zn in medium (Table 3)"
  ],
  "ada:chromatographicSeparationApplied": "None (direct dissolution analysis; stated section 2.4)",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 0.1 M HNO3 + 0.3 M HF — 'The acid matrix containing HF was used only in the final dilution step'",
  "ada:washTimeBetweenSamples": "120 s (Table 1)",
  "ada:uncertaintyLevel": "2 sigma -- \"with 2r analytical uncertainty\" and \"the gray area represents the 2r spread in the B/Ca measured at 10 ppm [Ca]Matrix\" (r = sigma in the extracted text)",
  "ada:calibrationMeasurementFrequency": "Standard 3 brackets each block of seven samples — §2.3.1",
  "ada:oxideProductionMethodAndThreshold": "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)",
  "ada:internalStandardElement": "all: none — Me/Ca ratios, with Ca measured in both resolutions",
  "ada:secondaryReferenceMaterialDefault": [
    "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix — the four Cambridge consistency standards (§2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
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
  "schema:description": "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (\u00a72.3) Reported detail: ada:driftCorrectionMethod = N \u2014 the blocks of seven are bracketed by acid blanks and a consistency standard; at low calcium concentrations there was 'minimal instrumental sensitivity drift' (\u00a72.3.1).",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
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
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Foraminifera calcite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Handpicked 1\u20132 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 \u00b5L of supernatant diluted with 200 \u00b5L 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF \u2014 \u00a72.4; the HF-bearing matrix 'was used only in the final dilution step'",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "LR; MR \u2014 low resolution (\u0394m/m = 300) and medium resolution (\u0394m/m = 4000) methods, 'Calcium was measured in both low and medium resolution to maintain accuracy of Me/Ca ratios obtained from the two mass resolution modes' (Table 3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "all: detector cross-calibration between pulse and analog modes performed daily \u2014 \u00a72.3.1"
          },
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "None"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      },
      {
        "schema:name": "Sample digestion",
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
            "schema:value": "N/A \u2014 simple dissolution; stated section 2.4"
          }
        ],
        "schema:description": "dissolution (minimum volume of 1 M HNO3, 40\u201360 \u00b5L, then centrifuged 2 min at 10,000 rpm) \u2014 \u00a72.4",
        "bios:reagent": [
          {
            "schema:name": "dissolution: 1 M HNO3 \u2014 \u00a72.4",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Pt-normal sampler + Pt-H skimmer (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 RF power 1250 W (Table 1)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Dual mode, fixed for each isotope: counting for 7Li, 11B, 111Cd, 137Ba, 238U, 55Mn, 56Fe, 66Zn and analog for 25Mg, 27Al, 43Ca, 87Sr, 23Na \u2014 Tables 1 and 3; 'measured at a fixed detection mode to avoid detection mode switch (pulse to analog) during analysis' (\u00a72.3.1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "120 s washout (Table 1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\""
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfScansPerReplicate": "LR: 15 passes \u00d7 3 runs; MR: 5 passes \u00d7 3 runs \u2014 Table 3; Table 1 prints 3 passes for MR",
  "ada:numberOfReplicatesPerSample": "3 runs (LR and MR; Table 3)",
  "ada:analysisSequenceDefault": "Blocks of seven samples, each bracketed by a pair of acid blanks and internal consistency standards (Standard 3 of the calibration) \u2014 \u00a72.3.1",
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "instrumentWarmUpSessionDurationLimit",
      "schema:name": "Instrument Warm up Session Duration Limit",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Partially -- \"The instrument was conditioned with a 10 [ppb solution]\" before analysis, and detector mode was \"kept fixed through the entire run to avoid detection mode switch induced changes in sensitivity\". No warm-up time or session duration limit stated"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2 \u2014 low and medium resolution (Tables 1 and 3)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
  },
  "ada:samplingUnitType": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:reportedProperties": [
    "B/Ca (\u00b5mol/mol); Li/Ca, Mg/Ca, Al/Ca, Sr/Ca, Cd/Ca, Ba/Ca, U/Ca, Na/Ca, Mn/Ca, Fe/Ca, Zn/Ca (\u00b5mol/mol or mmol/mol) \u2014 Me/Ca ratios; Li, Mg, Al, Sr, Cd, Ba and U in low resolution, Na, Mn, Fe and Zn in medium (Table 3)"
  ],
  "ada:chromatographicSeparationApplied": "None (direct dissolution analysis; stated section 2.4)",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 0.1 M HNO3 + 0.3 M HF \u2014 'The acid matrix containing HF was used only in the final dilution step'",
  "ada:washTimeBetweenSamples": "120 s (Table 1)",
  "ada:uncertaintyLevel": "2 sigma -- \"with 2r analytical uncertainty\" and \"the gray area represents the 2r spread in the B/Ca measured at 10 ppm [Ca]Matrix\" (r = sigma in the extracted text)",
  "ada:calibrationMeasurementFrequency": "Standard 3 brackets each block of seven samples \u2014 \u00a72.3.1",
  "ada:oxideProductionMethodAndThreshold": "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)",
  "ada:internalStandardElement": "all: none \u2014 Me/Ca ratios, with Ca measured in both resolutions",
  "ada:secondaryReferenceMaterialDefault": [
    "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix \u2014 the four Cambridge consistency standards (\u00a72.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-P4> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Handpicked 1–2 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 µL of supernatant diluted with 200 µL 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF — §2.4; the HF-bearing matrix 'was used only in the final dilution step'" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "dissolution (minimum volume of 1 M HNO3, 40–60 µL, then centrifuged 2 min at 10,000 rpm) — §2.4" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "dissolution: 1 M HNO3 — §2.4" ] ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "LR; MR — low resolution (Δm/m = 300) and medium resolution (Δm/m = 4000) methods, 'Calcium was measured in both low and medium resolution to maintain accuracy of Me/Ca ratios obtained from the two mass resolution modes' (Table 3)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> ;
    schema1:datePublished "missing" ;
    schema1:description "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (§2.3) Reported detail: ada:driftCorrectionMethod = N — the blocks of seven are bracketed by acid blanks and a consistency standard; at low calcium concentrations there was 'minimal instrumental sensitivity drift' (§2.3.1)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — P4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Blocks of seven samples, each bracketed by a pair of acid blanks and internal consistency standards (Standard 3 of the calibration) — §2.3.1" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Standard 3 brackets each block of seven samples — §2.3.1" ;
    ada:chromatographicSeparationApplied "None (direct dissolution analysis; stated section 2.4)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 0.1 M HNO3 + 0.3 M HF — 'The acid matrix containing HF was used only in the final dilution step'" ;
    ada:internalStandardElement "all: none — Me/Ca ratios, with Ca measured in both resolutions" ;
    ada:isotopeDilutionSpike "None" ;
    ada:numberOfAcquisitionPasses "2 — low and medium resolution (Tables 1 and 3)" ;
    ada:numberOfReplicatesPerSample "3 runs (LR and MR; Table 3)" ;
    ada:numberOfScansPerReplicate "LR: 15 passes × 3 runs; MR: 5 passes × 3 runs — Table 3; Table 1 prints 3 passes for MR" ;
    ada:oxideProductionMethodAndThreshold "Sensitivity criteria used (not oxide threshold): >=250000 cps/ppb for 11B; >=2500000 for 115In; >=2000000 for 175Lu (stated section 2.3.1)" ;
    ada:reportedProperties "B/Ca (µmol/mol); Li/Ca, Mg/Ca, Al/Ca, Sr/Ca, Cd/Ca, Ba/Ca, U/Ca, Na/Ca, Mn/Ca, Fe/Ca, Zn/Ca (µmol/mol or mmol/mol) — Me/Ca ratios; Li, Mg, Al, Sr, Cd, Ba and U in low resolution, Na, Mn, Fe and Zn in medium (Table 3)" ;
    ada:samplingUnitType "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"" ;
    ada:secondaryReferenceMaterialDefault "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix — the four Cambridge consistency standards (§2.2)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Foraminifera calcite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "B",
                "Ba",
                "Cd",
                "Fe",
                "Li",
                "Mg",
                "Mn",
                "Na",
                "Sr",
                "U",
                "Zn" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "2 sigma -- \"with 2r analytical uncertainty\" and \"the gray area represents the 2r spread in the B/Ca measured at 10 ppm [Ca]Matrix\" (r = sigma in the extracted text)" ;
    ada:washTimeBetweenSamples "120 s (Table 1)" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Element XR single-collector SF-ICP-MS (stated section 2.3)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Pt-normal sampler + Pt-H skimmer (Table 1)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "Partially -- \"The instrument was conditioned with a 10 [ppb solution]\" before analysis, and detector mode was \"kept fixed through the entire run to avoid detection mode switch induced changes in sensitivity\". No warm-up time or session duration limit stated" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR and MR (stated Table 1 and section 2.3)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "120 s washout (Table 1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1250 W (Table 1)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1250 ;
    schema1:description "1250 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Pt sampler and Pt skimmer (Table 1)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Dual mode, fixed for each isotope: counting for 7Li, 11B, 111Cd, 137Ba, 238U, 55Mn, 56Fe, 66Zn and analog for 25Mg, 27Al, 43Ca, 87Sr, 23Na — Tables 1 and 3; 'measured at a fixed detection mode to avoid detection mode switch (pulse to analog) during analysis' (§2.3.1)" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: detector cross-calibration between pulse and analog modes performed daily — §2.3.1" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "N/A — simple dissolution; stated section 2.4" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "ESI 50 uL microconcentric nebulizer; self-aspirating (Table 1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90% Reported detail: ada:driftCorrectionMethod = N — 'Instrumental drift of SF-ICP-MS has only a negligible effect on the reproducibility of ID determined concentrations since isotope ratios are used'.",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Rb",
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
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — RF power 1235 W (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "granite",
      "rhyolite",
      "shale",
      "peridotite",
      "synthetic glass"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1–3), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution — cleanroom, twice sub-boiled acids (Samples and sample preparation)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "LR; HR — two solutions of different dilution: dilution factor ~21000 for LR and ~1000 for HR; 'the transmission decreases by a factor of about 100 from the LR to the HR mode'",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Eq. 1 for the ID elements and Eq. 2 for the RSF elements, from mass-fractionation- and background-corrected mean ratios, with R_ik in Eq. 2 corrected for the spike contribution to isotope k"
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
        "ada:detectionLimitMethod": "all: 3 s of total procedural blanks including spiking, 50 measurements in LR and 20 in HR — Limits of detection",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Closed 15 ml Savillex PFA vials, placed in Parr bombs for samples with refractory minerals"
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
            "schema:defaultValue": "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N"
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
            "schema:defaultValue": 3,
            "schema:description": "hotplate HF-HNO3: 130 °C; bomb HF-HNO3: 180 °C; fluoride removal: ca. 80 °C (evaporation); chloride conversion: 80 °C, then 50 °C (evaporation); final uptake: N"
          }
        ],
        "schema:description": "hotplate HF-HNO3 (non-refractory samples of basaltic composition, 12 h at 130 °C in closed 15 ml Savillex PFA vials); bomb HF-HNO3 (samples with refractory minerals such as granites, stirred 7 days at 180 °C in Parr bombs, reopened after 3 days and refilled with 0.5 ml HF); fluoride removal (re-dissolved in a few drops of 14 mol/l HNO3 and evaporated to incipient dryness, repeated twice); chloride conversion (2 ml 6 mol/l HCl heated at 80 °C, then evaporated at 50 °C); final uptake (5 ml 7 mol/l HNO3) — Samples and sample preparation",
        "bios:reagent": [
          {
            "schema:name": "hotplate HF-HNO3: 1–2 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l); bomb HF-HNO3: 1–2 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l), and 0.5 ml HF after 3 days; fluoride removal: 14 mol/l HNO3; chloride conversion: 6 mol/l HCl; final uptake: 7 mol/l HNO3",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:numberOfScansPerReplicate": "all: 70 to 120 scans of the whole mass spectrum — for one analysis, a total acquisition time of 10 minutes per sample",
  "ada:numberOfReplicatesPerSample": "3 — 'Triplicate determinations were performed for each digestion'",
  "ada:analysisSequenceDefault": "N — a total of ca. 20 minutes per sample 'including the measurement of blank, standard solution, washout'; the order is not stated",
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
          "schema:description": "About 100 mg of whole-rock powder"
        }
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "filteringApproachDefault",
      "schema:name": "Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2 — the LR and HR solutions",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
  },
  "ada:samplingUnitType": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:reportedProperties": [
    "Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (µg/g) — Equations 1 and 2"
  ],
  "ada:chromatographicSeparationApplied": "None — 'dissolved rock samples are analysed directly by ID without previous separation'",
  "ada:isotopeDilutionSpike": "Three multi-element spikes: MES 1 (86Sr, 135Ba, 145Nd, 149Sm, 235U), MES 2 (155Gd, 161Dy, 167Er, 171Yb, 207Pb), MES 3 (91Zr, 179Hf) — Table 1; calibrated by reverse ID against Alfa Aesar specpure solutions, spike-concentration uncertainty 0.5–1% RSD",
  "ada:finalSolutionMatrix": "LR: 0.4 mol/l HNO3, about 120 µl of the uptake solution diluted to 50 ml (dilution factor ~21000); HR: 0.4 mol/l HNO3, 2.5 ml of the uptake solution diluted with H2O to 50 ml (dilution factor ~1000) — ca. 6 µl of a Ru-Re solution (60 µg/g Ru, 20 µg/g Re) added to each dilution",
  "ada:uncertaintyLevel": "RSD for repeatability of triplicate determinations; \"confidence intervals (1s)\"; the method result is quoted as a \"combined standard uncertainty\"",
  "ada:calibrationMeasurementFrequency": "Standard solution once per analytical run (e.g. once per day) — RSF values constant within 1s over at least ten hours",
  "ada:blankBackgroundCorrectionMethod": "N — 'After correction for background and mass fractionation'; the method is not described",
  "ada:internalStandardElement": "all: the ID-determined elements, for the RSF elements (Table 1 ratios, e.g. 93Nb/90Zr, 175Lu/172Yb) — Ru and Re are added for the mass-fractionation correction, not as internal standards",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90% Reported detail: ada:driftCorrectionMethod = N \u2014 'Instrumental drift of SF-ICP-MS has only a negligible effect on the reproducibility of ID determined concentrations since isotope ratios are used'.",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Rb",
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
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 RF power 1235 W (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)"
            },
            {
              "@id": "ada:parameter/module/ICPMS/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "samplerAndSkimmerConeMaterial",
              "schema:name": "Sampler and Skimmer Cone Material",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "granite",
      "rhyolite",
      "shale",
      "peridotite",
      "synthetic glass"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1\u20133), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution \u2014 cleanroom, twice sub-boiled acids (Samples and sample preparation)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "LR; HR \u2014 two solutions of different dilution: dilution factor ~21000 for LR and ~1000 for HR; 'the transmission decreases by a factor of about 100 from the LR to the HR mode'",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "schema:additionalProperty": []
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/ICPMS/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "isotopeDilutionDataReductionMethod",
            "schema:name": "Isotope Dilution Data Reduction Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Eq. 1 for the ID elements and Eq. 2 for the RSF elements, from mass-fractionation- and background-corrected mean ratios, with R_ik in Eq. 2 corrected for the spike contribution to isotope k"
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
        "ada:detectionLimitMethod": "all: 3 s of total procedural blanks including spiking, 50 measurements in LR and 20 in HR \u2014 Limits of detection",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Closed 15 ml Savillex PFA vials, placed in Parr bombs for samples with refractory minerals"
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
            "schema:defaultValue": "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N"
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
            "schema:defaultValue": 3,
            "schema:description": "hotplate HF-HNO3: 130 \u00b0C; bomb HF-HNO3: 180 \u00b0C; fluoride removal: ca. 80 \u00b0C (evaporation); chloride conversion: 80 \u00b0C, then 50 \u00b0C (evaporation); final uptake: N"
          }
        ],
        "schema:description": "hotplate HF-HNO3 (non-refractory samples of basaltic composition, 12 h at 130 \u00b0C in closed 15 ml Savillex PFA vials); bomb HF-HNO3 (samples with refractory minerals such as granites, stirred 7 days at 180 \u00b0C in Parr bombs, reopened after 3 days and refilled with 0.5 ml HF); fluoride removal (re-dissolved in a few drops of 14 mol/l HNO3 and evaporated to incipient dryness, repeated twice); chloride conversion (2 ml 6 mol/l HCl heated at 80 \u00b0C, then evaporated at 50 \u00b0C); final uptake (5 ml 7 mol/l HNO3) \u2014 Samples and sample preparation",
        "bios:reagent": [
          {
            "schema:name": "hotplate HF-HNO3: 1\u20132 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l); bomb HF-HNO3: 1\u20132 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l), and 0.5 ml HF after 3 days; fluoride removal: 14 mol/l HNO3; chloride conversion: 6 mol/l HCl; final uptake: 7 mol/l HNO3",
            "@type": [
              "schema:DefinedTerm"
            ]
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
  "ada:numberOfScansPerReplicate": "all: 70 to 120 scans of the whole mass spectrum \u2014 for one analysis, a total acquisition time of 10 minutes per sample",
  "ada:numberOfReplicatesPerSample": "3 \u2014 'Triplicate determinations were performed for each digestion'",
  "ada:analysisSequenceDefault": "N \u2014 a total of ca. 20 minutes per sample 'including the measurement of blank, standard solution, washout'; the order is not stated",
  "ada:driftCorrectionMethod": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
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
          "schema:description": "About 100 mg of whole-rock powder"
        }
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "filteringApproachDefault",
      "schema:name": "Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Dixon outlier test on each block of ten ratios \u2014 'Generally, less than one ratio had to be excluded from the whole data set'"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2 \u2014 the LR and HR solutions",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution SF-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
  },
  "ada:samplingUnitType": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:reportedProperties": [
    "Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (\u00b5g/g) \u2014 Equations 1 and 2"
  ],
  "ada:chromatographicSeparationApplied": "None \u2014 'dissolved rock samples are analysed directly by ID without previous separation'",
  "ada:isotopeDilutionSpike": "Three multi-element spikes: MES 1 (86Sr, 135Ba, 145Nd, 149Sm, 235U), MES 2 (155Gd, 161Dy, 167Er, 171Yb, 207Pb), MES 3 (91Zr, 179Hf) \u2014 Table 1; calibrated by reverse ID against Alfa Aesar specpure solutions, spike-concentration uncertainty 0.5\u20131% RSD",
  "ada:finalSolutionMatrix": "LR: 0.4 mol/l HNO3, about 120 \u00b5l of the uptake solution diluted to 50 ml (dilution factor ~21000); HR: 0.4 mol/l HNO3, 2.5 ml of the uptake solution diluted with H2O to 50 ml (dilution factor ~1000) \u2014 ca. 6 \u00b5l of a Ru-Re solution (60 \u00b5g/g Ru, 20 \u00b5g/g Re) added to each dilution",
  "ada:uncertaintyLevel": "RSD for repeatability of triplicate determinations; \"confidence intervals (1s)\"; the method result is quoted as a \"combined standard uncertainty\"",
  "ada:calibrationMeasurementFrequency": "Standard solution once per analytical run (e.g. once per day) \u2014 RSF values constant within 1s over at least ten hours",
  "ada:blankBackgroundCorrectionMethod": "N \u2014 'After correction for background and mass fractionation'; the method is not described",
  "ada:internalStandardElement": "all: the ID-determined elements, for the RSF elements (Table 1 ratios, e.g. 93Nb/90Zr, 175Lu/172Yb) \u2014 Ru and Re are added for the mass-fractionation correction, not as internal standards",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:oxideProductionMethodAndThreshold": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionSficpmsTAPP-Willbold2005> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "hotplate HF-HNO3 (non-refractory samples of basaltic composition, 12 h at 130 °C in closed 15 ml Savillex PFA vials); bomb HF-HNO3 (samples with refractory minerals such as granites, stirred 7 days at 180 °C in Parr bombs, reopened after 3 days and refilled with 0.5 ml HF); fluoride removal (re-dissolved in a few drops of 14 mol/l HNO3 and evaporated to incipient dryness, repeated twice); chloride conversion (2 ml 6 mol/l HCl heated at 80 °C, then evaporated at 50 °C); final uptake (5 ml 7 mol/l HNO3) — Samples and sample preparation" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "hotplate HF-HNO3: 1–2 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l); bomb HF-HNO3: 1–2 ml HF (24 mol/l) + 0.2 ml HNO3 (14 mol/l), and 0.5 ml HF after 3 days; fluoride removal: 14 mol/l HNO3; chloride conversion: 6 mol/l HCl; final uptake: 7 mol/l HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3 s of total procedural blanks including spiking, 50 measurements in LR and 20 in HR — Limits of detection" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1–3), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution — cleanroom, twice sub-boiled acids (Samples and sample preparation)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "LR; HR — two solutions of different dilution: dilution factor ~21000 for LR and ~1000 for HR; 'the transmission decreases by a factor of about 100 from the LR to the HR mode'" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90% Reported detail: ada:driftCorrectionMethod = N — 'Instrumental drift of SF-ICP-MS has only a negligible effect on the reproducibility of ID determined concentrations since isotope ratios are used'." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution SF-ICP-MS" ] ;
    schema1:name "solutionSficpms protocol — Willbold2005" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "N — a total of ca. 20 minutes per sample 'including the measurement of blank, standard solution, washout'; the order is not stated" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\"" ;
    ada:blankBackgroundCorrectionMethod "N — 'After correction for background and mass fractionation'; the method is not described" ;
    ada:calibrationMeasurementFrequency "Standard solution once per analytical run (e.g. once per day) — RSF values constant within 1s over at least ten hours" ;
    ada:chromatographicSeparationApplied "None — 'dissolved rock samples are analysed directly by ID without previous separation'" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "LR: 0.4 mol/l HNO3, about 120 µl of the uptake solution diluted to 50 ml (dilution factor ~21000); HR: 0.4 mol/l HNO3, 2.5 ml of the uptake solution diluted with H2O to 50 ml (dilution factor ~1000) — ca. 6 µl of a Ru-Re solution (60 µg/g Ru, 20 µg/g Re) added to each dilution" ;
    ada:internalStandardElement "all: the ID-determined elements, for the RSF elements (Table 1 ratios, e.g. 93Nb/90Zr, 175Lu/172Yb) — Ru and Re are added for the mass-fractionation correction, not as internal standards" ;
    ada:isotopeDilutionSpike "Three multi-element spikes: MES 1 (86Sr, 135Ba, 145Nd, 149Sm, 235U), MES 2 (155Gd, 161Dy, 167Er, 171Yb, 207Pb), MES 3 (91Zr, 179Hf) — Table 1; calibrated by reverse ID against Alfa Aesar specpure solutions, spike-concentration uncertainty 0.5–1% RSD" ;
    ada:numberOfAcquisitionPasses "2 — the LR and HR solutions" ;
    ada:numberOfReplicatesPerSample "3 — 'Triplicate determinations were performed for each digestion'" ;
    ada:numberOfScansPerReplicate "all: 70 to 120 scans of the whole mass spectrum — for one analysis, a total acquisition time of 10 minutes per sample" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (µg/g) — Equations 1 and 2" ;
    ada:samplingUnitType "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"" ;
    ada:secondaryReferenceMaterialDefault "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "andesite",
                "basalt",
                "granite",
                "peridotite",
                "rhyolite",
                "shale",
                "synthetic glass" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ba",
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
                "Rb",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Tm",
                "U",
                "Y",
                "Yb",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD for repeatability of triplicate determinations; \"confidence intervals (1s)\"; the method result is quoted as a \"combined standard uncertainty\"" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ThermoFinnigan ELEMENT2 (stated section on instrumentation)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\"" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.9 L/min (Table 3)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "1.0 mm Ni sampler + 0.5 mm Ni skimmer (Table 3)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (Table 3)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "Eq. 1 for the ID elements and Eq. 2 for the RSF elements, from mass-fractionation- and background-corrected mean ratios, with R_ik in Eq. 2 corrected for the spike contribution to isotope k" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1235 W (Table 3)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1235 ;
    schema1:description "1235 W (Table 3)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni sampler and Ni skimmer (Table 3)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "hotplate HF-HNO3: 130 °C; bomb HF-HNO3: 180 °C; fluoride removal: ca. 80 °C (evaporation); chloride conversion: 80 °C, then 50 °C (evaporation); final uptake: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Closed 15 ml Savillex PFA vials, placed in Parr bombs for samples with refractory minerals" ;
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
    schema1:description "About 100 mg of whole-rock powder" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution SF-ICP-MS Technique-Aligned Protocol Profile (solutionSficpmsTAPP)
description: Solution sector-field (high-resolution) ICP-MS extension of the base
  TAPP definition, generated from tapp/Current TAPPs/Solution_SF-ICP-MS_TAPP_v89.csv
  via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    ada:targetSpeciesTemplate:
      type: object
      properties:
        ada:defaultTargetSpecies:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
        ada:targetSpeciesColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetSpeciesIdentifierColumn
            - title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the target species element they serve where they serve one. Covers
                atomic isotopes and, where a reaction cell shifts an target species
                onto a different mass, the product mass actually measured. Includes
                interference-monitor and internal-standard masses, which serve no
                target species and so have no parent element. The target species list
                is given by the Target Species field and is never inferred from the
                element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses
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
            - title: Dwell Time per Mass
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass
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
            - title: Calibration Strategy per Target Species
              description: Approach used to convert measured ion signals to reported
                concentrations, and specifically any case where different target species
                or target species groups within one procedure are calibrated differently
                - different primary standards for different mass ranges or phases,
                or one element serving as internal standard while others are externally
                calibrated. Where a single strategy applies to all target species,
                record that strategy. Where the procedure reports isotope ratios only
                and no concentrations, record 'Not applicable (isotope ratios only)'.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: calibrationStrategyPerTargetSpecies
                schema:name:
                  const: Calibration Strategy per Target Species
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
            - title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: spectralInterferenceCorrectionsApplied
                schema:name:
                  const: Spectral Interference Corrections Applied
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
              description: The isobaric, polyatomic and doubly charged species that
                overlap the measured masses and are corrected in data reduction -
                direct isobars, oxides and argides, hydrides, and abundance-sensitivity
                tailing from an adjacent large beam. Name each species and the mass
                it affects.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                reported."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
              description: Offset between measured and accepted values for secondary
                reference materials, and the method used to assess it. Specify the
                reference material and the source of its accepted values, the number
                of analyses, and the quantities assessed. Report systematic biases
                and their likely causes. Express the offset in the form appropriate
                to what the procedure reports - percent relative bias for concentrations,
                or deviation in delta or ratio units for isotopic quantities.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
            - title: Counting Statistics Error
              description: "Uncertainty predicted from counting statistics \u2014
                the theoretical limit set by the Poisson distribution of the counts
                accumulated \u2014 for each reported quantity per analysis, with the
                sigma level stated. Derived from the counts on the target species
                together with those on any background or blank subtracted from it.
                Distinct from the scatter actually observed within a measurement or
                between repeated measurements, which is recorded separately."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: countingStatisticsError
                schema:name:
                  const: Counting Statistics Error
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
            - title: Internal (Within-Measurement) Analytical Precision and Assessment
                Method
              description: Precision of a single measurement, derived from the scatter
                of the cycles, sweeps or integrations that make it up, together with
                the method used to assess it. State the statistic (2SE, 2SD, 1s RSD),
                the number of cycles it is computed over, and the reported quantity
                it applies to. Distinct from Counting Statistics Error, which records
                the uncertainty predicted from the counts rather than the scatter
                observed; where a procedure reports both, record the observed value
                here and the predicted value there.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: internalAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Internal (Within-Measurement) Analytical Precision and Assessment
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
          allOf:
          - contains:
              title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the target species element they serve where they serve one. Covers
                atomic isotopes and, where a reaction cell shifts an target species
                onto a different mass, the product mass actually measured. Includes
                interference-monitor and internal-standard masses, which serve no
                target species and so have no parent element. The target species list
                is given by the Target Species field and is never inferred from the
                element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/monitoredMasses
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
              title: Dwell Time per Mass
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/dwellTimePerMass
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
              title: Calibration Strategy per Target Species
              description: Approach used to convert measured ion signals to reported
                concentrations, and specifically any case where different target species
                or target species groups within one procedure are calibrated differently
                - different primary standards for different mass ranges or phases,
                or one element serving as internal standard while others are externally
                calibrated. Where a single strategy applies to all target species,
                record that strategy. Where the procedure reports isotope ratios only
                and no concentrations, record 'Not applicable (isotope ratios only)'.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/calibrationStrategyPerTargetSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: calibrationStrategyPerTargetSpecies
                schema:name:
                  const: Calibration Strategy per Target Species
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
              title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/spectralInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: spectralInterferenceCorrectionsApplied
                schema:name:
                  const: Spectral Interference Corrections Applied
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
              description: The isobaric, polyatomic and doubly charged species that
                overlap the measured masses and are corrected in data reduction -
                direct isobars, oxides and argides, hydrides, and abundance-sensitivity
                tailing from an adjacent large beam. Name each species and the mass
                it affects.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/interferingSpecies
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                reported."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
              description: Offset between measured and accepted values for secondary
                reference materials, and the method used to assess it. Specify the
                reference material and the source of its accepted values, the number
                of analyses, and the quantities assessed. Report systematic biases
                and their likely causes. Express the offset in the form appropriate
                to what the procedure reports - percent relative bias for concentrations,
                or deviation in delta or ratio units for isotopic quantities.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
          - contains:
              title: Counting Statistics Error
              description: "Uncertainty predicted from counting statistics \u2014
                the theoretical limit set by the Poisson distribution of the counts
                accumulated \u2014 for each reported quantity per analysis, with the
                sigma level stated. Derived from the counts on the target species
                together with those on any background or blank subtracted from it.
                Distinct from the scatter actually observed within a measurement or
                between repeated measurements, which is recorded separately."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/countingStatisticsError
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: countingStatisticsError
                schema:name:
                  const: Counting Statistics Error
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
              title: Internal (Within-Measurement) Analytical Precision and Assessment
                Method
              description: Precision of a single measurement, derived from the scatter
                of the cycles, sweeps or integrations that make it up, together with
                the method used to assess it. State the statistic (2SE, 2SD, 1s RSD),
                the number of cycles it is computed over, and the reported quantity
                it applies to. Distinct from Counting Statistics Error, which records
                the uncertainty predicted from the counts rather than the scatter
                observed; where a procedure reports both, record the observed value
                here and the predicted value there.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: internalAnalyticalPrecisionAndAssessmentMethod
                schema:name:
                  const: Internal (Within-Measurement) Analytical Precision and Assessment
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
      required:
      - ada:defaultTargetSpecies
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_plasmaThermalMode
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_plasmaThermalMode
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_configuration
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_samplerAndSkimmerConeMaterial
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_configuration
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_samplerAndSkimmerConeMaterial
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
                        schema:additionalProperty:
                          type: array
                          items:
                            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_torchDepth
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_torchDepth
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
              schema:model:
                type: object
                properties:
                  schema:name:
                    description: Model designation of the instrument that performs
                      the measurement, including any generation or configuration suffix.
                      Conventionally written with the manufacturer name included;
                      Instrument Manufacturer records the vendor separately, as a
                      controlled value, so that procedures remain findable by vendor.
                    type: string
                    readOnly: true
                required:
                - schema:name
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
                  - title: Doubly-Charged Species Production
                    description: Measured percentage of doubly-charged ion production
                      for the monitored species at the time of instrument tuning.
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                allOf:
                - contains:
                    title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Doubly-Charged Species Production
                    description: Measured percentage of doubly-charged ion production
                      for the monitored species at the time of instrument tuning.
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                  minContains: 0
                  maxContains: 1
              schema:manufacturer:
                type: object
                properties:
                  schema:name:
                    description: Manufacturer of the instrument that performs the
                      measurement, recorded as a controlled value. Where a procedure
                      couples a sample-introduction system to an analysing instrument,
                      this records the analysing instrument. Instrument Model gives
                      the specific designation.
                    type: string
                    enum:
                    - Thermo Fisher Scientific
                    - Agilent
                    - PerkinElmer
                    - Nu Instruments
                    - Analytik Jena
                    - Shimadzu
                    - Unknown
                    - N/A
                    - None
                    - missing
                    readOnly: true
                required:
                - schema:name
            required:
            - schema:manufacturer
            - schema:model
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: ICPMS
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    ada:targetMaterialTemplate:
      type: object
      properties:
        ada:defaultTargetMaterials:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
        ada:targetMaterialColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetMaterialIdentifierColumn
            - title: Primary Calibration Standard Name
              description: "Name and reference material identifier of the primary
                reference material(s) against which the instrument is calibrated \u2014
                converting raw signal intensities to concentrations, or anchoring
                an isotope ratio as the bracketing standard or zero-delta reference.
                Give the material name, its source or supplier, and a citation for
                the accepted values used. Where calibration instead uses the vendor's
                stored library or theoretical response factors rather than measured
                reference materials \u2014 'standardless' or 'semi-quantitative' quantification
                \u2014 record that here, naming the library or model used. 'None'
                means no calibration was performed at all, which is a different answer."
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: primaryCalibrationStandardName
                schema:name:
                  const: Primary Calibration Standard Name
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
              title: Primary Calibration Standard Name
              description: "Name and reference material identifier of the primary
                reference material(s) against which the instrument is calibrated \u2014
                converting raw signal intensities to concentrations, or anchoring
                an isotope ratio as the bracketing standard or zero-delta reference.
                Give the material name, its source or supplier, and a citation for
                the accepted values used. Where calibration instead uses the vendor's
                stored library or theoretical response factors rather than measured
                reference materials \u2014 'standardless' or 'semi-quantitative' quantification
                \u2014 record that here, naming the library or model used. 'None'
                means no calibration was performed at all, which is a different answer."
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: primaryCalibrationStandardName
                schema:name:
                  const: Primary Calibration Standard Name
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
      - ada:defaultTargetMaterials
    schema:actionProcess:
      type: object
      properties:
        schema:step:
          type: array
          items:
            type: object
            allOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/WorkflowStep
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionVesselType
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
                  schema:description:
                    description: Each distinct acid digestion step applied to dissolve
                      the sample, listed in the order performed and named by its attack.
                      A step is distinct when its acid mixture, vessel, temperature
                      or duration differs from the one before; an evaporation or dry-down
                      that carries no attack of its own is part of the step it follows,
                      and an identical attack repeated on the residue is a repeat
                      of that step rather than a new one. Enumerating the steps is
                      what allows Digestion Acid(s), Digestion Temperature and Digestion
                      Duration to be recorded per step. Record N/A where the sample
                      is introduced without acid digestion.
                    anyOf:
                    - type: string
                      readOnly: true
                    - type: array
                      items:
                        type: string
                        readOnly: true
                required:
                - schema:description
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
                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_guardElectrode
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_guardElectrode
                      minContains: 0
                      maxContains: 1
                  schema:description:
                    description: "The acquisition passes the procedure is divided
                      into, named and described so that fields keyed by acquisition
                      pass can point at them. A pass is a sub-procedure: a distinct
                      traversal of the measurement with its own configuration, run
                      in sequence on the same material. State what distinguishes each
                      pass \u2014 resolution mode, cup or cell configuration, plasma
                      or introduction path, spot size \u2014 since that differs by
                      technique. Identical repeats of one configuration are replicates,
                      not passes, and belong in Number of Replicates."
                    anyOf:
                    - type: string
                      readOnly: true
                    - type: array
                      items:
                        type: string
                        readOnly: true
                required:
                - schema:description
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_pulseAnalogDetectorNonlinearityCorrection
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      - title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual results
                          contribute to a combined result, together with the outcome
                          of applying them: how many results were obtained, how many
                          were included, and on what grounds any were excluded. An
                          individual result is the value of the reported quantity
                          obtained from one acquisition: a replicate measurement of
                          the same solution or location, a spot or grain within a
                          sample, or an independently prepared aliquot or digestion,
                          whichever the procedure combines. Distinct from filtering
                          the acquired signal during data reduction (removing spikes,
                          cycles or scans, or discarding an acquisition whose signal
                          is compromised): this field records which finished results
                          enter the combined result, and on what grounds.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/analysisInclusionAndRejectionCriteriaDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: analysisInclusionAndRejectionCriteriaDefault
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_pulseAnalogDetectorNonlinearityCorrection
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual results
                          contribute to a combined result, together with the outcome
                          of applying them: how many results were obtained, how many
                          were included, and on what grounds any were excluded. An
                          individual result is the value of the reported quantity
                          obtained from one acquisition: a replicate measurement of
                          the same solution or location, a spot or grain within a
                          sample, or an independently prepared aliquot or digestion,
                          whichever the procedure combines. Distinct from filtering
                          the acquired signal during data reduction (removing spikes,
                          cycles or scans, or discarding an acquisition whose signal
                          is compromised): this field records which finished results
                          enter the combined result, and on what grounds.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionSficpmsTAPP/analysisInclusionAndRejectionCriteriaDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: analysisInclusionAndRejectionCriteriaDefault
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      minContains: 0
                      maxContains: 1
          allOf:
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
            percentage of the centre mass (%). Record 'N/A' if E-scan acquisition
            mode is not used.
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
            the results averaged (Y/N). Record 'N/A' if not applicable to the instrument.
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
      allOf:
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        minContains: 0
        maxContains: 1
      - contains:
          title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Record 'N/A' if E-scan acquisition
            mode is not used.
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
            the results averaged (Y/N). Record 'N/A' if not applicable to the instrument.
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        minContains: 0
        maxContains: 1
    ada:monitoredPropertyTemplate:
      type: object
      properties:
        ada:monitoredPropertyColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/MonitoredPropertyIdentifierColumn
            - title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionSficpmsTAPP/massResolutionAssignment
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
              title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionSficpmsTAPP/massResolutionAssignment
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
        measurements acquired per sample solution.
      anyOf:
      - type: integer
      - type: string
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
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleAliquotMassOrVolume
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleAliquotMassOrVolume
                  minContains: 0
                  maxContains: 1
    ada:numberOfAcquisitionPasses:
      description: Number of acquisition passes the procedure runs. A count of the
        passes enumerated in Acquisition Pass, recorded separately so multi-pass procedures
        are findable without parsing that field.
      anyOf:
      - type: integer
      - type: string
      readOnly: true
  required:
  - ada:numberOfScansPerReplicate
  - ada:numberOfReplicatesPerSample
  - ada:driftCorrectionMethod
  - ada:numberOfAcquisitionPasses

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
    "nxs": "https://manual.nexusformat.org/classes/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
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

