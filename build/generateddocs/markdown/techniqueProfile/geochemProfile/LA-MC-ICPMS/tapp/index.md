
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
        "schema:name": "Data acquisition",
        "schema:description": "Single pass — 'The routine data acquisition consisted of one block of 120 cycles (0.524 s integration time per cycle), with the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3). No second traversal or alternate configuration is described",
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
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Cycle level: the cycles at the beginning and end of ablation are discarded, leaving 60-70 of the 90 ablation cycles (p.3). Technical criteria (p.5): (a) data with ⁸⁷Rb/⁸⁶Sr > 1 deleted, the Rb interference correction being invalid above that; (b) data with ⁸⁸Sr signal < 0.2 V discarded for poor ⁸⁷Sr/⁸⁶Sr precision. Run level: runs with stable signals go to the Normal group, runs with large ⁸⁷Rb/⁸⁶Sr variation to the SUIA group (NWA 10597: 36 Normal, 6 SUIA; NWA 6950: 94 Normal, 21 SUIA). For NWA 6950 only data with initial ⁸⁷Sr/⁸⁶Sr of 0.7025-0.7035 were kept, those at 0.7072-0.7076 being from glasses and pyroxenes in or around black veins and interpreted as later-altered (p.8)"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/peakFlatnessMethodAndThreshold",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "peakFlatnessMethodAndThreshold",
            "schema:name": "Peak Flatness Method and Threshold",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Optimised during tuning on NIST 610 by adjusting the He and Ar gas flow rates, torch position, RF power and source lens settings 'for maximum sensitivity and optimum peak flatness' (p.3); no numerical acceptance threshold is stated"
          },
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
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "L4=⁸³Kr (gas background monitor, no target species); L3=¹⁶⁷Er²⁺ (interference monitor, no target species); L2=⁸⁴Sr (Sr); L1=⁸⁵Rb (Rb); C=⁸⁶Sr (Sr); H1=¹⁷³Yb²⁺ (interference monitor, no target species); H2=⁸⁷Sr (Sr); H3=⁸⁸Sr (Sr). Static multi-collection, one configuration throughout (Table 1 'Cup-configuration', p.2; array spans L4–H3, p.2)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupArrayConfiguration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupArrayConfiguration",
              "schema:name": "Faraday Cup Array Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Nine Faraday cups fitted with 10¹¹ Ω resistors, plus seven fixed electron multiplier ion counters; the Faraday collector array spans L4 to H3 (p.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing",
          "ada:collectorConfiguration": [
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "schema:defaultValue": "10¹¹ Ω on all nine Faraday cups (p.2)"
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
              "schema:defaultValue": "Low resolution for all eight monitored masses — 'the mass spectrometer was operated in low mass resolution mode' (p.3); Table 1 'Instrument resolution ~ 400 (low mode)'. Single acquisition pass, so one assignment applies throughout"
            }
          ]
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Not installed — 'traditional (MC-)ICP-MS without the reaction/collision cell' (p.1); contrasted against 'MC-ICP-MS with collision cell' in the conclusion (pp.8-9)",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Laser-off cycles at the start of the same block — 'the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3); 30 cycles x 0.524 s ≈ 15.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/massFractionationLaw",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "massFractionationLaw",
      "schema:name": "Mass Fractionation Law",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Exponential"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfBlocksPerMeasurementDefault",
      "schema:name": "Number of Blocks per Measurement",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlockDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfCyclesPerBlockDefault",
      "schema:name": "Number of Cycles per Block",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 120,
      "schema:description": "120 (Table 1, 'Cycles of each block 120'; p.3)"
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
      "@id": "ada:parameter/laMcicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min⁻¹ (two-volume cell)",
  "ada:constantsAndReferenceValuesUsedDefault": "⁸⁷Rb decay constant 1.393 ± 0.004 x 10⁻¹¹ yr⁻¹ (Nebel et al. 2011), p.1; ⁸⁸Sr/⁸⁶Sr = 8.37520933 for mass fractionation correction (p.4); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for the ⁸⁷Rb/⁸⁶Sr calculation (p.4); natural ⁸⁷Rb/⁸⁵Rb of 0.38571 cited for the interference-correction principle (p.1)",
  "ada:isobaricInterferenceCorrectionsApplied": "Yes — correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law)",
  "ada:massBiasCorrectionStrategy": "Internal normalisation to an assumed ⁸⁸Sr/⁸⁶Sr = 8.37520933 applying the exponential law (Russell et al. 1978), after interference correction (p.4). The ⁸⁷Rb isobaric correction on ⁸⁷Sr uses the ⁸⁵Rb signal and a user-specified ⁸⁷Rb/⁸⁵Rb, also via the exponential law, with that ratio calibrated by measuring reference materials of known ⁸⁷Sr/⁸⁶Sr (p.4)",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Random selection among the target phases — 'The plagioclases, pyroxenes, and ilmenites in NWA 10597 were measured randomly' (p.7); target phases are plagioclase, pyroxene, ilmenite and glass (abstract; p.7-8)",
  "ada:withinSessionPrecision": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1",
  "ada:numberOfAcquisitionPasses": "1",
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
  "ada:samplingUnit": "Analysis point — one individual run, a continuous line scan within a single mineral grain or glass; the paper counts and reports 'individual runs' (36 and 6 for NWA 10597; 94 and 21 for NWA 6950), pp.7-8",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)"
    }
  ],
  "ada:analyticalMode": [
    "Transect"
  ],
  "ada:reportedProperties": [
    "⁸⁷Sr/⁸⁶Sr (dimensionless ratio); ⁸⁷Rb/⁸⁶Sr (dimensionless ratio); Rb–Sr isochron age (Ma); initial ⁸⁷Sr/⁸⁶Sr (dimensionless ratio) — Tables 2 and 3"
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan at 2–6 µm s⁻¹)"
  ],
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:sampleIntroduction": "He filled into the two-volume ablation cell; Ar mixed into the sample-out line downstream of the ablation chamber before the torch; a signal-smoothing device downstream of the sample cell (Hu et al. 2015) that 'significantly reduced the short-term variability of the signal'; 12 ml min⁻¹ N₂ added to the carrier gas via a simple Y connector behind the signal-smoothing device (p.3)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "Sr, ⁸⁸Sr/⁸⁶Sr = 8.37520933, exponential law (Russell et al. 1978), p.4",
  "ada:uncertaintyLevel": "2SD for reference-material mean values (Table 2); within-run repeatability quoted as U_SD and U_SE at 95% confidence (Eqs. 1-2, p.5); isochron ages quoted with IsoplotR and Monte Carlo uncertainties (Table 3)",
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr⁺ signals removed by correction; no additional Kr peak stripping applied",
  "ada:internalStandardElement": "No conventional IS; ⁸⁵Rb used to calculate ⁸⁷Rb/⁸⁶Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
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
        "schema:name": "Data acquisition",
        "schema:description": "Single pass \u2014 'The routine data acquisition consisted of one block of 120 cycles (0.524 s integration time per cycle), with the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3). No second traversal or alternate configuration is described",
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
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Cycle level: the cycles at the beginning and end of ablation are discarded, leaving 60-70 of the 90 ablation cycles (p.3). Technical criteria (p.5): (a) data with \u2078\u2077Rb/\u2078\u2076Sr > 1 deleted, the Rb interference correction being invalid above that; (b) data with \u2078\u2078Sr signal < 0.2 V discarded for poor \u2078\u2077Sr/\u2078\u2076Sr precision. Run level: runs with stable signals go to the Normal group, runs with large \u2078\u2077Rb/\u2078\u2076Sr variation to the SUIA group (NWA 10597: 36 Normal, 6 SUIA; NWA 6950: 94 Normal, 21 SUIA). For NWA 6950 only data with initial \u2078\u2077Sr/\u2078\u2076Sr of 0.7025-0.7035 were kept, those at 0.7072-0.7076 being from glasses and pyroxenes in or around black veins and interpreted as later-altered (p.8)"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/peakFlatnessMethodAndThreshold",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "peakFlatnessMethodAndThreshold",
            "schema:name": "Peak Flatness Method and Threshold",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "Optimised during tuning on NIST 610 by adjusting the He and Ar gas flow rates, torch position, RF power and source lens settings 'for maximum sensitivity and optimum peak flatness' (p.3); no numerical acceptance threshold is stated"
          },
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
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "L4=\u2078\u00b3Kr (gas background monitor, no target species); L3=\u00b9\u2076\u2077Er\u00b2\u207a (interference monitor, no target species); L2=\u2078\u2074Sr (Sr); L1=\u2078\u2075Rb (Rb); C=\u2078\u2076Sr (Sr); H1=\u00b9\u2077\u00b3Yb\u00b2\u207a (interference monitor, no target species); H2=\u2078\u2077Sr (Sr); H3=\u2078\u2078Sr (Sr). Static multi-collection, one configuration throughout (Table 1 'Cup-configuration', p.2; array spans L4\u2013H3, p.2)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupArrayConfiguration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupArrayConfiguration",
              "schema:name": "Faraday Cup Array Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Nine Faraday cups fitted with 10\u00b9\u00b9 \u03a9 resistors, plus seven fixed electron multiplier ion counters; the Faraday collector array spans L4 to H3 (p.2)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing",
          "ada:collectorConfiguration": [
            {
              "@id": "ada:channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "schema:defaultValue": "10\u00b9\u00b9 \u03a9 on all nine Faraday cups (p.2)"
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
              "schema:defaultValue": "Low resolution for all eight monitored masses \u2014 'the mass spectrometer was operated in low mass resolution mode' (p.3); Table 1 'Instrument resolution ~ 400 (low mode)'. Single acquisition pass, so one assignment applies throughout"
            }
          ]
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Not installed \u2014 'traditional (MC-)ICP-MS without the reaction/collision cell' (p.1); contrasted against 'MC-ICP-MS with collision cell' in the conclusion (pp.8-9)",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Laser-off cycles at the start of the same block \u2014 'the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3); 30 cycles x 0.524 s \u2248 15.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/massFractionationLaw",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "massFractionationLaw",
      "schema:name": "Mass Fractionation Law",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Exponential"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfBlocksPerMeasurementDefault",
      "schema:name": "Number of Blocks per Measurement",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlockDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfCyclesPerBlockDefault",
      "schema:name": "Number of Cycles per Block",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 120,
      "schema:description": "120 (Table 1, 'Cycles of each block 120'; p.3)"
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
      "@id": "ada:parameter/laMcicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "Single line scan per location (1 block of 120 cycles at 0.524 s integration)"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He, 0.90 l min\u207b\u00b9 (two-volume cell)",
  "ada:constantsAndReferenceValuesUsedDefault": "\u2078\u2077Rb decay constant 1.393 \u00b1 0.004 x 10\u207b\u00b9\u00b9 yr\u207b\u00b9 (Nebel et al. 2011), p.1; \u2078\u2078Sr/\u2078\u2076Sr = 8.37520933 for mass fractionation correction (p.4); \u2078\u2077Rb/\u2078\u2075Rb = 0.385706 and \u2078\u2076Sr/\u2078\u2078Sr = 0.119351 for the \u2078\u2077Rb/\u2078\u2076Sr calculation (p.4); natural \u2078\u2077Rb/\u2078\u2075Rb of 0.38571 cited for the interference-correction principle (p.1)",
  "ada:isobaricInterferenceCorrectionsApplied": "Yes \u2014 correction for doubly charged ions: \u00b9\u2076\u2078Er\u00b2\u207a on \u2078\u2074Sr; \u00b9\u2077\u2070Er\u00b2\u207a and \u00b9\u2077\u2070Yb\u00b2\u207a on \u2078\u2075Rb; \u00b9\u2077\u00b2Yb\u00b2\u207a on \u2078\u2076Sr; \u00b9\u2077\u2074Yb\u00b2\u207a on \u2078\u2077Sr; \u2078\u2077Rb isobaric on \u2078\u2077Sr (corrected using 85Rb signal and exponential law)",
  "ada:massBiasCorrectionStrategy": "Internal normalisation to an assumed \u2078\u2078Sr/\u2078\u2076Sr = 8.37520933 applying the exponential law (Russell et al. 1978), after interference correction (p.4). The \u2078\u2077Rb isobaric correction on \u2078\u2077Sr uses the \u2078\u2075Rb signal and a user-specified \u2078\u2077Rb/\u2078\u2075Rb, also via the exponential law, with that ratio calibrated by measuring reference materials of known \u2078\u2077Sr/\u2078\u2076Sr (p.4)",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Random selection among the target phases \u2014 'The plagioclases, pyroxenes, and ilmenites in NWA 10597 were measured randomly' (p.7); target phases are plagioclase, pyroxene, ilmenite and glass (abstract; p.7-8)",
  "ada:withinSessionPrecision": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: \u00b13% for most reference glasses; 87Sr/86Sr relative errors: <0.2\u2030 for materials with 87Rb/86Sr <1",
  "ada:numberOfAcquisitionPasses": "1",
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
  "ada:samplingUnit": "Analysis point \u2014 one individual run, a continuous line scan within a single mineral grain or glass; the paper counts and reports 'individual runs' (36 and 6 for NWA 10597; 94 and 21 for NWA 6950), pp.7-8",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087\u20131096)"
    }
  ],
  "ada:analyticalMode": [
    "Transect"
  ],
  "ada:reportedProperties": [
    "\u2078\u2077Sr/\u2078\u2076Sr (dimensionless ratio); \u2078\u2077Rb/\u2078\u2076Sr (dimensionless ratio); Rb\u2013Sr isochron age (Ma); initial \u2078\u2077Sr/\u2078\u2076Sr (dimensionless ratio) \u2014 Tables 2 and 3"
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan at 2\u20136 \u00b5m s\u207b\u00b9)"
  ],
  "ada:internalStandardApproach": "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)",
  "ada:sampleIntroduction": "He filled into the two-volume ablation cell; Ar mixed into the sample-out line downstream of the ablation chamber before the torch; a signal-smoothing device downstream of the sample cell (Hu et al. 2015) that 'significantly reduced the short-term variability of the signal'; 12 ml min\u207b\u00b9 N\u2082 added to the carrier gas via a simple Y connector behind the signal-smoothing device (p.3)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "Sr, \u2078\u2078Sr/\u2078\u2076Sr = 8.37520933, exponential law (Russell et al. 1978), p.4",
  "ada:uncertaintyLevel": "2SD for reference-material mean values (Table 2); within-run repeatability quoted as U_SD and U_SE at 95% confidence (Eqs. 1-2, p.5); isochron ages quoted with IsoplotR and Monte Carlo uncertainties (Table 3)",
  "ada:blankBackgroundCorrectionMethod": "First 30 cycles (no laser ablation) used for background collection; background Kr\u207a signals removed by correction; no additional Kr peak stripping applied",
  "ada:internalStandardElement": "No conventional IS; \u2078\u2075Rb used to calculate \u2078\u2077Rb/\u2078\u2076Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses",
  "ada:signalIntegrationIntervalMethod": "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle",
  "ada:secondaryReferenceMaterialDefault": [
    "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 \u2014 measured as unknowns for 87Sr/86Sr data quality evaluation"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of \u2078\u2077Rb/\u2078\u2076Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for \u2078\u2077Sr/\u2078\u2076Sr data quality evaluation",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:betweenSessionPrecision": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Single pass — 'The routine data acquisition consisted of one block of 120 cycles (0.524 s integration time per cycle), with the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3). No second traversal or alternate configuration is described" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> ;
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
    schema1:object [ schema1:name "Lunar meteorite silicates (plagioclase, pyroxene, ilmenite, glass)" ],
        [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zhang et al. (2022) At. Spectrosc. 43; ISO-Compass software; Zhang et al. (2018)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Transect (continuous line scan at 2–6 µm s⁻¹)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "14 reference glasses analyzed to evaluate accuracy and provide calibration factors; natural minerals as unknowns for data quality evaluation; 1 block of 120 cycles per analysis" ;
    ada:analyticalAccuracy "87Sr/86Sr relative errors <0.2‰ for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within ±3% for 11 glasses; exceptions: NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) — all within stated ±3% criterion" ;
    ada:analyticalMode "Transect" ;
    ada:backgroundCountTimeDefault "30 cycles × 0.524 s ≈ 15.7 s (first 30 cycles of the 120-cycle block with no laser ablation)" ;
    ada:betweenSessionPrecision "missing" ;
    ada:blankBackgroundCorrectionMethod "First 30 cycles (no laser ablation) used for background collection; background Kr⁺ signals removed by correction; no additional Kr peak stripping applied" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He, 0.90 l min⁻¹ (two-volume cell)" ;
    ada:constantsAndReferenceValuesUsedDefault "⁸⁷Rb decay constant 1.393 ± 0.004 x 10⁻¹¹ yr⁻¹ (Nebel et al. 2011), p.1; ⁸⁸Sr/⁸⁶Sr = 8.37520933 for mass fractionation correction (p.4); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for the ⁸⁷Rb/⁸⁶Sr calculation (p.4); natural ⁸⁷Rb/⁸⁵Rb of 0.38571 cited for the interference-correction principle (p.1)" ;
    ada:elementalFractionationCorrection "Femtosecond laser substantially reduces elemental fractionation; no explicit downhole correction; Rb/Sr elemental fractionation corrected externally by analyzing series of reference glasses; exponential law for Sr isotope mass bias (88Sr/86Sr = 8.37521)" ;
    ada:internalNormalizationElementAndIsotopeRatio "Sr, ⁸⁸Sr/⁸⁶Sr = 8.37520933, exponential law (Russell et al. 1978), p.4" ;
    ada:internalStandardApproach "No conventional IS; external calibration only (Rb/Sr elemental fractionation corrected by series of reference glasses; 87Sr/86Sr mass bias corrected by exponential law using 88Sr/86Sr = 8.37521)" ;
    ada:internalStandardElement "No conventional IS; ⁸⁵Rb used to calculate ⁸⁷Rb/⁸⁶Sr via 87Rb/85Rb; external calibration for Rb/Sr elemental fractionation using reference glasses" ;
    ada:isobaricInterferenceCorrectionsApplied "Yes — correction for doubly charged ions: ¹⁶⁸Er²⁺ on ⁸⁴Sr; ¹⁷⁰Er²⁺ and ¹⁷⁰Yb²⁺ on ⁸⁵Rb; ¹⁷²Yb²⁺ on ⁸⁶Sr; ¹⁷⁴Yb²⁺ on ⁸⁷Sr; ⁸⁷Rb isobaric on ⁸⁷Sr (corrected using 85Rb signal and exponential law)" ;
    ada:massBiasCorrectionStrategy "Internal normalisation to an assumed ⁸⁸Sr/⁸⁶Sr = 8.37520933 applying the exponential law (Russell et al. 1978), after interference correction (p.4). The ⁸⁷Rb isobaric correction on ⁸⁷Sr uses the ⁸⁵Rb signal and a user-specified ⁸⁷Rb/⁸⁵Rb, also via the exponential law, with that ratio calibrated by measuring reference materials of known ⁸⁷Sr/⁸⁶Sr (p.4)" ;
    ada:numberOfAcquisitionPasses "1" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 for instrument parameter optimization; series of reference glasses (NIST 612, BHVO-2G, BCR-2G, NKT-1G, TB-1G, ATHO-G, KL2-G, ML3B-G, StHs6/80-G, T1-G) for external calibration of ⁸⁷Rb/⁸⁶Sr ratio; natural clinopyroxenes (NHB-9, YY12-01) and anorthite (YG4301) as unknown samples for ⁸⁷Sr/⁸⁶Sr data quality evaluation" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:reportedProperties "⁸⁷Sr/⁸⁶Sr (dimensionless ratio); ⁸⁷Rb/⁸⁶Sr (dimensionless ratio); Rb–Sr isochron age (Ma); initial ⁸⁷Sr/⁸⁶Sr (dimensionless ratio) — Tables 2 and 3" ;
    ada:sampleIntroduction "He filled into the two-volume ablation cell; Ar mixed into the sample-out line downstream of the ablation chamber before the torch; a signal-smoothing device downstream of the sample cell (Hu et al. 2015) that 'significantly reduced the short-term variability of the signal'; 12 ml min⁻¹ N₂ added to the carrier gas via a simple Y connector behind the signal-smoothing device (p.3)" ;
    ada:samplingUnit "Analysis point — one individual run, a continuous line scan within a single mineral grain or glass; the paper counts and reports 'individual runs' (36 and 6 for NWA 10597; 94 and 21 for NWA 6950), pp.7-8" ;
    ada:samplingUnitSelectionCriteriaDefault "Random selection among the target phases — 'The plagioclases, pyroxenes, and ilmenites in NWA 10597 were measured randomly' (p.7); target phases are plagioclase, pyroxene, ilmenite and glass (abstract; p.7-8)" ;
    ada:secondaryReferenceMaterialDefault "Natural clinopyroxenes NHB-9 and YY12-01 (reference values given in Table 2); anorthite YG4301 — measured as unknowns for 87Sr/86Sr data quality evaluation" ;
    ada:signalIntegrationIntervalMethod "Regions of integration for gas background and sample signal selected first; cycles at beginning and end of ablation discarded; for heterogeneous minerals (unstable 87Rb/86Sr): SUIA (Smallest Unit Isochron Age) data reduction strategy applied per cycle" ;
    ada:uncertaintyLevel "2SD for reference-material mean values (Table 2); within-run repeatability quoted as U_SD and U_SE at 95% confidence (Eqs. 1-2, p.5); isochron ages quoted with IsoplotR and Monte Carlo uncertainties (Table 3)" ;
    ada:withinSessionPrecision "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1" ;
    bios:computationalTool [ schema1:name "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/channelColumn/laMcicpmsTAPP/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10¹¹ Ω on all nine Faraday cups (p.2)" ;
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
    schema1:defaultValue "Low resolution for all eight monitored masses — 'the mass spectrometer was operated in low mass resolution mode' (p.3); Table 1 'Instrument resolution ~ 400 (low mode)'. Single acquisition pass, so one assignment applies throughout" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:value "Cycle level: the cycles at the beginning and end of ablation are discarded, leaving 60-70 of the 90 ablation cycles (p.3). Technical criteria (p.5): (a) data with ⁸⁷Rb/⁸⁶Sr > 1 deleted, the Rb interference correction being invalid above that; (b) data with ⁸⁸Sr signal < 0.2 V discarded for poor ⁸⁷Sr/⁸⁶Sr precision. Run level: runs with stable signals go to the Normal group, runs with large ⁸⁷Rb/⁸⁶Sr variation to the SUIA group (NWA 10597: 36 Normal, 6 SUIA; NWA 6950: 94 Normal, 21 SUIA). For NWA 6950 only data with initial ⁸⁷Sr/⁸⁶Sr of 0.7025-0.7035 were kept, those at 0.7072-0.7076 being from glasses and pyroxenes in or around black veins and interpreted as later-altered (p.8)" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

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

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "Laser-off cycles at the start of the same block — 'the first 30 cycles for background collection (no laser ablation) and the remaining 90 cycles for signal collection' (p.3); 30 cycles x 0.524 s ≈ 15.7 s" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Array Configuration" ;
    schema1:value "Nine Faraday cups fitted with 10¹¹ Ω resistors, plus seven fixed electron multiplier ion counters; the Faraday collector array spans L4 to H3 (p.2)" ;
    schema1:valueName "faradayCupArrayConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Fractionation Law" ;
    schema1:value "Exponential" ;
    schema1:valueName "massFractionationLaw" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:valueName "numberOfBlocksPerMeasurementDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 120 ;
    schema1:description "120 (Table 1, 'Cycles of each block 120'; p.3)" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> a schema1:PropertyValueSpecification ;
    schema1:name "Peak Flatness Method and Threshold" ;
    schema1:value "Optimised during tuning on NIST 610 by adjusting the He and Ar gas flow rates, torch position, RF power and source lens settings 'for maximum sensitivity and optimum peak flatness' (p.3); no numerical acceptance threshold is stated" ;
    schema1:valueName "peakFlatnessMethodAndThreshold" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field (MC-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific NEPTUNE Plus (MC-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "L4=⁸³Kr (gas background monitor, no target species); L3=¹⁶⁷Er²⁺ (interference monitor, no target species); L2=⁸⁴Sr (Sr); L1=⁸⁵Rb (Rb); C=⁸⁶Sr (Sr); H1=¹⁷³Yb²⁺ (interference monitor, no target species); H2=⁸⁷Sr (Sr); H3=⁸⁸Sr (Sr). Static multi-collection, one configuration throughout (Table 1 'Cup-configuration', p.2; array spans L4–H3, p.2)" ;
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
    schema1:name "Not installed — 'traditional (MC-)ICP-MS without the reaction/collision cell' (p.1); contrasted against 'MC-ICP-MS with collision cell' in the conclusion (pp.8-9)" .

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

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/interPassDataDependency> ;
    schema1:value "Single line scan per location (1 block of 120 cycles at 0.524 s integration)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP)
description: Laser-ablation multi-collector ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/LA-MC-ICPMS_TAPP_v78.csv via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
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
                                cycle (seconds).
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
                            - title: Ion Counter Dead Time
                              description: Dead time of the ion-counting detector(s),
                                used in the dead-time correction applied to high count
                                rates. Distinct from pulse/analog cross-calibration,
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
                              description: Mass resolution mode used for acquisition.
                                One target species may be acquired at more than one
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
                                cycle (seconds).
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
                              title: Ion Counter Dead Time
                              description: Dead time of the ion-counting detector(s),
                                used in the dead-time correction applied to high count
                                rates. Distinct from pulse/analog cross-calibration,
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
                              description: Mass resolution mode used for acquisition.
                                One target species may be acquired at more than one
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
                required:
                - schema:name
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
            required:
            - ada:laserPulseDuration
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
        - title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/laMcicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/reactionProductIonMassShiftTransition
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
        - title: Inter-Pass Data Dependency
          description: "Which earlier acquisition pass supplied inputs to this one,
            and what those inputs are \u2014 for example a concentration measured
            in one pass and used as the internal standard for a later pass on the
            same location. Records the dependency only; the settings of each pass
            are carried by the fields keyed by acquisition pass, and the passes themselves
            are enumerated by Acquisition Pass. Leave empty for a pass that consumes
            no earlier output. Not applicable to raster mapping, where each spatial
            location is visited exactly once."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/interPassDataDependency
            schema:name:
              const: Inter-Pass Data Dependency
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
          title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/laMcicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/reactionProductIonMassShiftTransition
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
      - contains:
          title: Inter-Pass Data Dependency
          description: "Which earlier acquisition pass supplied inputs to this one,
            and what those inputs are \u2014 for example a concentration measured
            in one pass and used as the internal standard for a later pass on the
            same location. Records the dependency only; the settings of each pass
            are carried by the fields keyed by acquisition pass, and the passes themselves
            are enumerated by Acquisition Pass. Leave empty for a pass that consumes
            no earlier output. Not applicable to raster mapping, where each spatial
            location is visited exactly once."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/interPassDataDependency
            schema:name:
              const: Inter-Pass Data Dependency
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
    ada:massBiasCorrectionStrategy:
      description: 'Strategy used to correct instrumental isotopic mass fractionation,
        also called mass bias or mass discrimination. Distinct from Elemental Fractionation
        Correction, which addresses inter-element fractionation during ablation and
        transport: this field addresses discrimination between isotopes of the same
        element, and applies wherever the procedure reports isotope ratios.'
      type: string
      readOnly: true
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
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
                  const: ada:analyteColumn/laMcicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:analyteColumn/laMcicpmsTAPP/countingStatisticsError
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
                  const: ada:analyteColumn/laMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
              title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
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
                  const: ada:analyteColumn/laMcicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:analyteColumn/laMcicpmsTAPP/countingStatisticsError
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
                  const: ada:analyteColumn/laMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
    ada:numberOfAcquisitionPasses:
      description: Number of acquisition passes the procedure runs. A count of the
        passes enumerated in Acquisition Pass, recorded separately so multi-pass procedures
        are findable without parsing that field.
      anyOf:
      - type: integer
      - type: string
      readOnly: true
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
  - ada:numberOfAcquisitionPasses

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
    "nxs": "https://manual.nexusformat.org/classes/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
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

