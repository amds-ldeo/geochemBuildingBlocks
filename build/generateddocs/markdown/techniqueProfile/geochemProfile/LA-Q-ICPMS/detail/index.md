
# LA-Q-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Nakanishi2022
detail instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology.
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
  "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)"
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
          "schema:value": "N/A — spot mode"
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
          "schema:value": 0.9,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.9–1.2 L/min — Table 1, 'Make-up gas'"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 1,
          "schema:description": "1–3 spots per metal grain — 'the mean Re/Os abundance ratios for each of the 1–3 analytical spots' (Table 3)"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 16,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "Ar, plasma gas 16 L/min; cool gas 12–13 L/min — Table 1 lists both rows under 'Ar gas flow rate'"
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
                  "schema:value": 0.6,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "Ar, 0.6–1.2 L/min — Table 1, 'Auxiliary'"
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
                  "schema:value": 1400,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1400 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/Collision-Reaction-Cell"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS"
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 30 µm diameter — 'Each spot analysis on the sample produced a pit of 30 µm in diameter' (p.3)",
          "ada:laserFluence": "12 J cm⁻²",
          "ada:laserRepetitionRate": "all: 20 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "Tawallah Valley (IVB iron meteorite) — 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
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
                "schema:value": "N — ²⁴Mg, ²⁹Si, ³¹P and ³³S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 µm diamond paste; carbon-coated before the EPMA measurements (§2.1–2.2). Whether the coat was removed before ablation is not stated; the later 0.5 µm polish (§2.5) preceded micromilling, not ablation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan"
      },
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N — the 2SE is stated for individual measurements (p.4), not for a standard"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (electron probe microanalysis)",
        "schema:description": "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: metal grains by host chondrule within each section — e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) — in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N — LODs not formally stated",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot \u2014 \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 \u2026) that tie the analyses back to those images (table p.6)"
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
          "schema:value": "N/A \u2014 spot mode"
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
          "schema:value": 0.9,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.9\u20131.2 L/min \u2014 Table 1, 'Make-up gas'"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 1,
          "schema:description": "1\u20133 spots per metal grain \u2014 'the mean Re/Os abundance ratios for each of the 1\u20133 analytical spots' (Table 3)"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 16,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "Ar, plasma gas 16 L/min; cool gas 12\u201313 L/min \u2014 Table 1 lists both rows under 'Ar gas flow rate'"
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
                  "schema:value": 0.6,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "Ar, 0.6\u20131.2 L/min \u2014 Table 1, 'Auxiliary'"
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
                  "schema:value": 1400,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1400 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/Collision-Reaction-Cell"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS"
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 30 \u00b5m diameter \u2014 'Each spot analysis on the sample produced a pit of 30 \u00b5m in diameter' (p.3)",
          "ada:laserFluence": "12 J cm\u207b\u00b2",
          "ada:laserRepetitionRate": "all: 20 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Nakanishi2022/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "Tawallah Valley (IVB iron meteorite) \u2014 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
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
                "schema:value": "N \u2014 \u00b2\u2074Mg, \u00b2\u2079Si, \u00b3\u00b9P and \u00b3\u00b3S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 \u00b5m diamond paste; carbon-coated before the EPMA measurements (\u00a72.1\u20132.2). Whether the coat was removed before ablation is not stated; the later 0.5 \u00b5m polish (\u00a72.5) preceded micromilling, not ablation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan"
      },
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N \u2014 the 2SE is stated for individual measurements (p.4), not for a standard"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (electron probe microanalysis)",
        "schema:description": "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: metal grains by host chondrule within each section \u2014 e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) \u2014 in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N \u2014 LODs not formally stated",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Nakanishi2022 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]" ;
                    schema1:name "EPMA (electron probe microanalysis)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "N — the 2SE is stated for individual measurements (p.4), not for a standard" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 µm diamond paste; carbon-coated before the EPMA measurements (§2.1–2.2). Whether the coat was removed before ablation is not stated; the later 0.5 µm polish (§2.5) preceded micromilling, not ablation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "Tawallah Valley (IVB iron meteorite) — 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "N — LODs not formally stated" ;
    ada:fundingSourceForAnalysis "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: metal grains by host chondrule within each section — e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) — in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 .

<https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-Nakanishi2022/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "12 J cm⁻²" ;
    ada:laserRepetitionRate "all: 20 Hz" ;
    ada:laserSpotGeometry "all: 30 µm diameter — 'Each spot analysis on the sample produced a pit of 30 µm in diameter' (p.3)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "1–3 spots per metal grain — 'the mean Re/Os abundance ratios for each of the 1–3 analytical spots' (Table 3)" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.6–1.2 L/min — Table 1, 'Auxiliary'" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, plasma gas 16 L/min; cool gas 12–13 L/min — Table 1 lists both rows under 'Ar gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 16 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "N — ²⁴Mg, ²⁹Si, ³¹P and ³³S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.9–1.2 L/min — Table 1, 'Make-up gas'" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1400 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1400 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)" .


```


### detail example Liu2024
detail instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences.
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
  "@id": "ex:laQicpmsTAPP-detail-Liu2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "Surface cleaning with ethanol before analysis"
              }
            ],
            "schema:description": "Li2B4O7 flux (350.0 ± 0.3 mg) and powdered sample (10.00 ± 0.03 mg) weighed into a small Pt–Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (§2.3)",
            "@type": [
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
                "schema:value": "N — Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
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
          "schema:value": "N/A — spot mode"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 9,
          "schema:description": "9 spots per glass disk — 'Nine spot analyses (spot size = 100 µm) were arranged in a grid pattern to cover the entire glass' (§3.1); Table 2 'n = 9 spots'"
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
          "schema:value": 45,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N — ablation lasted 45 s (§2.2); the integration interval is not stated"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:description": "15 L/min — Table 1 'Plasma gas flow'"
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
                  "schema:value": 0.85,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.85 L/min — Table 1 'Auxiliary gas flow'"
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
                  "schema:value": 1550,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1550 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95–1.05' (§2.2); sampling depth 8 mm (Table 1)"
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
              "schema:value": "25 s washout between analyses — §2.2"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Iolite 4 (Paton et al. 2011)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 100 µm — '100 µm-diameter ablating spots' (§2.2); Table 1 gives 'Ablation spot size 100 × 100 µm'",
          "ada:laserFluence": "6.79 J cm⁻²",
          "ada:laserRepetitionRate": "all: 1 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A — six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (§2.1); reference values from GeoReM (§3.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China"
      },
      "ada:ablationSpotDuration": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] — §3.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] — §3.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: relative standard deviation — 'relative standard deviations are reported as the precision measure'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)"
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
      "schema:name": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: 0.005–23.5 µg g⁻¹ — LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007–0.45 µg g⁻¹ calculated for NIST 610 (§3.2)",
  "ada:limitOfQuantificationMethod": "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 × LOD — §3.2",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Liu2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "Li\u2082B\u2084O\u2087 flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "Surface cleaning with ethanol before analysis"
              }
            ],
            "schema:description": "Li2B4O7 flux (350.0 \u00b1 0.3 mg) and powdered sample (10.00 \u00b1 0.03 mg) weighed into a small Pt\u2013Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (\u00a72.3)",
            "@type": [
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
                "schema:value": "N \u2014 Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "N \u2014 the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
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
          "schema:value": "N/A \u2014 spot mode"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 9,
          "schema:description": "9 spots per glass disk \u2014 'Nine spot analyses (spot size = 100 \u00b5m) were arranged in a grid pattern to cover the entire glass' (\u00a73.1); Table 2 'n = 9 spots'"
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
          "schema:value": 45,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N \u2014 ablation lasted 45 s (\u00a72.2); the integration interval is not stated"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:description": "15 L/min \u2014 Table 1 'Plasma gas flow'"
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
                  "schema:value": 0.85,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.85 L/min \u2014 Table 1 'Auxiliary gas flow'"
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
                  "schema:value": 1550,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1550 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95\u20131.05' (\u00a72.2); sampling depth 8 mm (Table 1)"
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
              "schema:value": "25 s washout between analyses \u2014 \u00a72.2"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Iolite 4 (Paton et al. 2011)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 100 \u00b5m \u2014 '100 \u00b5m-diameter ablating spots' (\u00a72.2); Table 1 gives 'Ablation spot size 100 \u00d7 100 \u00b5m'",
          "ada:laserFluence": "6.79 J cm\u207b\u00b2",
          "ada:laserRepetitionRate": "all: 1 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2024/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A \u2014 six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (\u00a72.1); reference values from GeoReM (\u00a73.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China"
      },
      "ada:ablationSpotDuration": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] \u2014 \u00a73.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] \u2014 \u00a73.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: relative standard deviation \u2014 'relative standard deviations are reported as the precision measure'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "ThO/Th = measured at <0.3%; U/Th = 0.95\u20131.05 (on NIST SRM 612)"
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
      "schema:name": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95\u20131.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: 0.005\u201323.5 \u00b5g g\u207b\u00b9 \u2014 LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007\u20130.45 \u00b5g g\u207b\u00b9 calculated for NIST 610 (\u00a73.2)",
  "ada:limitOfQuantificationMethod": "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 \u00d7 LOD \u2014 \u00a73.2",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Liu2024 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: relative standard deviation — 'relative standard deviations are reported as the precision measure'" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] — §3.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] — §3.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio>,
                                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
                            schema1:description "Li2B4O7 flux (350.0 ± 0.3 mg) and powdered sample (10.00 ± 0.03 mg) weighed into a small Pt–Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (§2.3)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A — six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (§2.1); reference values from GeoReM (§3.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS" ;
                    ada:reagentRole "referenceMaterial" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Iolite 4 (Paton et al. 2011)" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:ablationSpotDuration "45 s ablation (after 25 s gas blank; 25 s washout between analyses)" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "all: 0.005–23.5 µg g⁻¹ — LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007–0.45 µg g⁻¹ calculated for NIST 610 (§3.2)" ;
    ada:fundingSourceForAnalysis "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ;
    ada:limitOfQuantificationMethod "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 × LOD — §3.2" ;
    ada:mappingArea "missing" ;
    ada:oxideProduction "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 .

<https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2024/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "6.79 J cm⁻²" ;
    ada:laserRepetitionRate "all: 1 Hz" ;
    ada:laserSpotGeometry "all: 100 µm — '100 µm-diameter ablating spots' (§2.2); Table 1 gives 'Ablation spot size 100 × 100 µm'" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "9 spots per glass disk — 'Nine spot analyses (spot size = 100 µm) were arranged in a grid pattern to cover the entire glass' (§3.1); Table 2 'n = 9 spots'" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> ;
    schema1:value 9 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.85 L/min — Table 1 'Auxiliary gas flow'" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.5e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "15 L/min — Table 1 'Plasma gas flow'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95–1.05' (§2.2); sampling depth 8 mm (Table 1)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "25 s washout between analyses — §2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1550 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1550 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "N — ablation lasted 45 s (§2.2); the integration interval is not stated" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 45 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> a schema1:PropertyValue ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> ;
    schema1:value "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> a schema1:PropertyValue ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
    schema1:value "Surface cleaning with ethanol before analysis" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described" .


```


### detail example Liu2025
detail instance derived from Liu et al. 2025 (GCA 393) Experimental silicate glass Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsTAPP-detail-Liu2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
          "schema:value": "N/A — spot mode"
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
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
                "schema:value": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)"
      },
      "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 40 µm beam diameter — 'a 40 μm beam diameter for glasses' (§2.2.2)",
          "ada:laserFluence": "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")",
          "ada:laserRepetitionRate": "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "ICPMS",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025/instrument/ICPMS"
        }
      ],
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Au: ~0.01 ppm; Cu: ~0.1 ppm — 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (§2.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Liu2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
          "schema:value": "N/A \u2014 spot mode"
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated \u2014 \u00a72.2.2"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
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
                "schema:value": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered \u2014 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (\u00a72.2.2)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (\u00a72.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology \u2014 LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (\u00a72.2.2)"
      },
      "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 40 \u00b5m beam diameter \u2014 'a 40 \u03bcm beam diameter for glasses' (\u00a72.2.2)",
          "ada:laserFluence": "~2.5 J cm\u207b\u00b2 (stated as \"energy of ~2.5 J/cm\u00b2\")",
          "ada:laserRepetitionRate": "all: 7 Hz \u2014 'operated at 7 Hz ablation frequency' (\u00a72.2.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NIST 612; BCR-2G \u2014 'NIST 612 and BCR-2G as monitoring standards' (\u00a72.2.2)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "ICPMS",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025/instrument/ICPMS"
        }
      ],
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Au: ~0.01 ppm; Cu: ~0.1 ppm \u2014 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (\u00a72.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Liu2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/laQicpmsTAPP-detail-Liu2025/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Liu2025/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Au: ~0.01 ppm; Cu: ~0.1 ppm — 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (§2.2.2)" ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2025/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:name "ICPMS" .

<https://example.org/laQicpmsTAPP-detail-Liu2025/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")" ;
    ada:laserRepetitionRate "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)" ;
    ada:laserSpotGeometry "all: 40 µm beam diameter — 'a 40 μm beam diameter for glasses' (§2.2.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .


```


### detail example Liu2025-2
detail instance derived from Liu et al. 2025 (GCA 393) Experimental sulfide Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsTAPP-detail-Liu2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
          "schema:value": "N/A — spot mode"
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
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
                "schema:value": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)"
      },
      "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 20 µm beam diameter — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)",
          "ada:laserFluence": "~2.5 J cm⁻²",
          "ada:laserRepetitionRate": "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025-2/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "ICPMS",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025-2/instrument/ICPMS"
        }
      ],
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N — detection limits are stated for silicate melts only (§2.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Liu2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
          "schema:value": "N/A \u2014 spot mode"
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated \u2014 \u00a72.2.2"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
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
                "schema:value": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered \u2014 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (\u00a72.2.2)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (\u00a72.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology \u2014 LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (\u00a72.2.2)"
      },
      "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 20 \u00b5m beam diameter \u2014 '20 \u03bcm for sulfides, selecting grain sizes larger than 20 \u00b5m for the latter' (\u00a72.2.2)",
          "ada:laserFluence": "~2.5 J cm\u207b\u00b2",
          "ada:laserRepetitionRate": "all: 7 Hz \u2014 'operated at 7 Hz ablation frequency' (\u00a72.2.2)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025-2/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NIST 612; BCR-2G \u2014 'NIST 612 and BCR-2G as monitoring standards' (\u00a72.2.2)",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "ICPMS",
          "@id": "ex:laQicpmsTAPP-detail-Liu2025-2/instrument/ICPMS"
        }
      ],
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N \u2014 detection limits are stated for silicate melts only (\u00a72.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Liu2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/laQicpmsTAPP-detail-Liu2025-2/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Liu2025-2/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "N — detection limits are stated for silicate melts only (§2.2.2)" ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2025-2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:name "ICPMS" .

<https://example.org/laQicpmsTAPP-detail-Liu2025-2/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "~2.5 J cm⁻²" ;
    ada:laserRepetitionRate "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)" ;
    ada:laserSpotGeometry "all: 20 µm beam diameter — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .


```


### detail example Liu2016
detail instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Silicates, oxides & glass Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsTAPP-detail-Liu2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "N/A — in situ"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N — not stated"
              }
            ],
            "schema:description": "N — sections UT1 to UT3 (p.3); their preparation is not described",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
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
                "schema:value": "N — not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
          "schema:value": "N/A — spot analysis"
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
          "schema:value": "N — not stated",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N — not stated"
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
          "schema:value": "N/A — spot analysis",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A — spot analysis"
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
          "schema:value": "N — not stated",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/LaserAblation/laserEnergy",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/LaserAblation/laserEnergy"
                }
              ],
              "schema:name": "Laser Energy",
              "schema:value": 150,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "150 mJ output energy — Methods, p.4"
            }
          ],
          "ada:laserSpotGeometry": "all: 24 and 32 µm diameter, and 90 µm for a few olivine analyses — '24 and 32 µm diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 µm beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)",
          "ada:laserFluence": "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)",
          "ada:laserRepetitionRate": "all: 5 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/Laser-Ablation-System"
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": "N — not stated",
                  "schema:unitText": "no value available: unnamed property"
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
                  "schema:value": "N — not stated",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "N — not stated"
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
              "schema:value": "N — not stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "N — not stated",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Geosciences, Virginia Tech"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Tissint Martian meteorite"
        }
      ],
      "schema:description": "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 µm beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)",
      "ada:ablationSpotDuration": "N — not stated",
      "ada:rasterLineSpacing": "N/A — spot analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 1σ, one standard deviation of the average — Table 3 note b: '1σ is 1 standard deviation of the average'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "N — not stated"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' — Methods, p.4"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N — not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N — ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Liu2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "N/A \u2014 in situ"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N \u2014 not stated"
              }
            ],
            "schema:description": "N \u2014 sections UT1 to UT3 (p.3); their preparation is not described",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
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
                "schema:value": "N \u2014 not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
          "schema:value": "N/A \u2014 spot analysis"
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
          "schema:value": "N \u2014 not stated",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N \u2014 not stated"
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
          "schema:value": "N/A \u2014 spot analysis",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A \u2014 spot analysis"
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
          "schema:value": "N \u2014 not stated",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/LaserAblation/laserEnergy",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/LaserAblation/laserEnergy"
                }
              ],
              "schema:name": "Laser Energy",
              "schema:value": 150,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "150 mJ output energy \u2014 Methods, p.4"
            }
          ],
          "ada:laserSpotGeometry": "all: 24 and 32 \u00b5m diameter, and 90 \u00b5m for a few olivine analyses \u2014 '24 and 32 \u00b5m diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 \u00b5m beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)",
          "ada:laserFluence": "7\u201310 J/m\u00b2 \u2014 as written: 'a fluence rate of 7\u201310 J/m2 on the sample' (Methods, p.4)",
          "ada:laserRepetitionRate": "all: 5 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/Laser-Ablation-System"
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": "N \u2014 not stated",
                  "schema:unitText": "no value available: unnamed property"
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
                  "schema:value": "N \u2014 not stated",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "N \u2014 not stated"
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
              "schema:value": "N \u2014 not stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "N \u2014 not stated",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Geosciences, Virginia Tech"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Tissint Martian meteorite"
        }
      ],
      "schema:description": "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 \u00b5m beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)",
      "ada:ablationSpotDuration": "N \u2014 not stated",
      "ada:rasterLineSpacing": "N/A \u2014 spot analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 1\u03c3, one standard deviation of the average \u2014 Table 3 note b: '1\u03c3 is 1 standard deviation of the average'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "N \u2014 not stated"
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
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' \u2014 Methods, p.4"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N \u2014 not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N \u2014 ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Liu2016 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' — Methods, p.4" ;
                    schema1:name "EPMA (EMP)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "N — not stated" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 1σ, one standard deviation of the average — Table 3 note b: '1σ is 1 standard deviation of the average'" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio>,
                                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
                            schema1:description "N — sections UT1 to UT3 (p.3); their preparation is not described" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 µm beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "N — not stated" ;
                    ada:reagentRole "referenceMaterial" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Department of Geosciences, Virginia Tech" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "Tissint Martian meteorite" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:ablationSpotDuration "N — not stated" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot analysis" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N — ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)" ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "N — not stated" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2016/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)" ;
    ada:laserRepetitionRate "all: 5 Hz" ;
    ada:laserSpotGeometry "all: 24 and 32 µm diameter, and 90 µm for a few olivine analyses — '24 and 32 µm diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 µm beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> a schema1:PropertyValue ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> ;
    schema1:value "N/A — in situ" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> a schema1:PropertyValue ;
    schema1:description "150 mJ output energy — Methods, p.4" ;
    schema1:name "Laser Energy" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 150 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> a schema1:PropertyValue ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> a schema1:PropertyValue ;
    schema1:name "Signal Smoothing" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> a schema1:PropertyValue ;
    schema1:name "Transect Length" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .


```


### detail example Liu2016-2
detail instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsTAPP-detail-Liu2016-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "N/A — in situ"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N — not stated"
              }
            ],
            "schema:description": "N — sections UT1 to UT3 (p.3); their preparation is not described",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
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
                "schema:value": "N — not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
          "schema:value": "N/A — spot analysis"
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
          "schema:value": "N — not stated",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N — not stated"
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
          "schema:value": "N/A — spot analysis",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A — spot analysis"
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
          "schema:value": "N — not stated",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/LaserAblation/laserEnergy",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/LaserAblation/laserEnergy"
                }
              ],
              "schema:name": "Laser Energy",
              "schema:value": 150,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "150 mJ output energy — Methods, p.4"
            }
          ],
          "ada:laserSpotGeometry": "all: ~24 µm diameter — 'The smaller spot (~24 µm) size was used for phosphate analysis' (Methods, p.4)",
          "ada:laserFluence": "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)",
          "ada:laserRepetitionRate": "all: 5 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/Laser-Ablation-System"
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": "N — not stated",
                  "schema:unitText": "no value available: unnamed property"
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
                  "schema:value": "N — not stated",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "N — not stated"
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
              "schema:value": "N — not stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "N — not stated",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Geosciences, Virginia Tech"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Tissint Martian meteorite"
        }
      ],
      "ada:ablationSpotDuration": "N — not stated",
      "ada:rasterLineSpacing": "N/A — spot analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' — Methods, p.4"
      }
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "N — not stated"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N — not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N — Table 3's LODs are for the glasses",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-Liu2016-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatio"
                  }
                ],
                "schema:name": "Fusion Flux and Dilution Ratio",
                "schema:value": "N/A \u2014 in situ"
              },
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N \u2014 not stated"
              }
            ],
            "schema:description": "N \u2014 sections UT1 to UT3 (p.3); their preparation is not described",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
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
                "schema:value": "N \u2014 not stated"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
            }
          ],
          "schema:name": "Pre-Analysis Imaging and Screening",
          "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
          "schema:value": "N/A \u2014 spot analysis"
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
          "schema:value": "N \u2014 not stated",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N \u2014 not stated"
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
          "schema:value": "N/A \u2014 spot analysis",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A \u2014 spot analysis"
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
          "schema:value": "N \u2014 not stated",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/LaserAblation/laserEnergy",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/LaserAblation/laserEnergy"
                }
              ],
              "schema:name": "Laser Energy",
              "schema:value": 150,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "150 mJ output energy \u2014 Methods, p.4"
            }
          ],
          "ada:laserSpotGeometry": "all: ~24 \u00b5m diameter \u2014 'The smaller spot (~24 \u00b5m) size was used for phosphate analysis' (Methods, p.4)",
          "ada:laserFluence": "7\u201310 J/m\u00b2 \u2014 as written: 'a fluence rate of 7\u201310 J/m2 on the sample' (Methods, p.4)",
          "ada:laserRepetitionRate": "all: 5 Hz",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/Laser-Ablation-System"
        },
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": "N \u2014 not stated",
                  "schema:unitText": "no value available: unnamed property"
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
                  "schema:value": "N \u2014 not stated",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "Collision Reaction Cell",
              "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "schema:value": "N \u2014 not stated"
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
              "schema:value": "N \u2014 not stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "N \u2014 not stated",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Geosciences, Virginia Tech"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Tissint Martian meteorite"
        }
      ],
      "ada:ablationSpotDuration": "N \u2014 not stated",
      "ada:rasterLineSpacing": "N/A \u2014 spot analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' \u2014 Methods, p.4"
      }
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "N \u2014 not stated"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N \u2014 not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N \u2014 Table 3's LODs are for the glasses",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-Liu2016-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' — Methods, p.4" ;
                    schema1:name "EPMA (EMP)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "N — not stated" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio>,
                                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
                            schema1:description "N — sections UT1 to UT3 (p.3); their preparation is not described" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "AMS ver. 1.0 (Mutchler et al. 2008)" ;
                    ada:toolRole "dataReduction" ],
                [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "N — not stated" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Department of Geosciences, Virginia Tech" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "Tissint Martian meteorite" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:ablationSpotDuration "N — not stated" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot analysis" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "N — Table 3's LODs are for the glasses" ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "N — not stated" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-Liu2016-2/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)" ;
    ada:laserRepetitionRate "all: 5 Hz" ;
    ada:laserSpotGeometry "all: ~24 µm diameter — 'The smaller spot (~24 µm) size was used for phosphate analysis' (Methods, p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/numberOfReplicates> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> a schema1:PropertyValue ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatio> ;
    schema1:value "N/A — in situ" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> a schema1:PropertyValue ;
    schema1:description "150 mJ output energy — Methods, p.4" ;
    schema1:name "Laser Energy" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergy> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 150 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> a schema1:PropertyValue ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> a schema1:PropertyValue ;
    schema1:name "Signal Smoothing" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
    schema1:value "N — not stated" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> a schema1:PropertyValue ;
    schema1:name "Transect Length" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot analysis" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .


```


### detail example P6
detail instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS.
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
  "@id": "ex:laQicpmsTAPP-detail-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
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
              "schema:value": "~300"
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
              "schema:value": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 15.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15.00 L min-1 Ar"
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
                  "schema:value": 0.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.80 L min-1 Ar"
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
                  "schema:value": 1350,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1350 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltage"
                    }
                  ],
                  "schema:name": "Cell Exit Discrimination Voltage",
                  "schema:value": -40.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 50, 90, 150 µm — Table 1 'Spot size'; chosen according to Lu and Hf contents",
          "ada:laserFluence": "4 J cm-2",
          "ada:laserRepetitionRate": "all: 10 Hz — Table 1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-P6/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 — ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U–Pb reference materials test the Lu–Hf ages against their ID-TIMS U–Pb ages",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint"
            }
          ],
          "schema:name": "Total Integration Time per Output Data Point",
          "schema:value": 0.659,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.659 s"
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
          "schema:value": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio"
            }
          ],
          "schema:name": "Collision/Reaction Gas Mixture Ratio",
          "schema:value": "all: high-purity NH3 — found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
      },
      "schema:identifier": "N — 20 analytical sessions over 3 months referenced, no identifier stated",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N — not described; §2.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "ada:ablationSpotDuration": "25 s",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5–8.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2–36.0%] — isochron age uncertainties of 3.5–10% for the garnet samples"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] — against ID-TIMS U–Pb ages of the same reference materials"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 ± 2.2 Ma)"
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
  "ada:spotDiameterMeasured": "50, 90, 150 um",
  "ada:sessionIdentifier": "N — 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnitName": "Sample name only — \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-detail-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "ICPMS",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
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
              "schema:value": "~300"
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
              "schema:value": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 15.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15.00 L min-1 Ar"
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
                  "schema:value": 0.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.80 L min-1 Ar"
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
                  "schema:value": 1350,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1350 W"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Collision Reaction Cell",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltage"
                    }
                  ],
                  "schema:name": "Cell Exit Discrimination Voltage",
                  "schema:value": -40.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-P6/instrument/ICPMS"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "Laser Ablation System",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "ada:laserSpotGeometry": "all: 50, 90, 150 \u00b5m \u2014 Table 1 'Spot size'; chosen according to Lu and Hf contents",
          "ada:laserFluence": "4 J cm-2",
          "ada:laserRepetitionRate": "all: 10 Hz \u2014 Table 1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:laQicpmsTAPP-detail-P6/instrument/Laser-Ablation-System"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 \u2014 ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U\u2013Pb reference materials test the Lu\u2013Hf ages against their ID-TIMS U\u2013Pb ages",
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q2356542"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
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
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint"
            }
          ],
          "schema:name": "Total Integration Time per Output Data Point",
          "schema:value": 0.659,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.659 s"
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
          "schema:value": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio"
            }
          ],
          "schema:name": "Collision/Reaction Gas Mixture Ratio",
          "schema:value": "all: high-purity NH3 \u2014 found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
      },
      "schema:identifier": "N \u2014 20 analytical sessions over 3 months referenced, no identifier stated",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N \u2014 not described; \u00a72.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "ada:ablationSpotDuration": "25 s",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5\u20138.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2\u201336.0%] \u2014 isochron age uncertainties of 3.5\u201310% for the garnet samples"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] \u2014 against ID-TIMS U\u2013Pb ages of the same reference materials"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N \u2014 e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 \u00b1 2.2 Ma)"
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
  "ada:spotDiameterMeasured": "50, 90, 150 um",
  "ada:sessionIdentifier": "N \u2014 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnitName": "Sample name only \u2014 \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:laQicpmsTAPP-detail-P6 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 ± 2.2 Ma)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5–8.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2–36.0%] — isochron age uncertainties of 3.5–10% for the garnet samples" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] — against ID-TIMS U–Pb ages of the same reference materials" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "N — not described; §2.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio>,
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint>,
                <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N — 20 analytical sessions over 3 months referenced, no identifier stated" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 — ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U–Pb reference materials test the Lu–Hf ages against their ID-TIMS U–Pb ages" ;
                    ada:reagentRole "referenceMaterial" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS>,
                <https://example.org/laQicpmsTAPP-detail-P6/instrument/Laser-Ablation-System> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:ablationSpotDuration "25 s" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610" ;
    ada:samplingUnitName "Sample name only — \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled" ;
    ada:sessionIdentifier "N — 20 analytical sessions over 3 months referenced, no identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter 50 ;
    ada:spotDiameterMeasured "50, 90, 150 um" ;
    ada:transectLength -9999 .

<https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/cellExitDiscriminationVoltage> ;
    schema1:additionalType wd:Q3099911,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laQicpmsTAPP-detail-P6/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "4 J cm-2" ;
    ada:laserRepetitionRate "all: 10 Hz — Table 1" ;
    ada:laserSpotGeometry "all: 50, 90, 150 µm — Table 1 'Spot size'; chosen according to Lu and Hf contents" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio> a schema1:PropertyValue ;
    schema1:name "Collision/Reaction Gas Mixture Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio> ;
    schema1:value "all: high-purity NH3 — found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint> a schema1:PropertyValue ;
    schema1:description "0.659 s" ;
    schema1:name "Total Integration Time per Output Data Point" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6.59e-01 .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/cellExitDiscriminationVoltage> a schema1:PropertyValue ;
    schema1:description "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)" ;
    schema1:name "Cell Exit Discrimination Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/CollisionCell/cellExitDiscriminationVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value -4e+01 .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.80 L min-1 Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "15.00 L min-1 Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.5e+01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "~300" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1350 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1350 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              - title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/ionCounterDeadTime
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
              - title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
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
                    const: ada:parameter/laQicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/numberOfReplicates
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              minContains: 0
              maxContains: 1
            - contains:
                title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/ionCounterDeadTime
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
            - contains:
                title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
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
                    const: ada:parameter/laQicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/numberOfReplicates
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                    const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
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
          schema:instrument:
            type: array
            items:
              type: object
              allOf:
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindInstrument
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindSoftware
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedComputationalTool
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindReagent
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedReagent
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
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                allOf:
                                - contains:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                  minContains: 0
                                  maxContains: 1
                                - contains:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                        - title: Doubly-Charged Species Monitor
                          description: "The mass ratio monitored to estimate doubly-charged
                            ion (M\xB2\u207A) formation during instrument tuning.
                            The monitor species and the mass positions monitored should
                            be stated explicitly. Analogous to Oxide Production Method
                            and Threshold for oxide monitoring."
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
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
                          description: Measured percentage of doubly-charged ion production
                            for the monitored species at the time of instrument tuning.
                            The acceptable threshold is typically <1% or <3%. Record
                            both the threshold and the measured value.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
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
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                        minContains: 0
                        maxContains: 1
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Doubly-Charged Species Monitor
                          description: "The mass ratio monitored to estimate doubly-charged
                            ion (M\xB2\u207A) formation during instrument tuning.
                            The monitor species and the mass positions monitored should
                            be stated explicitly. Analogous to Oxide Production Method
                            and Threshold for oxide monitoring."
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
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
                          description: Measured percentage of doubly-charged ion production
                            for the monitored species at the time of instrument tuning.
                            The acceptable threshold is typically <1% or <3%. Record
                            both the threshold and the measured value.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
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
  itemIdentifier: ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld)

## Sources

* [LA-Q-ICP-MS_TAPP_v15.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail`

