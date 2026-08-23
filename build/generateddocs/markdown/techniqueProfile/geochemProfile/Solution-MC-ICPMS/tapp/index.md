
# Solution MC-ICP-MS Technique-Aligned Procedure Profile (solutionMcicpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.tapp` *v0.1*

Solution multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/Solution_MC-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### solutionMcicpmsTAPP example P0
solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP Münster.
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
  "@id": "ex:solutionMcicpmsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P0",
  "schema:description": "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP Münster (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Chondrules, matrix separates and bulk rock of the Allende CV3 chondrite"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.3,
          "schema:description": "0.3–0.5 g digested; ~100 ng Mo consumed per measurement"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated"
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
            "schema:defaultValue": "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half"
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
            "schema:value": "\"closed Savillex beakers\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"HF–HNO3(–HClO4), followed by inverse aqua regia\"",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Standard sample and (H) skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "schema:value": "Savillex C-Flow PFA nebulizer"
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
              "schema:description": "~50 µl/min"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Cetac Aridus II"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "Alfa Aesar Mo solution standard",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\""
  ],
  "ada:reportedProperties": [
    "εiMo relative to the Alfa Aesar solution standard, εiMo = [(iMo/96Mo)sample/(iMo/96Mo)standard − 1] x 10^4"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut für Planetologie, University of Münster"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TIMS — Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Digestion aliquot — \"All samples (0.3–0.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "98Mo/96Mo = 1.453173",
  "ada:chromatographicSeparationApplied": "Yes — two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mo (and Ba by TIMS)"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P0",
  "schema:description": "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP M\u00fcnster (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Chondrules, matrix separates and bulk rock of the Allende CV3 chondrite"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 0.3,
          "schema:description": "0.3\u20130.5 g digested; ~100 ng Mo consumed per measurement"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated"
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
            "schema:defaultValue": "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half"
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
            "schema:value": "\"closed Savillex beakers\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"HF\u2013HNO3(\u2013HClO4), followed by inverse aqua regia\"",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Standard sample and (H) skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "schema:value": "Savillex C-Flow PFA nebulizer"
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
              "schema:description": "~50 \u00b5l/min"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Cetac Aridus II"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "Alfa Aesar Mo solution standard",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\""
  ],
  "ada:reportedProperties": [
    "\u03b5iMo relative to the Alfa Aesar solution standard, \u03b5iMo = [(iMo/96Mo)sample/(iMo/96Mo)standard \u2212 1] x 10^4"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut f\u00fcr Planetologie, University of M\u00fcnster"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TIMS \u2014 Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Digestion aliquot \u2014 \"All samples (0.3\u20130.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "98Mo/96Mo = 1.453173",
  "ada:chromatographicSeparationApplied": "Yes \u2014 two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mo (and Ba by TIMS)"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P0 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"HF–HNO3(–HClO4), followed by inverse aqua regia\"" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP Münster (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institut für Planetologie, University of Münster" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P0" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Chondrules, matrix separates and bulk rock of the Allende CV3 chondrite" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TIMS — Ba isotopes on a Thermo Scientific Triton Plus at the same institute; Hf-W on the same sample digestions" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Mo (and Ba by TIMS)" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalNormalizationElementAndIsotopeRatio "98Mo/96Mo = 1.453173" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "Alfa Aesar Mo solution standard" ;
    ada:reportedProperties "εiMo relative to the Alfa Aesar solution standard, εiMo = [(iMo/96Mo)sample/(iMo/96Mo)standard − 1] x 10^4" ;
    ada:sampleSequenceDesign "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"" ;
    ada:samplingUnit "Digestion aliquot — \"All samples (0.3–0.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "98Mo/96Mo = 1.453173 for internal normalization; 134Ba/136Ba = 0.3078 (Carlson et al. 2007) for the TIMS half" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Cetac Aridus II" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "\"closed Savillex beakers\"" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Savillex C-Flow PFA nebulizer" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3e-01 ;
    schema1:description "0.3–0.5 g digested; ~100 ng Mo consumed per measurement" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "~50 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch>,
        <https://example.org/instrument/part/Collector> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:name "Collector" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Standard sample and (H) skimmer cones" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni" .


```


### solutionMcicpmsTAPP example P1
solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI.
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
  "@id": "ex:solutionMcicpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P1",
  "schema:description": "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Sulfate minerals (anhydrite, barite, gypsum) and sulfide minerals (pyrite, chalcopyrite)"
          ]
        },
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
          "schema:description": "<50 mg weighed; 500 µg S taken for column purification"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral standard cut as a 2 mm thick section, polished and mounted on a 45x25 mm petrographic slide for the laser half; solution half dissolved from weighed mineral",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "\"Pt-guard electrode: On, grounded\""
          }
        ],
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
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
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
            "schema:value": "15 ml PTFE digestion vessel"
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
            "schema:description": "\"less than 70 °C\" for the first evaporation; 70 °C for the total digestion"
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
            "schema:defaultValue": "Not stated for the individual steps beyond \"taken to dryness\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "5 ml HNO3 (50%), then 3 ml concentrated HNO3 + 2 mL HCl (50%); residue dissolved in 4 mL 2% HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "NEPTUNE (\"Thermo Electron NEPTUNE\")",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "X-cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "schema:value": "PFA-50, Elemental Scientific, Inc."
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
              "schema:value": "SSI cyclonic spray dual chamber, Elemental Scientific, Inc.; cooling not stated"
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
              "schema:description": "50 µL/min"
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
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8–0.9 L/min Ar (sample gas)"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1150,
              "schema:description": "~1150 W"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "~15 L/min Ar"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8 L/min Ar"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Wet plasma — solutions \"introduced as a 'wet' aerosol (in 2% HNO3) into the ICP torch via a cyclonic spray dual chamber\"; dry plasma deliberately rejected as \"not viable for bulk analysis\""
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
          "schema:description": "32S(L3), 33S(C), 34S(H3)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "\"High (entrance slit); Low (detector slit)\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Wash-out 2 min for solution"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None — and deliberately: \"passing solutions through a desolvating nebulizer to obtain dry plasma conditions is not viable for bulk analysis\""
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123",
  "ada:secondaryReferenceMaterialDefault": [
    "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions"
  ],
  "ada:reportedProperties": [
    "δ34S and δ33S in permil vs V-CDT"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Woods Hole Oceanographic Institution"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-ablation MC-ICP-MS — the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"",
        "schema:description": "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable — \"Our setup allows for interchangeable bulk and in situ S isotope measurement\""
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Purified solution aliquot — \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 µg of S\" taken for column purification",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98±4%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "2% (w/w) HNO3, 50 ppm S stock",
  "ada:washTimeBetweenSamples": "2 min for solution work (4 min for laser)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "S"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P1",
  "schema:description": "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Sulfate minerals (anhydrite, barite, gypsum) and sulfide minerals (pyrite, chalcopyrite)"
          ]
        },
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
          "schema:description": "<50 mg weighed; 500 \u00b5g S taken for column purification"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mineral standard cut as a 2 mm thick section, polished and mounted on a 45x25 mm petrographic slide for the laser half; solution half dissolved from weighed mineral",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "\"Pt-guard electrode: On, grounded\""
          }
        ],
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
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
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
            "schema:value": "15 ml PTFE digestion vessel"
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
            "schema:description": "\"less than 70 \u00b0C\" for the first evaporation; 70 \u00b0C for the total digestion"
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
            "schema:defaultValue": "Not stated for the individual steps beyond \"taken to dryness\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "5 ml HNO3 (50%), then 3 ml concentrated HNO3 + 2 mL HCl (50%); residue dissolved in 4 mL 2% HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "NEPTUNE (\"Thermo Electron NEPTUNE\")",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "X-cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "schema:value": "PFA-50, Elemental Scientific, Inc."
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
              "schema:value": "SSI cyclonic spray dual chamber, Elemental Scientific, Inc.; cooling not stated"
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
              "schema:description": "50 \u00b5L/min"
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
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8\u20130.9 L/min Ar (sample gas)"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1150,
              "schema:description": "~1150 W"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "~15 L/min Ar"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8 L/min Ar"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Wet plasma \u2014 solutions \"introduced as a 'wet' aerosol (in 2% HNO3) into the ICP torch via a cyclonic spray dual chamber\"; dry plasma deliberately rejected as \"not viable for bulk analysis\""
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
          "schema:description": "32S(L3), 33S(C), 34S(H3)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "\"High (entrance slit); Low (detector slit)\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Wash-out 2 min for solution"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None \u2014 and deliberately: \"passing solutions through a desolvating nebulizer to obtain dry plasma conditions is not viable for bulk analysis\""
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123",
  "ada:secondaryReferenceMaterialDefault": [
    "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions"
  ],
  "ada:reportedProperties": [
    "\u03b434S and \u03b433S in permil vs V-CDT"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Woods Hole Oceanographic Institution"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-ablation MC-ICP-MS \u2014 the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"",
        "schema:description": "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable \u2014 \"Our setup allows for interchangeable bulk and in situ S isotope measurement\""
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Purified solution aliquot \u2014 \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 \u00b5g of S\" taken for column purification",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98\u00b14%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "2% (w/w) HNO3, 50 ppm S stock",
  "ada:washTimeBetweenSamples": "2 min for solution work (4 min for laser)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "S"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:solutionMcicpmsTAPP-P1 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Mineral standard cut as a 2 mm thick section, polished and mounted on a 45x25 mm petrographic slide for the laser half; solution half dissolved from weighed mineral" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/guardElectrode> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "5 ml HNO3 (50%), then 3 ml concentrated HNO3 + 2 mL HCl (50%); residue dissolved in 4 mL 2% HNO3" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Woods Hole Oceanographic Institution" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Sulfate minerals (anhydrite, barite, gypsum) and sulfide minerals (pyrite, chalcopyrite)" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: the laser is connected directly to the spray chamber so ablated particles mix with 2% HNO3 and are \"effectively analyzed as a wet plasma ensuring that ablated aerosols are closely matrix-matched to solution standards\". Sequence: interchangeable — \"Our setup allows for interchangeable bulk and in situ S isotope measurement\"" ;
                    schema1:name "Laser-ablation MC-ICP-MS — the same NEPTUNE, with a NewWave UP213 laser, \"such that laser ablation and solution aspiration can be operated simultaneously\"" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "S" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98±4%" ;
    ada:finalSolutionMatrix "2% (w/w) HNO3, 50 ppm S stock" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123" ;
    ada:reportedProperties "δ34S and δ33S in permil vs V-CDT" ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Purified solution aliquot — \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 µg of S\" taken for column purification" ;
    ada:secondaryReferenceMaterialDefault "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "2 min for solution work (4 min for laser)" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None — and deliberately: \"passing solutions through a desolvating nebulizer to obtain dry plasma conditions is not viable for bulk analysis\"" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Not stated for the individual steps beyond \"taken to dryness\"" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 70 ;
    schema1:description "\"less than 70 °C\" for the first evaporation; 70 °C for the total digestion" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "15 ml PTFE digestion vessel" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "~0.8–0.9 L/min Ar (sample gas)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "PFA-50, Elemental Scientific, Inc." ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "<50 mg weighed; 500 µg S taken for column purification" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "50 µL/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "SSI cyclonic spray dual chamber, Elemental Scientific, Inc.; cooling not stated" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "~0.8 L/min Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "~15 L/min Ar" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Wash-out 2 min for solution" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1150 ;
    schema1:description "~1150 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "NEPTUNE (\"Thermo Electron NEPTUNE\")" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "32S(L3), 33S(C), 34S(H3)" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/guardElectrode> a schema1:PropertyValue ;
    schema1:name "Guard Electrode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/guardElectrode> ;
    schema1:value "\"Pt-guard electrode: On, grounded\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "X-cones" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "\"High (entrance slit); Low (detector slit)\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Wet plasma — solutions \"introduced as a 'wet' aerosol (in 2% HNO3) into the ICP torch via a cyclonic spray dual chamber\"; dry plasma deliberately rejected as \"not viable for bulk analysis\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni" .


```


### solutionMcicpmsTAPP example P2
solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P2",
  "schema:description": "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv). Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero from a blank solution subtracted from all measurements.",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Iron meteorites and terrestrial basalt geostandards"
          ]
        },
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
          "schema:description": "~1-2 mg Fe per analysis; ~50 mg meteorite pieces"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
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
            "schema:defaultValue": "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)"
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
            "schema:value": "Hot plate, closed vessel not specified beyond \"on a hot plate\""
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
            "schema:defaultValue": 120,
            "schema:description": "Iron meteorites 120 °C; basalts 150 °C"
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
            "schema:defaultValue": "Iron meteorites 24 hours; basalts 48 hours"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Iron meteorites: aqua regia (3:1 HCl-HNO3). Basalts: HF-HNO3 (2:1) followed by several steps of aqua regia. All converted to chloride and redissolved in 0.25 ml 10 M HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune \"upgraded to Neptune Plus specifications\"",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "H skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "\"We used Ni or Pt sampler and H skimmer cones ... The main motivation for using Pt cones was an increase in sensitivity and a decrease in the frequency of cone cleaning\""
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
              "schema:value": "Cyclonic glass spray chamber (wet) or ESI Apex Ω desolvating nebulizer (dry)"
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
              "schema:value": "Cyclonic glass spray chamber for wet-plasma MR-mode work; cooling not stated"
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
              "schema:description": "~100 µl/min"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Both, by mode — \"either a cyclonic glass spray chamber (wet plasma, MR-mode, Pt cones) or an ESI Apex Ω desolvating nebulizer system (dry plasma, HR-mode, Ni cones)\""
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
          "schema:description": "54Fe, 56Fe, 57Fe, 58Fe in static mode, with 53Cr and 60Ni monitored simultaneously",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium or high resolution — \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 2,
          "schema:description": "None — the Apex Ω was run \"with no auxiliary N2 flow\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "210 s washout between all measurements"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "ESI Apex Ω for HR-mode dry plasma work, \"with no auxiliary N2 flow\"; none for MR-mode wet plasma"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "On-peak zero (acid blank)",
  "ada:primaryStandardNameDefault": "IRMM-524a",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2 and BCR-2"
  ],
  "ada:reportedProperties": [
    "µ-notation Fe isotope ratios relative to IRMM-524a"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Prior Pt, Mo, Ni and/or W isotope analyses on the same digestions"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Solution aliquot of a digestion — \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014",
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3 (measured at 10 µg/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"",
  "ada:washTimeBetweenSamples": "210 s",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Fe"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P2",
  "schema:description": "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv). Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero from a blank solution subtracted from all measurements.",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Iron meteorites and terrestrial basalt geostandards"
          ]
        },
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
          "schema:description": "~1-2 mg Fe per analysis; ~50 mg meteorite pieces"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
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
            "schema:defaultValue": "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)"
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
            "schema:value": "Hot plate, closed vessel not specified beyond \"on a hot plate\""
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
            "schema:defaultValue": 120,
            "schema:description": "Iron meteorites 120 \u00b0C; basalts 150 \u00b0C"
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
            "schema:defaultValue": "Iron meteorites 24 hours; basalts 48 hours"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Iron meteorites: aqua regia (3:1 HCl-HNO3). Basalts: HF-HNO3 (2:1) followed by several steps of aqua regia. All converted to chloride and redissolved in 0.25 ml 10 M HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune \"upgraded to Neptune Plus specifications\"",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "H skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "\"We used Ni or Pt sampler and H skimmer cones ... The main motivation for using Pt cones was an increase in sensitivity and a decrease in the frequency of cone cleaning\""
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
              "schema:value": "Cyclonic glass spray chamber (wet) or ESI Apex \u03a9 desolvating nebulizer (dry)"
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
              "schema:value": "Cyclonic glass spray chamber for wet-plasma MR-mode work; cooling not stated"
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
              "schema:description": "~100 \u00b5l/min"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Both, by mode \u2014 \"either a cyclonic glass spray chamber (wet plasma, MR-mode, Pt cones) or an ESI Apex \u03a9 desolvating nebulizer system (dry plasma, HR-mode, Ni cones)\""
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
          "schema:description": "54Fe, 56Fe, 57Fe, 58Fe in static mode, with 53Cr and 60Ni monitored simultaneously",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium or high resolution \u2014 \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 2,
          "schema:description": "None \u2014 the Apex \u03a9 was run \"with no auxiliary N2 flow\""
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "210 s washout between all measurements"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "ESI Apex \u03a9 for HR-mode dry plasma work, \"with no auxiliary N2 flow\"; none for MR-mode wet plasma"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "On-peak zero (acid blank)",
  "ada:primaryStandardNameDefault": "IRMM-524a",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2 and BCR-2"
  ],
  "ada:reportedProperties": [
    "\u00b5-notation Fe isotope ratios relative to IRMM-524a"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Prior Pt, Mo, Ni and/or W isotope analyses on the same digestions"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Solution aliquot of a digestion \u2014 \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014",
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3 (measured at 10 \u00b5g/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"",
  "ada:washTimeBetweenSamples": "210 s",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Fe"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P2 a cdi:Activity,
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
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Iron meteorites: aqua regia (3:1 HCl-HNO3). Basalts: HF-HNO3 (2:1) followed by several steps of aqua regia. All converted to chloride and redissolved in 0.25 ml 10 M HCl" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv). Reported detail: ada:blankBackgroundCorrectionMethod = On-peak zero from a blank solution subtracted from all measurements." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Chicago" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Iron meteorites and terrestrial basalt geostandards" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Prior Pt, Mo, Ni and/or W isotope analyses on the same digestions" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Fe" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "On-peak zero (acid blank)" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%" ;
    ada:finalSolutionMatrix "0.3 M HNO3 (measured at 10 µg/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"" ;
    ada:internalNormalizationElementAndIsotopeRatio "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "IRMM-524a" ;
    ada:reportedProperties "µ-notation Fe isotope ratios relative to IRMM-524a" ;
    ada:sampleSequenceDesign "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"" ;
    ada:samplingUnit "Solution aliquot of a digestion — \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2 and BCR-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "210 s" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "ESI Apex Ω for HR-mode dry plasma work, \"with no auxiliary N2 flow\"; none for MR-mode wet plasma" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Iron meteorites 24 hours; basalts 48 hours" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 120 ;
    schema1:description "Iron meteorites 120 °C; basalts 150 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Hot plate, closed vessel not specified beyond \"on a hot plate\"" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Cyclonic glass spray chamber (wet) or ESI Apex Ω desolvating nebulizer (dry)" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "~1-2 mg Fe per analysis; ~50 mg meteorite pieces" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Cyclonic glass spray chamber for wet-plasma MR-mode work; cooling not stated" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "None — the Apex Ω was run \"with no auxiliary N2 flow\"" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "210 s washout between all measurements" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune \"upgraded to Neptune Plus specifications\"" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "54Fe, 56Fe, 57Fe, 58Fe in static mode, with 53Cr and 60Ni monitored simultaneously" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "H skimmer cones" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "Medium or high resolution — \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Both, by mode — \"either a cyclonic glass spray chamber (wet plasma, MR-mode, Pt cones) or an ESI Apex Ω desolvating nebulizer system (dry plasma, HR-mode, Ni cones)\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "\"We used Ni or Pt sampler and H skimmer cones ... The main motivation for using Pt cones was an increase in sensitivity and a decrease in the frequency of cone cleaning\"" .


```


### solutionMcicpmsTAPP example P3
solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P3",
  "schema:description": "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Calcium-aluminium-rich inclusions (CAIs)"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": "Two (\"These steps were performed twice\")"
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
            "schema:defaultValue": "Hot plate, temperature not stated"
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
            "schema:defaultValue": "1 week per step, performed twice"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"redissolved in a 2:1 mixture of HCl:HNO3 for 1 week on a hot plate ... These steps were performed twice\"; dried and dissolved in concentrated HNO3, diluted in 3 M HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus \"with the addition of an OnTool booster\"",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Static mode for most REEs; a subconfiguration for Dy and Yb to monitor isobaric interferences",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing — \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "OL-REE series",
  "ada:calibrationMeasurementFrequency": "Every sample, spaced by 300 s rinsing",
  "ada:reportedProperties": [
    "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "ada:samplingUnit": "Fraction of a CAI digestion — \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25–50 µm resin, 94 steps, 188 ml, 16 h at 70 °C, 0.17 ml/min). Overall yields >95%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "15–25 ppb for the most abundant isotope",
  "ada:washTimeBetweenSamples": "300 s rinsing between bracketed measurements",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "The rare earth elements — La",
      "Ce",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Dy",
      "Er",
      "Yb and Y"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P3",
  "schema:description": "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Calcium-aluminium-rich inclusions (CAIs)"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" \u2014 an explicit exclusion, on chemical rather than statistical grounds"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": "Two (\"These steps were performed twice\")"
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
            "schema:defaultValue": "Hot plate, temperature not stated"
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
            "schema:defaultValue": "1 week per step, performed twice"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"redissolved in a 2:1 mixture of HCl:HNO3 for 1 week on a hot plate ... These steps were performed twice\"; dried and dissolved in concentrated HNO3, diluted in 3 M HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus \"with the addition of an OnTool booster\"",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Static mode for most REEs; a subconfiguration for Dy and Yb to monitor isobaric interferences",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing \u2014 \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "OL-REE series",
  "ada:calibrationMeasurementFrequency": "Every sample, spaced by 300 s rinsing",
  "ada:reportedProperties": [
    "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "ada:samplingUnit": "Fraction of a CAI digestion \u2014 \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25\u201350 \u00b5m resin, 94 steps, 188 ml, 16 h at 70 \u00b0C, 0.17 ml/min). Overall yields >95%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "15\u201325 ppb for the most abundant isotope",
  "ada:washTimeBetweenSamples": "300 s rinsing between bracketed measurements",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "The rare earth elements \u2014 La",
      "Ce",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Dy",
      "Er",
      "Yb and Y"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"redissolved in a 2:1 mixture of HCl:HNO3 for 1 week on a hot plate ... These steps were performed twice\"; dried and dissolved in concentrated HNO3, diluted in 3 M HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Chicago" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Calcium-aluminium-rich inclusions (CAIs)" ] ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Ce",
                "Dy",
                "Er",
                "Eu",
                "Gd",
                "Nd",
                "Sm",
                "The rare earth elements — La",
                "Yb and Y" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample, spaced by 300 s rinsing" ;
    ada:chromatographicSeparationApplied "Yes — U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25–50 µm resin, 94 steps, 188 ml, 16 h at 70 °C, 0.17 ml/min). Overall yields >95%" ;
    ada:finalSolutionMatrix "15–25 ppb for the most abundant isotope" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "OL-REE series" ;
    ada:reportedProperties "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation" ;
    ada:sampleSequenceDesign "Standard-sample bracketing — \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"" ;
    ada:samplingUnit "Fraction of a CAI digestion — \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "300 s rinsing between bracketed measurements" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "1 week per step, performed twice" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Hot plate, temperature not stated" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value "Two (\"These steps were performed twice\")" ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus \"with the addition of an OnTool booster\"" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "Static mode for most REEs; a subconfiguration for Dy and Yb to monitor isobaric interferences" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .


```


### solutionMcicpmsTAPP example Tissot2020
solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT.
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
  "@id": "ex:solutionMcicpmsTAPP-Tissot2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — Tissot2020",
  "schema:description": "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Single zircon and baddeleyite crystals, and bulk rock"
          ]
        },
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
          "schema:description": "Single crystals; ~50 µl (5% of sample) taken for concentration measurement"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Crushing in a stainless steel mortar, sieving through 375 µm plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "Double-spike inversion, Rmeas = [p·RSpike + (1−p)·RStd·(Mx/Mn)^α]·(Mx/Mi)^β, solved by weighted minimisation over four ratios"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated"
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
            "schema:defaultValue": "238U/235U = 137.818 (45), 18O/16O = 0.00205 (44), and α = 0.18 ± 0.02%/amu from repeat NBS-981 analyses; U decay constants of (47); Th/U[magma] = 2.8 ± 1.0 for the initial 230Th disequilibrium correction"
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
            "schema:value": "\"clean Teflon microcapsules\" inside \"a large-volume Parr digestion vessel\""
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
            "schema:defaultValue": 215,
            "schema:description": "215 °C"
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
            "schema:defaultValue": "Zircon 48 hours (U-Pb) and 60 hours (Zr isotopes)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "29 M HF; after conversion to a chloride matrix for U-Pb. Zr aliquots taken up in 3 M HNO3 + 0.5 M HF",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Plasma II",
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
              "schema:value": "Cetac Aridus II desolvator nebulizer"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Dry plasma — \"Analyses were conducted in dry plasma mode using a Cetac Aridus II desolvator nebulizer\""
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
          "schema:description": "Masses 90, 91, 92, 93, 94, 95, 96 and 98 \"measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block\"",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Cetac Aridus II — \"Analyses were conducted in dry plasma mode\""
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
      "schema:value": "N/A — no added internal standard element"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty"
    }
  ],
  "ada:sampleSequenceDesign": "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "ZrNIST",
  "ada:calibrationMeasurementFrequency": "Every sample — \"Each sample measurement was individually bracketed\"",
  "ada:reportedProperties": [
    "δ9x/90ZrNIST in permil — δ91/90Zr, δ92/90Zr, δ94/90Zr and δ96/90Zr"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Massachusetts Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions",
        "schema:description": "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Single crystal — \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Mathematica — \"Data were reduced using a minimization approach implemented in Mathematica\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG-1X for U-Pb; Ln-Spec (~300 µl, 25–50 µm) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks",
  "ada:isotopeDilutionSpike": "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio",
  "ada:finalSolutionMatrix": "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Zr"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-Tissot2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 Tissot2020",
  "schema:description": "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Single zircon and baddeleyite crystals, and bulk rock"
          ]
        },
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
          "schema:description": "Single crystals; ~50 \u00b5l (5% of sample) taken for concentration measurement"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Crushing in a stainless steel mortar, sieving through 375 \u00b5m plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "Double-spike inversion, Rmeas = [p\u00b7RSpike + (1\u2212p)\u00b7RStd\u00b7(Mx/Mn)^\u03b1]\u00b7(Mx/Mi)^\u03b2, solved by weighted minimisation over four ratios"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated"
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
            "schema:defaultValue": "238U/235U = 137.818 (45), 18O/16O = 0.00205 (44), and \u03b1 = 0.18 \u00b1 0.02%/amu from repeat NBS-981 analyses; U decay constants of (47); Th/U[magma] = 2.8 \u00b1 1.0 for the initial 230Th disequilibrium correction"
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
            "schema:value": "\"clean Teflon microcapsules\" inside \"a large-volume Parr digestion vessel\""
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
            "schema:defaultValue": 215,
            "schema:description": "215 \u00b0C"
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
            "schema:defaultValue": "Zircon 48 hours (U-Pb) and 60 hours (Zr isotopes)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "29 M HF; after conversion to a chloride matrix for U-Pb. Zr aliquots taken up in 3 M HNO3 + 0.5 M HF",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Plasma II",
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
              "schema:value": "Cetac Aridus II desolvator nebulizer"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Dry plasma \u2014 \"Analyses were conducted in dry plasma mode using a Cetac Aridus II desolvator nebulizer\""
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
          "schema:description": "Masses 90, 91, 92, 93, 94, 95, 96 and 98 \"measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block\"",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Cetac Aridus II \u2014 \"Analyses were conducted in dry plasma mode\""
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
      "schema:value": "N/A \u2014 no added internal standard element"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty"
    }
  ],
  "ada:sampleSequenceDesign": "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "ZrNIST",
  "ada:calibrationMeasurementFrequency": "Every sample \u2014 \"Each sample measurement was individually bracketed\"",
  "ada:reportedProperties": [
    "\u03b49x/90ZrNIST in permil \u2014 \u03b491/90Zr, \u03b492/90Zr, \u03b494/90Zr and \u03b496/90Zr"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Massachusetts Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions",
        "schema:description": "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Single crystal \u2014 \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Mathematica \u2014 \"Data were reduced using a minimization approach implemented in Mathematica\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG-1X for U-Pb; Ln-Spec (~300 \u00b5l, 25\u201350 \u00b5m) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks",
  "ada:isotopeDilutionSpike": "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio",
  "ada:finalSolutionMatrix": "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Zr"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-Tissot2020 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Crushing in a stainless steel mortar, sieving through 375 µm plastic mesh, washing in a plastic gold pan, hand magnet, Frantz LB-1 magnetic separation, methylene iodide heavy liquid, hand picking under high-purity ethanol" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "29 M HF; after conversion to a chloride matrix for U-Pb. Zr aliquots taken up in 3 M HNO3 + 0.5 M HF" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Massachusetts Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — Tissot2020" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Single zircon and baddeleyite crystals, and bulk rock" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: 3 M HCl washes from the U-Pb anion chemistry were collected and became the Zr aliquots, so the same crystal yields a U-Pb date and a Zr isotopic composition. Sequence: U-Pb purification first, Zr purification from its washes" ;
                    schema1:name "ID-TIMS U-Pb on an Isotopx X-62 at MIT, and solution Q-ICP-MS (Agilent 7700) for Zr and Hf concentrations, on aliquots of the same dissolutions" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Zr" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "Every sample — \"Each sample measurement was individually bracketed\"" ;
    ada:chromatographicSeparationApplied "Yes — AG-1X for U-Pb; Ln-Spec (~300 µl, 25–50 µm) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks" ;
    ada:finalSolutionMatrix "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "ZrNIST" ;
    ada:reportedProperties "δ9x/90ZrNIST in permil — δ91/90Zr, δ92/90Zr, δ94/90Zr and δ96/90Zr" ;
    ada:sampleSequenceDesign "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank" ;
    ada:samplingUnit "Single crystal — \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 ;
    bios:computationalTool [ schema1:name "Mathematica — \"Data were reduced using a minimization approach implemented in Mathematica\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "238U/235U = 137.818 (45), 18O/16O = 0.00205 (44), and α = 0.18 ± 0.02%/amu from repeat NBS-981 analyses; U decay constants of (47); Th/U[magma] = 2.8 ± 1.0 for the initial 230Th disequilibrium correction" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Cetac Aridus II — \"Analyses were conducted in dry plasma mode\"" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Zircon 48 hours (U-Pb) and 60 hours (Zr isotopes)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 215 ;
    schema1:description "215 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "\"clean Teflon microcapsules\" inside \"a large-volume Parr digestion vessel\"" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Cetac Aridus II desolvator nebulizer" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "Single crystals; ~50 µl (5% of sample) taken for concentration measurement" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\"" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nu Plasma II" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "Masses 90, 91, 92, 93, 94, 95, 96 and 98 \"measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block\"" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "Double-spike inversion, Rmeas = [p·RSpike + (1−p)·RStd·(Mx/Mn)^α]·(Mx/Mi)^β, solved by weighted minimisation over four ratios" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Dry plasma — \"Analyses were conducted in dry plasma mode using a Cetac Aridus II desolvator nebulizer\"" .


```


### solutionMcicpmsTAPP example Dauphas2019
solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago.
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
  "@id": "ex:solutionMcicpmsTAPP-Dauphas2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — Dauphas2019",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate rocks — geostandards including basalts, granites and peridotites, and the Allende chondrite"
          ]
        },
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
          "schema:description": "~100 mg or less; ~40 ng Rb typical"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
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
            "schema:defaultValue": "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885"
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
            "schema:value": "30 ml fluoropolymer vessel"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": "Three"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Three steps of concentrated HF–HNO3–HCl–HClO4; step (i) \"4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4\"",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Normal sampler and skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "\"a dual cyclonic-Scott-type quartz spray chamber\"; cooling not stated"
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
              "schema:description": "100 µl/min"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "85Rb, 87Rb+87Sr and 88Sr on three collectors, 88Sr on H1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Low resolution"
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash in 0.45 M HNO3"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None — spray chamber introduction"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM984",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende"
  ],
  "ada:reportedProperties": [
    "δ87Rb in permil relative to NIST SRM984"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "ada:samplingUnit": "Digestion aliquot — \"Samples of about 100 mg or less were digested\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A — Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes — five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3, ~15–25 ppb Rb",
  "ada:washTimeBetweenSamples": "60 s wash in 0.45 M HNO3, with a 90 s take-up time",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Rb"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-Dauphas2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 Dauphas2019",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate rocks \u2014 geostandards including basalts, granites and peridotites, and the Allende chondrite"
          ]
        },
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
          "schema:description": "~100 mg or less; ~40 ng Rb typical"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Whole-rock powder",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
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
            "schema:defaultValue": "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885"
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
            "schema:value": "30 ml fluoropolymer vessel"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": "Three"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Three steps of concentrated HF\u2013HNO3\u2013HCl\u2013HClO4; step (i) \"4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4\"",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Normal sampler and skimmer cones"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "Ni"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "\"a dual cyclonic-Scott-type quartz spray chamber\"; cooling not stated"
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
              "schema:description": "100 \u00b5l/min"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "85Rb, 87Rb+87Sr and 88Sr on three collectors, 88Sr on H1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Low resolution"
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "60 s wash in 0.45 M HNO3"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None \u2014 spray chamber introduction"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM984",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende"
  ],
  "ada:reportedProperties": [
    "\u03b487Rb in permil relative to NIST SRM984"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Chicago"
  },
  "ada:samplingUnit": "Digestion aliquot \u2014 \"Samples of about 100 mg or less were digested\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A \u2014 Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes \u2014 five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3, ~15\u201325 ppb Rb",
  "ada:washTimeBetweenSamples": "60 s wash in 0.45 M HNO3, with a 90 s take-up time",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Rb"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-Dauphas2019 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Three steps of concentrated HF–HNO3–HCl–HClO4; step (i) \"4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4\"" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Chicago" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — Dauphas2019" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate rocks — geostandards including basalts, granites and peridotites, and the Allende chondrite" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Rb" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%" ;
    ada:finalSolutionMatrix "0.3 M HNO3, ~15–25 ppb Rb" ;
    ada:internalNormalizationElementAndIsotopeRatio "N/A — Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM984" ;
    ada:reportedProperties "δ87Rb in permil relative to NIST SRM984" ;
    ada:sampleSequenceDesign "Standard-sample bracketing" ;
    ada:samplingUnit "Digestion aliquot — \"Samples of about 100 mg or less were digested\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "60 s wash in 0.45 M HNO3, with a 90 s take-up time" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None — spray chamber introduction" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "30 ml fluoropolymer vessel" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value "Three" ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 mg or less; ~40 ng Rb typical" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "100 µl/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "\"a dual cyclonic-Scott-type quartz spray chamber\"; cooling not stated" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "60 s wash in 0.45 M HNO3" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "85Rb, 87Rb+87Sr and 88Sr on three collectors, 88Sr on H1" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Normal sampler and skimmer cones" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "Low resolution" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "Ni" .


```


### solutionMcicpmsTAPP example P6
solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL.
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
  "@id": "ex:solutionMcicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P6",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Osmium isotope reference material solutions"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 600,
          "schema:description": "Up to 600 ng Os consumed per analysis; ~300 µl of solution"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N/A — reference material solutions, no solid preparation",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — n = 45 per analysis. No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "N/A — reference material solutions in 3 or 5 mol/l Teflon-distilled HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune",
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
              "schema:value": "ESI PFA-50 micro-flow nebuliser"
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
              "schema:value": "Glass Expansion micro-cyclonic \"Cinnabar\" spray chamber; cooling not stated"
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
              "schema:defaultValue": 80,
              "schema:description": "~80 µl/min, free aspiration"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "L4=182W, L3=184Os, L2=185Re, L1=186Os, Ax=187Os, H1=188Os, H2=189Os, H3=190Os, H4=192Os, with 184W, 186W and 187Re as interference monitors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None — \"Although greater sensitivity could be attained using a desolvating nebuliser such systems have been shown to suffer severe memory problems for Os\""
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "UMd, DTM, LOsST and DROsS Os reference materials",
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Arthur Holmes Isotope Geology Laboratory, Durham"
  },
  "ada:samplingUnit": "Reference material solution aliquot — 200 ng/ml to 2.5 µg/ml Os, ~300 µl consumed per analysis",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Microsoft Excel — \"Following analysis all intensity data was exported and re-processed offline using Excel\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "N/A — reference material solutions",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 or 5 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Os"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P6",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Osmium isotope reference material solutions"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 600,
          "schema:description": "Up to 600 ng Os consumed per analysis; ~300 \u00b5l of solution"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N/A \u2014 reference material solutions, no solid preparation",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 n = 45 per analysis. No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "N/A \u2014 reference material solutions in 3 or 5 mol/l Teflon-distilled HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune",
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
              "schema:value": "ESI PFA-50 micro-flow nebuliser"
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
              "schema:value": "Glass Expansion micro-cyclonic \"Cinnabar\" spray chamber; cooling not stated"
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
              "schema:defaultValue": 80,
              "schema:description": "~80 \u00b5l/min, free aspiration"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "L4=182W, L3=184Os, L2=185Re, L1=186Os, Ax=187Os, H1=188Os, H2=189Os, H3=190Os, H4=192Os, with 184W, 186W and 187Re as interference monitors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background \u2014 a 99.99% decrease reached after 220 s for DTM"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None \u2014 \"Although greater sensitivity could be attained using a desolvating nebuliser such systems have been shown to suffer severe memory problems for Os\""
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "UMd, DTM, LOsST and DROsS Os reference materials",
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Arthur Holmes Isotope Geology Laboratory, Durham"
  },
  "ada:samplingUnit": "Reference material solution aliquot \u2014 200 ng/ml to 2.5 \u00b5g/ml Os, ~300 \u00b5l consumed per analysis",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Microsoft Excel \u2014 \"Following analysis all intensity data was exported and re-processed offline using Excel\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "N/A \u2014 reference material solutions",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 or 5 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Os"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:solutionMcicpmsTAPP-P6 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A — reference material solutions, no solid preparation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N/A — reference material solutions in 3 or 5 mol/l Teflon-distilled HCl" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Arthur Holmes Isotope Geology Laboratory, Durham" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P6" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Osmium isotope reference material solutions" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Os" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "N/A — reference material solutions" ;
    ada:finalSolutionMatrix "3 or 5 mol/l Teflon-distilled HCl" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "UMd, DTM, LOsST and DROsS Os reference materials" ;
    ada:reportedProperties "187Os/188Os, 186Os/188Os and 184Os/188Os ratios" ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Reference material solution aliquot — 200 ng/ml to 2.5 µg/ml Os, ~300 µl consumed per analysis" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions" ;
    bios:computationalTool [ schema1:name "Microsoft Excel — \"Following analysis all intensity data was exported and re-processed offline using Excel\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — n = 45 per analysis. No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None — \"Although greater sensitivity could be attained using a desolvating nebuliser such systems have been shown to suffer severe memory problems for Os\"" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "ESI PFA-50 micro-flow nebuliser" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 600 ;
    schema1:description "Up to 600 ng Os consumed per analysis; ~300 µl of solution" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 80 ;
    schema1:description "~80 µl/min, free aspiration" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Glass Expansion micro-cyclonic \"Cinnabar\" spray chamber; cooling not stated" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "L4=182W, L3=184Os, L2=185Re, L1=186Os, Ax=187Os, H1=188Os, H2=189Os, H3=190Os, H4=192Os, with 184W, 186W and 187Re as interference monitors" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .


```


### solutionMcicpmsTAPP example P7
solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL.
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
  "@id": "ex:solutionMcicpmsTAPP-P7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P7",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Osmium isotope reference material solutions"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 6400,
          "schema:description": "~6400 µl of solution per analysis"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N/A — reference material solutions, no solid preparation",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — n = 50 per analysis. No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "N/A — reference material solutions in Teflon-distilled 3 mol/l HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Plasma",
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
              "schema:value": "ESI PFA-50 low uptake nebuliser"
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
              "schema:value": "GE Cinnabar micro-cyclonic spray chamber"
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
              "schema:defaultValue": 6400,
              "schema:description": "Not stated; ~6400 µl consumed over a ~16 min analysis"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Two-sequence static multi-collection",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "DTM and LOsST",
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NERC Isotope Geosciences Laboratory (NIGL)"
  },
  "ada:samplingUnit": "Reference material solution aliquot — ~6400 µl consumed per analysis",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Online processing on the instrument — \"Samples were processed on-line for W and Re interferences and instrumental mass bias\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "N/A — reference material solutions",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Os"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P7",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Osmium isotope reference material solutions"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 6400,
          "schema:description": "~6400 \u00b5l of solution per analysis"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N/A \u2014 reference material solutions, no solid preparation",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 n = 50 per analysis. No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "N/A \u2014 reference material solutions in Teflon-distilled 3 mol/l HCl",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Nu Plasma",
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
              "schema:value": "ESI PFA-50 low uptake nebuliser"
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
              "schema:value": "GE Cinnabar micro-cyclonic spray chamber"
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
              "schema:defaultValue": 6400,
              "schema:description": "Not stated; ~6400 \u00b5l consumed over a ~16 min analysis"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Two-sequence static multi-collection",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "None"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "DTM and LOsST",
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NERC Isotope Geosciences Laboratory (NIGL)"
  },
  "ada:samplingUnit": "Reference material solution aliquot \u2014 ~6400 \u00b5l consumed per analysis",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Online processing on the instrument \u2014 \"Samples were processed on-line for W and Re interferences and instrumental mass bias\""
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "N/A \u2014 reference material solutions",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Os"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleSequenceDesign": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:solutionMcicpmsTAPP-P7 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N/A — reference material solutions in Teflon-distilled 3 mol/l HCl" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A — reference material solutions, no solid preparation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NERC Isotope Geosciences Laboratory (NIGL)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P7" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Osmium isotope reference material solutions" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Os" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "N/A — reference material solutions" ;
    ada:finalSolutionMatrix "3 mol/l Teflon-distilled HCl" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "DTM and LOsST" ;
    ada:reportedProperties "187Os/188Os, 186Os/188Os and 184Os/188Os ratios" ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "Reference material solution aliquot — ~6400 µl consumed per analysis" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels" ;
    bios:computationalTool [ schema1:name "Online processing on the instrument — \"Samples were processed on-line for W and Re interferences and instrumental mass bias\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — n = 50 per analysis. No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "None" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "ESI PFA-50 low uptake nebuliser" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6400 ;
    schema1:description "~6400 µl of solution per analysis" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6400 ;
    schema1:description "Not stated; ~6400 µl consumed over a ~16 min analysis" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "GE Cinnabar micro-cyclonic spray chamber" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nu Plasma" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "Two-sequence static multi-collection" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .


```


### solutionMcicpmsTAPP example Moynier2017
solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP.
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
  "@id": "ex:solutionMcicpmsTAPP-Moynier2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — Moynier2017",
  "schema:description": "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Whole-rock terrestrial igneous rocks, chondrites, achondrites and Apollo lunar samples"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 125,
          "schema:description": "<=125 mg powder, calculated to yield >20 ng Rb"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "\"any ratio outside 2σ was discarded\" — an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\""
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
            "schema:value": "\"closed Teflon bombs\""
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
            "schema:defaultValue": 130,
            "schema:description": "130 °C for both the HF/HNO3 and the 6N HCl steps"
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
            "schema:defaultValue": "\">48 h\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"a mixture of concentrated HF/HNO3\"; after evaporation \"6N HCl was added\" to dissolve fluoride complexes",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Sample cone Jet; skimmer cone H"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "Peristaltic pump at 5 rpm"
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
              "schema:defaultValue": 1.03,
              "schema:description": "1.03 L/min (sample gas)"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "16 L/min"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.01,
              "schema:description": "1.01 L/min"
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
          "schema:description": "L2=84Sr, L1=85Rb, C=86Sr, H1=87Rb+87Sr, H2=88Sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "APEX, used alongside the spray chamber as an alternative introduction system in different sessions"
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
      "schema:value": "N/A — no added internal standard element"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "spikeOutlierFilteringApproachDefault",
      "schema:name": "Spike / Outlier Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"any ratio outside 2σ was discarded\""
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"Errors are determined from repeated measurements\""
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks"
  ],
  "ada:reportedProperties": [
    "δ87Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard − 1] x 1000"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut de Physique du Globe de Paris"
  },
  "ada:samplingUnit": "Weighed powder aliquot — \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A — Rb has two stable isotopes; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes — DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.1N HNO3",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Rb"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-Moynier2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 Moynier2017",
  "schema:description": "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Whole-rock terrestrial igneous rocks, chondrites, achondrites and Apollo lunar samples"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 125,
          "schema:description": "<=125 mg powder, calculated to yield >20 ng Rb"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "\"any ratio outside 2\u03c3 was discarded\" \u2014 an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\""
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
            "schema:value": "\"closed Teflon bombs\""
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
            "schema:defaultValue": 130,
            "schema:description": "130 \u00b0C for both the HF/HNO3 and the 6N HCl steps"
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
            "schema:defaultValue": "\">48 h\""
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"a mixture of concentrated HF/HNO3\"; after evaporation \"6N HCl was added\" to dissolve fluoride complexes",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Sample cone Jet; skimmer cone H"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 5,
              "schema:description": "Peristaltic pump at 5 rpm"
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
              "schema:defaultValue": 1.03,
              "schema:description": "1.03 L/min (sample gas)"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "16 L/min"
            },
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1.01,
              "schema:description": "1.01 L/min"
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
          "schema:description": "L2=84Sr, L1=85Rb, C=86Sr, H1=87Rb+87Sr, H2=88Sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "APEX, used alongside the spray chamber as an alternative introduction system in different sessions"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "spikeOutlierFilteringApproachDefault",
      "schema:name": "Spike / Outlier Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"any ratio outside 2\u03c3 was discarded\""
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"Errors are determined from repeated measurements\""
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks"
  ],
  "ada:reportedProperties": [
    "\u03b487Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard \u2212 1] x 1000"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institut de Physique du Globe de Paris"
  },
  "ada:samplingUnit": "Weighed powder aliquot \u2014 \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A \u2014 Rb has two stable isotopes; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes \u2014 DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.1N HNO3",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Rb"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-Moynier2017 a cdi:Activity,
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
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"a mixture of concentrated HF/HNO3\"; after evaporation \"6N HCl was added\" to dissolve fluoride complexes" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institut de Physique du Globe de Paris" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — Moynier2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Whole-rock terrestrial igneous rocks, chondrites, achondrites and Apollo lunar samples" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Rb" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"" ;
    ada:chromatographicSeparationApplied "Yes — DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005" ;
    ada:finalSolutionMatrix "0.1N HNO3" ;
    ada:internalNormalizationElementAndIsotopeRatio "N/A — Rb has two stable isotopes; bracketing used instead" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions" ;
    ada:reportedProperties "δ87Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard − 1] x 1000" ;
    ada:sampleSequenceDesign "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"" ;
    ada:samplingUnit "Weighed powder aliquot — \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"" ;
    ada:secondaryReferenceMaterialDefault "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"any ratio outside 2σ was discarded\" — an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\"" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "APEX, used alongside the spray chamber as an alternative introduction system in different sessions" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\">48 h\"" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 130 ;
    schema1:description "130 °C for both the HF/HNO3 and the 6N HCl steps" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "\"closed Teflon bombs\"" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.03e+00 ;
    schema1:description "1.03 L/min (sample gas)" ;
    schema1:name "Nebulizer Gas Flow Rate" ;
    schema1:valueName "nebulizerGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 125 ;
    schema1:description "<=125 mg powder, calculated to yield >20 ng Rb" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "Peristaltic pump at 5 rpm" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.01e+00 ;
    schema1:description "1.01 L/min" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "16 L/min" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"any ratio outside 2σ was discarded\"" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"Errors are determined from repeated measurements\"" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "L2=84Sr, L1=85Rb, C=86Sr, H1=87Rb+87Sr, H2=88Sr" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Sample cone Jet; skimmer cone H" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .


```


### solutionMcicpmsTAPP example P9
solutionMcicpmsTAPP instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich.
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
  "@id": "ex:solutionMcicpmsTAPP-P9",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P9",
  "schema:description": "solutionMcicpmsTAPP instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Ryugu returned samples, carbonaceous chondrites, eucrites and terrestrial rock reference materials"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 25,
          "schema:description": "Ryugu <25 mg with ~40–70 ng Zr; 15 ng Zr consumed per 30 ppb analysis"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Homogenised powder — Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — n stated per reference material (n = 13–99 for terrestrial RMs over 10 months; n = 17–38 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated"
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
            "schema:defaultValue": "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)"
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
            "schema:value": "Octagonal-body Savillex vials; Parr bomb (Ivuna PB, BCR-2, AGV-1); hotplate (BHVO-2)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 3,
            "schema:description": "Ivuna high PT: two (HF-HNO3 then HCl)"
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
            "schema:defaultValue": 180,
            "schema:description": "180 °C (hotplate), 120 °C (HNO3-HCl), 220 °C (Savillex, Tagish Lake and Tarda), 170 °C (Parr bomb, Ivuna PB), 160 °C (Ivuna high PT)"
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
            "schema:defaultValue": "3–7 days (hotplate), 12 h (HNO3-HCl), \"about a week\" (Tagish Lake and Tarda), 3 days + 2 days (Ivuna high PT)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Concentrated HF-HNO3, then a HNO3-HCl mixture, then a HNO3-H2O2 mixture; Ivuna high PT: concentrated HF-HNO3 for 3 days then concentrated HCl for 2 days",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "\"Normal skimmer and sampler cones were utilized\""
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
              "schema:value": "PFA nebulizer with an Aridus II desolvating nebulizer system"
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
              "schema:defaultValue": 0.05,
              "schema:description": "~0.05 mL/min"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "90Zr–96Zr and 95Mo on 10^11 Ω cups; 99Ru and 101Ru on 10^12 Ω cups",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Aridus II"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:oxideProductionMethodAndThreshold": "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "NIST SRM 3169",
  "ada:calibrationMeasurementFrequency": "Each session — \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony"
  ],
  "ada:reportedProperties": [
    "ε91Zr, ε92Zr and ε96Zr relative to NIST SRM 3169"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\""
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Digestion aliquot — Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)",
  "ada:chromatographicSeparationApplied": "Yes — four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Zr"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P9",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P9",
  "schema:description": "solutionMcicpmsTAPP instance derived from Sch\u00f6nb\u00e4chler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Ryugu returned samples, carbonaceous chondrites, eucrites and terrestrial rock reference materials"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 25,
          "schema:description": "Ryugu <25 mg with ~40\u201370 ng Zr; 15 ng Zr consumed per 30 ppb analysis"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Homogenised powder \u2014 Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 n stated per reference material (n = 13\u201399 for terrestrial RMs over 10 months; n = 17\u201338 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated"
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
            "schema:defaultValue": "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)"
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
            "schema:value": "Octagonal-body Savillex vials; Parr bomb (Ivuna PB, BCR-2, AGV-1); hotplate (BHVO-2)"
          },
          {
            "@id": "ada:parameter/module/SolutionIntroduction/numberOfDigestionSteps",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "numberOfDigestionSteps",
            "schema:name": "Number of Digestion Steps",
            "ada:dataType": "integer",
            "ada:fieldScope": "session",
            "schema:value": 3,
            "schema:description": "Ivuna high PT: two (HF-HNO3 then HCl)"
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
            "schema:defaultValue": 180,
            "schema:description": "180 \u00b0C (hotplate), 120 \u00b0C (HNO3-HCl), 220 \u00b0C (Savillex, Tagish Lake and Tarda), 170 \u00b0C (Parr bomb, Ivuna PB), 160 \u00b0C (Ivuna high PT)"
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
            "schema:defaultValue": "3\u20137 days (hotplate), 12 h (HNO3-HCl), \"about a week\" (Tagish Lake and Tarda), 3 days + 2 days (Ivuna high PT)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Concentrated HF-HNO3, then a HNO3-HCl mixture, then a HNO3-H2O2 mixture; Ivuna high PT: concentrated HF-HNO3 for 3 days then concentrated HCl for 2 days",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "\"Normal skimmer and sampler cones were utilized\""
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
              "schema:value": "PFA nebulizer with an Aridus II desolvating nebulizer system"
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
              "schema:defaultValue": 0.05,
              "schema:description": "~0.05 mL/min"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "90Zr\u201396Zr and 95Mo on 10^11 \u03a9 cups; 99Ru and 101Ru on 10^12 \u03a9 cups",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Aridus II"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:oxideProductionMethodAndThreshold": "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated",
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "NIST SRM 3169",
  "ada:calibrationMeasurementFrequency": "Each session \u2014 \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony"
  ],
  "ada:reportedProperties": [
    "\u03b591Zr, \u03b592Zr and \u03b596Zr relative to NIST SRM 3169"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\""
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Digestion aliquot \u2014 Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)",
  "ada:chromatographicSeparationApplied": "Yes \u2014 four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Zr"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P9 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Concentrated HF-HNO3, then a HNO3-HCl mixture, then a HNO3-H2O2 mixture; Ivuna high PT: concentrated HF-HNO3 for 3 days then concentrated HCl for 2 days" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Homogenised powder — Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ETH Zurich; sample digestion and separation at Tokyo Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P9" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Ryugu returned samples, carbonaceous chondrites, eucrites and terrestrial rock reference materials" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Mg, K, Ca, Ti, Cr, Fe, Cu, Zn, Mo and Nd isotope data \"all obtained from the same sample digestions and are therefore directly comparable\"" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Zr" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "Each session — \"The Zr standard material NIST SRM 3169 was analyzed in each session\"" ;
    ada:chromatographicSeparationApplied "Yes — four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples" ;
    ada:finalSolutionMatrix "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)" ;
    ada:internalNormalizationElementAndIsotopeRatio "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated" ;
    ada:primaryStandardNameDefault "NIST SRM 3169" ;
    ada:reportedProperties "ε91Zr, ε92Zr and ε96Zr relative to NIST SRM 3169" ;
    ada:sampleSequenceDesign "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"" ;
    ada:samplingUnit "Digestion aliquot — Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — n stated per reference material (n = 13–99 for terrestrial RMs over 10 months; n = 17–38 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "94Zr/90Zr = 0.3381 and 91Zr/90Zr = 0.21798, both Minster & Ricard (1981)" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Aridus II" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3–7 days (hotplate), 12 h (HNO3-HCl), \"about a week\" (Tagish Lake and Tarda), 3 days + 2 days (Ivuna high PT)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 180 ;
    schema1:description "180 °C (hotplate), 120 °C (HNO3-HCl), 220 °C (Savillex, Tagish Lake and Tarda), 170 °C (Parr bomb, Ivuna PB), 160 °C (Ivuna high PT)" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "Octagonal-body Savillex vials; Parr bomb (Ivuna PB, BCR-2, AGV-1); hotplate (BHVO-2)" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "PFA nebulizer with an Aridus II desolvating nebulizer system" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/numberOfDigestionSteps> a schema1:PropertyValueSpecification ;
    schema1:description "Ivuna high PT: two (HF-HNO3 then HCl)" ;
    schema1:name "Number of Digestion Steps" ;
    schema1:value 3 ;
    schema1:valueName "numberOfDigestionSteps" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 25 ;
    schema1:description "Ryugu <25 mg with ~40–70 ng Zr; 15 ng Zr consumed per 30 ppb analysis" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5e-02 ;
    schema1:description "~0.05 mL/min" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "90Zr–96Zr and 95Mo on 10^11 Ω cups; 99Ru and 101Ru on 10^12 Ω cups" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "\"Normal skimmer and sampler cones were utilized\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .


```


### solutionMcicpmsTAPP example P10
solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen.
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
  "@id": "ex:solutionMcicpmsTAPP-P10",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P10",
  "schema:description": "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bulk chondrite powders"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk powder; for the Si aliquot, NaOH fusion in silver crucibles",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 °C for the 10 M HCl Cr(VI) speciation step; 720 °C for the NaOH fusion"
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
            "schema:defaultValue": "3 h (Cr(VI) speciation), >1 week at room temperature (Cr(III) speciation), 13 min (NaOH fusion)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Cr/Mg route: 6 M HCl loading, 10 M HCl pretreatment, 0.5 M HCl, 0.5 M HNO3, 1 M HF, 6 M HCl elutions; Si route: NaOH fusion then Milli-Q water and HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neoma",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "A Jet and X cone"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 30,
              "schema:description": "30 µl/min for Cr and for Mg"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": "Stated qualitatively — measured \"at low radiofrequency power and sample gas inflow\" to reduce gas-based interferences"
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
          "schema:description": "49Ti, 51V, 56Fe alongside 50Cr, 52Cr, 53Cr, 54Cr; 24Mg, 25Mg, 26Mg",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium resolution, M/ΔM > 6,000"
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": "None — \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\""
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "ESI Apex HF with an actively cooled membrane unit (Cr); ESI Apex Omega (Mg)"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "IRMM-014, SRM979, DTS-2b",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO2 and DTS-2b, \"processed alongside the samples\""
  ],
  "ada:reportedProperties": [
    "µ-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Fraction of a bulk digestion — \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Fe",
      "Cr and Mg"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P10",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P10",
  "schema:description": "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bulk chondrite powders"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk powder; for the Si aliquot, NaOH fusion in silver crucibles",
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 130,
            "schema:description": "130 \u00b0C for the 10 M HCl Cr(VI) speciation step; 720 \u00b0C for the NaOH fusion"
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
            "schema:defaultValue": "3 h (Cr(VI) speciation), >1 week at room temperature (Cr(III) speciation), 13 min (NaOH fusion)"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "Cr/Mg route: 6 M HCl loading, 10 M HCl pretreatment, 0.5 M HCl, 0.5 M HNO3, 1 M HF, 6 M HCl elutions; Si route: NaOH fusion then Milli-Q water and HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neoma",
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "A Jet and X cone"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sampleUptakeRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sampleUptakeRateDefault",
              "schema:name": "Sample Uptake Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 30,
              "schema:description": "30 \u00b5l/min for Cr and for Mg"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": "Stated qualitatively \u2014 measured \"at low radiofrequency power and sample gas inflow\" to reduce gas-based interferences"
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
          "schema:description": "49Ti, 51V, 56Fe alongside 50Cr, 52Cr, 53Cr, 54Cr; 24Mg, 25Mg, 26Mg",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium resolution, M/\u0394M > 6,000"
        },
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "makeUpGasAndFlowRateDefault",
          "schema:name": "Make-up Gas and Flow Rate",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": "None \u2014 \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\""
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "ESI Apex HF with an actively cooled membrane unit (Cr); ESI Apex Omega (Mg)"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:blankBackgroundCorrectionMethod": "N/A",
  "ada:primaryStandardNameDefault": "IRMM-014, SRM979, DTS-2b",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO2 and DTS-2b, \"processed alongside the samples\""
  ],
  "ada:reportedProperties": [
    "\u00b5-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Fraction of a bulk digestion \u2014 \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Fe",
      "Cr and Mg"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P10 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Bulk powder; for the Si aliquot, NaOH fusion in silver crucibles" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Cr/Mg route: 6 M HCl loading, 10 M HCl pretreatment, 0.5 M HCl, 0.5 M HNO3, 1 M HF, 6 M HCl elutions; Si route: NaOH fusion then Milli-Q water and HNO3" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Centre for Star and Planet Formation, Globe Institute, University of Copenhagen" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P10" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bulk chondrite powders" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "ICP-MS for Sr and Rb weathering assessment; Si isotopes on a separate NaOH-fusion aliquot" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Cr and Mg",
                "Fe" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "N/A" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg" ;
    ada:finalSolutionMatrix "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "IRMM-014, SRM979, DTS-2b" ;
    ada:reportedProperties "µ-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b" ;
    ada:sampleSequenceDesign "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value" ;
    ada:samplingUnit "Fraction of a bulk digestion — \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO2 and DTS-2b, \"processed alongside the samples\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "ESI Apex HF with an actively cooled membrane unit (Cr); ESI Apex Omega (Mg)" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3 h (Cr(VI) speciation), >1 week at room temperature (Cr(III) speciation), 13 min (NaOH fusion)" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 130 ;
    schema1:description "130 °C for the 10 M HCl Cr(VI) speciation step; 720 °C for the NaOH fusion" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 30 ;
    schema1:description "30 µl/min for Cr and for Mg" ;
    schema1:name "Sample Uptake Rate" ;
    schema1:valueName "sampleUptakeRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None — \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\"" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Stated qualitatively — measured \"at low radiofrequency power and sample gas inflow\" to reduce gas-based interferences" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neoma" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "49Ti, 51V, 56Fe alongside 50Cr, 52Cr, 53Cr, 54Cr; 24Mg, 25Mg, 26Mg" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleUptakeRateDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "A Jet and X cone" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "Medium resolution, M/ΔM > 6,000" .


```


### solutionMcicpmsTAPP example P11
solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL.
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
  "@id": "ex:solutionMcicpmsTAPP-P11",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P11",
  "schema:description": "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "CI chondrite Oued Chebeika 002 and geostandard"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
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
            "schema:description": "70 °C for the HCl step; 140 °C for the HF/HNO3 mixture"
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
            "schema:defaultValue": "20 h for the HF/HNO3 step"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Measured \"on the left 'shoulder' of the peak to resolve the difference between 40Ar1H+ and 41K+\""
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
              "schema:value": "Elemental Scientific APEX Omega desolvating nebulizer"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Elemental Scientific APEX Omega"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM 3141a",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing)",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:reportedProperties": [
    "δ41K in permil relative to NIST SRM 3141a"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS",
        "schema:description": "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — twice through 1.5 mL Bio-Rad AG50W-X8 100–200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "300 ppb K solution",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "K"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P11",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P11",
  "schema:description": "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "CI chondrite Oued Chebeika 002 and geostandard"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "analysisInclusionAndRejectionCriteriaDefault",
            "schema:name": "Analysis Inclusion and Rejection Criteria",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Partially \u2014 \"Each sample was measured approximately 20 times\". No rejection rule stated"
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
      },
      {
        "schema:name": "Sample digestion",
        "schema:additionalProperty": [
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
            "schema:description": "70 \u00b0C for the HCl step; 140 \u00b0C for the HF/HNO3 mixture"
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
            "schema:defaultValue": "20 h for the HF/HNO3 step"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Measured \"on the left 'shoulder' of the peak to resolve the difference between 40Ar1H+ and 41K+\""
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
              "schema:value": "Elemental Scientific APEX Omega desolvating nebulizer"
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
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Torch"
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Elemental Scientific APEX Omega"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "NIST SRM 3141a",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing)",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:reportedProperties": [
    "\u03b441K in permil relative to NIST SRM 3141a"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS",
        "schema:description": "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 twice through 1.5 mL Bio-Rad AG50W-X8 100\u2013200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "300 ppb K solution",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "K"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:samplingUnit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P11 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P11" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "CI chondrite Oued Chebeika 002 and geostandard" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Functional: pre-cut and post-cut fractions either side of the K collection were measured by Q-ICP-MS \"to monitor for K loss during column chemistry\". Sequence: Q-ICP-MS check before MC-ICP-MS measurement" ;
                    schema1:name "Laser-fluorination oxygen isotopes on a Thermo Finnigan MAT 253 Plus; K loss monitored by Thermo Fisher iCAP Q ICP-MS" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "K" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample (bracketing)" ;
    ada:chromatographicSeparationApplied "Yes — twice through 1.5 mL Bio-Rad AG50W-X8 100–200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3" ;
    ada:finalSolutionMatrix "300 ppb K solution" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM 3141a" ;
    ada:reportedProperties "δ41K in permil relative to NIST SRM 3141a" ;
    ada:sampleSequenceDesign "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Elemental Scientific APEX Omega" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "20 h for the HF/HNO3 step" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 70 ;
    schema1:description "70 °C for the HCl step; 140 °C for the HF/HNO3 mixture" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> a schema1:PropertyValueSpecification ;
    schema1:name "Nebulizer Type" ;
    schema1:value "Elemental Scientific APEX Omega desolvating nebulizer" ;
    schema1:valueName "nebulizerType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch>,
        <https://example.org/instrument/part/Collector> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:name "Collector" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "Measured \"on the left 'shoulder' of the peak to resolve the difference between 40Ar1H+ and 41K+\"" .


```


### solutionMcicpmsTAPP example P12
solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL.
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
  "@id": "ex:solutionMcicpmsTAPP-P12",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P12",
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bennu returned sample aggregate"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
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
            "schema:value": "\"in a closed beaker\""
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
            "schema:defaultValue": 170,
            "schema:description": "170 °C"
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
            "schema:defaultValue": "48 h"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"concentrated HF and HNO3 in a 3:1 ratio\", followed by fluxing in concentrated HNO3 and HCl with 1 ml H2O2 added to remove organics; brought up in 5 ml 0.5 M HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "High-mass-resolution slit for K; low-mass-resolution slit for Cu and Zn"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Quartz glass dual cyclonic spray chamber for Cu and Zn; cooling not stated"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Dry plasma for K — \"all K isotope analyses were undertaken using a 'dry plasma' technique with the Elemental Scientific APEX Ω high-sensitivity desolvation system\"; wet plasma for Cu and Zn via a quartz glass dual cyclonic spray chamber"
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
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Elemental Scientific APEX Ω for K (\"dry plasma technique\"); none for Cu and Zn"
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
      "schema:value": "N/A — no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:reportedProperties": [
    "δ41K, δ65Cu and δ66Zn in permil, each defined explicitly against its bracketing standard"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Split of a single digest — \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 200–400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "200 ppb for K and Zn; 100 ppb for Cu",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "K",
      "Cu and Zn"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P12",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P12",
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bennu returned sample aggregate"
          ]
        }
      ]
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
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
            "schema:value": "\"in a closed beaker\""
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
            "schema:defaultValue": 170,
            "schema:description": "170 \u00b0C"
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
            "schema:defaultValue": "48 h"
          }
        ],
        "bios:reagent": [
          {
            "schema:name": "\"concentrated HF and HNO3 in a 3:1 ratio\", followed by fluxing in concentrated HNO3 and HCl with 1 ml H2O2 added to remove organics; brought up in 5 ml 0.5 M HNO3",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "High-mass-resolution slit for K; low-mass-resolution slit for Cu and Zn"
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
              "@id": "ada:parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "sprayChamberTypeAndCoolingTemperature",
              "schema:name": "Spray Chamber Type and Cooling Temperature",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Quartz glass dual cyclonic spray chamber for Cu and Zn; cooling not stated"
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
              "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Dry plasma for K \u2014 \"all K isotope analyses were undertaken using a 'dry plasma' technique with the Elemental Scientific APEX \u03a9 high-sensitivity desolvation system\"; wet plasma for Cu and Zn via a quartz glass dual cyclonic spray chamber"
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
        },
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "Collector",
          "@id": "ex:instrument/part/Collector"
        }
      ],
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
      "@id": "ada:parameter/module/SolutionIntroduction/desolvationSystem",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "desolvationSystem",
      "schema:name": "Desolvation System",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Elemental Scientific APEX \u03a9 for K (\"dry plasma technique\"); none for Cu and Zn"
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
      "schema:value": "N/A \u2014 no added internal standard element"
    }
  ],
  "ada:sampleSequenceDesign": "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:perAnalyteCalibrationStrategy": [
    "N/A"
  ],
  "ada:primaryStandardNameDefault": "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:reportedProperties": [
    "\u03b441K, \u03b465Cu and \u03b466Zn in permil, each defined explicitly against its bracketing standard"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Split of a single digest \u2014 \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 200\u2013400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "200 ppb for K and Zn; 100 ppb for Cu",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "K",
      "Cu and Zn"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P12 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"concentrated HF and HNO3 in a 3:1 ratio\", followed by fluxing in concentrated HNO3 and HCl with 1 ml H2O2 added to remove organics; brought up in 5 ml 0.5 M HNO3" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P12" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bennu returned sample aggregate" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "High-resolution ICP-MS (Thermo Element XR) at LLNL for bulk elemental abundances, on splits of the same digest" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Cu and Zn",
                "K" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 200–400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn" ;
    ada:finalSolutionMatrix "200 ppb for K and Zn; 100 ppb for Cu" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:perAnalyteCalibrationStrategy "N/A" ;
    ada:primaryStandardNameDefault "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon" ;
    ada:reportedProperties "δ41K, δ65Cu and δ66Zn in permil, each defined explicitly against its bracketing standard" ;
    ada:sampleSequenceDesign "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"" ;
    ada:samplingUnit "Split of a single digest — \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Elemental Scientific APEX Ω for K (\"dry plasma technique\"); none for Cu and Zn" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "48 h" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 170 ;
    schema1:description "170 °C" ;
    schema1:name "Digestion Temperature" ;
    schema1:valueName "digestionTemperatureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> a schema1:PropertyValueSpecification ;
    schema1:name "Digestion Vessel Type" ;
    schema1:value "\"in a closed beaker\"" ;
    schema1:valueName "digestionVesselType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> a schema1:PropertyValueSpecification ;
    schema1:name "Spray Chamber Type and Cooling Temperature" ;
    schema1:value "Quartz glass dual cyclonic spray chamber for Cu and Zn; cooling not stated" ;
    schema1:valueName "sprayChamberTypeAndCoolingTemperature" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch>,
        <https://example.org/instrument/part/Collector> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sprayChamberTypeAndCoolingTemperature> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:name "Collector" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "High-mass-resolution slit for K; low-mass-resolution slit for Cu and Zn" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/plasmaThermalMode> ;
    schema1:value "Dry plasma for K — \"all K isotope analyses were undertaken using a 'dry plasma' technique with the Elemental Scientific APEX Ω high-sensitivity desolvation system\"; wet plasma for Cu and Zn via a quartz glass dual cyclonic spray chamber" .


```


### solutionMcicpmsTAPP example P13
solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich.
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
  "@id": "ex:solutionMcicpmsTAPP-P13",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol — P13",
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bennu returned sample aggregate"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 5.2,
          "schema:description": "5.2 mg"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium mass resolution, R ≈ 6,600–7,000 (R = m/m0.95 − m0.05)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "\"Titanium isotopes were collected in two cup configurations\"",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
      "schema:value": "N/A — no added internal standard element"
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A — no isotope dilution applied"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Coordinated dissolution shared with the WUSTL split — see the WUSTL column",
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
  "ada:reportedProperties": [
    "ε50Ti"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geochemistry and Petrology, ETH Zurich"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "A 5.2 mg aliquot of Bennu aggregate",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — three-step anion exchange chromatography; yields 75–100%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Ti"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:solutionMcicpmsTAPP-P13",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P13",
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv).",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Bennu returned sample aggregate"
          ]
        },
        {
          "@id": "ada:parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleAliquotMassOrVolumeDefault",
          "schema:name": "Sample Aliquot Mass or Volume",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 5.2,
          "schema:description": "5.2 mg"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Multi-collector sector-field ICP-MS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Neptune Plus",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/solutionMcicpmsTAPP/massResolutionSetting"
            }
          ],
          "schema:name": "Mass Resolution Setting",
          "schema:value": "Medium mass resolution, R \u2248 6,600\u20137,000 (R = m/m0.95 \u2212 m0.05)"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "\"Titanium isotopes were collected in two cup configurations\"",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:name": "missing"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
      "schema:value": "N/A \u2014 no added internal standard element"
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
            "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod"
              }
            ],
            "schema:name": "Isotope Dilution Data Reduction Method",
            "schema:value": "N/A \u2014 no isotope dilution applied"
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
      },
      {
        "schema:name": "Sample digestion",
        "bios:reagent": [
          {
            "schema:name": "Coordinated dissolution shared with the WUSTL split \u2014 see the WUSTL column",
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
  "ada:reportedProperties": [
    "\u03b550Ti"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Solution MC-ICP-MS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geochemistry and Petrology, ETH Zurich"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "A 5.2 mg aliquot of Bennu aggregate",
  "ada:analyticalMode": [
    "Solution nebulisation (continuous)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 three-step anion exchange chromatography; yields 75\u2013100%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Ti"
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
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:sampleSequenceDesign": "missing",
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:solutionMcicpmsTAPP-P13 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Coordinated dissolution shared with the WUSTL split — see the WUSTL column" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geochemistry and Petrology, ETH Zurich" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Solution MC-ICP-MS" ] ;
    schema1:name "solutionMcicpms protocol — P13" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bennu returned sample aggregate" ],
                <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Coordinated dissolution shared with the WUSTL K/Cu/Zn procedure; SIMS oxygen isotopes" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> ;
            ada:defaultAnalytes "Ti" ] ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:chromatographicSeparationApplied "Yes — three-step anion exchange chromatography; yields 75–100%" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedProperties "ε50Ti" ;
    ada:sampleSequenceDesign "missing" ;
    ada:samplingUnit "A 5.2 mg aliquot of Bennu aggregate" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> a schema1:PropertyValueSpecification ;
    schema1:name "Internal Standard Concentration" ;
    schema1:value "N/A — no added internal standard element" ;
    schema1:valueName "internalStandardConcentration" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/sampleAliquotMassOrVolumeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5.2e+00 ;
    schema1:description "5.2 mg" ;
    schema1:name "Sample Aliquot Mass or Volume" ;
    schema1:valueName "sampleAliquotMassOrVolumeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "\"Titanium isotopes were collected in two cup configurations\"" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Sample-Introduction-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> a schema1:PropertyValue ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod> ;
    schema1:value "N/A — no isotope dilution applied" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/massResolutionSetting> ;
    schema1:value "Medium mass resolution, R ≈ 6,600–7,000 (R = m/m0.95 − m0.05)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution MC-ICP-MS Technique-Aligned Procedure Profile (solutionMcicpmsTAPP)
description: Solution multi-collector ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/Solution_MC-ICP-MS_TAPP_v30.csv via the path-driven
  pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- type: object
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
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:name:
                          const: Target Material
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:value:
                          type: array
                          items:
                            description: General description of the material type(s)
                              this procedure is designed to analyse. Used for discoverability
                              and procedure matching, and because the material type
                              constrains sample preparation, calibration and matrix-matching
                              requirements.
                            anyOf:
                            - type: string
                              enum:
                              - Basalt
                              - Chondrite
                              - Seawater
                              - Mineral separate
                              - Synthetic solution
                              - N/A
                              - None
                              - missing
                            - type: string
                            readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Target Material
                    required:
                    - schema:name
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_sampleAliquotMassOrVolume
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
                    const: Sample preparation
                required:
                - schema:name
              then:
                properties:
                  schema:description:
                    description: General approach to mechanical sample preparation
                      prior to dissolution (e.g., whole-rock crushing and powdering,
                      mineral separation). Documents how the solid material was conditioned
                      before acid digestion.
                    anyOf:
                    - type: string
                      readOnly: true
                    - type: array
                      items:
                        type: string
                        readOnly: true
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_numberOfDigestionSteps
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionTemperature
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionDuration
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_digestionVesselType
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_numberOfDigestionSteps
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
                      description: Whether a guard electrode (grounded shield electrode)
                        is installed and active on the torch assembly. Capacitively
                        decouples the plasma from the load coil, reducing secondary
                        discharge and improving ion extraction efficiency.
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/solutionMcicpmsTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/solutionMcicpmsTAPP/guardElectrode
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
                        description: Whether a guard electrode (grounded shield electrode)
                          is installed and active on the torch assembly. Capacitively
                          decouples the plasma from the load coil, reducing secondary
                          discharge and improving ion extraction efficiency.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionMcicpmsTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionMcicpmsTAPP/guardElectrode
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
                      - title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          isotope ratios and/or elemental concentrations from spike-sample
                          mixture measurements. For double-spike procedures, isotope
                          ratios and concentrations are co-determined through the
                          spike inversion. For conventional ID concentration procedures
                          (separate concentration spike), IUPAC ID equations are used.
                          Record 'None' if neither isotope dilution nor double-spike
                          methods are used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod
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
                        description: "Post-acquisition normalization applied to output
                          isotope ratio data beyond the primary mass bias correction.
                          Examples: correction of \u03B4 values for decay of enriched
                          spike isotopes between calibration and use date (double-spike
                          procedures); age correction of \u03B4238U for secular disequilibrium.
                          Record 'None' if no additional normalization is applied."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          isotope ratios and/or elemental concentrations from spike-sample
                          mixture measurements. For double-spike procedures, isotope
                          ratios and concentrations are co-determined through the
                          spike inversion. For conventional ID concentration procedures
                          (separate concentration spike), IUPAC ID equations are used.
                          Record 'None' if neither isotope dilution nor double-spike
                          methods are used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeDilutionDataReductionMethod
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
                        description: "Post-acquisition normalization applied to output
                          isotope ratio data beyond the primary mass bias correction.
                          Examples: correction of \u03B4 values for decay of enriched
                          spike isotopes between calibration and use date (double-spike
                          procedures); age correction of \u03B4238U for secular disequilibrium.
                          Record 'None' if no additional normalization is applied."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
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
                  const: Sample preparation
              required:
              - schema:name
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
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: "Mass resolution mode used in this procedure. MC-ICP-MS
                      instruments allow selection of low resolution (LR; m/\u0394m
                      \u2248 300\u2013400), medium resolution (MR; m/\u0394m \u2248
                      3000\u20138000), or high resolution (HR; m/\u0394m \u2248 10,000\u201312,000).
                      Most isotope ratio measurements use low resolution after chemical
                      separation has removed interfering elements. Medium or high
                      resolution is used when polyatomic interferences (e.g., ArN+,
                      ArO+, ArOH+ on Fe isotopes) cannot be fully resolved by chemistry
                      alone. Procedure registers the mode in use; analyst confirms
                      at session start."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionMcicpmsTAPP/massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                  - title: Make-up Gas and Flow Rate
                    description: "Supplementary gas added to the sample-carrying stream
                      between the sample introduction system and the plasma, with
                      its identity and the procedure-registered target flow rate.
                      Argon make-up is standard and maintains total gas delivery where
                      the carrier flow alone is insufficient \u2014 downstream of
                      an ablation cell, or of a desolvation system that has removed
                      solvent load. Small nitrogen or hydrogen additions are also
                      made here to enhance sensitivity for some elements; record them
                      with their own flow, whose unit commonly differs from the make-up
                      flow. Record 'None' explicitly where no supplementary gas is
                      added, to distinguish it from not reported."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault
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
                  - title: Memory Effect Mitigation
                    description: Procedure applied to minimize carryover of analyte
                      isotopes between successive sample introductions. In MC-ICP-MS,
                      extended rinse periods with the same acid matrix as samples
                      (see Wash Time Between Samples) are the primary mitigation.
                      At data processing level, documents any flagging or exclusion
                      of measurements preceded by samples with significantly different
                      isotopic compositions where carryover may be suspected.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault
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
                    title: Instrument Serial Number or Lab Identifier
                    description: Serial number or laboratory-internal identifier for
                      the specific instrument unit. Supports traceability to instrument
                      service records.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: "Mass resolution mode used in this procedure. MC-ICP-MS
                      instruments allow selection of low resolution (LR; m/\u0394m
                      \u2248 300\u2013400), medium resolution (MR; m/\u0394m \u2248
                      3000\u20138000), or high resolution (HR; m/\u0394m \u2248 10,000\u201312,000).
                      Most isotope ratio measurements use low resolution after chemical
                      separation has removed interfering elements. Medium or high
                      resolution is used when polyatomic interferences (e.g., ArN+,
                      ArO+, ArOH+ on Fe isotopes) cannot be fully resolved by chemistry
                      alone. Procedure registers the mode in use; analyst confirms
                      at session start."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/solutionMcicpmsTAPP/massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
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
                    title: Make-up Gas and Flow Rate
                    description: "Supplementary gas added to the sample-carrying stream
                      between the sample introduction system and the plasma, with
                      its identity and the procedure-registered target flow rate.
                      Argon make-up is standard and maintains total gas delivery where
                      the carrier flow alone is insufficient \u2014 downstream of
                      an ablation cell, or of a desolvation system that has removed
                      solvent load. Small nitrogen or hydrogen additions are also
                      made here to enhance sensitivity for some elements; record them
                      with their own flow, whose unit commonly differs from the make-up
                      flow. Record 'None' explicitly where no supplementary gas is
                      added, to distinguish it from not reported."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault
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
                    title: Memory Effect Mitigation
                    description: Procedure applied to minimize carryover of analyte
                      isotopes between successive sample introductions. In MC-ICP-MS,
                      extended rinse periods with the same acid matrix as samples
                      (see Wash Time Between Samples) are the primary mitigation.
                      At data processing level, documents any flagging or exclusion
                      of measurements preceded by samples with significantly different
                      isotopic compositions where carryover may be suspected.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault
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
                        schema:name:
                          description: Type of plasma torch used (e.g., standard quartz,
                            high-matrix, low-flow).
                          anyOf:
                          - type: string
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              readOnly: true
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
                                const: ada:parameter/solutionMcicpmsTAPP/torchDepthDefault
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
                                  const: ada:parameter/solutionMcicpmsTAPP/torchDepthDefault
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
                              description: "Geometry and designation of the sampler
                                and skimmer cones installed during analysis. For Neptune-type
                                instruments, H-cones (standard) and X-cones (high-sensitivity,
                                ~3\xD7 higher transmission) are common options; the
                                choice affects ion beam intensity and is a procedure
                                design decision. Jet cones combined with an interface
                                pump upgrade are used on some instruments for enhanced
                                sensitivity."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration
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
                                skimmer cones. Nickel (Ni) is standard for HNO3 matrices.
                                Platinum (Pt) cones are used for HCl-rich matrices
                                (e.g., 6 M HCl in Fe chemistry procedures) due to
                                greater corrosion resistance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial
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
                              description: "Geometry and designation of the sampler
                                and skimmer cones installed during analysis. For Neptune-type
                                instruments, H-cones (standard) and X-cones (high-sensitivity,
                                ~3\xD7 higher transmission) are common options; the
                                choice affects ion beam intensity and is a procedure
                                design decision. Jet cones combined with an interface
                                pump upgrade are used on some instruments for enhanced
                                sensitivity."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/interfaceConeConfiguration
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
                                skimmer cones. Nickel (Ni) is standard for HNO3 matrices.
                                Platinum (Pt) cones are used for HCl-rich matrices
                                (e.g., 6 M HCl in Fe chemistry procedures) due to
                                greater corrosion resistance.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/samplerAndSkimmerConeMaterial
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
                            const: Collision Reaction Cell
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: "Whether a collision or reaction cell is installed
                            and its operating mode for this procedure. Most conventional
                            multi-collector instruments have no cell \u2014 mass bias
                            and isobaric interferences are handled entirely by chemical
                            separation and mass-bias correction (record 'Not installed').
                            A small number of modern MC-ICP-MS instruments (e.g.,
                            Nu Instruments Sapphire, Thermo Scientific Neoma MS/MS)
                            add a hexapole collision/reaction cell upstream of the
                            collector array, operated in STD/KED/DRC modes analogous
                            to quadrupole ICP-MS/MS instruments, to suppress polyatomic
                            and isobaric interferences before simultaneous multi-collection.
                            Specific gas types, flow rates, and voltages are documented
                            in Group 4."
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
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Collision Gas Type
                              description: Type of collision gas used in KED mode
                                for polyatomic interference suppression, on collision/reaction-cell-equipped
                                MC-ICP-MS instruments (e.g., Nu Sapphire, Thermo Neoma
                                MS/MS). Record 'N/A' if the instrument has no cell
                                or KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/collisionGasType
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
                            - title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas in KED mode
                                (mL/min), on collision/reaction-cell-equipped MC-ICP-MS
                                instruments. Higher flow rates provide greater interference
                                suppression at the cost of analyte sensitivity. Record
                                'N/A' if the instrument has no cell or KED mode is
                                not used. Record 'N/A' where Collision/Reaction Cell
                                (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRateDefault
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
                            - title: Cell Exit Discrimination Voltage
                              description: Kinetic energy discrimination offset voltage
                                applied at the exit of the collision cell (V), on
                                collision/reaction-cell-equipped MC-ICP-MS instruments.
                                Controls the degree of polyatomic ion suppression.
                                Record 'N/A' if the instrument has no cell or KED
                                mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                            - title: Reaction Gas Type
                              description: Type of reactive gas introduced into the
                                dynamic reaction cell (e.g., NH3, O2, CH4), on collision/reaction-cell-equipped
                                MC-ICP-MS instruments. Record 'N/A' if the instrument
                                has no cell or DRC mode is not used. Record 'N/A'
                                where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/reactionGasType
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
                            - title: Reaction Gas Flow Rate
                              description: Flow rate of the reaction gas in DRC mode
                                (mL/min), on collision/reaction-cell-equipped MC-ICP-MS
                                instruments. Record 'N/A' if the instrument has no
                                cell or DRC mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRateDefault
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
                          allOf:
                          - contains:
                              title: Collision Gas Type
                              description: Type of collision gas used in KED mode
                                for polyatomic interference suppression, on collision/reaction-cell-equipped
                                MC-ICP-MS instruments (e.g., Nu Sapphire, Thermo Neoma
                                MS/MS). Record 'N/A' if the instrument has no cell
                                or KED mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/collisionGasType
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
                              title: Collision Gas Flow Rate
                              description: Flow rate of the collision gas in KED mode
                                (mL/min), on collision/reaction-cell-equipped MC-ICP-MS
                                instruments. Higher flow rates provide greater interference
                                suppression at the cost of analyte sensitivity. Record
                                'N/A' if the instrument has no cell or KED mode is
                                not used. Record 'N/A' where Collision/Reaction Cell
                                (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRateDefault
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
                              title: Cell Exit Discrimination Voltage
                              description: Kinetic energy discrimination offset voltage
                                applied at the exit of the collision cell (V), on
                                collision/reaction-cell-equipped MC-ICP-MS instruments.
                                Controls the degree of polyatomic ion suppression.
                                Record 'N/A' if the instrument has no cell or KED
                                mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include KED.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                              title: Reaction Gas Type
                              description: Type of reactive gas introduced into the
                                dynamic reaction cell (e.g., NH3, O2, CH4), on collision/reaction-cell-equipped
                                MC-ICP-MS instruments. Record 'N/A' if the instrument
                                has no cell or DRC mode is not used. Record 'N/A'
                                where Collision/Reaction Cell (CRC) Configuration
                                does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/reactionGasType
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
                          - contains:
                              title: Reaction Gas Flow Rate
                              description: Flow rate of the reaction gas in DRC mode
                                (mL/min), on collision/reaction-cell-equipped MC-ICP-MS
                                instruments. Record 'N/A' if the instrument has no
                                cell or DRC mode is not used. Record 'N/A' where Collision/Reaction
                                Cell (CRC) Configuration does not include DRC.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRateDefault
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
                            - title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/rfPowerDefault
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
                            - title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault
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
                            - title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault
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
                            - title: Plasma Thermal Mode
                              description: Whether the ICP plasma is operated under
                                normal (hot) or cool plasma conditions. Normal plasma
                                (>1000 W RF) is standard for solution MC-ICP-MS. Cool
                                plasma is rarely used in MC-ICP-MS due to stability
                                requirements for high-precision isotope ratio work.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode
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
                          allOf:
                          - contains:
                              title: RF Power
                              description: Radiofrequency forward power applied to
                                the plasma (W). Controls ionization efficiency and
                                oxide production rates.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/rfPowerDefault
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
                          - contains:
                              title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant) argon
                                gas stream (L/min). Influences plasma temperature
                                and oxide ion formation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRateDefault
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
                              title: Auxiliary Gas Flow Rate
                              description: Flow rate of the intermediate (auxiliary)
                                argon gas stream between torch body and injector tube
                                (L/min).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRateDefault
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
                              title: Plasma Thermal Mode
                              description: Whether the ICP plasma is operated under
                                normal (hot) or cool plasma conditions. Normal plasma
                                (>1000 W RF) is standard for solution MC-ICP-MS. Cool
                                plasma is rarely used in MC-ICP-MS due to stability
                                requirements for high-precision isotope ratio work.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/plasmaThermalMode
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
                          const: Collision Reaction Cell
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
        - title: Spike / Outlier Filtering Approach
          description: Criteria used to identify and exclude anomalous cycles or replicate
            measurements from the calculated isotope ratio mean. Filtering is applied
            after baseline subtraction and before mass bias correction.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault
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
              const: ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_desolvationSystem
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Procedure_internalStandardConcentration
        minContains: 0
        maxContains: 1
      - contains:
          title: Spike / Outlier Filtering Approach
          description: Criteria used to identify and exclude anomalous cycles or replicate
            measurements from the calculated isotope ratio mean. Filtering is applied
            after baseline subtraction and before mass bias correction.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault
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
              const: ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault
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
    ada:sampleSequenceDesign:
      description: "Description of the measurement order within a session: how sample
        solutions, bracketing standards, secondary reference materials, and blanks
        are interleaved. For SSB procedures, each sample is bracketed by two standards
        (standard\u2013sample\u2013standard); the bracketing standard is the same
        isotopic material as the zero-delta reference. For double-spike procedures,
        standards are spiked to the same level as samples before analysis."
      type: string
      readOnly: true
    ada:internalStandardElement:
      description: 'Element added at a known concentration to all sample and standard
        solutions to serve as an internal normalization standard for mass bias correction
        (SSB + internal normalization procedures). The element must have a known isotopic
        composition and mass similar to the analyte. Examples: Ni or Cu doping for
        Fe isotopes (must verify complete matrix separation); Tl for Pb isotopes;
        Cd for Sb isotopes. Specify element and monitored isotope. Record ''None''
        if SSB without internal standard or double-spike method is used.'
      type: string
      readOnly: true
    ada:oxideProductionMethodAndThreshold:
      description: Method used to quantify plasma oxide production and the acceptance
        threshold applied before commencing analysis. Record both the monitored mass
        ratio(s) and the maximum allowed threshold(s). Measured values are recorded
        in Oxide Production. CeO+/Ce+ (m/z 156/140) is the standard monitor proxy.
        Stricter oxide thresholds may be required for analytes sensitive to oxide
        interferences (e.g., BaO+ on REE isotopes).
      type: string
      readOnly: true
    ada:perAnalyteCalibrationStrategy:
      type: array
      items:
        description: Approach used to convert measured ion signals to elemental concentrations,
          where concentration data are also a product of the procedure (e.g., isotope
          dilution combined with isotope ratio measurement). For procedures producing
          isotope ratios only (no concentration output), record 'Not applicable (isotope
          ratios only)'. For double-spike procedures that simultaneously yield concentrations,
          record the ID calculation approach. Where different elements use different
          strategies, record each.
        type: string
        enum:
        - Not applicable (isotope ratios only)
        - Isotope dilution via double-spike inversion (concentrations co-determined
          with isotope ratios)
        - IUPAC isotope dilution equations (separate ID spike)
        - N/A
        - None
        - missing
        readOnly: true
    ada:signalIntegrationIntervalMethod:
      description: Method used to define which portion of the acquisition signal is
        integrated for each measurement. In MC-ICP-MS, all cycles within a block are
        typically used unless signal instability is detected. Specify the rule for
        including or excluding individual cycles.
      type: string
      enum:
      - All cycles included unless signal instability detected
      - Visual inspection of cycle-by-cycle data; outlier cycles excluded manually
      - "Automated 2\u03C3 outlier rejection per block"
      - N/A
      - None
      - missing
      readOnly: true
    ada:blankBackgroundCorrectionMethod:
      description: Method used to subtract instrument background from analytical signals.
        In MC-ICP-MS, on-peak zero subtraction (aspirating the same acid matrix as
        samples while measuring background at the analyte masses with beam deflector
        or from baseline cycles at the start of each block) is standard. For isotope
        ratio procedures where procedural blank is minor relative to the sample signal,
        on-peak zero is often sufficient. For low-level analyses, procedural blank
        must be measured and subtracted.
      type: string
      enum:
      - On-peak zero (acid blank)
      - Procedural blank
      - On-peak zero + procedural blank
      - N/A
      - None
      - missing
      readOnly: true
    ada:channelTemplate:
      type: object
      properties:
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: Isobaric Interference Corrections Applied
              description: 'Whether mathematical corrections for residual isobaric
                or polyatomic interferences are applied in data reduction, supplementary
                to any interference suppression achieved by chemical separation or
                mass resolution. In solution MC-ICP-MS, chemical separation is the
                primary interference mitigation; mathematical corrections address
                residual contributions. Common examples: 204Hg on 204Pb; abundance
                sensitivity tailing of 238U onto 236U and 235U.'
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
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
              description: List of isobaric or polyatomic species mathematically corrected
                in data reduction. Includes direct isobars (e.g., 54Cr+ on 54Fe+,
                58Ni+ on 58Fe+), abundance sensitivity tailing (e.g., 238U tail on
                235U and 236U in U isotope measurements), and hydride interferences
                (e.g., 238UH+ at mass 239).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies
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
              description: Mathematical approach used to calculate and remove residual
                interference contributions. For direct isobars, interference monitor
                masses (e.g., 202Hg to correct 204Hg on 204Pb) are measured simultaneously
                and used with natural abundance ratios to calculate the interference
                contribution. For abundance sensitivity, the tailing factor is measured
                using a pure standard.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod
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
              title: Isobaric Interference Corrections Applied
              description: 'Whether mathematical corrections for residual isobaric
                or polyatomic interferences are applied in data reduction, supplementary
                to any interference suppression achieved by chemical separation or
                mass resolution. In solution MC-ICP-MS, chemical separation is the
                primary interference mitigation; mathematical corrections address
                residual contributions. Common examples: 204Hg on 204Pb; abundance
                sensitivity tailing of 238U onto 236U and 235U.'
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
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
              description: List of isobaric or polyatomic species mathematically corrected
                in data reduction. Includes direct isobars (e.g., 54Cr+ on 54Fe+,
                58Ni+ on 58Fe+), abundance sensitivity tailing (e.g., 238U tail on
                235U and 236U in U isotope measurements), and hydride interferences
                (e.g., 238UH+ at mass 239).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies
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
              description: Mathematical approach used to calculate and remove residual
                interference contributions. For direct isobars, interference monitor
                masses (e.g., 202Hg to correct 204Hg on 204Pb) are measured simultaneously
                and used with natural abundance ratios to calculate the interference
                contribution. For abundance sensitivity, the tailing factor is measured
                using a pure standard.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod
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
    ada:primaryStandardNameDefault:
      description: "Name and reference material identifier of the isotopic reference
        standard used as the bracketing standard (SSB) or zero-delta anchor. This
        is an isotopic composition standard (not a concentration standard): it defines
        the isotopic composition against which all sample \u03B4 or \u03B5 values
        are normalized. Must be a pure, homogeneous, internationally distributed material
        with well-characterized isotopic composition. For double-spike procedures,
        also used for spike calibration. Include the material name, its source or
        supplier, and a citation for the accepted values used, since results calibrated
        against different published values for the same material are not directly
        comparable."
      type: string
    ada:calibrationMeasurementFrequency:
      description: "How often the primary isotopic standard is measured relative to
        unknown samples within a session. For SSB, typically one standard measurement
        before and one after each sample (standard\u2013sample\u2013standard triplet).
        Specify the bracketing scheme."
      type: string
      readOnly: true
    ada:secondaryReferenceMaterialDefault:
      type: array
      items:
        description: Reference material(s) measured as unknowns to independently assess
          analytical accuracy. Specify material name and the isotopic composition
          reference source (certified value, consensus value, or literature compilation).
          For isotope ratio procedures, secondary RMs are geological materials with
          published isotopic compositions (e.g., BHVO-2 for Fe isotopes) or pure isotopic
          standards of certified composition.
        type: string
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set), applicable when
                isotope dilution concentrations are also reported. For pure isotope
                ratio procedures (no concentration output), this field is N/A or reports
                the minimum sample mass required for a measurement at target precision.
                Specify units \xB5g/g or \xB5g/L and whether values are procedure-typical
                estimates or session-measured. Record 'N/A' where the procedure produces
                isotope ratios only and reports no concentrations."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimit
                schema:name:
                  const: Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
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
            - title: Detection Limit Method
              description: Method used to calculate detection limits for each reported
                concentration variable, where concentration data are reported.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
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
            - title: Limit of Quantification (LOQ) Method
              description: Method used to determine the limit of quantification, where
                applicable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod
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
            - title: Analytical Accuracy and Assessment Method
              description: "Accuracy of isotope ratio or \u03B4-value measurements
                relative to certified or published consensus values and the method
                used to assess it. For isotope ratio procedures, accuracy is typically
                assessed by comparing measured \u03B4 values for secondary geological
                reference materials against published interlaboratory compilations
                or certified values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
          allOf:
          - contains:
              title: Detection Limit
              description: "Elemental detection limits, one per reported concentration
                variable (one per analyte, these being the same set), applicable when
                isotope dilution concentrations are also reported. For pure isotope
                ratio procedures (no concentration output), this field is N/A or reports
                the minimum sample mass required for a measurement at target precision.
                Specify units \xB5g/g or \xB5g/L and whether values are procedure-typical
                estimates or session-measured. Record 'N/A' where the procedure produces
                isotope ratios only and reports no concentrations."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/detectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimit
                schema:name:
                  const: Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
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
            minContains: 0
            maxContains: 1
          - contains:
              title: Detection Limit Method
              description: Method used to calculate detection limits for each reported
                concentration variable, where concentration data are reported.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
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
              title: Limit of Quantification (LOQ) Method
              description: Method used to determine the limit of quantification, where
                applicable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/limitOfQuantificationMethod
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
              title: Analytical Accuracy and Assessment Method
              description: "Accuracy of isotope ratio or \u03B4-value measurements
                relative to certified or published consensus values and the method
                used to assess it. For isotope ratio procedures, accuracy is typically
                assessed by comparing measured \u03B4 values for secondary geological
                reference materials against published interlaboratory compilations
                or certified values."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/solutionMcicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
  required:
  - ada:sampleSequenceDesign
  - ada:internalStandardElement
  - ada:oxideProductionMethodAndThreshold
  - ada:signalIntegrationIntervalMethod
  - ada:blankBackgroundCorrectionMethod
  - ada:primaryStandardNameDefault
  - ada:calibrationMeasurementFrequency

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld)

## Sources

* [Solution_MC-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp`

