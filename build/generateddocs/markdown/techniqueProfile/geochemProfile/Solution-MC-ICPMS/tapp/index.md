
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP Münster (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "schema:value": "\"closed Savillex beakers\""
          }
        ],
        "schema:description": "1: HF-HNO3 (-HClO4), closed Savillex beakers on a hotplate | 2: inverse aqua regia. Both steps stated; conditions not given beyond 'on a hotplate'.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Standard sample and (H) skimmer cones"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
      "schema:defaultValue": 100,
      "schema:description": "100 isotope ratio measurements, preceded by 40 baseline integrations"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.4,
      "schema:description": "8.4 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "40 on-peak-zero baseline integrations of 8.4 s preceding each measurement"
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 98Mo/96Mo = 1.453173 using the exponential law, plus bracketing against the Alfa Aesar standard",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁹²Mo",
      "⁹⁴Mo",
      "⁹⁵Mo",
      "⁹⁶Mo",
      "⁹⁷Mo",
      "⁹⁸Mo",
      "¹⁰⁰Mo (Mo)",
      "⁹¹Zr",
      "⁹⁹Ru (interference monitors, no target species) — \"Isobaric interferences of Zr and Ru on Mo masses were corrected by monitoring 91Zr and 99Ru\" (p.2)",
      "mass bias normalised to 98Mo/96Mo and ε⁹²/⁹⁴/⁹⁵/⁹⁷/¹⁰⁰Mo reported (pp.2–3)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "εiMo relative to the Alfa Aesar solution standard, εiMo = [(iMo/96Mo)sample/(iMo/96Mo)standard − 1] x 10^4"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "98Mo/96Mo = 1.453173",
  "ada:chromatographicSeparationApplied": "Yes — two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:uncertaintyLevel": "2 s.d. for external reproducibility (n = 24 for Mo, n = 14 for Ba)",
  "ada:blankBackgroundCorrectionMethod": "On-peak-zero baseline integrations subtracted",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\""
  ],
  "ada:primaryStandardNameDefault": "Alfa Aesar Mo solution standard",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP M\u00fcnster (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "schema:value": "\"closed Savillex beakers\""
          }
        ],
        "schema:description": "1: HF-HNO3 (-HClO4), closed Savillex beakers on a hotplate | 2: inverse aqua regia. Both steps stated; conditions not given beyond 'on a hotplate'.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Standard sample and (H) skimmer cones"
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
      "schema:defaultValue": 100,
      "schema:description": "100 isotope ratio measurements, preceded by 40 baseline integrations"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.4,
      "schema:description": "8.4 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "40 on-peak-zero baseline integrations of 8.4 s preceding each measurement"
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 98Mo/96Mo = 1.453173 using the exponential law, plus bracketing against the Alfa Aesar standard",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2079\u00b2Mo",
      "\u2079\u2074Mo",
      "\u2079\u2075Mo",
      "\u2079\u2076Mo",
      "\u2079\u2077Mo",
      "\u2079\u2078Mo",
      "\u00b9\u2070\u2070Mo (Mo)",
      "\u2079\u00b9Zr",
      "\u2079\u2079Ru (interference monitors, no target species) \u2014 \"Isobaric interferences of Zr and Ru on Mo masses were corrected by monitoring 91Zr and 99Ru\" (p.2)",
      "mass bias normalised to 98Mo/96Mo and \u03b5\u2079\u00b2/\u2079\u2074/\u2079\u2075/\u2079\u2077/\u00b9\u2070\u2070Mo reported (pp.2\u20133)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b5iMo relative to the Alfa Aesar solution standard, \u03b5iMo = [(iMo/96Mo)sample/(iMo/96Mo)standard \u2212 1] x 10^4"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "98Mo/96Mo = 1.453173",
  "ada:chromatographicSeparationApplied": "Yes \u2014 two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:uncertaintyLevel": "2 s.d. for external reproducibility (n = 24 for Mo, n = 14 for Ba)",
  "ada:blankBackgroundCorrectionMethod": "On-peak-zero baseline integrations subtracted",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\""
  ],
  "ada:primaryStandardNameDefault": "Alfa Aesar Mo solution standard",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:finalSolutionMatrix": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: HF-HNO3 (-HClO4), closed Savillex beakers on a hotplate | 2: inverse aqua regia. Both steps stated; conditions not given beyond 'on a hotplate'." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"HF–HNO3(–HClO4), followed by inverse aqua regia\"" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Chondrule, matrix and bulk rock separates; preparation detailed in the supplementary material" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Budde+etal2016 | Neptune Plus | IfP Münster (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Bracketing runs of the Alfa Aesar solution standard; BHVO-2 digestions \"analyzed together with each set of samples\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "On-peak-zero baseline integrations subtracted" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "mass bias normalised to 98Mo/96Mo and ε⁹²/⁹⁴/⁹⁵/⁹⁷/¹⁰⁰Mo reported (pp.2–3)",
                "¹⁰⁰Mo (Mo)",
                "⁹²Mo",
                "⁹¹Zr",
                "⁹⁴Mo",
                "⁹⁵Mo",
                "⁹⁶Mo",
                "⁹⁷Mo",
                "⁹⁸Mo",
                "⁹⁹Ru (interference monitors, no target species) — \"Isobaric interferences of Zr and Ru on Mo masses were corrected by monitoring 91Zr and 99Ru\" (p.2)" ] ;
    ada:chromatographicSeparationApplied "Yes — two-stage anion exchange for W, with Mo collected in 3 M HNO3 and further purified on Eichrom TRU Resin; Ba separated on AG50-X8" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalNormalizationElementAndIsotopeRatio "98Mo/96Mo = 1.453173" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Internal normalization to 98Mo/96Mo = 1.453173 using the exponential law, plus bracketing against the Alfa Aesar standard" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "Alfa Aesar Mo solution standard" ;
    ada:reportedProperties "εiMo relative to the Alfa Aesar solution standard, εiMo = [(iMo/96Mo)sample/(iMo/96Mo)standard − 1] x 10^4" ;
    ada:samplingUnit "Digestion aliquot — \"All samples (0.3–0.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, \"several digestions of which were processed through the full analytical protocol and analyzed together with each set of samples\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "2 s.d. for external reproducibility (n = 24 for Mo, n = 14 for Ba)" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
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

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Standard sample and (H) skimmer cones" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "40 on-peak-zero baseline integrations of 8.4 s preceding each measurement" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.4e+00 ;
    schema1:description "8.4 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Fractionation Law" ;
    schema1:value "Exponential law" ;
    schema1:valueName "massFractionationLaw" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "100 isotope ratio measurements, preceded by 40 baseline integrations" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
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
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "missing" ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "@id": "ada:parameter/module/ICPMS/guardElectrode",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "guardElectrode",
            "schema:name": "Guard Electrode",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
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
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "1: 5 ml HNO3 (50%), hot plate below 70 deg C, taken to dryness | 2: 3 ml concentrated HNO3 + 2 ml HCl (50%), sealed PTFE vessel, 70 deg C, taken to dryness. The subsequent 4 ml 2% HNO3 is the final uptake, not a step.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "X-cones"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "~15 L/min Ar"
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
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8 L/min Ar"
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
              "schema:value": "Nine Faraday cups — \"equipped with nine Faraday Cups\" (p.3); Table 1 gives detection system \"Faraday cups\" and acquisition mode \"Static, analogue detectors\" (p.3). No ion counter stated"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "\"High (entrance slit); Low (detector slit)\""
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
          "schema:defaultValue": "Wash-out 2 min for solution"
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
      "schema:defaultValue": 20,
      "schema:description": "20 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.5,
      "schema:description": "8.5 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against matrix-matched purified S solutions",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "³²S (L3)",
      "³³S (C)",
      "³⁴S (H3) — Table 1 \"Cup configuration\"",
      "p.3. All three serve the single target species S"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ34S and δ33S in permil vs V-CDT"
  ],
  "ada:chromatographicSeparationApplied": "Yes — cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98±4%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "2% (w/w) HNO3, 50 ppm S stock",
  "ada:washTimeBetweenSamples": "2 min for solution work (4 min for laser)",
  "ada:uncertaintyLevel": "\"external reproducibility is reported at the 2σ error level\"; long-term reproducibility \"typically 0.20‰ and 0.45‰ (2σ) for solution and laser\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions"
  ],
  "ada:primaryStandardNameDefault": "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "@id": "ex:solutionMcicpmsTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P1",
  "schema:description": "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "@id": "ada:parameter/module/ICPMS/guardElectrode",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "guardElectrode",
            "schema:name": "Guard Electrode",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
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
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "1: 5 ml HNO3 (50%), hot plate below 70 deg C, taken to dryness | 2: 3 ml concentrated HNO3 + 2 ml HCl (50%), sealed PTFE vessel, 70 deg C, taken to dryness. The subsequent 4 ml 2% HNO3 is the final uptake, not a step.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "X-cones"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "~15 L/min Ar"
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
              "schema:defaultValue": 0.8,
              "schema:description": "~0.8 L/min Ar"
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
              "schema:value": "Nine Faraday cups \u2014 \"equipped with nine Faraday Cups\" (p.3); Table 1 gives detection system \"Faraday cups\" and acquisition mode \"Static, analogue detectors\" (p.3). No ion counter stated"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "\"High (entrance slit); Low (detector slit)\""
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
          "schema:defaultValue": "Wash-out 2 min for solution"
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
      "schema:defaultValue": 20,
      "schema:description": "20 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.5,
      "schema:description": "8.5 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against matrix-matched purified S solutions",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u00b3\u00b2S (L3)",
      "\u00b3\u00b3S (C)",
      "\u00b3\u2074S (H3) \u2014 Table 1 \"Cup configuration\"",
      "p.3. All three serve the single target species S"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b434S and \u03b433S in permil vs V-CDT"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98\u00b14%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "2% (w/w) HNO3, 50 ppm S stock",
  "ada:washTimeBetweenSamples": "2 min for solution work (4 min for laser)",
  "ada:uncertaintyLevel": "\"external reproducibility is reported at the 2\u03c3 error level\"; long-term reproducibility \"typically 0.20\u2030 and 0.45\u2030 (2\u03c3) for solution and laser\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions"
  ],
  "ada:primaryStandardNameDefault": "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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

ex:solutionMcicpmsTAPP-P1 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: 5 ml HNO3 (50%), hot plate below 70 deg C, taken to dryness | 2: 3 ml concentrated HNO3 + 2 ml HCl (50%), sealed PTFE vessel, 70 deg C, taken to dryness. The subsequent 4 ml 2% HNO3 is the final uptake, not a step." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "5 ml HNO3 (50%), then 3 ml concentrated HNO3 + 2 mL HCl (50%); residue dissolved in 4 mL 2% HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Mineral standard cut as a 2 mm thick section, polished and mounted on a 45x25 mm petrographic slide for the laser half; solution half dissolved from weighed mineral" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "p.3. All three serve the single target species S",
                "³²S (L3)",
                "³³S (C)",
                "³⁴S (H3) — Table 1 \"Cup configuration\"" ] ;
    ada:chromatographicSeparationApplied "Yes — cation exchange AG50-X8 (H+ form), 2.5 ml resin, conditioned with 1.4 N HNO3; S passes through while matrix elements are retained. Yield 98±4%" ;
    ada:finalSolutionMatrix "2% (w/w) HNO3, 50 ppm S stock" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Standard-sample bracketing against matrix-matched purified S solutions" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "In-house S_Alfa and S_Spex 20 ppm S solutions, calibrated against IAEA-S-1, S-2, S-4 and NBS-123" ;
    ada:reportedProperties "δ34S and δ33S in permil vs V-CDT" ;
    ada:samplingUnit "Purified solution aliquot — \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 µg of S\" taken for column purification" ;
    ada:secondaryReferenceMaterialDefault "Sch-M-2 anhydrite mineral standard; geological reference samples with known isotope compositions" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "\"external reproducibility is reported at the 2σ error level\"; long-term reproducibility \"typically 0.20‰ and 0.45‰ (2σ) for solution and laser\"" ;
    ada:washTimeBetweenSamples "2 min for solution work (4 min for laser)" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "~0.8 L/min Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "X-cones" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "~15 L/min Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> a schema1:PropertyValueSpecification ;
    schema1:name "Guard Electrode" ;
    schema1:value "\"Pt-guard electrode: On, grounded\"" ;
    schema1:valueName "guardElectrode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "\"High (entrance slit); Low (detector slit)\"" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Wash-out 2 min for solution" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "Wet plasma — solutions \"introduced as a 'wet' aerosol (in 2% HNO3) into the ICP torch via a cyclonic spray dual chamber\"; dry plasma deliberately rejected as \"not viable for bulk analysis\"" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1150 ;
    schema1:description "~1150 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Array Configuration" ;
    schema1:value "Nine Faraday cups — \"equipped with nine Faraday Cups\" (p.3); Table 1 gives detection system \"Faraday cups\" and acquisition mode \"Static, analogue detectors\" (p.3). No ion counter stated" ;
    schema1:valueName "faradayCupArrayConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.5e+00 ;
    schema1:description "8.5 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 20 ;
    schema1:description "20 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "NEPTUNE (\"Thermo Electron NEPTUNE\")" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "Measurements made \"on the flat-topped peak shoulder\" in MR or HR mode; no numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "Iron meteorites, 1: aqua regia (3:1 HCl-HNO3), 120 deg C, 24 h on a hot plate. Basalts, 1: HF-HNO3 (2:1), 150 deg C, 48 h on a hot plate | 2: 'several steps of aqua regia', number not stated. Both routes then converted to chloride and taken up in 0.25 ml 10 M HCl.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "H skimmer cones"
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^10 Ω for 56Fe+; 10^11 Ω for 54Fe, 57Fe, 58Fe; 10^12 Ω for the 53Cr and 60Ni interference monitors"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium or high resolution — \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\""
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
          "schema:defaultValue": 2,
          "schema:description": "None — the Apex Ω was run \"with no auxiliary N2 flow\""
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
          "schema:defaultValue": "210 s washout between all measurements"
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
      "schema:defaultValue": 25,
      "schema:description": "25 (HR) or 50 (MR) cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.369,
      "schema:description": "8.369 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "\"On peak zero intensities from a blank solution measured at the beginning of each sequence were subtracted from all individual measurements\""
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549 using the exponential law, with IRMM-524a bracketing",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁵⁴Fe",
      "⁵⁶Fe",
      "⁵⁷Fe",
      "⁵⁸Fe (Fe)",
      "⁵³Cr",
      "⁶⁰Ni (interference monitors, no target species) — \"Ion beams of 54Fe+",
      "56Fe+",
      "57Fe+",
      "and 58Fe+ were analyzed in static mode on Faraday collectors... Possible isobaric interferences from 54Cr+ and 58Ni+ were measured simultaneously by monitoring 53Cr+ and 60Ni+\" (p.6)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "µ-notation Fe isotope ratios relative to IRMM-524a"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014",
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3 (measured at 10 µg/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"",
  "ada:washTimeBetweenSamples": "210 s",
  "ada:blankBackgroundCorrectionMethod": "On-peak zero from a blank solution subtracted from all measurements",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2 and BCR-2"
  ],
  "ada:primaryStandardNameDefault": "IRMM-524a",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "Measurements made \"on the flat-topped peak shoulder\" in MR or HR mode; no numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "Iron meteorites, 1: aqua regia (3:1 HCl-HNO3), 120 deg C, 24 h on a hot plate. Basalts, 1: HF-HNO3 (2:1), 150 deg C, 48 h on a hot plate | 2: 'several steps of aqua regia', number not stated. Both routes then converted to chloride and taken up in 0.25 ml 10 M HCl.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "H skimmer cones"
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^10 \u03a9 for 56Fe+; 10^11 \u03a9 for 54Fe, 57Fe, 58Fe; 10^12 \u03a9 for the 53Cr and 60Ni interference monitors"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium or high resolution \u2014 \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\""
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
          "schema:defaultValue": 2,
          "schema:description": "None \u2014 the Apex \u03a9 was run \"with no auxiliary N2 flow\""
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
          "schema:defaultValue": "210 s washout between all measurements"
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
      "schema:defaultValue": 25,
      "schema:description": "25 (HR) or 50 (MR) cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.369,
      "schema:description": "8.369 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "\"On peak zero intensities from a blank solution measured at the beginning of each sequence were subtracted from all individual measurements\""
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549 using the exponential law, with IRMM-524a bracketing",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2075\u2074Fe",
      "\u2075\u2076Fe",
      "\u2075\u2077Fe",
      "\u2075\u2078Fe (Fe)",
      "\u2075\u00b3Cr",
      "\u2076\u2070Ni (interference monitors, no target species) \u2014 \"Ion beams of 54Fe+",
      "56Fe+",
      "57Fe+",
      "and 58Fe+ were analyzed in static mode on Faraday collectors... Possible isobaric interferences from 54Cr+ and 58Ni+ were measured simultaneously by monitoring 53Cr+ and 60Ni+\" (p.6)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u00b5-notation Fe isotope ratios relative to IRMM-524a"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014",
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3 (measured at 10 \u00b5g/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"",
  "ada:washTimeBetweenSamples": "210 s",
  "ada:blankBackgroundCorrectionMethod": "On-peak zero from a blank solution subtracted from all measurements",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2 and BCR-2"
  ],
  "ada:primaryStandardNameDefault": "IRMM-524a",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:solutionMcicpmsTAPP-P2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Iron meteorite pieces \"cut using a diamond saw, polished with SiC abrasive paper, and cleaned in ethanol\"" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Iron meteorites, 1: aqua regia (3:1 HCl-HNO3), 120 deg C, 24 h on a hot plate. Basalts, 1: HF-HNO3 (2:1), 150 deg C, 48 h on a hot plate | 2: 'several steps of aqua regia', number not stated. Both routes then converted to chloride and taken up in 0.25 ml 10 M HCl." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Iron meteorites: aqua regia (3:1 HCl-HNO3). Basalts: HF-HNO3 (2:1) followed by several steps of aqua regia. All converted to chloride and redissolved in 0.25 ml 10 M HCl" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "\"Sample analyses were bracketed by measurements of the reference material IRMM-524a\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "On-peak zero from a blank solution subtracted from all measurements" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "56Fe+",
                "57Fe+",
                "and 58Fe+ were analyzed in static mode on Faraday collectors... Possible isobaric interferences from 54Cr+ and 58Ni+ were measured simultaneously by monitoring 53Cr+ and 60Ni+\" (p.6)",
                "⁵³Cr",
                "⁵⁴Fe",
                "⁵⁶Fe",
                "⁵⁷Fe",
                "⁵⁸Fe (Fe)",
                "⁶⁰Ni (interference monitors, no target species) — \"Ion beams of 54Fe+" ] ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 (200-400 mesh) anion resin, 3 ml, 10.5 cm PFA columns; repeated with new resin. Overall Fe yield >99%" ;
    ada:finalSolutionMatrix "0.3 M HNO3 (measured at 10 µg/g Fe in 0.45 M HNO3); all sample and standard solutions \"prepared with the same 0.3 M HNO3 solution\"" ;
    ada:internalNormalizationElementAndIsotopeRatio "57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549, the certified ratios of IRMM-014" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Internal normalization to 57Fe/56Fe = 0.023095 or 57Fe/54Fe = 0.362549 using the exponential law, with IRMM-524a bracketing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "IRMM-524a" ;
    ada:reportedProperties "µ-notation Fe isotope ratios relative to IRMM-524a" ;
    ada:samplingUnit "Solution aliquot of a digestion — \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2 and BCR-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "missing" ;
    ada:washTimeBetweenSamples "210 s" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "57Fe/56Fe = 0.023095 and 57Fe/54Fe = 0.362549, \"the certified ratios of IRMM-014\" (Craddock and Dauphas, 2010)" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "H skimmer cones" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "None — the Apex Ω was run \"with no auxiliary N2 flow\"" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "Medium or high resolution — \"the measurements were made on the flat-topped peak shoulder in either medium-resolution (MR) or high-resolution (HR) mode\"" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "210 s washout between all measurements" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "Both, by mode — \"either a cyclonic glass spray chamber (wet plasma, MR-mode, Pt cones) or an ESI Apex Ω desolvating nebulizer system (dry plasma, HR-mode, Ni cones)\"" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "\"We used Ni or Pt sampler and H skimmer cones ... The main motivation for using Pt cones was an increase in sensitivity and a decrease in the frequency of cone cleaning\"" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "\"On peak zero intensities from a blank solution measured at the beginning of each sequence were subtracted from all individual measurements\"" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:value "10^10 Ω for 56Fe+; 10^11 Ω for 54Fe, 57Fe, 58Fe; 10^12 Ω for the 53Cr and 60Ni interference monitors" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.369e+00 ;
    schema1:description "8.369 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Fractionation Law" ;
    schema1:value "Exponential law" ;
    schema1:valueName "massFractionationLaw" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 25 ;
    schema1:description "25 (HR) or 50 (MR) cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> a schema1:PropertyValueSpecification ;
    schema1:name "Peak Flatness Method and Threshold" ;
    schema1:value "Measurements made \"on the flat-topped peak shoulder\" in MR or HR mode; no numeric threshold stated" ;
    schema1:valueName "peakFlatnessMethodAndThreshold" ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune \"upgraded to Neptune Plus specifications\"" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 160,
            "schema:description": "160 deg C (hot plate)"
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
            "schema:defaultValue": "2 weeks for the HF-HNO3-HClO4 step and 1 week for the HCl-HNO3 step, the pair performed twice"
          }
        ],
        "schema:description": "1: HF/HNO3 in 3:1 proportion with a few drops of HClO4, hot plate 160 deg C, 2 weeks | 2: evaporated to dryness and redissolved in a 2:1 mixture of HCl:HNO3, 1 week on a hot plate. \"These steps were performed twice to ensure complete digestion\" -- the PAIR is repeated, so under the 2026-09-08 grain rule the members are 2, not 4. The subsequent concentrated HNO3 and 3 M HNO3 are dry-down and uptake, not steps. Resolves the cell left open on 2026-09-08.",
        "bios:reagent": [
          {
            "schema:name": "HF/HNO3 in 3:1 proportion with a few drops of HClO4, then -- after evaporation to dryness -- a 2:1 mixture of HCl:HNO3; dried down and dissolved in concentrated HNO3, diluted in 3 M HNO3 and centrifuged. The first HF/HNO3-HClO4 attack was missing from this cell before 2026-09-08.",
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
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
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
  "ada:analysisSequenceDefault": "Standard-sample bracketing — \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"",
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
      "schema:defaultValue": 40,
      "schema:description": "40 cycles in the main configuration; the subconfiguration measured twice"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.142,
      "schema:description": "4.142 s in the subconfiguration"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against OL-REE standards — \"SSB is advantageous over the double-spike approach because one can distinguish mass-dependent fractionation from isotopic anomalies\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N — the paper states \"The cup configurations used for isotopic analyses of the REEs are provided in table S2\" (p.9)",
      "that supplementary table is not in the archived PDF"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation"
  ],
  "ada:chromatographicSeparationApplied": "Yes — U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25–50 µm resin, 94 steps, 188 ml, 16 h at 70 °C, 0.17 ml/min). Overall yields >95%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "15–25 ppb for the most abundant isotope",
  "ada:washTimeBetweenSamples": "300 s rinsing between bracketed measurements",
  "ada:uncertaintyLevel": "Not stated in the section read",
  "ada:calibrationMeasurementFrequency": "Every sample, spaced by 300 s rinsing",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "OL-REE series",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 160,
            "schema:description": "160 deg C (hot plate)"
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
            "schema:defaultValue": "2 weeks for the HF-HNO3-HClO4 step and 1 week for the HCl-HNO3 step, the pair performed twice"
          }
        ],
        "schema:description": "1: HF/HNO3 in 3:1 proportion with a few drops of HClO4, hot plate 160 deg C, 2 weeks | 2: evaporated to dryness and redissolved in a 2:1 mixture of HCl:HNO3, 1 week on a hot plate. \"These steps were performed twice to ensure complete digestion\" -- the PAIR is repeated, so under the 2026-09-08 grain rule the members are 2, not 4. The subsequent concentrated HNO3 and 3 M HNO3 are dry-down and uptake, not steps. Resolves the cell left open on 2026-09-08.",
        "bios:reagent": [
          {
            "schema:name": "HF/HNO3 in 3:1 proportion with a few drops of HClO4, then -- after evaporation to dryness -- a 2:1 mixture of HCl:HNO3; dried down and dissolved in concentrated HNO3, diluted in 3 M HNO3 and centrifuged. The first HF/HNO3-HClO4 attack was missing from this cell before 2026-09-08.",
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
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
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
  "ada:analysisSequenceDefault": "Standard-sample bracketing \u2014 \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"",
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
      "schema:defaultValue": 40,
      "schema:description": "40 cycles in the main configuration; the subconfiguration measured twice"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.142,
      "schema:description": "4.142 s in the subconfiguration"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against OL-REE standards \u2014 \"SSB is advantageous over the double-spike approach because one can distinguish mass-dependent fractionation from isotopic anomalies\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N \u2014 the paper states \"The cup configurations used for isotopic analyses of the REEs are provided in table S2\" (p.9)",
      "that supplementary table is not in the archived PDF"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25\u201350 \u00b5m resin, 94 steps, 188 ml, 16 h at 70 \u00b0C, 0.17 ml/min). Overall yields >95%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "15\u201325 ppb for the most abundant isotope",
  "ada:washTimeBetweenSamples": "300 s rinsing between bracketed measurements",
  "ada:uncertaintyLevel": "Not stated in the section read",
  "ada:calibrationMeasurementFrequency": "Every sample, spaced by 300 s rinsing",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "OL-REE series",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: HF/HNO3 in 3:1 proportion with a few drops of HClO4, hot plate 160 deg C, 2 weeks | 2: evaporated to dryness and redissolved in a 2:1 mixture of HCl:HNO3, 1 week on a hot plate. \"These steps were performed twice to ensure complete digestion\" -- the PAIR is repeated, so under the 2026-09-08 grain rule the members are 2, not 4. The subsequent concentrated HNO3 and 3 M HNO3 are dry-down and uptake, not steps. Resolves the cell left open on 2026-09-08." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "HF/HNO3 in 3:1 proportion with a few drops of HClO4, then -- after evaporation to dryness -- a 2:1 mixture of HCl:HNO3; dried down and dissolved in concentrated HNO3, diluted in 3 M HNO3 and centrifuged. The first HF/HNO3-HClO4 attack was missing from this cell before 2026-09-08." ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing — \"On average, LREEs were measured nine times bracketed by OL-REE isotope standard spaced apart by 300-s rinsing time\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample, spaced by 300 s rinsing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "N — the paper states \"The cup configurations used for isotopic analyses of the REEs are provided in table S2\" (p.9)",
                "that supplementary table is not in the archived PDF" ] ;
    ada:chromatographicSeparationApplied "Yes — U/TEVA, TODGA, then two-step FPLC on Ln-Spec resin (70 cm x 1.6 mm, 1.4 ml of 25–50 µm resin, 94 steps, 188 ml, 16 h at 70 °C, 0.17 ml/min). Overall yields >95%" ;
    ada:finalSolutionMatrix "15–25 ppb for the most abundant isotope" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Standard-sample bracketing against OL-REE standards — \"SSB is advantageous over the double-spike approach because one can distinguish mass-dependent fractionation from isotopic anomalies\"" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "OL-REE series" ;
    ada:reportedProperties "Mass-dependent REE isotopic fractionation relative to the OL-REE standards, in delta notation" ;
    ada:samplingUnit "Fraction of a CAI digestion — \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "Not stated in the section read" ;
    ada:washTimeBetweenSamples "300 s rinsing between bracketed measurements" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4.142e+00 ;
    schema1:description "4.142 s in the subconfiguration" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 40 ;
    schema1:description "40 cycles in the main configuration; the subconfiguration measured twice" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2 weeks for the HF-HNO3-HClO4 step and 1 week for the HCl-HNO3 step, the pair performed twice" ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 160 ;
    schema1:description "160 deg C (hot plate)" ;
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
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "\"a minimization approach implemented in Mathematica, taking into account all ratios (i.e., 91/90Zr, 92/90Zr, 94/90Zr, and 96/90Zr) with different weighs being assigned to each based on their associated uncertainty\", cross-checked against two exact three-ratio solutions"
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
            "schema:defaultValue": "48 h at 215 deg C in a Parr vessel. The 60 h previously recorded here is the chemical-abrasion ANNEALING at 900 deg C, not a digestion; the abrasion leach itself is 12 h."
          }
        ],
        "schema:description": "Untreated crystals, 1: 29 M HF in a PFA microcapsule inside a Parr vessel, 215 deg C, 48 h. Chemically abraded crystals (19 zircons), 1: 12-h partial dissolution in 29 M HF at 215 deg C under pressure, after annealing at 900 deg C for 60 h | 2: the same complete digestion. The annealing is a pre-treatment, not a digestion step.",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
      "schema:manufacturer": {
        "schema:name": "Nu Instruments",
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
      "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlockDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfCyclesPerBlockDefault",
      "schema:name": "Number of Cycles per Block",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 50,
      "schema:description": "50 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "5 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "\"On-peak-zero correction was done using the mean acid blank intensities before data processing to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
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
      "schema:value": "Power-law form used in the double-spike inversion equation"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "91Zr-96Zr"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
    }
  ],
  "ada:analysisSequenceDefault": "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank",
  "ada:massBiasCorrectionStrategy": "91Zr-96Zr double spike inversion, with ZrNIST bracketing after inversion",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "Masses 90",
      "91",
      "92",
      "93",
      "94",
      "95",
      "96 and 98 — \"Masses 90",
      "91",
      "92",
      "93",
      "94",
      "95",
      "96",
      "and 98 were measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block",
      "allowing direct monitoring of all Zr isotopes and Mo interferences (masses 95 and 98)\" (p.11). 95 and 98 carry the Mo monitors and serve no target species"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ9x/90ZrNIST in permil — δ91/90Zr, δ92/90Zr, δ94/90Zr and δ96/90Zr"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG-1X for U-Pb; Ln-Spec (~300 µl, 25–50 µm) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks",
  "ada:isotopeDilutionSpike": "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio",
  "ada:finalSolutionMatrix": "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr",
  "ada:uncertaintyLevel": "\"the external reproducibility (at 2σ) of the spiked ZrNIST measurements from each run, which in all cases was similar in magnitude or slightly larger than the internal uncertainty determined from counting statistics\"",
  "ada:calibrationMeasurementFrequency": "Every sample — \"Each sample measurement was individually bracketed\"",
  "ada:blankBackgroundCorrectionMethod": "On-peak-zero correction using mean acid blank intensities",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "ZrNIST",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "\"a minimization approach implemented in Mathematica, taking into account all ratios (i.e., 91/90Zr, 92/90Zr, 94/90Zr, and 96/90Zr) with different weighs being assigned to each based on their associated uncertainty\", cross-checked against two exact three-ratio solutions"
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
            "schema:defaultValue": "48 h at 215 deg C in a Parr vessel. The 60 h previously recorded here is the chemical-abrasion ANNEALING at 900 deg C, not a digestion; the abrasion leach itself is 12 h."
          }
        ],
        "schema:description": "Untreated crystals, 1: 29 M HF in a PFA microcapsule inside a Parr vessel, 215 deg C, 48 h. Chemically abraded crystals (19 zircons), 1: 12-h partial dissolution in 29 M HF at 215 deg C under pressure, after annealing at 900 deg C for 60 h | 2: the same complete digestion. The annealing is a pre-treatment, not a digestion step.",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
      "schema:manufacturer": {
        "schema:name": "Nu Instruments",
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
      "@id": "ada:parameter/module/MCICPMS/numberOfCyclesPerBlockDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "numberOfCyclesPerBlockDefault",
      "schema:name": "Number of Cycles per Block",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 50,
      "schema:description": "50 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "5 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "\"On-peak-zero correction was done using the mean acid blank intensities before data processing to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\""
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
      "schema:value": "Power-law form used in the double-spike inversion equation"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "91Zr-96Zr"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
    }
  ],
  "ada:analysisSequenceDefault": "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank",
  "ada:massBiasCorrectionStrategy": "91Zr-96Zr double spike inversion, with ZrNIST bracketing after inversion",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "Masses 90",
      "91",
      "92",
      "93",
      "94",
      "95",
      "96 and 98 \u2014 \"Masses 90",
      "91",
      "92",
      "93",
      "94",
      "95",
      "96",
      "and 98 were measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block",
      "allowing direct monitoring of all Zr isotopes and Mo interferences (masses 95 and 98)\" (p.11). 95 and 98 carry the Mo monitors and serve no target species"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b49x/90ZrNIST in permil \u2014 \u03b491/90Zr, \u03b492/90Zr, \u03b494/90Zr and \u03b496/90Zr"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG-1X for U-Pb; Ln-Spec (~300 \u00b5l, 25\u201350 \u00b5m) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks",
  "ada:isotopeDilutionSpike": "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio",
  "ada:finalSolutionMatrix": "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr",
  "ada:uncertaintyLevel": "\"the external reproducibility (at 2\u03c3) of the spiked ZrNIST measurements from each run, which in all cases was similar in magnitude or slightly larger than the internal uncertainty determined from counting statistics\"",
  "ada:calibrationMeasurementFrequency": "Every sample \u2014 \"Each sample measurement was individually bracketed\"",
  "ada:blankBackgroundCorrectionMethod": "On-peak-zero correction using mean acid blank intensities",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "ZrNIST",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:description "Untreated crystals, 1: 29 M HF in a PFA microcapsule inside a Parr vessel, 215 deg C, 48 h. Chemically abraded crystals (19 zircons), 1: 12-h partial dissolution in 29 M HF at 215 deg C under pressure, after annealing at 900 deg C for 60 h | 2: the same complete digestion. The annealing is a pre-treatment, not a digestion step." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "29 M HF; after conversion to a chloride matrix for U-Pb. Zr aliquots taken up in 3 M HNO3 + 0.5 M HF" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "\"Each sample measurement was individually bracketed by measurements of the ZrNIST solution spiked at the same level as our samples and matched in concentration (60 ng/g) as well as acid matrix\"; each measurement preceded by an acid blank" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "On-peak-zero correction using mean acid blank intensities" ;
    ada:calibrationMeasurementFrequency "Every sample — \"Each sample measurement was individually bracketed\"" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "91",
                "92",
                "93",
                "94",
                "95",
                "96",
                "96 and 98 — \"Masses 90",
                "Masses 90",
                "allowing direct monitoring of all Zr isotopes and Mo interferences (masses 95 and 98)\" (p.11). 95 and 98 carry the Mo monitors and serve no target species",
                "and 98 were measured in static mode at 0.5 amu spacing in the Nu Plasma II collector block" ] ;
    ada:chromatographicSeparationApplied "Yes — AG-1X for U-Pb; Ln-Spec (~300 µl, 25–50 µm) for Zr, giving >95% Zr, undetectable REEs and <3% of initial Hf; TODGA first stage for bulk rocks" ;
    ada:finalSolutionMatrix "0.59 M HNO3 + 0.28 M HF, samples and bracketing standards matched in matrix and at 60 ng/g total Zr" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "In-house 91Zr-96Zr double spike, added at a 0.43:0.57 spike-to-sample Zr mass ratio" ;
    ada:massBiasCorrectionStrategy "91Zr-96Zr double spike inversion, with ZrNIST bracketing after inversion" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "ZrNIST" ;
    ada:reportedProperties "δ9x/90ZrNIST in permil — δ91/90Zr, δ92/90Zr, δ94/90Zr and δ96/90Zr" ;
    ada:samplingUnit "Single crystal — \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "\"the external reproducibility (at 2σ) of the spiked ZrNIST measurements from each run, which in all cases was similar in magnitude or slightly larger than the internal uncertainty determined from counting statistics\"" ;
    ada:washTimeBetweenSamples -9999 ;
    bios:computationalTool [ schema1:name "Mathematica — \"Data were reduced using a minimization approach implemented in Mathematica\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
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

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "Double-spike inversion, Rmeas = [p·RSpike + (1−p)·RStd·(Mx/Mn)^α]·(Mx/Mi)^β, solved by weighted minimisation over four ratios" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "On-peak-zero acid blank before each sample \"to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\"" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "Dry plasma — \"Analyses were conducted in dry plasma mode using a Cetac Aridus II desolvator nebulizer\"" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "\"On-peak-zero correction was done using the mean acid blank intensities before data processing to account for blank contribution as well as any 'memory' effects from the Aridus II sample introduction system during the run\"" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "\"a minimization approach implemented in Mathematica, taking into account all ratios (i.e., 91/90Zr, 92/90Zr, 94/90Zr, and 96/90Zr) with different weighs being assigned to each based on their associated uncertainty\", cross-checked against two exact three-ratio solutions" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "91Zr-96Zr" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "5 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Fractionation Law" ;
    schema1:value "Power-law form used in the double-spike inversion equation" ;
    schema1:valueName "massFractionationLaw" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "50 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Cetac Aridus II — \"Analyses were conducted in dry plasma mode\"" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "48 h at 215 deg C in a Parr vessel. The 60 h previously recorded here is the chemical-abrasion ANNEALING at 900 deg C, not a digestion; the abrasion leach itself is 12 h." ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nu Instruments" ] ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "schema:value": "30 ml fluoropolymer vessel"
          }
        ],
        "schema:description": "1: 4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4 | 2: not stated | 3: not stated. The paper numbers three steps of concentrated HF-HNO3-HCl-HClO4 but gives the composition only of step (i).",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Normal sampler and skimmer cones"
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
              "schema:value": "Nine Faraday collectors — \"The MC-ICPMS at the University of Chicago is equipped with nine Faraday collectors\" (p.8). No ion counter stated"
            },
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "\"All three collectors were equipped with the 10^11 Ω amplifiers\""
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Low resolution"
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
          "schema:defaultValue": "60 s wash in 0.45 M HNO3"
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
      "schema:defaultValue": "A single block"
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
      "schema:defaultValue": 25,
      "schema:description": "25 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.194,
      "schema:description": "4.194 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against NIST SRM984",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁸⁵Rb",
      "⁸⁷Rb (Rb)",
      "⁸⁸Sr (interference monitor, no target species) — \"Rubidium-85 and -87 were measured on L2 and axial (A) Faraday collectors",
      "respectively\"",
      "and the ⁸⁷Sr contribution \"was corrected for by monitoring 88Sr\" (p.8)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ87Rb in permil relative to NIST SRM984"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A — Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes — five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3, ~15–25 ppb Rb",
  "ada:washTimeBetweenSamples": "60 s wash in 0.45 M HNO3, with a 90 s take-up time",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM984",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "schema:value": "30 ml fluoropolymer vessel"
          }
        ],
        "schema:description": "1: 4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4 | 2: not stated | 3: not stated. The paper numbers three steps of concentrated HF-HNO3-HCl-HClO4 but gives the composition only of step (i).",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "Normal sampler and skimmer cones"
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
              "schema:value": "Nine Faraday collectors \u2014 \"The MC-ICPMS at the University of Chicago is equipped with nine Faraday collectors\" (p.8). No ion counter stated"
            },
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "\"All three collectors were equipped with the 10^11 \u03a9 amplifiers\""
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Low resolution"
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
          "schema:defaultValue": "60 s wash in 0.45 M HNO3"
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
      "schema:defaultValue": "A single block"
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
      "schema:defaultValue": 25,
      "schema:description": "25 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.194,
      "schema:description": "4.194 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against NIST SRM984",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2078\u2075Rb",
      "\u2078\u2077Rb (Rb)",
      "\u2078\u2078Sr (interference monitor, no target species) \u2014 \"Rubidium-85 and -87 were measured on L2 and axial (A) Faraday collectors",
      "respectively\"",
      "and the \u2078\u2077Sr contribution \"was corrected for by monitoring 88Sr\" (p.8)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b487Rb in permil relative to NIST SRM984"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A \u2014 Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes \u2014 five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.3 M HNO3, ~15\u201325 ppb Rb",
  "ada:washTimeBetweenSamples": "60 s wash in 0.45 M HNO3, with a 90 s take-up time",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM984",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:solutionMcicpmsTAPP-Dauphas2019 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Whole-rock powder" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: 4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4 | 2: not stated | 3: not stated. The paper numbers three steps of concentrated HF-HNO3-HCl-HClO4 but gives the composition only of step (i)." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Three steps of concentrated HF–HNO3–HCl–HClO4; step (i) \"4 ml 28 M HF + 2 ml 15 M HNO3 + 1 ml 10 M HClO4\"" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "and the ⁸⁷Sr contribution \"was corrected for by monitoring 88Sr\" (p.8)",
                "respectively\"",
                "⁸⁵Rb",
                "⁸⁷Rb (Rb)",
                "⁸⁸Sr (interference monitor, no target species) — \"Rubidium-85 and -87 were measured on L2 and axial (A) Faraday collectors" ] ;
    ada:chromatographicSeparationApplied "Yes — five steps: AG50W-X8 cation, a second cation column, AG1-X8 anion in 2 M HF for Ti, a 40 cm Eichrom Sr resin column for Rb-K, and an AG50W-X8 clean-up. Yields >95%" ;
    ada:finalSolutionMatrix "0.3 M HNO3, ~15–25 ppb Rb" ;
    ada:internalNormalizationElementAndIsotopeRatio "N/A — Rb has two stable isotopes, so internal normalization is not possible; bracketing used instead" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Standard-sample bracketing against NIST SRM984" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM984" ;
    ada:reportedProperties "δ87Rb in permil relative to NIST SRM984" ;
    ada:samplingUnit "Digestion aliquot — \"Samples of about 100 mg or less were digested\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "missing" ;
    ada:washTimeBetweenSamples "60 s wash in 0.45 M HNO3, with a 90 s take-up time" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "87Sr/88Sr = 0.085, \"which is the terrestrial Sr ratio\", used for the 87Sr interference correction; sensitivity tested at 0.0835 and 0.0885" ;
    schema1:name "Constants Reference Values" ;
    schema1:valueName "constantsReferenceValuesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Normal sampler and skimmer cones" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "Low resolution" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "60 s wash in 0.45 M HNO3" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "Ni" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:value "\"All three collectors were equipped with the 10^11 Ω amplifiers\"" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Array Configuration" ;
    schema1:value "Nine Faraday collectors — \"The MC-ICPMS at the University of Chicago is equipped with nine Faraday collectors\" (p.8). No ion counter stated" ;
    schema1:valueName "faradayCupArrayConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4.194e+00 ;
    schema1:description "4.194 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "A single block" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:valueName "numberOfBlocksPerMeasurementDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 25 ;
    schema1:description "25 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
              "schema:value": "\"The Durham Neptune has a 9 Faraday collector array equipped with 10^11 Ω resistor amplifiers which allow a maximum beam of 50 V per channel\" (p.3). An SEM ion counter is also present — abundance sensitivity \"was determined by scanning the low mass tail of a 30 V 192Os beam using the SEM\" (p.3); its position is not stated"
            },
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 Ω"
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM"
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
          "schema:defaultValue": "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\""
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
      "schema:defaultValue": 9,
      "schema:description": "9 blocks"
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
      "schema:defaultValue": 5,
      "schema:description": "5 cycles per block"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4,
      "schema:description": "4 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Electronic baselines \"measured, on peak with the line of sight valve closed\"; peak centering and baselines \"were not carried out at the start of each analysis to reduce measurement time and conserve sample but were repeated several times during an analytical session\""
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
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
      "schema:value": "\"Instrument electronic baselines and amplifier gains were then measured ... while the Neptune was allowed to warm up for half an hour\""
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/faradayCupGainCalibrationMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "faradayCupGainCalibrationMethod",
            "schema:name": "Faraday Cup Gain Calibration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "\"Instrument electronic baselines and amplifier gains were then measured, on peak with the line of sight valve closed\"; \"Although amplifier gains were measured at the start of each session the Virtual Amplifier was used in rotation mode to cancel out amplifier gains\""
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
            "schema:value": "Tuned for \"optimal peak shape\"; mass calibration updated by peak-centering on the centre-cup mass 187Os. No numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "N/A - reference material solutions, no digestion.",
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
  "ada:massBiasCorrectionStrategy": "Instrumental mass bias correction applied offline in Excel alongside abundance sensitivity and W/Re interference corrections",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "¹⁸⁴Os",
      "¹⁸⁶Os",
      "¹⁸⁷Os",
      "¹⁸⁸Os",
      "¹⁸⁹Os",
      "¹⁹⁰Os",
      "¹⁹²Os (Os)",
      "¹⁸⁵Re and ¹⁸²W/¹⁸⁴W/¹⁸⁶W (interference monitors, no target species) — the Os masses are those whose ratios to ¹⁸⁸Os the paper measures and reports",
      "the Re and W monitors are named throughout the interference-correction discussion (§3.6, pp.12–18)",
      "and the L3 detector is named as carrying ¹⁸⁴Os (p.26). The paper gives no single cup-configuration table"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "ada:chromatographicSeparationApplied": "N/A — reference material solutions",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 or 5 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions",
  "ada:uncertaintyLevel": "2SD for short- and long-term reproducibility; within-run errors as \"2 standard errors of the mean (2SE = 2SD/n^0.5; where n = 45 for the Neptune analyses\"",
  "ada:blankBackgroundCorrectionMethod": "Corrections applied offline for abundance sensitivity, W and Re atomic interferences and instrumental mass bias",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "UMd, DTM, LOsST and DROsS Os reference materials",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "@id": "ex:solutionMcicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P6",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
              "schema:value": "\"The Durham Neptune has a 9 Faraday collector array equipped with 10^11 \u03a9 resistor amplifiers which allow a maximum beam of 50 V per channel\" (p.3). An SEM ion counter is also present \u2014 abundance sensitivity \"was determined by scanning the low mass tail of a 30 V 192Os beam using the SEM\" (p.3); its position is not stated"
            },
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 \u03a9"
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background \u2014 a 99.99% decrease reached after 220 s for DTM"
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
          "schema:defaultValue": "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\""
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
      "schema:defaultValue": 9,
      "schema:description": "9 blocks"
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
      "schema:defaultValue": 5,
      "schema:description": "5 cycles per block"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4,
      "schema:description": "4 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Electronic baselines \"measured, on peak with the line of sight valve closed\"; peak centering and baselines \"were not carried out at the start of each analysis to reduce measurement time and conserve sample but were repeated several times during an analytical session\""
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
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
      "schema:value": "\"Instrument electronic baselines and amplifier gains were then measured ... while the Neptune was allowed to warm up for half an hour\""
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/faradayCupGainCalibrationMethod",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "faradayCupGainCalibrationMethod",
            "schema:name": "Faraday Cup Gain Calibration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "\"Instrument electronic baselines and amplifier gains were then measured, on peak with the line of sight valve closed\"; \"Although amplifier gains were measured at the start of each session the Virtual Amplifier was used in rotation mode to cancel out amplifier gains\""
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
            "schema:value": "Tuned for \"optimal peak shape\"; mass calibration updated by peak-centering on the centre-cup mass 187Os. No numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "N/A - reference material solutions, no digestion.",
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
  "ada:massBiasCorrectionStrategy": "Instrumental mass bias correction applied offline in Excel alongside abundance sensitivity and W/Re interference corrections",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u00b9\u2078\u2074Os",
      "\u00b9\u2078\u2076Os",
      "\u00b9\u2078\u2077Os",
      "\u00b9\u2078\u2078Os",
      "\u00b9\u2078\u2079Os",
      "\u00b9\u2079\u2070Os",
      "\u00b9\u2079\u00b2Os (Os)",
      "\u00b9\u2078\u2075Re and \u00b9\u2078\u00b2W/\u00b9\u2078\u2074W/\u00b9\u2078\u2076W (interference monitors, no target species) \u2014 the Os masses are those whose ratios to \u00b9\u2078\u2078Os the paper measures and reports",
      "the Re and W monitors are named throughout the interference-correction discussion (\u00a73.6, pp.12\u201318)",
      "and the L3 detector is named as carrying \u00b9\u2078\u2074Os (p.26). The paper gives no single cup-configuration table"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "ada:chromatographicSeparationApplied": "N/A \u2014 reference material solutions",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 or 5 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions",
  "ada:uncertaintyLevel": "2SD for short- and long-term reproducibility; within-run errors as \"2 standard errors of the mean (2SE = 2SD/n^0.5; where n = 45 for the Neptune analyses\"",
  "ada:blankBackgroundCorrectionMethod": "Corrections applied offline for abundance sensitivity, W and Re atomic interferences and instrumental mass bias",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "UMd, DTM, LOsST and DROsS Os reference materials",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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

ex:solutionMcicpmsTAPP-P6 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A - reference material solutions, no digestion." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N/A — reference material solutions in 3 or 5 mol/l Teflon-distilled HCl" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A — reference material solutions, no solid preparation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupGainCalibrationMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Neptune | Durham AHIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "Corrections applied offline for abundance sensitivity, W and Re atomic interferences and instrumental mass bias" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "and the L3 detector is named as carrying ¹⁸⁴Os (p.26). The paper gives no single cup-configuration table",
                "the Re and W monitors are named throughout the interference-correction discussion (§3.6, pp.12–18)",
                "¹⁸⁴Os",
                "¹⁸⁵Re and ¹⁸²W/¹⁸⁴W/¹⁸⁶W (interference monitors, no target species) — the Os masses are those whose ratios to ¹⁸⁸Os the paper measures and reports",
                "¹⁸⁶Os",
                "¹⁸⁷Os",
                "¹⁸⁸Os",
                "¹⁸⁹Os",
                "¹⁹²Os (Os)",
                "¹⁹⁰Os" ] ;
    ada:chromatographicSeparationApplied "N/A — reference material solutions" ;
    ada:finalSolutionMatrix "3 or 5 mol/l Teflon-distilled HCl" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Instrumental mass bias correction applied offline in Excel alongside abundance sensitivity and W/Re interference corrections" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "UMd, DTM, LOsST and DROsS Os reference materials" ;
    ada:reportedProperties "187Os/188Os, 186Os/188Os and 184Os/188Os ratios" ;
    ada:samplingUnit "Reference material solution aliquot — 200 ng/ml to 2.5 µg/ml Os, ~300 µl consumed per analysis" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "2SD for short- and long-term reproducibility; within-run errors as \"2 standard errors of the mean (2SE = 2SD/n^0.5; where n = 45 for the Neptune analyses\"" ;
    ada:washTimeBetweenSamples "\"Teflon-distilled (TD) 3 or 5 mol/l HCl acid was aspirated between analyses until the 192Os beam decreased to acceptable background levels\"; not required in single-RM sessions" ;
    bios:computationalTool [ schema1:name "Microsoft Excel — \"Following analysis all intensity data was exported and re-processed offline using Excel\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — n = 45 per analysis. No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"At the start of each analytical session the Neptune was tuned for maximum sensitivity and optimal peak shape using an Os solution, either the UMd or DTM RMs, and the mass calibration was updated by peak-centering on the centre-cup mass 187Os\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "\"Instrument electronic baselines and amplifier gains were then measured ... while the Neptune was allowed to warm up for half an hour\"" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Desolvating nebulisers deliberately avoided because of \"severe memory problems for Os\"; ESI PFA-50 low-uptake nebuliser and GE Cinnabar micro-cyclonic spray chamber chosen \"in the hope these would reduce the long Os washout times and poor memory usually associated with solution introduction of Os\"; wash acid aspirated until the 192Os beam fell to background — a 99.99% decrease reached after 220 s for DTM" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "Electronic baselines \"measured, on peak with the line of sight valve closed\"; peak centering and baselines \"were not carried out at the start of each analysis to reduce measurement time and conserve sample but were repeated several times during an analytical session\"" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:value "10^11 Ω" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Array Configuration" ;
    schema1:value "\"The Durham Neptune has a 9 Faraday collector array equipped with 10^11 Ω resistor amplifiers which allow a maximum beam of 50 V per channel\" (p.3). An SEM ion counter is also present — abundance sensitivity \"was determined by scanning the low mass tail of a 30 V 192Os beam using the SEM\" (p.3); its position is not stated" ;
    schema1:valueName "faradayCupArrayConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupGainCalibrationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Gain Calibration Method" ;
    schema1:value "\"Instrument electronic baselines and amplifier gains were then measured, on peak with the line of sight valve closed\"; \"Although amplifier gains were measured at the start of each session the Virtual Amplifier was used in rotation mode to cancel out amplifier gains\"" ;
    schema1:valueName "faradayCupGainCalibrationMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4 ;
    schema1:description "4 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9 ;
    schema1:description "9 blocks" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:valueName "numberOfBlocksPerMeasurementDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "5 cycles per block" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> a schema1:PropertyValueSpecification ;
    schema1:name "Peak Flatness Method and Threshold" ;
    schema1:value "Tuned for \"optimal peak shape\"; mass calibration updated by peak-centering on the centre-cup mass 187Os. No numeric threshold stated" ;
    schema1:valueName "peakFlatnessMethodAndThreshold" ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
              "schema:value": "Seven Faraday cups — \"fitted with a 7 Faraday ‘U–Pb’ collector block and 10^11 Ω resistor amplifiers which permitted maximum beam sizes of 10 V per channel\" (p.4). No ion counter stated"
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
      "schema:description": "1 block"
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
      "schema:defaultValue": 50,
      "schema:description": "50 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8,
      "schema:description": "8 s for sequence 1 and 4 s for sequence 2"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "N/A - reference material solutions, no digestion.",
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
  "ada:massBiasCorrectionStrategy": "\"Samples were processed on-line for W and Re interferences and instrumental mass bias\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N — the paper describes the Nu Plasma acquisition only as two-sequence static multi-collection and gives no mass list or cup configuration for that instrument"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "ada:chromatographicSeparationApplied": "N/A — reference material solutions",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels",
  "ada:uncertaintyLevel": "2SD and 2SE, with n = 50 for the Nu Plasma analyses",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "DTM and LOsST",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "@id": "ex:solutionMcicpmsTAPP-P7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "solutionMcicpms protocol \u2014 P7",
  "schema:description": "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
              "schema:value": "Seven Faraday cups \u2014 \"fitted with a 7 Faraday \u2018U\u2013Pb\u2019 collector block and 10^11 \u03a9 resistor amplifiers which permitted maximum beam sizes of 10 V per channel\" (p.4). No ion counter stated"
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
      "schema:description": "1 block"
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
      "schema:defaultValue": 50,
      "schema:description": "50 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8,
      "schema:description": "8 s for sequence 1 and 4 s for sequence 2"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "N/A - reference material solutions, no digestion.",
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
  "ada:massBiasCorrectionStrategy": "\"Samples were processed on-line for W and Re interferences and instrumental mass bias\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N \u2014 the paper describes the Nu Plasma acquisition only as two-sequence static multi-collection and gives no mass list or cup configuration for that instrument"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "187Os/188Os, 186Os/188Os and 184Os/188Os ratios"
  ],
  "ada:chromatographicSeparationApplied": "N/A \u2014 reference material solutions",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "3 mol/l Teflon-distilled HCl",
  "ada:washTimeBetweenSamples": "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels",
  "ada:uncertaintyLevel": "2SD and 2SE, with n = 50 for the Nu Plasma analyses",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:primaryStandardNameDefault": "DTM and LOsST",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:analysisSequenceDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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

ex:solutionMcicpmsTAPP-P7 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A - reference material solutions, no digestion." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N/A — reference material solutions in Teflon-distilled 3 mol/l HCl" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N/A — reference material solutions, no solid preparation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Nowell+etal2008 | Nu Plasma | NIGL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "N — the paper describes the Nu Plasma acquisition only as two-sequence static multi-collection and gives no mass list or cup configuration for that instrument" ] ;
    ada:chromatographicSeparationApplied "N/A — reference material solutions" ;
    ada:finalSolutionMatrix "3 mol/l Teflon-distilled HCl" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "\"Samples were processed on-line for W and Re interferences and instrumental mass bias\"" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "DTM and LOsST" ;
    ada:reportedProperties "187Os/188Os, 186Os/188Os and 184Os/188Os ratios" ;
    ada:samplingUnit "Reference material solution aliquot — ~6400 µl consumed per analysis" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "2SD and 2SE, with n = 50 for the Nu Plasma analyses" ;
    ada:washTimeBetweenSamples "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels" ;
    bios:computationalTool [ schema1:name "Online processing on the instrument — \"Samples were processed on-line for W and Re interferences and instrumental mass bias\"" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — n = 50 per analysis. No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "TD 3 mol/l HCl aspirated between analyses until the Os beam decreased to acceptable background levels" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Array Configuration" ;
    schema1:value "Seven Faraday cups — \"fitted with a 7 Faraday ‘U–Pb’ collector block and 10^11 Ω resistor amplifiers which permitted maximum beam sizes of 10 V per channel\" (p.4). No ion counter stated" ;
    schema1:valueName "faradayCupArrayConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8 ;
    schema1:description "8 s for sequence 1 and 4 s for sequence 2" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1 block" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:valueName "numberOfBlocksPerMeasurementDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 50 ;
    schema1:description "50 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nu Plasma" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupArrayConfiguration> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "1: concentrated HF/HNO3, closed Teflon bombs, 130 deg C, >48 h | 2: after evaporation of the HF/HNO3, 6N HCl at 130 deg C to dissolve fluoride complexes. Samples were then evaporated to dryness and were ready for chemistry.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "16 L/min"
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
      "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "filteringApproachDefault",
      "schema:name": "Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"any ratio outside 2σ was discarded\""
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
      "schema:defaultValue": 20,
      "schema:description": "Blocks of 20 cycles"
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
      "schema:defaultValue": 20,
      "schema:description": "20 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.389,
      "schema:description": "8.389 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"",
  "ada:massBiasCorrectionStrategy": "\"Measurements were made using standard-sample bracketing to correct for instrumental mass bias\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁸⁴Sr (L2)",
      "⁸⁵Rb (L1)",
      "⁸⁶Sr (C)",
      "⁸⁷Rb + ⁸⁷Sr (H1)",
      "⁸⁸Sr (H2) — Table 2",
      "p.3. ⁸⁵Rb and ⁸⁷Rb serve the target species Rb",
      "the Sr masses are interference monitors with no target species",
      "⁸⁸Sr being the one used to correct ⁸⁷Sr on ⁸⁷Rb"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ87Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard − 1] x 1000"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A — Rb has two stable isotopes; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes — DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.1N HNO3",
  "ada:uncertaintyLevel": "\"the 2 standard error (2se) is reported unless stated otherwise\"; for samples analysed fewer than 3 times, \"the largest 2 se reported for a sample analyzed multiple times has been used\"",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "1: concentrated HF/HNO3, closed Teflon bombs, 130 deg C, >48 h | 2: after evaporation of the HF/HNO3, 6N HCl at 130 deg C to dissolve fluoride complexes. Samples were then evaporated to dryness and were ready for chemistry.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "16 L/min"
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
      "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "filteringApproachDefault",
      "schema:name": "Filtering Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "\"any ratio outside 2\u03c3 was discarded\""
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
      "schema:defaultValue": 20,
      "schema:description": "Blocks of 20 cycles"
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
      "schema:defaultValue": 20,
      "schema:description": "20 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.389,
      "schema:description": "8.389 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"",
  "ada:massBiasCorrectionStrategy": "\"Measurements were made using standard-sample bracketing to correct for instrumental mass bias\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2078\u2074Sr (L2)",
      "\u2078\u2075Rb (L1)",
      "\u2078\u2076Sr (C)",
      "\u2078\u2077Rb + \u2078\u2077Sr (H1)",
      "\u2078\u2078Sr (H2) \u2014 Table 2",
      "p.3. \u2078\u2075Rb and \u2078\u2077Rb serve the target species Rb",
      "the Sr masses are interference monitors with no target species",
      "\u2078\u2078Sr being the one used to correct \u2078\u2077Sr on \u2078\u2077Rb"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b487Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard \u2212 1] x 1000"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "N/A \u2014 Rb has two stable isotopes; bracketing used instead",
  "ada:chromatographicSeparationApplied": "Yes \u2014 DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.1N HNO3",
  "ada:uncertaintyLevel": "\"the 2 standard error (2se) is reported unless stated otherwise\"; for samples analysed fewer than 3 times, \"the largest 2 se reported for a sample analyzed multiple times has been used\"",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "\"Whole rock samples were crushed by hand using an agate mortar until a fine powder was obtained. A minimum of 0.5 g of terrestrial rock or meteorite and 100 mg of lunar samples was crushed in order to avoid non-representational sample analysis\"" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: concentrated HF/HNO3, closed Teflon bombs, 130 deg C, >48 h | 2: after evaporation of the HF/HNO3, 6N HCl at 130 deg C to dissolve fluoride complexes. Samples were then evaporated to dryness and were ready for chemistry." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"a mixture of concentrated HF/HNO3\"; after evaporation \"6N HCl was added\" to dissolve fluoride complexes" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing; an external pure Rb ICP-MS solution \"analyzed as an external standard during each analytical session to monitor the reproducibility\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample (bracketing), plus an external pure Rb solution \"during each analytical session\"" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "p.3. ⁸⁵Rb and ⁸⁷Rb serve the target species Rb",
                "the Sr masses are interference monitors with no target species",
                "⁸⁴Sr (L2)",
                "⁸⁵Rb (L1)",
                "⁸⁶Sr (C)",
                "⁸⁷Rb + ⁸⁷Sr (H1)",
                "⁸⁸Sr (H2) — Table 2",
                "⁸⁸Sr being the one used to correct ⁸⁷Sr on ⁸⁷Rb" ] ;
    ada:chromatographicSeparationApplied "Yes — DGA resin Ca removal (1.8 mL), then AG50 X12 (20 mL and 10 mL) in 3N HCl, then AG50 X8 (1 mL) in 0.5N HCl. Reduces K/Rb by a factor of 200 to K/Rb<2 and gives 88Sr/85Rb<0.005" ;
    ada:finalSolutionMatrix "0.1N HNO3" ;
    ada:internalNormalizationElementAndIsotopeRatio "N/A — Rb has two stable isotopes; bracketing used instead" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "\"Measurements were made using standard-sample bracketing to correct for instrumental mass bias\"" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM984 RbCl; BCR-2 as an alternative bracketing standard in some sessions" ;
    ada:reportedProperties "δ87Rb in permil = [(87Rb/85Rb)sample/(87Rb/85Rb)standard − 1] x 1000" ;
    ada:samplingUnit "Weighed powder aliquot — \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"" ;
    ada:secondaryReferenceMaterialDefault "BCR-2, AGV-2, BHVO-2, GS-N and other terrestrial rocks" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "\"the 2 standard error (2se) is reported unless stated otherwise\"; for samples analysed fewer than 3 times, \"the largest 2 se reported for a sample analyzed multiple times has been used\"" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"any ratio outside 2σ was discarded\" — an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\"" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.01e+00 ;
    schema1:description "1.01 L/min" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Sample cone Jet; skimmer cone H" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "16 L/min" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"any ratio outside 2σ was discarded\"" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.389e+00 ;
    schema1:description "8.389 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfBlocksPerMeasurementDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 20 ;
    schema1:description "Blocks of 20 cycles" ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:valueName "numberOfBlocksPerMeasurementDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 20 ;
    schema1:description "20 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
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
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "schema:value": "Octagonal-body Savillex vials; Parr bomb (Ivuna PB, BCR-2, AGV-1); hotplate (BHVO-2)"
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
        "schema:description": "Main route 1: concentrated HF-HNO3 | 2: HNO3-HCl | 3: HNO3-H2O2. Ivuna high-PT route 1: concentrated HF-HNO3, 3 days | 2: concentrated HCl, 2 days.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 Ω for 90Zr–96Zr and 95Mo; 10^12 Ω for 99Ru and 101Ru"
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
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
        ]
      },
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
          "schema:defaultValue": "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\""
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
      "schema:defaultValue": 60,
      "schema:description": "60 ratios"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.2,
      "schema:description": "4.2 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Both: \"Electronic baselines were measured for 30 s prior to each analysis. An on-peak background correction was performed.\""
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 94Zr/90Zr = 0.3381 using the exponential law; an initial Mo correction uses a mass bias relative to 91Zr/90Zr = 0.21798; results reported by standard sample bracketing to NIST SRM 3169",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁹⁰Zr",
      "⁹¹Zr",
      "⁹²Zr",
      "⁹⁴Zr",
      "⁹⁶Zr (Zr)",
      "⁹⁵Mo",
      "⁹⁹Ru",
      "¹⁰¹Ru (interference monitors, no target species) — \"Faraday cups with 10¹¹ Ω amplifiers were used to collect Zr masses 90Zr to 96Zr and 95Mo",
      "whereas 10¹² Ω amplifiers were applied for the collection of 99Ru and 101Ru\" (p.6)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "ε91Zr, ε92Zr and ε96Zr relative to NIST SRM 3169"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)",
  "ada:chromatographicSeparationApplied": "Yes — four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)",
  "ada:uncertaintyLevel": "Both quoted: \"external precision expressed as 2 standard deviations (2SD)\" and 2SE per analysis",
  "ada:calibrationMeasurementFrequency": "Each session — \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:oxideProductionMethodAndThreshold": "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated",
  "ada:blankBackgroundCorrectionMethod": "\"An on-peak background correction was performed\"; background corrections averaged 0.3, 2 and 98 ppm for 91Zr/90Zr, 92Zr/90Zr and 96Zr/90Zr",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 3169",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Sch\u00f6nb\u00e4chler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "schema:value": "Octagonal-body Savillex vials; Parr bomb (Ivuna PB, BCR-2, AGV-1); hotplate (BHVO-2)"
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
        "schema:description": "Main route 1: concentrated HF-HNO3 | 2: HNO3-HCl | 3: HNO3-H2O2. Ivuna high-PT route 1: concentrated HF-HNO3, 3 days | 2: concentrated HCl, 2 days.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 \u03a9 for 90Zr\u201396Zr and 95Mo; 10^12 \u03a9 for 99Ru and 101Ru"
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
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
        ]
      },
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
          "schema:defaultValue": "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\""
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
      "schema:defaultValue": 60,
      "schema:description": "60 ratios"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4.2,
      "schema:description": "4.2 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Both: \"Electronic baselines were measured for 30 s prior to each analysis. An on-peak background correction was performed.\""
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
      "schema:value": "Exponential law"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:massBiasCorrectionStrategy": "Internal normalization to 94Zr/90Zr = 0.3381 using the exponential law; an initial Mo correction uses a mass bias relative to 91Zr/90Zr = 0.21798; results reported by standard sample bracketing to NIST SRM 3169",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2079\u2070Zr",
      "\u2079\u00b9Zr",
      "\u2079\u00b2Zr",
      "\u2079\u2074Zr",
      "\u2079\u2076Zr (Zr)",
      "\u2079\u2075Mo",
      "\u2079\u2079Ru",
      "\u00b9\u2070\u00b9Ru (interference monitors, no target species) \u2014 \"Faraday cups with 10\u00b9\u00b9 \u03a9 amplifiers were used to collect Zr masses 90Zr to 96Zr and 95Mo",
      "whereas 10\u00b9\u00b2 \u03a9 amplifiers were applied for the collection of 99Ru and 101Ru\" (p.6)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b591Zr, \u03b592Zr and \u03b596Zr relative to NIST SRM 3169"
  ],
  "ada:internalNormalizationElementAndIsotopeRatio": "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)",
  "ada:chromatographicSeparationApplied": "Yes \u2014 four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)",
  "ada:uncertaintyLevel": "Both quoted: \"external precision expressed as 2 standard deviations (2SD)\" and 2SE per analysis",
  "ada:calibrationMeasurementFrequency": "Each session \u2014 \"The Zr standard material NIST SRM 3169 was analyzed in each session\"",
  "ada:oxideProductionMethodAndThreshold": "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated",
  "ada:blankBackgroundCorrectionMethod": "\"An on-peak background correction was performed\"; background corrections averaged 0.3, 2 and 98 ppm for 91Zr/90Zr, 92Zr/90Zr and 96Zr/90Zr",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 3169",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Homogenised powder — Ivuna aliquots taken \"from a larger homogenized powder (550 mg)\"" ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Core/constantsReferenceValuesDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Main route 1: concentrated HF-HNO3 | 2: HNO3-HCl | 3: HNO3-H2O2. Ivuna high-PT route 1: concentrated HF-HNO3, 3 days | 2: concentrated HCl, 2 days." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Concentrated HF-HNO3, then a HNO3-HCl mixture, then a HNO3-H2O2 mixture; Ivuna high PT: concentrated HF-HNO3 for 3 days then concentrated HCl for 2 days" ] ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard sample bracketing against NIST SRM 3169; \"The Zr standard material NIST SRM 3169 was analyzed in each session\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "\"An on-peak background correction was performed\"; background corrections averaged 0.3, 2 and 98 ppm for 91Zr/90Zr, 92Zr/90Zr and 96Zr/90Zr" ;
    ada:calibrationMeasurementFrequency "Each session — \"The Zr standard material NIST SRM 3169 was analyzed in each session\"" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "whereas 10¹² Ω amplifiers were applied for the collection of 99Ru and 101Ru\" (p.6)",
                "¹⁰¹Ru (interference monitors, no target species) — \"Faraday cups with 10¹¹ Ω amplifiers were used to collect Zr masses 90Zr to 96Zr and 95Mo",
                "⁹²Zr",
                "⁹¹Zr",
                "⁹⁰Zr",
                "⁹⁴Zr",
                "⁹⁵Mo",
                "⁹⁶Zr (Zr)",
                "⁹⁹Ru" ] ;
    ada:chromatographicSeparationApplied "Yes — four-step separation on anion exchange (AG 1-X8), DGA and LN resin; two-stage anion exchange for Ivuna; three-stage AG 1-X8 + LN for terrestrial samples" ;
    ada:finalSolutionMatrix "0.5 M HNO3 - 0.005 M HF at 30 ppb Zr (also 17 and 60 ppb)" ;
    ada:internalNormalizationElementAndIsotopeRatio "94Zr/90Zr = 0.3381 (Minster & Ricard 1981)" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Internal normalization to 94Zr/90Zr = 0.3381 using the exponential law; an initial Mo correction uses a mass bias relative to 91Zr/90Zr = 0.21798; results reported by standard sample bracketing to NIST SRM 3169" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "Argide and Ar-Ar-oxide interferences on 94Zr and 96Zr minimised by tuning; no numeric threshold stated" ;
    ada:primaryStandardNameDefault "NIST SRM 3169" ;
    ada:reportedProperties "ε91Zr, ε92Zr and ε96Zr relative to NIST SRM 3169" ;
    ada:samplingUnit "Digestion aliquot — Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2, BCR-2, AGV-1, SCo-1; eucrites Bouvante and Bereba; CO chondrite Colony" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "Both quoted: \"external precision expressed as 2 standard deviations (2SD)\" and 2SE per analysis" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
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

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "\"Normal skimmer and sampler cones were utilized\"" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "\"Tuning was performed to minimize interferences of 40Ar2 16O+ and 40Ar2 14N+ on 96Zr+ and 94Zr+ and with it the on-peak background corrections\"" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "Both: \"Electronic baselines were measured for 30 s prior to each analysis. An on-peak background correction was performed.\"" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:value "10^11 Ω for 90Zr–96Zr and 95Mo; 10^12 Ω for 99Ru and 101Ru" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4.2e+00 ;
    schema1:description "4.2 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/massFractionationLaw> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Fractionation Law" ;
    schema1:value "Exponential law" ;
    schema1:valueName "massFractionationLaw" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 60 ;
    schema1:description "60 ratios" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 150,
            "schema:description": "150 deg C for 1 day then 210 deg C for 2 days (Parr bomb); hotplate for the aqua regia step; 720 deg C for the NaOH fusion (Si route). The 130 deg C 10 M HCl step previously recorded here is Cr(VI) speciation during column chemistry, not a digestion."
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
            "schema:defaultValue": "3 days in the Parr bomb (1 + 2 days) then 2 days in aqua regia; 13 min for the NaOH fusion. The 3 h and >1 week previously recorded here are Cr speciation during column chemistry."
          }
        ],
        "schema:description": "Bulk and chondrule route, 1: 3:1 7 M HNO3 : 28 M HF in Parr bombs, 3 days (1 day at 150 deg C, 2 days at 210 deg C) | 2: dried down and taken up in aqua regia, 2 further days on a hotplate. Si route, 1: NaOH fusion in silver crucibles, 720 deg C, 13 min, the fusion cake dissolved in Milli-Q water and acidified with HNO3 -- a fusion rather than an acid digestion.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 Ω for 24Mg, 25Mg, 26Mg"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium resolution, M/ΔM > 6,000"
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
          "schema:defaultValue": "None — \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\""
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
          "schema:defaultValue": "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences"
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
      "schema:defaultValue": 200,
      "schema:description": "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.3,
      "schema:description": "Fe 8.3 s; Cr 8.3 s; Mg 16.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "On-peak baseline — Fe 25 x 16.7 s; Cr 75 s; Mg 25 x 16.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "²⁴Mg",
      "²⁵Mg",
      "²⁶Mg (Mg) — \"The isotopes 24Mg",
      "25Mg and 26Mg were analysed using 10¹¹ Ω resistors\" (p.8)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "µ-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut",
  "ada:uncertaintyLevel": "\"the mean and 2 x standard error (SE) of ten individual standard-bracketed sample analyses\"",
  "ada:blankBackgroundCorrectionMethod": "On-peak baseline measurement preceding each analysis",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO2 and DTS-2b, \"processed alongside the samples\""
  ],
  "ada:primaryStandardNameDefault": "IRMM-014, SRM979, DTS-2b",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 150,
            "schema:description": "150 deg C for 1 day then 210 deg C for 2 days (Parr bomb); hotplate for the aqua regia step; 720 deg C for the NaOH fusion (Si route). The 130 deg C 10 M HCl step previously recorded here is Cr(VI) speciation during column chemistry, not a digestion."
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
            "schema:defaultValue": "3 days in the Parr bomb (1 + 2 days) then 2 days in aqua regia; 13 min for the NaOH fusion. The 3 h and >1 week previously recorded here are Cr speciation during column chemistry."
          }
        ],
        "schema:description": "Bulk and chondrule route, 1: 3:1 7 M HNO3 : 28 M HF in Parr bombs, 3 days (1 day at 150 deg C, 2 days at 210 deg C) | 2: dried down and taken up in aqua regia, 2 further days on a hotplate. Si route, 1: NaOH fusion in silver crucibles, 720 deg C, 13 min, the fusion cake dissolved in Milli-Q water and acidified with HNO3 -- a fusion rather than an acid digestion.",
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
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
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/MCICPMS/faradayCupAmplifierResistorValues",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "faradayCupAmplifierResistorValues",
              "schema:name": "Faraday Cup Amplifier Resistor Values",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "10^11 \u03a9 for 24Mg, 25Mg, 26Mg"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium resolution, M/\u0394M > 6,000"
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
          "schema:defaultValue": "None \u2014 \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\""
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
          "schema:defaultValue": "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences"
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
      "schema:defaultValue": 200,
      "schema:description": "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.3,
      "schema:description": "Fe 8.3 s; Cr 8.3 s; Mg 16.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/baselineMeasurementApproach",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "baselineMeasurementApproach",
      "schema:name": "Baseline Measurement Approach",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "On-peak baseline \u2014 Fe 25 x 16.7 s; Cr 75 s; Mg 25 x 16.7 s"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u00b2\u2074Mg",
      "\u00b2\u2075Mg",
      "\u00b2\u2076Mg (Mg) \u2014 \"The isotopes 24Mg",
      "25Mg and 26Mg were analysed using 10\u00b9\u00b9 \u03a9 resistors\" (p.8)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u00b5-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut",
  "ada:uncertaintyLevel": "\"the mean and 2 x standard error (SE) of ten individual standard-bracketed sample analyses\"",
  "ada:blankBackgroundCorrectionMethod": "On-peak baseline measurement preceding each analysis",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO2 and DTS-2b, \"processed alongside the samples\""
  ],
  "ada:primaryStandardNameDefault": "IRMM-014, SRM979, DTS-2b",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Bulk and chondrule route, 1: 3:1 7 M HNO3 : 28 M HF in Parr bombs, 3 days (1 day at 150 deg C, 2 days at 210 deg C) | 2: dried down and taken up in aqua regia, 2 further days on a hotplate. Si route, 1: NaOH fusion in silver crucibles, 720 deg C, 13 min, the fusion cake dissolved in Milli-Q water and acidified with HNO3 -- a fusion rather than an acid digestion." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Cr/Mg route: 6 M HCl loading, 10 M HCl pretreatment, 0.5 M HCl, 0.5 M HNO3, 1 M HF, 6 M HCl elutions; Si route: NaOH fusion then Milli-Q water and HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Bulk powder; for the Si aliquot, NaOH fusion in silver crucibles" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing, \"ten individual standard-bracketed sample analyses\" per reported value" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "On-peak baseline measurement preceding each analysis" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "25Mg and 26Mg were analysed using 10¹¹ Ω resistors\" (p.8)",
                "²⁴Mg",
                "²⁵Mg",
                "²⁶Mg (Mg) — \"The isotopes 24Mg" ] ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 anion (1 ml) for Fe, then AG50-X12 cation (1 ml) twice for Cr and Mg" ;
    ada:finalSolutionMatrix "0.5 M HNO3 (Cr); 6 M HCl elution of the final Cr cut" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Standard-sample bracketing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "IRMM-014, SRM979, DTS-2b" ;
    ada:reportedProperties "µ-notation Fe relative to IRMM-014, Cr relative to SRM979, Mg relative to DTS-2b" ;
    ada:samplingUnit "Fraction of a bulk digestion — \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO2 and DTS-2b, \"processed alongside the samples\"" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "\"the mean and 2 x standard error (SE) of ten individual standard-bracketed sample analyses\"" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "A Jet and X cone" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Measured \"at low radiofrequency power and sample gas inflow\" deliberately, to reduce gas-based interferences" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None — \"The samples were measured without the use of an auxiliary gas to the introduction system to reduce gas-based interferences\"" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "Medium resolution, M/ΔM > 6,000" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Stated qualitatively — measured \"at low radiofrequency power and sample gas inflow\" to reduce gas-based interferences" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/baselineMeasurementApproach> a schema1:PropertyValueSpecification ;
    schema1:name "Baseline Measurement Approach" ;
    schema1:value "On-peak baseline — Fe 25 x 16.7 s; Cr 75 s; Mg 25 x 16.7 s" ;
    schema1:valueName "baselineMeasurementApproach" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> a schema1:PropertyValueSpecification ;
    schema1:name "Faraday Cup Amplifier Resistor Values" ;
    schema1:value "10^11 Ω for 24Mg, 25Mg, 26Mg" ;
    schema1:valueName "faradayCupAmplifierResistorValues" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.3e+00 ;
    schema1:description "Fe 8.3 s; Cr 8.3 s; Mg 16.7 s" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 200 ;
    schema1:description "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "ESI Apex HF with an actively cooled membrane unit (Cr); ESI Apex Omega (Mg)" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3 days in the Parr bomb (1 + 2 days) then 2 days in aqua regia; 13 min for the NaOH fusion. The 3 h and >1 week previously recorded here are Cr speciation during column chemistry." ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 deg C for 1 day then 210 deg C for 2 days (Parr bomb); hotplate for the aqua regia step; 720 deg C for the NaOH fusion (Si route). The 130 deg C 10 M HCl step previously recorded here is Cr(VI) speciation during column chemistry, not a digestion." ;
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

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neoma" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/faradayCupAmplifierResistorValues> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "Measurements taken \"on the left 'shoulder' of the peak\"; no numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 150,
            "schema:description": "150 deg C (hotplate). The 70 and 140 deg C previously recorded here belong to the carbonate-removal pre-treatment and to the cosmogenic-radionuclide dissolution, which are different preparations in the same paper."
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
            "schema:defaultValue": "About 1 week for the HF-HNO3 step. The 20 h previously recorded here is the cosmogenic-radionuclide dissolution, a different preparation."
          }
        ],
        "schema:description": "1: 3:2 concentrated HF : double-distilled HNO3 in PFA vials, hotplate 150 deg C, about 1 week | 2: dried down, dissolved in 1 ml concentrated HNO3, with 1 ml H2O2 added slowly in 0.1 ml increments | 3: dried down, dissolved in double-distilled HCl. The final 5 ml 2% HNO3 is the uptake, not a step.",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4,
        "bios:reagent": []
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
      "schema:defaultValue": 20,
      "schema:description": "\"Each sample was measured approximately 20 times\""
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against NIST SRM 3141a",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "³⁹K",
      "⁴¹K (K) — δ⁴¹K is defined from the ⁴¹K/³⁹K ratio (p.4). ⁴⁰Ar¹H⁺ is named as the interference on ⁴¹K⁺ (p.4) but is not itself a monitored mass"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ41K in permil relative to NIST SRM 3141a"
  ],
  "ada:chromatographicSeparationApplied": "Yes — twice through 1.5 mL Bio-Rad AG50W-X8 100–200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "300 ppb K solution",
  "ada:uncertaintyLevel": "Stated as ± values on δ41K without an explicit convention in the section read",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing)",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 3141a",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "Measurements taken \"on the left 'shoulder' of the peak\"; no numeric threshold stated"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
            "@id": "ada:parameter/module/SolutionIntroduction/digestionTemperatureDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "digestionTemperatureDefault",
            "schema:name": "Digestion Temperature",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 150,
            "schema:description": "150 deg C (hotplate). The 70 and 140 deg C previously recorded here belong to the carbonate-removal pre-treatment and to the cosmogenic-radionuclide dissolution, which are different preparations in the same paper."
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
            "schema:defaultValue": "About 1 week for the HF-HNO3 step. The 20 h previously recorded here is the cosmogenic-radionuclide dissolution, a different preparation."
          }
        ],
        "schema:description": "1: 3:2 concentrated HF : double-distilled HNO3 in PFA vials, hotplate 150 deg C, about 1 week | 2: dried down, dissolved in 1 ml concentrated HNO3, with 1 ml H2O2 added slowly in 0.1 ml increments | 3: dried down, dissolved in double-distilled HCl. The final 5 ml 2% HNO3 is the uptake, not a step.",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 4,
        "bios:reagent": []
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
      "schema:defaultValue": 20,
      "schema:description": "\"Each sample was measured approximately 20 times\""
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples",
  "ada:massBiasCorrectionStrategy": "Standard-sample bracketing against NIST SRM 3141a",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u00b3\u2079K",
      "\u2074\u00b9K (K) \u2014 \u03b4\u2074\u00b9K is defined from the \u2074\u00b9K/\u00b3\u2079K ratio (p.4). \u2074\u2070Ar\u00b9H\u207a is named as the interference on \u2074\u00b9K\u207a (p.4) but is not itself a monitored mass"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b441K in permil relative to NIST SRM 3141a"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 twice through 1.5 mL Bio-Rad AG50W-X8 100\u2013200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "300 ppb K solution",
  "ada:uncertaintyLevel": "Stated as \u00b1 values on \u03b441K without an explicit convention in the section read",
  "ada:calibrationMeasurementFrequency": "Every sample (bracketing)",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 3141a",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: 3:2 concentrated HF : double-distilled HNO3 in PFA vials, hotplate 150 deg C, about 1 week | 2: dried down, dissolved in 1 ml concentrated HNO3, with 1 ml H2O2 added slowly in 0.1 ml increments | 3: dried down, dissolved in double-distilled HCl. The final 5 ml 2% HNO3 is the uptake, not a step." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Broussard+etal2026 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing against NIST SRM 3141a; BHVO-2 measured alongside the samples" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Every sample (bracketing)" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "³⁹K",
                "⁴¹K (K) — δ⁴¹K is defined from the ⁴¹K/³⁹K ratio (p.4). ⁴⁰Ar¹H⁺ is named as the interference on ⁴¹K⁺ (p.4) but is not itself a monitored mass" ] ;
    ada:chromatographicSeparationApplied "Yes — twice through 1.5 mL Bio-Rad AG50W-X8 100–200 mesh cation resin, loading, matrix elution and K elution all in 0.5 M HNO3" ;
    ada:finalSolutionMatrix "300 ppb K solution" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Standard-sample bracketing against NIST SRM 3141a" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM 3141a" ;
    ada:reportedProperties "δ41K in permil relative to NIST SRM 3141a" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "Stated as ± values on δ41K without an explicit convention in the section read" ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated" ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "Measured \"on the left 'shoulder' of the peak to resolve the difference between 40Ar1H+ and 41K+\"" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 20 ;
    schema1:description "\"Each sample was measured approximately 20 times\"" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/peakFlatnessMethodAndThreshold> a schema1:PropertyValueSpecification ;
    schema1:name "Peak Flatness Method and Threshold" ;
    schema1:value "Measurements taken \"on the left 'shoulder' of the peak\"; no numeric threshold stated" ;
    schema1:valueName "peakFlatnessMethodAndThreshold" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem> a schema1:PropertyValueSpecification ;
    schema1:name "Desolvation System" ;
    schema1:value "Elemental Scientific APEX Omega" ;
    schema1:valueName "desolvationSystem" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "About 1 week for the HF-HNO3 step. The 20 h previously recorded here is the cosmogenic-radionuclide dissolution, a different preparation." ;
    schema1:name "Digestion Duration" ;
    schema1:valueName "digestionDurationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 deg C (hotplate). The 70 and 140 deg C previously recorded here belong to the carbonate-removal pre-treatment and to the cosmogenic-radionuclide dissolution, which are different preparations in the same paper." ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "missing" ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/nebulizerType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Sample Introduction System" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .


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
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "1: concentrated HF and HNO3 in a 3:1 ratio, closed beaker, 170 deg C, 48 h | 2: fluxing in concentrated HNO3 and HCl, with 1 ml H2O2 added slowly during the HNO3 flux to remove organics. The 5 ml 0.5 M HNO3 is the uptake, not a step.",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"",
  "ada:massBiasCorrectionStrategy": "\"To correct for instrument mass bias, the sample–standard bracketing technique was used for all analyses\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "³⁹K",
      "⁴¹K (K)",
      "⁶³Cu",
      "⁶⁵Cu (Cu)",
      "⁶⁴Zn",
      "⁶⁶Zn (Zn) — the three delta values are defined from the ⁴¹K/³⁹K",
      "⁶⁵Cu/⁶³Cu and ⁶⁶Zn/⁶⁴Zn ratios (p.7)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "δ41K, δ65Cu and δ66Zn in permil, each defined explicitly against its bracketing standard"
  ],
  "ada:chromatographicSeparationApplied": "Yes — AG1-X8 200–400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "200 ppb for K and Zn; 100 ppb for Cu",
  "ada:uncertaintyLevel": "2 s.d.",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:primaryStandardNameDefault": "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "1: concentrated HF and HNO3 in a 3:1 ratio, closed beaker, 170 deg C, 48 h | 2: fluxing in concentrated HNO3 and HCl, with 1 ml H2O2 added slowly during the HNO3 flux to remove organics. The 5 ml 0.5 M HNO3 is the uptake, not a step.",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/plasmaThermalMode",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "plasmaThermalMode",
              "schema:name": "Plasma Thermal Mode",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
            "Collector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/ICPMS/part/Collector",
          "schema:description": "missing"
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
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
    }
  ],
  "ada:analysisSequenceDefault": "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"",
  "ada:massBiasCorrectionStrategy": "\"To correct for instrument mass bias, the sample\u2013standard bracketing technique was used for all analyses\"",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u00b3\u2079K",
      "\u2074\u00b9K (K)",
      "\u2076\u00b3Cu",
      "\u2076\u2075Cu (Cu)",
      "\u2076\u2074Zn",
      "\u2076\u2076Zn (Zn) \u2014 the three delta values are defined from the \u2074\u00b9K/\u00b3\u2079K",
      "\u2076\u2075Cu/\u2076\u00b3Cu and \u2076\u2076Zn/\u2076\u2074Zn ratios (p.7)"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b441K, \u03b465Cu and \u03b466Zn in permil, each defined explicitly against its bracketing standard"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 AG1-X8 200\u2013400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:finalSolutionMatrix": "200 ppb for K and Zn; 100 ppb for Cu",
  "ada:uncertaintyLevel": "2 s.d.",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
  "ada:secondaryReferenceMaterialDefault": [
    "BHVO-2"
  ],
  "ada:primaryStandardNameDefault": "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
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
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionDurationDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionTemperatureDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/digestionVesselType> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "1: concentrated HF and HNO3 in a 3:1 ratio, closed beaker, 170 deg C, 48 h | 2: fluxing in concentrated HNO3 and HCl, with 1 ml H2O2 added slowly during the HNO3 flux to remove organics. The 5 ml 0.5 M HNO3 is the uptake, not a step." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "\"concentrated HF and HNO3 in a 3:1 ratio\", followed by fluxing in concentrated HNO3 and HCl with 1 ml H2O2 added to remove organics; brought up in 5 ml 0.5 M HNO3" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/desolvationSystem>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | WUSTL (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "Standard-sample bracketing for all analyses; BHVO-2 \"analysed alongside all sample analyses\"" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "³⁹K",
                "⁴¹K (K)",
                "⁶³Cu",
                "⁶⁴Zn",
                "⁶⁵Cu (Cu)",
                "⁶⁵Cu/⁶³Cu and ⁶⁶Zn/⁶⁴Zn ratios (p.7)",
                "⁶⁶Zn (Zn) — the three delta values are defined from the ⁴¹K/³⁹K" ] ;
    ada:chromatographicSeparationApplied "Yes — AG1-X8 200–400 mesh anion resin, 5 ml 1.5 M HBr to elute the matrix and 3 ml 0.5 M HNO3 to elute Zn" ;
    ada:finalSolutionMatrix "200 ppb for K and Zn; 100 ppb for Cu" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "\"To correct for instrument mass bias, the sample–standard bracketing technique was used for all analyses\"" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST-SRM 3141a, NIST-SRM 976, JMC-Lyon" ;
    ada:reportedProperties "δ41K, δ65Cu and δ66Zn in permil, each defined explicitly against its bracketing standard" ;
    ada:samplingUnit "Split of a single digest — \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"" ;
    ada:secondaryReferenceMaterialDefault "BHVO-2" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "2 s.d." ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "High-mass-resolution slit for K; low-mass-resolution slit for Cu and Zn" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "Dry plasma for K — \"all K isotope analyses were undertaken using a 'dry plasma' technique with the Elemental Scientific APEX Ω high-sensitivity desolvation system\"; wet plasma for Cu and Zn via a quartz glass dual cyclonic spray chamber" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> ;
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium mass resolution, R ≈ 6,600–7,000 (R = m/m0.95 − m0.05)"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
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
          "schema:description": "Two cup configurations: (1) ⁴⁶Ti–⁵⁰Ti and ⁴⁴Ca; (2) ⁴⁹Ti, ⁵⁰Ti, ⁵¹V, ⁵²Cr, ⁵³Cr — \"Titanium isotopes were collected in two cup configurations\" (p.8). Cup positions are not stated",
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
      "schema:defaultValue": 40,
      "schema:description": "40 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.39,
      "schema:description": "8.39 s for the first cup configuration and 4.19 s for the second — \"A sample measurement consisted of 40 cycles with 8.39 s integration time for the first configuration and 4.19 s for the second\" (p.8). The 4 s in the same paper is the LLNL procedure's (p.8), not this one"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — no double spike used"
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
            "schema:value": "N/A — no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A — no double spike used"
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
        "schema:description": "Coordinated dissolution shared with the WUSTL split - see the WUSTL column.",
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
  "ada:massBiasCorrectionStrategy": "Internal normalization to 49Ti/47Ti = 0.749766 using the exponential law, plus bracketing against an in-house Alfa Aesar Ti wire standard — \"the isotope data were normalized to a 49Ti/47Ti ratio of 0.749766 (ref. 72), using the exponential law\"; results reported \"applying the sample–standard bracketing method\" (p.8)",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "⁴⁶Ti",
      "⁴⁷Ti",
      "⁴⁸Ti",
      "⁴⁹Ti",
      "⁵⁰Ti (Ti)",
      "⁴⁴Ca",
      "⁵¹V",
      "⁵²Cr",
      "⁵³Cr (interference monitors, no target species) — \"Titanium isotopes were collected in two cup configurations. First",
      "all five Ti isotopes and 44Ca were measured enabling correction of the Ca interference on 46Ti and 48Ti. The second configuration included 49Ti",
      "50Ti",
      "51V",
      "52Cr and 53Cr to correct for isobaric interferences from V and Cr on 50Ti\" (p.8). ⁴⁵Sc belongs to the LLNL procedure in the same paper",
      "not this one"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "ε46Ti, ε48Ti and ε50Ti (parts per 10^4) relative to an in-house Alfa Aesar Ti wire standard, εiTi = [(iTi/47Ti)sample/(iTi/47Ti)standard − 1] × 10^4, \"where i refers to the isotope masses 46Ti, 48Ti and 50Ti\" (p.8)"
  ],
  "ada:chromatographicSeparationApplied": "Yes — three-step anion exchange chromatography; yields 75–100%",
  "ada:isotopeDilutionSpike": "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:uncertaintyLevel": "2 s.d.",
  "ada:internalStandardElement": "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
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
  "schema:description": "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv).",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Medium mass resolution, R \u2248 6,600\u20137,000 (R = m/m0.95 \u2212 m0.05)"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
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
          "schema:description": "Two cup configurations: (1) \u2074\u2076Ti\u2013\u2075\u2070Ti and \u2074\u2074Ca; (2) \u2074\u2079Ti, \u2075\u2070Ti, \u2075\u00b9V, \u2075\u00b2Cr, \u2075\u00b3Cr \u2014 \"Titanium isotopes were collected in two cup configurations\" (p.8). Cup positions are not stated",
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
      "schema:defaultValue": 40,
      "schema:description": "40 cycles"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/integrationTimePerCycleDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "integrationTimePerCycleDefault",
      "schema:name": "Integration Time per Cycle",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8.39,
      "schema:description": "8.39 s for the first cup configuration and 4.19 s for the second \u2014 \"A sample measurement consisted of 40 cycles with 8.39 s integration time for the first configuration and 4.19 s for the second\" (p.8). The 4 s in the same paper is the LLNL procedure's (p.8), not this one"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeIsotopePair",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeIsotopePair",
      "schema:name": "Double Spike Isotope Pair",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/module/MCICPMS/doubleSpikeMixingRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "doubleSpikeMixingRatioDefault",
      "schema:name": "Double Spike Mixing Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 no double spike used"
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
            "schema:value": "N/A \u2014 no isotope dilution applied"
          },
          {
            "@id": "ada:parameter/module/MCICPMS/doubleSpikeInversionAlgorithm",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "doubleSpikeInversionAlgorithm",
            "schema:name": "Double-Spike Inversion Algorithm",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:value": "N/A \u2014 no double spike used"
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
        "schema:description": "Coordinated dissolution shared with the WUSTL split - see the WUSTL column.",
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
  "ada:massBiasCorrectionStrategy": "Internal normalization to 49Ti/47Ti = 0.749766 using the exponential law, plus bracketing against an in-house Alfa Aesar Ti wire standard \u2014 \"the isotope data were normalized to a 49Ti/47Ti ratio of 0.749766 (ref. 72), using the exponential law\"; results reported \"applying the sample\u2013standard bracketing method\" (p.8)",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "\u2074\u2076Ti",
      "\u2074\u2077Ti",
      "\u2074\u2078Ti",
      "\u2074\u2079Ti",
      "\u2075\u2070Ti (Ti)",
      "\u2074\u2074Ca",
      "\u2075\u00b9V",
      "\u2075\u00b2Cr",
      "\u2075\u00b3Cr (interference monitors, no target species) \u2014 \"Titanium isotopes were collected in two cup configurations. First",
      "all five Ti isotopes and 44Ca were measured enabling correction of the Ca interference on 46Ti and 48Ti. The second configuration included 49Ti",
      "50Ti",
      "51V",
      "52Cr and 53Cr to correct for isobaric interferences from V and Cr on 50Ti\" (p.8). \u2074\u2075Sc belongs to the LLNL procedure in the same paper",
      "not this one"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
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
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
  "ada:reportedProperties": [
    "\u03b546Ti, \u03b548Ti and \u03b550Ti (parts per 10^4) relative to an in-house Alfa Aesar Ti wire standard, \u03b5iTi = [(iTi/47Ti)sample/(iTi/47Ti)standard \u2212 1] \u00d7 10^4, \"where i refers to the isotope masses 46Ti, 48Ti and 50Ti\" (p.8)"
  ],
  "ada:chromatographicSeparationApplied": "Yes \u2014 three-step anion exchange chromatography; yields 75\u2013100%",
  "ada:isotopeDilutionSpike": "N/A \u2014 no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization",
  "ada:uncertaintyLevel": "2 s.d.",
  "ada:internalStandardElement": "N/A \u2014 mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element",
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
  "ada:internalNormalizationElementAndIsotopeRatio": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:primaryStandardNameDefault": "missing",
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Coordinated dissolution shared with the WUSTL split - see the WUSTL column." ;
                    schema1:name "Sample digestion" ;
                    schema1:position 4 ;
                    bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Coordinated dissolution shared with the WUSTL split — see the WUSTL column" ] ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod>,
                        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault>,
        <https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SolutionIntroduction/internalStandardConcentration> ;
    schema1:datePublished "missing" ;
    schema1:description "solutionMcicpmsTAPP instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich (publication column of Solution_MC-ICP-MS_TAPP_v79.csv)." ;
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
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyticalMode "Solution nebulisation (continuous)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> ;
            ada:defaultChannels "50Ti",
                "51V",
                "52Cr and 53Cr to correct for isobaric interferences from V and Cr on 50Ti\" (p.8). ⁴⁵Sc belongs to the LLNL procedure in the same paper",
                "all five Ti isotopes and 44Ca were measured enabling correction of the Ca interference on 46Ti and 48Ti. The second configuration included 49Ti",
                "not this one",
                "⁴⁴Ca",
                "⁴⁶Ti",
                "⁴⁷Ti",
                "⁴⁸Ti",
                "⁴⁹Ti",
                "⁵²Cr",
                "⁵³Cr (interference monitors, no target species) — \"Titanium isotopes were collected in two cup configurations. First",
                "⁵¹V",
                "⁵⁰Ti (Ti)" ] ;
    ada:chromatographicSeparationApplied "Yes — three-step anion exchange chromatography; yields 75–100%" ;
    ada:finalSolutionMatrix "missing" ;
    ada:internalNormalizationElementAndIsotopeRatio "missing" ;
    ada:internalStandardElement "N/A — mass bias corrected by standard-sample bracketing, internal normalization or a double spike rather than by an added internal standard element" ;
    ada:isotopeDilutionSpike "N/A — no isotope dilution spike; mass bias handled by standard-sample bracketing or internal normalization" ;
    ada:massBiasCorrectionStrategy "Internal normalization to 49Ti/47Ti = 0.749766 using the exponential law, plus bracketing against an in-house Alfa Aesar Ti wire standard — \"the isotope data were normalized to a 49Ti/47Ti ratio of 0.749766 (ref. 72), using the exponential law\"; results reported \"applying the sample–standard bracketing method\" (p.8)" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:reportedProperties "ε46Ti, ε48Ti and ε50Ti (parts per 10^4) relative to an in-house Alfa Aesar Ti wire standard, εiTi = [(iTi/47Ti)sample/(iTi/47Ti)standard − 1] × 10^4, \"where i refers to the isotope masses 46Ti, 48Ti and 50Ti\" (p.8)" ;
    ada:samplingUnit "A 5.2 mg aliquot of Bennu aggregate" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:uncertaintyLevel "2 s.d." ;
    ada:washTimeBetweenSamples -9999 .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/isotopeDilutionDataReductionMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Isotope Dilution Data Reduction Method" ;
    schema1:value "N/A — no isotope dilution applied" ;
    schema1:valueName "isotopeDilutionDataReductionMethod" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution Setting" ;
    schema1:value "Medium mass resolution, R ≈ 6,600–7,000 (R = m/m0.95 − m0.05)" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeInversionAlgorithm> a schema1:PropertyValueSpecification ;
    schema1:name "Double-Spike Inversion Algorithm" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeInversionAlgorithm" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeIsotopePair> a schema1:PropertyValueSpecification ;
    schema1:name "Double Spike Isotope Pair" ;
    schema1:value "N/A — no double spike used" ;
    schema1:valueName "doubleSpikeIsotopePair" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/doubleSpikeMixingRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — no double spike used" ;
    schema1:name "Double Spike Mixing Ratio" ;
    schema1:valueName "doubleSpikeMixingRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/integrationTimePerCycleDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.39e+00 ;
    schema1:description "8.39 s for the first cup configuration and 4.19 s for the second — \"A sample measurement consisted of 40 cycles with 8.39 s integration time for the first configuration and 4.19 s for the second\" (p.8). The 4 s in the same paper is the LLNL procedure's (p.8), not this one" ;
    schema1:name "Integration Time per Cycle" ;
    schema1:valueName "integrationTimePerCycleDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/MCICPMS/numberOfCyclesPerBlockDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 40 ;
    schema1:description "40 cycles" ;
    schema1:name "Number of Cycles per Block" ;
    schema1:valueName "numberOfCyclesPerBlockDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Multi-collector sector-field ICP-MS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collector>,
        <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Sample-Introduction-System>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Neptune Plus" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collector" ;
    schema1:description "Two cup configurations: (1) ⁴⁶Ti–⁵⁰Ti and ⁴⁴Ca; (2) ⁴⁹Ti, ⁵⁰Ti, ⁵¹V, ⁵²Cr, ⁵³Cr — \"Titanium isotopes were collected in two cup configurations\" (p.8). Cup positions are not stated" ;
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


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution MC-ICP-MS Technique-Aligned Procedure Profile (solutionMcicpmsTAPP)
description: Solution multi-collector ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/Solution_MC-ICP-MS_TAPP_v79.csv via the path-driven
  pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/ProcedureIdentification
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
                              this procedure is designed to analyse.
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupGainCalibrationMethod
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeInversionAlgorithm
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
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
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupGainCalibrationMethod
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_peakFlatnessMethodAndThreshold
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeInversionAlgorithm
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_icpTuning
                  - title: Doubly-Charged Species Monitor
                    description: "The mass ratio monitored to estimate doubly-charged
                      ion (M\xB2\u207A) formation during instrument tuning. The monitor
                      species and the mass positions monitored should be stated explicitly.
                      Analogous to Oxide Production Method and Threshold for oxide
                      monitoring."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
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
                        const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupArrayConfiguration
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupAmplifierResistorValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupArrayConfiguration
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_faradayCupAmplifierResistorValues
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
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Collector
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_integrationTimePerCycle
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeIsotopePair
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_doubleSpikeMixingRatio
        - title: Error Correlation Between Reported Quantities
          description: The correlation coefficient between pairs of reported quantities
            whose uncertainties are not independent, together with the pair it applies
            to and how it was obtained.
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        - title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/solutionMcicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/reactionProductIonMassShiftTransition
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfBlocksPerMeasurement
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_numberOfCyclesPerBlock
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_integrationTimePerCycle
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_baselineMeasurementApproach
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Procedure_massFractionationLaw
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
          title: Error Correlation Between Reported Quantities
          description: The correlation coefficient between pairs of reported quantities
            whose uncertainties are not independent, together with the pair it applies
            to and how it was obtained.
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
              const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/solutionMcicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/reactionProductIonMassShiftTransition
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
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/countingStatisticsError
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/countingStatisticsError
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
                  const: ada:analyteColumn/solutionMcicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
    ada:channelTemplate:
      type: object
      properties:
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
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
            - title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment
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
              title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/spectralInterferenceCorrectionsApplied
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
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
          - contains:
              title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/solutionMcicpmsTAPP/massResolutionAssignment
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
        ada:defaultChannels:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
      required:
      - ada:defaultChannels
    ada:massBiasCorrectionStrategy:
      description: 'Primary strategy used to correct for instrumental isotopic mass
        fractionation. Four main strategies: (1) Sample-standard bracketing (SSB):
        alternating sample and isotopic standard measurements; bias interpolated linearly
        between bracketing measurements. (2) Double-spike: a mixture of two enriched
        isotopes of the target species element added before digestion provides an
        internal monitor of both instrumental and chemical mass fractionation. (3)
        Internal normalization: an element of known isotopic composition added to
        samples and standards; measured ratio of normalizing element used to calculate
        the mass bias factor applied to target species ratios. (4) SSB + internal
        normalization: both strategies applied simultaneously for redundant bias correction.'
      type: string
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
  - ada:massBiasCorrectionStrategy
  - ada:numberOfAcquisitionPasses

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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp/context.jsonld)

## Sources

* [Solution_MC-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-MC-ICPMS/tapp`

