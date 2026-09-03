
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
  "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability",
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16.0,
              "schema:description": "Cool gas: 16.0 l min⁻¹ Ar"
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min⁻¹ (two-volume cell)",
  "ada:isobaricInterferenceCorrectionsApplied": "Yes — correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
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
      "@id": "ada:parameter/module/ICPMS/uncertaintyPropagationMethodDefault",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr⁺ signals removed by correction; no additional Kr peak stripping applied",
  "ada:internalStandardElement": "No conventional IS; ⁸⁵Rb used to calculate ⁸⁷Rb/⁸⁶Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
  "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability",
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
              "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRateDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16.0,
              "schema:description": "Cool gas: 16.0 l min\u207b\u00b9 Ar"
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
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
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min\u207b\u00b9 (two-volume cell)",
  "ada:isobaricInterferenceCorrectionsApplied": "Yes \u2014 correction for doubly charged ions: \u00b9\u2076\u2078Er\u00b2\u207a on \u2078\u2074Sr; \u00b9\u2077\u2070Er\u00b2\u207a and \u00b9\u2077\u2070Yb\u00b2\u207a on \u2078\u2075Rb; \u00b9\u2077\u00b2Yb\u00b2\u207a on \u2078\u2076Sr; \u00b9\u2077\u2074Yb\u00b2\u207a on \u2078\u2077Sr; \u2078\u2077Rb isobaric on \u2078\u2077Sr (corrected using 85Rb signal and exponential law)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
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
      "@id": "ada:parameter/module/ICPMS/uncertaintyPropagationMethodDefault",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr\u207a signals removed by correction; no additional Kr peak stripping applied",
  "ada:internalStandardElement": "No conventional IS; \u2078\u2075Rb used to calculate \u2078\u2077Rb/\u2078\u2076Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 \u2014 measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of \u2078\u2077Rb/\u2078\u2076Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for \u2078\u2077Sr/\u2078\u2076Sr data quality evaluation",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/uncertaintyPropagationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zhang et al. (China Univ. of Geosciences Wuhan)" ] ;
    schema1:datePublished "missing" ;
    schema1:description "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "National Natural Science Foundation of China (NSFC)" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-MC-ICP-MS" ] ;
    schema1:name "Zhang et al. (2022) Lunar Meteorite Rb-Sr Transect fs-LA-MC-ICP-MS v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ],
        [ schema1:name "Lunar meteorite silicates (plagioclase, pyroxene, ilmenite, glass)" ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zhang et al. (2022) At. Spectrosc. 43; ISO-Compass software; Zhang et al. (2018)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Transect (continuous line scan at 2–6 µm s⁻¹)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "14 reference glasses analyzed to evaluate accuracy and provide calibration factors; natural minerals as unknowns for data quality evaluation; 1 block of 120 cycles per analysis" ;
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
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:isobaricInterferenceCorrectionsApplied "Yes — correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation" ;
    ada:signalIntegrationIntervalMethod "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle" ;
    ada:uncertaintyLevel "missing" ;
    ada:withinSessionPrecision "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1" ;
    bios:computationalTool [ schema1:name "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)" ;
            ada:toolRole "dataReduction" ] .

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

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "missing" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "Auxiliary: 0.80 l min⁻¹ Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "X skimmer cone + Jet sample cone (high-sensitivity configuration)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.6e+01 ;
    schema1:description "Cool gas: 16.0 l min⁻¹ Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N₂ added downstream" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "Ar make-up (flow rate not separately stated); N₂ 12 ml min⁻¹ added via Y-connector downstream of signal-smoothing device" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM ≈ 400)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1250 ;
    schema1:description "1250 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Standard error (SE = SD/√n) for repeatability within individual runs; assessed separately for 87Sr/86Sr and 87Rb/86Sr using signal intensity regression" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single line scan per location (1 block of 120 cycles at 0.524 s integration)" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (two-volume cell)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
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
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
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
        <https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/massResolutionAssignment> .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> ;
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


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP)
description: Laser-ablation multi-collector ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/LA-MC-ICPMS_TAPP_v68.csv via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/ProcedureIdentification
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_signalSmoothing
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_signalSmoothing
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
                      minContains: 0
                      maxContains: 1
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_fusionFluxAndDilutionRatio
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_preAblationSurfaceTreatment
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_fusionFluxAndDilutionRatio
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_preAblationSurfaceTreatment
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
                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_guardElectrode
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_guardElectrode
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
                  const: Data acquisition
              required:
              - schema:name
    ada:analyticalAccuracy:
      description: Offset between measured and accepted values for secondary reference
        materials, and the method used to assess it. Specify the reference material
        and the source of its accepted values, the number of analyses, and the quantities
        assessed. Report systematic biases and their likely causes. Express the offset
        in the form appropriate to what the procedure reports - percent relative bias
        for concentrations, or deviation in delta or ratio units for isotopic quantities.
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_cellExitDiscriminationVoltage
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_gasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_collisionGasType
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasType
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_cellExitDiscriminationVoltage
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_gasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_collisionGasType
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Procedure_reactionGasType
                            minContains: 0
                            maxContains: 1
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
                                Report the resistor value per cup position, or note
                                'all 10\xB9\xB9 \u03A9' if uniform."
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
                              description: Duration of signal integration per measurement
                                cycle (seconds). Where different isotope channels
                                use different integration schemes, record the time
                                for each channel.
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
                              description: Equation or procedure used to calculate
                                and remove each interference contribution, together
                                with how its magnitude was established - a monitor
                                mass measured simultaneously and scaled by natural
                                abundance ratios, a production-rate factor measured
                                on a reference material or interference standard solution,
                                or a tailing factor measured on a pure standard. Name
                                the reference material used.
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
                              description: The isobaric, polyatomic and doubly charged
                                species that overlap the measured masses and are corrected
                                in data reduction - direct isobars, oxides and argides,
                                hydrides, and abundance-sensitivity tailing from an
                                adjacent large beam. Name each species and the mass
                                it affects.
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
                            - title: Mass Resolution Assignment
                              description: Mass resolution mode used for acquisition.
                                One analyte may be acquired at more than one resolution,
                                so the assignment is per acquired mass rather than
                                per element. The overall mode(s) used in the procedure
                                are recorded in Mass Resolution Setting (Group 3).
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
                                Report the resistor value per cup position, or note
                                'all 10\xB9\xB9 \u03A9' if uniform."
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
                              description: Duration of signal integration per measurement
                                cycle (seconds). Where different isotope channels
                                use different integration schemes, record the time
                                for each channel.
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
                              description: Equation or procedure used to calculate
                                and remove each interference contribution, together
                                with how its magnitude was established - a monitor
                                mass measured simultaneously and scaled by natural
                                abundance ratios, a production-rate factor measured
                                on a reference material or interference standard solution,
                                or a tailing factor measured on a pure standard. Name
                                the reference material used.
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
                              description: The isobaric, polyatomic and doubly charged
                                species that overlap the measured masses and are corrected
                                in data reduction - direct isobars, oxides and argides,
                                hydrides, and abundance-sensitivity tailing from an
                                adjacent large beam. Name each species and the mass
                                it affects.
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
                              title: Mass Resolution Assignment
                              description: Mass resolution mode used for acquisition.
                                One analyte may be acquired at more than one resolution,
                                so the assignment is per acquired mass rather than
                                per element. The overall mode(s) used in the procedure
                                are recorded in Mass Resolution Setting (Group 3).
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
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
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
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
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
                description: Duration of each individual laser pulse, including units.
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
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeIsotopePair
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeMixingRatio
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_multiRunSequentialAnalysisDesign
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_uncertaintyPropagationMethod
      allOf:
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_multiRunSequentialAnalysisDesign
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_uncertaintyPropagationMethod
        minContains: 0
        maxContains: 1
    ada:betweenSessionPrecision:
      description: "Precision of measurements across multiple analytical sessions
        over weeks to months \u2014 long-term or intermediate precision \u2014 and
        the method used to assess it. Report both the assessment method and the precision
        values, specifying the reference material, the number of measurements and
        sessions, the time span covered, and the statistic reported."
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
        - title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. The procedure may still state an acceptance threshold,
            which belongs with the inclusion criteria.
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
            with acceptable precision and accuracy. Required when concentrations near
            the LOD are reported.'
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
          title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. The procedure may still state an acceptance threshold,
            which belongs with the inclusion criteria.
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
            with acceptable precision and accuracy. Required when concentrations near
            the LOD are reported.'
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
    ada:isobaricInterferenceCorrectionsApplied:
      description: Whether mathematical corrections for isobaric, polyatomic or residual
        interferences are applied in data reduction, supplementary to any suppression
        already achieved by chemical separation, mass resolution, or a collision/reaction
        cell. Detail for each affected mass is carried by Interfering Species and
        Interference Correction Method.
      anyOf:
      - type: string
        enum:
        - "Yes \u2014 \u2078\u2077Rb on \u2078\u2077Sr, corrected from the \u2078\u2075Rb
          monitor"
        - "Yes \u2014 doubly-charged Er and Yb on the Sr and Rb masses"
        - No explicit corrections applied; medium resolution resolves the polyatomic
          interferences
        - N/A
        - None
        - missing
      - type: string
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
                measurable with acceptable precision and accuracy. Required when concentrations
                near the LOD are reported.'
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
            - title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One analyte
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
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
            - title: Instrument Sensitivity
              description: "Instrument sensitivity achieved in the session, with the
                isotope or channel it was measured on and the conditions it applies
                to. May be expressed either as detected signal per unit concentration
                or per unit mass of analyte delivered \u2014 counts per second per
                ppb, volts per ppm, counts per picogram \u2014 or as useful yield,
                the percentage of sampled atoms ultimately detected as ions, with
                the method used to derive it cited. A sensitivity the procedure requires
                before analyses may begin belongs with the tuning acceptance criteria."
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
                measurable with acceptable precision and accuracy. Required when concentrations
                near the LOD are reported.'
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
              title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One analyte
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
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
              title: Instrument Sensitivity
              description: "Instrument sensitivity achieved in the session, with the
                isotope or channel it was measured on and the conditions it applies
                to. May be expressed either as detected signal per unit concentration
                or per unit mass of analyte delivered \u2014 counts per second per
                ppb, volts per ppm, counts per picogram \u2014 or as useful yield,
                the percentage of sampled atoms ultimately detected as ions, with
                the method used to derive it cited. A sensitivity the procedure requires
                before analyses may begin belongs with the tuning acceptance criteria."
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
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_sampleFormAnalyticalSubstrate
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_sampleFormAnalyticalSubstrate
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
  - ada:analyticalAccuracy
  - ada:betweenSessionPrecision
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:isobaricInterferenceCorrectionsApplied
  - ada:massBiasCorrectionStrategy
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

