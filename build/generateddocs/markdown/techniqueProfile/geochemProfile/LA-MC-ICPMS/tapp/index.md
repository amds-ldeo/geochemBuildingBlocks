
# LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.tapp` *v0.1*

Laser-ablation multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-MC-ICPMS_TAPP_v13.csv via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### laMcicpmsTAPP example Zhang2022
laMcicpmsTAPP instance derived from Zhang et al. 2022 (At. Spectrosc. 43) Lunar meteorite silicates (Rb-Sr geochronology) Line scan (transect) fs-LA-MC-ICP-MS China Univ. of Geosciences.
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
  "@id": "ex:laMcicpmsTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Lunar Meteorite Rb-Sr Transect fs-LA-MC-ICP-MS v1",
  "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability Reported detail: ada:isobaricInterferenceCorrectionsApplied = correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law).",
  "ada:analysisSequenceDefault": "14 reference glasses analyzed to evaluate accuracy and provide calibration factors; natural minerals as unknowns for data quality evaluation; 1 block of 120 cycles per analysis",
  "ada:analyticalAccuracy": "87Sr/86Sr relative errors <0.2‰ for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within ±3% for 11 glasses; exceptions: NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) — all within stated ±3% criterion",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field (MC-ICP-MS)",
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
              "@id": "ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "Auxiliary: 0.80 l min⁻¹ Ar"
            },
            {
              "@id": "ada:parameter/laMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16.0,
              "schema:description": "Cool gas: 16.0 l min⁻¹ Ar"
            },
            {
              "@id": "ada:parameter/laMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1250,
              "schema:description": "1250 W"
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
              "@id": "ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "X skimmer cone + Jet sample cone (high-sensitivity configuration)"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "ada:collectorConfiguration": [
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupGainCalibrationMethod",
              "schema:name": "Faraday Cup Gain Calibration Method",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "integrationTimePerCycle",
              "schema:name": "Integration Time per Cycle",
              "ada:dataType": "number",
              "schema:defaultValue": 0.524,
              "schema:description": "0.524 s integration time per cycle (one block of 120 cycles = 62.88 s total)"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "interferenceCorrectionMethod",
              "schema:name": "Interference Correction Method",
              "ada:dataType": "string",
              "schema:defaultValue": "Sequential interference correction: (a) doubly charged Er and Yb corrections on Sr masses using measured 167Er²⁺ and 173Yb²⁺ signals and natural isotope ratios; (b) 87Rb isobaric correction on 87Sr using measured 85Rb signal and user-specified 87Rb/85Rb calculated from exponential law for mass bias"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/interferingSpecies",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "interferingSpecies",
              "schema:name": "Interfering Species",
              "ada:dataType": "string",
              "schema:defaultValue": [
                "¹⁶⁸Er²⁺ on ⁸⁴Sr",
                "¹⁷⁰Er²⁺ + ¹⁷⁰Yb²⁺ on ⁸⁵Rb",
                "¹⁷²Yb²⁺ on ⁸⁶Sr",
                "¹⁷⁴Yb²⁺ on ⁸⁷Sr",
                "⁸⁷Rb on ⁸⁷Sr (isobaric)"
              ]
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "ionCounterDeadTime",
              "schema:name": "Ion Counter Dead Time",
              "ada:dataType": "number",
              "schema:defaultValue": -9999
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/massResolutionAssignment",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "massResolutionAssignment",
              "schema:name": "Mass Resolution Assignment",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            }
          ]
        },
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
          "@id": "ada:parameter/laMcicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laMcicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Seven fixed electron multiplier ICs + nine Faraday cups (1011 Ω resistors)"
        },
        {
          "@id": "ada:parameter/laMcicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N₂ added downstream"
        },
        {
          "@id": "ada:parameter/laMcicpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/ΔM ≈ 400)"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific NEPTUNE Plus (MC-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:laserPulseDuration": "300 fs (Yb:KGW PHAROS femtosecond amplifier)",
      "schema:model": {
        "schema:name": "New Wave Research NWR FemtoUC (Yb:KGW fs, 257 nm PHAROS amplifier)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "257 nm Yb:KGW femtosecond; pulse duration 300 fs (PHAROS system)",
      "schema:name": "Two-volume cell (constant distance between laser and aerosol extraction)",
      "ada:laserSpotGeometryDefault": "50–60 µm circular",
      "ada:laserFluenceDefault": "~60% of maximum output (PHAROS system; exact J cm⁻² not converted)",
      "ada:laserRepetitionRateDefault": "10–30 Hz (varied based on Sr concentration in samples)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:backgroundCountTimeDefault": "30 cycles × 0.524 s ≈ 15.7 s (first 30 cycles of the 120-cycle block with no laser ablation)",
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr⁺ signals removed by correction; no additional Kr peak stripping applied",
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min⁻¹ (two-volume cell)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:internalStandardElement": "No conventional IS; ⁸⁵Rb used to calculate ⁸⁷Rb/⁸⁶Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:isobaricInterferenceCorrectionsApplied": true,
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
    },
    {
      "@id": "ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 12,
      "schema:description": "Ar make-up (flow rate not separately stated); N₂ 12 ml min⁻¹ added via Y-connector downstream of signal-smoothing device"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2–6 µm s⁻¹ (varied based on Sr concentration in target minerals)"
    },
    {
      "@id": "ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Standard error (SE = SD/√n) for repeatability within individual runs; assessed separately for 87Sr/86Sr and 87Rb/86Sr using signal intensity regression"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (two-volume cell)",
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
            "@id": "ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "⁸⁸Sr/⁸⁶Sr = 8.37520933 used for Sr isotope mass fractionation correction (exponential law); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for ⁸⁷Rb/⁸⁶Sr calculation; external calibration factor from reference glasses applied to correct Rb/Sr elemental fractionation"
          },
          {
            "@id": "ada:parameter/laMcicpmsTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability"
          },
          {
            "@id": "ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals"
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
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zhang et al. (2022) At. Spectrosc. 43; ISO-Compass software; Zhang et al. (2018)"
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
          "@id": "ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished thin section (two-volume cell)"
        }
      ]
    },
    {
      "schema:name": "Lunar meteorite silicates (plagioclase, pyroxene, ilmenite, glass)"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:withinSessionPrecision": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-MC-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Zhang et al. (China Univ. of Geosciences Wuhan)",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "National Natural Science Foundation of China (NSFC)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan at 2–6 µm s⁻¹)"
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "L4 (⁸³Kr)",
      "L3 (¹⁶⁷Er²⁺)",
      "L2 (⁸⁴Sr)",
      "L1 (⁸⁵Rb)",
      "C (⁸⁶Sr)",
      "H1 (¹⁷³Yb²⁺)",
      "H2 (⁸⁷Sr)",
      "H3 (⁸⁸Sr) (7 cups monitoring Kr, Rb, Er, Yb, Sr)"
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
        "@id": "ada:analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "perAnalyteCalibrationStrategy",
        "schema:name": "Per-Analyte Calibration Strategy",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/instrumentSensitivity",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "instrumentSensitivity",
        "schema:name": "Instrument Sensitivity",
        "ada:dataType": "number"
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:uncertaintyLevel": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laMcicpmsTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Lunar Meteorite Rb-Sr Transect fs-LA-MC-ICP-MS v1",
  "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability Reported detail: ada:isobaricInterferenceCorrectionsApplied = correction for doubly charged ions: \u00b9\u2076\u2078Er\u00b2\u207a on \u2078\u2074Sr; \u00b9\u2077\u2070Er\u00b2\u207a and \u00b9\u2077\u2070Yb\u00b2\u207a on \u2078\u2075Rb; \u00b9\u2077\u00b2Yb\u00b2\u207a on \u2078\u2076Sr; \u00b9\u2077\u2074Yb\u00b2\u207a on \u2078\u2077Sr; \u2078\u2077Rb isobaric on \u2078\u2077Sr (corrected using 85Rb signal and exponential law).",
  "ada:analysisSequenceDefault": "14 reference glasses analyzed to evaluate accuracy and provide calibration factors; natural minerals as unknowns for data quality evaluation; 1 block of 120 cycles per analysis",
  "ada:analyticalAccuracy": "87Sr/86Sr relative errors <0.2\u2030 for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within \u00b13% for 11 glasses; exceptions: NIST 610 (\u22122.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) \u2014 all within stated \u00b13% criterion",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field (MC-ICP-MS)",
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
              "@id": "ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "Auxiliary: 0.80 l min\u207b\u00b9 Ar"
            },
            {
              "@id": "ada:parameter/laMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16.0,
              "schema:description": "Cool gas: 16.0 l min\u207b\u00b9 Ar"
            },
            {
              "@id": "ada:parameter/laMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1250,
              "schema:description": "1250 W"
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
              "@id": "ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "X skimmer cone + Jet sample cone (high-sensitivity configuration)"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "ada:collectorConfiguration": [
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupGainCalibrationMethod",
              "schema:name": "Faraday Cup Gain Calibration Method",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "integrationTimePerCycle",
              "schema:name": "Integration Time per Cycle",
              "ada:dataType": "number",
              "schema:defaultValue": 0.524,
              "schema:description": "0.524 s integration time per cycle (one block of 120 cycles = 62.88 s total)"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "interferenceCorrectionMethod",
              "schema:name": "Interference Correction Method",
              "ada:dataType": "string",
              "schema:defaultValue": "Sequential interference correction: (a) doubly charged Er and Yb corrections on Sr masses using measured 167Er\u00b2\u207a and 173Yb\u00b2\u207a signals and natural isotope ratios; (b) 87Rb isobaric correction on 87Sr using measured 85Rb signal and user-specified 87Rb/85Rb calculated from exponential law for mass bias"
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/interferingSpecies",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "interferingSpecies",
              "schema:name": "Interfering Species",
              "ada:dataType": "string",
              "schema:defaultValue": [
                "\u00b9\u2076\u2078Er\u00b2\u207a on \u2078\u2074Sr",
                "\u00b9\u2077\u2070Er\u00b2\u207a + \u00b9\u2077\u2070Yb\u00b2\u207a on \u2078\u2075Rb",
                "\u00b9\u2077\u00b2Yb\u00b2\u207a on \u2078\u2076Sr",
                "\u00b9\u2077\u2074Yb\u00b2\u207a on \u2078\u2077Sr",
                "\u2078\u2077Rb on \u2078\u2077Sr (isobaric)"
              ]
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "ionCounterDeadTime",
              "schema:name": "Ion Counter Dead Time",
              "ada:dataType": "number",
              "schema:defaultValue": -9999
            },
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/massResolutionAssignment",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "massResolutionAssignment",
              "schema:name": "Mass Resolution Assignment",
              "ada:dataType": "string",
              "schema:defaultValue": "missing"
            }
          ]
        },
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
          "@id": "ada:parameter/laMcicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laMcicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Seven fixed electron multiplier ICs + nine Faraday cups (1011 \u03a9 resistors)"
        },
        {
          "@id": "ada:parameter/laMcicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N\u2082 added downstream"
        },
        {
          "@id": "ada:parameter/laMcicpmsTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/\u0394M \u2248 400)"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific NEPTUNE Plus (MC-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:laserPulseDuration": "300 fs (Yb:KGW PHAROS femtosecond amplifier)",
      "schema:model": {
        "schema:name": "New Wave Research NWR FemtoUC (Yb:KGW fs, 257 nm PHAROS amplifier)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "257 nm Yb:KGW femtosecond; pulse duration 300 fs (PHAROS system)",
      "schema:name": "Two-volume cell (constant distance between laser and aerosol extraction)",
      "ada:laserSpotGeometryDefault": "50\u201360 \u00b5m circular",
      "ada:laserFluenceDefault": "~60% of maximum output (PHAROS system; exact J cm\u207b\u00b2 not converted)",
      "ada:laserRepetitionRateDefault": "10\u201330 Hz (varied based on Sr concentration in samples)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:backgroundCountTimeDefault": "30 cycles \u00d7 0.524 s \u2248 15.7 s (first 30 cycles of the 120-cycle block with no laser ablation)",
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr\u207a signals removed by correction; no additional Kr peak stripping applied",
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min\u207b\u00b9 (two-volume cell)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:internalStandardElement": "No conventional IS; \u2078\u2075Rb used to calculate \u2078\u2077Rb/\u2078\u2076Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:isobaricInterferenceCorrectionsApplied": true,
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
    },
    {
      "@id": "ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 12,
      "schema:description": "Ar make-up (flow rate not separately stated); N\u2082 12 ml min\u207b\u00b9 added via Y-connector downstream of signal-smoothing device"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2\u20136 \u00b5m s\u207b\u00b9 (varied based on Sr concentration in target minerals)"
    },
    {
      "@id": "ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Standard error (SE = SD/\u221an) for repeatability within individual runs; assessed separately for 87Sr/86Sr and 87Rb/86Sr using signal intensity regression"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (two-volume cell)",
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
            "@id": "ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "\u2078\u2078Sr/\u2078\u2076Sr = 8.37520933 used for Sr isotope mass fractionation correction (exponential law); \u2078\u2077Rb/\u2078\u2075Rb = 0.385706 and \u2078\u2076Sr/\u2078\u2078Sr = 0.119351 for \u2078\u2077Rb/\u2078\u2076Sr calculation; external calibration factor from reference glasses applied to correct Rb/Sr elemental fractionation"
          },
          {
            "@id": "ada:parameter/laMcicpmsTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability"
          },
          {
            "@id": "ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals"
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
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of \u2078\u2077Rb/\u2078\u2076Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for \u2078\u2077Sr/\u2078\u2076Sr data quality evaluation",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zhang et al. (2022) At. Spectrosc. 43; ISO-Compass software; Zhang et al. (2018)"
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
          "@id": "ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished thin section (two-volume cell)"
        }
      ]
    },
    {
      "schema:name": "Lunar meteorite silicates (plagioclase, pyroxene, ilmenite, glass)"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 \u2014 measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:withinSessionPrecision": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: \u00b13% for most reference glasses; 87Sr/86Sr relative errors: <0.2\u2030 for materials with 87Rb/86Sr <1",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-MC-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Zhang et al. (China Univ. of Geosciences Wuhan)",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "National Natural Science Foundation of China (NSFC)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087\u20131096)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan at 2\u20136 \u00b5m s\u207b\u00b9)"
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "L4 (\u2078\u00b3Kr)",
      "L3 (\u00b9\u2076\u2077Er\u00b2\u207a)",
      "L2 (\u2078\u2074Sr)",
      "L1 (\u2078\u2075Rb)",
      "C (\u2078\u2076Sr)",
      "H1 (\u00b9\u2077\u00b3Yb\u00b2\u207a)",
      "H2 (\u2078\u2077Sr)",
      "H3 (\u2078\u2078Sr) (7 cups monitoring Kr, Rb, Er, Yb, Sr)"
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
        "@id": "ada:analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "perAnalyteCalibrationStrategy",
        "schema:name": "Per-Analyte Calibration Strategy",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laMcicpmsTAPP/instrumentSensitivity",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "instrumentSensitivity",
        "schema:name": "Instrument Sensitivity",
        "ada:dataType": "number"
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:uncertaintyLevel": "missing",
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

ex:laMcicpmsTAPP-Zhang2022 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section (two-volume cell)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zhang et al. (China Univ. of Geosciences Wuhan)" ] ;
    schema1:datePublished "missing" ;
    schema1:description "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability Reported detail: ada:isobaricInterferenceCorrectionsApplied = correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "National Natural Science Foundation of China (NSFC)" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-MC-ICP-MS" ] ;
    schema1:name "Zhang et al. (2022) Lunar Meteorite Rb-Sr Transect fs-LA-MC-ICP-MS v1" ;
    schema1:object [ schema1:name "Lunar meteorite silicates (plagioclase, pyroxene, ilmenite, glass)" ],
        [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zhang et al. (2022) At. Spectrosc. 43; ISO-Compass software; Zhang et al. (2018)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Transect (continuous line scan at 2–6 µm s⁻¹)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "14 reference glasses analyzed to evaluate accuracy and provide calibration factors; natural minerals as unknowns for data quality evaluation; 1 block of 120 cycles per analysis" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/instrumentSensitivity>,
                <https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy> ;
            ada:defaultAnalytes "C (⁸⁶Sr)",
                "H1 (¹⁷³Yb²⁺)",
                "H2 (⁸⁷Sr)",
                "H3 (⁸⁸Sr) (7 cups monitoring Kr, Rb, Er, Yb, Sr)",
                "L1 (⁸⁵Rb)",
                "L2 (⁸⁴Sr)",
                "L3 (¹⁶⁷Er²⁺)",
                "L4 (⁸³Kr)" ] ;
    ada:analyticalAccuracy "87Sr/86Sr relative errors <0.2‰ for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within ±3% for 11 glasses; exceptions: NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) — all within stated ±3% criterion" ;
    ada:backgroundCountTimeDefault "30 cycles × 0.524 s ≈ 15.7 s (first 30 cycles of the 120-cycle block with no laser ablation)" ;
    ada:betweenSessionPrecision "missing" ;
    ada:blankBackgroundCorrectionMethod "First 30 cycles (no laser ablation) used for background collection; background Kr⁺ signals removed by correction; no additional Kr peak stripping applied" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He, 0.90 l min⁻¹ (two-volume cell)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardApproach "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)" ;
    ada:internalStandardElement "No conventional IS; ⁸⁵Rb used to calculate ⁸⁷Rb/⁸⁶Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses" ;
    ada:isobaricInterferenceCorrectionsApplied true ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation" ;
    ada:signalIntegrationIntervalMethod "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    ada:withinSessionPrecision "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1" ;
    bios:computationalTool [ schema1:name "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/instrumentSensitivity> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Sensitivity" ;
    schema1:valueName "instrumentSensitivity" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Per-Analyte Calibration Strategy" ;
    schema1:valueName "perAnalyteCalibrationStrategy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "missing" ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "missing" ;
    schema1:name "Faraday Cup Gain Calibration Method" ;
    schema1:valueName "faradayCupGainCalibrationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/integrationTimePerCycle> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5.24e-01 ;
    schema1:description "0.524 s integration time per cycle (one block of 120 cycles = 62.88 s total)" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycle" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Sequential interference correction: (a) doubly charged Er and Yb corrections on Sr masses using measured 167Er²⁺ and 173Yb²⁺ signals and natural isotope ratios; (b) 87Rb isobaric correction on 87Sr using measured 85Rb signal and user-specified 87Rb/85Rb calculated from exponential law for mass bias" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "¹⁶⁸Er²⁺ on ⁸⁴Sr",
        "¹⁷²Yb²⁺ on ⁸⁶Sr",
        "¹⁷⁰Er²⁺ + ¹⁷⁰Yb²⁺ on ⁸⁵Rb",
        "¹⁷⁴Yb²⁺ on ⁸⁷Sr",
        "⁸⁷Rb on ⁸⁷Sr (isobaric)" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/ionCounterDeadTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue -9999 ;
    schema1:name "Ion Counter Dead Time" ;
    schema1:valueName "ionCounterDeadTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "missing" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "Auxiliary: 0.80 l min⁻¹ Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.6e+01 ;
    schema1:description "Cool gas: 16.0 l min⁻¹ Ar" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N₂ added downstream" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "Ar make-up (flow rate not separately stated); N₂ 12 ml min⁻¹ added via Y-connector downstream of signal-smoothing device" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM ≈ 400)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "⁸⁸Sr/⁸⁶Sr = 8.37520933 used for Sr isotope mass fractionation correction (exponential law); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for ⁸⁷Rb/⁸⁶Sr calculation; external calibration factor from reference glasses applied to correct Rb/Sr elemental fractionation" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1250 ;
    schema1:description "1250 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (two-volume cell)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Standard error (SE = SD/√n) for repeatability within individual runs; assessed separately for 87Sr/86Sr and 87Rb/86Sr using signal intensity regression" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2–6 µm s⁻¹ (varied based on Sr concentration in target minerals)" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field (MC-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific NEPTUNE Plus (MC-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:name "missing" ;
    ada:collectorConfiguration <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/integrationTimePerCycle>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/interferingSpecies>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/ionCounterDeadTime>,
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/massResolutionAssignment> .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "New Wave Research NWR FemtoUC (Yb:KGW fs, 257 nm PHAROS amplifier)" ] ;
    schema1:name "Two-volume cell (constant distance between laser and aerosol extraction)" ;
    ada:laserFluenceDefault "~60% of maximum output (PHAROS system; exact J cm⁻² not converted)" ;
    ada:laserPulseDuration "300 fs (Yb:KGW PHAROS femtosecond amplifier)" ;
    ada:laserRepetitionRateDefault "10–30 Hz (varied based on Sr concentration in samples)" ;
    ada:laserSpotGeometryDefault "50–60 µm circular" ;
    ada:laserType "257 nm Yb:KGW femtosecond; pulse duration 300 fs (PHAROS system)" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/detectorConfiguration> ;
    schema1:value "Seven fixed electron multiplier ICs + nine Faraday cups (1011 Ω resistors)" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "X skimmer cone + Jet sample cone (high-sensitivity configuration)" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single line scan per location (1 block of 120 cycles at 0.524 s integration)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP)
description: Laser-ablation multi-collector ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/LA-MC-ICPMS_TAPP_v27.csv via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
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
                    const: Data reduction
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeInversionAlgorithm
                      - title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          mass fractions from spike-sample isotope ratio measurements
                          in isotope dilution (ID) analysis. Record 'None' if isotope
                          dilution is not used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laMcicpmsTAPP/isotopeDilutionDataReductionMethod
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
                        description: Any post-acquisition normalization applied to
                          correct for systematic biases identified from secondary
                          reference materials, or stoichiometric normalization applied
                          per pixel in mapping. Distinct from the primary internal
                          standard approach captured in Internal Standard Approach.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      - title: Signal Smoothing
                        description: 'Description of any signal smoothing device or
                          approach installed between the ablation cell and the ICP-MS
                          to reduce pulse-to-pulse signal variability. Note: active
                          signal smoothing devices (e.g., squid, SCFAST) are generally
                          incompatible with high-resolution raster mapping because
                          they degrade spatial resolution by mixing aerosol from successive
                          laser shots. For mapping analyses, report "None" explicitly.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/signalSmoothingDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: signalSmoothingDefault
                          schema:name:
                            const: Signal Smoothing
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
                      - title: Spike / Outlier Filtering Approach
                        description: Method used to identify and remove anomalous
                          signal spikes arising from micronuggets, inclusions, cracks,
                          or instrument artifacts during time-resolved signal processing.
                          Editable because the specific implementation may vary between
                          sessions while remaining within the procedure framework.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault
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
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeInversionAlgorithm
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          mass fractions from spike-sample isotope ratio measurements
                          in isotope dilution (ID) analysis. Record 'None' if isotope
                          dilution is not used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laMcicpmsTAPP/isotopeDilutionDataReductionMethod
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
                        description: Any post-acquisition normalization applied to
                          correct for systematic biases identified from secondary
                          reference materials, or stoichiometric normalization applied
                          per pixel in mapping. Distinct from the primary internal
                          standard approach captured in Internal Standard Approach.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Signal Smoothing
                        description: 'Description of any signal smoothing device or
                          approach installed between the ablation cell and the ICP-MS
                          to reduce pulse-to-pulse signal variability. Note: active
                          signal smoothing devices (e.g., squid, SCFAST) are generally
                          incompatible with high-resolution raster mapping because
                          they degrade spatial resolution by mixing aerosol from successive
                          laser shots. For mapping analyses, report "None" explicitly.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/signalSmoothingDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: signalSmoothingDefault
                          schema:name:
                            const: Signal Smoothing
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
                        title: Spike / Outlier Filtering Approach
                        description: Method used to identify and remove anomalous
                          signal spikes arising from micronuggets, inclusions, cracks,
                          or instrument artifacts during time-resolved signal processing.
                          Editable because the specific implementation may vary between
                          sessions while remaining within the procedure framework.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault
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
                  ada:detectionLimitMethod:
                    description: Reference or description of the method used to calculate
                      session detection limits. Mandatory at analysis level. Must
                      be consistent with the method applied to generate the Detection
                      Limit values reported above.
                    anyOf:
                    - type: string
                      enum:
                      - "3\u03C3 blank"
                      - "3\u03C3 background"
                      - "3\u03C3 counting statistics"
                      - "3\xD7 blank mean"
                      - Poisson statistics
                      - N/A
                      - None
                      - missing
                    - type: string
                    readOnly: true
            - if:
                properties:
                  schema:name:
                    const: Sample preparation
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Fusion Flux and Dilution Ratio
                        description: For procedures using fused glass, the flux type
                          and sample:flux dilution ratio used to prepare the analytical
                          glass.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatioDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: fusionFluxAndDilutionRatioDefault
                          schema:name:
                            const: Fusion Flux and Dilution Ratio
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_preAblationSurfaceTreatment
                    allOf:
                    - contains:
                        title: Fusion Flux and Dilution Ratio
                        description: For procedures using fused glass, the flux type
                          and sample:flux dilution ratio used to prepare the analytical
                          glass.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatioDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: fusionFluxAndDilutionRatioDefault
                          schema:name:
                            const: Fusion Flux and Dilution Ratio
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_preAblationSurfaceTreatment
                      minContains: 0
                      maxContains: 1
                  schema:description:
                    description: Description of how samples were prepared for analysis
                      (mounting, polishing, coating, fusion procedure, etc.).
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
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
                      description: Whether the guard electrode (also called extraction
                        lens or Fassel torch shield) was active during analysis.
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/laMcicpmsTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/laMcicpmsTAPP/guardElectrode
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
                        description: Whether the guard electrode (also called extraction
                          lens or Fassel torch shield) was active during analysis.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laMcicpmsTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laMcicpmsTAPP/guardElectrode
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
          allOf:
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Sample preparation
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Data acquisition
              required:
              - schema:name
    ada:analysisSequenceDefault:
      description: Repeating order of primary calibration standard(s), quality control
        standard(s), and unknown analyses within a measurement session. Editable to
        allow minor adjustments while maintaining the bracketing strategy defined
        in the procedure.
      type: string
    ada:analyticalAccuracy:
      description: 'Offset between measured and accepted reference values for secondary
        reference materials, expressed as % relative bias. Report both the assessment
        method and the accuracy values. Specify: (1) secondary RM used and source
        of reference values, (2) number of analyses, and (3) elements or element groups
        assessed. Report any systematic biases and likely causes.'
      type: string
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
                                argon gas stream that positions the plasma relative
                                to the load coil, in L/min. Affects ion extraction
                                efficiency and oxide production rates. Distinct from
                                the carrier gas (which transports ablation aerosol)
                                and the coolant (plasma) gas.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault
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
                              description: Flow rate of the outer (coolant/plasma)
                                argon gas stream that sustains the ICP plasma, in
                                L/min. Determines plasma volume and stability. Set
                                during initial plasma optimisation and confirmed at
                                each session start.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/coolantGasFlowRateDefault
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
                                cool plasma (\u2264900 W RF) or normal (hot) plasma
                                (>1000 W RF) conditions. Cool plasma substantially
                                reduces argide-based polyatomic interferences (e.g.,
                                \u2074\u2070Ar on \u2074\u2070Ca, \u2074\u2070Ar\u2074\u2070Ar
                                on \u2078\u2070Se). This is a fundamental method design
                                choice that determines which interference corrections
                                are necessary and should be documented independently
                                of the RF Power field."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/plasmaThermalMode
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
                              description: ICP radiofrequency forward power in watts.
                                Affects plasma temperature, ionisation efficiency,
                                oxide formation, and whether cool or normal plasma
                                conditions are in effect. The procedure registers
                                a target value optimised during initial setup; the
                                analyst confirms or fine-adjusts during session tuning.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/rfPowerDefault
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
                                argon gas stream that positions the plasma relative
                                to the load coil, in L/min. Affects ion extraction
                                efficiency and oxide production rates. Distinct from
                                the carrier gas (which transports ablation aerosol)
                                and the coolant (plasma) gas.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRateDefault
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
                              description: Flow rate of the outer (coolant/plasma)
                                argon gas stream that sustains the ICP plasma, in
                                L/min. Determines plasma volume and stability. Set
                                during initial plasma optimisation and confirmed at
                                each session start.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/coolantGasFlowRateDefault
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
                                cool plasma (\u2264900 W RF) or normal (hot) plasma
                                (>1000 W RF) conditions. Cool plasma substantially
                                reduces argide-based polyatomic interferences (e.g.,
                                \u2074\u2070Ar on \u2074\u2070Ca, \u2074\u2070Ar\u2074\u2070Ar
                                on \u2078\u2070Se). This is a fundamental method design
                                choice that determines which interference corrections
                                are necessary and should be documented independently
                                of the RF Power field."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/plasmaThermalMode
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
                              description: ICP radiofrequency forward power in watts.
                                Affects plasma temperature, ionisation efficiency,
                                oxide formation, and whether cool or normal plasma
                                conditions are in effect. The procedure registers
                                a target value optimised during initial setup; the
                                analyst confirms or fine-adjusts during session tuning.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/rfPowerDefault
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
                            - title: Cell Exit Discrimination Voltage
                              description: Bias voltage applied at the collision/reaction
                                cell exit to discriminate between analyte ions and
                                low-energy polyatomic interferences in KED mode, in
                                volts (V). A negative bias preferentially retards
                                slow polyatomic ions while transmitting faster analyte
                                ions. Record 'None' if the CRC is in STD mode. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                            - title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas (typically
                                He) introduced into the collision/reaction cell, in
                                mL/min. Controls the degree of ion thermalization
                                and KED efficiency. Record 'None' if the CRC is in
                                STD mode. Record 'N/A' where Collision/Reaction Cell
                                (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/collisionGasFlowRateDefault
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
                            - title: Collision Gas Type
                              description: Type of collision gas introduced into the
                                collision/reaction cell in KED mode. Helium (He) is
                                the standard collision gas for kinetic energy discrimination
                                due to its low mass and chemical inertness. Record
                                'None' if the CRC is in STD mode or not installed.
                                Record 'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/collisionGasType
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
                            - title: Reaction Gas Flow Rate
                              description: Flow rate of the reactive gas introduced
                                into the dynamic reaction cell (DRC), in mL/min. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/reactionGasFlowRateDefault
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
                            - title: Reaction Gas Type
                              description: "Type of reactive gas introduced into the
                                dynamic reaction cell (DRC) for interference removal
                                through ion-molecule reactions. Common reaction gases
                                include NH\u2083 (e.g., for Fe, Ca, K isotopes) and
                                O\u2082 (e.g., for As, Ge). Record 'None' if DRC mode
                                is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include DRC."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/reactionGasType
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
                          allOf:
                          - contains:
                              title: Cell Exit Discrimination Voltage
                              description: Bias voltage applied at the collision/reaction
                                cell exit to discriminate between analyte ions and
                                low-energy polyatomic interferences in KED mode, in
                                volts (V). A negative bias preferentially retards
                                slow polyatomic ions while transmitting faster analyte
                                ions. Record 'None' if the CRC is in STD mode. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                              title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas (typically
                                He) introduced into the collision/reaction cell, in
                                mL/min. Controls the degree of ion thermalization
                                and KED efficiency. Record 'None' if the CRC is in
                                STD mode. Record 'N/A' where Collision/Reaction Cell
                                (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/collisionGasFlowRateDefault
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
                              title: Collision Gas Type
                              description: Type of collision gas introduced into the
                                collision/reaction cell in KED mode. Helium (He) is
                                the standard collision gas for kinetic energy discrimination
                                due to its low mass and chemical inertness. Record
                                'None' if the CRC is in STD mode or not installed.
                                Record 'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/collisionGasType
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
                              title: Reaction Gas Flow Rate
                              description: Flow rate of the reactive gas introduced
                                into the dynamic reaction cell (DRC), in mL/min. Record
                                'N/A' where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/reactionGasFlowRateDefault
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
                          - contains:
                              title: Reaction Gas Type
                              description: "Type of reactive gas introduced into the
                                dynamic reaction cell (DRC) for interference removal
                                through ion-molecule reactions. Common reaction gases
                                include NH\u2083 (e.g., for Fe, Ca, K isotopes) and
                                O\u2082 (e.g., for As, Ge). Record 'None' if DRC mode
                                is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include DRC."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/reactionGasType
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
                        schema:name:
                          description: Whether a collision or reaction cell is installed
                            and its operating mode. In standard mode (STD), no cell
                            gas is introduced and the cell acts only as an ion guide.
                            In kinetic energy discrimination (KED) mode, helium thermalizes
                            ions so that polyatomic interferences (larger collision
                            cross-section) are selectively retarded by a cell exit
                            barrier voltage. In dynamic reaction cell (DRC) mode,
                            a reactive gas selectively neutralizes specific interferences
                            through ion-molecule reactions. On ICP-MS/MS instruments
                            (e.g., Agilent 8900), a second mass filter preceding the
                            cell enables precursor-ion selection. Specific gas types,
                            flow rates, and cell voltages are documented in Group
                            4. Record 'Not applicable' for SF-ICP-MS instruments,
                            which lack collision/reaction cells. Record 'N/A' where
                            the instrument is not fitted with a collision/reaction
                            cell.
                          anyOf:
                          - type: string
                            enum:
                            - Not installed
                            - STD (standard mode, no gas)
                            - KED (kinetic energy discrimination, He gas)
                            - DRC (dynamic reaction cell, reactive gas)
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
                              - N/A
                              - None
                              - missing
                              readOnly: true
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Collector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        ada:collectorConfiguration:
                          type: array
                          items:
                            anyOf:
                            - title: Faraday Cup Amplifier Resistor Values
                              description: "Resistance values (\u03A9) of the feedback
                                resistors in the Faraday cup amplifiers. Standard
                                amplifiers use 10\xB9\xB9 \u03A9 resistors, yielding
                                1 V per ~6.24 \xD7 10\u2076 ion counts per second.
                                High-gain amplifiers (10\xB9\xB2 or 10\xB9\xB3 \u03A9)
                                are fitted to selected cups to improve signal-to-noise
                                for very low-intensity beams (e.g., 234U, low-abundance
                                spike isotopes). Report the resistor value per cup
                                position, or note 'all 10\xB9\xB9 \u03A9' if uniform."
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: faradayCupAmplifierResistorValues
                                schema:name:
                                  const: Faraday Cup Amplifier Resistor Values
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
                            - title: Faraday Cup Gain Calibration Method
                              description: 'Method used to calibrate the relative
                                gain (amplification factor) of each Faraday cup amplifier
                                at the start of or during each analytical session.
                                Relative gain differences between amplifiers cause
                                systematic errors in isotope ratios if uncorrected.
                                Common approaches: instrument internal gain calibration
                                routine (measures signal in each cup sequentially
                                using a common beam), amplifier rotation procedure,
                                or measurement of a known isotope ratio solution in
                                each cup. For instruments with SEM detectors, also
                                describes the SEM-to-Faraday cross-calibration sequence.
                                Specify frequency (per session, per block, weekly).'
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: faradayCupGainCalibrationMethod
                                schema:name:
                                  const: Faraday Cup Gain Calibration Method
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
                            - title: Integration Time per Cycle
                              description: "Duration of signal integration per measurement
                                cycle (seconds). Determines counting statistics per
                                cycle. Longer integration times improve shot-noise
                                precision but increase the impact of signal drift
                                within the integration window. For high-gain (10\xB9\xB2
                                or 10\xB9\xB3 \u03A9) amplifier channels, longer integration
                                times are often required to accumulate sufficient
                                charge. Procedure specifies the standard integration
                                time; analyst may confirm or adjust within procedure
                                bounds. Where different isotope channels use different
                                integration schemes, record the time for each channel."
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: integrationTimePerCycle
                                schema:name:
                                  const: Integration Time per Cycle
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
                            - title: Interference Correction Method
                              description: Equation or procedure used to correct for
                                isobaric interferences, including the production rate
                                factor and the reference material used to measure
                                it.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod
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
                            - title: Interfering Species
                              description: Elemental or molecular species (oxides,
                                argides, doubly charged ions) overlapping with the
                                measured isotope.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/interferingSpecies
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
                            - title: Ion Counter Dead Time
                              description: Dead time of each ion-counting detector
                                channel, used in the dead-time correction applied
                                to high count rates. Distinct from pulse/analog cross-calibration,
                                which relates the two detector modes rather than correcting
                                counting losses within the pulse-counting mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: ionCounterDeadTime
                                schema:name:
                                  const: Ion Counter Dead Time
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
                            - title: Mass Resolution Assignment
                              description: Mass resolution mode assigned to each acquired
                                mass. The selected resolution determines which polyatomic
                                interferences are physically resolved by the magnetic
                                sector. One analyte may be acquired at more than one
                                resolution, so the assignment is per acquired mass
                                rather than per element. The overall mode(s) used
                                in the procedure are recorded in Mass Resolution Setting
                                (Group 3).
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/massResolutionAssignment
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
                              title: Faraday Cup Amplifier Resistor Values
                              description: "Resistance values (\u03A9) of the feedback
                                resistors in the Faraday cup amplifiers. Standard
                                amplifiers use 10\xB9\xB9 \u03A9 resistors, yielding
                                1 V per ~6.24 \xD7 10\u2076 ion counts per second.
                                High-gain amplifiers (10\xB9\xB2 or 10\xB9\xB3 \u03A9)
                                are fitted to selected cups to improve signal-to-noise
                                for very low-intensity beams (e.g., 234U, low-abundance
                                spike isotopes). Report the resistor value per cup
                                position, or note 'all 10\xB9\xB9 \u03A9' if uniform."
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: faradayCupAmplifierResistorValues
                                schema:name:
                                  const: Faraday Cup Amplifier Resistor Values
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
                              title: Faraday Cup Gain Calibration Method
                              description: 'Method used to calibrate the relative
                                gain (amplification factor) of each Faraday cup amplifier
                                at the start of or during each analytical session.
                                Relative gain differences between amplifiers cause
                                systematic errors in isotope ratios if uncorrected.
                                Common approaches: instrument internal gain calibration
                                routine (measures signal in each cup sequentially
                                using a common beam), amplifier rotation procedure,
                                or measurement of a known isotope ratio solution in
                                each cup. For instruments with SEM detectors, also
                                describes the SEM-to-Faraday cross-calibration sequence.
                                Specify frequency (per session, per block, weekly).'
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/faradayCupGainCalibrationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: faradayCupGainCalibrationMethod
                                schema:name:
                                  const: Faraday Cup Gain Calibration Method
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
                              title: Integration Time per Cycle
                              description: "Duration of signal integration per measurement
                                cycle (seconds). Determines counting statistics per
                                cycle. Longer integration times improve shot-noise
                                precision but increase the impact of signal drift
                                within the integration window. For high-gain (10\xB9\xB2
                                or 10\xB9\xB3 \u03A9) amplifier channels, longer integration
                                times are often required to accumulate sufficient
                                charge. Procedure specifies the standard integration
                                time; analyst may confirm or adjust within procedure
                                bounds. Where different isotope channels use different
                                integration schemes, record the time for each channel."
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: integrationTimePerCycle
                                schema:name:
                                  const: Integration Time per Cycle
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
                              title: Interference Correction Method
                              description: Equation or procedure used to correct for
                                isobaric interferences, including the production rate
                                factor and the reference material used to measure
                                it.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/interferenceCorrectionMethod
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
                          - contains:
                              title: Interfering Species
                              description: Elemental or molecular species (oxides,
                                argides, doubly charged ions) overlapping with the
                                measured isotope.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/interferingSpecies
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
                              title: Ion Counter Dead Time
                              description: Dead time of each ion-counting detector
                                channel, used in the dead-time correction applied
                                to high count rates. Distinct from pulse/analog cross-calibration,
                                which relates the two detector modes rather than correcting
                                counting losses within the pulse-counting mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: ionCounterDeadTime
                                schema:name:
                                  const: Ion Counter Dead Time
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
                              title: Mass Resolution Assignment
                              description: Mass resolution mode assigned to each acquired
                                mass. The selected resolution determines which polyatomic
                                interferences are physically resolved by the magnetic
                                sector. One analyte may be acquired at more than one
                                resolution, so the assignment is per acquired mass
                                rather than per element. The overall mode(s) used
                                in the procedure are recorded in Mass Resolution Setting
                                (Group 3).
                              type: object
                              properties:
                                '@id':
                                  const: ada:channelColumn/laMcicpmsTAPP/massResolutionAssignment
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
                        schema:additionalProperty:
                          type: array
                          items:
                            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupArrayConfiguration
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupArrayConfiguration
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
                              description: Combination of sample cone and skimmer
                                cone installed during analysis.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration
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
                                skimmer cones. Common materials are nickel (standard),
                                platinum (for high-TDS or organic-matrix samples),
                                and aluminium (for high-purity work). Cone material
                                affects sensitivity, matrix tolerance, and long-term
                                stability. State both sampler and skimmer materials;
                                if identical, a single statement is acceptable.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/samplerAndSkimmerConeMaterial
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
                              description: Combination of sample cone and skimmer
                                cone installed during analysis.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/interfaceConeConfiguration
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
                                skimmer cones. Common materials are nickel (standard),
                                platinum (for high-TDS or organic-matrix samples),
                                and aluminium (for high-purity work). Cone material
                                affects sensitivity, matrix tolerance, and long-term
                                stability. State both sampler and skimmer materials;
                                if identical, a single statement is acceptable.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/samplerAndSkimmerConeMaterial
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
                            const: Torch
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
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
                                const: ada:parameter/laMcicpmsTAPP/torchDepthDefault
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
                                  const: ada:parameter/laMcicpmsTAPP/torchDepthDefault
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
                        schema:name:
                          description: "Type of plasma torch installed. Injector inner
                            diameter (typically 1.5\u20132.5 mm) affects aerosol transport
                            efficiency and plasma conditions in LA-ICP-MS."
                          anyOf:
                          - type: string
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              readOnly: true
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
                          const: Collision Reaction Cell
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Collector
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
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laMcicpmsTAPP/detectorConfiguration
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
                  - title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. Doubly-charged
                      ions appear at half the mass of the parent ion and can cause
                      isobaric interferences on analytes in that mass region. The
                      monitor species and the mass positions monitored should be stated
                      explicitly. Analogous to Oxide Production Method and Threshold
                      for oxide monitoring."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                      The procedure should specify the acceptable threshold (e.g.,
                      <1%, <3%); the measured value for each session is recorded here.
                      Report both the threshold and the measured value where possible.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                  - title: ICP Tuning
                    description: Description of the approach used to optimise ICP
                      plasma conditions prior to analysis, including the reference
                      material used for tuning and the acceptance criteria (e.g.,
                      oxide production threshold, sensitivity targets, mass calibration).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/icpTuningDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: icpTuningDefault
                      schema:name:
                        const: ICP Tuning
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
                        const: ada:parameter/laMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: Operating mass resolution of the mass analyser. For
                      quadrupole instruments this is fixed at unit resolution by instrument
                      design. For sector-field instruments the analyst selects low,
                      medium, or high resolution to balance sensitivity against spectral
                      interference suppression.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/massResolutionSettingDefault
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
                    description: Procedure applied to identify and minimise memory
                      effects from high-concentration elements in the previous sample
                      or standard that may contaminate subsequent analyses, or from
                      incomplete aerosol washout between adjacent pixels in raster
                      mapping mode. For mapping, the mitigation strategy involves
                      controlling scan speed relative to washout time to ensure each
                      pixel signal is sufficiently free of the preceding pixel's contribution.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/memoryEffectMitigationDefault
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
                    title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laMcicpmsTAPP/detectorConfiguration
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
                    title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. Doubly-charged
                      ions appear at half the mass of the parent ion and can cause
                      isobaric interferences on analytes in that mass region. The
                      monitor species and the mass positions monitored should be stated
                      explicitly. Analogous to Oxide Production Method and Threshold
                      for oxide monitoring."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                      The procedure should specify the acceptable threshold (e.g.,
                      <1%, <3%); the measured value for each session is recorded here.
                      Report both the threshold and the measured value where possible.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                    title: ICP Tuning
                    description: Description of the approach used to optimise ICP
                      plasma conditions prior to analysis, including the reference
                      material used for tuning and the acceptance criteria (e.g.,
                      oxide production threshold, sensitivity targets, mass calibration).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/icpTuningDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: icpTuningDefault
                      schema:name:
                        const: ICP Tuning
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
                        const: ada:parameter/laMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: Operating mass resolution of the mass analyser. For
                      quadrupole instruments this is fixed at unit resolution by instrument
                      design. For sector-field instruments the analyst selects low,
                      medium, or high resolution to balance sensitivity against spectral
                      interference suppression.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/massResolutionSettingDefault
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
                    description: Procedure applied to identify and minimise memory
                      effects from high-concentration elements in the previous sample
                      or standard that may contaminate subsequent analyses, or from
                      incomplete aerosol washout between adjacent pixels in raster
                      mapping mode. For mapping, the mitigation strategy involves
                      controlling scan speed relative to washout time to ensure each
                      pixel signal is sufficiently free of the preceding pixel's contribution.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/memoryEffectMitigationDefault
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
              schema:manufacturer:
                type: object
                properties:
                  schema:name:
                    description: Manufacturer of the instrument that performs the
                      measurement, recorded as a controlled value so that procedures
                      can be found by vendor. Where a procedure couples a sample-introduction
                      system to an analysing instrument, this records the analysing
                      instrument. Instrument Model gives the specific designation.
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
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: Laser Ablation System
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserBeamEnergyProfile
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserEnergy
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserBeamEnergyProfile
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserEnergy
                  minContains: 0
                  maxContains: 1
              ada:laserPulseDuration:
                description: 'Duration of each individual laser pulse, including units.
                  Pulse duration determines the ablation regime: nanosecond (ns) pulses
                  involve significant thermal effects and elemental fractionation;
                  femtosecond (fs) pulses are non-thermal and substantially reduce
                  elemental fractionation and matrix effects. This is a fixed hardware
                  property of the laser system.'
                anyOf:
                - type: string
                  readOnly: true
                - type: array
                  items:
                    type: string
                    readOnly: true
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: ICPMS
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: Laser Ablation System
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    ada:backgroundCountTimeDefault:
      description: Total time spent measuring gas blank (background signal with laser
        off or shutter closed) before each ablation event, in seconds. For spot and
        transect analysis, a discrete background interval is measured before each
        ablation. For mapping, background is typically measured once per raster line
        or at the start of a map session rather than before each individual pixel.
        Editable to allow session-specific adjustment.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
        - title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeIsotopePair
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeMixingRatio
        - title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/instrumentWarmUpSessionDurationLimit
            schema:name:
              const: Instrument Warm-up / Session Duration Limit
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
        - title: Matrix Offset Correction (LIEF)
          description: Whether an empirical correction was applied to account for
            systematic differences in laser-induced elemental fractionation (LIEF)
            patterns between the external calibration standard and the sample matrix.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/matrixOffsetCorrection
            schema:name:
              const: Matrix Offset Correction (LIEF)
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Multi-Run Sequential Analysis Design
          description: Whether the procedure uses a single acquisition pass or multiple
            sequential runs on the same sample location, each optimized for different
            analytical objectives. For multi-run designs, describe the number of runs,
            their purpose, key laser and instrument settings per run, and how outputs
            of one run feed into data reduction of another. Not applicable to raster
            mapping, where each spatial location is visited exactly once.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign
            schema:name:
              const: Multi-Run Sequential Analysis Design
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        - title: Make-up Gas and Flow Rate
          description: "Supplementary gas added to the sample-carrying stream between
            the sample introduction system and the plasma, with its identity and the
            procedure-registered target flow rate. Argon make-up is standard and maintains
            total gas delivery where the carrier flow alone is insufficient \u2014
            downstream of an ablation cell, or of a desolvation system that has removed
            solvent load. Small nitrogen or hydrogen additions are also made here
            to enhance sensitivity for some elements; record them with their own flow,
            whose unit commonly differs from the make-up flow. Record 'None' explicitly
            where no supplementary gas is added, to distinguish it from not reported."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
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
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
        minContains: 0
        maxContains: 1
      - contains:
          title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeIsotopePair
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeMixingRatio
        minContains: 0
        maxContains: 1
      - contains:
          title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/instrumentWarmUpSessionDurationLimit
            schema:name:
              const: Instrument Warm-up / Session Duration Limit
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
        minContains: 0
        maxContains: 1
      - contains:
          title: Matrix Offset Correction (LIEF)
          description: Whether an empirical correction was applied to account for
            systematic differences in laser-induced elemental fractionation (LIEF)
            patterns between the external calibration standard and the sample matrix.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/matrixOffsetCorrection
            schema:name:
              const: Matrix Offset Correction (LIEF)
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
          title: Multi-Run Sequential Analysis Design
          description: Whether the procedure uses a single acquisition pass or multiple
            sequential runs on the same sample location, each optimized for different
            analytical objectives. For multi-run designs, describe the number of runs,
            their purpose, key laser and instrument settings per run, and how outputs
            of one run feed into data reduction of another. Not applicable to raster
            mapping, where each spatial location is visited exactly once.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/multiRunSequentialAnalysisDesign
            schema:name:
              const: Multi-Run Sequential Analysis Design
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        minContains: 0
        maxContains: 1
      - contains:
          title: Make-up Gas and Flow Rate
          description: "Supplementary gas added to the sample-carrying stream between
            the sample introduction system and the plasma, with its identity and the
            procedure-registered target flow rate. Argon make-up is standard and maintains
            total gas delivery where the carrier flow alone is insufficient \u2014
            downstream of an ablation cell, or of a desolvation system that has removed
            solvent load. Small nitrogen or hydrogen additions are also made here
            to enhance sensitivity for some elements; record them with their own flow,
            whose unit commonly differs from the make-up flow. Record 'None' explicitly
            where no supplementary gas is added, to distinguish it from not reported."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
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
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
    ada:betweenSessionPrecision:
      description: "Precision of measurements across multiple analytical sessions
        over weeks to months \u2014 long-term or intermediate precision \u2014 and
        the method used to assess it. Report both the assessment method and the precision
        values, specifying the reference material, the number of measurements and
        sessions, the time span covered, and the statistic reported. Long-term precision
        is normally poorer than within-session precision and is the figure a data
        user should carry when comparing results from different sessions."
      type: string
    ada:blankBackgroundCorrectionMethod:
      description: 'Method used to subtract the gas blank (background signal with
        laser off) from the ablation signal. For spot and transect analysis: typically
        the mean of a pre-ablation gas blank interval is subtracted per isotope per
        analysis. For mapping: background may be subtracted per raster line, per map
        session, or using a separate gas blank map acquired under identical conditions.'
      type: string
      readOnly: true
    ada:calibrationMeasurementFrequency:
      description: How often the primary calibration standard is measured relative
        to unknown samples within a session. For LA-ICP-MS, this defines the bracketing
        interval between calibration standard ablations used to monitor and correct
        for instrumental drift.
      type: string
      readOnly: true
    ada:carrierGasFlowRateDefault:
      description: "Gas used to transport ablated aerosol from the ablation cell to
        the ICP-MS torch, with the procedure-registered target flow rate(s). Helium
        is standard for most UV laser systems due to superior aerosol transport. Flow
        rates are procedure targets; actual session values may be adjusted within
        \xB110% during tuning."
      type: string
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
    schema:variableMeasured:
      type: array
      items:
        anyOf:
        - title: Dataset variable
          description: A measured variable of this dataset that is not one of the
            procedure's declared reported properties. schema:variableMeasured carries
            the dataset's actual variables; the reported-property branches above are
            permitted members of it, not the whole of it.
          type: object
          required:
          - '@type'
          properties:
            '@type':
              type: array
              contains:
                enum:
                - cdi:InstanceVariable
                - schema:PropertyValue
        - title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. Answers whether a reported aggregate is defensible as
            a single population. Procedure-level tier is N/A because the value cannot
            be known before the analysis; the procedure may still state an acceptance
            threshold, which belongs with the inclusion criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/goodnessOfFitOrDispersionStatisticDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: goodnessOfFitOrDispersionStatisticDefault
            schema:name:
              const: Goodness-of-Fit or Dispersion Statistic
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
        - title: Limit of Quantification (LOQ) Method
          description: 'Reference or description of the method used to calculate the
            limit of quantification (LOQ): the lowest concentration reliably measurable
            with acceptable precision and accuracy. Mandatory at analysis level when
            concentrations near the LOD are reported. Concentrations between LOD and
            LOQ are detectable but not reliably quantifiable.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: limitOfQuantificationMethodDefault
            schema:name:
              const: Limit of Quantification (LOQ) Method
            ada:dataType:
              const: uri
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
        - title: Normalization / Standards-Based Correction
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
          title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
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
          title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. Answers whether a reported aggregate is defensible as
            a single population. Procedure-level tier is N/A because the value cannot
            be known before the analysis; the procedure may still state an acceptance
            threshold, which belongs with the inclusion criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/goodnessOfFitOrDispersionStatisticDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: goodnessOfFitOrDispersionStatisticDefault
            schema:name:
              const: Goodness-of-Fit or Dispersion Statistic
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
          title: Limit of Quantification (LOQ) Method
          description: 'Reference or description of the method used to calculate the
            limit of quantification (LOQ): the lowest concentration reliably measurable
            with acceptable precision and accuracy. Mandatory at analysis level when
            concentrations near the LOD are reported. Concentrations between LOD and
            LOQ are detectable but not reliably quantifiable.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: limitOfQuantificationMethodDefault
            schema:name:
              const: Limit of Quantification (LOQ) Method
            ada:dataType:
              const: uri
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
          title: Normalization / Standards-Based Correction
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
    ada:elementalFractionationCorrection:
      type: array
      items:
        description: Method used to correct for laser-induced elemental fractionation
          (LIEF), including downhole fractionation during prolonged ablation, matrix-dependent
          fractionation between sample and calibration standard, and any specific
          correction algorithm applied. Reference the software function or publication.
        type: string
        readOnly: true
    ada:internalStandardApproach:
      description: Method used to determine the internal standard (IS) concentration
        for each unknown sample, used to correct for variable ablation yield between
        analyses. The approach is a fundamental procedure design choice that cannot
        be changed by analysts.
      type: string
      readOnly: true
    ada:internalStandardElement:
      description: Element(s) used as the internal standard, and how the IS concentration
        value was determined for unknown samples. For mapping procedures using oxide-sum
        normalization, report "None (oxide-sum normalization)" and cite the method
        reference.
      type: string
      readOnly: true
    ada:isobaricInterferenceCorrectionsApplied:
      description: 'Whether isobaric interference corrections were applied for any
        measured isotope in this procedure. A procedure-level Boolean: if the procedure
        includes interference corrections, this is always Yes. Detail for each affected
        mass is captured in Interfering Species and Interference Correction Method.'
      type: boolean
      readOnly: true
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Limit of Quantification (LOQ) Method
              description: 'Reference or description of the method used to calculate
                the limit of quantification (LOQ): the lowest concentration reliably
                measurable with acceptable precision and accuracy. Mandatory at analysis
                level when concentrations near the LOD are reported. Concentrations
                between LOD and LOQ are detectable but not reliably quantifiable.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: limitOfQuantificationMethod
                schema:name:
                  const: Limit of Quantification (LOQ) Method
                ada:dataType:
                  const: uri
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
                  const: ada:analyteColumn/laMcicpmsTAPP/massResolutionAssignment
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
                  const: ada:analyteColumn/laMcicpmsTAPP/monitoredMasses
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
            - title: Per-Analyte Calibration Strategy
              description: "Documents cases where different analytes or analyte groups
                within the same session are calibrated using different strategies
                \u2014 for example, one element used as the internal standard while
                trace elements are calibrated by an external reference material, or
                different primary standards applied to different mass ranges or mineral
                phases. If a single calibration strategy applies uniformly to all
                analytes, state that here and refer to Internal Standard Approach
                and Normalization / Standards-Based Correction for details. Free text;
                list the strategy for each analyte or analyte group as needed."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: perAnalyteCalibrationStrategy
                schema:name:
                  const: Per-Analyte Calibration Strategy
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
            - title: Instrument Sensitivity
              description: "Instrument sensitivity achieved in the session, with the
                isotope or channel it was measured on and the conditions it applies
                to. May be expressed either as detected signal per unit concentration
                or per unit mass of analyte delivered \u2014 counts per second per
                ppb, volts per ppm, counts per picogram \u2014 or as useful yield,
                the percentage of sampled atoms ultimately detected as ions, with
                the method used to derive it cited. Useful yield is the more comparable
                of the two wherever the amount of material consumed varies between
                procedures, as it does with spot size, fluence and repetition rate.
                Records what the instrument actually delivered; a sensitivity the
                procedure requires before analyses may begin belongs with the tuning
                acceptance criteria."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/instrumentSensitivity
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: instrumentSensitivity
                schema:name:
                  const: Instrument Sensitivity
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: O
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
          allOf:
          - contains:
              title: Limit of Quantification (LOQ) Method
              description: 'Reference or description of the method used to calculate
                the limit of quantification (LOQ): the lowest concentration reliably
                measurable with acceptable precision and accuracy. Mandatory at analysis
                level when concentrations near the LOD are reported. Concentrations
                between LOD and LOQ are detectable but not reliably quantifiable.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/limitOfQuantificationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: limitOfQuantificationMethod
                schema:name:
                  const: Limit of Quantification (LOQ) Method
                ada:dataType:
                  const: uri
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
                  const: ada:analyteColumn/laMcicpmsTAPP/massResolutionAssignment
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
                  const: ada:analyteColumn/laMcicpmsTAPP/monitoredMasses
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
              title: Per-Analyte Calibration Strategy
              description: "Documents cases where different analytes or analyte groups
                within the same session are calibrated using different strategies
                \u2014 for example, one element used as the internal standard while
                trace elements are calibrated by an external reference material, or
                different primary standards applied to different mass ranges or mineral
                phases. If a single calibration strategy applies uniformly to all
                analytes, state that here and refer to Internal Standard Approach
                and Normalization / Standards-Based Correction for details. Free text;
                list the strategy for each analyte or analyte group as needed."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/perAnalyteCalibrationStrategy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: perAnalyteCalibrationStrategy
                schema:name:
                  const: Per-Analyte Calibration Strategy
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
              title: Instrument Sensitivity
              description: "Instrument sensitivity achieved in the session, with the
                isotope or channel it was measured on and the conditions it applies
                to. May be expressed either as detected signal per unit concentration
                or per unit mass of analyte delivered \u2014 counts per second per
                ppb, volts per ppm, counts per picogram \u2014 or as useful yield,
                the percentage of sampled atoms ultimately detected as ions, with
                the method used to derive it cited. Useful yield is the more comparable
                of the two wherever the amount of material consumed varies between
                procedures, as it does with spot size, fluence and repetition rate.
                Records what the instrument actually delivered; a sensitivity the
                procedure requires before analyses may begin belongs with the tuning
                acceptance criteria."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laMcicpmsTAPP/instrumentSensitivity
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: instrumentSensitivity
                schema:name:
                  const: Instrument Sensitivity
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: O
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
    ada:massBiasCorrectionStrategy:
      description: 'Strategy used to correct instrumental isotopic mass fractionation,
        also called mass bias or mass discrimination. Distinct from Elemental Fractionation
        Correction, which addresses inter-element fractionation during ablation and
        transport: this field addresses discrimination between isotopes of the same
        element, and applies wherever the procedure reports isotope ratios.'
      type: string
      readOnly: true
    ada:oxideProductionMethodAndThreshold:
      description: "Method used to quantify plasma oxide production and the acceptance
        threshold applied before commencing analysis. Record both the monitored mass
        ratio(s) and the maximum allowed threshold(s). Measured values are recorded
        in Oxide Production. The ThO\u207A/Th\u207A ratio (mass 248/232) is most widely
        used, but UO\u207A/U\u207A (mass 254/238) or CeO\u207A/Ce\u207A (mass 156/140)
        may also be used."
      type: string
      readOnly: true
    ada:primaryStandardNameDefault:
      description: Primary reference material(s) used to calibrate the instrument
        and convert raw signal intensities to concentrations or isotope ratios. Include
        material name, source institution, and citation for the accepted values used.
        Editable because the specific lot or certification vintage may differ between
        sessions while the material type remains the same.
      type: string
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
                  title: Sample Form / Analytical Substrate
                  description: Physical form of the material as it enters the ablation
                    cell. Editable to accommodate legitimate variations (e.g., thin
                    section vs. mount) that do not alter the analytical procedure.
                  type: object
                  properties:
                    '@id':
                      const: ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault
                    '@type':
                      const:
                      - schema:PropertyValueSpecification
                    schema:valueName:
                      const: sampleFormAnalyticalSubstrateDefault
                    schema:name:
                      const: Sample Form / Analytical Substrate
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
                    title: Sample Form / Analytical Substrate
                    description: Physical form of the material as it enters the ablation
                      cell. Editable to accommodate legitimate variations (e.g., thin
                      section vs. mount) that do not alter the analytical procedure.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrateDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleFormAnalyticalSubstrateDefault
                      schema:name:
                        const: Sample Form / Analytical Substrate
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
            '@type':
              contains:
                const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
          required:
          - '@type'
    ada:sampleIntroduction:
      description: "Configuration by which the ablated aerosol is delivered to the
        plasma, including tubing, any signal-homogenising device, and any co-aspirated
        solution introduced alongside the aerosol \u2014 for example a Tl solution
        used for instrumental mass bias correction, or an isotopic spike used for
        isotope dilution. Distinct from the carrier and make-up gas fields, which
        record gas identity and flow rather than what else enters the plasma."
      type: string
      readOnly: true
    ada:secondaryReferenceMaterialDefault:
      type: array
      items:
        description: Quality-control reference materials analysed as unknowns alongside
          samples in the same session to assess accuracy and monitor drift. Include
          material name, source, and citation for accepted values used for comparison.
          Editable because selection of secondary RMs may vary across sessions.
        type: string
    ada:signalIntegrationIntervalMethod:
      description: 'Approach used to select the stable signal interval for integration
        during data reduction, and to exclude anomalous signals from inclusions or
        cracks. For spot/transect analysis: involves identifying and excluding transient
        start/end instabilities within the time-resolved signal. For mapping analysis:
        corresponds to defining Volumes of Interest (VOIs) or applying phase masks
        across the 2D map (e.g., manual selection, automated clustering, threshold-based
        masking).'
      type: string
      readOnly: true
    ada:uncertaintyLevel:
      description: "The convention at which reported uncertainties are quoted \u2014
        1-sigma, 2-sigma, or a 95% confidence interval \u2014 and whether a measured
        spread is reported as a standard error or a standard deviation. A reported
        uncertainty is not interpretable without it: the same numeric value means
        different things at 1-sigma and at 95% confidence. State the convention applying
        to all values reported under this procedure, and state each separately where
        different reported quantities use different conventions. Distinct from Uncertainty
        Propagation Method, which addresses how component uncertainties are combined
        rather than how the result is quoted."
      anyOf:
      - type: string
        enum:
        - "2\u03C3 (95% confidence)"
        - "1\u03C3 (68% confidence)"
        - 95% confidence interval
        - 2 standard errors (2SE)
        - 1 standard deviation (1SD)
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:withinSessionPrecision:
      description: Precision of repeated measurements within a single analytical session
        and the method used to assess it. Report both the assessment method and the
        precision values. The assessment method must specify the reference material
        or standard measured, the number of replicates n, and the statistic reported
        (1s RSD, 2s RSD, 2SD, 2SE, 95% CI). Distinct from the internal precision of
        a single measurement, which derives from counting statistics over the cycles
        of that measurement rather than from repeated analyses.
      type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spot
        - Transect
        - Mapping
  required:
  - ada:analysisSequenceDefault
  - ada:analyticalAccuracy
  - ada:backgroundCountTimeDefault
  - ada:betweenSessionPrecision
  - ada:blankBackgroundCorrectionMethod
  - ada:calibrationMeasurementFrequency
  - ada:carrierGasFlowRateDefault
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:internalStandardApproach
  - ada:internalStandardElement
  - ada:isobaricInterferenceCorrectionsApplied
  - ada:massBiasCorrectionStrategy
  - ada:oxideProductionMethodAndThreshold
  - ada:primaryStandardNameDefault
  - ada:sampleIntroduction
  - ada:signalIntegrationIntervalMethod
  - ada:uncertaintyLevel
  - ada:withinSessionPrecision

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/tapp/context.jsonld)

## Sources

* [LA-MC-ICPMS_TAPP_v13.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-MC-ICPMS/tapp`

