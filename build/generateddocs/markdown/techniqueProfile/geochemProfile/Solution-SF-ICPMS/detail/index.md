
# Solution SF-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from Desem+etal2022 | Nu Attom SC-SF-ICP-MS | Univ Melbourne.
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
  "@id": "ex:solutionSficpmsTAPP-detail-P0",
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
              "schema:value": "N — Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3"
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
              "schema:value": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
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
              "schema:value": "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\""
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
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
                  "schema:value": 0.33,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.33 ml/min (stated section 2.3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System"
            },
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "ICP Source",
              "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)",
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
      "ada:proceduralBlankLevel": "Pb: total procedural blank <100 pg — 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios ≥1500 (§2.3)",
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
                "schema:value": "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law"
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
            "schema:description": "Soils oven-dried (50 °C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' — §2.1, §2.2, §2.4; the rock chips were analysed by MC-ICP-MS only",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Melbourne, Australia (affiliation)"
      },
      "schema:identifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] — Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (§2.4)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] — Table 1 and §3"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2sd — '(2sd, n = 22)'; averages given with '±2sd%'"
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)",
        "schema:description": "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:sensitivityYield": "all: ~1000 kcps/ppb Pb total — 'tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks' (§2.4)",
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnitName": "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-P0",
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
              "schema:value": "N \u2014 Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3"
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
              "schema:value": "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)"
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
              "schema:value": "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\""
            }
          ],
          "schema:hasPart": [
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
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
                  "schema:value": 0.33,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.33 ml/min (stated section 2.3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System"
            },
            {
              "schema:additionalType": [
                "ICP Source",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "ICP Source",
              "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P0/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)",
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
      "ada:proceduralBlankLevel": "Pb: total procedural blank <100 pg \u2014 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios \u22651500 (\u00a72.3)",
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
                "schema:value": "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law"
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
            "schema:description": "Soils oven-dried (50 \u00b0C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' \u2014 \u00a72.1, \u00a72.2, \u00a72.4; the rock chips were analysed by MC-ICP-MS only",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Melbourne, Australia (affiliation)"
      },
      "schema:identifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] \u2014 Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (\u00a72.4)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] \u2014 Table 1 and \u00a73"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 2sd \u2014 '(2sd, n = 22)'; averages given with '\u00b12sd%'"
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)",
        "schema:description": "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler"
  ],
  "ada:sensitivityYield": "all: ~1000 kcps/ppb Pb total \u2014 'tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks' (\u00a72.4)",
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnitName": "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
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
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionSficpmsTAPP-detail-P0 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Q-ICP-MS Pb isotope ratios compared with SF-ICP-MS values for validation; Q-ICP-MS showed higher uncertainties (stated section 2.4)" ;
                    schema1:name "Agilent 7700x Q-ICP-MS (used for Pb isotope comparison; stated section 2.4)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] — Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (§2.4)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 2sd — '(2sd, n = 22)'; averages given with '±2sd%'" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] — Table 1 and §3" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Soils oven-dried (50 °C, 7 days), not sieved; total-dissolution (TD) and aqua-regia (AR) splits; the SC-SF-ICP-MS splits 'redissolved and diluted to 2 ml in high purity 2% HNO3 doped with 1 ppb of high-purity thallium' — §2.1, §2.2, §2.4; the rock chips were analysed by MC-ICP-MS only" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:description "Nu Attom SC-SF-ICP-MS in single-collector mode; 30 sets x 2000 sweeps = 4.5 min total analysis; Tl-spiked matrix (1 ppb Tl) for mass bias correction; blank ~900 cps on 208Pb (stated section 2.3)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "BCR-2, AGV-2, JB-2, BR, JB-3 (stated Tables 1-2)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Melbourne, Australia (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Pb: total procedural blank <100 pg — 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios ≥1500 (§2.3)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The Attom was operated with a Glass Expansion cyclonic spray chamber and glass nebulizer (uptake rate 0.33 ml/min)\"; \"both operated in wet plasma mode\"; ESI SC-2 DX autosampler" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena" ;
    ada:samplingUnitName "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered" ;
    ada:sensitivityYield "all: ~1000 kcps/ppb Pb total — 'tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks' (§2.4)" ;
    ada:sessionIdentifier "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "ICP Source" .

<https://example.org/solutionSficpmsTAPP-detail-P0/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "205Tl/203Tl = 2.3871 (Woodhead 2002), used to correct instrumental mass fractionation by internal normalisation with the exponential law" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"The instrument was tuned to provide ~1000 kcps/ppb Pbtotal while maintaining flat-topped peaks\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "N — Nu Attom uses deflector peak jump; no LR/MR/HR designation stated; stated section 2.3" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "10 s wash in two 2% HNO3 reservoirs between samples (stated section 2.3)" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "0.33 ml/min (stated section 2.3)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3.3e-01 .


```


### detail example P1
detail instance derived from Li+etal2016 | Thermo Element I | IGGCAS Beijing.
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
  "@id": "ex:solutionSficpmsTAPP-detail-P1",
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
                  "schema:value": 0.96,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.96 L/min (Table 1)"
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
                  "schema:value": 14.6,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "14.6 L/min (Table 1)"
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
                  "schema:value": 1300,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1300 W (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 0.9,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.90 L/min (sampling gas; Table 1)"
                },
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
                  "schema:value": 200,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "200 uL/min (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "60 s wash between samples (Table 1)"
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
              "schema:value": "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\""
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "FER-2 — iron-formation reference material (CCRMP), 'used to validate of the proposed method' (§2.2)",
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
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
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
                "schema:value": "HCl-HNO3 attack: 48 h; re-dissolution: N — §2.3.1"
              },
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
                "schema:description": "HCl-HNO3 attack: 130 °C; re-dissolution: 130 °C (evaporation) — §2.3.1"
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
            "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
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
              "schema:description": "~100 mg mineral powder (stated section 2.3)"
            }
          ],
          "schema:name": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N — ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
      },
      "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "FER-2 [all: RSD <5%] — three analyses, Table 3 (§3)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "FER-2 [all: most ratios to literature values within 0.9–1.1] — Fig. 7 (§3)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: s, one standard deviation, and RSD — 'Mean ± 1 s (n = 3)'; 'RSD = standard deviation/mean × 100%'"
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
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnitName": "Sample name only — \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean ± s (n = 3)\" with the replicates unlabelled (table, p.8)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N — method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-P1",
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
                  "schema:value": 0.96,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.96 L/min (Table 1)"
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
                  "schema:value": 14.6,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "14.6 L/min (Table 1)"
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
                  "schema:value": 1300,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1300 W (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 0.9,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.90 L/min (sampling gas; Table 1)"
                },
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
                  "schema:value": 200,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "200 uL/min (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "60 s wash between samples (Table 1)"
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
              "schema:value": "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\""
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P1/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "FER-2 \u2014 iron-formation reference material (CCRMP), 'used to validate of the proposed method' (\u00a72.2)",
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
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
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
                "schema:value": "HCl-HNO3 attack: 48 h; re-dissolution: N \u2014 \u00a72.3.1"
              },
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
                "schema:description": "HCl-HNO3 attack: 130 \u00b0C; re-dissolution: 130 \u00b0C (evaporation) \u2014 \u00a72.3.1"
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
            "schema:description": "Mineral separates (~100 mg powder; stated section 2.3)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
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
              "schema:description": "~100 mg mineral powder (stated section 2.3)"
            }
          ],
          "schema:name": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N \u2014 ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)"
      },
      "schema:description": "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "FER-2 [all: RSD <5%] \u2014 three analyses, Table 3 (\u00a73)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "FER-2 [all: most ratios to literature values within 0.9\u20131.1] \u2014 Fig. 7 (\u00a73)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: s, one standard deviation, and RSD \u2014 'Mean \u00b1 1 s (n = 3)'; 'RSD = standard deviation/mean \u00d7 100%'"
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
    "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnitName": "Sample name only \u2014 \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean \u00b1 s (n = 3)\" with the replicates unlabelled (table, p.8)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N \u2014 method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL",
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

ex:solutionSficpmsTAPP-detail-P1 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: s, one standard deviation, and RSD — 'Mean ± 1 s (n = 3)'; 'RSD = standard deviation/mean × 100%'" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "FER-2 [all: most ratios to literature values within 0.9–1.1] — Fig. 7 (§3)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "FER-2 [all: RSD <5%] — three analyses, Table 3 (§3)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Mineral separates (~100 mg powder; stated section 2.3)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:description "Chromatographic separation (AG1-X8 + TRUspec) performed before SF-ICP-MS; reflected power <2 W (stated Table 1); pulse counting detection only" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "FER-2 — iron-formation reference material (CCRMP), 'used to validate of the proposed method' (§2.2)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N — ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Sample uptake rate 200 uL min-1\"; \"The components of the sample introduction system: nebulizer, spray chamber, torch, and the cones\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N — method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)" ;
    ada:samplingUnitName "Sample name only — \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean ± s (n = 3)\" with the replicates unlabelled (table, p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionSficpmsTAPP-detail-P1/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.96 L/min (Table 1)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.6e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "14.6 L/min (Table 1)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.46e+01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"The instrument was tuned using a 5 ng mL-1 solution containing Be, Rh and U in order to maximize the sensitivity covering the low-mid-high mass range. MO+/M+ ratios measured for Ce under the routine experiment conditions maintained at less than 2 permil\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "60 s wash between samples (Table 1)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1300 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1300 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "HCl-HNO3 attack: 48 h; re-dissolution: N — §2.3.1" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "HCl-HNO3 attack: 130 °C; re-dissolution: 130 °C (evaporation) — §2.3.1" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.90 L/min (sampling gas; Table 1)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "~100 mg mineral powder (stated section 2.3)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "200 uL/min (Table 1)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 200 .


```


### detail example P2
detail instance derived from Lu+etal2007 | Finnigan ELEMENT | PML Okayama.
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
  "@id": "ex:solutionSficpmsTAPP-detail-P2",
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
                  "schema:description": "1.2 L/min (stated Table in section 2.1.2)"
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
                  "schema:description": "14 L/min (stated Table in section 2.1.2)"
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
                  "schema:value": 1.1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.1 kW (stated Table in section 2.1.2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 0.9,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.90 L/min (stated Table in section 2.1.2)"
                },
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
                  "schema:description": "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "MR (M/Delta-m = 3000; stated section 2.1.2)"
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
              "schema:value": "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample — §2.1.2"
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
              "schema:value": "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — GSJ and USGS silicate reference materials (§2.3); the chondrites are samples",
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
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
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
        "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [Ti: RSD 3.6% (2.3–5.4%)] — TTi/93Nb RSD% (Table 2b)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] — abstract; Tables 5 and 6"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% — 'Averages of the reproducibility (RSD %)'"
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti — abstract; §2.7"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
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
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Ti: 4 µg/g; other: N — 3σ in rock; 21 ng/g in solution (Table 2b)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-P2",
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
                  "schema:description": "1.2 L/min (stated Table in section 2.1.2)"
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
                  "schema:description": "14 L/min (stated Table in section 2.1.2)"
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
                  "schema:value": 1.1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.1 kW (stated Table in section 2.1.2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 0.9,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.90 L/min (stated Table in section 2.1.2)"
                },
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
                  "schema:description": "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "MR (M/Delta-m = 3000; stated section 2.1.2)"
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
              "schema:value": "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample \u2014 \u00a72.1.2"
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
              "schema:value": "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P2/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 \u2014 GSJ and USGS silicate reference materials (\u00a72.3); the chondrites are samples",
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
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Data processing",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
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
        "schema:name": "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "schema:description": "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [Ti: RSD 3.6% (2.3\u20135.4%)] \u2014 TTi/93Nb RSD% (Table 2b)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] \u2014 abstract; Tables 5 and 6"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD% \u2014 'Averages of the reproducibility (RSD %)'"
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
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)",
        "schema:description": "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti \u2014 abstract; \u00a72.7"
      }
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\""
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
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Ti: 4 \u00b5g/g; other: N \u2014 3\u03c3 in rock; 21 ng/g in solution (Table 2b)",
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

ex:solutionSficpmsTAPP-detail-P2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "The SF-ICP-MS measures Ti as the (47Ti + 49Ti)/93Nb ratio; the Q-ICP-MS measures B, Zr, Nb, Mo, Sn, Sb, Hf and Ta on the same solutions and gives the Nb concentration used for Ti — abstract; §2.7" ;
                    schema1:name "Agilent 7500cs Q-ICP-MS at PML (B, Zr, Nb, Mo, Sn, Sb, Hf, Ta on same samples; stated section 2.1.1)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] — abstract; Tables 5 and 6" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD% — 'Averages of the reproducibility (RSD %)'" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "all [Ti: RSD 3.6% (2.3–5.4%)] — TTi/93Nb RSD% (Table 2b)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Whole-rock powder (decomposed in TFM bomb; same as Q-ICP-MS portion; stated section 2.1.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ] ] ;
            schema1:description "Continuous sample introduction with an uptake time of 60 s (0.04 ml per measurement); quartz glass torch with sapphire injector (Table 1b)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 — GSJ and USGS silicate reference materials (§2.3); the chondrites are samples" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Pheasant Memorial Laboratory (PML), Okayama University (section 2.1.2)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- stated in the acquisition parameters: \"Middle resolution 50 s with 30 scans (continuous nebulization)\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Ti: 4 µg/g; other: N — 3σ in rock; 21 ng/g in solution (Table 2b)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnitName "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionSficpmsTAPP-detail-P2/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.2 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.2e+00 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "14 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 14 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "Partially -- an oxide acceptance criterion is registered in the operating conditions, \"Oxide forming rate <1% (CeO+/Ce+)\"; no tuning solution or tuning procedure stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "MR (M/Delta-m = 3000; stated section 2.1.2)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "0.5 mol/l HF carrier and wash solution; ~3 min wash per sample — §2.1.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1.1 kW (stated Table in section 2.1.2)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.1e+00 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "ultrasonic HF decomposition: <70 °C; bomb HF decomposition: 245 °C; re-dissolution: N — abstract" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 70 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.90 L/min (stated Table in section 2.1.2)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "Self-aspiration; uptake time 60 s (stated section 2.1.2); volumetric flow rate N" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .


```


### detail example P3
detail instance derived from Milne+etal2010 | Thermo Finnigan Element I | FSU NHMFL.
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
  "@id": "ex:solutionSficpmsTAPP-detail-P3",
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
                  "schema:value": 1.05,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.05 L/min (varied and optimized daily; Table 2)"
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
                  "schema:value": 13,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "13 L/min (Table 2)"
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
                  "schema:value": 1300,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1300 W (Table 2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 1.2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.2 L/min (varied and optimized daily; Table 2)"
                },
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
                  "schema:value": 150,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "150 uL/min (Table 2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
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
              "schema:value": "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NASS-5; SAFe S1; SAFe D2 — NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (§2.6)",
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
              "schema:value": 12,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "12 mL seawater (stated section 2.2)"
            }
          ],
          "schema:name": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Mn: 0.433 ± 0.026; Fe: 2.791 ± 0.083; Co: 0.078 ± 0.006; Ni: 0.457 ± 0.104; Cu: 0.184 ± 0.027; Zn: 3.044 ± 0.018; Cd: 0.045 ± 0.003; Pb: 0.017 ± 0.001 — pmol, mean reagent blank ± 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)",
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
                "schema:value": "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated"
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
            "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
      },
      "schema:identifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
      "schema:description": "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (§2.2–2.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] — Table 6"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] — Table 6"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: %RSD, with 1 S.D. for blanks — 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank ± 1S.D.'"
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
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:sensitivityYield": "59Co: ~5000 cps/nM; 55Mn: ~3100 cps/nM; other: N — slopes of the standard additions (Fig. 2, Table 4); the highest Mn sensitivity, 3560 cps/nM, at pH 8.1; the 5 ppb In tuning solution gave ~1,000,000 cps",
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnitName": "Sample name only — seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 — nM, 3 SD, for the extraction of a 12 mL sample (Table 5)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-P3",
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
                  "schema:value": 1.05,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.05 L/min (varied and optimized daily; Table 2)"
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
                  "schema:value": 13,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "13 L/min (Table 2)"
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
                  "schema:value": 1300,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1300 W (Table 2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 1.2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.2 L/min (varied and optimized daily; Table 2)"
                },
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
                  "schema:value": 150,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "150 uL/min (Table 2)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "LR (R ~300) and MR (R ~4000; stated section 2.4)"
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
              "schema:value": "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P3/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "NASS-5; SAFe S1; SAFe D2 \u2014 NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (\u00a72.6)",
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
              "schema:value": 12,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "12 mL seawater (stated section 2.2)"
            }
          ],
          "schema:name": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "Mn: 0.433 \u00b1 0.026; Fe: 2.791 \u00b1 0.083; Co: 0.078 \u00b1 0.006; Ni: 0.457 \u00b1 0.104; Cu: 0.184 \u00b1 0.027; Zn: 3.044 \u00b1 0.018; Cd: 0.045 \u00b1 0.003; Pb: 0.017 \u00b1 0.001 \u2014 pmol, mean reagent blank \u00b1 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)",
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
                "schema:value": "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated"
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
            "schema:description": "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)"
      },
      "schema:identifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
      "schema:description": "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (\u00a72.2\u20132.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] \u2014 Table 6"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] \u2014 Table 6"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: %RSD, with 1 S.D. for blanks \u2014 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank \u00b1 1S.D.'"
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
    "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\""
  ],
  "ada:sensitivityYield": "59Co: ~5000 cps/nM; 55Mn: ~3100 cps/nM; other: N \u2014 slopes of the standard additions (Fig. 2, Table 4); the highest Mn sensitivity, 3560 cps/nM, at pH 8.1; the 5 ppb In tuning solution gave ~1,000,000 cps",
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnitName": "Sample name only \u2014 seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 \u2014 nM, 3 SD, for the extraction of a 12 mL sample (Table 5)",
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

ex:solutionSficpmsTAPP-detail-P3 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] — Table 6" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] — Table 6" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: %RSD, with 1 S.D. for blanks — 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank ± 1S.D.'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Open-ocean seawater; off-line pre-concentration using Toyopearl AF-Chelate-650M chelating resin (stated section 2.2)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:description "Off-line pre-concentration on Toyopearl AF-Chelate-650M resin; enriched isotope spikes added before extraction; standard additions for Mn and Co (§2.2–2.3)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "NASS-5; SAFe S1; SAFe D2 — NASS-5 (NRCC certified open-ocean seawater) and the SAFe inter-comparison samples (§2.6)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "National High Magnetic Field Laboratory (NHMFL), Florida State University (stated section 2.4)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "Mn: 0.433 ± 0.026; Fe: 2.791 ± 0.083; Co: 0.078 ± 0.006; Ni: 0.457 ± 0.104; Cu: 0.184 ± 0.027; Zn: 3.044 ± 0.018; Cd: 0.045 ± 0.003; Pb: 0.017 ± 0.001 — pmol, mean reagent blank ± 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"Nebuliser PFA microflow (PFA-100), Elemental Scientific\"; \"Nebuliser sample uptake rate 150 uL min-1\"; \"Autosampler CETAC ASX-100\". The flow-injection manifold of sec 2.2 is the offline pre-concentration step, not the ICP-MS introduction: \"prevented the online coupling of the flow injection system directly to an ICP-MS\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 — nM, 3 SD, for the extraction of a 12 mL sample (Table 5)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008" ;
    ada:samplingUnitName "Sample name only — seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled" ;
    ada:sensitivityYield "59Co: ~5000 cps/nM; 55Mn: ~3100 cps/nM; other: N — slopes of the standard additions (Fig. 2, Table 4); the highest Mn sensitivity, 3560 cps/nM, at pH 8.1; the 5 ppb In tuning solution gave ~1,000,000 cps" ;
    ada:sessionIdentifier "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionSficpmsTAPP-detail-P3/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "Partially -- \"A mass bias correction factor for each of the six elements was calculated from the measured natural isotopic ratio divided by the true natural isotopic ratio\". The true natural isotopic ratios used, and their source, are not stated" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.05 L/min (varied and optimized daily; Table 2)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.05e+00 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "13 L/min (Table 2)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 13 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"At the start of each day, prior to any sample analysis, the instrument was first tuned to produce maximum sensitivity and stability while also maintaining low oxide formation ... using a 5ppb solution of In\"; \"Further tuning using a 5ppb solution of Fe in the medium resolution mode ensured maximum separation of the 56Fe peak from the 40Ar16O peak\"; oxide formation \"typically below 5%\", above 10% causing problems" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "LR (R ~300) and MR (R ~4000; stated section 2.4)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1300 W (Table 2)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1300 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.2 L/min (varied and optimized daily; Table 2)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.2e+00 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "12 mL seawater (stated section 2.2)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 12 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "150 uL/min (Table 2)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 150 .


```


### detail example P4
detail instance derived from Misra+etal2014 | Thermo Element XR | Univ Cambridge.
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
  "@id": "ex:solutionSficpmsTAPP-detail-P4",
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
              "schema:value": "LR and MR (stated Table 1 and section 2.3)"
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
              "schema:value": "120 s washout (Table 1)"
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
              "schema:value": "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\""
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
                  "schema:description": "1250 W (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
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
                  "schema:description": "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/Sample-Introduction-System"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix — the four Cambridge consistency standards (§2.2)",
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
                "schema:value": "all: detector cross-calibration between pulse and analog modes performed daily — §2.3.1"
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
            "schema:description": "Handpicked 1–2 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 µL of supernatant diluted with 200 µL 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF — §2.4; the HF-bearing matrix 'was used only in the final dilution step'",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
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
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1-2 mg foraminifera shells (stated section 2.4)"
            }
          ],
          "schema:name": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "B: 2.0 ± 1.0 µmol/mol (as B/Ca); other: N — abstract",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
      },
      "schema:identifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
      "schema:description": "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (§2.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [B/Ca: 4.0% (2σ), average within-run external precision] — abstract"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: ±2σ of repeat analyses over 8 months] — Table 4; n = 180, 130, 100 and 150"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] — Fig. 2"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:sensitivityYield": "N — 'a typical sensitivity of 2.5 × 10^6 cps/ppb on 115In' (§3.1), the tuning isotope; 1 ppb 11B and 115In sensitivities by spray chamber, injector and acid matrix in Table 2",
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnitName": "Sample name only — consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "B/Ca: 2 µmol/mol; other: N — 'We report a B/Ca detection limit of 2 µmol/mol' (abstract)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-P4",
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
              "schema:value": "LR and MR (stated Table 1 and section 2.3)"
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
              "schema:value": "120 s washout (Table 1)"
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
              "schema:value": "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\""
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
                  "schema:description": "1250 W (Table 1)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
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
                  "schema:description": "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/Sample-Introduction-System"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-P4/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix \u2014 the four Cambridge consistency standards (\u00a72.2)",
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
                "schema:value": "all: detector cross-calibration between pulse and analog modes performed daily \u2014 \u00a72.3.1"
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
            "schema:description": "Handpicked 1\u20132 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 \u00b5L of supernatant diluted with 200 \u00b5L 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF \u2014 \u00a72.4; the HF-bearing matrix 'was used only in the final dilution step'",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample digestion",
            "schema:position": 3,
            "@type": [
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
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1-2 mg foraminifera shells (stated section 2.4)"
            }
          ],
          "schema:name": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "B: 2.0 \u00b1 1.0 \u00b5mol/mol (as B/Ca); other: N \u2014 abstract",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)"
      },
      "schema:identifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
      "schema:description": "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (\u00a72.3)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "all [B/Ca: 4.0% (2\u03c3), average within-run external precision] \u2014 abstract"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: \u00b12\u03c3 of repeat analyses over 8 months] \u2014 Table 4; n = 180, 130, 100 and 150"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] \u2014 Fig. 2"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer"
  ],
  "ada:sensitivityYield": "N \u2014 'a typical sensitivity of 2.5 \u00d7 10^6 cps/ppb on 115In' (\u00a73.1), the tuning isotope; 1 ppb 11B and 115In sensitivities by spray chamber, injector and acid matrix in Table 2",
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnitName": "Sample name only \u2014 consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "B/Ca: 2 \u00b5mol/mol; other: N \u2014 'We report a B/Ca detection limit of 2 \u00b5mol/mol' (abstract)",
  "ada:limitOfQuantificationMethod": "missing"
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

ex:solutionSficpmsTAPP-detail-P4 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "all [B/Ca: 4.0% (2σ), average within-run external precision] — abstract" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: ±2σ of repeat analyses over 8 months] — Table 4; n = 180, 130, 100 and 150" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] — Fig. 2" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample digestion" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Handpicked 1–2 mg of species- and size-specific shells, cracked, clay removed (MQ water, methanol), reductively and/or oxidatively cleaned, leached in 0.001 M HNO3, dissolved in 1 M HNO3 and centrifuged; 5 µL of supernatant diluted with 200 µL 0.1 M HNO3 as the Me/Ca stock, Ca measured by ICP-AES, then diluted to [Ca] 10 ppm with 0.1 M HNO3 + 0.3 M HF — §2.4; the HF-bearing matrix 'was used only in the final dilution step'" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:description "Teflon Scott-type single-pass spray chamber and platinum injector (1.8 mm I.D.) to reduce instrumental boron blanks; HF in the final matrix for rapid boron washout (§2.3)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "N -- \"a single instrument session\" referenced; no session identifier stated" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "CAM-wuellerstorfi; CAM-Uvig-1; CAM-Uvig-2; CAM-Mix — the four Cambridge consistency standards (§2.2)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Godwin Laboratory for Palaeoclimate Research, University of Cambridge (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "B: 2.0 ± 1.0 µmol/mol (as B/Ca); other: N — abstract" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"a Teflon Scott type (single pass) spray chamber was constructed\"; \"we used a platinum injector (1.8 mm I.D.)\"; ESI nebulizer" ;
    ada:detectionLimit "B/Ca: 2 µmol/mol; other: N — 'We report a B/Ca detection limit of 2 µmol/mol' (abstract)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction" ;
    ada:samplingUnitName "Sample name only — consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)" ;
    ada:sensitivityYield "N — 'a typical sensitivity of 2.5 × 10^6 cps/ppb on 115In' (§3.1), the tuning isotope; 1 ppb 11B and 115In sensitivities by spray chamber, injector and acid matrix in Table 2" ;
    ada:sessionIdentifier "N -- \"a single instrument session\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionSficpmsTAPP-detail-P4/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "\"Instrumental sensitivity was optimized on 11B, 115In, and 175Lu\", with sensitivities \"set as operational criteria\"; \"in medium resolution tuning, the instrument was optimized on 56Fe to achieve a mass resolution\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "LR and MR (stated Table 1 and section 2.3)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "120 s washout (Table 1)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1250 W (Table 1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1250 .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "all: detector cross-calibration between pulse and analog modes performed daily — §2.3.1" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "1-2 mg foraminifera shells (stated section 2.4)" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "50 uL ESI nebulizer; uptake time 70 s (Table 1); volumetric flow rate N" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .


```


### detail example Willbold2005
detail instance derived from Willbold2005 | ThermoFinnigan ELEMENT2 | MPI Mainz.
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
  "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005",
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
                  "schema:description": "0.9 L/min (Table 3)"
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
                  "schema:description": "15 L/min (Table 3)"
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
                  "schema:value": 1235,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1235 W (Table 3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 1.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.0 L/min (sample gas; Table 3)"
                },
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
                  "schema:description": "~100 uL/min (Table 3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)",
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
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
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
                "schema:value": "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N"
              },
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
                "schema:description": "hotplate HF-HNO3: 130 °C; bomb HF-HNO3: 180 °C; fluoride removal: ca. 80 °C (evaporation); chloride conversion: 80 °C, then 50 °C (evaporation); final uptake: N"
              }
            ],
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
                "schema:value": "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'"
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
                "schema:value": "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\""
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1–3), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution — cleanroom, twice sub-boiled acids (Samples and sample preparation)",
            "@type": [
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
              "schema:description": "About 100 mg of whole-rock powder"
            }
          ],
          "schema:name": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "N — the total procedural blanks enter only through the LOD",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
      },
      "schema:description": "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90%",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] — Table 4"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-1 [all: RSD of five independent digestions over 4 months, 1–3%] — abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-1 [all: within 1–2% of published ID data and 2–3% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3–4% of published data] — abstract; Table 5"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD — Tables 4 and 5"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnitName": "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8–9); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "all: about 0.1 to 10 ng/g sample equivalent for most elements — Figure 2",
  "ada:limitOfQuantificationMethod": "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g — 'about 10 to 20 times the LOD for most elements'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005",
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
                  "schema:description": "0.9 L/min (Table 3)"
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
                  "schema:description": "15 L/min (Table 3)"
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
                  "schema:value": 1235,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1235 W (Table 3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/ICP-Source"
            },
            {
              "schema:additionalType": [
                "Sample Introduction System",
                {
                  "@id": "https://www.wikidata.org/entity/Q3099911"
                }
              ],
              "schema:additionalProperty": [
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
                  "schema:value": 1.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.0 L/min (sample gas; Table 3)"
                },
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
                  "schema:description": "~100 uL/min (Table 3)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "missing",
              "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/Sample-Introduction-System"
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
              "schema:value": "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS"
        },
        {
          "ada:reagentRole": "referenceMaterial",
          "schema:name": "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)",
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
            "schema:name": "Sample digestion",
            "schema:additionalProperty": [
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
                "schema:value": "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N"
              },
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
                "schema:description": "hotplate HF-HNO3: 130 \u00b0C; bomb HF-HNO3: 180 \u00b0C; fluoride removal: ca. 80 \u00b0C (evaporation); chloride conversion: 80 \u00b0C, then 50 \u00b0C (evaporation); final uptake: N"
              }
            ],
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
                "schema:value": "Dixon outlier test on each block of ten ratios \u2014 'Generally, less than one ratio had to be excluded from the whole data set'"
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
                "schema:value": "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\""
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1\u20133), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution \u2014 cleanroom, twice sub-boiled acids (Samples and sample preparation)",
            "@type": [
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
              "schema:description": "About 100 mg of whole-rock powder"
            }
          ],
          "schema:name": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
          "schema:description": "no value available: schema:description"
        }
      ],
      "ada:proceduralBlankLevel": "N \u2014 the total procedural blanks enter only through the LOD",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)"
      },
      "schema:description": "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90%",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] \u2014 Table 4"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "BHVO-1 [all: RSD of five independent digestions over 4 months, 1\u20133%] \u2014 abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "BHVO-1 [all: within 1\u20132% of published ID data and 2\u20133% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3\u20134% of published data] \u2014 abstract; Table 5"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: RSD \u2014 Tables 4 and 5"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\""
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnitName": "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8\u20139); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:detectionLimit": "all: about 0.1 to 10 ng/g sample equivalent for most elements \u2014 Figure 2",
  "ada:limitOfQuantificationMethod": "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g \u2014 'about 10 to 20 times the LOD for most elements'"
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

ex:solutionSficpmsTAPP-detail-Willbold2005 a schema1:Dataset,
        schema1:Product ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] — Table 4" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "BHVO-1 [all: RSD of five independent digestions over 4 months, 1–3%] — abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "BHVO-1 [all: within 1–2% of published ID data and 2–3% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3–4% of published data] — abstract; Table 5" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: RSD — Tables 4 and 5" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration>,
                                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
                            schema1:name "Sample digestion" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "About 100 mg whole-rock powder spiked with the three multi-element spikes (MES 1–3), digested in HF-HNO3, converted to chlorides, taken up in 7 mol/l HNO3 and diluted for LR and HR, with a Ru-Re solution added to each dilution — cleanroom, twice sub-boiled acids (Samples and sample preparation)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues>,
                                <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Magnetic jump followed by electric scan (Table 3); acquisition 10 min per sample; ca. 20 min per sample in all, a mass spectrometer efficiency of almost 90%" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:DefinedTerm ;
                    schema1:additionalType wd:Q2356542 ;
                    schema1:name "AGV-1, AGV-2, BCR-1, BCR-2, BHVO-1, BHVO-2, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, BIR-1, OU-6, BCR-2G, BHVO-2G, BIR-1G, PCC-1 (stated Table 5)" ;
                    ada:reagentRole "referenceMaterial" ],
                <https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Max-Planck-Institut fuer Chemie (MPIC), Mainz, Germany (affiliation)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
                    schema1:description "no value available: schema:description" ;
                    schema1:name "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "N — the total procedural blanks enter only through the LOD" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous) -- \"The ELEMENT2 was equipped with an ESI microconcentric Teflon nebuliser (flow rate ca. 100 ul min-1) and an ESI Teflon spray chamber\"; \"Sample uptake rate ca. 100 ul min-1\"" ;
    ada:detectionLimit "all: about 0.1 to 10 ng/g sample equivalent for most elements — Figure 2" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:limitOfQuantificationMethod "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g — 'about 10 to 20 times the LOD for most elements'" ;
    ada:oxideProduction "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)" ;
    ada:samplingUnitName "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8–9); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 .

<https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType wd:Q3099911,
        "ICPMS" ;
    schema1:hasPart <https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/Sample-Introduction-System> ;
    schema1:name "no value available: schema:name" .

<https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType wd:Q3099911,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/solutionSficpmsTAPP-detail-Willbold2005/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:additionalType wd:Q3099911,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> a schema1:PropertyValue ;
    schema1:name "Constants Reference Values" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValues> ;
    schema1:value "Relative atomic masses M_El and M_S \"(Loss 2003)\"; \"the known natural isotopic abundances of the isotopes i and k in the sample (Rosman and Taylor 1998)\", stated to be adequately known (\"uncertainty < 0.2%\"); in-run mass fractionation determined \"by comparing determined 47Ti/49Ti, 99Ru/101Ru (in LR mode), 151Eu/153Eu (in HR mode) and 185Re/187Re ratios with known values (Rosman and Taylor 1998)\". For Pb the paper compares two reference choices -- \"average Pb isotope abundances (Rosman and Taylor 1998)\" versus the BHVO-1 TIMS composition of \"Woodhead and Hergt 2000\" -- and quantifies the consequence: \"The difference between both approaches is 0.4% (concentration of Pb: 2.13 ug g-1 versus 2.14 ug g-1)\"" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.9 L/min (Table 3)" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "15 L/min (Table 3)" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "LR (M/Delta-m = 300) and HR (M/Delta-m = 11000; stated section on instrumentation)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1235 W (Table 3)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1235 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> a schema1:PropertyValue ;
    schema1:name "Digestion Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDuration> ;
    schema1:value "hotplate HF-HNO3: 12 h; bomb HF-HNO3: 7 days; other: N" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> a schema1:PropertyValue ;
    schema1:description "hotplate HF-HNO3: 130 °C; bomb HF-HNO3: 180 °C; fluoride removal: ca. 80 °C (evaporation); chloride conversion: 80 °C, then 50 °C (evaporation); final uptake: N" ;
    schema1:name "Digestion Temperature" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperature> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> a schema1:PropertyValue ;
    schema1:description "1.0 L/min (sample gas; Table 3)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1e+00 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> a schema1:PropertyValue ;
    schema1:description "About 100 mg of whole-rock powder" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolume> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> a schema1:PropertyValue ;
    schema1:description "~100 uL/min (Table 3)" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing
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
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                allOf:
                                - contains:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                  minContains: 0
                                  maxContains: 1
                                - contains:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                  minContains: 0
                                  maxContains: 1
                                - contains:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
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
                                const: Sample Introduction System
                              schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                          required:
                          - schema:additionalType
                    schema:additionalProperty:
                      type: array
                      items:
                        anyOf:
                        - title: Doubly-Charged Species Monitor
                          description: "The mass ratio monitored to estimate doubly-charged
                            ion (M\xB2\u207A) formation during instrument tuning.
                            The monitor species and the mass positions monitored should
                            be stated explicitly. Analogous to Oxide Production Method
                            and Threshold for oxide monitoring."
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
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
                              const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                      allOf:
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
                              const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
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
                              const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
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
          schema:additionalProperty:
            type: array
            items:
              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
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
  itemIdentifier: ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld)

## Sources

* [Solution_SF-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail`

