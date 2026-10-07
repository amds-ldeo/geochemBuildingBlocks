
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
  "schema:description": "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As — §3.1, §3.2, §3.3 Reported detail: ada:signalCollectionMode = Peak hopping, one point per peak — §3.1; ada:driftCorrectionMethod = Rh internal standard, and a calibration solution analysed repeatedly as a drift monitor over the run — drift minimised by flushing a rock solution for 30 min before tuning (§3.1).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "andesite",
      "basalt",
      "granite",
      "granodiorite",
      "rhyolite",
      "peridotite",
      "dunite",
      "dolerite",
      "diabase",
      "shale",
      "sandstone",
      "limestone",
      "loess",
      "graywacke"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard — clean-room conditions (§3.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "PTFE-lined stainless steel bomb (home-made; stated section 3.3)"
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
            "schema:description": "bomb attack: 190 °C; re-dissolution: 150 °C — §3.3"
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
            "schema:defaultValue": "bomb attack: 48 h; re-dissolution: overnight — §3.3"
          }
        ],
        "schema:description": "bomb attack (1 ml HNO3 + 1 ml HF, 190 °C for 48 h, then evaporated to incipient dryness and twice taken to dryness with 1 ml HNO3); re-dissolution (1.5 ml HNO3 + 2.5 ml ultra-pure water, capped, 150 °C overnight) — §3.3 numbers five operations; the evaporations carry no attack of their own",
        "bios:reagent": [
          {
            "schema:name": "bomb attack: HNO3 + HF; re-dissolution: HNO3 — §3.3",
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
          "schema:defaultValue": 50,
          "schema:description": "50 mg (stated section 3.3)"
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
        "schema:name": "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
              "schema:defaultValue": 3.1,
              "schema:description": "N — 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (§3.1)"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
            },
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
              "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
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
              "schema:value": "N — RF power 1350 W (§3.1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N — an ELAN 6100 DRC; no cell gas or cell mode is described (§3.1)",
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesMonitorDefault",
          "schema:name": "Doubly-Charged Species Monitor",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ — §3.1"
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
          "schema:defaultValue": "Ce2+/Ce+ below 2.5% — §3.1"
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
          "schema:defaultValue": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
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
          "schema:defaultValue": "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\""
        }
      ],
      "schema:manufacturer": {
        "schema:name": "PerkinElmer",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
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
      "W",
      "Tl",
      "Pb",
      "Bi",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "114Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "115In",
        "targetSpecies": "In"
      },
      {
        "monitoredProperty": "118Sn",
        "targetSpecies": "Sn"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: three sweeps per reading and three readings per replicate — §3.1",
  "ada:signalCollectionMode": "Peak hopping",
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
      "schema:value": 0.5,
      "schema:description": "0.50 ml of 1.0 µg/ml Rh in the 50 ml final solution — §3.3"
    },
    {
      "@id": "ada:parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "instrumentWarmUpSessionDurationLimit",
      "schema:name": "Instrument Warm up Session Duration Limit",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Partially -- instrument conditioning before tuning is stated: \"Drift was minimized by flushing through a rock solution for 30 min before tuning the instrument for a run\". No warm-up time after plasma ignition and no session duration limit stated"
    }
  ],
  "ada:driftCorrectionMethod": "N/A",
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
  "ada:samplingUnitType": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:reportedProperties": [
    "Li, Be, B, Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Ge, As, Rb, Sr, Y, Zr, Nb, Mo, Cd, In, Sn, Sb, Te, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Tl, Pb, Bi, Th, U (ppm) — Table 2; blanks in ppb"
  ],
  "ada:chromatographicSeparationApplied": "None — the digest is analysed directly (§3.3)",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 1.5 ml HNO3 and 2.5 ml water made up to 50 ml with ultra-pure water and 0.50 ml of 1.0 µg/ml Rh — §3.3",
  "ada:washTimeBetweenSamples": "N — 'manual analyses in which care was taken to completely wash-out B and Ta signals between samples' (§3.1)",
  "ada:uncertaintyLevel": "RSD% -- \"The RSD is the relative standard deviation in percent\"; n = 4-7 per reference material",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ and Ce2+/Ce+ below 2.5%, with the nebulizer gas flow optimised for maximum Mg, Co, Rh, Ce, Pb and U signals — §3.1",
  "ada:internalStandardElement": "all: Rh — §3.1, §3.3",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 — five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (§3.4)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
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
  "schema:description": "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As \u2014 \u00a73.1, \u00a73.2, \u00a73.3 Reported detail: ada:signalCollectionMode = Peak hopping, one point per peak \u2014 \u00a73.1; ada:driftCorrectionMethod = Rh internal standard, and a calibration solution analysed repeatedly as a drift monitor over the run \u2014 drift minimised by flushing a rock solution for 30 min before tuning (\u00a73.1).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "andesite",
      "basalt",
      "granite",
      "granodiorite",
      "rhyolite",
      "peridotite",
      "dunite",
      "dolerite",
      "diabase",
      "shale",
      "sandstone",
      "limestone",
      "loess",
      "graywacke"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard \u2014 clean-room conditions (\u00a73.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "PTFE-lined stainless steel bomb (home-made; stated section 3.3)"
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
            "schema:description": "bomb attack: 190 \u00b0C; re-dissolution: 150 \u00b0C \u2014 \u00a73.3"
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
            "schema:defaultValue": "bomb attack: 48 h; re-dissolution: overnight \u2014 \u00a73.3"
          }
        ],
        "schema:description": "bomb attack (1 ml HNO3 + 1 ml HF, 190 \u00b0C for 48 h, then evaporated to incipient dryness and twice taken to dryness with 1 ml HNO3); re-dissolution (1.5 ml HNO3 + 2.5 ml ultra-pure water, capped, 150 \u00b0C overnight) \u2014 \u00a73.3 numbers five operations; the evaporations carry no attack of their own",
        "bios:reagent": [
          {
            "schema:name": "bomb attack: HNO3 + HF; re-dissolution: HNO3 \u2014 \u00a73.3",
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
          "schema:defaultValue": 50,
          "schema:description": "50 mg (stated section 3.3)"
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
        "schema:name": "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
              "schema:defaultValue": 3.1,
              "schema:description": "N \u2014 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (\u00a73.1)"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 14,
              "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
            },
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
              "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
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
              "schema:value": "N \u2014 RF power 1350 W (\u00a73.1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N \u2014 an ELAN 6100 DRC; no cell gas or cell mode is described (\u00a73.1)",
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "doublyChargedSpeciesMonitorDefault",
          "schema:name": "Doubly-Charged Species Monitor",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Ce2+/Ce+ \u2014 \u00a73.1"
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
          "schema:defaultValue": "Ce2+/Ce+ below 2.5% \u2014 \u00a73.1"
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
          "schema:defaultValue": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
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
          "schema:defaultValue": "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\""
        }
      ],
      "schema:manufacturer": {
        "schema:name": "PerkinElmer",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
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
      "W",
      "Tl",
      "Pb",
      "Bi",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "114Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "115In",
        "targetSpecies": "In"
      },
      {
        "monitoredProperty": "118Sn",
        "targetSpecies": "Sn"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: three sweeps per reading and three readings per replicate \u2014 \u00a73.1",
  "ada:signalCollectionMode": "Peak hopping",
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
      "schema:value": 0.5,
      "schema:description": "0.50 ml of 1.0 \u00b5g/ml Rh in the 50 ml final solution \u2014 \u00a73.3"
    },
    {
      "@id": "ada:parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "instrumentWarmUpSessionDurationLimit",
      "schema:name": "Instrument Warm up Session Duration Limit",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Partially -- instrument conditioning before tuning is stated: \"Drift was minimized by flushing through a rock solution for 30 min before tuning the instrument for a run\". No warm-up time after plasma ignition and no session duration limit stated"
    }
  ],
  "ada:driftCorrectionMethod": "N/A",
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
  "ada:samplingUnitType": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:reportedProperties": [
    "Li, Be, B, Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Ge, As, Rb, Sr, Y, Zr, Nb, Mo, Cd, In, Sn, Sb, Te, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Tl, Pb, Bi, Th, U (ppm) \u2014 Table 2; blanks in ppb"
  ],
  "ada:chromatographicSeparationApplied": "None \u2014 the digest is analysed directly (\u00a73.3)",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 1.5 ml HNO3 and 2.5 ml water made up to 50 ml with ultra-pure water and 0.50 ml of 1.0 \u00b5g/ml Rh \u2014 \u00a73.3",
  "ada:washTimeBetweenSamples": "N \u2014 'manual analyses in which care was taken to completely wash-out B and Ta signals between samples' (\u00a73.1)",
  "ada:uncertaintyLevel": "RSD% -- \"The RSD is the relative standard deviation in percent\"; n = 4-7 per reference material",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ and Ce2+/Ce+ below 2.5%, with the nebulizer gas flow optimised for maximum Mg, Co, Rh, Ce, Pb and U signals \u2014 \u00a73.1",
  "ada:internalStandardElement": "all: Rh \u2014 \u00a73.1, \u00a73.3",
  "ada:secondaryReferenceMaterialDefault": [
    "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 \u2014 five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (\u00a73.4)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
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

<ex:solutionQicpmsTAPP-Gao2008> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "bomb attack (1 ml HNO3 + 1 ml HF, 190 °C for 48 h, then evaporated to incipient dryness and twice taken to dryness with 1 ml HNO3); re-dissolution (1.5 ml HNO3 + 2.5 ml ultra-pure water, capped, 150 °C overnight) — §3.3 numbers five operations; the evaporations carry no attack of their own" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "bomb attack: HNO3 + HF; re-dissolution: HNO3 — §3.3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard — clean-room conditions (§3.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As — §3.1, §3.2, §3.3 Reported detail: ada:signalCollectionMode = Peak hopping, one point per peak — §3.1; ada:driftCorrectionMethod = Rh internal standard, and a calibration solution analysed repeatedly as a drift monitor over the run — drift minimised by flushing a rock solution for 30 min before tuning (§3.1)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Gao2008" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None — the digest is analysed directly (§3.3)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 1.5 ml HNO3 and 2.5 ml water made up to 50 ml with ultra-pure water and 0.50 ml of 1.0 µg/ml Rh — §3.3" ;
    ada:internalStandardElement "all: Rh — §3.1, §3.3" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate "all: three sweeps per reading and three readings per replicate — §3.1" ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
                [ ],
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ and Ce2+/Ce+ below 2.5%, with the nebulizer gas flow optimised for maximum Mg, Co, Rh, Ce, Pb and U signals — §3.1" ;
    ada:reportedProperties "Li, Be, B, Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Ge, As, Rb, Sr, Y, Zr, Nb, Mo, Cd, In, Sn, Sb, Te, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Tl, Pb, Bi, Th, U (ppm) — Table 2; blanks in ppb" ;
    ada:samplingUnitType "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml" ;
    ada:secondaryReferenceMaterialDefault "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 — five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (§3.4)" ;
    ada:signalCollectionMode "Peak hopping" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "andesite",
                "basalt",
                "diabase",
                "dolerite",
                "dunite",
                "granite",
                "granodiorite",
                "graywacke",
                "limestone",
                "loess",
                "peridotite",
                "rhyolite",
                "sandstone",
                "shale" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "As",
                "B",
                "Ba",
                "Be",
                "Bi",
                "Cd",
                "Ce",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Ga",
                "Gd",
                "Ge",
                "Hf",
                "Ho",
                "In",
                "La",
                "Li",
                "Lu",
                "Mo",
                "Nb",
                "Nd",
                "Ni",
                "Pb",
                "Pr",
                "Rb",
                "Sb",
                "Sc",
                "Sm",
                "Sn",
                "Sr",
                "Ta",
                "Tb",
                "Te",
                "Th",
                "Tl",
                "Tm",
                "U",
                "V",
                "W",
                "Y",
                "Yb",
                "Zn",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD% -- \"The RSD is the relative standard deviation in percent\"; n = 4-7 per reference material" ;
    ada:washTimeBetweenSamples "N — 'manual analyses in which care was taken to completely wash-out B and Ta signals between samples' (§3.1)" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "PerkinElmer" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "PerkinElmer SCIEX ELAN 6100 DRC (stated section 3.1)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "N — an ELAN 6100 DRC; no cell gas or cell mode is described (§3.1)" .

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

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (intermediate gas; stated section 3.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 14 ;
    schema1:description "14 L/min (outer ICP gas; stated section 3.1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "Partially -- instrument conditioning before tuning is stated: \"Drift was minimized by flushing through a rock solution for 30 min before tuning the instrument for a run\". No warm-up time after plasma ignition and no session duration limit stated" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1350 W (§3.1)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1350 ;
    schema1:description "1350 W (stated section 3.1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "bomb attack: 48 h; re-dissolution: overnight — §3.3" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 190 ;
    schema1:description "bomb attack: 190 °C; re-dissolution: 150 °C — §3.3" ;
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

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:description "0.50 ml of 1.0 µg/ml Rh in the 50 ml final solution — §3.3" ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value 5e-01 ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3.1e+00 ;
    schema1:description "N — 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (§3.1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Glass microconcentric nebulizer (MCN; stated section 3.1)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
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

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ce2+/Ce+ — §3.1" ;
    schema1:name "Doubly-Charged Species Monitor" ;
    schema1:valueName "doublyChargedSpeciesMonitorDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ce2+/Ce+ below 2.5% — §3.1" ;
    schema1:name "Doubly-Charged Species Production" ;
    schema1:valueName "doublyChargedSpeciesProductionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60–240 ppm Ca (Table 1, §2, §3.5) Reported detail: ada:signalCollectionMode = Peak hopping — Table 1; ada:driftCorrectionMethod = Drift monitors of intermediate concentration every 3 samples, corrected off-line by linear interpolation between two consecutive monitors — §3.4.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "foraminiferal calcite"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:defaultValue": 300,
          "schema:description": "Ten to twenty tests, about 300 µg of shells — §2; one measurement uses 250 µl at 100 ppm Ca, equivalent to 60 µg calcite"
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
        "schema:name": "PerkinElmer Elan DRC II (stated section 2 and Table 1)",
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
          "schema:value": "Pulse counting for all isotopes — Table 1; 'We determined all isotopes using pulse mode to avoid the need for cross calibration' (§3.1)"
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
          "schema:defaultValue": "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks — §2, §3.2"
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
          "schema:defaultValue": "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\""
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
              "schema:description": "15 L/min (Table 1)"
            },
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
              "schema:description": "1.2 L/min (Table 1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N — an Elan DRC II; no cell gas or cell mode is described",
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
        "schema:name": "PerkinElmer",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "B",
      "Mg",
      "Al",
      "Mn",
      "Zn",
      "Sr",
      "Cd",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "7Li",
        "targetSpecies": "Li"
      },
      {
        "monitoredProperty": "11B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "25Mg",
        "targetSpecies": "Mg"
      },
      {
        "monitoredProperty": "46Ca"
      },
      {
        "monitoredProperty": "27Al",
        "targetSpecies": "Al"
      },
      {
        "monitoredProperty": "55Mn",
        "targetSpecies": "Mn"
      },
      {
        "monitoredProperty": "66Zn",
        "targetSpecies": "Zn"
      },
      {
        "monitoredProperty": "87Sr",
        "targetSpecies": "Sr"
      },
      {
        "monitoredProperty": "111Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "238U",
        "targetSpecies": "U"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: 250 sweeps per reading, 1 reading per replicate — Table 1",
  "ada:numberOfReplicatesPerSample": "6 — Table 1",
  "ada:analysisSequenceDefault": "8 external calibration standards, then 50–80 samples interspersed with drift correction standards every 3 samples — 6–10 hours (§3.4)",
  "ada:signalCollectionMode": "Peak hopping",
  "ada:driftCorrectionMethod": "N/A",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 µl 0.075 M HNO3. 20 µl diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca — §2",
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
        "schema:position": 2,
        "schema:description": "missing"
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
            "schema:defaultValue": "N/A — all isotopes in pulse mode 'to avoid the need for cross calibration' (§3.1)"
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
        "ada:detectionLimitMethod": "all: 3 × SD/m, with SD of several measurements of a sample whose ratio is close to the blank and m the calibration slope — Table 2 note b",
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
        "schema:description": "dissolution (200 µl 0.075 M HNO3) — §2; the paper does not call it a digestion",
        "bios:reagent": [
          {
            "schema:name": "dissolution: 0.075 M HNO3 — §2",
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
      "schema:value": "Cone conditioning with pure Ca solution (100 ppm) for 0.5–1 hours before optimisation — §3.4; blanks stable over a typical run of ~5 hr (§3.2)"
    }
  ],
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
  "ada:samplingUnitType": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:reportedProperties": [
    "Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (µmol/mol); Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); U/Ca (nmol/mol) — Table 2 note a"
  ],
  "ada:chromatographicSeparationApplied": "None",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 0.075 M HNO3 at 100 ppm Ca — §2; working standards diluted with the same acid",
  "ada:washTimeBetweenSamples": "60 s — Table 1; uptake time 65 s",
  "ada:uncertaintyLevel": "RSD% -- \"RSD% (relative standard deviation) = [SD of measurements/average ratio]*100%\"",
  "ada:calibrationMeasurementFrequency": "8 calibration standards per run, drift monitors every 3 samples — §3.4",
  "ada:oxideProductionMethodAndThreshold": "CeO/Ce within 3% — 'Plasma robustness was monitored by constraining CeO/Ce ratio within 3%' (§2)",
  "ada:blankBackgroundCorrectionMethod": "Average blank subtracted from the average raw intensities of 6 replicate scans — blanks in the same acid as used for dissolution and dilution (§3.2)",
  "ada:internalStandardElement": "all: none — element/Ca intensity ratios against matrix-matched external standards (§3)",
  "ada:secondaryReferenceMaterialDefault": [
    "N — precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60\u2013240 ppm Ca (Table 1, \u00a72, \u00a73.5) Reported detail: ada:signalCollectionMode = Peak hopping \u2014 Table 1; ada:driftCorrectionMethod = Drift monitors of intermediate concentration every 3 samples, corrected off-line by linear interpolation between two consecutive monitors \u2014 \u00a73.4.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "foraminiferal calcite"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:defaultValue": 300,
          "schema:description": "Ten to twenty tests, about 300 \u00b5g of shells \u2014 \u00a72; one measurement uses 250 \u00b5l at 100 ppm Ca, equivalent to 60 \u00b5g calcite"
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
        "schema:name": "PerkinElmer Elan DRC II (stated section 2 and Table 1)",
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
          "schema:value": "Pulse counting for all isotopes \u2014 Table 1; 'We determined all isotopes using pulse mode to avoid the need for cross calibration' (\u00a73.1)"
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
          "schema:defaultValue": "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks \u2014 \u00a72, \u00a73.2"
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
          "schema:defaultValue": "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\""
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
              "schema:description": "15 L/min (Table 1)"
            },
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
              "schema:description": "1.2 L/min (Table 1)"
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
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N \u2014 an Elan DRC II; no cell gas or cell mode is described",
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
        "schema:name": "PerkinElmer",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "B",
      "Mg",
      "Al",
      "Mn",
      "Zn",
      "Sr",
      "Cd",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "7Li",
        "targetSpecies": "Li"
      },
      {
        "monitoredProperty": "11B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "25Mg",
        "targetSpecies": "Mg"
      },
      {
        "monitoredProperty": "46Ca"
      },
      {
        "monitoredProperty": "27Al",
        "targetSpecies": "Al"
      },
      {
        "monitoredProperty": "55Mn",
        "targetSpecies": "Mn"
      },
      {
        "monitoredProperty": "66Zn",
        "targetSpecies": "Zn"
      },
      {
        "monitoredProperty": "87Sr",
        "targetSpecies": "Sr"
      },
      {
        "monitoredProperty": "111Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "238U",
        "targetSpecies": "U"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: 250 sweeps per reading, 1 reading per replicate \u2014 Table 1",
  "ada:numberOfReplicatesPerSample": "6 \u2014 Table 1",
  "ada:analysisSequenceDefault": "8 external calibration standards, then 50\u201380 samples interspersed with drift correction standards every 3 samples \u2014 6\u201310 hours (\u00a73.4)",
  "ada:signalCollectionMode": "Peak hopping",
  "ada:driftCorrectionMethod": "N/A",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 \u00b5l 0.075 M HNO3. 20 \u00b5l diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca \u2014 \u00a72",
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
        "schema:position": 2,
        "schema:description": "missing"
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
            "schema:defaultValue": "N/A \u2014 all isotopes in pulse mode 'to avoid the need for cross calibration' (\u00a73.1)"
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
        "ada:detectionLimitMethod": "all: 3 \u00d7 SD/m, with SD of several measurements of a sample whose ratio is close to the blank and m the calibration slope \u2014 Table 2 note b",
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
        "schema:description": "dissolution (200 \u00b5l 0.075 M HNO3) \u2014 \u00a72; the paper does not call it a digestion",
        "bios:reagent": [
          {
            "schema:name": "dissolution: 0.075 M HNO3 \u2014 \u00a72",
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
      "schema:value": "Cone conditioning with pure Ca solution (100 ppm) for 0.5\u20131 hours before optimisation \u2014 \u00a73.4; blanks stable over a typical run of ~5 hr (\u00a73.2)"
    }
  ],
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
  "ada:samplingUnitType": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:reportedProperties": [
    "Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (\u00b5mol/mol); Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); U/Ca (nmol/mol) \u2014 Table 2 note a"
  ],
  "ada:chromatographicSeparationApplied": "None",
  "ada:isotopeDilutionSpike": "None",
  "ada:finalSolutionMatrix": "all: 0.075 M HNO3 at 100 ppm Ca \u2014 \u00a72; working standards diluted with the same acid",
  "ada:washTimeBetweenSamples": "60 s \u2014 Table 1; uptake time 65 s",
  "ada:uncertaintyLevel": "RSD% -- \"RSD% (relative standard deviation) = [SD of measurements/average ratio]*100%\"",
  "ada:calibrationMeasurementFrequency": "8 calibration standards per run, drift monitors every 3 samples \u2014 \u00a73.4",
  "ada:oxideProductionMethodAndThreshold": "CeO/Ce within 3% \u2014 'Plasma robustness was monitored by constraining CeO/Ce ratio within 3%' (\u00a72)",
  "ada:blankBackgroundCorrectionMethod": "Average blank subtracted from the average raw intensities of 6 replicate scans \u2014 blanks in the same acid as used for dissolution and dilution (\u00a73.2)",
  "ada:internalStandardElement": "all: none \u2014 element/Ca intensity ratios against matrix-matched external standards (\u00a73)",
  "ada:secondaryReferenceMaterialDefault": [
    "N \u2014 precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
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

<ex:solutionQicpmsTAPP-P1> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 µl 0.075 M HNO3. 20 µl diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca — §2" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3 × SD/m, with SD of several measurements of a sample whose ratio is close to the blank and m the calibration slope — Table 2 note b" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "dissolution (200 µl 0.075 M HNO3) — §2; the paper does not call it a digestion" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "dissolution: 0.075 M HNO3 — §2" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> ;
    schema1:datePublished "missing" ;
    schema1:description "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60–240 ppm Ca (Table 1, §2, §3.5) Reported detail: ada:signalCollectionMode = Peak hopping — Table 1; ada:driftCorrectionMethod = Drift monitors of intermediate concentration every 3 samples, corrected off-line by linear interpolation between two consecutive monitors — §3.4." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Cambridge (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — P1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)" ;
                    schema1:name "ICP-AES (for initial [Ca] determination; stated section 2)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "8 external calibration standards, then 50–80 samples interspersed with drift correction standards every 3 samples — 6–10 hours (§3.4)" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler" ;
    ada:blankBackgroundCorrectionMethod "Average blank subtracted from the average raw intensities of 6 replicate scans — blanks in the same acid as used for dissolution and dilution (§3.2)" ;
    ada:calibrationMeasurementFrequency "8 calibration standards per run, drift monitors every 3 samples — §3.4" ;
    ada:chromatographicSeparationApplied "None" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 0.075 M HNO3 at 100 ppm Ca — §2; working standards diluted with the same acid" ;
    ada:internalStandardElement "all: none — element/Ca intensity ratios against matrix-matched external standards (§3)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate "all: 250 sweeps per reading, 1 reading per replicate — Table 1" ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample "6 — Table 1" ;
    ada:oxideProductionMethodAndThreshold "CeO/Ce within 3% — 'Plasma robustness was monitored by constraining CeO/Ce ratio within 3%' (§2)" ;
    ada:reportedProperties "Li/Ca, B/Ca, Mn/Ca, Zn/Ca, Cd/Ca (µmol/mol); Mg/Ca, Sr/Ca, Al/Ca (mmol/mol); U/Ca (nmol/mol) — Table 2 note a" ;
    ada:samplingUnitType "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)" ;
    ada:secondaryReferenceMaterialDefault "N — precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)" ;
    ada:signalCollectionMode "Peak hopping" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "foraminiferal calcite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "B",
                "Cd",
                "Li",
                "Mg",
                "Mn",
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
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD% -- \"RSD% (relative standard deviation) = [SD of measurements/average ratio]*100%\"" ;
    ada:washTimeBetweenSamples "60 s — Table 1; uptake time 65 s" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "PerkinElmer" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "PerkinElmer Elan DRC II (stated section 2 and Table 1)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "N — an Elan DRC II; no cell gas or cell mode is described" .

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

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.2e+00 ;
    schema1:description "1.2 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (Table 1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "Cone conditioning with pure Ca solution (100 ppm) for 0.5–1 hours before optimisation — §3.4; blanks stable over a typical run of ~5 hr (§3.2)" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks — §2, §3.2" ;
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

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Pulse counting for all isotopes — Table 1; 'We determined all isotopes using pulse mode to avoid the need for cross calibration' (§3.1)" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — all isotopes in pulse mode 'to avoid the need for cross calibration' (§3.1)" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
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

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 300 ;
    schema1:description "Ten to twenty tests, about 300 µg of shells — §2; one measurement uses 250 µl at 100 ppm Ca, equivalent to 60 µg calcite" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996–0.999, Table 2) Reported detail: ada:driftCorrectionMethod = Mass discrimination corrected with the mean elemental ratios of the calibrator measured before and after each sample — step (d).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "peridotite",
      "dunite",
      "synthetic glass",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor ≥ 1000 — clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution",
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
            "schema:value": "Eq. 1 for Sm (ID), with the pseudo-concentration Q calibrated on spike-standard mixtures, and Eq. 2 for Cd, In, Tl and Bi (ID-IS) — details in Makishima and Nakamura (2006)"
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
            "schema:defaultValue": "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference"
          }
        ],
        "ada:detectionLimitMethod": "all: 3s of the background signal of 0.5 mol/l HNO3, average of eight sessions — Results",
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFE bomb for peridotites and chondrites — the vessel for the ultrasonic digestion is not stated"
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
            "schema:description": "bomb HF: 245 °C; other: N"
          }
        ],
        "schema:description": "ultrasonic HF-HClO4 (basalts, andesites and NIST SRM 612, 614, 616, with the Sm spike, in an ultrasonic bath, dried to decompose fluorides); bomb HF (peridotites and chondrites, with the Sm spike, in a TFE bomb at 245 °C); HClO4 drying (the bomb digests); final uptake (0.5 mol/l HNO3) — after Yokoyama et al. (1999) and Makishima and Nakamura (2006)",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF-HClO4: HF + HClO4; bomb HF: HF; HClO4 drying: HClO4; final uptake: 0.5 mol/l HNO3",
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
          "schema:defaultValue": 15,
          "schema:description": "15–42 mg (basalts and andesites); 30–63 mg (peridotites); 8–22 mg (NIST glasses); 9–28 mg (chondrites)"
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
        "schema:name": "Agilent 7500cs (stated section 2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3"
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
      "@id": "ex:instrument/ICPMS",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cd",
      "In",
      "Tl",
      "Bi"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "111Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "115In",
        "targetSpecies": "In"
      },
      {
        "monitoredProperty": "205Tl",
        "targetSpecies": "Tl"
      },
      {
        "monitoredProperty": "209Bi",
        "targetSpecies": "Bi"
      },
      {
        "monitoredProperty": "95Mo"
      },
      {
        "monitoredProperty": "113Cd"
      },
      {
        "monitoredProperty": "118Sn"
      },
      {
        "monitoredProperty": "149Sm"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:analysisSequenceDefault": "Multi-element standard solution after every third sample, Mo standard solution after every sixth sample — each measurement ~6 min, including ~200 s wash",
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
      "schema:value": 1.22,
      "schema:description": "N — Sm at 1.22 ng/ml in the calibrator"
    }
  ],
  "ada:driftCorrectionMethod": "N/A",
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Makishima and Nakamura (2006) — 'Details of these methods and ICP operating conditions are described in Makishima and Nakamura (2006)'"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:reportedProperties": [
    "Cd, In, Tl, Bi (µg/g) — Tables 3–5; detection limits in pg/ml and ng/g"
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis)",
  "ada:isotopeDilutionSpike": "149Sm-enriched spike — for the ID of Sm, whose ¹⁴⁹Sm intensity is the internal standard for Cd, In, Tl and Bi",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HNO3, dilution factor ≥ 1000 — the same acid for calibrator, sample and washout solutions",
  "ada:washTimeBetweenSamples": "~200 s with 0.5 mol/l HNO3 — 0.5 mol/l HF aspirated for 200 s after the Mo standard",
  "ada:uncertaintyLevel": "RSD% (n = 5) and RPD (relative percentage difference) -- both used; \"RPD, relative percentage difference\"",
  "ada:calibrationMeasurementFrequency": "After every third sample",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 0.01 under the operating conditions — MoO+/Mo+ from a Mo standard every sixth sample, 0.8–7.4 × 10⁻⁴ during the study",
  "ada:internalStandardElement": "all: Sm (149Sm) — the spike isotope (ID-IS)",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 — the chondrites are samples"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
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
  "@id": "ex:solutionQicpmsTAPP-Agilent7500",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionQicpms protocol \u2014 Agilent7500",
  "schema:description": "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996\u20130.999, Table 2) Reported detail: ada:driftCorrectionMethod = Mass discrimination corrected with the mean elemental ratios of the calibrator measured before and after each sample \u2014 step (d).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "basalt",
      "andesite",
      "peridotite",
      "dunite",
      "synthetic glass",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor \u2265 1000 \u2014 clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution",
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
            "schema:value": "Eq. 1 for Sm (ID), with the pseudo-concentration Q calibrated on spike-standard mixtures, and Eq. 2 for Cd, In, Tl and Bi (ID-IS) \u2014 details in Makishima and Nakamura (2006)"
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
            "schema:defaultValue": "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference"
          }
        ],
        "ada:detectionLimitMethod": "all: 3s of the background signal of 0.5 mol/l HNO3, average of eight sessions \u2014 Results",
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "TFE bomb for peridotites and chondrites \u2014 the vessel for the ultrasonic digestion is not stated"
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
            "schema:description": "bomb HF: 245 \u00b0C; other: N"
          }
        ],
        "schema:description": "ultrasonic HF-HClO4 (basalts, andesites and NIST SRM 612, 614, 616, with the Sm spike, in an ultrasonic bath, dried to decompose fluorides); bomb HF (peridotites and chondrites, with the Sm spike, in a TFE bomb at 245 \u00b0C); HClO4 drying (the bomb digests); final uptake (0.5 mol/l HNO3) \u2014 after Yokoyama et al. (1999) and Makishima and Nakamura (2006)",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF-HClO4: HF + HClO4; bomb HF: HF; HClO4 drying: HClO4; final uptake: 0.5 mol/l HNO3",
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
          "schema:defaultValue": 15,
          "schema:description": "15\u201342 mg (basalts and andesites); 30\u201363 mg (peridotites); 8\u201322 mg (NIST glasses); 9\u201328 mg (chondrites)"
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
        "schema:name": "Agilent 7500cs (stated section 2)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3"
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
      "@id": "ex:instrument/ICPMS",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cd",
      "In",
      "Tl",
      "Bi"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "111Cd",
        "targetSpecies": "Cd"
      },
      {
        "monitoredProperty": "115In",
        "targetSpecies": "In"
      },
      {
        "monitoredProperty": "205Tl",
        "targetSpecies": "Tl"
      },
      {
        "monitoredProperty": "209Bi",
        "targetSpecies": "Bi"
      },
      {
        "monitoredProperty": "95Mo"
      },
      {
        "monitoredProperty": "113Cd"
      },
      {
        "monitoredProperty": "118Sn"
      },
      {
        "monitoredProperty": "149Sm"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:analysisSequenceDefault": "Multi-element standard solution after every third sample, Mo standard solution after every sixth sample \u2014 each measurement ~6 min, including ~200 s wash",
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
      "schema:value": 1.22,
      "schema:description": "N \u2014 Sm at 1.22 ng/ml in the calibrator"
    }
  ],
  "ada:driftCorrectionMethod": "N/A",
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Makishima and Nakamura (2006) \u2014 'Details of these methods and ICP operating conditions are described in Makishima and Nakamura (2006)'"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:reportedProperties": [
    "Cd, In, Tl, Bi (\u00b5g/g) \u2014 Tables 3\u20135; detection limits in pg/ml and ng/g"
  ],
  "ada:chromatographicSeparationApplied": "None (direct analysis)",
  "ada:isotopeDilutionSpike": "149Sm-enriched spike \u2014 for the ID of Sm, whose \u00b9\u2074\u2079Sm intensity is the internal standard for Cd, In, Tl and Bi",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HNO3, dilution factor \u2265 1000 \u2014 the same acid for calibrator, sample and washout solutions",
  "ada:washTimeBetweenSamples": "~200 s with 0.5 mol/l HNO3 \u2014 0.5 mol/l HF aspirated for 200 s after the Mo standard",
  "ada:uncertaintyLevel": "RSD% (n = 5) and RPD (relative percentage difference) -- both used; \"RPD, relative percentage difference\"",
  "ada:calibrationMeasurementFrequency": "After every third sample",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 0.01 under the operating conditions \u2014 MoO+/Mo+ from a Mo standard every sixth sample, 0.8\u20137.4 \u00d7 10\u207b\u2074 during the study",
  "ada:internalStandardElement": "all: Sm (149Sm) \u2014 the spike isotope (ID-IS)",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 \u2014 the chondrites are samples"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionQicpmsTAPP-Agilent7500> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3s of the background signal of 0.5 mol/l HNO3, average of eight sessions — Results" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "ultrasonic HF-HClO4 (basalts, andesites and NIST SRM 612, 614, 616, with the Sm spike, in an ultrasonic bath, dried to decompose fluorides); bomb HF (peridotites and chondrites, with the Sm spike, in a TFE bomb at 245 °C); HClO4 drying (the bomb digests); final uptake (0.5 mol/l HNO3) — after Yokoyama et al. (1999) and Makishima and Nakamura (2006)" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "ultrasonic HF-HClO4: HF + HClO4; bomb HF: HF; HClO4 drying: HClO4; final uptake: 0.5 mol/l HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor ≥ 1000 — clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996–0.999, Table 2) Reported detail: ada:driftCorrectionMethod = Mass discrimination corrected with the mean elemental ratios of the calibrator measured before and after each sample — step (d)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7500" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Makishima and Nakamura (2006) — 'Details of these methods and ICP operating conditions are described in Makishima and Nakamura (2006)'" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Multi-element standard solution after every third sample, Mo standard solution after every sixth sample — each measurement ~6 min, including ~200 s wash" ;
    ada:analyticalMode "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "After every third sample" ;
    ada:chromatographicSeparationApplied "None (direct analysis)" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 0.5 mol/l HNO3, dilution factor ≥ 1000 — the same acid for calibrator, sample and washout solutions" ;
    ada:internalStandardElement "all: Sm (149Sm) — the spike isotope (ID-IS)" ;
    ada:isotopeDilutionSpike "149Sm-enriched spike — for the ID of Sm, whose ¹⁴⁹Sm intensity is the internal standard for Cd, In, Tl and Bi" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ],
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 0.01 under the operating conditions — MoO+/Mo+ from a Mo standard every sixth sample, 0.8–7.4 × 10⁻⁴ during the study" ;
    ada:reportedProperties "Cd, In, Tl, Bi (µg/g) — Tables 3–5; detection limits in pg/ml and ng/g" ;
    ada:samplingUnitType "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"" ;
    ada:secondaryReferenceMaterialDefault "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 — the chondrites are samples" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "andesite",
                "basalt",
                "carbonaceous chondrite",
                "dunite",
                "peridotite",
                "synthetic glass" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Bi",
                "Cd",
                "In",
                "Tl" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD% (n = 5) and RPD (relative percentage difference) -- both used; \"RPD, relative percentage difference\"" ;
    ada:washTimeBetweenSamples "~200 s with 0.5 mol/l HNO3 — 0.5 mol/l HF aspirated for 200 s after the Mo standard" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Agilent" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500cs (stated section 2)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

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
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "Eq. 1 for Sm (ID), with the pseudo-concentration Q calibrated on spike-standard mixtures, and Eq. 2 for Cd, In, Tl and Bi (ID-IS) — details in Makishima and Nakamura (2006)" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 245 ;
    schema1:description "bomb HF: 245 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "TFE bomb for peridotites and chondrites — the vessel for the ultrasonic digestion is not stated" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:description "N — Sm at 1.22 ng/ml in the calibrator" ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value 1.22e+00 ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15–42 mg (basalts and andesites); 30–63 mg (peridotites); 8–22 mg (NIST glasses); 9–28 mg (chondrites)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 °C for ~48 h; the digestion for the elemental analysis is not stated — Methods Reported detail: ada:driftCorrectionMethod = Sc, In and Re internal standards — Methods.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "m/z 23–75: He; other: N — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/gasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "gasFlowRateDefault",
              "schema:name": "Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "5 mL/min — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
            }
          ],
          "schema:name": "m/z 23–75: collision-reaction cell with helium; other: N — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods); the masses are not listed",
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
        "schema:name": "Agilent",
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
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N — 'The elemental content of samples was analyzed' (Methods); the element list is in Tables S1–S2",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:driftCorrectionMethod": "N/A",
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
        "schema:position": 1,
        "schema:description": "missing"
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
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
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
        "schema:position": 4,
        "schema:description": "missing"
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
        "schema:name": "MC-ICP-MS — Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)",
        "schema:description": "N — the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:reportedProperties": [
    "N — concentrations in µg/g in the text (e.g. '[Zn] = 309 µg/g'); the list is in Tables S1–S2"
  ],
  "ada:chromatographicSeparationApplied": "N — the chemical purification described is for the Zn isotopes",
  "ada:isotopeDilutionSpike": "None",
  "ada:uncertaintyLevel": "N -- no uncertainty convention stated for the elemental (Q-ICP-MS) data; the \"2SD, n = 4\" in Methods applies to the delta-66Zn MC-ICP-MS results",
  "ada:internalStandardElement": "all: Sc, In, Re — 'added to the sample solutions to correct for any signal drift and matrix effects' (Methods)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 \u00b0C for ~48 h; the digestion for the elemental analysis is not stated \u2014 Methods Reported detail: ada:driftCorrectionMethod = Sc, In and Re internal standards \u2014 Methods.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "m/z 23\u201375: He; other: N \u2014 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/gasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "gasFlowRateDefault",
              "schema:name": "Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "5 mL/min \u2014 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
            }
          ],
          "schema:name": "m/z 23\u201375: collision-reaction cell with helium; other: N \u2014 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods); the masses are not listed",
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
        "schema:name": "Agilent",
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
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N \u2014 'The elemental content of samples was analyzed' (Methods); the element list is in Tables S1\u2013S2",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:driftCorrectionMethod": "N/A",
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
        "schema:position": 1,
        "schema:description": "missing"
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
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
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
        "schema:position": 4,
        "schema:description": "missing"
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
        "schema:name": "MC-ICP-MS \u2014 Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)",
        "schema:description": "N \u2014 the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:reportedProperties": [
    "N \u2014 concentrations in \u00b5g/g in the text (e.g. '[Zn] = 309 \u00b5g/g'); the list is in Tables S1\u2013S2"
  ],
  "ada:chromatographicSeparationApplied": "N \u2014 the chemical purification described is for the Zn isotopes",
  "ada:isotopeDilutionSpike": "None",
  "ada:uncertaintyLevel": "N -- no uncertainty convention stated for the elemental (Q-ICP-MS) data; the \"2SD, n = 4\" in Methods applies to the delta-66Zn MC-ICP-MS results",
  "ada:internalStandardElement": "all: Sc, In, Re \u2014 'added to the sample solutions to correct for any signal drift and matrix effects' (Methods)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionQicpmsTAPP-Agilent7900> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 °C for ~48 h; the digestion for the elemental analysis is not stated — Methods Reported detail: ada:driftCorrectionMethod = Sc, In and Re internal standards — Methods." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institut de Physique du Globe de Paris (IPGP), France (affiliation)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7900" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "N — the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated" ;
                    schema1:name "MC-ICP-MS — Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\"" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "N — the chemical purification described is for the Zn isotopes" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalStandardElement "all: Sc, In, Re — 'added to the sample solutions to correct for any signal drift and matrix effects' (Methods)" ;
    ada:isotopeDilutionSpike "None" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "N — concentrations in µg/g in the text (e.g. '[Zn] = 309 µg/g'); the list is in Tables S1–S2" ;
    ada:samplingUnitType "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:targetSpeciesDeclaration "N — 'The elemental content of samples was analyzed' (Methods); the element list is in Tables S1–S2" ] ;
    ada:uncertaintyLevel "N -- no uncertainty convention stated for the elemental (Q-ICP-MS) data; the \"2SD, n = 4\" in Methods applies to the delta-66Zn MC-ICP-MS results" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Agilent" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (stated Methods)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/gasFlowRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "m/z 23–75: collision-reaction cell with helium; other: N — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods); the masses are not listed" .

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

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Collision Gas Type" ;
    schema1:value "m/z 23–75: He; other: N — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)" ;
    schema1:valueName "collisionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/gasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "5 mL/min — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)" ;
    schema1:name "Gas Flow Rate" ;
    schema1:valueName "gasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "None" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
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

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca–Al–Mg fluorides tested in 19 synthetic solutions (§2.4, §2.6) Reported detail: ada:signalCollectionMode = 1 point per mass — Table 1a; ada:driftCorrectionMethod = Mass discrimination from the standard solution average, usually without drift over 2 h; when drift was observed, the standard measured before and after the sample was averaged — §2.7, §2.8.",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Powders weighed with the B, Zr–Hf and Mo–Sn–Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted — §2.5; GSJ samples and PCC-1 further pulverised (§2.3)",
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
            "@id": "ada:parameter/module/ICPMS/guardElectrode",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "guardElectrode",
            "schema:name": "Guard Electrode",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Shield torch used — §2.1.1"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
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
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "all: P/A factor determined each day before measurement — §2.1.1"
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
            "schema:value": "Eq. 1 with the pseudo-concentration Q calibrated on spike–standard mixtures, and the mass discrimination correction factor applied to the measured ratios — §2.7"
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
            "schema:defaultValue": "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) — §2.7"
          }
        ],
        "ada:detectionLimitMethod": "all: 3σ, calculated for silicate samples at the dilution factor of ~340 where matrix effects are absent — §3.6",
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Teflon (TFM-PTFE) bomb for peridotites and meteorites — §2.2.3, §2.5"
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
        "schema:description": "ultrasonic HF decomposition (basalts and andesites, <70 °C); bomb HF decomposition (peridotites and meteorites, 245 °C, mannitol added after heating); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) — abstract; §2.5",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF decomposition: 30 mol/l HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF — §2.5",
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
          "schema:defaultValue": 20,
          "schema:description": "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) — §2.5"
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
        "schema:name": "Agilent 7500cs (stated section 2.1.1)",
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
              "schema:value": "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)"
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
              "schema:value": "Scott double-pass, cooled at 2 °C, made of Teflon — Table 1a"
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
              "schema:defaultValue": 1,
              "schema:description": "N — self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (§2.6)"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (stated Table in section 2.1.1)"
            },
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
              "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
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
              "schema:value": "N — plasma power 1.6 kW (Table 1a)"
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
          "schema:name": "Quartz glass torch with Pt injector — Table 1a",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "all: no gas introduced into the octopole collision cell — 'collision gases were not introduced into the cell' (§2.1.1)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
          "schema:value": "Pulse counting and analog (>10^6 cps), switched automatically — Zr, Nb, Mo and Sb sometimes in analog at DF < ~250 (§2.1.1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.25,
          "schema:description": "Ar, 0.25 l/min — Table 1a"
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
          "schema:defaultValue": "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 — §2.1.1"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "B",
      "Zr",
      "Nb",
      "Mo",
      "Sn",
      "Sb",
      "Hf",
      "Ta"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "10B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "11B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "90Zr",
        "targetSpecies": "Zr"
      },
      {
        "monitoredProperty": "91Zr",
        "targetSpecies": "Zr"
      },
      {
        "monitoredProperty": "93Nb",
        "targetSpecies": "Nb"
      },
      {
        "monitoredProperty": "95Mo",
        "targetSpecies": "Mo"
      },
      {
        "monitoredProperty": "97Mo",
        "targetSpecies": "Mo"
      },
      {
        "monitoredProperty": "118Sn",
        "targetSpecies": "Sn"
      },
      {
        "monitoredProperty": "119Sn",
        "targetSpecies": "Sn"
      },
      {
        "monitoredProperty": "121Sb",
        "targetSpecies": "Sb"
      },
      {
        "monitoredProperty": "123Sb",
        "targetSpecies": "Sb"
      },
      {
        "monitoredProperty": "178Hf",
        "targetSpecies": "Hf"
      },
      {
        "monitoredProperty": "179Hf",
        "targetSpecies": "Hf"
      },
      {
        "monitoredProperty": "181Ta",
        "targetSpecies": "Ta"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: 48 scans in 30 s, 1 point per mass — Table 1a",
  "ada:analysisSequenceDefault": "Standard solution every two samples; each sample ~6 min including ~3 min wash. Pseudo-FI: a 40 s background step with the probe in the sample, then 30 s of sample signal — §2.1.1, §2.6",
  "ada:signalCollectionMode": "N/A",
  "ada:driftCorrectionMethod": "N/A",
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
        "schema:name": "SF-ICP-MS — Ti on a Finnigan ELEMENT at PML (§2.1.2)",
        "schema:description": "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions — §2.5, §2.8"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:reportedProperties": [
    "B, Zr, Nb, Mo, Sn, Sb, Hf, Ta (µg/g) — Tables 5–8; Nb from Nb/Zr and Nb/Mo, Ta from Ta/Mo and Ta/Hf, and their averages"
  ],
  "ada:chromatographicSeparationApplied": "None — the method 'does not require ion-exchange separation' (§1); only the Zr–Hf spike was purified",
  "ada:isotopeDilutionSpike": "10B spike; 91Zr–179Hf mixed spike; 97Mo–119Sn–121Sb mixed spike — §2.2.2–2.2.4; Nb and Ta are not spiked",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HF with mannitol, diluted — 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (§2.5)",
  "ada:washTimeBetweenSamples": "~3 min with 0.5 mol/l HF — §2.1.1; background measured after a 200 s wash (Table 1a)",
  "ada:uncertaintyLevel": "RSD% with observed ranges in parentheses",
  "ada:calibrationMeasurementFrequency": "Every two samples — §2.1.1",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% — Table 1a",
  "ada:blankBackgroundCorrectionMethod": "Background measured before each sample after a 200 s wash, and procedural blank corrections from Table 4 applied to all analyses — Table 1a; §3.6, corrections usually <1% in basalts and andesites and <4% in peridotites and meteorites",
  "ada:internalStandardElement": "all: the ID-determined Zr, Mo and Hf, as references for Nb and Ta (ID-IS) — §2.8, §3.5; Mo is preferred",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — §2.3; the chondrites are samples"
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
  "schema:description": "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca\u2013Al\u2013Mg fluorides tested in 19 synthetic solutions (\u00a72.4, \u00a72.6) Reported detail: ada:signalCollectionMode = 1 point per mass \u2014 Table 1a; ada:driftCorrectionMethod = Mass discrimination from the standard solution average, usually without drift over 2 h; when drift was observed, the standard measured before and after the sample was averaged \u2014 \u00a72.7, \u00a72.8.",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Powders weighed with the B, Zr\u2013Hf and Mo\u2013Sn\u2013Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted \u2014 \u00a72.5; GSJ samples and PCC-1 further pulverised (\u00a72.3)",
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
            "@id": "ada:parameter/module/ICPMS/guardElectrode",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "guardElectrode",
            "schema:name": "Guard Electrode",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Shield torch used \u2014 \u00a72.1.1"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
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
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "all: P/A factor determined each day before measurement \u2014 \u00a72.1.1"
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
            "schema:value": "Eq. 1 with the pseudo-concentration Q calibrated on spike\u2013standard mixtures, and the mass discrimination correction factor applied to the measured ratios \u2014 \u00a72.7"
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
            "schema:defaultValue": "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) \u2014 \u00a72.7"
          }
        ],
        "ada:detectionLimitMethod": "all: 3\u03c3, calculated for silicate samples at the dilution factor of ~340 where matrix effects are absent \u2014 \u00a73.6",
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionVesselType",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionVesselType",
            "schema:name": "Digestion Vessel Type",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Teflon (TFM-PTFE) bomb for peridotites and meteorites \u2014 \u00a72.2.3, \u00a72.5"
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
        "schema:description": "ultrasonic HF decomposition (basalts and andesites, <70 \u00b0C); bomb HF decomposition (peridotites and meteorites, 245 \u00b0C, mannitol added after heating); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) \u2014 abstract; \u00a72.5",
        "bios:reagent": [
          {
            "schema:name": "ultrasonic HF decomposition: 30 mol/l HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF \u2014 \u00a72.5",
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
          "schema:defaultValue": 20,
          "schema:description": "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) \u2014 \u00a72.5"
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
        "schema:name": "Agilent 7500cs (stated section 2.1.1)",
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
              "schema:value": "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)"
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
              "schema:value": "Scott double-pass, cooled at 2 \u00b0C, made of Teflon \u2014 Table 1a"
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
              "schema:defaultValue": 1,
              "schema:description": "N \u2014 self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (\u00a72.6)"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "15 L/min (stated Table in section 2.1.1)"
            },
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
              "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
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
              "schema:value": "N \u2014 plasma power 1.6 kW (Table 1a)"
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
          "schema:name": "Quartz glass torch with Pt injector \u2014 Table 1a",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "all: no gas introduced into the octopole collision cell \u2014 'collision gases were not introduced into the cell' (\u00a72.1.1)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
          "schema:value": "Pulse counting and analog (>10^6 cps), switched automatically \u2014 Zr, Nb, Mo and Sb sometimes in analog at DF < ~250 (\u00a72.1.1)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.25,
          "schema:description": "Ar, 0.25 l/min \u2014 Table 1a"
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
          "schema:defaultValue": "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 \u2014 \u00a72.1.1"
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "B",
      "Zr",
      "Nb",
      "Mo",
      "Sn",
      "Sb",
      "Hf",
      "Ta"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "10B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "11B",
        "targetSpecies": "B"
      },
      {
        "monitoredProperty": "90Zr",
        "targetSpecies": "Zr"
      },
      {
        "monitoredProperty": "91Zr",
        "targetSpecies": "Zr"
      },
      {
        "monitoredProperty": "93Nb",
        "targetSpecies": "Nb"
      },
      {
        "monitoredProperty": "95Mo",
        "targetSpecies": "Mo"
      },
      {
        "monitoredProperty": "97Mo",
        "targetSpecies": "Mo"
      },
      {
        "monitoredProperty": "118Sn",
        "targetSpecies": "Sn"
      },
      {
        "monitoredProperty": "119Sn",
        "targetSpecies": "Sn"
      },
      {
        "monitoredProperty": "121Sb",
        "targetSpecies": "Sb"
      },
      {
        "monitoredProperty": "123Sb",
        "targetSpecies": "Sb"
      },
      {
        "monitoredProperty": "178Hf",
        "targetSpecies": "Hf"
      },
      {
        "monitoredProperty": "179Hf",
        "targetSpecies": "Hf"
      },
      {
        "monitoredProperty": "181Ta",
        "targetSpecies": "Ta"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "ada:massCyclesPerReplicate": "all: 48 scans in 30 s, 1 point per mass \u2014 Table 1a",
  "ada:analysisSequenceDefault": "Standard solution every two samples; each sample ~6 min including ~3 min wash. Pseudo-FI: a 40 s background step with the probe in the sample, then 30 s of sample signal \u2014 \u00a72.1.1, \u00a72.6",
  "ada:signalCollectionMode": "N/A",
  "ada:driftCorrectionMethod": "N/A",
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
        "schema:name": "SF-ICP-MS \u2014 Ti on a Finnigan ELEMENT at PML (\u00a72.1.2)",
        "schema:description": "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions \u2014 \u00a72.5, \u00a72.8"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:reportedProperties": [
    "B, Zr, Nb, Mo, Sn, Sb, Hf, Ta (\u00b5g/g) \u2014 Tables 5\u20138; Nb from Nb/Zr and Nb/Mo, Ta from Ta/Mo and Ta/Hf, and their averages"
  ],
  "ada:chromatographicSeparationApplied": "None \u2014 the method 'does not require ion-exchange separation' (\u00a71); only the Zr\u2013Hf spike was purified",
  "ada:isotopeDilutionSpike": "10B spike; 91Zr\u2013179Hf mixed spike; 97Mo\u2013119Sn\u2013121Sb mixed spike \u2014 \u00a72.2.2\u20132.2.4; Nb and Ta are not spiked",
  "ada:finalSolutionMatrix": "all: 0.5 mol/l HF with mannitol, diluted \u2014 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (\u00a72.5)",
  "ada:washTimeBetweenSamples": "~3 min with 0.5 mol/l HF \u2014 \u00a72.1.1; background measured after a 200 s wash (Table 1a)",
  "ada:uncertaintyLevel": "RSD% with observed ranges in parentheses",
  "ada:calibrationMeasurementFrequency": "Every two samples \u2014 \u00a72.1.1",
  "ada:oxideProductionMethodAndThreshold": "CeO+/Ce+ < 1% \u2014 Table 1a",
  "ada:blankBackgroundCorrectionMethod": "Background measured before each sample after a 200 s wash, and procedural blank corrections from Table 4 applied to all analyses \u2014 Table 1a; \u00a73.6, corrections usually <1% in basalts and andesites and <4% in peridotites and meteorites",
  "ada:internalStandardElement": "all: the ID-determined Zr, Mo and Hf, as references for Nb and Ta (ID-IS) \u2014 \u00a72.8, \u00a73.5; Mo is preferred",
  "ada:secondaryReferenceMaterialDefault": [
    "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 \u2014 \u00a72.3; the chondrites are samples"
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

<ex:solutionQicpmsTAPP-Agilent7500-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Powders weighed with the B, Zr–Hf and Mo–Sn–Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted — §2.5; GSJ samples and PCC-1 further pulverised (§2.3)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "ultrasonic HF decomposition (basalts and andesites, <70 °C); bomb HF decomposition (peridotites and meteorites, 245 °C, mannitol added after heating); re-dissolution (dried, then 5 ml 0.5 mol/l HF in an ultrasonic bath, fluorides removed by centrifuging) — abstract; §2.5" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "ultrasonic HF decomposition: 30 mol/l HF; bomb HF decomposition: 30 mol/l HF; re-dissolution: 0.5 mol/l HF — §2.5" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3σ, calculated for silicate samples at the dilution factor of ~340 where matrix effects are absent — §3.6" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca–Al–Mg fluorides tested in 19 synthetic solutions (§2.4, §2.6) Reported detail: ada:signalCollectionMode = 1 point per mass — Table 1a; ada:driftCorrectionMethod = Mass discrimination from the standard solution average, usually without drift over 2 h; when drift was observed, the standard measured before and after the sample was averaged — §2.7, §2.8." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — Agilent7500-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions — §2.5, §2.8" ;
                    schema1:name "SF-ICP-MS — Ti on a Finnigan ELEMENT at PML (§2.1.2)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard solution every two samples; each sample ~6 min including ~3 min wash. Pseudo-FI: a 40 s background step with the probe in the sample, then 30 s of sample signal — §2.1.1, §2.6" ;
    ada:analyticalMode "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\"" ;
    ada:blankBackgroundCorrectionMethod "Background measured before each sample after a 200 s wash, and procedural blank corrections from Table 4 applied to all analyses — Table 1a; §3.6, corrections usually <1% in basalts and andesites and <4% in peridotites and meteorites" ;
    ada:calibrationMeasurementFrequency "Every two samples — §2.1.1" ;
    ada:chromatographicSeparationApplied "None — the method 'does not require ion-exchange separation' (§1); only the Zr–Hf spike was purified" ;
    ada:driftCorrectionMethod "N/A" ;
    ada:finalSolutionMatrix "all: 0.5 mol/l HF with mannitol, diluted — 'The mannitol and HF concentrations in all samples and standard solutions were diluted to be similar to each other' (§2.5)" ;
    ada:internalStandardElement "all: the ID-determined Zr, Mo and Hf, as references for Nb and Ta (ID-IS) — §2.8, §3.5; Mo is preferred" ;
    ada:isotopeDilutionSpike "10B spike; 91Zr–179Hf mixed spike; 97Mo–119Sn–121Sb mixed spike — §2.2.2–2.2.4; Nb and Ta are not spiked" ;
    ada:massCyclesPerReplicate "all: 48 scans in 30 s, 1 point per mass — Table 1a" ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
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
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "CeO+/Ce+ < 1% — Table 1a" ;
    ada:reportedProperties "B, Zr, Nb, Mo, Sn, Sb, Hf, Ta (µg/g) — Tables 5–8; Nb from Nb/Zr and Nb/Mo, Ta from Ta/Mo and Ta/Hf, and their averages" ;
    ada:samplingUnitType "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites" ;
    ada:secondaryReferenceMaterialDefault "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — §2.3; the chondrites are samples" ;
    ada:signalCollectionMode "N/A" ;
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
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "B",
                "Hf",
                "Mo",
                "Nb",
                "Sb",
                "Sn",
                "Ta",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "RSD% with observed ranges in parentheses" ;
    ada:washTimeBetweenSamples "~3 min with 0.5 mol/l HF — §2.1.1; background measured after a 200 s wash (Table 1a)" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Agilent" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500cs (stated section 2.1.1)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "all: no gas introduced into the octopole collision cell — 'collision gases were not introduced into the cell' (§2.1.1)" .

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
    schema1:name "Quartz glass torch with Pt injector — Table 1a" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) — §2.7" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.90 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "1 mm Pt sampler + 0.4 mm Pt skimmer (stated Table in section 2.1.1)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> a schema1:PropertyValueSpecification ;
    schema1:name "Guard Electrode" ;
    schema1:value "Shield torch used — §2.1.1" ;
    schema1:valueName "guardElectrode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "Eq. 1 with the pseudo-concentration Q calibrated on spike–standard mixtures, and the mass discrimination correction factor applied to the measured ratios — §2.7" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2.5e-01 ;
    schema1:description "Ar, 0.25 l/min — Table 1a" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 — §2.1.1" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — plasma power 1.6 kW (Table 1a)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.6e+00 ;
    schema1:description "1.6 kW (stated Table in section 2.1.1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Pt sampler and Pt skimmer (stated Table in section 2.1.1)" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Pulse counting and analog (>10^6 cps), switched automatically — Zr, Nb, Mo and Sb sometimes in analog at DF < ~250 (§2.1.1)" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: P/A factor determined each day before measurement — §2.1.1" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
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
    schema1:value "Teflon (TFM-PTFE) bomb for peridotites and meteorites — §2.2.3, §2.5" ;
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

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 20 ;
    schema1:description "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) — §2.5" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "N — self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (§2.6)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Scott double-pass, cooled at 2 °C, made of Teflon — Table 1a" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "suspended particulate matter — digestates of the particles from the 1000 mg/L SPM isotherm experiments in freshwater (§2.3, §2.4)",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 °C) — §2.2",
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
        "schema:position": 2,
        "schema:description": "missing"
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) for Te; microwave vessels (START 1500, MLS) then PTFE vessels for Se — §2.2"
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
            "schema:description": "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); microwave digestion: up to 210 °C; Se recovery: 70 °C — §2.2"
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
            "schema:defaultValue": "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 °C, then cooled overnight; Se recovery: 1 h; other: N — §2.2"
          }
        ],
        "schema:description": "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 °C, with 750 µL 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 °C, re-dissolved with 250 µL 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); microwave digestion (40–50 mg, START 1500, 3 mL 65% HNO3, 0.5 mL 30% H2O2, 0.25 mL 40% HF and 0.5 mL Milli-Q water, ramped to 210 °C and held 10 min, cooled overnight); Se recovery (evaporated to dryness at 70 °C in PTFE vessels, recovered with 270 µL 65% HNO3 at 70 °C for 1 h, made up to 6 mL) — §2.2; the first two steps for Te, the last two for Se",
        "bios:reagent": [
          {
            "schema:name": "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; microwave digestion: HNO3 + H2O2 + HF; Se recovery: 65% HNO3 — §2.2",
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (Te, tri-acid); 40–50 mg (Se, microwave) — §2.2"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "125Te, 77Se: O2; other: N — 'oxygen-shift mode using O2 as collision gas' (§2.3)"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — the paper calls the O2 a collision gas"
            }
          ],
          "schema:name": "125Te, 77Se: oxygen-shift mode with O2 as cell gas; other: N — §2.3, §2.4",
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "125Te",
        "targetSpecies": "Te"
      },
      {
        "monitoredProperty": "77Se",
        "targetSpecies": "Se"
      },
      {
        "monitoredProperty": "103Rh"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "125Te: 125Te + 16O → 141TeO; 77Se: 77Se + 16O → 93SeO; other: N — §2.3, §2.4"
    }
  ],
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se — particulate concentrations from the digestates; units not stated for this instrument"
  ],
  "ada:finalSolutionMatrix": "N — Te digests brought to 10 mL with Milli-Q water, Se digests to 6 mL (§2.2)",
  "ada:uncertaintyLevel": "Mean +/- SD",
  "ada:internalStandardElement": "all: 103Rh — 'to correct for matrix effects' (§2.3)",
  "ada:secondaryReferenceMaterialDefault": [
    "NCS 73307 — stream sediment, for the total digestions"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:samplingUnitType": "missing",
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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "suspended particulate matter \u2014 digestates of the particles from the 1000 mg/L SPM isotherm experiments in freshwater (\u00a72.3, \u00a72.4)",
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 \u00b0C) \u2014 \u00a72.2",
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
        "schema:position": 2,
        "schema:description": "missing"
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) for Te; microwave vessels (START 1500, MLS) then PTFE vessels for Se \u2014 \u00a72.2"
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
            "schema:description": "tri-acid digestion: 110 \u00b0C; re-dissolution: 120 \u00b0C (evaporation); microwave digestion: up to 210 \u00b0C; Se recovery: 70 \u00b0C \u2014 \u00a72.2"
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
            "schema:defaultValue": "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 \u00b0C, then cooled overnight; Se recovery: 1 h; other: N \u2014 \u00a72.2"
          }
        ],
        "schema:description": "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 \u00b0C, with 750 \u00b5L 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 \u00b0C, re-dissolved with 250 \u00b5L 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); microwave digestion (40\u201350 mg, START 1500, 3 mL 65% HNO3, 0.5 mL 30% H2O2, 0.25 mL 40% HF and 0.5 mL Milli-Q water, ramped to 210 \u00b0C and held 10 min, cooled overnight); Se recovery (evaporated to dryness at 70 \u00b0C in PTFE vessels, recovered with 270 \u00b5L 65% HNO3 at 70 \u00b0C for 1 h, made up to 6 mL) \u2014 \u00a72.2; the first two steps for Te, the last two for Se",
        "bios:reagent": [
          {
            "schema:name": "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; microwave digestion: HNO3 + H2O2 + HF; Se recovery: 65% HNO3 \u2014 \u00a72.2",
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (Te, tri-acid); 40\u201350 mg (Se, microwave) \u2014 \u00a72.2"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "125Te, 77Se: O2; other: N \u2014 'oxygen-shift mode using O2 as collision gas' (\u00a72.3)"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 the paper calls the O2 a collision gas"
            }
          ],
          "schema:name": "125Te, 77Se: oxygen-shift mode with O2 as cell gas; other: N \u2014 \u00a72.3, \u00a72.4",
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
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "125Te",
        "targetSpecies": "Te"
      },
      {
        "monitoredProperty": "77Se",
        "targetSpecies": "Se"
      },
      {
        "monitoredProperty": "103Rh"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "125Te: 125Te + 16O \u2192 141TeO; 77Se: 77Se + 16O \u2192 93SeO; other: N \u2014 \u00a72.3, \u00a72.4"
    }
  ],
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se \u2014 particulate concentrations from the digestates; units not stated for this instrument"
  ],
  "ada:finalSolutionMatrix": "N \u2014 Te digests brought to 10 mL with Milli-Q water, Se digests to 6 mL (\u00a72.2)",
  "ada:uncertaintyLevel": "Mean +/- SD",
  "ada:internalStandardElement": "all: 103Rh \u2014 'to correct for matrix effects' (\u00a72.3)",
  "ada:secondaryReferenceMaterialDefault": [
    "NCS 73307 \u2014 stream sediment, for the total digestions"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:samplingUnitType": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionQicpmsTAPP-Agilent8800> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 °C, with 750 µL 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 °C, re-dissolved with 250 µL 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); microwave digestion (40–50 mg, START 1500, 3 mL 65% HNO3, 0.5 mL 30% H2O2, 0.25 mL 40% HF and 0.5 mL Milli-Q water, ramped to 210 °C and held 10 min, cooled overnight); Se recovery (evaporated to dryness at 70 °C in PTFE vessels, recovered with 270 µL 65% HNO3 at 70 °C for 1 h, made up to 6 mL) — §2.2; the first two steps for Te, the last two for Se" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; microwave digestion: HNO3 + H2O2 + HF; Se recovery: 65% HNO3 — §2.2" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 °C) — §2.2" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel (publication column of Solution_Q-ICP-MS_TAPP_v94.csv)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "N — 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — Agilent8800" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "N — Te digests brought to 10 mL with Milli-Q water, Se digests to 6 mL (§2.2)" ;
    ada:internalStandardElement "all: 103Rh — 'to correct for matrix effects' (§2.3)" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
                [ ],
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Te, Se — particulate concentrations from the digestates; units not stated for this instrument" ;
    ada:samplingUnitType "missing" ;
    ada:secondaryReferenceMaterialDefault "NCS 73307 — stream sediment, for the total digestions" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "suspended particulate matter — digestates of the particles from the 1000 mg/L SPM isotherm experiments in freshwater (§2.3, §2.4)" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Se",
                "Te" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "Mean +/- SD" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Agilent" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 8800 (QQQ-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "125Te, 77Se: oxygen-shift mode with O2 as cell gas; other: N — §2.3, §2.4" .

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
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Collision Gas Type" ;
    schema1:value "125Te, 77Se: O2; other: N — 'oxygen-shift mode using O2 as collision gas' (§2.3)" ;
    schema1:valueName "collisionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Reaction Gas Type" ;
    schema1:value "N — the paper calls the O2 a collision gas" ;
    schema1:valueName "reactionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 °C, then cooled overnight; Se recovery: 1 h; other: N — §2.2" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 110 ;
    schema1:description "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); microwave digestion: up to 210 °C; Se recovery: 70 °C — §2.2" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Closed PP tubes (DigiTUBEs, SCP Science) for Te; microwave vessels (START 1500, MLS) then PTFE vessels for Se — §2.2" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 30 ;
    schema1:description "30 mg (Te, tri-acid); 40–50 mg (Se, microwave) — §2.2" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> a schema1:PropertyValue ;
    schema1:name "Reaction Product Ion / Mass-Shift Transition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:value "125Te: 125Te + 16O → 141TeO; 77Se: 77Se + 16O → 93SeO; other: N — §2.3, §2.4" .


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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "sediment"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "SPM recovered by centrifugation, oven dried (70 °C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) — §2.2, Table 1",
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
        "schema:description": "KED; O2 mode — '126Te measured in KED-mode (He)'; '125Te ... in mass-shift O2-mode'; Se 'with the O2-mode' (§2.3, §2.4)",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) for the total digestion; acid-washed PP Falcon 50 mL tubes for the extractions — §2.2"
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
            "schema:description": "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 °C; F3 H2O2: 85 °C, then 25 °C"
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
            "schema:defaultValue": "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N"
          }
        ],
        "schema:description": "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 °C, with 750 µL 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 °C, re-dissolved with 250 µL 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); F1 acetate (500 mg, 10 mL 1 M NaOAc with 5 M HOAc pH adjustment, 6 h shaking at 25 °C); F2 ascorbate (200 mg, 12.5 mL ascorbate solution pH 8, 24 h at 25 °C); F3 H2O2 (500 mg, 2.5 mL 30% H2O2 at pH 5 + 1.5 mL 30% H2O2 + 2.5 mL 1 M ammonium acetate, 2 h + 3 h at 85 °C + 30 min shaking at 25 °C); F4 HCl (200 mg, 12.5 mL 1 M HCl, 24 h at 25 °C); F4N HNO3 (200 mg, 12.5 mL 1 M HNO3, 24 h at 25 °C) — §2.2 and Table 1 (after Audry et al. 2006)",
        "bios:reagent": [
          {
            "schema:name": "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; F1 acetate: 1 M NaOAc + 5 M HOAc; F2 ascorbate: ascorbate solution; F3 H2O2: 30% H2O2 + 1 M ammonium acetate; F4 HCl: 1 M HCl; F4N HNO3: 1 M HNO3",
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (total digestion); 200–500 mg per extraction — §2.2, Table 1"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "126Te: He; 125Te, 77Se, 78Se, 80Se, 82Se: O2; other: N — §2.3, §2.4"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — the O2 mode is named, not its gas role"
            }
          ],
          "schema:name": "126Te: KED with He; 125Te, 77Se, 78Se, 80Se, 82Se: mass-shift O2 mode; other: N — §2.3, §2.4",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "§2.3"
      },
      {
        "monitoredProperty": "§2.4"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "N — 'mass-shift O2-mode'; the product ions are not stated for this instrument"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2",
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
  "ada:samplingUnitType": "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se (mg/kg) — particulate concentrations"
  ],
  "ada:chromatographicSeparationApplied": "None",
  "ada:finalSolutionMatrix": "N — digests brought to 10 mL with Milli-Q water; extracts in their extraction reagents",
  "ada:uncertaintyLevel": "Mean ± SD",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 1643f, NCS 73307, NIST 1640a — freshwater, stream sediment and freshwater"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardElement": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "sediment"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "SPM recovered by centrifugation, oven dried (70 \u00b0C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) \u2014 \u00a72.2, Table 1",
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
        "schema:description": "KED; O2 mode \u2014 '126Te measured in KED-mode (He)'; '125Te ... in mass-shift O2-mode'; Se 'with the O2-mode' (\u00a72.3, \u00a72.4)",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
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
            "schema:value": "Closed PP tubes (DigiTUBEs, SCP Science) for the total digestion; acid-washed PP Falcon 50 mL tubes for the extractions \u2014 \u00a72.2"
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
            "schema:description": "tri-acid digestion: 110 \u00b0C; re-dissolution: 120 \u00b0C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 \u00b0C; F3 H2O2: 85 \u00b0C, then 25 \u00b0C"
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
            "schema:defaultValue": "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N"
          }
        ],
        "schema:description": "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 \u00b0C, with 750 \u00b5L 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 \u00b0C, re-dissolved with 250 \u00b5L 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); F1 acetate (500 mg, 10 mL 1 M NaOAc with 5 M HOAc pH adjustment, 6 h shaking at 25 \u00b0C); F2 ascorbate (200 mg, 12.5 mL ascorbate solution pH 8, 24 h at 25 \u00b0C); F3 H2O2 (500 mg, 2.5 mL 30% H2O2 at pH 5 + 1.5 mL 30% H2O2 + 2.5 mL 1 M ammonium acetate, 2 h + 3 h at 85 \u00b0C + 30 min shaking at 25 \u00b0C); F4 HCl (200 mg, 12.5 mL 1 M HCl, 24 h at 25 \u00b0C); F4N HNO3 (200 mg, 12.5 mL 1 M HNO3, 24 h at 25 \u00b0C) \u2014 \u00a72.2 and Table 1 (after Audry et al. 2006)",
        "bios:reagent": [
          {
            "schema:name": "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; F1 acetate: 1 M NaOAc + 5 M HOAc; F2 ascorbate: ascorbate solution; F3 H2O2: 30% H2O2 + 1 M ammonium acetate; F4 HCl: 1 M HCl; F4N HNO3: 1 M HNO3",
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
          "schema:defaultValue": 30,
          "schema:description": "30 mg (total digestion); 200\u2013500 mg per extraction \u2014 \u00a72.2, Table 1"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "126Te: He; 125Te, 77Se, 78Se, 80Se, 82Se: O2; other: N \u2014 \u00a72.3, \u00a72.4"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 the O2 mode is named, not its gas role"
            }
          ],
          "schema:name": "126Te: KED with He; 125Te, 77Se, 78Se, 80Se, 82Se: mass-shift O2 mode; other: N \u2014 \u00a72.3, \u00a72.4",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:monitoredPropertyTemplate": {
    "ada:defaultMonitoredProperties": [
      {
        "monitoredProperty": "\u00a72.3"
      },
      {
        "monitoredProperty": "\u00a72.4"
      }
    ],
    "ada:monitoredPropertyColumns": [
      {
        "schema:valueName": "monitoredProperty",
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
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "N \u2014 'mass-shift O2-mode'; the product ions are not stated for this instrument"
    }
  ],
  "ada:numberOfAcquisitionPasses": "2",
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
  "ada:samplingUnitType": "Weighed sediment aliquot \u2014 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se (mg/kg) \u2014 particulate concentrations"
  ],
  "ada:chromatographicSeparationApplied": "None",
  "ada:finalSolutionMatrix": "N \u2014 digests brought to 10 mL with Milli-Q water; extracts in their extraction reagents",
  "ada:uncertaintyLevel": "Mean \u00b1 SD",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 1643f, NCS 73307, NIST 1640a \u2014 freshwater, stream sediment and freshwater"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:internalStandardElement": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionQicpmsTAPP-P6> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "tri-acid digestion (30 mg in closed PP DigiTUBEs on a heating block, 2 h at 110 °C, with 750 µL 14 M HNO3, 1.5 mL 10 M HCl and 2.5 mL 29 M HF); re-dissolution (evaporated at 120 °C, re-dissolved with 250 µL 14 M HNO3 and heating, brought to 10 mL with Milli-Q water); F1 acetate (500 mg, 10 mL 1 M NaOAc with 5 M HOAc pH adjustment, 6 h shaking at 25 °C); F2 ascorbate (200 mg, 12.5 mL ascorbate solution pH 8, 24 h at 25 °C); F3 H2O2 (500 mg, 2.5 mL 30% H2O2 at pH 5 + 1.5 mL 30% H2O2 + 2.5 mL 1 M ammonium acetate, 2 h + 3 h at 85 °C + 30 min shaking at 25 °C); F4 HCl (200 mg, 12.5 mL 1 M HCl, 24 h at 25 °C); F4N HNO3 (200 mg, 12.5 mL 1 M HNO3, 24 h at 25 °C) — §2.2 and Table 1 (after Audry et al. 2006)" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "tri-acid digestion: 14 M HNO3 + 10 M HCl + 29 M HF; re-dissolution: 14 M HNO3; F1 acetate: 1 M NaOAc + 5 M HOAc; F2 ascorbate: ascorbate solution; F3 H2O2: 30% H2O2 + 1 M ammonium acetate; F4 HCl: 1 M HCl; F4N HNO3: 1 M HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "SPM recovered by centrifugation, oven dried (70 °C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) — §2.2, Table 1" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "KED; O2 mode — '126Te measured in KED-mode (He)'; '125Te ... in mass-shift O2-mode'; Se 'with the O2-mode' (§2.3, §2.4)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated (publication column of Solution_Q-ICP-MS_TAPP_v94.csv)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "N — instrument given as 'iCAP-TQ, Thermo' with no laboratory stated" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — P6" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "None" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "N — digests brought to 10 mL with Milli-Q water; extracts in their extraction reagents" ;
    ada:internalStandardElement "missing" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:monitoredPropertyTemplate [ ada:defaultMonitoredProperties [ ],
                [ ] ;
            ada:monitoredPropertyColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "monitoredProperty" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> ] ;
    ada:numberOfAcquisitionPasses "2" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Te, Se (mg/kg) — particulate concentrations" ;
    ada:samplingUnitType "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction" ;
    ada:secondaryReferenceMaterialDefault "NIST 1643f, NCS 73307, NIST 1640a — freshwater, stream sediment and freshwater" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "sediment" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Se",
                "Te" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "Mean ± SD" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCAP-TQ" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "126Te: KED with He; 125Te, 77Se, 78Se, 80Se, 82Se: mass-shift O2 mode; other: N — §2.3, §2.4" .

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
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Collision Gas Type" ;
    schema1:value "126Te: He; 125Te, 77Se, 78Se, 80Se, 82Se: O2; other: N — §2.3, §2.4" ;
    schema1:valueName "collisionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Reaction Gas Type" ;
    schema1:value "N — the O2 mode is named, not its gas role" ;
    schema1:valueName "reactionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 110 ;
    schema1:description "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 °C; F3 H2O2: 85 °C, then 25 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Closed PP tubes (DigiTUBEs, SCP Science) for the total digestion; acid-washed PP Falcon 50 mL tubes for the extractions — §2.2" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 30 ;
    schema1:description "30 mg (total digestion); 200–500 mg per extraction — §2.2, Table 1" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> a schema1:PropertyValue ;
    schema1:name "Reaction Product Ion / Mass-Shift Transition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:value "N — 'mass-shift O2-mode'; the product ions are not stated for this instrument" .


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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "estuarine water"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Se masses: He + H2; other: N — §2.4"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N/A — collision mode only"
            }
          ],
          "schema:name": "Se masses: CCT mode, collision cell with He:H2; other: N — the Se masses are not listed; no cell mode is stated for Te (§2.4)",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "collisionReactionGasMixtureRatioDefault",
      "schema:name": "Collision/Reaction Gas Mixture Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Se masses: He:H2 = 92% : 8%; other: N — 'to minimise 40Ar37Cl interferences' (§2.4)"
    },
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "N/A — on-mass measurement in CCT mode"
    }
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
        "schema:position": 1,
        "schema:description": "missing"
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "Te run; Se run — dissolved Te 'directly analysed by ICP-MS (X-Series II, Thermo Fisher Scientific)' (§2.3), no laboratory named; dissolved Se on the 'XSeries 2, Thermo Fisher Scientific, KIT' (§2.4)",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
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
        "schema:position": 4,
        "schema:description": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:numberOfAcquisitionPasses": "2",
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
  "ada:samplingUnitType": "N — sub-sampled water aliquots",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se (µg/L) — dissolved concentrations"
  ],
  "ada:finalSolutionMatrix": "Te run: seawater matrices diluted in 2% HNO3, freshwater analysed directly; Se run: N — §2.3",
  "ada:internalStandardElement": "Se run: 103Rh and 115In; Te run: N — §2.4",
  "ada:secondaryReferenceMaterialDefault": [
    "CRM-TMDW, NIST 1643f — drinking water and freshwater"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:uncertaintyLevel": "missing",
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
  "schema:description": "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v94.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "estuarine water"
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Se masses: He + H2; other: N \u2014 \u00a72.4"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N/A \u2014 collision mode only"
            }
          ],
          "schema:name": "Se masses: CCT mode, collision cell with He:H2; other: N \u2014 the Se masses are not listed; no cell mode is stated for Te (\u00a72.4)",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Te",
      "Se"
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "collisionReactionGasMixtureRatioDefault",
      "schema:name": "Collision/Reaction Gas Mixture Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Se masses: He:H2 = 92% : 8%; other: N \u2014 'to minimise 40Ar37Cl interferences' (\u00a72.4)"
    },
    {
      "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "N/A \u2014 on-mass measurement in CCT mode"
    }
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
        "schema:position": 1,
        "schema:description": "missing"
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "Te run; Se run \u2014 dissolved Te 'directly analysed by ICP-MS (X-Series II, Thermo Fisher Scientific)' (\u00a72.3), no laboratory named; dissolved Se on the 'XSeries 2, Thermo Fisher Scientific, KIT' (\u00a72.4)",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
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
        "schema:position": 4,
        "schema:description": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:numberOfAcquisitionPasses": "2",
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
  "ada:samplingUnitType": "N \u2014 sub-sampled water aliquots",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Te, Se (\u00b5g/L) \u2014 dissolved concentrations"
  ],
  "ada:finalSolutionMatrix": "Te run: seawater matrices diluted in 2% HNO3, freshwater analysed directly; Se run: N \u2014 \u00a72.3",
  "ada:internalStandardElement": "Se run: 103Rh and 115In; Te run: N \u2014 \u00a72.4",
  "ada:secondaryReferenceMaterialDefault": [
    "CRM-TMDW, NIST 1643f \u2014 drinking water and freshwater"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:isotopeDilutionSpike": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:uncertaintyLevel": "missing",
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

<ex:solutionQicpmsTAPP-P7> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Te run; Se run — dissolved Te 'directly analysed by ICP-MS (X-Series II, Thermo Fisher Scientific)' (§2.3), no laboratory named; dissolved Se on the 'XSeries 2, Thermo Fisher Scientific, KIT' (§2.4)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionQicpmsTAPP instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe (publication column of Solution_Q-ICP-MS_TAPP_v94.csv)." ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Karlsruhe Institute of Technology (KIT), Germany" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS" ] ;
    schema1:name "solutionQicpms protocol — P7" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "Te run: seawater matrices diluted in 2% HNO3, freshwater analysed directly; Se run: N — §2.3" ;
    ada:internalStandardElement "Se run: 103Rh and 115In; Te run: N — §2.4" ;
    ada:isotopeDilutionSpike "missing" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfAcquisitionPasses "2" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Te, Se (µg/L) — dissolved concentrations" ;
    ada:samplingUnitType "N — sub-sampled water aliquots" ;
    ada:secondaryReferenceMaterialDefault "CRM-TMDW, NIST 1643f — drinking water and freshwater" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "estuarine water" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Se",
                "Te" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "missing" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "XSeries 2" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Se masses: CCT mode, collision cell with He:H2; other: N — the Se masses are not listed; no cell mode is stated for Te (§2.4)" .

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
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Collision Gas Type" ;
    schema1:value "Se masses: He + H2; other: N — §2.4" ;
    schema1:valueName "collisionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Reaction Gas Type" ;
    schema1:value "N/A — collision mode only" ;
    schema1:valueName "reactionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Se masses: He:H2 = 92% : 8%; other: N — 'to minimise 40Ar37Cl interferences' (§2.4)" ;
    schema1:name "Collision/Reaction Gas Mixture Ratio" ;
    schema1:valueName "collisionReactionGasMixtureRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> a schema1:PropertyValue ;
    schema1:name "Reaction Product Ion / Mass-Shift Transition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:value "N/A — on-mass measurement in CCT mode" .


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
  "schema:description": "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 µL of 100 ng/g Rh added as internal standard — Methods",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "carbonaceous asteroid particle; carbonaceous chondrite — eight Ryugu TD1 particles, and the Smithsonian Allende powder for reproducibility",
    "ada:defaultTargetMaterials": [
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 µg readability) and transferred to PFA vials without powdering — ISO class 5 cleanroom; acids distilled once",
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
        "schema:description": "Group-1; Group-2; Group-3 — the grouping of Yokoyama, Nagashima, et al. (2023), each on its own solution",
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "ID-IS of Yokoyama et al. (2017) for Group-1 and of Kagami and Yokoyama (2021) for Group-3, isotope dilution for Ti, Zr, Mo, Hf and W"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches — 'to maintain high-pressure–temperature conditions'"
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
            "schema:description": "HF-HNO3 attack: 120 °C, then 220 °C; HNO3-HCl step: 150 °C; HNO3 step: 80 °C; final uptake: N"
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
            "schema:defaultValue": "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N"
          }
        ],
        "schema:description": "HF-HNO3 attack (0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water, 3 h in an ultrasonic bath, then capped 12 h at 120 °C and 5 days at 220 °C, dried at 100 °C); HNO3-HCl step (0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O, sealed, 150 °C for 1 day, dried at 100 °C); HNO3 step (0.2 mL HNO3 + 0.2 mL H2O, 80 °C for 1 day, dried at 90 °C); final uptake (5 mL 0.5 M HNO3) — Acid digestion",
        "bios:reagent": [
          {
            "schema:name": "HF-HNO3 attack: HF + HNO3; HNO3-HCl step: HNO3 + HCl; HNO3 step: HNO3; final uptake: 0.5 M HNO3",
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
          "schema:defaultValue": 1.478,
          "schema:description": "1.478–4.325 mg per particle; 20 mg of Allende — 4%–10% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He; Ga, As, Se, Cd, In, Na, P, K, Ca: O2; other: N — Group-1 otherwise in non-gas SQ mode"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N — the O2 mode is named, not its gas role"
            }
          ],
          "schema:name": "Li, Be, Sc, Rb, Sr, Y, Ag, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U: non-gas SQ mode; Ga, As, Se, Cd, In, Na, P, K, Ca: O2 mode; Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He KED mode — Methods",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:numberOfAcquisitionPasses": "3",
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
  "ada:samplingUnitType": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Li, Be, Sc, Ga, As, Se, Rb, Sr, Y, Ag, Cd, In, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U, Na, Mg, Al, P, K, Ca, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Mo (µg/g) — Table 1; 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%)'"
  ],
  "ada:isotopeDilutionSpike": "113In–203Tl (Group-1, ID-IS); 49Ti; 91Zr–179Hf; 97Mo–182W (Group-3) — with enrichments and concentrations stated (Methods)",
  "ada:finalSolutionMatrix": "Group-1: 0.5 M HNO3, DF 20,000; Group-2: 0.5 M HNO3, DF 200,000; Group-3: 0.5 M HNO3 with ~0.05 M HF, DF 20,000 — digests in 5 mL 0.5 M HNO3 at DF 1200–3400",
  "ada:uncertaintyLevel": "2σ — Table 1",
  "ada:internalStandardElement": "Group-1: 103Rh, with the 113In–203Tl ID-IS; Group-2: 103Rh; Group-3: 91Zr and 179Hf, for Nb and Ta — Methods",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Allende powder — 20 mg, dissolved and measured under the same procedure, n = 5"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
  "schema:description": "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 \u00b5L of 100 ng/g Rh added as internal standard \u2014 Methods",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "carbonaceous asteroid particle; carbonaceous chondrite \u2014 eight Ryugu TD1 particles, and the Smithsonian Allende powder for reproducibility",
    "ada:defaultTargetMaterials": [
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
        "@id": "ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName",
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
        "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 \u00b5g readability) and transferred to PFA vials without powdering \u2014 ISO class 5 cleanroom; acids distilled once",
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
        "schema:description": "Group-1; Group-2; Group-3 \u2014 the grouping of Yokoyama, Nagashima, et al. (2023), each on its own solution",
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "ID-IS of Yokoyama et al. (2017) for Group-1 and of Kagami and Yokoyama (2021) for Group-3, isotope dilution for Ti, Zr, Mo, Hf and W"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action"
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
            "schema:value": "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches \u2014 'to maintain high-pressure\u2013temperature conditions'"
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
            "schema:description": "HF-HNO3 attack: 120 \u00b0C, then 220 \u00b0C; HNO3-HCl step: 150 \u00b0C; HNO3 step: 80 \u00b0C; final uptake: N"
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
            "schema:defaultValue": "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N"
          }
        ],
        "schema:description": "HF-HNO3 attack (0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water, 3 h in an ultrasonic bath, then capped 12 h at 120 \u00b0C and 5 days at 220 \u00b0C, dried at 100 \u00b0C); HNO3-HCl step (0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O, sealed, 150 \u00b0C for 1 day, dried at 100 \u00b0C); HNO3 step (0.2 mL HNO3 + 0.2 mL H2O, 80 \u00b0C for 1 day, dried at 90 \u00b0C); final uptake (5 mL 0.5 M HNO3) \u2014 Acid digestion",
        "bios:reagent": [
          {
            "schema:name": "HF-HNO3 attack: HF + HNO3; HNO3-HCl step: HNO3 + HCl; HNO3 step: HNO3; final uptake: 0.5 M HNO3",
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
          "schema:defaultValue": 1.478,
          "schema:description": "1.478\u20134.325 mg per particle; 20 mg of Allende \u2014 4%\u201310% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2"
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/collisionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "collisionGasType",
              "schema:name": "Collision Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He; Ga, As, Se, Cd, In, Na, P, K, Ca: O2; other: N \u2014 Group-1 otherwise in non-gas SQ mode"
            },
            {
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "N \u2014 the O2 mode is named, not its gas role"
            }
          ],
          "schema:name": "Li, Be, Sc, Rb, Sr, Y, Ag, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U: non-gas SQ mode; Ga, As, Se, Cd, In, Na, P, K, Ca: O2 mode; Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He KED mode \u2014 Methods",
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
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
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
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:numberOfAcquisitionPasses": "3",
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
  "ada:samplingUnitType": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:reportedProperties": [
    "Li, Be, Sc, Ga, As, Se, Rb, Sr, Y, Ag, Cd, In, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U, Na, Mg, Al, P, K, Ca, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Mo (\u00b5g/g) \u2014 Table 1; 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%)'"
  ],
  "ada:isotopeDilutionSpike": "113In\u2013203Tl (Group-1, ID-IS); 49Ti; 91Zr\u2013179Hf; 97Mo\u2013182W (Group-3) \u2014 with enrichments and concentrations stated (Methods)",
  "ada:finalSolutionMatrix": "Group-1: 0.5 M HNO3, DF 20,000; Group-2: 0.5 M HNO3, DF 200,000; Group-3: 0.5 M HNO3 with ~0.05 M HF, DF 20,000 \u2014 digests in 5 mL 0.5 M HNO3 at DF 1200\u20133400",
  "ada:uncertaintyLevel": "2\u03c3 \u2014 Table 1",
  "ada:internalStandardElement": "Group-1: 103Rh, with the 113In\u2013203Tl ID-IS; Group-2: 103Rh; Group-3: 91Zr and 179Hf, for Nb and Ta \u2014 Methods",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Allende powder \u2014 20 mg, dissolved and measured under the same procedure, n = 5"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:chromatographicSeparationApplied": "missing",
  "ada:driftCorrectionMethod": "missing",
  "ada:massCyclesPerReplicate": -9999,
  "ada:numberOfReplicatesPerSample": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:solutionQicpmsTAPP-P8> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "HF-HNO3 attack (0.2 mL HF + 0.1 mL HNO3 + 0.4 mL water, 3 h in an ultrasonic bath, then capped 12 h at 120 °C and 5 days at 220 °C, dried at 100 °C); HNO3-HCl step (0.2 mL HNO3 + 0.2 mL HCl + 0.2 mL H2O, sealed, 150 °C for 1 day, dried at 100 °C); HNO3 step (0.2 mL HNO3 + 0.2 mL H2O, 80 °C for 1 day, dried at 90 °C); final uptake (5 mL 0.5 M HNO3) — Acid digestion" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "HF-HNO3 attack: HF + HNO3; HNO3-HCl step: HNO3 + HCl; HNO3 step: HNO3; final uptake: 0.5 M HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 µg readability) and transferred to PFA vials without powdering — ISO class 5 cleanroom; acids distilled once" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Group-1; Group-2; Group-3 — the grouping of Yokoyama, Nagashima, et al. (2023), each on its own solution" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 µL of 100 ng/g Rh added as internal standard — Methods" ;
    schema1:instrument <ex:instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Science Tokyo" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution Q-ICP-MS (triple-quadrupole platform)" ] ;
    schema1:name "solutionQicpms protocol — P8" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "missing" ;
    ada:driftCorrectionMethod "missing" ;
    ada:finalSolutionMatrix "Group-1: 0.5 M HNO3, DF 20,000; Group-2: 0.5 M HNO3, DF 200,000; Group-3: 0.5 M HNO3 with ~0.05 M HF, DF 20,000 — digests in 5 mL 0.5 M HNO3 at DF 1200–3400" ;
    ada:internalStandardElement "Group-1: 103Rh, with the 113In–203Tl ID-IS; Group-2: 103Rh; Group-3: 91Zr and 179Hf, for Nb and Ta — Methods" ;
    ada:isotopeDilutionSpike "113In–203Tl (Group-1, ID-IS); 49Ti; 91Zr–179Hf; 97Mo–182W (Group-3) — with enrichments and concentrations stated (Methods)" ;
    ada:massCyclesPerReplicate -9999 ;
    ada:numberOfAcquisitionPasses "3" ;
    ada:numberOfReplicatesPerSample -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:reportedProperties "Li, Be, Sc, Ga, As, Se, Rb, Sr, Y, Ag, Cd, In, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U, Na, Mg, Al, P, K, Ca, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Mo (µg/g) — Table 1; 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%)'" ;
    ada:samplingUnitType "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende" ;
    ada:secondaryReferenceMaterialDefault "Smithsonian Allende powder — 20 mg, dissolved and measured under the same procedure, n = 5" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "carbonaceous asteroid particle; carbonaceous chondrite — eight Ryugu TD1 particles, and the Smithsonian Allende powder for reproducibility" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ag",
                "Al",
                "As",
                "Ba",
                "Be",
                "Bi",
                "Ca",
                "Cd",
                "Ce",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Fe",
                "Ga",
                "Gd",
                "Hf",
                "Ho",
                "In",
                "K",
                "La",
                "Li",
                "Lu",
                "Mg",
                "Mn",
                "Mo",
                "Na",
                "Nb",
                "Nd",
                "Ni",
                "P",
                "Pb",
                "Pr",
                "Rb",
                "Sc",
                "Se",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Ti",
                "Tl",
                "Tm",
                "U",
                "V",
                "W",
                "Y",
                "Yb",
                "Zn",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:uncertaintyLevel "2σ — Table 1" ;
    ada:washTimeBetweenSamples -9999 .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Sample-Introduction-System>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCAP TQ" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Li, Be, Sc, Rb, Sr, Y, Ag, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl, Pb, Bi, Th, U: non-gas SQ mode; Ga, As, Se, Cd, In, Na, P, K, Ca: O2 mode; Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He KED mode — Methods" .

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
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/collisionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Collision Gas Type" ;
    schema1:value "Mg, Al, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ti, Zr, Nb, Hf, Ta, Mo, W: He; Ga, As, Se, Cd, In, Na, P, K, Ca: O2; other: N — Group-1 otherwise in non-gas SQ mode" ;
    schema1:valueName "collisionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Reaction Gas Type" ;
    schema1:value "N — the O2 mode is named, not its gas role" ;
    schema1:valueName "reactionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "ID-IS of Yokoyama et al. (2017) for Group-1 and of Kagami and Yokoyama (2021) for Group-3, isotope dilution for Ti, Zr, Mo, Hf and W" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "HF-HNO3 attack: 120 °C, then 220 °C; HNO3-HCl step: 150 °C; HNO3 step: 80 °C; final uptake: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "PFA hexagonal cap vials (6 mL, Savillex), tightly capped with polypropylene wrenches — 'to maintain high-pressure–temperature conditions'" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.478e+00 ;
    schema1:description "1.478–4.325 mg per particle; 20 mg of Allende — 4%–10% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution Q-ICP-MS Technique-Aligned Protocol Profile (solutionQicpmsTAPP)
description: Solution quadrupole ICP-MS extension of the base TAPP definition, generated
  from tapp/Current TAPPs/Solution_Q-ICP-MS_TAPP_v94.csv via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
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
                  const: ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName
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
                  const: ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionVesselType
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
                            const: ada:parameter/solutionQicpmsTAPP/analysisInclusionAndRejectionCriteriaDefault
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
                            const: ada:parameter/solutionQicpmsTAPP/analysisInclusionAndRejectionCriteriaDefault
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
                  - title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
                  minContains: 0
                  maxContains: 1
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_plasmaThermalMode
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_plasmaThermalMode
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
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_collisionGasType
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_gasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_cellExitDiscriminationVoltage
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasType
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasFlowRate
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_collisionGasType
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_gasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_cellExitDiscriminationVoltage
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasType
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasFlowRate
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
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Collision Reaction Cell
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
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
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_internalStandardConcentration
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        - title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: collisionReactionGasMixtureRatioDefault
            schema:name:
              const: Collision/Reaction Gas Mixture Ratio
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
        - title: Reaction Product Ion / Mass-Shift Transition
          description: Where a monitored mass is produced by a reaction in the collision/reaction
            cell, the precursor ion, the reagent gas and the product ion measured.
            Records the mass-shift chemistry relating the mass measured to the target
            species it reports, which the monitored mass alone does not state. Record
            'N/A' where the target species is measured on its own mass.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition
            schema:name:
              const: Reaction Product Ion / Mass-Shift Transition
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
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
      - contains:
          title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: collisionReactionGasMixtureRatioDefault
            schema:name:
              const: Collision/Reaction Gas Mixture Ratio
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
          title: Reaction Product Ion / Mass-Shift Transition
          description: Where a monitored mass is produced by a reaction in the collision/reaction
            cell, the precursor ion, the reagent gas and the product ion measured.
            Records the mass-shift chemistry relating the mass measured to the target
            species it reports, which the monitored mass alone does not state. Record
            'N/A' where the target species is measured on its own mass.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionQicpmsTAPP/reactionProductIonMassShiftTransition
            schema:name:
              const: Reaction Product Ion / Mass-Shift Transition
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
    ada:monitoredPropertyTemplate:
      type: object
      properties:
        ada:defaultMonitoredProperties:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
        ada:monitoredPropertyColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/MonitoredPropertyIdentifierColumn
            - title: Dwell Time per Mass
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass
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
            - title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied
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
              description: The isobaric, polyatomic and doubly charged species that
                overlap the measured masses and are corrected in data reduction -
                direct isobars, oxides and argides, hydrides, and abundance-sensitivity
                tailing from an adjacent large beam. Name each species and the mass
                it affects.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod
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
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/dwellTimePerMass
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
              title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/spectralInterferenceCorrectionsApplied
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
              description: The isobaric, polyatomic and doubly charged species that
                overlap the measured masses and are corrected in data reduction -
                direct isobars, oxides and argides, hydrides, and abundance-sensitivity
                tailing from an adjacent large beam. Name each species and the mass
                it affects.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferingSpecies
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/solutionQicpmsTAPP/interferenceCorrectionMethod
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
      required:
      - ada:defaultMonitoredProperties
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
        measurements acquired per sample solution.
      anyOf:
      - type: integer
      - type: string
    ada:signalCollectionMode:
      description: Mode used to collect ion signal across the monitored masses. In
        peak hopping mode, the quadrupole jumps sequentially between pre-set mass
        positions and dwells at each peak; in scanning mode, the quadrupole sweeps
        continuously across a defined mass range.
      type: string
      enum:
      - Peak hopping
      - Scanning
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
    ada:numberOfAcquisitionPasses:
      description: Number of acquisition passes the procedure runs. A count of the
        passes enumerated in Acquisition Pass, recorded separately so multi-pass procedures
        are findable without parsing that field.
      anyOf:
      - type: integer
      - type: string
      readOnly: true
  required:
  - ada:massCyclesPerReplicate
  - ada:numberOfReplicatesPerSample
  - ada:signalCollectionMode
  - ada:driftCorrectionMethod
  - ada:numberOfAcquisitionPasses

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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp/context.jsonld)

## Sources

* [Solution_Q-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-Q-ICPMS/tapp`

