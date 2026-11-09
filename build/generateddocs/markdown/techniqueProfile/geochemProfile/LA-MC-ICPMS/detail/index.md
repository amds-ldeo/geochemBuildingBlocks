
# LA-MC-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Zhang2022
detail instance derived from Zhang et al. 2022 (At. Spectrosc. 43) Lunar meteorite silicates (Rb-Sr geochronology) Line scan (transect) fs-LA-MC-ICP-MS China Univ. of Geosciences.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
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
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.8,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Auxiliary: 0.80 l min⁻¹ Ar"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16.0,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Cool gas: 16.0 l min⁻¹ Ar"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1250,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1250 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/ICP-Source"
                },
                {
                  "schema:additionalType": [
                    "Collector",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycle",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycle"
                        }
                      ],
                      "schema:name": "Integration Time per Cycle",
                      "schema:value": 0.524,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "all: 0.524 s — one block of 120 cycles = 62.88 s total"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collector"
                },
                {
                  "schema:additionalType": [
                    "Collision Reaction Cell",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "Collision Reaction Cell",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N₂ added downstream"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/ΔM ≈ 400)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 50–60 µm circular",
              "ada:laserFluence": "~60% of maximum output (PHAROS system; exact J cm⁻² not converted)",
              "ada:laserRepetitionRate": "all: 10–30 Hz — varied based on Sr concentration in samples",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NHB-9, YY12-01 (natural clinopyroxenes); YG4301 (anorthite) — measured as unknowns for ⁸⁷Sr/⁸⁶Sr data quality evaluation; reference values in Table 2",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/Core/constantsReferenceValues",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/Core/constantsReferenceValues"
            }
          ],
          "schema:name": "Constants Reference Values",
          "schema:value": "⁸⁷Rb decay constant 1.393 ± 0.004 x 10⁻¹¹ yr⁻¹ (Nebel et al. 2011), p.1; ⁸⁸Sr/⁸⁶Sr = 8.37520933 for mass fractionation correction (p.4); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for the ⁸⁷Rb/⁸⁶Sr calculation (p.4); natural ⁸⁷Rb/⁸⁵Rb of 0.38571 cited for the interference-correction principle (p.1)"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurement",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurement"
            }
          ],
          "schema:name": "Number of Blocks per Measurement",
          "schema:value": 1,
          "schema:description": "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlock",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlock"
            }
          ],
          "schema:name": "Number of Cycles per Block",
          "schema:value": 120,
          "schema:description": "all: 120 — Table 1, 'Cycles of each block 120' (p.3)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 12,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar make-up (flow rate not separately stated); N₂ 12 ml min⁻¹ added via Y-connector downstream of signal-smoothing device"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 60,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "60–70 cycles × 0.524 s ≈ 31–37 s (final integrated signal window after discarding beginning and end cycles from 90 acquired cycles)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectLength",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectLength"
            }
          ],
          "schema:name": "Transect Length",
          "schema:value": 10597,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 2–6 µm s⁻¹ — varied based on Sr concentration in target minerals"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/signalSmoothing",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/signalSmoothing"
                  }
                ],
                "schema:name": "Signal Smoothing",
                "schema:value": "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability"
              },
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (two-volume cell)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China"
      },
      "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "all [⁸⁷Sr/⁸⁶Sr: relative error <0.2‰ where ⁸⁷Rb/⁸⁶Sr <1 (12 of 14 reference materials); ⁸⁷Rb/⁸⁶Sr: within ±3% for 11 glasses] — exceptions NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%), all within the stated ±3% criterion"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [⁸⁷Sr/⁸⁶Sr, ⁸⁷Rb/⁸⁶Sr: standard error at 95% confidence (USE) per individual run, dependent on signal intensity] — regression in Fig. 3; relative errors for ⁸⁷Rb/⁸⁶Sr ±3% for most reference glasses, and for ⁸⁷Sr/⁸⁶Sr <0.2‰ where ⁸⁷Rb/⁸⁶Sr <1"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Rb–Sr isochron age, initial ⁸⁷Sr/⁸⁶Sr: MSWD from IsoplotR; other: N — Table 3: NWA 10597 Normal group 24, SUIA group 1.5; NWA 6950 Normal group 21, SUIA group 1.5. The high Normal-group values are attributed to large dispersion, 'especially for the data with ⁸⁷Rb/⁸⁶Sr ranging from 0.05 to 0.15' measured in pyroxenes (p.7)"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08"
    }
  ],
  "ada:analyticalMode": [
    "Transect"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — runs in \"NWA 10597 and NWA 6950\" (p.3), counted by reduction group (\"Normal group n=36\", \"SUIA group n=244\", table p.7), not labelled; reference materials by name (NHB-9, YY12-01, YG4301, p.3)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:mappingArea": "missing",
  "ada:peakFlatness": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
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
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.8,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Auxiliary: 0.80 l min\u207b\u00b9 Ar"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16.0,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Cool gas: 16.0 l min\u207b\u00b9 Ar"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1250,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1250 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/ICP-Source"
                },
                {
                  "schema:additionalType": [
                    "Collector",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycle",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycle"
                        }
                      ],
                      "schema:name": "Integration Time per Cycle",
                      "schema:value": 0.524,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "all: 0.524 s \u2014 one block of 120 cycles = 62.88 s total"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collector"
                },
                {
                  "schema:additionalType": [
                    "Collision Reaction Cell",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "Collision Reaction Cell",
                  "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N\u2082 added downstream"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/\u0394M \u2248 400)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 50\u201360 \u00b5m circular",
              "ada:laserFluence": "~60% of maximum output (PHAROS system; exact J cm\u207b\u00b2 not converted)",
              "ada:laserRepetitionRate": "all: 10\u201330 Hz \u2014 varied based on Sr concentration in samples",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laMcicpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087\u20131096)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NHB-9, YY12-01 (natural clinopyroxenes); YG4301 (anorthite) \u2014 measured as unknowns for \u2078\u2077Sr/\u2078\u2076Sr data quality evaluation; reference values in Table 2",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/Core/constantsReferenceValues",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/Core/constantsReferenceValues"
            }
          ],
          "schema:name": "Constants Reference Values",
          "schema:value": "\u2078\u2077Rb decay constant 1.393 \u00b1 0.004 x 10\u207b\u00b9\u00b9 yr\u207b\u00b9 (Nebel et al. 2011), p.1; \u2078\u2078Sr/\u2078\u2076Sr = 8.37520933 for mass fractionation correction (p.4); \u2078\u2077Rb/\u2078\u2075Rb = 0.385706 and \u2078\u2076Sr/\u2078\u2078Sr = 0.119351 for the \u2078\u2077Rb/\u2078\u2076Sr calculation (p.4); natural \u2078\u2077Rb/\u2078\u2075Rb of 0.38571 cited for the interference-correction principle (p.1)"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurement",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/numberOfBlocksPerMeasurement"
            }
          ],
          "schema:name": "Number of Blocks per Measurement",
          "schema:value": 1,
          "schema:description": "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlock",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlock"
            }
          ],
          "schema:name": "Number of Cycles per Block",
          "schema:value": 120,
          "schema:description": "all: 120 \u2014 Table 1, 'Cycles of each block 120' (p.3)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 12,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar make-up (flow rate not separately stated); N\u2082 12 ml min\u207b\u00b9 added via Y-connector downstream of signal-smoothing device"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 60,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "60\u201370 cycles \u00d7 0.524 s \u2248 31\u201337 s (final integrated signal window after discarding beginning and end cycles from 90 acquired cycles)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectLength",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectLength"
            }
          ],
          "schema:name": "Transect Length",
          "schema:value": 10597,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 2\u20136 \u00b5m s\u207b\u00b9 \u2014 varied based on Sr concentration in target minerals"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/signalSmoothing",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/signalSmoothing"
                  }
                ],
                "schema:name": "Signal Smoothing",
                "schema:value": "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability"
              },
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (two-volume cell)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China"
      },
      "schema:description": "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "all [\u2078\u2077Sr/\u2078\u2076Sr: relative error <0.2\u2030 where \u2078\u2077Rb/\u2078\u2076Sr <1 (12 of 14 reference materials); \u2078\u2077Rb/\u2078\u2076Sr: within \u00b13% for 11 glasses] \u2014 exceptions NIST 610 (\u22122.97%), NIST 612 (+2.02%), ATHO-G (+2.89%), all within the stated \u00b13% criterion"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [\u2078\u2077Sr/\u2078\u2076Sr, \u2078\u2077Rb/\u2078\u2076Sr: standard error at 95% confidence (USE) per individual run, dependent on signal intensity] \u2014 regression in Fig. 3; relative errors for \u2078\u2077Rb/\u2078\u2076Sr \u00b13% for most reference glasses, and for \u2078\u2077Sr/\u2078\u2076Sr <0.2\u2030 where \u2078\u2077Rb/\u2078\u2076Sr <1"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Rb\u2013Sr isochron age, initial \u2078\u2077Sr/\u2078\u2076Sr: MSWD from IsoplotR; other: N \u2014 Table 3: NWA 10597 Normal group 24, SUIA group 1.5; NWA 6950 Normal group 21, SUIA group 1.5. The high Normal-group values are attributed to large dispersion, 'especially for the data with \u2078\u2077Rb/\u2078\u2076Sr ranging from 0.05 to 0.15' measured in pyroxenes (p.7)"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08"
    }
  ],
  "ada:analyticalMode": [
    "Transect"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 runs in \"NWA 10597 and NWA 6950\" (p.3), counted by reduction group (\"Normal group n=36\", \"SUIA group n=244\", table p.7), not labelled; reference materials by name (NHB-9, YY12-01, YG4301, p.3)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:mappingArea": "missing",
  "ada:peakFlatness": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laMcicpmsTAPP-detail-Zhang2022 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "all [⁸⁷Sr/⁸⁶Sr, ⁸⁷Rb/⁸⁶Sr: standard error at 95% confidence (USE) per individual run, dependent on signal intensity] — regression in Fig. 3; relative errors for ⁸⁷Rb/⁸⁶Sr ±3% for most reference glasses, and for ⁸⁷Sr/⁸⁶Sr <0.2‰ where ⁸⁷Rb/⁸⁶Sr <1" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "Rb–Sr isochron age, initial ⁸⁷Sr/⁸⁶Sr: MSWD from IsoplotR; other: N — Table 3: NWA 10597 Normal group 24, SUIA group 1.5; NWA 6950 Normal group 21, SUIA group 1.5. The high Normal-group values are attributed to large dispersion, 'especially for the data with ⁸⁷Rb/⁸⁶Sr ranging from 0.05 to 0.15' measured in pyroxenes (p.7)" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "all [⁸⁷Sr/⁸⁶Sr: relative error <0.2‰ where ⁸⁷Rb/⁸⁶Sr <1 (12 of 14 reference materials); ⁸⁷Rb/⁸⁶Sr: within ±3% for 11 glasses] — exceptions NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%), all within the stated ±3% criterion" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach>,
                                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section (two-volume cell)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:description "LA-MC-ICP-MS transect mode with Rb-Sr isotope ratio measurement; SUIA (Smallest Unit Isochron Age) data reduction strategy developed for heterogeneous minerals; signal-smoothing device used to reduce short-term variability" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "State Key Laboratory of Geological Processes and Mineral Resources, China Univ. Geosciences, Wuhan, China" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "ISO-Compass software (Zhang et al. 2020, J. Anal. At. Spectrom. 35, 1087–1096)" ;
                            ada:toolRole "dataReduction" ] ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "NHB-9, YY12-01 (natural clinopyroxenes); YG4301 (anorthite) — measured as unknowns for ⁸⁷Sr/⁸⁶Sr data quality evaluation; reference values in Table 2" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS>,
                        <https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System> ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Transect" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — runs in \"NWA 10597 and NWA 6950\" (p.3), counted by reduction group (\"Normal group n=36\", \"SUIA group n=244\", table p.7), not labelled; reference materials by name (NHB-9, YY12-01, YG4301, p.3)" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 .

<https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collector>,
        <https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:name "missing" .

<https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laMcicpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "~60% of maximum output (PHAROS system; exact J cm⁻² not converted)" ;
    ada:laserRepetitionRate "all: 10–30 Hz — varied based on Sr concentration in samples" ;
    ada:laserSpotGeometry "all: 50–60 µm circular" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "⁸⁷Rb decay constant 1.393 ± 0.004 x 10⁻¹¹ yr⁻¹ (Nebel et al. 2011), p.1; ⁸⁸Sr/⁸⁶Sr = 8.37520933 for mass fractionation correction (p.4); ⁸⁷Rb/⁸⁵Rb = 0.385706 and ⁸⁶Sr/⁸⁸Sr = 0.119351 for the ⁸⁷Rb/⁸⁶Sr calculation (p.4); natural ⁸⁷Rb/⁸⁵Rb of 0.38571 cited for the interference-correction principle (p.1)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Auxiliary: 0.80 l min⁻¹ Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Cool gas: 16.0 l min⁻¹ Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.6e+01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Cycles with 87Rb/86Sr >1 deleted (invalid Rb interference correction); cycles with 88Sr signal <0.2 V discarded (poor precision); SUIA method applied to heterogeneous minerals" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "NIST 610 used to optimize He/Ar gas flows, torch position, RF power, and source lens settings for max sensitivity and peak flatness; small N₂ added downstream" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar make-up (flow rate not separately stated); N₂ 12 ml min⁻¹ added via Y-connector downstream of signal-smoothing device" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 12 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low resolution (M/ΔM ≈ 400)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1250 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1250 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "60–70 cycles × 0.524 s ≈ 31–37 s (final integrated signal window after discarding beginning and end cycles from 90 acquired cycles)" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> a schema1:PropertyValue ;
    schema1:name "Signal Smoothing" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
    schema1:value "Signal-smoothing device used downstream from ablation cell (model not specified); significantly reduced short-term signal variability" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> a schema1:PropertyValue ;
    schema1:description "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size" ;
    schema1:name "Transect Length" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10597 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "all: 2–6 µm s⁻¹ — varied based on Sr concentration in target minerals" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 0.524 s — one block of 120 cycles = 62.88 s total" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5.24e-01 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:description "1 (Table 1, 'Block number 1'; p.3 'one block of 120 cycles')" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 120 — Table 1, 'Cycles of each block 120' (p.3)" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 120 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-MC-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              - title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatio
                  schema:name:
                    const: Collision/Reaction Gas Mixture Ratio
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              minContains: 0
              maxContains: 1
            - contains:
                title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              minContains: 0
              maxContains: 1
            - contains:
                title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatio
                  schema:name:
                    const: Collision/Reaction Gas Mixture Ratio
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
          prov:used:
            type: array
            items:
              type: object
              allOf:
              - if:
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
                        - type: object
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
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
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              anyOf:
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
                                              - title: Ion Counter Dead Time
                                                description: Dead time of the ion-counting
                                                  detector(s), used in the dead-time
                                                  correction applied to high count
                                                  rates. Distinct from pulse/analog
                                                  cross-calibration, which relates
                                                  the two detector modes rather than
                                                  correcting counting losses within
                                                  the pulse-counting mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/ionCounterDeadTime
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/ionCounterDeadTime
                                                  schema:name:
                                                    const: Ion Counter Dead Time
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
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Ion Counter Dead Time
                                                description: Dead time of the ion-counting
                                                  detector(s), used in the dead-time
                                                  correction applied to high count
                                                  rates. Distinct from pulse/analog
                                                  cross-calibration, which relates
                                                  the two detector modes rather than
                                                  correcting counting losses within
                                                  the pulse-counting mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/ionCounterDeadTime
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/ionCounterDeadTime
                                                  schema:name:
                                                    const: Ion Counter Dead Time
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
                                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
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
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                  allOf:
                                  - contains:
                                      title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    minContains: 0
                                    maxContains: 1
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
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
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
                          const: Sample preparation
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                            minContains: 0
                            maxContains: 1
                  - if:
                      properties:
                        schema:name:
                          const: Data processing
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
            type: string
        required:
        - ada:proceduralBlankLevel
      title: Analysis Events
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Analytical Accuracy
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Offset between measured and accepted values for secondary
                  reference materials, and the method used to assess it. Specify the
                  reference material and the source of its accepted values, the number
                  of analyses, and the quantities assessed. Report systematic biases
                  and their likely causes. Express the offset in the form appropriate
                  to what the procedure reports - percent relative bias for concentrations,
                  or deviation in delta or ratio units for isotopic quantities.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Between-Session Analytical Precision
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: "Precision of measurements across multiple analytical
                  sessions over weeks to months \u2014 long-term or intermediate precision
                  \u2014 and the method used to assess it. Report both the assessment
                  method and the precision values, specifying the reference material,
                  the number of measurements and sessions, the time span covered,
                  and the statistic reported."
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Within-Session Analytical Precision
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Precision of repeated measurements within a single analytical
                  session and the method used to assess it. Report both the assessment
                  method and the precision values. The assessment method must specify
                  the reference material or standard measured, the number of replicates
                  n, and the statistic reported (1s RSD, 2s RSD, 2SD, 2SE, 95% CI).
                  Distinct from the internal precision of a single measurement, which
                  derives from counting statistics over the cycles of that measurement
                  rather than from repeated analyses.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
            required:
            - dqv:value
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Accuracy
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Between-Session Analytical Precision
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Within-Session Analytical Precision
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/context.jsonld)

## Sources

* [LA-MC-ICPMS_TAPP_v13.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail`

