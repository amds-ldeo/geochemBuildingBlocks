
# Solution Q-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Gao2008
detail instance derived from Hu+Gao2008 | PerkinElmer ELAN 6100 DRC | NWU Xi'an.
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
  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 190,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "bomb attack: 190 °C; re-dissolution: 150 °C — §3.3"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "bomb attack: 48 h; re-dissolution: overnight — §3.3"
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
            "schema:description": "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard — clean-room conditions (§3.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "50 mg (stated section 3.3)"
            }
          ],
          "schema:name": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 0.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.20 ml/min (stated section 3.1)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 3.1,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "N — 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (§3.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1350,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1350 W (stated section 3.1)"
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
                      "schema:value": 14,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
                    },
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
                      "schema:value": 1.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "Ce2+/Ce+ — §3.1"
                },
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Production",
                  "schema:value": "Ce2+/Ce+ below 2.5% — §3.1"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
                },
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
                  "schema:value": "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 — five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (§3.4)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Li: 0.036 ± 0.028; Be: 0.00091 ± 0.00049; B: 0.39 ± 0.26; Sc: 0.033 ± 0.011; V: 0.50 ± 0.38; Cr: 0.53 ± 0.16; Co: 0.0046 ± 0.0032; Ni: 0.065 ± 0.037; Cu: 0.072 ± 0.022; Zn: 0.80 ± 0.56; Ga: 0.0037 ± 0.0020; Ge: 0.0081 ± 0.0040; As: 0.021 ± 0.009; Rb: 0.11 ± 0.05; Sr: 0.018 ± 0.018; Y: 0.0018 ± 0.0017; Zr: 0.0030 ± 0.0015; Nb: 0.0012 ± 0.0012; Mo: 0.035 ± 0.030; Cd: 0.0026 ± 0.0015; In: 0.00016 ± 0.00004; Sn: 0.0083 ± 0.0016; Sb: 0.010 ± 0.006; Te: 0.00097 ± 0.00014; Cs: 0.00060 ± 0.00034; Ba: 0.075 ± 0.063; La: 0.0025 ± 0.0020; Ce: 0.0028 ± 0.0016; Pr: 0.00056 ± 0.00042; Nd: 0.0019 ± 0.0017; Sm: 0.00079 ± 0.00036; Eu: 0.00023 ± 0.00014; Gd: 0.00063 ± 0.00054; Tb: 0.00013 ± 0.00005; Dy: 0.00058 ± 0.00038; Ho: 0.00013 ± 0.00008; Er: 0.00027 ± 0.00020; Tm: 0.00011 ± 0.00003; Yb: 0.00043 ± 0.00025; Lu: 0.00015 ± 0.00007; Hf: 0.0010 ± 0.0012; Ta: 0.00017 ± 0.00009; W: 0.023 ± 0.010; Tl: 0.0026 ± 0.0009; Pb: 0.043 ± 0.020; Bi: 0.00049 ± 0.00028; Th: 0.00062 ± 0.00050; U: 0.00027 ± 0.00025 — ppb, mean ± STD of n = 5 blanks (Table 2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)"
      },
      "schema:description": "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As — §3.1, §3.2, §3.3",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4–7 analyses, usually <8%] — Table 2 and §3.4; whether the replicates share a session is not stated"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] — Tables 2 and 3, §3.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD, relative standard deviation in percent — Table 2: 'The RSD is the relative standard deviation in percent'"
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnitName": "Sample name only — Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 190,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "bomb attack: 190 \u00b0C; re-dissolution: 150 \u00b0C \u2014 \u00a73.3"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "bomb attack: 48 h; re-dissolution: overnight \u2014 \u00a73.3"
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
            "schema:description": "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard \u2014 clean-room conditions (\u00a73.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "50 mg (stated section 3.3)"
            }
          ],
          "schema:name": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 0.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.20 ml/min (stated section 3.1)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 3.1,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "N \u2014 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (\u00a73.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1350,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1350 W (stated section 3.1)"
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
                      "schema:value": 14,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "14 L/min (outer ICP gas; stated section 3.1)"
                    },
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
                      "schema:value": 1.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.2 L/min (intermediate gas; stated section 3.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "Ce2+/Ce+ \u2014 \u00a73.1"
                },
                {
                  "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Production",
                  "schema:value": "Ce2+/Ce+ below 2.5% \u2014 \u00a73.1"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)"
                },
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
                  "schema:value": "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 \u2014 five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (\u00a73.4)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Li: 0.036 \u00b1 0.028; Be: 0.00091 \u00b1 0.00049; B: 0.39 \u00b1 0.26; Sc: 0.033 \u00b1 0.011; V: 0.50 \u00b1 0.38; Cr: 0.53 \u00b1 0.16; Co: 0.0046 \u00b1 0.0032; Ni: 0.065 \u00b1 0.037; Cu: 0.072 \u00b1 0.022; Zn: 0.80 \u00b1 0.56; Ga: 0.0037 \u00b1 0.0020; Ge: 0.0081 \u00b1 0.0040; As: 0.021 \u00b1 0.009; Rb: 0.11 \u00b1 0.05; Sr: 0.018 \u00b1 0.018; Y: 0.0018 \u00b1 0.0017; Zr: 0.0030 \u00b1 0.0015; Nb: 0.0012 \u00b1 0.0012; Mo: 0.035 \u00b1 0.030; Cd: 0.0026 \u00b1 0.0015; In: 0.00016 \u00b1 0.00004; Sn: 0.0083 \u00b1 0.0016; Sb: 0.010 \u00b1 0.006; Te: 0.00097 \u00b1 0.00014; Cs: 0.00060 \u00b1 0.00034; Ba: 0.075 \u00b1 0.063; La: 0.0025 \u00b1 0.0020; Ce: 0.0028 \u00b1 0.0016; Pr: 0.00056 \u00b1 0.00042; Nd: 0.0019 \u00b1 0.0017; Sm: 0.00079 \u00b1 0.00036; Eu: 0.00023 \u00b1 0.00014; Gd: 0.00063 \u00b1 0.00054; Tb: 0.00013 \u00b1 0.00005; Dy: 0.00058 \u00b1 0.00038; Ho: 0.00013 \u00b1 0.00008; Er: 0.00027 \u00b1 0.00020; Tm: 0.00011 \u00b1 0.00003; Yb: 0.00043 \u00b1 0.00025; Lu: 0.00015 \u00b1 0.00007; Hf: 0.0010 \u00b1 0.0012; Ta: 0.00017 \u00b1 0.00009; W: 0.023 \u00b1 0.010; Tl: 0.0026 \u00b1 0.0009; Pb: 0.043 \u00b1 0.020; Bi: 0.00049 \u00b1 0.00028; Th: 0.00062 \u00b1 0.00050; U: 0.00027 \u00b1 0.00025 \u2014 ppb, mean \u00b1 STD of n = 5 blanks (Table 2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)"
      },
      "schema:description": "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As \u2014 \u00a73.1, \u00a73.2, \u00a73.3",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4\u20137 analyses, usually <8%] \u2014 Table 2 and \u00a73.4; whether the replicates share a session is not stated"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] \u2014 Tables 2 and 3, \u00a73.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD, relative standard deviation in percent \u2014 Table 2: 'The RSD is the relative standard deviation in percent'"
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnitName": "Sample name only \u2014 Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-Gao2008 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4–7 analyses, usually <8%] — Table 2 and §3.4; whether the replicates share a session is not stated" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] — Tables 2 and 3, §3.4" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD, relative standard deviation in percent — Table 2: 'The RSD is the relative standard deviation in percent'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Fifty milligrams of rock powder digested in a sealed PTFE-lined stainless steel bomb, taken up and made up to 50 ml with ultra-pure water and Rh internal standard — clean-room conditions (§3.3); for As and Te, 4.80 ml of sample solution plus 0.20 ml ethanol" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:description "Auto lens voltages optimised on a 10 ng/ml Mg, Co, Rh, Ce, Pb and U solution; As and Te measured in 4.80 ml sample solution plus 0.20 ml ethanol; HF boiled before sub-boiling distillation to remove volatile As — §3.1, §3.2, §3.3" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "State Key Laboratory of Continental Dynamics, Northwest University, Xi'an (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "AGV-1, BHVO-1, G-2, GSR-5, SCO-1, JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 — five in Table 2 for accuracy and precision; eighteen more in Table 3 for Mo, Cd, In, Sn, Sb, W, Tl, Bi, As and Te (§3.4)" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Li: 0.036 ± 0.028; Be: 0.00091 ± 0.00049; B: 0.39 ± 0.26; Sc: 0.033 ± 0.011; V: 0.50 ± 0.38; Cr: 0.53 ± 0.16; Co: 0.0046 ± 0.0032; Ni: 0.065 ± 0.037; Cu: 0.072 ± 0.022; Zn: 0.80 ± 0.56; Ga: 0.0037 ± 0.0020; Ge: 0.0081 ± 0.0040; As: 0.021 ± 0.009; Rb: 0.11 ± 0.05; Sr: 0.018 ± 0.018; Y: 0.0018 ± 0.0017; Zr: 0.0030 ± 0.0015; Nb: 0.0012 ± 0.0012; Mo: 0.035 ± 0.030; Cd: 0.0026 ± 0.0015; In: 0.00016 ± 0.00004; Sn: 0.0083 ± 0.0016; Sb: 0.010 ± 0.006; Te: 0.00097 ± 0.00014; Cs: 0.00060 ± 0.00034; Ba: 0.075 ± 0.063; La: 0.0025 ± 0.0020; Ce: 0.0028 ± 0.0016; Pr: 0.00056 ± 0.00042; Nd: 0.0019 ± 0.0017; Sm: 0.00079 ± 0.00036; Eu: 0.00023 ± 0.00014; Gd: 0.00063 ± 0.00054; Tb: 0.00013 ± 0.00005; Dy: 0.00058 ± 0.00038; Ho: 0.00013 ± 0.00008; Er: 0.00027 ± 0.00020; Tm: 0.00011 ± 0.00003; Yb: 0.00043 ± 0.00025; Lu: 0.00015 ± 0.00007; Hf: 0.0010 ± 0.0012; Ta: 0.00017 ± 0.00009; W: 0.023 ± 0.010; Tl: 0.0026 ± 0.0009; Pb: 0.043 ± 0.020; Bi: 0.00049 ± 0.00028; Th: 0.00062 ± 0.00050; U: 0.00027 ± 0.00025 — ppb, mean ± STD of n = 5 blanks (Table 2)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"A glass microconcentric nebulizer (MCN) and a cyclonic spray chamber comprised the sample introduction system, with a typical sample uptake rate of 0.20 ml/min\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites" ;
    ada:samplingUnitName "Sample name only — Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor>,
        <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionQicpmsTAPP-detail-Gao2008/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.2 L/min (intermediate gas; stated section 3.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.2e+00 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "14 L/min (outer ICP gas; stated section 3.1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 14 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "Autolens voltages \"set by optimizing a solution of 10 ng/ml Mg, Co, Rh, Ce, Pb and U\"; \"The nebulizer gas flow rate was optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U, while keeping the CeO+/Ce+ and Ce2+/Ce+ ratios below 2.5%\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "Alternating 5% HNO3 + 0.1% HF and 3% HNO3 washout for B and Ta (stated section 3.1)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1350 W (stated section 3.1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1350 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "bomb attack: 48 h; re-dissolution: overnight — §3.3" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "bomb attack: 190 °C; re-dissolution: 150 °C — §3.3" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 190 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "N — 'optimized to obtain maximum signal intensities for Mg, Co, Rh, Ce, Pb and U' (§3.1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3.1e+00 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "50 mg (stated section 3.3)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "0.20 ml/min (stated section 3.1)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2e-01 .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor> a schema1:PropertyValue ;
    schema1:name "Doubly-Charged Species Monitor" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor> ;
    schema1:value "Ce2+/Ce+ — §3.1" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction> a schema1:PropertyValue ;
    schema1:name "Doubly-Charged Species Production" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction> ;
    schema1:value "Ce2+/Ce+ below 2.5% — §3.1" .


```


### detail example P1
detail instance derived from Yu+etal2005 | PerkinElmer ELAN DRC II | Univ Cambridge.
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
  "@id": "ex:solutionQicpmsTAPP-detail-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 300,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Ten to twenty tests, about 300 µg of shells — §2; one measurement uses 250 µl at 100 ppm Ca, equivalent to 60 µg calcite"
            }
          ],
          "schema:name": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 60,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 0.99,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.99-1.02 L/min (Table 1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1300,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1300 W (Table 1)"
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
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "15 L/min (Table 1)"
                    },
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
                      "schema:value": 1.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.2 L/min (Table 1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks — §2, §3.2"
                },
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
                  "schema:value": "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "N — precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N/A — all isotopes in pulse mode 'to avoid the need for cross calibration' (§3.1)"
              },
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
                "schema:value": "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%"
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
            "schema:description": "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 µl 0.075 M HNO3. 20 µl diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca — §2",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "ada:proceduralBlankLevel": "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N — relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (§3.2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Cambridge (affiliation)"
      },
      "schema:identifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
      "schema:description": "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60–240 ppm Ca (Table 1, §2, §3.5)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2–7.8), 5.05% (0.5–1.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07–0.24), 4.80% (0.01–0.07); U/Ca: 2.54%] — RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, §3.6)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2–7.8), 1.69% (0.5–1.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07–0.24), 0.80% (0.01–0.07); U/Ca: 1.09%] — Acc.% = (average measured − true)/true × 100 on external standards (Table 2)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% = SD of measurements / average ratio × 100 — table notes"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-AES (for initial [Ca] determination; stated section 2)",
        "schema:description": "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:sensitivityYield": "7Li: 2500 cps/ppb; 11B: 1000 cps/ppb; 25Mg: 800 cps/ppb; 46Ca: 0.5 cps/ppb; 27Al: 15000 cps/ppb; 55Mn: 12000 cps/ppb; 66Zn: 2500 cps/ppb; 87Sr: 1500 cps/ppb; 111Cd: 1500 cps/ppb; 238U: 9000 cps/ppb — typical count rate (Table 1); ~40 kHz for 1 ppb ¹¹⁵In at 60 µl/min (§2)",
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnitName": "N — only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 — in the units of the ratio (Table 2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 300,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Ten to twenty tests, about 300 \u00b5g of shells \u2014 \u00a72; one measurement uses 250 \u00b5l at 100 ppm Ca, equivalent to 60 \u00b5g calcite"
            }
          ],
          "schema:name": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 60,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 0.99,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.99-1.02 L/min (Table 1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1300,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1300 W (Table 1)"
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
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "15 L/min (Table 1)"
                    },
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
                      "schema:value": 1.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.2 L/min (Table 1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks \u2014 \u00a72, \u00a73.2"
                },
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
                  "schema:value": "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-P1/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "N \u2014 precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N/A \u2014 all isotopes in pulse mode 'to avoid the need for cross calibration' (\u00a73.1)"
              },
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
                "schema:value": "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%"
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
            "schema:description": "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 \u00b5l 0.075 M HNO3. 20 \u00b5l diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca \u2014 \u00a72",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "ada:proceduralBlankLevel": "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N \u2014 relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (\u00a73.2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Cambridge (affiliation)"
      },
      "schema:identifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
      "schema:description": "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60\u2013240 ppm Ca (Table 1, \u00a72, \u00a73.5)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2\u20137.8), 5.05% (0.5\u20131.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07\u20130.24), 4.80% (0.01\u20130.07); U/Ca: 2.54%] \u2014 RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, \u00a73.6)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2\u20137.8), 1.69% (0.5\u20131.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07\u20130.24), 0.80% (0.01\u20130.07); U/Ca: 1.09%] \u2014 Acc.% = (average measured \u2212 true)/true \u00d7 100 on external standards (Table 2)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% = SD of measurements / average ratio \u00d7 100 \u2014 table notes"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-AES (for initial [Ca] determination; stated section 2)",
        "schema:description": "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler"
  ],
  "ada:sensitivityYield": "7Li: 2500 cps/ppb; 11B: 1000 cps/ppb; 25Mg: 800 cps/ppb; 46Ca: 0.5 cps/ppb; 27Al: 15000 cps/ppb; 55Mn: 12000 cps/ppb; 66Zn: 2500 cps/ppb; 87Sr: 1500 cps/ppb; 111Cd: 1500 cps/ppb; 238U: 9000 cps/ppb \u2014 typical count rate (Table 1); ~40 kHz for 1 ppb \u00b9\u00b9\u2075In at 60 \u00b5l/min (\u00a72)",
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnitName": "N \u2014 only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 \u2014 in the units of the ratio (Table 2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-P1 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "ICP-AES measured initial Ca concentration; sample then diluted to 100 ppm Ca for Q-ICP-MS analysis; ICP-AES performed first (stated section 2)" ;
                    schema1:name "ICP-AES (for initial [Ca] determination; stated section 2)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2–7.8), 5.05% (0.5–1.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07–0.24), 4.80% (0.01–0.07); U/Ca: 2.54%] — RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, §3.6)" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2–7.8), 1.69% (0.5–1.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07–0.24), 0.80% (0.01–0.07); U/Ca: 1.09%] — Acc.% = (average measured − true)/true × 100 on external standards (Table 2)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD% = SD of measurements / average ratio × 100 — table notes" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues>,
                                <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Ten to twenty tests handpicked, crushed gently, cleaned of clays (water, methanol) and silicates, reductively and oxidatively cleaned, rinsed twice in 0.001 M HNO3 and dissolved in 200 µl 0.075 M HNO3. 20 µl diluted for Ca by ICP-AES, the remainder diluted to 100 ppm Ca — §2" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:description "Cetac ASX-100 autosampler; auto lens on; 0.03 mm ID pump tubing at 12 rpm; Ca matrix effects tested over 60–240 ppm Ca (Table 1, §2, §3.5)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Cambridge (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N — precision and accuracy are assessed on external standards of known ratio (Table 2); core-top results are compared with published data (Table 4)" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N — relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (§3.2)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- quartz cyclonic spray chamber and \"glass micro-concentric nebulizer Micromist FM005 ... producing an uptake rate of ~60 ul/min at a pump rate of 12 rpm\"; Cetac ASX100 autosampler" ;
    ada:detectionLimit "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 — in the units of the ratio (Table 2)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 6 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods" ;
    ada:samplingUnitName "N — only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated" ;
    ada:sensitivityYield "7Li: 2500 cps/ppb; 11B: 1000 cps/ppb; 25Mg: 800 cps/ppb; 46Ca: 0.5 cps/ppb; 27Al: 15000 cps/ppb; 55Mn: 12000 cps/ppb; 66Zn: 2500 cps/ppb; 87Sr: 1500 cps/ppb; 111Cd: 1500 cps/ppb; 238U: 9000 cps/ppb — typical count rate (Table 1); ~40 kHz for 1 ppb ¹¹⁵In at 60 µl/min (§2)" ;
    ada:sessionIdentifier "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionQicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "Natural isotopic abundances used to select isotopes and derive correction factors: the Li standard \"was artificially depleted of 7Li (92.32% vs 92.48% for natural)\"; \"The natural abundance of 11B (80.17%) is also different from values of foraminiferal samples which are expected to be 80.40-80.43% if assumed to have d11B ratios of 25-27 permil\", giving \"correction factors (0.9983 for Li and 0.9968-0.9971 for B)\"; 111Cd 12.8%, 112Cd 24.1%, 114Cd 28.7%, 238U 99.3%" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.2 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.2e+00 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "15 L/min (Table 1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"The instrument sensitivity was optimized daily using a 10 ppb Mg-In-U standard\"; \"Plasma robustness was monitored by constraining CeO/Ce ratio within 3% to refrain formation of polyatomic oxides\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "Longer washout and uptake times for B, and a quartz spray chamber to reduce B blanks — §2, §3.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1300 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1300 .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N/A — all isotopes in pulse mode 'to avoid the need for cross calibration' (§3.1)" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.99-1.02 L/min (Table 1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.9e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "Ten to twenty tests, about 300 µg of shells — §2; one measurement uses 250 µl at 100 ppm Ca, equivalent to 60 µg calcite" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 300 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~60 uL/min (stated Table 1; 0.03 mm ID pump tubing)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .


```


### detail example Agilent7500
detail instance derived from Makishima+etal2011 | Agilent 7500cs | PML Okayama.
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
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 245,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "bomb HF: 245 °C; other: N"
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
            "schema:name": "Data processing",
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
                "schema:value": "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor ≥ 1000 — clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 3
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15–42 mg (basalts and andesites); 30–63 mg (peridotites); 8–22 mg (NIST glasses); 9–28 mg (chondrites)"
            }
          ],
          "schema:name": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
          "schema:description": "no value available: schema:description"
        }
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
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 — the chondrites are samples",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg — total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)"
      },
      "schema:identifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
      "schema:description": "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996–0.999, Table 2)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [Cd: 2.0%; In, Tl, Bi: 1.6%] — RPD of X/¹⁴⁹Sm between neighbouring calibrator runs (Table 1)"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3–10%]; JP-1, PCC-1, DTS-1 [Cd: 7–16%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2–3%; In: 0.7–3%; Tl: 6–12%; Bi: 1–4%] — intermediate precision, RSD of n = 4–8 separate decompositions (Tables 3 and 4)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] — Table 3; In, Tl and Bi compared with previous studies"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD — 'The normalised ratios after evaporation together with the RSD (n = 5)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:sensitivityYield": "111Cd: 0.04; 115In: 0.5; 149Sm: 0.09; 205Tl: 0.5; 209Bi: 0.6 — count pg⁻¹ ml (Table 1)",
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnitName": "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) — \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 — 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)",
  "ada:limitOfQuantificationMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 245,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "bomb HF: 245 \u00b0C; other: N"
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
            "schema:name": "Data processing",
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
                "schema:value": "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor \u2265 1000 \u2014 clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 3
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15\u201342 mg (basalts and andesites); 30\u201363 mg (peridotites); 8\u201322 mg (NIST glasses); 9\u201328 mg (chondrites)"
            }
          ],
          "schema:name": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
          "schema:description": "no value available: schema:description"
        }
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
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 \u2014 the chondrites are samples",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg \u2014 total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)"
      },
      "schema:identifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
      "schema:description": "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996\u20130.999, Table 2)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [Cd: 2.0%; In, Tl, Bi: 1.6%] \u2014 RPD of X/\u00b9\u2074\u2079Sm between neighbouring calibrator runs (Table 1)"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3\u201310%]; JP-1, PCC-1, DTS-1 [Cd: 7\u201316%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2\u20133%; In: 0.7\u20133%; Tl: 6\u201312%; Bi: 1\u20134%] \u2014 intermediate precision, RSD of n = 4\u20138 separate decompositions (Tables 3 and 4)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] \u2014 Table 3; In, Tl and Bi compared with previous studies"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD \u2014 'The normalised ratios after evaporation together with the RSD (n = 5)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\""
  ],
  "ada:sensitivityYield": "111Cd: 0.04; 115In: 0.5; 149Sm: 0.09; 205Tl: 0.5; 209Bi: 0.6 \u2014 count pg\u207b\u00b9 ml (Table 1)",
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnitName": "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) \u2014 \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 \u2014 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)",
  "ada:limitOfQuantificationMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-Agilent7500 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] — Table 3; In, Tl and Bi compared with previous studies" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "all [Cd: 2.0%; In, Tl, Bi: 1.6%] — RPD of X/¹⁴⁹Sm between neighbouring calibrator runs (Table 1)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD — 'The normalised ratios after evaporation together with the RSD (n = 5)'" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3–10%]; JP-1, PCC-1, DTS-1 [Cd: 7–16%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2–3%; In: 0.7–3%; Tl: 6–12%; Bi: 1–4%] — intermediate precision, RSD of n = 4–8 separate decompositions (Tables 3 and 4)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Rock powders decomposed with the Sm spike; NIST glasses crushed roughly in a silicon nitride mortar, chips hand-picked, washed and dried; solutions diluted with 0.5 mol/l HNO3 to a dilution factor ≥ 1000 — clean room at PML; NIST SRM 610 decomposed without spike, the Sm spike added to its solution" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "ICP operating conditions as in Makishima and Nakamura (2006); pseudo-flow injection with transient signals integrated as total counts, ~0.013 ml per measurement; an evaporation test showed no loss of Cd, In, Tl or Bi (ratios 0.996–0.999, Table 2)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N -- \"an average of eight sessions\" referenced; no session identifier stated" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Pheasant Memorial Laboratory (PML) for Geochemistry and Cosmochemistry, Okayama University (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionQicpmsTAPP-detail-Agilent7500/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1, NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 — the chondrites are samples" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg — total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Flow injection -- \"The pseudo-flow injection (FI) sample introduction technique, in which transient signals were integrated as total counts, was employed with the ID-IS method to minimise total sample consumption volume (~0.013 ml)\"" ;
    ada:detectionLimit "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 — 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses" ;
    ada:samplingUnitName "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) — \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only" ;
    ada:sensitivityYield "111Cd: 0.04; 115In: 0.5; 149Sm: 0.09; 205Tl: 0.5; 209Bi: 0.6 — count pg⁻¹ ml (Table 1)" ;
    ada:sessionIdentifier "N -- \"an average of eight sessions\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7500/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "115Sn/118Sn = 0.014 and 113In/115In = 0.0448 (Rosman and Taylor 1998); 94Mo/95Mo = 0.58; MoOH+/MoO+ ~0.15 (measured); 111Cd/113Cd = 1.05 as reference" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "~200 s wash with 0.5 mol/l HNO3, and 200 s with 0.5 mol/l HF after the Mo standard, since Mo was difficult to wash out with HNO3" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "bomb HF: 245 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 245 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "15–42 mg (basalts and andesites); 30–63 mg (peridotites); 8–22 mg (NIST glasses); 9–28 mg (chondrites)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .


```


### detail example Agilent7900
detail instance derived from Long+etal2025 | Agilent 7900 | IPGP France.
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
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 0.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.2 mL/min (stated Methods)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "@id": "ada:parameter/module/CollisionCell/gasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/CollisionCell/gasFlowRate"
                        }
                      ],
                      "schema:name": "Gas Flow Rate",
                      "schema:value": 5,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "5 mL/min — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Collision-Reaction-Cell"
                },
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "ICP Source",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut de Physique du Globe de Paris (IPGP), France (affiliation)"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 °C for ~48 h; the digestion for the elemental analysis is not stated — Methods",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "MC-ICP-MS — Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)",
        "schema:description": "N — the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnitName": "Sample name only — meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 0.2,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.2 mL/min (stated Methods)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "@id": "ada:parameter/module/CollisionCell/gasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/CollisionCell/gasFlowRate"
                        }
                      ],
                      "schema:name": "Gas Flow Rate",
                      "schema:value": 5,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "5 mL/min \u2014 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Collision-Reaction-Cell"
                },
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "ICP Source",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut de Physique du Globe de Paris (IPGP), France (affiliation)"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 \u00b0C for ~48 h; the digestion for the elemental analysis is not stated \u2014 Methods",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "MC-ICP-MS \u2014 Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)",
        "schema:description": "N \u2014 the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnitName": "Sample name only \u2014 meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionQicpmsTAPP-detail-Agilent7900 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "N — the elements are measured by Q-ICP-MS and the Zn isotopes by MC-ICP-MS; whether on the same solutions is not stated" ;
                    schema1:name "MC-ICP-MS — Zn isotopes on a Thermo Neptune Plus at IPGP (Methods)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "The Zn-isotope procedure digests ~35 mg of bulk powder in HNO3-HF at 120 °C for ~48 h; the digestion for the elemental analysis is not stated — Methods" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institut de Physique du Globe de Paris (IPGP), France (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS> ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The sample was introduced into a Scott spray chamber through a MicroMist nebulizer at an uptake rate of 0.2 mL/min\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites" ;
    ada:samplingUnitName "Sample name only — meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/gasFlowRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7900/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/gasFlowRate> a schema1:PropertyValue ;
    schema1:description "5 mL/min — 'analyzing atomic masses from 23 (Na) to 75 (As) in a collision-reaction cell, utilizing helium gas at a flow rate of 5 mL/min' (Methods)" ;
    schema1:name "Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/CollisionCell/gasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "0.2 mL/min (stated Methods)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2e-01 .


```


### detail example Agilent7500-2
detail instance derived from Lu+etal2007 | Agilent 7500cs | PML Okayama.
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
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 70,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "ultrasonic HF decomposition: <70 °C; bomb HF decomposition: 245 °C; re-dissolution: N — abstract"
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
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "all: P/A factor determined each day before measurement — §2.1.1"
              },
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
                "schema:value": "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) — §2.7"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Powders weighed with the B, Zr–Hf and Mo–Sn–Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted — §2.5; GSJ samples and PCC-1 further pulverised (§2.3)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 3
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) — §2.5"
            }
          ],
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 1,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "N — self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (§2.6)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 0.92,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.92 L/min (stated Table in section 2.1.1)"
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
                      "schema:value": 0.25,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.25 l/min — Table 1a"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1.6,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.6 kW (stated Table in section 2.1.1)"
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
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "15 L/min (stated Table in section 2.1.1)"
                    },
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
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 — §2.1.1"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — §2.3; the chondrites are samples",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "B: 13–185 pg (ultrasonic); Zr: 0.9–29, 55; Nb: 2–5, 3; Mo: 0.2–10, ~134; Sn: ~323, ~276; Sb: 0.7–9, ~60; Hf: <12, <8; Ta: 0.6–7, 0.6–2 — total procedural blank in pg, ultrasonic then bomb method (Table 4)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)"
      },
      "schema:description": "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca–Al–Mg fluorides tested in 19 synthetic solutions (§2.4, §2.6)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0–4.6% RSD] — §3.7, Tables 5–6; Mo in JB-1 (15%) excluded as heterogeneous"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] — Tables 5–6; 'a significant difference exists for B in JA-2'"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% — Tables 5 and 6; 'Averages of the reproducibility (RSD %)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SF-ICP-MS — Ti on a Finnigan ELEMENT at PML (§2.1.2)",
        "schema:description": "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions — §2.5, §2.8"
      }
    }
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnitName": "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 — ng/g in rock, 3σ (Table 2a); in solution, in pg/g",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 70,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "ultrasonic HF decomposition: <70 \u00b0C; bomb HF decomposition: 245 \u00b0C; re-dissolution: N \u2014 abstract"
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
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "all: P/A factor determined each day before measurement \u2014 \u00a72.1.1"
              },
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
                "schema:value": "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) \u2014 \u00a72.7"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Powders weighed with the B, Zr\u2013Hf and Mo\u2013Sn\u2013Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted \u2014 \u00a72.5; GSJ samples and PCC-1 further pulverised (\u00a72.3)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 3
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) \u2014 \u00a72.5"
            }
          ],
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
          "schema:description": "no value available: schema:description"
        }
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
                    "Sample Introduction System",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRate"
                        }
                      ],
                      "schema:name": "Sample Uptake Rate",
                      "schema:value": 1,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "N \u2014 self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (\u00a72.6)"
                    },
                    {
                      "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/SolutionIntroduction/nebulizerGasFlowRate"
                        }
                      ],
                      "schema:name": "Nebulizer Gas Flow Rate",
                      "schema:value": 0.92,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.92 L/min (stated Table in section 2.1.1)"
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
                      "schema:value": 0.25,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.25 l/min \u2014 Table 1a"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1.6,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.6 kW (stated Table in section 2.1.1)"
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
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "15 L/min (stated Table in section 2.1.1)"
                    },
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
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.90 L/min (stated Table in section 2.1.1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 \u2014 \u00a72.1.1"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 \u2014 \u00a72.3; the chondrites are samples",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "B: 13\u2013185 pg (ultrasonic); Zr: 0.9\u201329, 55; Nb: 2\u20135, 3; Mo: 0.2\u201310, ~134; Sn: ~323, ~276; Sb: 0.7\u20139, ~60; Hf: <12, <8; Ta: 0.6\u20137, 0.6\u20132 \u2014 total procedural blank in pg, ultrasonic then bomb method (Table 4)",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)"
      },
      "schema:description": "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca\u2013Al\u2013Mg fluorides tested in 19 synthetic solutions (\u00a72.4, \u00a72.6)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0\u20134.6% RSD] \u2014 \u00a73.7, Tables 5\u20136; Mo in JB-1 (15%) excluded as heterogeneous"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] \u2014 Tables 5\u20136; 'a significant difference exists for B in JA-2'"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% \u2014 Tables 5 and 6; 'Averages of the reproducibility (RSD %)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SF-ICP-MS \u2014 Ti on a Finnigan ELEMENT at PML (\u00a72.1.2)",
        "schema:description": "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions \u2014 \u00a72.5, \u00a72.8"
      }
    }
  ],
  "ada:analyticalMode": [
    "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnitName": "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"\u2013\"#8\" (p.7) are synthetic yield-test solutions, not samples",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 \u2014 ng/g in rock, 3\u03c3 (Table 2a); in solution, in pg/g",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-Agilent7500-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "The Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta, and its Nb (from Nb/Mo and Nb/Zr) is used for the SF-ICP-MS Ti calculation on the same solutions — §2.5, §2.8" ;
                    schema1:name "SF-ICP-MS — Ti on a Finnigan ELEMENT at PML (§2.1.2)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0–4.6% RSD] — §3.7, Tables 5–6; Mo in JB-1 (15%) excluded as heterogeneous" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD% — Tables 5 and 6; 'Averages of the reproducibility (RSD %)'" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] — Tables 5–6; 'a significant difference exists for B in JA-2'" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Powders weighed with the B, Zr–Hf and Mo–Sn–Sb spikes and decomposed with 30 mol/l HF and mannitol, dried, dissolved in 0.5 mol/l HF, fluorides removed by centrifuging, and the supernatant diluted — §2.5; GSJ samples and PCC-1 further pulverised (§2.3)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues>,
                                <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Pseudo-flow injection with the ASX-100 autosampler; recovery yields from Ca–Al–Mg fluorides tested in 19 synthetic solutions (§2.4, §2.6)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — §2.3; the chondrites are samples" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "B: 13–185 pg (ultrasonic); Zr: 0.9–29, 55; Nb: 2–5, 3; Mo: 0.2–10, ~134; Sn: ~323, ~276; Sb: 0.7–9, ~60; Hf: <12, <8; Ta: 0.6–7, 0.6–2 — total procedural blank in pg, ultrasonic then bomb method (Table 4)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Flow injection -- \"pseudo-FI\" declared as the data acquisition mode; sec 2.6 \"Pseudo-flow injection (FI) method for ICP-QMS\", explicitly contrasted with \"the continuous sample introduction method\"" ;
    ada:detectionLimit "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 — ng/g in rock, 3σ (Table 2a); in solution, in pg/g" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnitName "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionQicpmsTAPP-detail-Agilent7500-2/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "Spike ratios 91Zr/90Zr 29.0, 97Mo/95Mo 201, 119Sn/118Sn 30.1, 121Sb/123Sb 199, 179Hf/178Hf 25.1, against natural 0.218, 0.600, 0.355, 1.34, 0.499 (Rosman and Taylor 1998); 11B/10B spike 0.05348 and natural 4.053 by TIMS (Makishima et al. 1997) — §2.7" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.90 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "15 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.25 l/min — Table 1a" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.5e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "0.5 mol/l HF as carrier and wash, which washes out Zr, Nb, Hf and Ta; ~20 min of 0.5 mol/l HF after REE work in HNO3 — §2.1.1" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1.6 kW (stated Table in section 2.1.1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.6e+00 .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "all: P/A factor determined each day before measurement — §2.1.1" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "ultrasonic HF decomposition: <70 °C; bomb HF decomposition: 245 °C; re-dissolution: N — abstract" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 70 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.92 L/min (stated Table in section 2.1.1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.2e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~20 mg (basalts and andesites); ~50 mg (peridotites); ~10 mg (meteorites) — §2.5" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "N — self-aspiration (Table 1a); pseudo-FI uses 0.013 ml per sample (§2.6)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .


```


### detail example Agilent8800
detail instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel.
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
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent8800",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 110,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); microwave digestion: up to 210 °C; Se recovery: 70 °C — §2.2"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 °C, then cooled overnight; Se recovery: 1 h; other: N — §2.2"
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
            "schema:description": "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 °C) — §2.2",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 mg (Te, tri-acid); 40–50 mg (Se, microwave) — §2.2"
            }
          ],
          "schema:name": "N — SPM isotherm experiment at 1000 mg/L",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "N — 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW"
      },
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NCS 73307 — stream sediment, for the total digestions",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NCS 73307 [Te: 94 ± 17% recovery (N = 3); Se: 70–134% recovery (N = 3)] — §2.3, §2.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: SD — 'mean ± SD recovery values of 94 ± 17% (N = 3)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnitName": "N — the sorption-isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-Agilent8800",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 110,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "tri-acid digestion: 110 \u00b0C; re-dissolution: 120 \u00b0C (evaporation); microwave digestion: up to 210 \u00b0C; Se recovery: 70 \u00b0C \u2014 \u00a72.2"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 \u00b0C, then cooled overnight; Se recovery: 1 h; other: N \u2014 \u00a72.2"
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
            "schema:description": "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 \u00b0C) \u2014 \u00a72.2",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 mg (Te, tri-acid); 40\u201350 mg (Se, microwave) \u2014 \u00a72.2"
            }
          ],
          "schema:name": "N \u2014 SPM isotherm experiment at 1000 mg/L",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "N \u2014 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW"
      },
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NCS 73307 \u2014 stream sediment, for the total digestions",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NCS 73307 [Te: 94 \u00b1 17% recovery (N = 3); Se: 70\u2013134% recovery (N = 3)] \u2014 \u00a72.3, \u00a72.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: SD \u2014 'mean \u00b1 SD recovery values of 94 \u00b1 17% (N = 3)'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnitName": "N \u2014 the sorption-isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-Agilent8800 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "NCS 73307 [Te: 94 ± 17% recovery (N = 3); Se: 70–134% recovery (N = 3)] — §2.3, §2.4" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: SD — 'mean ± SD recovery values of 94 ± 17% (N = 3)'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "SPM recovered by centrifugation, oven dried, ground in agate mortars and totally digested: tri-acid for Te, microwave for Se (Se is volatile above 70 °C) — §2.2" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ] ] ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "N — 'Agilent 8800, Basel, Switzerland'; the Basel-area author affiliation is FHNW" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "N — SPM isotherm experiment at 1000 mg/L" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "NCS 73307 — stream sediment, for the total digestions" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "N — SPM isotherm experiment at 1000 mg/L" ;
    ada:samplingUnitName "N — the sorption-isotherm solutions carry no sample or unit identifiers" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "tri-acid digestion: 2 h; microwave digestion: 10 min at 210 °C, then cooled overnight; Se recovery: 1 h; other: N — §2.2" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); microwave digestion: up to 210 °C; Se recovery: 70 °C — §2.2" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 110 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "30 mg (Te, tri-acid); 40–50 mg (Se, microwave) — §2.2" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example P6
detail instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated.
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
  "@id": "ex:solutionQicpmsTAPP-detail-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 110,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 °C; F3 H2O2: 85 °C, then 25 °C"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N"
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
            "schema:description": "SPM recovered by centrifugation, oven dried (70 °C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) — §2.2, Table 1",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 mg (total digestion); 200–500 mg per extraction — §2.2, Table 1"
            }
          ],
          "schema:name": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Te: ~35 µg/L in the F3 extraction blanks; other: N — three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (§2.2)",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "N — instrument given as 'iCAP-TQ, Thermo' with no laboratory stated"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NIST 1643f, NCS 73307, NIST 1640a — freshwater, stream sediment and freshwater",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NIST 1643f [Te: 95 ± 5% (KED), 89 ± 10% (O2), N = 5; Se: 95 ± 3%]; NCS 73307 [Te: 99 ± 14% (KED), 70 ± 19% (O2), N = 4]; NIST 1640a [Se: 85 ± 2%] — recoveries (§2.3, §2.4)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnitName": "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Te: 0.1 ng/L; other: N — N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 110,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "tri-acid digestion: 110 \u00b0C; re-dissolution: 120 \u00b0C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 \u00b0C; F3 H2O2: 85 \u00b0C, then 25 \u00b0C"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N"
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
            "schema:description": "SPM recovered by centrifugation, oven dried (70 \u00b0C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) \u2014 \u00a72.2, Table 1",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 mg (total digestion); 200\u2013500 mg per extraction \u2014 \u00a72.2, Table 1"
            }
          ],
          "schema:name": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Te: ~35 \u00b5g/L in the F3 extraction blanks; other: N \u2014 three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (\u00a72.2)",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "N \u2014 instrument given as 'iCAP-TQ, Thermo' with no laboratory stated"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "NIST 1643f, NCS 73307, NIST 1640a \u2014 freshwater, stream sediment and freshwater",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NIST 1643f [Te: 95 \u00b1 5% (KED), 89 \u00b1 10% (O2), N = 5; Se: 95 \u00b1 3%]; NCS 73307 [Te: 99 \u00b1 14% (KED), 70 \u00b1 19% (O2), N = 4]; NIST 1640a [Se: 85 \u00b1 2%] \u2014 recoveries (\u00a72.3, \u00a72.4)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnitName": "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Te: 0.1 ng/L; other: N \u2014 N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-P6 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "NIST 1643f [Te: 95 ± 5% (KED), 89 ± 10% (O2), N = 5; Se: 95 ± 3%]; NCS 73307 [Te: 99 ± 14% (KED), 70 ± 19% (O2), N = 4]; NIST 1640a [Se: 85 ± 2%] — recoveries (§2.3, §2.4)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "SPM recovered by centrifugation, oven dried (70 °C), ground in agate mortars and aliquoted for tri-acid total digestion and parallel selective extractions (two replicates per extraction mode) — §2.2, Table 1" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ] ] ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "N — instrument given as 'iCAP-TQ, Thermo' with no laboratory stated" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "NIST 1643f, NCS 73307, NIST 1640a — freshwater, stream sediment and freshwater" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:proceduralBlankLevel "Te: ~35 µg/L in the F3 extraction blanks; other: N — three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (§2.2)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Te: 0.1 ng/L; other: N — N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307" ;
    ada:samplingUnitName "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "tri-acid digestion: 2 h; F1 acetate: 6 h; F2 ascorbate, F4 HCl, F4N HNO3: 24 h; F3 H2O2: 2 h + 3 h, then 30 min; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "tri-acid digestion: 110 °C; re-dissolution: 120 °C (evaporation); F1 acetate, F2 ascorbate, F4 HCl, F4N HNO3: 25 °C; F3 H2O2: 85 °C, then 25 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 110 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "30 mg (total digestion); 200–500 mg per extraction — §2.2, Table 1" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example P7
detail instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe.
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
  "@id": "ex:solutionQicpmsTAPP-detail-P7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "CRM-TMDW [Se: 98–106% recovery (N = 16)]; NIST 1643f [Se: 100–102% (N = 16); Te: 85–91% (N = 4)] — §2.3, §2.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Te, Se: SD — Figs 1–2"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio"
            }
          ],
          "schema:name": "Collision/Reaction Gas Mixture Ratio",
          "schema:value": "Se masses: He:H2 = 92% : 8%; other: N — 'to minimise 40Ar37Cl interferences' (§2.4)"
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
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "CRM-TMDW, NIST 1643f — drinking water and freshwater",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnitName": "N — the sorption-kinetics and isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Te: 0.01 µg/L; Se: 0.06 µg/L — N = 10 (§2.3, §2.4)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-P7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "CRM-TMDW [Se: 98\u2013106% recovery (N = 16)]; NIST 1643f [Se: 100\u2013102% (N = 16); Te: 85\u201391% (N = 4)] \u2014 \u00a72.3, \u00a72.4"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Te, Se: SD \u2014 Figs 1\u20132"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio"
            }
          ],
          "schema:name": "Collision/Reaction Gas Mixture Ratio",
          "schema:value": "Se masses: He:H2 = 92% : 8%; other: N \u2014 'to minimise 40Ar37Cl interferences' (\u00a72.4)"
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
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "N \u2014 sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "CRM-TMDW, NIST 1643f \u2014 drinking water and freshwater",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnitName": "N \u2014 the sorption-kinetics and isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Te: 0.01 \u00b5g/L; Se: 0.06 \u00b5g/L \u2014 N = 10 (\u00a72.3, \u00a72.4)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionQicpmsTAPP-detail-P7 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "Te, Se: SD — Figs 1–2" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "CRM-TMDW [Se: 98–106% recovery (N = 16)]; NIST 1643f [Se: 100–102% (N = 16); Te: 85–91% (N = 4)] — §2.3, §2.4" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Karlsruhe Institute of Technology (KIT), Germany" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "CRM-TMDW, NIST 1643f — drinking water and freshwater" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Te: 0.01 µg/L; Se: 0.06 µg/L — N = 10 (§2.3, §2.4)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f" ;
    ada:samplingUnitName "N — the sorption-kinetics and isotherm solutions carry no sample or unit identifiers" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio> a schema1:PropertyValue ;
    schema1:name "Collision/Reaction Gas Mixture Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio> ;
    schema1:value "Se masses: He:H2 = 92% : 8%; other: N — 'to minimise 40Ar37Cl interferences' (§2.4)" .


```


### detail example P8
detail instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo.
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
  "@id": "ex:solutionQicpmsTAPP-detail-P8",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 3,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "HF-HNO3 attack: 120 °C, then 220 °C; HNO3-HCl step: 150 °C; HNO3 step: 80 °C; final uptake: N"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N"
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
            "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 µg readability) and transferred to PFA vials without powdering — ISO class 5 cleanroom; acids distilled once",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 1.478,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1.478–4.325 mg per particle; 20 mg of Allende — 4%–10% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2"
            }
          ],
          "schema:name": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "N — blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Science Tokyo"
      },
      "schema:description": "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 µL of 100 ng/g Rh added as internal standard — Methods",
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "Smithsonian Allende powder — 20 mg, dissolved and measured under the same procedure, n = 5",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "N — the Allende replicate averages and uncertainties are in the supplementary materials"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnitName": "Sample name only — each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionQicpmsTAPP-detail-P8",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperature"
                  }
                ],
                "schema:name": "Digestion Temperature",
                "schema:value": 3,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "HF-HNO3 attack: 120 \u00b0C, then 220 \u00b0C; HNO3-HCl step: 150 \u00b0C; HNO3 step: 80 \u00b0C; final uptake: N"
              },
              {
                "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SolutionIntroduction/digestionDuration"
                  }
                ],
                "schema:name": "Digestion Duration",
                "schema:value": "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N"
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
            "schema:description": "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 \u00b5g readability) and transferred to PFA vials without powdering \u2014 ISO class 5 cleanroom; acids distilled once",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume"
                }
              ],
              "schema:name": "Sample Aliquot Mass or Volume",
              "schema:value": 1.478,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1.478\u20134.325 mg per particle; 20 mg of Allende \u2014 4%\u201310% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2"
            }
          ],
          "schema:name": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "N \u2014 blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Science Tokyo"
      },
      "schema:description": "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 \u00b5L of 100 ng/g Rh added as internal standard \u2014 Methods",
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "Smithsonian Allende powder \u2014 20 mg, dissolved and measured under the same procedure, n = 5",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "N \u2014 the Allende replicate averages and uncertainties are in the supplementary materials"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnitName": "Sample name only \u2014 each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing"
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

ex:solutionQicpmsTAPP-detail-P8 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "N — the Allende replicate averages and uncertainties are in the supplementary materials" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Particles individually weighed on a Mettler Toledo XPR2U microbalance (0.1 µg readability) and transferred to PFA vials without powdering — ISO class 5 cleanroom; acids distilled once" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:description "Group-1 dilution made after at least 30 min ultrasonic homogenisation 'to avoid elemental fractionation in the solution'; 175 µL of 100 ng/g Rh added as internal standard — Methods" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institute of Science Tokyo" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Smithsonian Allende powder — 20 mg, dissolved and measured under the same procedure, n = 5" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "N — blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder" ;
    ada:samplingUnitName "Sample name only — each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF-HNO3 attack: 3 h ultrasonic, 12 h, then 5 days; HNO3-HCl step: 1 day; HNO3 step: 1 day; final uptake: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF-HNO3 attack: 120 °C, then 220 °C; HNO3-HCl step: 150 °C; HNO3 step: 80 °C; final uptake: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "1.478–4.325 mg per particle; 20 mg of Allende — 4%–10% aliquots for Group-1 and Group-3, 0.4 mL of the Group-1 solution for Group-2" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.478e+00 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution Q-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing
  CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
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
                    schema:description:
                      description: Brief description of sample provenance, form, or
                        preparation state relevant to this analysis.
                      anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    schema:additionalProperty:
                      type: array
                      items:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleAliquotMassOrVolume
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleAliquotMassOrVolume
                        minContains: 0
                        maxContains: 1
                  required:
                  - schema:description
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                        const: Data processing
                    required:
                    - schema:name
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                  allOf:
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
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
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
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
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
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
                    const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
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
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Within-Session Analytical Precision
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
              const: Analytical Accuracy
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld)

## Sources

* [Solution_Q-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail`

