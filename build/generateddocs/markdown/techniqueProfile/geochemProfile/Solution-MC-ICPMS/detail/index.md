
# Solution MC-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from Budde+etal2016 | Neptune Plus | IfP Münster.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P0",
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
              "schema:value": 0.3,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "0.3–0.5 g digested; ~100 ng Mo consumed per measurement"
            }
          ],
          "schema:name": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
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
                      "schema:value": 50,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~50 µl/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2 — 'several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples'",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Mo: 0.7–1.2 ng — 'negligible, given that several hundred ng of Mo were analyzed for each sample'",
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
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
                "schema:value": "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half"
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
            "schema:description": "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material",
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
      "schema:additionalProperty": [
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
          "schema:value": 100,
          "schema:description": "all: 100 isotope ratio measurements, preceded by 40 baseline integrations — §2"
        },
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
          "schema:value": 8.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.4 s — §2"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Mo: Alfa Aesar Mo solution standard — mean of bracketing runs",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut für Planetologie, University of Münster"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2 [all: εⁱMo indistinguishable from the Alfa Aesar standard] — §2"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2 [all: ±0.14 (ε97Mo) to ±0.39 (ε92Mo), 2 s.d., n = 24] — external reproducibility (§2, Table S2); Ba by TIMS ±0.13–0.31 (n = 14)"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TIMS — Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N — total ion beam ~1.3 × 10⁻¹⁰ A for a ~100 ppb Mo solution at ~50 µl/min",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnitName": "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2–C4c\" in the same table are weighted means, not units. BHVO-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P0",
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
              "schema:value": 0.3,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "0.3\u20130.5 g digested; ~100 ng Mo consumed per measurement"
            }
          ],
          "schema:name": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
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
                      "schema:value": 50,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~50 \u00b5l/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P0/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2 \u2014 'several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples'",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Mo: 0.7\u20131.2 ng \u2014 'negligible, given that several hundred ng of Mo were analyzed for each sample'",
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
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
                "schema:value": "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half"
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
            "schema:description": "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material",
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
      "schema:additionalProperty": [
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
          "schema:value": 100,
          "schema:description": "all: 100 isotope ratio measurements, preceded by 40 baseline integrations \u2014 \u00a72"
        },
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
          "schema:value": 8.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.4 s \u2014 \u00a72"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Mo: Alfa Aesar Mo solution standard \u2014 mean of bracketing runs",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut f\u00fcr Planetologie, University of M\u00fcnster"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2 [all: \u03b5\u2071Mo indistinguishable from the Alfa Aesar standard] \u2014 \u00a72"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2 [all: \u00b10.14 (\u03b597Mo) to \u00b10.39 (\u03b592Mo), 2 s.d., n = 24] \u2014 external reproducibility (\u00a72, Table S2); Ba by TIMS \u00b10.13\u20130.31 (n = 14)"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TIMS \u2014 Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N \u2014 total ion beam ~1.3 \u00d7 10\u207b\u00b9\u2070 A for a ~100 ppb Mo solution at ~50 \u00b5l/min",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnitName": "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2\u2013C4c\" in the same table are weighted means, not units. BHVO-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P0 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TIMS — Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-2 [all: εⁱMo indistinguishable from the Alfa Aesar standard] — §2" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "BHVO-2 [all: ±0.14 (ε97Mo) to ±0.39 (ε92Mo), 2 s.d., n = 24] — external reproducibility (§2, Table S2); Ba by TIMS ±0.13–0.31 (n = 14)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institut für Planetologie, University of Münster" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2 — 'several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples'" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Mo: Alfa Aesar Mo solution standard — mean of bracketing runs" ;
            ada:proceduralBlankLevel "Mo: 0.7–1.2 ng — 'negligible, given that several hundred ng of Mo were analyzed for each sample'" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2" ;
    ada:samplingUnitName "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2–C4c\" in the same table are weighted means, not units. BHVO-2 by name only" ;
    ada:sensitivityYield "N — total ion beam ~1.3 × 10⁻¹⁰ A for a ~100 ppb Mo solution at ~50 µl/min" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 8.4 s — §2" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.4e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 100 isotope ratio measurements, preceded by 40 baseline integrations — §2" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "0.3–0.5 g digested; ~100 ng Mo consumed per measurement" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~50 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .


```


### detail example P1
detail instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P1",
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
                "schema:description": "HNO3 attack: below 70 °C; HNO3–HCl digestion: 70 °C; re-dissolution: N — §2.2"
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
                "schema:value": "N — 'taken to dryness'"
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
                "schema:value": "None, no automatic 2σ rejection of outlying cycles — 'Automatic rejection of outlying cycles (2σ outlier criterion) offered within the NEPTUNE software is not performed' (§2.4)"
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
            "schema:description": "Less than 50 mg weighed, digested, S purified on AG50-X8 cation exchange and diluted with 2% HNO3 to a 50 ppm S stock; for laser work, a 2 mm thick polished section on a petrographic slide — §2.1–2.2",
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
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<50 mg weighed; 500 µg S taken for column purification"
            }
          ],
          "schema:name": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
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
                      "schema:value": 50,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "50 µL/min"
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
                      "schema:value": 0.8,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~0.8–0.9 L/min Ar (sample gas)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1150,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~1150 W"
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
                      "schema:description": "~15 L/min Ar"
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
                      "schema:description": "~0.8 L/min Ar"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Wash-out 2 min for solution"
                },
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "N — ⁶⁴Zn²⁺, ⁶⁶Zn²⁺ and ⁶⁸Zn²⁺ are listed as interferences on the S masses, Table 2, p.4, and resolved by mass resolution, p.5; no M²⁺ tuning monitor or production ratio is stated"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123, Alfa, Sch-M-2, SW-Woods Hole, FeIII-sulfate, GAV-18, Ward's Py, Ward's Po — Table 3",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "S: ~0.05% (~0.25 µg per 500 µg S) — §2.2",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "all: 20 cycles — Table 1, §2.4"
        },
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
          "schema:value": 8.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.5 s — Table 1, §2.4"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (δ34S = −0.3‰) — §2.4",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Woods Hole Oceanographic Institution"
      },
      "schema:description": "Laser half: NewWave UP213 (213 nm), He carrier, 60 µm spot, 180 × 80 µm raster, 5 µm/s, 10 Hz, ~9–10 J/cm², ablated aerosol mixed with 2% HNO3 in the spray chamber — Table 1",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [δ34S: consistent with published consensus values within uncertainty] — §2.4, Table 3"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "Alfa [δ34S: ±0.21‰, 2σ, 20–30 replicates]; Sch-M-2 [δ34S: ±0.45‰, 2σ, 12 replicates, laser] — §3.2; S_Spex ±0.18‰; δ³³S an order of magnitude worse"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "δ34S, δ33S: two standard deviations of the replicates — Table 3 note"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-ablation MC-ICP-MS — the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"",
        "schema:description": "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable — \"Our setup allows for interchangeable bulk and in situ S isotope measurement\""
      }
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
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnitName": "Sample name only — Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P1",
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
                "schema:description": "HNO3 attack: below 70 \u00b0C; HNO3\u2013HCl digestion: 70 \u00b0C; re-dissolution: N \u2014 \u00a72.2"
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
                "schema:value": "N \u2014 'taken to dryness'"
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
                "schema:value": "None, no automatic 2\u03c3 rejection of outlying cycles \u2014 'Automatic rejection of outlying cycles (2\u03c3 outlier criterion) offered within the NEPTUNE software is not performed' (\u00a72.4)"
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
            "schema:description": "Less than 50 mg weighed, digested, S purified on AG50-X8 cation exchange and diluted with 2% HNO3 to a 50 ppm S stock; for laser work, a 2 mm thick polished section on a petrographic slide \u2014 \u00a72.1\u20132.2",
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
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<50 mg weighed; 500 \u00b5g S taken for column purification"
            }
          ],
          "schema:name": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
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
                      "schema:value": 50,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "50 \u00b5L/min"
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
                      "schema:value": 0.8,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~0.8\u20130.9 L/min Ar (sample gas)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1150,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~1150 W"
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
                      "schema:description": "~15 L/min Ar"
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
                      "schema:description": "~0.8 L/min Ar"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Wash-out 2 min for solution"
                },
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "N \u2014 \u2076\u2074Zn\u00b2\u207a, \u2076\u2076Zn\u00b2\u207a and \u2076\u2078Zn\u00b2\u207a are listed as interferences on the S masses, Table 2, p.4, and resolved by mass resolution, p.5; no M\u00b2\u207a tuning monitor or production ratio is stated"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P1/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123, Alfa, Sch-M-2, SW-Woods Hole, FeIII-sulfate, GAV-18, Ward's Py, Ward's Po \u2014 Table 3",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "S: ~0.05% (~0.25 \u00b5g per 500 \u00b5g S) \u2014 \u00a72.2",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "all: 20 cycles \u2014 Table 1, \u00a72.4"
        },
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
          "schema:value": 8.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.5 s \u2014 Table 1, \u00a72.4"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (\u03b434S = \u22120.3\u2030) \u2014 \u00a72.4",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Woods Hole Oceanographic Institution"
      },
      "schema:description": "Laser half: NewWave UP213 (213 nm), He carrier, 60 \u00b5m spot, 180 \u00d7 80 \u00b5m raster, 5 \u00b5m/s, 10 Hz, ~9\u201310 J/cm\u00b2, ablated aerosol mixed with 2% HNO3 in the spray chamber \u2014 Table 1",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [\u03b434S: consistent with published consensus values within uncertainty] \u2014 \u00a72.4, Table 3"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "Alfa [\u03b434S: \u00b10.21\u2030, 2\u03c3, 20\u201330 replicates]; Sch-M-2 [\u03b434S: \u00b10.45\u2030, 2\u03c3, 12 replicates, laser] \u2014 \u00a73.2; S_Spex \u00b10.18\u2030; \u03b4\u00b3\u00b3S an order of magnitude worse"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "\u03b434S, \u03b433S: two standard deviations of the replicates \u2014 Table 3 note"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-ablation MC-ICP-MS \u2014 the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"",
        "schema:description": "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable \u2014 \"Our setup allows for interchangeable bulk and in situ S isotope measurement\""
      }
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
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnitName": "Sample name only \u2014 Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P1 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable — \"Our setup allows for interchangeable bulk and in situ S isotope measurement\"" ;
                    schema1:name "Laser-ablation MC-ICP-MS — the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [δ34S: consistent with published consensus values within uncertainty] — §2.4, Table 3" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "Alfa [δ34S: ±0.21‰, 2σ, 20–30 replicates]; Sch-M-2 [δ34S: ±0.45‰, 2σ, 12 replicates, laser] — §3.2; S_Spex ±0.18‰; δ³³S an order of magnitude worse" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "δ34S, δ33S: two standard deviations of the replicates — Table 3 note" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Less than 50 mg weighed, digested, S purified on AG50-X8 cation exchange and diluted with 2% HNO3 to a 50 ppm S stock; for laser work, a 2 mm thick polished section on a petrographic slide — §2.1–2.2" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:description "Laser half: NewWave UP213 (213 nm), He carrier, 60 µm spot, 180 × 80 µm raster, 5 µm/s, 10 Hz, ~9–10 J/cm², ablated aerosol mixed with 2% HNO3 in the spray chamber — Table 1" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Woods Hole Oceanographic Institution" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123, Alfa, Sch-M-2, SW-Woods Hole, FeIII-sulfate, GAV-18, Ward's Py, Ward's Po — Table 3" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (δ34S = −0.3‰) — §2.4" ;
            ada:proceduralBlankLevel "S: ~0.05% (~0.25 µg per 500 µg S) — §2.2" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1" ;
    ada:samplingUnitName "Sample name only — Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "~0.8 L/min Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "~15 L/min Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "None, no automatic 2σ rejection of outlying cycles — 'Automatic rejection of outlying cycles (2σ outlier criterion) offered within the NEPTUNE software is not performed' (§2.4)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "Wash-out 2 min for solution" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "~1150 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1150 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 8.5 s — Table 1, §2.4" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.5e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 20 cycles — Table 1, §2.4" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "N — 'taken to dryness'" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HNO3 attack: below 70 °C; HNO3–HCl digestion: 70 °C; re-dissolution: N — §2.2" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "~0.8–0.9 L/min Ar (sample gas)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "<50 mg weighed; 500 µg S taken for column purification" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "50 µL/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> a schema1:PropertyValue ;
    schema1:name "Doubly-Charged Species Monitor" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> ;
    schema1:value "N — ⁶⁴Zn²⁺, ⁶⁶Zn²⁺ and ⁶⁸Zn²⁺ are listed as interferences on the S masses, Table 2, p.4, and resolved by mass resolution, p.5; no M²⁺ tuning monitor or production ratio is stated" .


```


### detail example P2
detail instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P2",
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
                "schema:value": 120,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "iron aqua regia: 120 °C; basalt HF–HNO3: 150 °C; other: N — §2.1"
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
                "schema:value": "iron aqua regia: 24 h; basalt HF–HNO3: 48 h; other: N — §2.1"
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
                "schema:value": "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)"
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
            "schema:description": "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"",
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
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~1-2 mg Fe per analysis; ~50 mg meteorite pieces"
            }
          ],
          "schema:name": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
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
                      "schema:value": 100,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~100 µl/min"
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
                      "schema:description": "None — the Apex Ω was run \"with no auxiliary N2 flow\""
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "210 s washout between all measurements"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2 — §2.1",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Fe: ~70 ng — 'negligible considering that 1-2 mg Fe was purified for each sample' (§2.2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 25,
          "schema:description": "HR: 25 cycles; MR: 50 cycles — §2.3"
        },
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
          "schema:value": 8.369,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.369 s — §2.3"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-524a — 'that has an identical isotopic composition to IRMM-014' (§2.3)",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2, BCR-2 [\"μ54Fe(7/6)\": average 2 ± 2 (95% c.i.); \"μ58Fe(7/6)\": average 4 ± 6 (95% c.i.); other: normal within uncertainties] — §3; agreeing with Schiller et al. (2020)"
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
        "schema:name": "N — the Fe was measured on digestions previously analysed for Pt, Mo, Ni and/or W isotopes (Kruijer et al. 2017 and others)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "56Fe: 1.4 nA (wet plasma, MR) to 2 nA (dry plasma, HR) — §2.3",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnitName": "Sample name only — meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P2",
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
                "schema:value": 120,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "iron aqua regia: 120 \u00b0C; basalt HF\u2013HNO3: 150 \u00b0C; other: N \u2014 \u00a72.1"
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
                "schema:value": "iron aqua regia: 24 h; basalt HF\u2013HNO3: 48 h; other: N \u2014 \u00a72.1"
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
                "schema:value": "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)"
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
            "schema:description": "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"",
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
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~1-2 mg Fe per analysis; ~50 mg meteorite pieces"
            }
          ],
          "schema:name": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
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
                      "schema:value": 100,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~100 \u00b5l/min"
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
                      "schema:description": "None \u2014 the Apex \u03a9 was run \"with no auxiliary N2 flow\""
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "210 s washout between all measurements"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P2/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2 \u2014 \u00a72.1",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Fe: ~70 ng \u2014 'negligible considering that 1-2 mg Fe was purified for each sample' (\u00a72.2)",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 25,
          "schema:description": "HR: 25 cycles; MR: 50 cycles \u2014 \u00a72.3"
        },
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
          "schema:value": 8.369,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.369 s \u2014 \u00a72.3"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-524a \u2014 'that has an identical isotopic composition to IRMM-014' (\u00a72.3)",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2, BCR-2 [\"\u03bc54Fe(7/6)\": average 2 \u00b1 2 (95% c.i.); \"\u03bc58Fe(7/6)\": average 4 \u00b1 6 (95% c.i.); other: normal within uncertainties] \u2014 \u00a73; agreeing with Schiller et al. (2020)"
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
        "schema:name": "N \u2014 the Fe was measured on digestions previously analysed for Pt, Mo, Ni and/or W isotopes (Kruijer et al. 2017 and others)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "56Fe: 1.4 nA (wet plasma, MR) to 2 nA (dry plasma, HR) \u2014 \u00a72.3",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnitName": "Sample name only \u2014 meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "N — the Fe was measured on digestions previously analysed for Pt, Mo, Ni and/or W isotopes (Kruijer et al. 2017 and others)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-2, BCR-2 [\"μ54Fe(7/6)\": average 2 ± 2 (95% c.i.); \"μ58Fe(7/6)\": average 4 ± 6 (95% c.i.); other: normal within uncertainties] — §3; agreeing with Schiller et al. (2020)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Chicago" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2, BCR-2 — §2.1" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Fe: IRMM-524a — 'that has an identical isotopic composition to IRMM-014' (§2.3)" ;
            ada:proceduralBlankLevel "Fe: ~70 ng — 'negligible considering that 1-2 mg Fe was purified for each sample' (§2.2)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a" ;
    ada:samplingUnitName "Sample name only — meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own" ;
    ada:sensitivityYield "56Fe: 1.4 nA (wet plasma, MR) to 2 nA (dry plasma, HR) — §2.3" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "None — the Apex Ω was run \"with no auxiliary N2 flow\"" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "210 s washout between all measurements" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 8.369 s — §2.3" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.369e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "HR: 25 cycles; MR: 50 cycles — §2.3" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 25 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "iron aqua regia: 24 h; basalt HF–HNO3: 48 h; other: N — §2.1" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "iron aqua regia: 120 °C; basalt HF–HNO3: 150 °C; other: N — §2.1" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 120 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~1-2 mg Fe per analysis; ~50 mg meteorite pieces" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~100 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .


```


### detail example P3
detail instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P3",
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
                "schema:description": "HF–HNO3–HClO4 attack: 160 °C; other: N"
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
                "schema:value": "HF–HNO3–HClO4 attack: 2 weeks; HCl–HNO3 attack: 1 week; final uptake: N"
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
            "schema:description": "CAIs extracted from Allende slabs with a stainless steel dental tool and powdered, digested, REEs recovered from the U/TEVA matrix cut, extracted on TODGA and separated by two-step FPLC on Ln-Spec — Materials and Methods, after Tissot et al. (34)",
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
              "schema:description": "N — ~30% of the U/TEVA matrix cut, equivalent to 24% of the whole CAI; CAIs of 15–440 mg"
            }
          ],
          "schema:name": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng — 'negligible compared to the amounts of REEs in the samples'",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 40,
          "schema:description": "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning — Materials and Methods"
        },
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
          "schema:value": 8.184,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.184 s — 4.142 s in the subconfiguration"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series — prepared in-house from high-purity ESPI oxide powders",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BCR-2 — 'processed with the CAIs'",
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
      "dqv:value": "BCR-2 [all: zero within error bars, typically < 0.05‰/amu] — Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1‰/amu"
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
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "140Ce: 10 V; 142Nd: 4 V; 152Sm: 3.5 V; 151Eu, 158Gd: 2 V; 164Dy: 3 V; 166Er, 174Yb: 1.5 V; other: N — at 15–25 ppb (LREE) or 1.5–10 ppb; the text prints '151Er' for ¹⁵¹Eu",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnitName": "Labelled: each CAI by name under its specimen number — Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); † marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P3",
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
                "schema:description": "HF\u2013HNO3\u2013HClO4 attack: 160 \u00b0C; other: N"
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
                "schema:value": "HF\u2013HNO3\u2013HClO4 attack: 2 weeks; HCl\u2013HNO3 attack: 1 week; final uptake: N"
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
            "schema:description": "CAIs extracted from Allende slabs with a stainless steel dental tool and powdered, digested, REEs recovered from the U/TEVA matrix cut, extracted on TODGA and separated by two-step FPLC on Ln-Spec \u2014 Materials and Methods, after Tissot et al. (34)",
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
              "schema:description": "N \u2014 ~30% of the U/TEVA matrix cut, equivalent to 24% of the whole CAI; CAIs of 15\u2013440 mg"
            }
          ],
          "schema:name": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng \u2014 'negligible compared to the amounts of REEs in the samples'",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 40,
          "schema:description": "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning \u2014 Materials and Methods"
        },
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
          "schema:value": 8.184,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.184 s \u2014 4.142 s in the subconfiguration"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series \u2014 prepared in-house from high-purity ESPI oxide powders",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BCR-2 \u2014 'processed with the CAIs'",
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
      "dqv:value": "BCR-2 [all: zero within error bars, typically < 0.05\u2030/amu] \u2014 Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1\u2030/amu"
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
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "140Ce: 10 V; 142Nd: 4 V; 152Sm: 3.5 V; 151Eu, 158Gd: 2 V; 164Dy: 3 V; 166Er, 174Yb: 1.5 V; other: N \u2014 at 15\u201325 ppb (LREE) or 1.5\u201310 ppb; the text prints '151Er' for \u00b9\u2075\u00b9Eu",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnitName": "Labelled: each CAI by name under its specimen number \u2014 Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); \u2020 marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P3 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BCR-2 [all: zero within error bars, typically < 0.05‰/amu] — Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1‰/amu" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "CAIs extracted from Allende slabs with a stainless steel dental tool and powdered, digested, REEs recovered from the U/TEVA matrix cut, extracted on TODGA and separated by two-step FPLC on Ln-Spec — Materials and Methods, after Tissot et al. (34)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
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
                            schema1:name "Data processing" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Chicago" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BCR-2 — 'processed with the CAIs'" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series — prepared in-house from high-purity ESPI oxide powders" ;
            ada:proceduralBlankLevel "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng — 'negligible compared to the amounts of REEs in the samples'" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9" ;
    ada:samplingUnitName "Labelled: each CAI by name under its specimen number — Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); † marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only" ;
    ada:sensitivityYield "140Ce: 10 V; 142Nd: 4 V; 152Sm: 3.5 V; 151Eu, 158Gd: 2 V; 164Dy: 3 V; 166Er, 174Yb: 1.5 V; other: N — at 15–25 ppb (LREE) or 1.5–10 ppb; the text prints '151Er' for ¹⁵¹Eu" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 8.184 s — 4.142 s in the subconfiguration" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.184e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning — Materials and Methods" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 40 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF–HNO3–HClO4 attack: 2 weeks; HCl–HNO3 attack: 1 week; final uptake: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF–HNO3–HClO4 attack: 160 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "N — ~30% of the U/TEVA matrix cut, equivalent to 24% of the whole CAI; CAIs of 15–440 mg" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example Tissot2020
detail instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-Tissot2020",
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
                "schema:value": 900,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "chemical abrasion: 900 °C (annealing), then 215 °C; U-Pb dissolution: 215 °C; Zr-only dissolution: 60 °C, then 215 °C; spike equilibration: 140 °C"
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
                "schema:value": "chemical abrasion: 60 h, then 12 h; U-Pb dissolution: 48 h; Zr-only dissolution: 2 h, then 60 h; spike equilibration: overnight"
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
                "schema:value": "N — the constants stated (²³⁸U/²³⁵U = 137.818, ¹⁸O/¹⁶O = 0.00205, α = 0.18%/amu) belong to the coupled ID-TIMS U-Pb work"
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
            "schema:description": "Crushing in a stainless steel mortar, sieving through 375 µm plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol",
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
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Single crystals; ~50 µl (5% of sample) taken for concentration measurement"
            }
          ],
          "schema:name": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
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
                  "schema:value": "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Tissot2020/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Mathematica — \"Data were reduced using a minimization approach implemented in Mathematica\"",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "N — the blank comparison stated concerns non-radiogenic Pb in the U-Pb work",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 50,
          "schema:description": "all: 50 cycles"
        },
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
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 5 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Zr: ZrNIST — a NIST gravimetric Zr solution being calibrated as an isotopic reference material",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Massachusetts Institute of Technology"
      },
      "schema:description": "Mo doping test: Offset δ94/90ZrNIST = −63.4 · x, x the Mo/Zr atomic ratio — used to show the residual Mo is negligible",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "ZrNIST [all: 2σ external reproducibility of the spiked ZrNIST measurements in each run]"
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
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions",
        "schema:description": "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N — 'around 572 V/ppm of total Zr'",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnitName": "Labelled: single crystals of FC-1 — zircons \"z1\"–\"z16\" with \"3_z…\" and \"4_z…\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"–\"b8\" with \"3_b…\" and \"4_b…\" series, and bulk rock \"WR1\" (Table 1, pp.4–6); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-Tissot2020",
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
                "schema:value": 900,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "chemical abrasion: 900 \u00b0C (annealing), then 215 \u00b0C; U-Pb dissolution: 215 \u00b0C; Zr-only dissolution: 60 \u00b0C, then 215 \u00b0C; spike equilibration: 140 \u00b0C"
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
                "schema:value": "chemical abrasion: 60 h, then 12 h; U-Pb dissolution: 48 h; Zr-only dissolution: 2 h, then 60 h; spike equilibration: overnight"
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
                "schema:value": "N \u2014 the constants stated (\u00b2\u00b3\u2078U/\u00b2\u00b3\u2075U = 137.818, \u00b9\u2078O/\u00b9\u2076O = 0.00205, \u03b1 = 0.18%/amu) belong to the coupled ID-TIMS U-Pb work"
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
            "schema:description": "Crushing in a stainless steel mortar, sieving through 375 \u00b5m plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol",
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
              "schema:value": 50,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Single crystals; ~50 \u00b5l (5% of sample) taken for concentration measurement"
            }
          ],
          "schema:name": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
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
                  "schema:value": "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Tissot2020/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Mathematica \u2014 \"Data were reduced using a minimization approach implemented in Mathematica\"",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "N \u2014 the blank comparison stated concerns non-radiogenic Pb in the U-Pb work",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 50,
          "schema:description": "all: 50 cycles"
        },
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
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 5 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Zr: ZrNIST \u2014 a NIST gravimetric Zr solution being calibrated as an isotopic reference material",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Massachusetts Institute of Technology"
      },
      "schema:description": "Mo doping test: Offset \u03b494/90ZrNIST = \u221263.4 \u00b7 x, x the Mo/Zr atomic ratio \u2014 used to show the residual Mo is negligible",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "ZrNIST [all: 2\u03c3 external reproducibility of the spiked ZrNIST measurements in each run]"
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
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions",
        "schema:description": "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N \u2014 'around 572 V/ppm of total Zr'",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnitName": "Labelled: single crystals of FC-1 \u2014 zircons \"z1\"\u2013\"z16\" with \"3_z\u2026\" and \"4_z\u2026\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"\u2013\"b8\" with \"3_b\u2026\" and \"4_b\u2026\" series, and bulk rock \"WR1\" (Table 1, pp.4\u20136); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-Tissot2020 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes" ;
                    schema1:name "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "ZrNIST [all: 2σ external reproducibility of the spiked ZrNIST measurements in each run]" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Crushing in a stainless steel mortar, sieving through 375 µm plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol" ;
                            schema1:name "Sample preparation" ;
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
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:description "Mo doping test: Offset δ94/90ZrNIST = −63.4 · x, x the Mo/Zr atomic ratio — used to show the residual Mo is negligible" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Massachusetts Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-Tissot2020/instrument/ICPMS> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Mathematica — \"Data were reduced using a minimization approach implemented in Mathematica\"" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Zr: ZrNIST — a NIST gravimetric Zr solution being calibrated as an isotopic reference material" ;
            ada:proceduralBlankLevel "N — the blank comparison stated concerns non-radiogenic Pb in the U-Pb work" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution" ;
    ada:samplingUnitName "Labelled: single crystals of FC-1 — zircons \"z1\"–\"z16\" with \"3_z…\" and \"4_z…\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"–\"b8\" with \"3_b…\" and \"4_b…\" series, and bulk rock \"WR1\" (Table 1, pp.4–6); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity" ;
    ada:sensitivityYield "N — 'around 572 V/ppm of total Zr'" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionMcicpmsTAPP-detail-Tissot2020/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "N — the constants stated (²³⁸U/²³⁵U = 137.818, ¹⁸O/¹⁶O = 0.00205, α = 0.18%/amu) belong to the coupled ID-TIMS U-Pb work" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\"" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 5 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 50 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "chemical abrasion: 60 h, then 12 h; U-Pb dissolution: 48 h; Zr-only dissolution: 2 h, then 60 h; spike equilibration: overnight" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "chemical abrasion: 900 °C (annealing), then 215 °C; U-Pb dissolution: 215 °C; Zr-only dissolution: 60 °C, then 215 °C; spike equilibration: 140 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 900 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "Single crystals; ~50 µl (5% of sample) taken for concentration measurement" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .


```


### detail example Dauphas2019
detail instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019",
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
                "schema:description": "HF–HNO3–HClO4 attack: 130 °C; HCl–HNO3 attack: 130 °C; HNO3 attack: N; Parr bomb: 175–180 °C"
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
                "schema:value": "HF–HNO3–HClO4 attack: 24 h; HCl–HNO3 attack: 24 h, twice; HNO3 attack: 24 h; Parr bomb: at least 3 days"
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
                "schema:value": "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885"
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
            "schema:description": "Whole-rock powder",
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
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100 mg or less; ~40 ng Rb typical"
            }
          ],
          "schema:name": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
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
                      "schema:value": 100,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "100 µl/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "60 s wash in 0.45 M HNO3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984, Allende — A.4",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Rb: ~0.14 ng — less than 0.5% of the Rb of a typical sample (40 ng)",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": "A single block"
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
          "schema:value": 25,
          "schema:description": "all: 25 cycles — a single block"
        },
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
          "schema:value": 4.194,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4.194 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [δ87Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [δ87Rb: reproducible, agree with published results] — A.4, Fig. 8"
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
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "85Rb: ~1–1.5 V at 15–25 ppb in low resolution",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnitName": "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 …)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019",
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
                "schema:description": "HF\u2013HNO3\u2013HClO4 attack: 130 \u00b0C; HCl\u2013HNO3 attack: 130 \u00b0C; HNO3 attack: N; Parr bomb: 175\u2013180 \u00b0C"
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
                "schema:value": "HF\u2013HNO3\u2013HClO4 attack: 24 h; HCl\u2013HNO3 attack: 24 h, twice; HNO3 attack: 24 h; Parr bomb: at least 3 days"
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
                "schema:value": "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885"
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
            "schema:description": "Whole-rock powder",
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
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100 mg or less; ~40 ng Rb typical"
            }
          ],
          "schema:name": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
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
                      "schema:value": 100,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "100 \u00b5l/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "60 s wash in 0.45 M HNO3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984, Allende \u2014 A.4",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Rb: ~0.14 ng \u2014 less than 0.5% of the Rb of a typical sample (40 ng)",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": "A single block"
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
          "schema:value": 25,
          "schema:description": "all: 25 cycles \u2014 a single block"
        },
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
          "schema:value": 4.194,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4.194 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Chicago"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [\u03b487Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [\u03b487Rb: reproducible, agree with published results] \u2014 A.4, Fig. 8"
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
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "85Rb: ~1\u20131.5 V at 15\u201325 ppb in low resolution",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnitName": "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 \u2026)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-Dauphas2019 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [δ87Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [δ87Rb: reproducible, agree with published results] — A.4, Fig. 8" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
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
                            schema1:description "Whole-rock powder" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Chicago" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984, Allende — A.4" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Rb: NIST SRM984" ;
            ada:proceduralBlankLevel "Rb: ~0.14 ng — less than 0.5% of the Rb of a typical sample (40 ng)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984" ;
    ada:samplingUnitName "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 …)" ;
    ada:sensitivityYield "85Rb: ~1–1.5 V at 15–25 ppb in low resolution" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-Dauphas2019/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "60 s wash in 0.45 M HNO3" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 4.194 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4.194e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> ;
    schema1:value "A single block" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 25 cycles — a single block" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 25 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF–HNO3–HClO4 attack: 24 h; HCl–HNO3 attack: 24 h, twice; HNO3 attack: 24 h; Parr bomb: at least 3 days" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF–HNO3–HClO4 attack: 130 °C; HCl–HNO3 attack: 130 °C; HNO3 attack: N; Parr bomb: 175–180 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~100 mg or less; ~40 ng Rb typical" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "100 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .


```


### detail example P6
detail instance derived from Nowell+etal2008 | Neptune | Durham AHIGL.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P6",
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
              "schema:value": 600,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Up to 600 ng Os consumed per analysis; ~300 µl of solution"
            }
          ],
          "schema:name": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
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
                      "schema:value": 80,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~80 µl/min, free aspiration"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM"
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
                  "schema:value": "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Microsoft Excel — \"Following analysis all intensity data was exported and re-processed offline using Excel\"",
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
              "schema:name": "UMd, DTM, LOsST, DROsS",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 9,
          "schema:description": "9 blocks"
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
          "schema:value": 5,
          "schema:description": "all: 5 cycles — 9 blocks (§3.1)"
        },
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
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Arthur Holmes Isotope Geology Laboratory, Durham"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N/A — reference material solutions, no solid preparation",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 2,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
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
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deltaOrEpsilonValueReferenceStandard": "no value available: ada:deltaOrEpsilonValueReferenceStandard",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "UMd [187Os/188Os: +26 ppm; 186Os/188Os: −125 ppm]; DTM [187Os/188Os: −12 ppm; 186Os/188Os: −108 ppm] — offset from Durham N-TIMS (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "UMd [187Os/188Os: 0.113795 ± 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 ± 26 (2SD, n = 121)] — 9 sessions over 11 months (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "UMd, DTM [all: 2SD of the analyses in each session] — Table 7a"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD — Table 7a: 'All quoted errors are 2SD'"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N — ~50 V for a 1 µg/ml Os solution at ~80 µl/min free aspiration",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) — the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P6",
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
              "schema:value": 600,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Up to 600 ng Os consumed per analysis; ~300 \u00b5l of solution"
            }
          ],
          "schema:name": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
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
                      "schema:value": 80,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~80 \u00b5l/min, free aspiration"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background \u2014 a 99.99% decrease reached after 220 s for DTM"
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
                  "schema:value": "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P6/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Microsoft Excel \u2014 \"Following analysis all intensity data was exported and re-processed offline using Excel\"",
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
              "schema:name": "UMd, DTM, LOsST, DROsS",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 9,
          "schema:description": "9 blocks"
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
          "schema:value": 5,
          "schema:description": "all: 5 cycles \u2014 9 blocks (\u00a73.1)"
        },
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
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Arthur Holmes Isotope Geology Laboratory, Durham"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N/A \u2014 reference material solutions, no solid preparation",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 2,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
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
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deltaOrEpsilonValueReferenceStandard": "no value available: ada:deltaOrEpsilonValueReferenceStandard",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "UMd [187Os/188Os: +26 ppm; 186Os/188Os: \u2212125 ppm]; DTM [187Os/188Os: \u221212 ppm; 186Os/188Os: \u2212108 ppm] \u2014 offset from Durham N-TIMS (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "UMd [187Os/188Os: 0.113795 \u00b1 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 \u00b1 26 (2SD, n = 121)] \u2014 9 sessions over 11 months (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "UMd, DTM [all: 2SD of the analyses in each session] \u2014 Table 7a"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD \u2014 Table 7a: 'All quoted errors are 2SD'"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N \u2014 ~50 V for a 1 \u00b5g/ml Os solution at ~80 \u00b5l/min free aspiration",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) \u2014 the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P6 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "UMd [187Os/188Os: 0.113795 ± 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 ± 26 (2SD, n = 121)] — 9 sessions over 11 months (Table 7a)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 2SD — Table 7a: 'All quoted errors are 2SD'" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "UMd [187Os/188Os: +26 ppm; 186Os/188Os: −125 ppm]; DTM [187Os/188Os: −12 ppm; 186Os/188Os: −108 ppm] — offset from Durham N-TIMS (Table 7a)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "UMd, DTM [all: 2SD of the analyses in each session] — Table 7a" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "N/A — reference material solutions, no solid preparation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Arthur Holmes Isotope Geology Laboratory, Durham" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "UMd, DTM, LOsST and DROsS Os isotope reference materials" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Microsoft Excel — \"Following analysis all intensity data was exported and re-processed offline using Excel\"" ;
                            ada:toolRole "dataReduction" ] ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "UMd, DTM, LOsST, DROsS" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "no value available: ada:deltaOrEpsilonValueReferenceStandard" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "UMd, DTM, LOsST and DROsS Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) — the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date" ;
    ada:sensitivityYield "N — ~50 V for a 1 µg/ml Os solution at ~80 µl/min free aspiration" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-P6/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 4 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:description "9 blocks" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> ;
    schema1:value 9 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 5 cycles — 9 blocks (§3.1)" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "Up to 600 ng Os consumed per analysis; ~300 µl of solution" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 600 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~80 µl/min, free aspiration" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 80 .


```


### detail example P7
detail instance derived from Nowell+etal2008 | Nu Plasma | NIGL.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P7",
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
              "schema:value": 6400,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~6400 µl of solution per analysis"
            }
          ],
          "schema:name": "DTM and LOsST Os isotope reference materials",
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
                      "schema:value": 400,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~400 µl/min, free aspiration — §3.2; ~6400 µl over a ~16 min analysis"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Online processing on the instrument — \"Samples were processed on-line for W and Re interferences and instrumental mass bias\"",
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
              "schema:name": "DTM, LOsST",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:description": "1 block"
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
          "schema:value": 50,
          "schema:description": "all: 50 cycles — 1 block"
        },
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
          "schema:value": 183,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "183W, 184Os, 185Re, 186Os, 187Os: 8 s; 190Os, 192Os: 4 s; 188Os, 189Os: 8 s (sequence 1), 4 s (sequence 2) — Table 2b"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NERC Isotope Geosciences Laboratory (NIGL)"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N/A — reference material solutions, no solid preparation",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 2,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
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
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deltaOrEpsilonValueReferenceStandard": "no value available: ada:deltaOrEpsilonValueReferenceStandard",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 ± 5] — Table 7a"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "DTM [187Os/188Os: 0.173910 ± 21 (2SD, n = 9)] — session 23-05-06 (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD — 'Reported errors are 2SD unless otherwise stated'"
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N — ~20 V for a 1 µg/ml Os solution at ~400 µl/min",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P7",
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
              "schema:value": 6400,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~6400 \u00b5l of solution per analysis"
            }
          ],
          "schema:name": "DTM and LOsST Os isotope reference materials",
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
                      "schema:value": 400,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~400 \u00b5l/min, free aspiration \u2014 \u00a73.2; ~6400 \u00b5l over a ~16 min analysis"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P7/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Online processing on the instrument \u2014 \"Samples were processed on-line for W and Re interferences and instrumental mass bias\"",
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
              "schema:name": "DTM, LOsST",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:description": "1 block"
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
          "schema:value": 50,
          "schema:description": "all: 50 cycles \u2014 1 block"
        },
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
          "schema:value": 183,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "183W, 184Os, 185Re, 186Os, 187Os: 8 s; 190Os, 192Os: 4 s; 188Os, 189Os: 8 s (sequence 1), 4 s (sequence 2) \u2014 Table 2b"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NERC Isotope Geosciences Laboratory (NIGL)"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "N/A \u2014 reference material solutions, no solid preparation",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 2,
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
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
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deltaOrEpsilonValueReferenceStandard": "no value available: ada:deltaOrEpsilonValueReferenceStandard",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 \u00b1 5] \u2014 Table 7a"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "DTM [187Os/188Os: 0.173910 \u00b1 21 (2SD, n = 9)] \u2014 session 23-05-06 (Table 7a)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD \u2014 'Reported errors are 2SD unless otherwise stated'"
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
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N \u2014 ~20 V for a 1 \u00b5g/ml Os solution at ~400 \u00b5l/min",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P7 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 2SD — 'Reported errors are 2SD unless otherwise stated'" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "DTM [187Os/188Os: 0.173910 ± 21 (2SD, n = 9)] — session 23-05-06 (Table 7a)" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 ± 5] — Table 7a" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "N/A — reference material solutions, no solid preparation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NERC Isotope Geosciences Laboratory (NIGL)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "DTM and LOsST Os isotope reference materials" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "DTM, LOsST" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Online processing on the instrument — \"Samples were processed on-line for W and Re interferences and instrumental mass bias\"" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "no value available: ada:deltaOrEpsilonValueReferenceStandard" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "DTM and LOsST Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only" ;
    ada:sensitivityYield "N — ~20 V for a 1 µg/ml Os solution at ~400 µl/min" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-P7/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "183W, 184Os, 185Re, 186Os, 187Os: 8 s; 190Os, 192Os: 4 s; 188Os, 189Os: 8 s (sequence 1), 4 s (sequence 2) — Table 2b" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 183 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:description "1 block" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 50 cycles — 1 block" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~6400 µl of solution per analysis" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6400 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~400 µl/min, free aspiration — §3.2; ~6400 µl over a ~16 min analysis" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 400 .


```


### detail example Moynier2017
detail instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017",
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
                "schema:description": "HF/HNO3 attack: 130 °C; HCl step: 130 °C"
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
                "schema:value": "HF/HNO3 attack: >48 h; HCl step: N"
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
                "schema:value": "\"any ratio outside 2σ was discarded\""
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
            "schema:description": "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"",
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
              "schema:value": 125,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<=125 mg powder, calculated to yield >20 ng Rb"
            }
          ],
          "schema:name": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
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
                      "schema:value": 5,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Peristaltic pump at 5 rpm"
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
                      "schema:value": 1.03,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.03 L/min (sample gas)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
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
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min"
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
                      "schema:value": 1.01,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.01 L/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "N — \"double-charged Er or Yb isotopes\" are named as interferences that the chemistry separates from Rb, p.2; no M²⁺ tuning monitor or production ratio is stated"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BCR-2, AGV-2, BHVO-2, GS-N, SRM984 through chemistry, Allende, pure Rb ICP-MS solution — §2.3",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "N — 'blocks of 20 cycles'"
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
          "schema:value": 20,
          "schema:description": "all: 20 cycles"
        },
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
          "schema:value": 8.389,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.389 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984 RbCl — BCR-2 as the bracketing standard in some sessions",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut de Physique du Globe de Paris"
      },
      "schema:description": "Extraction voltage −2000 V; peristaltic pump 5 rpm (Table 1)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "SRM984 through chemistry [δ87Rb: 0.00 ± 0.03‰]; Allende [δ87Rb: duplicate splits 0.12 ± 0.02‰ and 0.14 ± 0.04‰] — §2.3"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "pure Rb ICP-MS solution [δ87Rb: ±0.01‰ (n = 40)] — run as an external standard each session"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "85Rb: ~1.0 V — at 10 ppb (spray chamber) or 4 ppb (APEX); high beams avoided for memory",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnitName": "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017",
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
                "schema:description": "HF/HNO3 attack: 130 \u00b0C; HCl step: 130 \u00b0C"
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
                "schema:value": "HF/HNO3 attack: >48 h; HCl step: N"
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
                "schema:value": "\"any ratio outside 2\u03c3 was discarded\""
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
            "schema:description": "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"",
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
              "schema:value": 125,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<=125 mg powder, calculated to yield >20 ng Rb"
            }
          ],
          "schema:name": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
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
                      "schema:value": 5,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Peristaltic pump at 5 rpm"
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
                      "schema:value": 1.03,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.03 L/min (sample gas)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
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
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min"
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
                      "schema:value": 1.01,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1.01 L/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Collision-Reaction-Cell"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor"
                    }
                  ],
                  "schema:name": "Doubly-Charged Species Monitor",
                  "schema:value": "N \u2014 \"double-charged Er or Yb isotopes\" are named as interferences that the chemistry separates from Rb, p.2; no M\u00b2\u207a tuning monitor or production ratio is stated"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BCR-2, AGV-2, BHVO-2, GS-N, SRM984 through chemistry, Allende, pure Rb ICP-MS solution \u2014 \u00a72.3",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "N \u2014 'blocks of 20 cycles'"
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
          "schema:value": 20,
          "schema:description": "all: 20 cycles"
        },
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
          "schema:value": 8.389,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 8.389 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984 RbCl \u2014 BCR-2 as the bracketing standard in some sessions",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institut de Physique du Globe de Paris"
      },
      "schema:description": "Extraction voltage \u22122000 V; peristaltic pump 5 rpm (Table 1)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "SRM984 through chemistry [\u03b487Rb: 0.00 \u00b1 0.03\u2030]; Allende [\u03b487Rb: duplicate splits 0.12 \u00b1 0.02\u2030 and 0.14 \u00b1 0.04\u2030] \u2014 \u00a72.3"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "pure Rb ICP-MS solution [\u03b487Rb: \u00b10.01\u2030 (n = 40)] \u2014 run as an external standard each session"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "85Rb: ~1.0 V \u2014 at 10 ppb (spray chamber) or 4 ppb (APEX); high beams avoided for memory",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnitName": "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-Moynier2017 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "SRM984 through chemistry [δ87Rb: 0.00 ± 0.03‰]; Allende [δ87Rb: duplicate splits 0.12 ± 0.02‰ and 0.14 ± 0.04‰] — §2.3" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "pure Rb ICP-MS solution [δ87Rb: ±0.01‰ (n = 40)] — run as an external standard each session" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"" ;
                            schema1:name "Sample preparation" ;
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
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:description "Extraction voltage −2000 V; peristaltic pump 5 rpm (Table 1)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institut de Physique du Globe de Paris" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BCR-2, AGV-2, BHVO-2, GS-N, SRM984 through chemistry, Allende, pure Rb ICP-MS solution — §2.3" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Rb: NIST SRM984 RbCl — BCR-2 as the bracketing standard in some sessions" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984" ;
    ada:samplingUnitName "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only" ;
    ada:sensitivityYield "85Rb: ~1.0 V — at 10 ppb (spray chamber) or 4 ppb (APEX); high beams avoided for memory" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-Moynier2017/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.01 L/min" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.01e+00 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "16 L/min" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 16 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "\"any ratio outside 2σ was discarded\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1200 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 8.389 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.389e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:description "N — 'blocks of 20 cycles'" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurement> ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 20 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF/HNO3 attack: >48 h; HCl step: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF/HNO3 attack: 130 °C; HCl step: 130 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.03 L/min (sample gas)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.03e+00 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "<=125 mg powder, calculated to yield >20 ng Rb" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 125 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "Peristaltic pump at 5 rpm" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> a schema1:PropertyValue ;
    schema1:name "Doubly-Charged Species Monitor" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor> ;
    schema1:value "N — \"double-charged Er or Yb isotopes\" are named as interferences that the chemistry separates from Rb, p.2; no M²⁺ tuning monitor or production ratio is stated" .


```


### detail example P9
detail instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P9",
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
                "schema:description": "hotplate HF–HNO3: 180 °C; HNO3–HCl: 120 °C; high-PT HF–HNO3: 220 °C; Parr bomb: 170 °C; Ivuna high-PT: 160 °C; other: N"
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
                "schema:value": "hotplate HF–HNO3: 3–7 days; HNO3–HCl: 12 h; high-PT HF–HNO3: about a week; Ivuna high-PT: 3 days, then 2 days; other: N"
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
                "schema:value": "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)"
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
            "schema:description": "Homogenised powder — Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"",
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
              "schema:value": 25,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Ryugu <25 mg with ~40–70 ng Zr; 15 ng Zr consumed per 30 ppb analysis"
            }
          ],
          "schema:name": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
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
                      "schema:value": 0.05,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~0.05 mL/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Zr: 0.08–0.24 ng — 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 60,
          "schema:description": "all: 60 ratios — static collection"
        },
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
          "schema:value": 4.2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4.2 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Zr: NIST SRM 3169",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] — doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [ε91Zr: 0.3; ε92Zr: 0.2; ε96Zr: 1.0] — average 2SD over 10 months, n = 13–99 (eucrites and Colony n = 17–38)"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [ε91Zr: 0.35; ε92Zr: 0.21; ε96Zr: 1.00] — 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD of the individual measurements — Fig. 1: 'the 2 sd calculated from the individual sample measurements'"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\""
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N — total Zr ion beams 3.5–13 V at 30 ppb",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnitName": "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P9",
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
                "schema:description": "hotplate HF\u2013HNO3: 180 \u00b0C; HNO3\u2013HCl: 120 \u00b0C; high-PT HF\u2013HNO3: 220 \u00b0C; Parr bomb: 170 \u00b0C; Ivuna high-PT: 160 \u00b0C; other: N"
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
                "schema:value": "hotplate HF\u2013HNO3: 3\u20137 days; HNO3\u2013HCl: 12 h; high-PT HF\u2013HNO3: about a week; Ivuna high-PT: 3 days, then 2 days; other: N"
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
                "schema:value": "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)"
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
            "schema:description": "Homogenised powder \u2014 Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"",
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
              "schema:value": 25,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "Ryugu <25 mg with ~40\u201370 ng Zr; 15 ng Zr consumed per 30 ppb analysis"
            }
          ],
          "schema:name": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
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
                      "schema:value": 0.05,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "~0.05 mL/min"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Sample-Introduction-System"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\""
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P9/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "Zr: 0.08\u20130.24 ng \u2014 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna",
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 60,
          "schema:description": "all: 60 ratios \u2014 static collection"
        },
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
          "schema:value": 4.2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "all: 4.2 s"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Zr: NIST SRM 3169",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] \u2014 doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [\u03b591Zr: 0.3; \u03b592Zr: 0.2; \u03b596Zr: 1.0] \u2014 average 2SD over 10 months, n = 13\u201399 (eucrites and Colony n = 17\u201338)"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [\u03b591Zr: 0.35; \u03b592Zr: 0.21; \u03b596Zr: 1.00] \u2014 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2SD of the individual measurements \u2014 Fig. 1: 'the 2 sd calculated from the individual sample measurements'"
    },
    {
      "dqv:isMeasurementOf": "Peak Flatness",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\""
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "N \u2014 total Zr ion beams 3.5\u201313 V at 30 ppb",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnitName": "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P9 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\"" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "all [ε91Zr: 0.35; ε92Zr: 0.21; ε96Zr: 1.00] — 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 2SD of the individual measurements — Fig. 1: 'the 2 sd calculated from the individual sample measurements'" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] — doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [ε91Zr: 0.3; ε92Zr: 0.2; ε96Zr: 1.0] — average 2SD over 10 months, n = 13–99 (eucrites and Colony n = 17–38)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Homogenised powder — Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS> ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Zr: NIST SRM 3169" ;
            ada:proceduralBlankLevel "Zr: 0.08–0.24 ng — 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169" ;
    ada:samplingUnitName "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only" ;
    ada:sensitivityYield "N — total Zr ion beams 3.5–13 V at 30 ppb" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionMcicpmsTAPP-detail-P9/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\"" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "all: 4.2 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4.2e+00 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 60 ratios — static collection" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "hotplate HF–HNO3: 3–7 days; HNO3–HCl: 12 h; high-PT HF–HNO3: about a week; Ivuna high-PT: 3 days, then 2 days; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "hotplate HF–HNO3: 180 °C; HNO3–HCl: 120 °C; high-PT HF–HNO3: 220 °C; Parr bomb: 170 °C; Ivuna high-PT: 160 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "Ryugu <25 mg with ~40–70 ng Zr; 15 ng Zr consumed per 30 ppb analysis" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 25 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~0.05 mL/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5e-02 .


```


### detail example P10
detail instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P10",
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
                "schema:value": 150,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "Parr bomb: 150 °C, then 210 °C; aqua regia: N; NaOH fusion: 720 °C"
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
                "schema:value": "Parr bomb: 3 days; aqua regia: 2 days; NaOH fusion: 13 min"
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
            "schema:description": "Handpieces cut into 2 mm slabs with a diamond wire saw; saw dust and crushed fusion-crust-free pieces digested; chondrules drilled out with tungsten carbide bits — Methods",
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
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100–200 mg of saw dust and crushed pieces — 5% fractions for ICPMS and for Al/Mg"
            }
          ],
          "schema:name": "BHVO2 and DTS-2b processed alongside the samples",
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
                      "schema:value": 30,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "30 µl/min — for Fe, Cr and Mg"
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
                      "schema:value": "None, no auxiliary gas to the introduction system for Cr — Cr 'measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences'",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": "N — Cr measured 'at low radiofrequency power and sample gas inflow'",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO2, DTS-2b — 'processed alongside the samples'",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 200,
          "schema:description": "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles"
        },
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
          "schema:value": 54,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "54Fe, 56Fe, 57Fe, 58Fe, 50Cr, 52Cr, 53Cr, 54Cr: 8.3 s; 24Mg, 25Mg, 26Mg: 16.7 s; other: N"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — BHVO2 and DTS-2b results are in Supplementary Dataset 2"
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
        "schema:name": "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "24Mg, 25Mg, 26Mg: 80–90 V; other: N — typical signal intensities",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnitName": "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P10",
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
                "schema:value": 150,
                "schema:unitText": "no value available: unnamed property",
                "schema:description": "Parr bomb: 150 \u00b0C, then 210 \u00b0C; aqua regia: N; NaOH fusion: 720 \u00b0C"
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
                "schema:value": "Parr bomb: 3 days; aqua regia: 2 days; NaOH fusion: 13 min"
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
            "schema:description": "Handpieces cut into 2 mm slabs with a diamond wire saw; saw dust and crushed fusion-crust-free pieces digested; chondrules drilled out with tungsten carbide bits \u2014 Methods",
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
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100\u2013200 mg of saw dust and crushed pieces \u2014 5% fractions for ICPMS and for Al/Mg"
            }
          ],
          "schema:name": "BHVO2 and DTS-2b processed alongside the samples",
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
                      "schema:value": 30,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "30 \u00b5l/min \u2014 for Fe, Cr and Mg"
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
                      "schema:value": "None, no auxiliary gas to the introduction system for Cr \u2014 Cr 'measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences'",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Sample-Introduction-System"
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
                      "schema:value": "N \u2014 Cr measured 'at low radiofrequency power and sample gas inflow'",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/ICP-Source"
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
                  "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Collision-Reaction-Cell"
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
                  "schema:value": "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:solutionMcicpmsTAPP-detail-P10/instrument/ICPMS"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO2, DTS-2b \u2014 'processed alongside the samples'",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 200,
          "schema:description": "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles"
        },
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
          "schema:value": 54,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "54Fe, 56Fe, 57Fe, 58Fe, 50Cr, 52Cr, 53Cr, 54Cr: 8.3 s; 24Mg, 25Mg, 26Mg: 16.7 s; other: N"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 BHVO2 and DTS-2b results are in Supplementary Dataset 2"
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
        "schema:name": "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "24Mg, 25Mg, 26Mg: 80\u201390 V; other: N \u2014 typical signal intensities",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnitName": "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P10 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — BHVO2 and DTS-2b results are in Supplementary Dataset 2" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ] ;
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
                            schema1:description "Handpieces cut into 2 mm slabs with a diamond wire saw; saw dust and crushed fusion-crust-free pieces digested; chondrules drilled out with tungsten carbide bits — Methods" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "BHVO2 and DTS-2b processed alongside the samples" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO2, DTS-2b — 'processed alongside the samples'" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "BHVO2 and DTS-2b processed alongside the samples" ;
    ada:samplingUnitName "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only" ;
    ada:sensitivityYield "24Mg, 25Mg, 26Mg: 80–90 V; other: N — typical signal intensities" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "Collision Reaction Cell" .

<https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionMcicpmsTAPP-detail-P10/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "None, no auxiliary gas to the introduction system for Cr — Cr 'measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences'" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — Cr measured 'at low radiofrequency power and sample gas inflow'" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "54Fe, 56Fe, 57Fe, 58Fe, 50Cr, 52Cr, 53Cr, 54Cr: 8.3 s; 24Mg, 25Mg, 26Mg: 16.7 s; other: N" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 54 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 200 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "Parr bomb: 3 days; aqua regia: 2 days; NaOH fusion: 13 min" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "Parr bomb: 150 °C, then 210 °C; aqua regia: N; NaOH fusion: 720 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 150 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~100–200 mg of saw dust and crushed pieces — 5% fractions for ICPMS and for Al/Mg" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "30 µl/min — for Fe, Cr and Mg" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example P11
detail instance derived from Broussard+etal2026 | Neptune Plus | WUSTL.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P11",
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
                "schema:description": "HF–HNO3 attack: 150 °C; other: N"
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
                "schema:value": "HF–HNO3 attack: ~1 week; other: N"
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
            "schema:description": "Two fragments (39.49 mg and 48.34 mg) digested; ~7 mg of sample from the digest solutions taken for K — Bulk chemistry analysis; Potassium isotope analysis",
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
              "schema:value": 7,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~7 mg of sample — from the OC002A and OC002B solutions"
            }
          ],
          "schema:name": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "N — 'Each sample was measured approximately 20 times'"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST SRM 3141a",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2",
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
      "dqv:value": "BHVO-2 [δ41K: −0.448 ± 0.027‰, within error of reported values such as −0.46 ± 0.09‰ (Wang et al. 2021)]"
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
        "schema:name": "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS",
        "schema:description": "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement"
      }
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
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnitName": "Labelled: two solutions of the OC002 fragment — \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P11",
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
                "schema:description": "HF\u2013HNO3 attack: 150 \u00b0C; other: N"
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
                "schema:value": "HF\u2013HNO3 attack: ~1 week; other: N"
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
            "schema:description": "Two fragments (39.49 mg and 48.34 mg) digested; ~7 mg of sample from the digest solutions taken for K \u2014 Bulk chemistry analysis; Potassium isotope analysis",
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
              "schema:value": 7,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~7 mg of sample \u2014 from the OC002A and OC002B solutions"
            }
          ],
          "schema:name": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
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
          "schema:value": 20,
          "schema:description": "N \u2014 'Each sample was measured approximately 20 times'"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST SRM 3141a",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2",
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
      "dqv:value": "BHVO-2 [\u03b441K: \u22120.448 \u00b1 0.027\u2030, within error of reported values such as \u22120.46 \u00b1 0.09\u2030 (Wang et al. 2021)]"
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
        "schema:name": "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS",
        "schema:description": "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement"
      }
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
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnitName": "Labelled: two solutions of the OC002 fragment \u2014 \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P11 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement" ;
                    schema1:name "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-2 [δ41K: −0.448 ± 0.027‰, within error of reported values such as −0.46 ± 0.09‰ (Wang et al. 2021)]" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
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
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Two fragments (39.49 mg and 48.34 mg) digested; ~7 mg of sample from the digest solutions taken for K — Bulk chemistry analysis; Potassium isotope analysis" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Washington University in St. Louis" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deltaOrEpsilonValueReferenceStandard "K: NIST SRM 3141a" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a" ;
    ada:samplingUnitName "Labelled: two solutions of the OC002 fragment — \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "N — 'Each sample was measured approximately 20 times'" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF–HNO3 attack: ~1 week; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF–HNO3 attack: 150 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~7 mg of sample — from the OC002A and OC002B solutions" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7 .


```


### detail example P12
detail instance derived from Barnes+etal2025 | Neptune Plus | WUSTL.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P12",
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
                "schema:description": "HF–HNO3 attack: 170 °C; other: N"
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
                "schema:value": "HF–HNO3 attack: 48 h; other: N"
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
            "schema:description": "One digest split two ways: about half at WUSTL for K, Cu and Zn, half to LLNL and on to ETH Zurich — coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL",
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
              "schema:value": 20.66,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~20.66 mg split, about half used at WUSTL"
            }
          ],
          "schema:name": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
          "schema:identifier": "Curatorial sample identifiers stated: OREX-803015-101 (LLNL) and OREX-803015-100 (ETH Zurich)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2",
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
      "dqv:value": "N — 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9"
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
        "schema:name": "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest"
      }
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
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnitName": "Labelled: split \"OREX-803015-0\" — \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P12",
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
                "schema:description": "HF\u2013HNO3 attack: 170 \u00b0C; other: N"
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
                "schema:value": "HF\u2013HNO3 attack: 48 h; other: N"
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
            "schema:description": "One digest split two ways: about half at WUSTL for K, Cu and Zn, half to LLNL and on to ETH Zurich \u2014 coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL",
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
              "schema:value": 20.66,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~20.66 mg split, about half used at WUSTL"
            }
          ],
          "schema:name": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
          "schema:identifier": "Curatorial sample identifiers stated: OREX-803015-101 (LLNL) and OREX-803015-100 (ETH Zurich)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2",
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
      "dqv:value": "N \u2014 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9"
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
        "schema:name": "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest"
      }
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
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnitName": "Labelled: split \"OREX-803015-0\" \u2014 \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P12 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ],
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
                            schema1:description "One digest split two ways: about half at WUSTL for K, Cu and Zn, half to LLNL and on to ETH Zurich — coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Washington University in St. Louis" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:identifier "Curatorial sample identifiers stated: OREX-803015-101 (LLNL) and OREX-803015-100 (ETH Zurich)" ;
                    schema1:name "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:deltaOrEpsilonValueReferenceStandard "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon" ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2" ;
    ada:samplingUnitName "Labelled: split \"OREX-803015-0\" — \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF–HNO3 attack: 48 h; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF–HNO3 attack: 170 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~20.66 mg split, about half used at WUSTL" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.066e+01 .


```


### detail example P13
detail instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich.
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
  "@id": "ex:solutionMcicpmsTAPP-detail-P13",
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
                "schema:description": "HF–HNO3 attack: 170 °C; other: N"
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
                "schema:value": "HF–HNO3 attack: 48 h; other: N"
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
            "schema:description": "A 5.2 mg aliquot of the coordinated digest (OREX-803015-100), sent from WUSTL via LLNL — coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL",
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
              "schema:value": 5.2,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "5.2 mg"
            }
          ],
          "schema:name": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
          "schema:identifier": "OREX-803015-100",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Ti: 3.7 ng — a maximum blank contribution of 0.18%",
      "schema:additionalProperty": [
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
          "schema:value": 40,
          "schema:description": "all: 40 cycles"
        },
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
          "schema:value": 46,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "46Ti, 47Ti, 48Ti, 44Ca: 8.39 s; 51V, 52Cr, 53Cr: 4.19 s; 49Ti, 50Ti: 8.39 s (configuration 1), 4.19 s (configuration 2)"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A — no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Ti: in-house Alfa Aesar Ti wire standard",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geochemistry and Petrology, ETH Zurich"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, Agua Zarcas — Agua Zarcas is a CM2 chondrite",
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
      "dqv:value": "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2 [ε46Ti: ±0.17; ε48Ti: ±0.09; ε50Ti: ±0.16] — 2 s.d. of 9 analyses"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "48Ti: ~40 V — about 0.3 µg Ti consumed per measurement",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnitName": "Labelled: aliquot \"OREX-803015-100\" — \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-detail-P13",
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
                "schema:description": "HF\u2013HNO3 attack: 170 \u00b0C; other: N"
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
                "schema:value": "HF\u2013HNO3 attack: 48 h; other: N"
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
            "schema:description": "A 5.2 mg aliquot of the coordinated digest (OREX-803015-100), sent from WUSTL via LLNL \u2014 coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL",
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
              "schema:value": 5.2,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "5.2 mg"
            }
          ],
          "schema:name": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
          "schema:identifier": "OREX-803015-100",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Ti: 3.7 ng \u2014 a maximum blank contribution of 0.18%",
      "schema:additionalProperty": [
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
          "schema:value": 40,
          "schema:description": "all: 40 cycles"
        },
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
          "schema:value": 46,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "46Ti, 47Ti, 48Ti, 44Ca: 8.39 s; 51V, 52Cr, 53Cr: 4.19 s; 49Ti, 50Ti: 8.39 s (configuration 1), 4.19 s (configuration 2)"
        },
        {
          "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatio"
            }
          ],
          "schema:name": "Double Spike Mixing Ratio",
          "schema:value": "N/A \u2014 no double spike used"
        }
      ],
      "ada:deltaOrEpsilonValueReferenceStandard": "Ti: in-house Alfa Aesar Ti wire standard",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geochemistry and Petrology, ETH Zurich"
      },
      "prov:used": [
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "BHVO-2, Agua Zarcas \u2014 Agua Zarcas is a CM2 chondrite",
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
      "dqv:value": "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-2 [\u03b546Ti: \u00b10.17; \u03b548Ti: \u00b10.09; \u03b550Ti: \u00b10.16] \u2014 2 s.d. of 9 analyses"
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
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:sensitivityYield": "48Ti: ~40 V \u2014 about 0.3 \u00b5g Ti consumed per measurement",
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnitName": "Labelled: aliquot \"OREX-803015-100\" \u2014 \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
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

ex:solutionMcicpmsTAPP-detail-P13 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "BHVO-2 [ε46Ti: ±0.17; ε48Ti: ±0.09; ε50Ti: ±0.16] — 2 s.d. of 9 analyses" ],
        [ dqv:isMeasurementOf "Peak Flatness" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "A 5.2 mg aliquot of the coordinated digest (OREX-803015-100), sent from WUSTL via LLNL — coordinated dissolution of an ~20.66 mg split (OREX-803015-0) at WUSTL" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
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
                            schema1:name "Data processing" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle>,
                <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institute of Geochemistry and Petrology, ETH Zurich" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:identifier "OREX-803015-100" ;
                    schema1:name "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "BHVO-2, Agua Zarcas — Agua Zarcas is a CM2 chondrite" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:deltaOrEpsilonValueReferenceStandard "Ti: in-house Alfa Aesar Ti wire standard" ;
            ada:proceduralBlankLevel "Ti: 3.7 ng — a maximum blank contribution of 0.18%" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate" ;
    ada:samplingUnitName "Labelled: aliquot \"OREX-803015-100\" — \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)" ;
    ada:sensitivityYield "48Ti: ~40 V — about 0.3 µg Ti consumed per measurement" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> a schema1:PropertyValue ;
    schema1:description "46Ti, 47Ti, 48Ti, 44Ca: 8.39 s; 51V, 52Cr, 53Cr: 4.19 s; 49Ti, 50Ti: 8.39 s (configuration 1), 4.19 s (configuration 2)" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycle> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 46 .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:description "all: 40 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlock> ;
    schema1:value 40 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HF–HNO3 attack: 48 h; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HF–HNO3 attack: 170 °C; other: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "5.2 mg" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5.2e+00 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution MC-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing
  CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
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
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
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
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    minContains: 0
                                    maxContains: 1
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              - title: Error Correlation Between Reported Quantities
                description: 'Which pairs of reported quantities have uncertainties
                  that are not independent, and how the correlation coefficient between
                  each pair is obtained. In the dataset: report, for each analysis,
                  the correlation coefficient of each such pair.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  schema:name:
                    const: Error Correlation Between Reported Quantities
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              minContains: 0
              maxContains: 1
            - contains:
                title: Error Correlation Between Reported Quantities
                description: 'Which pairs of reported quantities have uncertainties
                  that are not independent, and how the correlation coefficient between
                  each pair is obtained. In the dataset: report, for each analysis,
                  the correlation coefficient of each such pair.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  schema:name:
                    const: Error Correlation Between Reported Quantities
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
                title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
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
          ada:deltaOrEpsilonValueReferenceStandard:
            description: "International or community-accepted isotopic reference standard
              used as the zero-delta anchor for expressing isotopic compositions in
              delta (\u03B4, per mil) or epsilon (\u03B5, per ten thousand) notation:
              \u03B4\u2071X = [(\u2071X/\u02B2X)sample / (\u2071X/\u02B2X)reference
              \u2212 1] \xD7 1000\u2030. The reporting reference is a per-study or
              per-publication decision. Specify the standard name, lot or batch number
              where applicable, and the certified or consensus isotope ratio used
              for normalization."
            type: string
        required:
        - ada:deltaOrEpsilonValueReferenceStandard
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
        - title: Isotope Ratio Reported
          description: Specific isotope ratio pair(s) reported as primary data output.
            The denominator isotope is typically the reference mass used in the delta
            notation (e.g., 54Fe for Fe isotopes, 235U for U isotopes). Report all
            ratio pairs routinely calculated and reported.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            schema:name:
              const: Isotope Ratio Reported
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
          title: Isotope Ratio Reported
          description: Specific isotope ratio pair(s) reported as primary data output.
            The denominator isotope is typically the reference mass used in the delta
            notation (e.g., 54Fe for Fe isotopes, 235U for U isotopes). Report all
            ratio pairs routinely calculated and reported.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            schema:name:
              const: Isotope Ratio Reported
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
      title: Measured Variables
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld)

## Sources

* [Solution_MC-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail`

